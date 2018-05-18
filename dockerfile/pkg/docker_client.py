# -*- coding: utf-8 -*-
"""Docker wrapper."""

import os
import docker
import retrying

from pkg import output
from pkg.validation import validate

__EXIT_CODE_ERROR_MESSAGE = "Container exited with non-zero exit code: {}"
__EXIT_CODE_ERROR_MESSAGE += ", image: {}, command: {}"
__EXIT_CODE_ERROR_MESSAGE += os.linesep + "stderr: {}"

__DEBUG_MESSAGE_STARTING = (
    "Starting container, image: {}"
    ", command: {}, options: {}"
)
__DEBUG_MESSAGE_FINISHED = "Container finished, stdout: {}"


def __get_client():
    """Get docker client from sock."""
    return docker.from_env()


def _not_keyboard_interrupt(exception):
    """Return True if exception is not KeyboardInterrupt exception."""
    return not isinstance(exception, KeyboardInterrupt)


@retrying.retry(
    retry_on_exception=_not_keyboard_interrupt,
    wait_random_min=1000,
    wait_random_max=2000,
    stop_max_attempt_number=10)
def run_container(
        image_name,
        command="",
        wait=True,
        expected_exit_codes=[0],
        **kwargs):
    """Run container with specified settings."""
    output.debug(__DEBUG_MESSAGE_STARTING.format(
        image_name,
        command,
        kwargs))
    container = __get_client().containers.run(
        image_name,
        command,
        detach=True,
        **kwargs)
    if wait:
        exit_code = container.wait()
        validate(
            exit_code in expected_exit_codes,
            __EXIT_CODE_ERROR_MESSAGE.format(
                exit_code,
                image_name,
                command,
                container.logs(stdout=False, stderr=True)))
        container_logs = container.logs(stdout=True, stderr=False)
        container_output = container_logs.decode("utf-8")
        output.debug(__DEBUG_MESSAGE_FINISHED.format(container_output))
        container.remove()
        return container_output


def remove_container(name):
    """Remove container."""
    __get_client().containers.get(name).remove(force=True)


def create_network(network_name):
    """Create bridge network."""
    __get_client().networks.create(network_name, driver="bridge")


def remove_network(network_name):
    """Remove network."""
    __get_client().networks.get(network_name).remove()

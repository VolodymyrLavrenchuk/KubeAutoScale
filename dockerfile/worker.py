# -*- coding: utf-8 -*-
import json
from os import environ as env
from time import sleep
from pkg import docker_client, output
from azure.mgmt.containerservice import ContainerServiceClient
from azure.common.credentials import ServicePrincipalCredentials

while True:
  output.log("Waiting for command...")
  azure_json=json.load(open('/etc/kubernetes/azure.json'))
  aadClientId=azure_json["aadClientId"]
  aadClientSecret=azure_json["aadClientSecret"]
  tenantId=azure_json["tenantId"]
  subscriptionId=azure_json["subscriptionId"]
  rg=azure_json["resourceGroup"]

  credentials = ServicePrincipalCredentials(
        client_id=aadClientId,
        secret=aadClientSecret,
        tenant=tenantId)

  container_client=ContainerServiceClient(credentials,subscriptionId)
  #print(dir(container_client.config))
  #print(container_client.config)
#  print(dir(container_client.container_services))
#  for item in container_client.container_services.list():
#    print(item)
  cs=container_client.container_services.get("rg-dmp-k8s-dmpcluster-dev-westus2","dmpcluster")
  print(dir(cs))
  sleep(int(env['SLEEP_INTERVAL']))
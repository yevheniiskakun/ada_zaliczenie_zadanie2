from django.shortcuts import render
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient
from azure.storage.blob.aio import ContainerClient


def get_AzureKV_secret(secret_name):  # storagecredentials, cosmos-readwrite-key, cosmos-endpoint
    KVUri = f"https://zadanie2adayevheniis.vault.azure.net"
    credential = DefaultAzureCredential()
    client = SecretClient(vault_url=KVUri, credential=credential)

    return (client.get_secret(secret_name)).value


def list_blobs_flat(blob_service_client: BlobServiceClient, container_name):
    container_client = blob_service_client.get_container_client(container=container_name)

    blob_list = container_client.list_blobs()

    return blob_list


def create_CDN_URLs():

    endpoint_hostname = "https://cdnmediayevheniiskakun.azureedge.net";
    storage_connectionstring = get_AzureKV_secret("storagecredentials")

    blob_service_client = BlobServiceClient.from_connection_string(storage_connectionstring, logging_enable=True)

    blob_list = list_blobs_flat(blob_service_client, "media")

    CDN_URLs_list = []
    for blob in blob_list:
        CDN_URLs_list.append(endpoint_hostname + "/" + blob.name)
        #print(endpoint_hostname + "/" + blob.name)

    return CDN_URLs_list


def index(request):
    CDN_URLs_list = create_CDN_URLs()
    context = {"CDN_URLs_list": CDN_URLs_list}


    return render(request, 'pages/index.html', context)

import os

from django.core.serializers import json
from django.shortcuts import render
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient
from azure.storage.blob.aio import ContainerClient
from azure.cosmos import CosmosClient
import socket
from datetime import datetime
import uuid
from .forms import ImageForm


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

def send_logs_CosmosDB(event, description = ""):
    endpoint = get_AzureKV_secret("cosmos-endpoint")
    #print(endpoint)
    credential = get_AzureKV_secret("cosmos-readwrite-key")
    #print(credential)
    client = CosmosClient(url=endpoint, credential=credential)
    database = client.get_database_client("media")
    #print(database)
    container = database.get_container_client("media")
    #print(container)

    hostname = socket.gethostname()
    description = f"User with IP: {socket.gethostbyname(hostname)} activity: {event} at {str(datetime.now())}"
    #print(description)
    id = str(uuid.uuid4())
    container.create_item({
        "id": id,
        "event": event,
        "description": description,
    })


def upload_Blob_StorageAccount(file):
    file_upload_name = str(uuid.uuid4()) + file.name
    blob_service_client = BlobServiceClient.from_connection_string(get_AzureKV_secret("storagecredentials"), logging_enable=True)
    container_client = blob_service_client.get_container_client(container="media")
    container_client.upload_blob(name = file_upload_name, data = file.read(), overwrite=True)

    send_logs_CosmosDB(f"blob with name: {file_upload_name} was uploaded")


def index(request):
    CDN_URLs_list = create_CDN_URLs()
    if request.POST:
        new_image_form = ImageForm(request.POST, request.FILES)
        print(new_image_form.is_valid())
        print(request.FILES)
        if new_image_form.is_valid():
            upload_Blob_StorageAccount(request.FILES["image"])
            print("request.FILES" + (request.FILES["image"]).name)
    new_image_form = ImageForm()
    context = {"CDN_URLs_list": CDN_URLs_list, "new_image_form": new_image_form}
    send_logs_CosmosDB("page was loaded")
    return render(request, 'pages/index.html', context)

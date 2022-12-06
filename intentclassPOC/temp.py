from azure.storage.blob import BlobClient

class AzureBlobStorage:
    def __init__(self, connection_string):
        self.connection_string = connection_string

    def upload_file(self, container_name, file_name, file):
        blob_client = BlobClient.from_connection_string(self.connection_string, container_name, file_name)
        blob_client.upload_blob(file)

    def download_file(self, container_name, file_name):
        blob_client = BlobClient.from_connection_string(self.connection_string, container_name, file_name)
        return blob_client.download_blob().readall()

    def delete_file(self, container_name, file_name):
        blob_client = BlobClient.from_connection_string(self.connection_string, container_name, file_name)
        blob_client.delete_blob()

    def list_files(self, container_name):
        blob_client = BlobClient.from_connection_string(self.connection_string, container_name)
        return blob_client.list_blobs()


AzureBlobStorage.upload_file('mycontainer', 'myblob', 'myblob.txt')


# blob = BlobClient(account_url="https://hrsadatastore.blob.core.windows.net",
#                   container_name="sfdcdata",
#                   blob_name="report1653576473320.csv",
#                   credential="kkGf4Dhza+3QXRuMe0XCRGxUkoe2Qo+j0LMcpdoKYcax4GrWyJyZJOFYi2YK+dYdO7Pg9/bCAVei+AStAjNrSg==")

# with open("report1653576473320.csv", "wb") as f:
#     data = blob.download_blob()
#     data.readinto(f)

# print(data)



	
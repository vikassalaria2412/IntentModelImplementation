from azure.storage.blob import BlobClient
import pandas as pd
import os
import logging
import sys
import numpy as np
class AzureBlobStorage:
    # def __init__(self,account_url,container_name,blob_name,credential,blob_path,connection_string):
    #     self.account_url = account_url
    #     self.container_name = container_name
    #     self.blob_name = blob_name
    #     self.credential = credential
    #     self.blob_path = blob_path
    #     self.connection_string = connection_string

    def __init__(self,blob_path,connection_string):
        self.blob_path = blob_path
        self.connection_string = connection_string

    

    # def blob_connect(self):
    #     blob_client = BlobClient(account_url=self.account_url,container_name=self.container_name,blob_name=self.blob_name,credential=self.credential)
    #     return blob_client

    
    # def blob_load(self):
    #     blob_client = self.blob_connect()
    #     blob_client.get_blob_to_text()
    #     blob_data = blob_client.download_blob()
    #     return blob_data

    def read_csv(self,blob_path,connection_string):
        mydata = pd.read_csv(
        f"abfs://{blob_path}",
        storage_options={
            "connection_string": os.environ[connection_string] 
    })
        return mydata





    blob = BlobClient(account_url="https://hrsadatastore.blob.core.windows.net",
                  container_name="sfdcdata",
                  blob_name="report1653576473320.csv",
                  credential="kkGf4Dhza+3QXRuMe0XCRGxUkoe2Qo+j0LMcpdoKYcax4GrWyJyZJOFYi2YK+dYdO7Pg9/bCAVei+AStAjNrSg==")

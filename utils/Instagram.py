from pathlib import Path
from instagrapi import Client




class Instagram:
    def __init__(self,username,password) -> None:
        self.client = Client()
        self.client.login(username,password)
    
    def postUpload(self,path,caption):
        self.client.photo_upload(Path(path),caption)
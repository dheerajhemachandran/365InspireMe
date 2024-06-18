from pathlib import Path
from instagrapi import Client




class Instagram:
    def __init__(self,username,password) -> None:
        self.client = Client()
        self.client.login(username,password)
    
    def postUpload(self,path,caption):
        self.client.photo_upload(Path(path),caption)

    def search_posts(self, hashtag, count=1):
        hashtag_info = self.client.hashtag_info(hashtag)
        posts = self.client.hashtag_medias_top(hashtag_info.name, amount=count)
        return posts

    def get_likers(self, media_id, count=10):
        likers = self.client.media_likers(media_id)
        return likers[:count]
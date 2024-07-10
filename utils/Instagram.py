from pathlib import Path
from instagrapi import Client




class Instagram:
    def __init__(self,username,password) -> None:
        self.client = Client()
        self.client.login(username,password)
    
    def postUpload(self,path,caption):
        self.client.photo_upload(Path(path),caption)

    def search_posts(self, hashtag, count=20):
        posts = self.client.hashtag_medias_recent(hashtag, amount=count)
        return posts
    
    def save_post(self,media_id):
        self.client.media_save(media_id)

    def get_likers(self, media_id, count=1):
        likers = self.client.media_likers(media_id)
        return likers[0]
    
    def like_and_comment(self,media_id,comment):
        self.client.media_like(media_id)
        self.client.media_comment(media_id,comment)

    def follow_user(self,username):
        user_id = self.client.user_id_from_username(username)
        print(user_id)
        self.client.user_follow(user_id)
        pass

    def unfollow_all_user(self,exclude_usernames):
        following_users=self.client.user_following(self.client.user_id,amount=0)
        print(following_users.keys())
        exclude_user_ids = set(self.client.user_id_from_username(username) for username in exclude_usernames)
        print(exclude_user_ids)
        for user_id in following_users.keys():
            if user_id not in exclude_user_ids:
                self.client.user_unfollow(user_id)
            # print(user_id)

    def logout(self):
        self.client.logout()

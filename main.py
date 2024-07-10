from utils.Image import Post
from utils.Quotes import Quotes
from utils.Instagram import Instagram
from dotenv import load_dotenv
import os


load_dotenv()

username=os.getenv('INSTA_USERNAME')
password=os.getenv('INSTA_PASSWORD')
instagram=Instagram(username,password)

# generate quote 
quotes=Quotes()
response=quotes.get_quotes()
content=response['content']
author=response['author']
caption=f"""
    {content}.

        - {author}

    #thoughtoftheday #quotes #aesthetic #lifequotes #Motivation #Inspiration #Quotes #PositiveVibes #LifeLessons #Mindset #Wisdom #DailyQuotes #SelfImprovement #MotivationalQuotes #fyp
    """

# generate post and upload
image = Post()
target=image.createImage(text=content)
# instagram.postUpload(target,caption)

# unfollowing users 
# exclude_usernames=['innerstrenght_','yours_dheeraj.07','sujana.zip']
# instagram.unfollow_all_user(exclude_usernames)


# following new 10 users 
# for i in instagram.search_posts(hashtag="quotes",count=10):
#     media_id=(i.pk)
#     comment='This is amazing! Check out my profile for more content like this! ✨'
#     instagram.like_and_comment(media_id,comment)
#     instagram.save_post(media_id)
#     username=instagram.get_likers(media_id).username
#     instagram.follow_user(username)

# logout
instagram.logout()
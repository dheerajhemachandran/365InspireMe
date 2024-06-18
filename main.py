from utils.Image import Post
from utils.Quotes import Quotes
from utils.Instagram import Instagram
from dotenv import load_dotenv
import os

load_dotenv()

username=os.getenv('INSTA_USERNAME')
password=os.getenv('INSTA_PASSWORD')

instagram=Instagram(username,password)

i=0
while (i<3):
    quotes=Quotes()
    response=quotes.get_quotes()
    content=response['content']
    author=response['author']

    caption=f"""
    {content}.

        - {author}

    #thoughtoftheday #quotes #aesthetic #lifequotes
    """

    image = Post()
    target=image.createImage(text=content)
    instagram.postUpload(target,caption)
    i+=1
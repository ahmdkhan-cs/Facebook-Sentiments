import facebook as fb
from .facebook_credentials import Credentials

class FetchData():

    def __init__(self):
        self.cred = Credentials()
        self.graph = fb.GraphAPI(self.cred.get_token())

    def fetch_all_posts(self, pageid):
        try:
            posts = self.graph.get_object(pageid, fields='posts{comments, picture, message, id}')['posts']['data']
        except:
            posts = []
        return posts

    def fetch_one_post(self, postid):
        post = self.graph.get_object(postid, fields='comments, picture, message')
        return post
        


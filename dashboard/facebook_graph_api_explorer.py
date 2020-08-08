import facebook as fb
from .facebook_credentials import Credentials

class FetchData():

    def __init__(self):
        self.cred = Credentials()
        self.graph = fb.GraphAPI(self.cred.get_token())


    def fetch_page_data(self, pageid):
        try:
            page_data = self.graph.get_object(pageid, fields='picture, name')
        except:
            page_data = {}
        
        return page_data

    def fetch_all_posts(self, pageid):
        try:
            posts = self.graph.get_object(pageid, fields='posts{comments, picture, message, id}')['posts']['data']
        except:
            posts = []
        return posts

    def fetch_one_post(self, postid):
        try:
            post = self.graph.get_object(postid, fields='comments, picture, message')
        except:
            post = {}
        return post
        


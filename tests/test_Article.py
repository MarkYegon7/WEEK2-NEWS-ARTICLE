import unittest
from app.models import Article

class   ArticleTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Article class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article= Article("Edmund Ingham","Moderna management is now talking about a private COVID vaccine market and hoping for government funds for a fall booster jab Read more on MRNA stock here.","2022-05-05T19:30:35Z", "https://seekingalpha.com/article/4507459-moderna-blowout-quarterly-earnings-wont-last-forever","https://static.seekingalpha.com/cdn/s3/uploads/getty_images/1181987981/image_1181987981.jpg?io=getty-c-w750","Moderna: Blowout Quarterly Earnings Won't Last Forever - But Q1 2022 Was Certainly One")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))
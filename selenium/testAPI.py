import logging
import requests
import yaml

with open('testdata.yaml', encoding='utf-8') as f:
    testdata = yaml.safe_load(f)


class APIHelper:
    def __init__(self):
        self.base_url = testdata['url']

    def create_post_api(self, token):
        try:
            requests.post(url=self.base_url + testdata['post'],
                          headers={'X-Auth-Token': token},
                          params={"title": testdata['title'],
                                  'description': testdata['description'],
                                  'content': testdata['content']})
            return True
        except:
            logging.exception('Exception with create post')
            return False

    def get_my_post(self, token):
        try:
            get_result = requests.get(url=self.base_url + testdata['post'],
                                   headers={'X-Auth-Token': token},
                                   params={'owner': 'Me'})
            return get_result
        except:
            logging.exception('Exception with request post')
            return None


    def get_not_my_posts(self, token):
        try:
            get_result = requests.get(url=self.base_url + testdata['post'],
                                      headers={'X-Auth-Token': token},
                                      params={'owner': 'notMe',
                                           'sort': 'createdAt',
                                           'order': 'ASC'})
            return get_result
        except:
            logging.exception('Exception with tittle list from another users')
            return None

    def check_title(self, result):
        try:
            title_list = [txt['title'] for txt in result.json()['data']]
            return title_list
        except:
            logging.exception('Exception with title list')
            return None


    def check_description(self, result):
        try:
            description_list = [txt['description'] for txt
                                in result.json()['data']]
            return description_list
        except:
            logging.exception('Exception with description list')
            return None

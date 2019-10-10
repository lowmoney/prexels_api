import requests

class prexels:
    # usefull constants
    URL = "https://api.pexels.com/v1/search?query="
    PER_PAGE = "&per_page="
    PAGE = "&page="

    # to call
    ids = []
    widths = []
    heights = []
    urls = []
    photographers = []
    photographer_urls = []
    photographer_ids = []
    originals = []
    extra_larges = []
    larges = []
    mediums = []
    smalls = []
    potraits = []
    landscapes = []
    tinys = []

    def __init__(self,API=None):
        if API is not None:
            self.API = API
        else:
            raise Exception('No API key!')
    
    def search(self,search=None,page=1,per_page=1):
        if search is not None:
            self.URL = self.URL + search.replace(" ","+") + self.PER_PAGE + per_page + self.PAGE + page
            r = requests.get(URL, headers = {"Authorization":self.API})

            if r.status_code == 200:
                images(r.text.json()['photos'])
            if r.status_code == 401:
                raise Exception('401 received, invalid API key was given')
            if r.status_code == 503:
                raise Exception('503 received, server not available')
            else:
                raise Exception('Something went wrong on the server side')

        else:
            raise Exception('Search argument not given')

    def images(self,json_body):
        for photo in json_body:
            try:
                self.ids.insert(photo['id'])
                self.widths.insert(photo['width'])
                self.heights.insert(photo['height'])
                self.urls.insert(photo['url'])
                self.photographers.insert(photo['photographer'])
                self.photographer_urls.insert(photo['photographer_url'])
                self.photographer_ids.insert(photo['photographer_id'])
                self.originals.insert(photo['original'])
                self.extra_larges.insert(photo['extra_large'])
                self.larges.insert(photo['large'])
                self.mediums.insert(photo['medium'])
                self.smalls.insert(photo['small'])
                self.potraits.insert(photo['potrait'])
                self.landscapes.insert(photo['landscape'])
                self.tinys.insert(photo['tiny'])
            except:
                pass
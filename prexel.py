import requests
import os
from PIL import Image

class prexels:
    # usefull constants
    URL = "https://api.pexels.com/v1/search?query="
    PER_PAGE = "&per_page="
    PAGE = "&page="

    VIDEOURL = "https://api.pexels.com/videos/search?query="
    VIDEO_PER_PAGE = "&per_page="
    VIDEO_PAGE = "&page="

    # image
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

    # Will come back later
    # # video
    # video_ids = []
    # video_widths = []
    # video_heights = []
    # video_urls = []
    # video_photographers = []
    # video_photographer_urls = []
    # video_photographer_ids = []
    # video_originals = []
    # video_extra_larges = []
    # video_larges = []
    # video_mediums = []
    # video_smalls = []
    # video_potraits = []
    # video_landscapes = []
    # video_tinys = []

    def __init__(self,API=None):
        if API is not None:
            self.API = API
            self.URL = "https://api.pexels.com/v1/search?query="
            self.PER_PAGE = "&per_page="
            self.PAGE = "&page="
        else:
            raise Exception('No API key!')
    
    # Search for the picture
    def search_images(self,search=None,page=1,per_page=1):
        if search is not None:
            search_url = self.URL + search.replace(" ","+") + self.PER_PAGE + str(per_page) + self.PAGE + str(page)
            r = requests.get(search_url, headers = {"Authorization":self.API})
            self.images(r.json()['photos'])
            # if r.status_code == 200:
            #     self.images(r.json()['photos'])
            # if r.status_code == 401:
            #     raise Exception('401 received, invalid API key was given')
            # if r.status_code == 503:
            #     raise Exception('503 received, server not available')
            # else:
            #     raise Exception(str(r.status_code) + ' Something went wrong on the server side')

        else:
            # Search must be given
            raise Exception('Search argument not given')

    def images(self,json_body):
        # Add all the attrs to the lists
        for photo in json_body:
            try:
                print(photo['id'])
                prexels.ids.insert(photo['id'])
                prexels.widths.insert(photo['width'])
                self.heights.insert(photo['height'])
                self.urls.insert(photo['url'])
                self.photographers.insert(photo['photographer'])
                self.photographer_urls.insert(photo['photographer_url'])
                self.photographer_ids.insert(photo['photographer_id'])
                self.originals.insert(photo['src']['original'])
                self.extra_larges.insert(photo['src']['extra_large'])
                self.larges.insert(photo['src']['large'])
                self.mediums.insert(photo['src']['medium'])
                self.smalls.insert(photo['src']['small'])
                self.potraits.insert(photo['src']['potrait'])
                self.landscapes.insert(photo['src']['landscape'])
                self.tinys.insert(photo['src']['tiny'])
            except:
                pass
    
    # def search_videos(self,search=None,page=1,per_page=1):
    #     if search is not None:
    #         self.URL = self.VIDEOURL + search.replace(" ","+") + self.VIDEO_PER_PAGE + per_page + self.VIDEO_PAGE + page
    #         r = requests.get(URL, headers = {"Authorization":self.API})

    #         if r.status_code == 200:
    #             images(r.json()['photos'])
    #         if r.status_code == 401:
    #             raise Exception('401 received, invalid API key was given')
    #         if r.status_code == 503:
    #             raise Exception('503 received, server not available')
    #         else:
    #             raise Exception('Something went wrong on the server side')

    #     else:
    #         # Search must be given
    #         raise Exception('Search argument not given')

    def download_images(self,size = "tinys",location=None):
        if location is not None:
            if size == "tinys":
                count = 0
                for tiny in tinys:
                    try:
                        img = Image.open(requests.get(tiny,timeout=5,stream=True).raw)
                        try:
                            img.save(location + str(count) + ".jpg")
                        except:
                            raise Exception('Location given is invalid')
                    except:
                        print("error finding photo")
                        pass
            if size == "landscapes":
                count = 0
                for landscape in self.landscapes:
                    try:
                        img = Image.open(requests.get(landscape,timeout=5,stream=True).raw)
                        try:
                            img.save(location + str(count) + ".jpg")
                        except:
                            raise Exception('Location given is invalid')
                    except:
                        print("error finding photo")
                        pass
            if size == "potraits":
                count = 0
                for potrait in self.potraits:
                    try:
                        img = Image.open(requests.get(potrait,timeout=5,stream=True).raw)
                        try:
                            img.save(location + str(count) + ".jpg")
                        except:
                            raise Exception('Location given is invalid')
                    except:
                        print("error finding photo")
                        pass
            if size == "smalls":
                count = 0
                for small in self.smalls:
                    try:
                        img = Image.open(requests.get(small,timeout=5,stream=True).raw)
                        try:
                            img.save(location + str(count) + ".jpg")
                        except:
                            raise Exception('Location given is invalid')
                    except:
                        print("error finding photo")
                        pass
            if size == "mediums":
                count = 0
                for medium in self.mediums:
                    try:
                        img = Image.open(requests.get(medium,timeout=5,stream=True).raw)
                        try:
                            img.save(location + str(count) + ".jpg")
                        except:
                            raise Exception('Location given is invalid')
                    except:
                        print("error finding photo")
                        pass
            if size == "larges":
                count = 0
                for large in self.larges:
                    try:
                        img = Image.open(requests.get(large,timeout=5,stream=True).raw)
                        try:
                            img.save(location + str(count) + ".jpg")
                        except:
                            raise Exception('Location given is invalid')
                    except:
                        print("error finding photo")
                        pass
            if size == "extra_larges":
                count = 0
                for extr_large in self.extra_larges:
                    try:
                        img = Image.open(requests.get(extr_large,timeout=5,stream=True).raw)
                        try:
                            img.save(location + str(count) + ".jpg")
                        except:
                            raise Exception('Location given is invalid')
                    except:
                        print("error finding photo")
                        pass
            if size == "originals":
                count = 0
                for original in self.originals:
                    try:
                        img = Image.open(requests.get(original
                        ,timeout=5,stream=True).raw)
                        try:
                            img.save(location + str(count) + ".jpg")
                        except:
                            raise Exception('Location given is invalid')
                    except:
                        print("error finding photo")
                        pass
        
        else:
            if size == "tinys":
                count = 0
                for tiny in tinys:
                    try:
                        img = Image.open(requests.get(tiny,timeout=5,stream=True).raw)
                        try:
                            img.save(str(count) + ".jpg")
                        except:
                            raise Exception('permission to save not given to cwd')
                    except:
                        print("error finding photo")
                        pass
            if size == "landscapes":
                count = 0
                for landscape in self.landscapes:
                    try:
                        img = Image.open(requests.get(landscape,timeout=5,stream=True).raw)
                        try:
                            img.save(str(count) + ".jpg")
                        except:
                            raise Exception('permission to save not given to cwd')
                    except:
                        print("error finding photo")
                        pass
            if size == "potraits":
                count = 0
                for potrait in self.potraits:
                    try:
                        img = Image.open(requests.get(potrait,timeout=5,stream=True).raw)
                        try:
                            img.save(str(count) + ".jpg")
                        except:
                            raise Exception('permission to save not given to cwd')
                    except:
                        print("error finding photo")
                        pass
            if size == "smalls":
                count = 0
                for small in self.smalls:
                    try:
                        img = Image.open(requests.get(small,timeout=5,stream=True).raw)
                        try:
                            img.save(str(count) + ".jpg")
                        except:
                            raise Exception('permission to save not given to cwd')
                    except:
                        print("error finding photo")
                        pass
            if size == "mediums":
                count = 0
                for medium in self.mediums:
                    try:
                        img = Image.open(requests.get(medium,timeout=5,stream=True).raw)
                        try:
                            img.save(str(count) + ".jpg")
                        except:
                            raise Exception('permission to save not given to cwd')
                    except:
                        print("error finding photo")
                        pass
            if size == "larges":
                count = 0
                for large in self.larges:
                    try:
                        img = Image.open(requests.get(large,timeout=5,stream=True).raw)
                        try:
                            img.save(str(count) + ".jpg")
                        except:
                            raise Exception('permission to save not given to cwd')
                    except:
                        print("error finding photo")
                        pass
            if size == "extra_larges":
                count = 0
                for extra_large in self.extra_larges:
                    try:
                        img = Image.open(requests.get(extra_large,timeout=5,stream=True).raw)
                        try:
                            img.save(str(count) + ".jpg")
                        except:
                            raise Exception('permission to save not given to cwd')
                    except:
                        print("error finding photo")
                        pass
            if size == "originals":
                count = 0
                for original in self.originals:
                    try:
                        img = Image.open(requests.get(original,timeout=5,stream=True).raw)
                        try:
                            img.save(str(count) + ".jpg")
                        except:
                            raise Exception('permission to save not given to cwd')
                    except:
                        print("error finding photo")
                        pass

    # def videos(self,json_body):
    #     # Add all the attrs to the lists
    #     for photo in json_body:
    #         try:
    #             self.ids.insert(photo['id'])
    #             self.widths.insert(photo['width'])
    #             self.heights.insert(photo['height'])
    #             self.urls.insert(photo['url'])
    #             self.photographers.insert(photo['photographer'])
    #             self.photographer_urls.insert(photo['photographer_url'])
    #             self.photographer_ids.insert(photo['photographer_id'])
    #             self.originals.insert(photo['original'])
    #             self.extra_larges.insert(photo['extra_large'])
    #             self.larges.insert(photo['large'])
    #             self.mediums.insert(photo['medium'])
    #             self.smalls.insert(photo['small'])
    #             self.potraits.insert(photo['potrait'])
    #             self.landscapes.insert(photo['landscape'])
    #             self.tinys.insert(photo['tiny'])
    #         except:
    #             pass

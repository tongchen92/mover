import requests
import os
import sys

token = 'EAAQV13Vk7zkBAKKqgpLnek1JvbZB4hYrOF6OD9geYzOZAB4YX8855r0iDq0CJBJlVGD5xCorX5tVqZCBpVAeRZBtWKNl0ZBhuA0SsyHROommuIcNZAX3rkYBlZA6YWUU07mB6WSRbzq6rVQbyWAjlLjVwi5I2CZAyKQ5l5N3IQOrJwZDZD'


def get_file():
    text_file = open("to_be_upload.txt", "r")
    files = text_file.readlines()

    vid_name = files.pop(0).rstrip()

    with open('to_be_upload.txt', 'w') as f:
        f.write(''.join(files))

    return vid_name


def fb_upload(file_name):
    title = file_name.replace('.mp4','')
    description = file_name + ' - Follow us to get your daily doses of cuteness!'

    page_id = '405591246712412'
    path = "{0}/videos".format(page_id)
    fb_url = "https://graph-video.facebook.com/{0}?access_token={1}".format(
             path, token)

    local_video_file = {'file': open('modified/'+file_name, 'rb')}
    r = requests.post(fb_url, params={'title': title, 'description':description}, files =local_video_file )

def main():
    fb_upload(get_file())


if __name__ == "__main__":
    main()

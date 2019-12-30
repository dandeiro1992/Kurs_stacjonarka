import requests
from sage import *
import os
import functools

def save_url_file(url, dir, file, msg):
    print(msg.format(file))

    r = requests.get(url, stream=True)
    file_path =os.path.join(dir, file)
    print(file_path+"\n")
    with open(file_path, "wb") as f:
        f.write(r.content)


dir = os.getcwd()+'/'

save_url_to_dir=functools.partial(save_url_file,dir=dir,msg="Please wait: {}")

url = 'http://mobilo24.eu/spis'
file = 'spis.html'

save_url_to_dir(url=url,file=file)



# msg = "Please wait - the file {} will be downloaded"
#
# url = 'http://mobilo24.eu/spis'
# dir = os.getcwd()+'/'
# file = 'spis.html'
# save_url_file(url, dir, file, msg)
#
# url = 'https://www.mobilo24.eu/wp-content/uploads/2015/11/Mobilo_logo_kolko_512-565b1626v1_site_icon.png'
# dir = os.getcwd()+'/'
# file = 'logo.png'
# save_url_file(url, dir, file, msg)

import os, sys, argparse
import requests
import random

parser = argparse.ArgumentParser()

parser.add_argument('--blur', help='Set the image blur')
parser.add_argument('--foo', help='Foo the program')
args = parser.parse_args()

def save_image(image):
  with open('image.jpg', 'wb') as f:
    f.write(image)
  f.close()

def request_wallpaper(URL):
  return requests.get(URL).content

def main():
  print(str())
  URL = 'https://picsum.photos/1920/1080.jpg'
  PATH = '~/Repos/wallpaper-gen/image.jpg'
  save_image(request_wallpaper(URL))

  os.system('gsettings set org.gnome.desktop.background picture-uri '+ PATH)

if __name__ == "__main__":
	main()

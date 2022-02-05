import os
import sys
import argparse
import requests
import random
import imageWriter
import phraseGenerator

parser = argparse.ArgumentParser()

parser.add_argument('--blur', default='4', help='Set the image blur (default=4)')
parser.add_argument('--widht', default='1920', help='Set the image widht (default=1920)')
parser.add_argument('--height', default='1080', help='Set the image height (default=1080)')

args = parser.parse_args()

def save_image(image):
  with open('image.jpg', 'wb') as f:
    f.write(image)
  f.close()

def main():
  PATH = os.getcwd()+'/image.jpg'
  URL = 'https://picsum.photos/'+args.widht+'/'+args.height+'.jpg'
  
  if args.blur:
    URL += '?blur='+args.blur
  save_image(requests.get(URL).content)

  phrase = phraseGenerator.raul_genival_phrase()
  if phrase:
    imageWriter.write_text_on_image(phrase)
  
  os.system('gsettings set org.gnome.desktop.background picture-uri '+ PATH)

if __name__ == "__main__":
	main()

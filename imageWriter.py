from PIL import Image 
from PIL import ImageFont
from PIL import ImageDraw

def write_text_on_image(phrase):
    wallpaper = Image.open('./image.jpg')
    
    screen_diagonal = (wallpaper.width**2 + wallpaper.height**2)**(1/2)
    
    phrase_font_const = int(screen_diagonal * 0.017)
    phrase_font = ImageFont.truetype('./Quintessential-Regular/Quintessential-Regular.ttf', phrase_font_const)
    
    phrase_padding_const = screen_diagonal * 0.05
    phrase_padding_right = wallpaper.width - phrase_padding_const
    phrase_padding_bottom = wallpaper.height - phrase_padding_const

    drawable_wallpaper = ImageDraw.Draw(wallpaper)
    #shadow text
    drawable_wallpaper.text((phrase_padding_right+4,phrase_padding_bottom+4), phrase, 
                            fill=(0, 0, 0, 5), font=phrase_font, anchor="rs")
    #real text
    drawable_wallpaper.text((phrase_padding_right,phrase_padding_bottom), phrase, 
                            fill=(255, 255, 255, 255), stroke_width=1, stroke_fill=(0,0,0),
                            font=phrase_font, anchor="rs")
    
    wallpaper.save('./image.jpg')

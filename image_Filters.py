'''
Simple image processing
'''

import graphics
from graphics import *
from random import randrange

def red_part_of_an_image(image):
    red_image = image.clone() 
    for y in range(0,image.getHeight()):
        for x in range(0,image.getWidth()):
            color = image.getPixel(x,y) # get the pixel color
            red_color = color[0] # pull out the red component
            new_color = [red_color, 0, 0] 
            red_image.setPixel(x,y, new_color) 
    return red_image 

def color_image_to_grey_scale(image):
    grey_image = image.clone() 
    for y in range(0,image.getHeight()):
        for x in range(0,image.getWidth()):
            color = image.getPixel(x,y) 
            c = (color[0]+color[1]+color[2])//3 
            new_color = [c, c, c] 
            grey_image.setPixel(x,y, new_color)  
    return grey_image

def photonegative_of_an_image(image):
    neg_image = image.clone() 
    for y in range(0,image.getHeight()):
        for x in range(0,image.getWidth()):
            color = image.getPixel(x,y) 
            c1 = 255-color[0]
            c2 = 255-color[1]
            c3 = 255-color[2]
            new_color = [c1, c2, c3] 
            neg_image.setPixel(x,y, new_color)  
    return neg_image 

def brighten_image(image):
    bright_image = image.clone() 
    for y in range(0,image.getHeight()):
        for x in range(0,image.getWidth()):
            color = image.getPixel(x,y) 
            c1 = color[0]*2
            c2 = color[1]*2
            c3 = color[2]*2
            new_color = [c1, c2, c3] # changing pixels to neg.
            bright_image.setPixel(x,y, new_color)  
    return bright_image 


def color_image_to_pointillist(image, win):
    art_image = image.clone()  
    for i in range(50000):
        x_loc = randrange(0,image.getWidth()-1)
        y_loc = randrange(0,image.getHeight() - 1)
        color = image.getPixel(x_loc, y_loc) 

        circle = graphics.Circle(Point(x_loc, y_loc), 5) 
        circle.setFill(color)
        circle.setWidth(0) 
        circle.draw(win)


def load_image(filename):

    image = graphics.Image(graphics.Point(0, 0), filename)

    image.move(int(image.getWidth()/2), int(image.getHeight()/2))
    return image


def main():

    image = load_image("me2.gif")

    win = graphics.GraphWin('Image Art', image.getWidth(), image.getHeight(), autoflush=False)
    win.setBackground('yellow') 

  
    image.draw(win)
    win.getMouse()

  
    red_image = red_part_of_an_image(image)
    red_image.draw(win)
    win.getMouse()

   
    grey = color_image_to_grey_scale(image)
    grey.draw(win)
    win.getMouse()

  
    photonegative = photonegative_of_an_image(image)
    photonegative.draw(win)
    win.getMouse()

    
    brightened_image = brighten_image(image)
    brightened_image.draw(win)
    win.getMouse()

    
    color_image_to_pointillist(image, win)
    win.getMouse()

    win.close()


main()

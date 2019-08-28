#!/usr/bin/env python3

import utils, open_color, arcade

utils.check_version((3,7))

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Smiley Face Example"

class Faces(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # Show the mouse cursor
        self.set_mouse_visible(True)
# these lines set the size of the screen and the limit of where you can move your mouse
        self.x = SCREEN_WIDTH / 2
        self.y = SCREEN_HEIGHT / 2
# sets the background to white
        arcade.set_background_color(open_color.white)
# draws the below shapes live, on the mouse cursor
    def on_draw(self):
        """ Draw the face """
        arcade.start_render() # begins the rendering of the face
        face_x,face_y = (self.x,self.y) # sets the location of the face, following your mouse cursor
        smile_x,smile_y = (face_x + 0,face_y - 10) # Sets the location of the smile
        eye1_x,eye1_y = (face_x - 30,face_y + 20)  # sets the location of the eyes (this and below line)
        eye2_x,eye2_y = (face_x + 30,face_y + 20)
        catch1_x,catch1_y = (face_x - 25,face_y + 25) # sets the location of the light catches (this and below line)
        catch2_x,catch2_y = (face_x + 35,face_y + 25) 
# the below lines all determine the size and the color of each component of the smiley face 
        arcade.draw_circle_filled(face_x, face_y, 100, open_color.yellow_3)
        arcade.draw_circle_outline(face_x, face_y, 100, open_color.black,4)
        arcade.draw_ellipse_filled(eye1_x,eye1_y,15,25,open_color.black)
        arcade.draw_ellipse_filled(eye2_x,eye2_y,15,25,open_color.black)
        arcade.draw_circle_filled(catch1_x,catch1_y,3,open_color.gray_2)
        arcade.draw_circle_filled(catch2_x,catch2_y,3,open_color.gray_2)
        arcade.draw_arc_outline(smile_x,smile_y,60,50,open_color.black,190,350,4)

# this connects the smiley face picture to the cursor, so that it follows you as you move around the screen
    def on_mouse_motion(self, x, y, dx, dy):
        """ Handle Mouse Motion """
        self.x = x
        self.y = y


# opens the window and runs the program
window = Faces()
arcade.run()
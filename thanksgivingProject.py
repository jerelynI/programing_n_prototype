#jerelyn
#12-2-24
#thankgiving project

import simplegui


frame = simplegui.create_frame("Thanksgiving Drawing", 600, 600)

#the table
def draw_table(canvas):
    # Table top
    canvas.draw_rectangle((200, 230), (400, 270), 2, "SaddleBrown", "Peru")
    # Table legs
    canvas.draw_rectangle((220, 270), (240, 300), 2, "SaddleBrown")  # Left leg
    canvas.draw_rectangle((360, 270), (380, 300), 2, "SaddleBrown")  # Right leg
    canvas.draw_rectangle((280, 270), (300, 300), 2, "SaddleBrown")  # Middle left leg
    canvas.draw_rectangle((320, 270), (340, 300), 2, "SaddleBrown")  # Middle right leg

def draw_turkey(canvas):
  #body
    canvas.draw_circle((300, 250), 70, 4, "Brown", "SaddleBrown")
 #head
    canvas.draw_circle((300, 200), 45, 4, "Brown", "SaddleBrown")
  #nose
    canvas.draw_polygon([(300, 200), (320, 205), (300, 210)], 2, "Orange", "Orange")
  #eyes
    canvas.draw_circle((290, 195), 5, 2, "Black", "Black")
    canvas.draw_circle((310, 195), 5, 2, "Black", "Black")

def draw(canvas):

    draw_turkey(canvas)

    leaf_centers = [(450, 90), (420, 120), (480, 130), (430, 150)]
    colors = ["Red", "Orange", "Yellow", "Brown"]
   
    canvas.draw_text("Happy Thanksgiving!", (170, 40), 38, "DarkOrange")

frame.set_draw_handler(draw)
frame.set_canvas_background("beige")
frame.start()

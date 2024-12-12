#jerelyn
#1-2
#12-12-24


import simplegui
import random
#global variable for the snow
snow_y =[]
#constants for window frame, snow
width = 600
height = 400
snow_flakes = 5
snowfall_speed = 1

for i in range(snow_flakes):
    snow_y.append(random.randint(0,height))
    
def draw(canvas):
    global snow_y
    #draw the background (light blue for sky
    canvas.draw_polygon([(0,0),(width,0), (width,height), (0,height)],1,"white", "LightBlue")
    for i in range(snow_flakes):
        snowflake_x = random.randint(0,width)
        snowflake_y = random.randint(0,height)
        canvas.draw_circle((snowflake_x, snow_y[1]), 10, 1, "white", "white")
    
frame = simplegui.create_frame("winter animation", width, height)
frame.set_draw_handler(draw)

frame.start()

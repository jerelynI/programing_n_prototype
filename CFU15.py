import simplegui


WIDTH = 200
HEIGHT = 200


def draw(canvas):
    #face
    canvas.draw_circle((100, 100), 80, 3, "black", "yellow")

    # eyes 
    canvas.draw_circle((70, 80), 10, 1, "black", "black")  # left eye
    canvas.draw_circle((130, 80), 10, 1, "black", "black")  # right eye

    #smile
    canvas.draw_line((70, 120), (130, 120), 3, "black")
    canvas.draw_line((70, 120), (100, 140), 3, "black")
    canvas.draw_line((130, 120), (100, 140), 3, "black")


frame = simplegui.create_frame("CFU15 Happy Shapes", WIDTH, HEIGHT)


frame.set_draw_handler(draw)
frame.start()

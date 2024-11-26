import simplegui

def draw_handler(canvas):
    canvas.draw_point([50,59],"white")
    canvas.draw_point([50,60],"white")
    canvas.draw_point([50,62],"white")
    canvas.draw_point([50,65],"white")
    canvas.draw_point([50,68],"white")
    canvas.draw_point([50,70],"white")
    canvas.draw_point([50,72],"white")
    canvas.draw_point([100,59],"white")
    canvas.draw_point([100,60],"white")
    canvas.draw_point([100,62],"white")
    canvas.draw_point([100,65],"white")
    canvas.draw_point([100,68],"white")
    canvas.draw_point([100,70],"white")
    canvas.draw_point([100,72],"white")
    canvas.draw_point([40,100],"white")
    canvas.draw_point([50,120],"white")
    canvas.draw_point([60,130],"white")
    canvas.draw_point([70,140],"white")
    canvas.draw_point([80,140],"white")
    canvas.draw_point([90,140],"white")
    canvas.draw_point([100,130],"white")
    canvas.draw_point([120,100],"white")
    canvas.draw_point([110,120],"white")
   

    
frame= simplegui.create_frame("CFU'13", 200,200)
frame.set_canvas_background("black")
frame.set_draw_handler(draw_handler)
frame.start()

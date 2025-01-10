#jerelyn
#CFU16
import simplegui

def draw_handeler(canvas):
    canvas.draw_circle((100, 140), 45, 95, "yellow")
    canvas.draw_circle((130, 145), 3, 5, "black")
    canvas.draw_circle((125, 143), 3, 5, "black")
    canvas.draw_circle((120, 150), 3, 5, "black")
    canvas.draw_circle((115, 150), 3, 5, "black")
    canvas.draw_circle((110, 150), 3, 5, "black")
    canvas.draw_circle((105, 150), 3, 5, "black")
    canvas.draw_circle((100, 150), 3, 5, "black")
    canvas.draw_circle((95, 150), 3, 5, "black")
    canvas.draw_circle((90, 150), 3, 5, "black")
    canvas.draw_circle((85, 150), 3, 5, "black")
    canvas.draw_circle((80, 150), 3, 5, "black")
    canvas.draw_circle((75, 150), 3, 5, "black")
    canvas.draw_circle((70, 146), 3, 5, "black")
    canvas.draw_circle((65, 144), 3, 5, "black")
    canvas.draw_circle((65, 75), 8, 19, "black")
    canvas.draw_circle((125, 75), 8, 19, "black")

frame = simplegui.create_frame("CFU 16", 200, 200)
frame.set_canvas_background("white")
frame.set_draw_handler(draw_handeler)
frame.start()

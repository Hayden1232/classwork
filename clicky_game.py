import arcade
import math
import random
 
WIDTH = 800
HEIGHT = 600
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Game"
 
window = arcade.Window(WIDTH, HEIGHT, "My Arcade Game")
arcade.set_background_color(arcade.color.WHITE)
 
# Initialize your variables here
circle_x = WIDTH//2
circle_y = HEIGHT//2
circle_radius = 100
Area = circle_radius * circle_radius * 3.14
total_value = 0
score = total_value
place_x = 30
place_y = 500

 
 
 
 
 
@window.event("on_draw")
def game_loop():
   # import global variables here.
   global circle_radius
   global total_value
   # update your variables here.
   score = total_value + 1
   # Draw things here.
   arcade.start_render()
   arcade.draw_circle_filled(circle_x, circle_y, circle_radius, arcade.color.RED)
   arcade.draw_text("The Circle Game", 30, 550, arcade.color.BLACK, 25)
   arcade.draw_text(f"Score: {score}", place_x, place_y, arcade.color.BLACK, 15)
@window.event
def on_mouse_press(mouse_x, mouse_y, button, modifiers):
 
   global circle_radius, circle_x, circle_y, total_value
   if button == arcade.MOUSE_BUTTON_LEFT:
      d = math.sqrt((mouse_x - circle_x)**2 + (mouse_y - circle_y)**2)
      if d < circle_radius:
          circle_radius = circle_radius + 15
          circle_x = random.randint(0, 800)
          circle_y = random.randint(0,600)
          total_value = total_value + 1 


arcade.run()


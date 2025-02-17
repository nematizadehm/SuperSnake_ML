import arcade
from scr.color import  Color


class Snake(arcade.Sprite):
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        super().__init__()
        self.speed = 8
        self.center_x = SCREEN_WIDTH // 2
        self.center_y = SCREEN_HEIGHT // 2
        self.change_x = 1
        self.change_y = 0
        self.width = 16
        self.height = 16
        self.color1 = Color.green
        self.color2 = Color.green_dark  
        self.score = 0
        self.r = 8
        self.body = []


    def draw(self):
        for i, part in enumerate(self.body):
            if i % 2 == 0:
                arcade.draw_circle_filled(part['x'], part['y'], self.r, self.color2)
            else:
                arcade.draw_circle_filled(part['x'], part['y'], self.r, self.color1)
                
        arcade.draw_circle_filled(self.center_x, self.center_y, self.r, self.color1)
 

    def on_update(self, delta_time: float = 1/60):
        self.body.append({'x': self.center_x, 'y': self.center_y})
        if len(self.body) > self.score:
            self.body.pop(0)
        self.center_x += self.speed * self.change_x
        self.center_y += self.speed * self.change_y

    def eat(self):
            self.score += 1
    def eat_poo(self , poo):
        del poo
        self.score -= 1
        if self.score < 0 :
            print("score :",self.score)
            arcade.draw_text("Game Over", 20 , 210  , arcade.color.RED , 80 ,  bold=True)
            arcade.close_window()
            exit(0)
        print("score :",self.score) 
    def move(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        self.body.append({'x':self.center_x, 'y':self.center_y})
        # print((self.body[0]["x"]))
        if len(self.body) > self.score:
            self.body.pop(0)

        if self.center_x<0:
            self.center_x= SCREEN_WIDTH
        elif self.center_x> SCREEN_WIDTH:
            self.center_x=0
        elif self.center_y<0:
            self.center_y=SCREEN_HEIGHT
        elif self.center_y>SCREEN_HEIGHT:
            self.center_y=0
        
        self.center_x += self.change_x*self.speed
        self.center_y += self.change_y*self.speed

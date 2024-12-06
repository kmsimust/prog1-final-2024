import turtle
import random
import Ball
import Clock

class Simulator:
    def __init__(self, num_balls):
        self.num_balls = num_balls
        self.ball_list = []
        turtle.speed(0)
        turtle.tracer(0)
        turtle.hideturtle()
        turtle.colormode(255)
        self.canvas_width = turtle.screensize()[0]
        self.canvas_height = turtle.screensize()[1]
        self.ball_radius = 0.05 * self.canvas_width
        for n in range(self.num_balls):
            x = (random.uniform(-1*self.canvas_width + self.ball_radius, self.canvas_width - self.ball_radius))
            y = (random.uniform(-1*self.canvas_height + self.ball_radius, self.canvas_height - self.ball_radius))
            vx = (10*random.uniform(-1.0, 1.0))
            vy = (10*random.uniform(-1.0, 1.0))
            ball_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            self.ball_list.append(Ball.Ball(self.ball_radius, x, y, vx, vy, ball_color))

    def draw_border(self):
        turtle.penup()
        turtle.goto(-self.canvas_width, -self.canvas_height)
        turtle.pensize(10)
        turtle.pendown()
        turtle.color((0, 0, 0))   
        for i in range(2):
            turtle.forward(2*self.canvas_width)
            turtle.left(90)
            turtle.forward(2*self.canvas_height)
            turtle.left(90)

    def run(self):
        dt = 0.2
        while True:  
            for t in range(0, 10):
                turtle.clear()
                self.draw_border() 
                Clock.Clock.clear(Tom)
                Clock.Clock.draw(Tom, t)
                Clock.Clock.my_delay(dt)
                for i in range(self.num_balls):
                    Ball.Ball.draw_ball(self.ball_list[i])
                    Ball.Ball.move_ball(self.ball_list[i], dt)
                    Ball.Ball.update_ball_velocity(self.ball_list[i])
                turtle.update()
        # hold the window; close it by clicking the window close 'x' mark
        turtle.done()


num_balls = 5
Tom = turtle.Turtle()
tom_color = (255, 0, 0)
Clock.Clock.init(Tom, tom_color)
my_simulator = Simulator(num_balls)
my_simulator.run()

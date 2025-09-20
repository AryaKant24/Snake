from turtle import Turtle,Screen
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]

class Snake:
     def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

     def create_snake(self):
          for position in STARTING_POSITIONS:
               self.add_segment(position)

     def add_segment(self,position):
          tim = Turtle()
          tim.shape("square")
          tim.color("white")
          tim.penup()
          tim.goto(position)
          self.snake.append(tim)
          
     
     def extend(self):
          self.add_segment(self.snake[-1].position())
          
         

     def move(self):
        for seg in range(len(self.snake)-1,0,-1):
                new_x = self.snake[seg-1].xcor()
                new_y = self.snake[seg-1].ycor()
                self.snake[seg].goto(new_x,new_y)
        self.snake[0].fd(20)

     def up(self):
         for seg in range(len(self.snake)-1,0,-1):
                new_x = self.snake[seg-1].xcor()
                new_y = self.snake[seg-1].ycor()
                self.snake[seg].goto(new_x,new_y)
         if(self.snake[0].heading() == 0):
             self.snake[0].left(90)
             self.move()
         elif(self.snake[0].heading() == 90):
              self.move()
         elif(self.snake[0].heading() == 180):
              self.snake[0].right(90)
              self.move()
         elif(self.snake[0].heading() == 270):
              self.move()
    
     def down(self):
         for seg in range(len(self.snake)-1,0,-1):
                new_x = self.snake[seg-1].xcor()
                new_y = self.snake[seg-1].ycor()
                self.snake[seg].goto(new_x,new_y)
         if(self.snake[0].heading() == 0):
             self.snake[0].right(90)
             self.move()
         elif(self.snake[0].heading() == 90):
              self.move()
         elif(self.snake[0].heading() == 180):
              self.snake[0].left(90)
              self.move()
         elif(self.snake[0].heading() == 270):
              self.move()

     def right(self):
         for seg in range(len(self.snake)-1,0,-1):
                new_x = self.snake[seg-1].xcor()
                new_y = self.snake[seg-1].ycor()
                self.snake[seg].goto(new_x,new_y)
         if(self.snake[0].heading() == 0):
             self.move()
         elif(self.snake[0].heading() == 90):
              self.snake[0].right(90)
              self.move()
         elif(self.snake[0].heading() == 180):
              self.move()
         elif(self.snake[0].heading() == 270):
              self.snake[0].left(90)
              self.move()
    
     def left(self):
         for seg in range(len(self.snake)-1,0,-1):
                new_x = self.snake[seg-1].xcor()
                new_y = self.snake[seg-1].ycor()
                self.snake[seg].goto(new_x,new_y)
         if(self.snake[0].heading() == 0):
             self.move()
         elif(self.snake[0].heading() == 90):
              self.snake[0].left(90)
              self.move()
         elif(self.snake[0].heading() == 180):
              self.move()
         elif(self.snake[0].heading() == 270):
              self.snake[0].right(90)
              self.move()
    
    
         
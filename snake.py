from turtle import Turtle

class Snake(Turtle):
    
    # Initializing the snake 
    def __init__(self):
        
        super().__init__()
        self.positions=[(-40,0),(-20,0),(0,0)]
        self.snake=[]
        self.hideturtle()
        self.create_snake()
    
    # Make the snake 
    def create_snake(self):
        for position in self.positions:
            new_segment=Turtle()    
            new_segment.shape("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position[0],position[1])
            
            self.snake.append(new_segment)

        self.head=self.snake[-1]
        
    # go ahead

    def move(self):
        
        for segment in range(len(self.snake)-1):
            self.snake[segment].goto(self.snake[segment+1].pos())
        
        self.head.forward(20)
    
    # Movement shapes
     
    def up(self):
        
        self.head.setheading(90)

    def down(self):
        self.head.setheading(270)

    def left(self):
        self.head.setheading(180)

    def right(self):
        self.head.setheading(0)

    #grow up when eat food 
    def add_segment(self):
        new_segment=Turtle()
        new_segment.shape("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(self.snake[0].pos())
        self.snake.insert(0,new_segment)

   
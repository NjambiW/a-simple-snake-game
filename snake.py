from turtle import Turtle

STARTING_POSITION = [(0, 0), (20, 0), (40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    """contains a list of positions and segments of the snake"""

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        snake_segment = Turtle(shape="square")
        snake_segment.color("white")
        snake_segment.penup()
        snake_segment.goto(position)
        self.segments.append(snake_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        """makes sure all the segments move together
        to create a singular movement of the snake"""
        for segment_number in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment_number - 1].xcor()
            new_y = self.segments[segment_number - 1].ycor()
            self.segments[segment_number].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def up(self):
        """moves the snake upwards"""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """moves the snake downwards"""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """moves the snake to the left"""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """moves the snake to the right"""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

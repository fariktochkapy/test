from tkinter import *
import random
WIDTH = 800
HEIGHT = 600
SEG_SIZE = 20
IN_GAME = True


def create_block():
    global BLOCK
    posx = SEG_SIZE * random.randint(1, (WIDTH - SEG_SIZE) / SEG_SIZE)
    posy = SEG_SIZE * random.randint(1, (HEIGHT - SEG_SIZE) / SEG_SIZE)
    BLOCK = c.create_oval(posx, posy,
                          posx + SEG_SIZE, posy + SEG_SIZE,
                          fill="red")



class Score(object):
    def __init__(self):
        self.score = 0
        self.x = 55
        self.y = 15
        c.create_text(self.x, self.y, text="Счёт: {}".format(self.score), font="Arial 20",
                      fill="Yellow", tag="score", state='hidden')


    def increment(self):
        c.delete("score")
        self.score += 1
        c.create_text(self.x, self.y, text="Счёт: {}".format(self.score), font="Arial 20",
                      fill="Yellow", tag="score")


    def reset(self):
        c.delete("score")
        self.score = 0



def main():
    global IN_GAME
    if IN_GAME:
        s.move()


        head_coords = c.coords(s.segments[-1].instance)
        x1, y1, x2, y2 = head_coords


        if x2 > WIDTH or x1 < 0 or y1 < 0 or y2 > HEIGHT:
            IN_GAME = False


        elif head_coords == c.coords(BLOCK):
            s.add_segment()
            c.delete(BLOCK)
            create_block()


        else:
            for index in range(len(s.segments) - 1):
                if head_coords == c.coords(s.segments[index].instance):
                    IN_GAME = False


        root.after(100, main)

    else:
        set_state(restart_text, 'normal')
        set_state(game_over_text, 'normal')
        set_state(close_but, 'normal')


class Segment(object):
    def __init__(self, x, y):
        self.instance = c.create_rectangle(x, y,
                                           x + SEG_SIZE, y + SEG_SIZE,
                                           fill="green")


class Snake(object):
    def __init__(self, segments):
        self.segments = segments


        self.mapping = {"Down": (0, 1), "Right": (1, 0),
                        "Up": (0, -1), "Left": (-1, 0)}


        self.vector = self.mapping["Right"]

    def move(self):
        for index in range(len(self.segments) - 1):
            segment = self.segments[index].instance
            x1, y1, x2, y2 = c.coords(self.segments[index + 1].instance)
            c.coords(segment, x1, y1, x2, y2)

        x1, y1, x2, y2 = c.coords(self.segments[-2].instance)
        c.coords(self.segments[-1].instance,
                 x1 + self.vector[0] * SEG_SIZE, y1 + self.vector[1] * SEG_SIZE,
                 x2 + self.vector[0] * SEG_SIZE, y2 + self.vector[1] * SEG_SIZE)

    def add_segment(self):
        score.increment()
        last_seg = c.coords(self.segments[0].instance)
        x = last_seg[2] - SEG_SIZE
        y = last_seg[3] - SEG_SIZE
        self.segments.insert(0, Segment(x, y))

    def change_direction(self, event):
        if event.keysym in self.mapping:
            self.vector = self.mapping[event.keysym]


    def reset_snake(self):
        for segment in self.segments:
            c.delete(segment.instance)


def set_state(item, state):
    c.itemconfigure(item, state=state)
    c.itemconfigure(BLOCK, state='hidden')


def clicked(event):
    global IN_GAME
    s.reset_snake()
    IN_GAME = True
    c.delete(BLOCK)
    score.reset()
    c.itemconfigure(restart_text, state='hidden')
    c.itemconfigure(game_over_text, state='hidden')
    c.itemconfigure(close_but, state='hidden')
    start_game()


def start_game():
    global s
    create_block()
    s = create_snake()


    c.bind("<KeyPress>", s.change_direction)
    main()

def create_snake():
    segments = [Segment(SEG_SIZE, SEG_SIZE),
                Segment(SEG_SIZE * 2, SEG_SIZE),
                Segment(SEG_SIZE * 3, SEG_SIZE)]
    return Snake(segments)


def close_win(root):
    exit()

root = Tk()
root.title("Змейка")

c = Canvas(root, width=WIDTH, height=HEIGHT, bg="#000000")
c.grid()

c.focus_set()

game_over_text = c.create_text(WIDTH / 2, HEIGHT / 2, text="Ты проиграл!",
                               font='Arial 20', fill='red',
                               state='hidden')

restart_text = c.create_text(WIDTH / 2, HEIGHT - HEIGHT / 3,
                             font='Arial 25',
                             fill='green',
                             text="Начать новую игру",
                             state='hidden')

close_but = c.create_text(WIDTH / 2, HEIGHT - HEIGHT / 5, font='Arial 25',
                          fill='green',
                          text="Выход из игры",
                          state='hidden')

c.tag_bind(restart_text, "<Button-1>", clicked)
c.tag_bind(close_but, "<Button-1>", close_win)

score = Score()

start_game()

root.mainloop()

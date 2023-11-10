import turtle

turtle.speed(0)


def draw_house(
    x=0,
    y=0,    
    base_w=100,
    base_h=10,
    base_color='grey',
    walls_w=100,
    walls_h=60,
    walls_color='red',
    roof_w=100,
    roof_h=30,
    roof_color='black'
):
    '''
    вызывает функцию рисования фундамента
    вызывает функцию рисования стен
    вызывает функцию рисования крыши

    x - левый нижний угол фундамента
    y - левый нижний угол фундамента

    base_w - ширина фундамента
    base_h - высота фундамента
    base_color - цвет фундамента

    walls_w - ширина стен
    walls_h - высота стен
    walls_color - цвет стен

    roof_w - ширина крыши
    roof_h - высота крыши
    roof_color - цвет крыши
    '''

    print('начинаем строить дом')
    draw_base(x, y, base_w, base_h, base_color)
    draw_walls(x, y, walls_w, walls_h, walls_color, base_h)
    draw_roof(x, y, roof_w, roof_h, roof_color, base_h, walls_h)


def draw_base(x, y, width, height, color):
    ''' рисует фундамент '''
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    draw_rectangle(width, height, color)


def draw_walls(x, y, width, height, color, base_h):
    ''' рисует стены '''
turtle.penup()
turtle.goto(x, y + base_h)
turtle.pendown()
draw_rectangle(width, hieght, color)
print('рисуем стены')


def draw_roof(x, y, width, hieght, color, base_h, walls_h, walls_w):
    ''' рисует крышу '''
turtle.penup()
turtle.goto(x, y + base_h + walls_h)
turtle.pendown()
turtle.fillcolor(color)
turtle.begin_fill()
top_x = walls_w // 2
top_y = y + hieght + walls_h
turtle.goto(top_x + walls_w // 2, y)
turtle.end_fill()

def draw_rectangle(width, height, color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.fd(width)
    turtle.lt(90)
    turtle.fd(height)
    turtle.lt(90)
    turtle.fd(width)
    turtle.lt(90)
    turtle.fd(height)
    turtle.lt(90)
    turtle.end_fill()


draw_house()

turtle.done()

def find_intersection(x1, x2, y1, y2) -> str:
    points_x = set()
    points_y = set()

if x1 < x2:
    step = 1
elif x1 > x2:
    step = -1
else:
    step = 0


    if step:
        for i in range(min((x1, x2)), max((x1, x2)) + 1, step):
            points_x.add(i)
    else:
        points_x.add(x1)

    if step:
        for i in range(min((y1, y2)), min((y1, y2)) + 1, step):
            points_y.add(i)
    else:
        points_y.add(y1)

  
    if points_x.intersection(points_y):
        return 'Да'
    else:
        return 'Нет'

print(find_intersection(5, 10, 2, 8))
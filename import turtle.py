import turtle


def koch_snowflake(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_snowflake(t, order - 1, size / 3)
            t.left(angle)


def main():
    screen = turtle.Screen()
    screen.title("Koch's Snowflake")

    t = turtle.Turtle()
    t.speed(3)

    order = int(input("Recursion level: "))
    
   
    for _ in range(3):
        koch_snowflake(t, order, 300)
        t.right(120)

    screen.mainloop()


if __name__ == "__main__":
    main()

draw_koch_curve(3)

import turtle
import pandas as pd
import csv
from time import sleep
# from state_name_class import New_txt
screen = turtle.Screen()
screen.title("Indian States Quiz")
img = "India-state.gif"
turtle.addshape(img)
turtle.shape(img)
lst2 = []
lst1 = []
screen.screensize(canvheight=150,canvwidth=150)
value = True
while value:
    def mouse_loacation(x,y):
        print(x,y)
    print(mouse_loacation)
    turtle.onscreenclick(mouse_loacation)
    answer = turtle.textinput('Guess The State','Type state name and drag it to the correct location').title()
    # if answer=='End':
    #     value = False
    s_data = pd.read_csv("states_data.csv")
    s_names = s_data['state']
    lst1 = s_names.to_list()
    print(lst1)
    if answer=='End':
        value = False
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(-150,0)
        t.write("Thanks For Playing",font=("Arial", 24, "normal"))
    else:
        if answer in lst1:
            t = turtle.Turtle()
            #Next Line is Little bit tricky
            new_data= s_data[s_names==answer]
            t.penup()
            t.goto(int(new_data.x),int(new_data.y))
            def write(ans):
                t.penup()
                t.write(ans)
                t.hideturtle()
            write(answer)
            t.hideturtle()
            t.penup()
            lst2.append(answer)
        x = 5
        for i in range(5):
            t2 = turtle.Turtle()
            t2.hideturtle()
            t2.pencolor("red")
            t3 = turtle.Turtle()
            t3.hideturtle()
            t3.pencolor("blue")
            t2.penup()
            t3.penup()
            t3.goto(-150,250)
            t3.write("Next Guess in"+"       "+"secoands", font=("Arial", 16, "normal"))
            t2.goto(0,250)
            screen.tracer(0)
            t2.write(x-i,font=("Arial", 16, "normal"))
            screen.update()
            sleep(1)
            t2.clear()

screen.mainloop()

l3 = []
with open('score',mode='w') as file1:
    for i in lst1:
        if i in lst2:
            file1.write(f'\n{i}')
        else:
            # file1.write(f'\n{i}')
            l3.append(i)
# data = pd.DataFrame(l3)
# data.to_csv("Missing_States.csv")
with open("Missing_States.csv",mode='w') as file2:
    for i in l3:
        file2.write(f"\n{i}")
print(l3)
# data = pd.read_csv('score')
# data.to_csv()




# screen.exitonclick()
# obj1 = New_txt()


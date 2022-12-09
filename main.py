BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *
import pandas as pd
import random
from iteration_utilities import unique_everseen

window = Tk()
window.title("Flash Card App")
window.config(background=BACKGROUND_COLOR)
window.config(padx=50,pady=50)
data_dict = {}
data_list = []

#data process
try:
    data = pd.read_csv("/Users/andyvo/Desktop/Science/python/100days/porfolio/flash-card-project/data/word_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv("/Users/andyvo/Desktop/Science/python/100days/porfolio/flash-card-project/data/deutsch_words.csv")
    #https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists/German_subtitles_1000  (link 1000 words)
    data_dict = data.to_dict(orient="records")
    seen = set()
    for d in data_dict:
        t = tuple(d.items())
        if t not in seen:
            seen.add(t)
            data_list.append(d)
else:
    data_dict = data.to_dict(orient="records")

    seen = set()
    for d in data_dict:
        t = tuple(d.items())
        if t not in seen:
            seen.add(t)
            data_list.append(d)



english_word = []
def skip_card():
    back()
test_dict = {"hey": "asdasd", "asd":"wewqe", "asd":"asds"}

def known_card():

    data_list.remove(english_word)
    data = pd.DataFrame(data_list)
    data.to_csv("/Users/andyvo/Desktop/Science/python/100days/porfolio/flash-card-project/data/word_to_learn.csv",index=False)
    front()


def next_card():
    # df = pd.read_csv("/Users/andyvo/Desktop/Science/python/100days/day30/flash-card-project-start/data/deutsch_words.csv")
    # df.drop([0, 1])
    data = pd.DataFrame(english_word, index=[0])
    data.to_csv("/Users/andyvo/Desktop/Science/python/100days/porfolio/flash-card-project/data/word_unknown.csv", mode="a", header=False)
    front()


def front():
    canvas.itemconfig(word_back, text="", fill="#B1DDC6")
    canvas.itemconfig(canvas_image, image = cart_front_img)
    choice_word = random.choice(data_list)
    canvas.itemconfig(title, text="Deutsch", fill="black")
    canvas.itemconfig(word, text=choice_word["Deutch"], fill="black")
    global english_word
    english_word = choice_word

def back():
    global english_word
    canvas.itemconfig(canvas_image, image = cart_back_img)
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text=english_word["English"], fill="white")
    canvas.itemconfig(word_back, text=english_word["Deutch"], fill="black")







canvas = Canvas(width=800, height=526)
cart_front_img = PhotoImage(file="/Users/andyvo/Desktop/Science/python/100days/porfolio/flash-card-project/images/card_front.png")

cart_back_img = PhotoImage(file="/Users/andyvo/Desktop/Science/python/100days/porfolio/flash-card-project/images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=cart_front_img)




title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"), fill="black")
word = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"), fill="black")
word_back = canvas.create_text(400, 400, text="", font=("Ariel", 60, "bold"), fill="black")
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=3)

button_x = PhotoImage(file="/Users/andyvo/Desktop/Science/python/100days/porfolio/flash-card-project/images/wrong.png")
button_y = PhotoImage(file="/Users/andyvo/Desktop/Science/python/100days/porfolio/flash-card-project/images/right.png")
skip_button = PhotoImage(file="/Users/andyvo/Desktop/Science/python/100days/porfolio/flash-card-project/images/skip.png")
x = Button(image=button_x, highlightthickness=0, command=next_card)
y = Button(image=button_y, highlightthickness=0, command=known_card)
skip = Button(text="Flip to the back",highlightthickness=0, command=skip_card)

x.grid(column=0, row=1)
y.grid(column=2, row=1)
skip.grid(column=1, row=1)






window.after(1, front)


window.mainloop()
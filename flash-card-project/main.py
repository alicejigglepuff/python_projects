from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    word_dic = original_data.to_dict(orient="records")
else:
    word_dic = data.to_dict(orient="records")
global current_card

# ------------------------ GENERATE NEW WORD ----------------------------#
def new_word():
    global current_card, flip
    window.after_cancel(flip)
    num = random.randint(0, len(word_dic))

    current_card = word_dic[num]
    french = current_card.get("French")

    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(word, text=french, fill="black")
    canvas.itemconfig(background_image, image=front_image)
    window.after(3000, flip_card)


# ------------------------ FLIP THE CARD ----------------------------#
def flip_card():
    canvas.itemconfig(background_image, image=back_image)
    canvas.itemconfig(title, text="English", fill="white")
    english = current_card.get("English")
    canvas.itemconfig(word, text=english, fill="white")


# ------------------------ Right Button ----------------------------#
def right():
    word_dic.remove(current_card)
    new_data = pandas.DataFrame(word_dic)
    new_data.to_csv("data/words_to_learn.csv", index=False)
    new_word()


# ------------------------ CREATE UI ----------------------------#
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip = window.after(3000, flip_card)

canvas = Canvas(width=800, height=600, bg=BACKGROUND_COLOR, highlightthickness=0)
front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")
background_image = canvas.create_image(405, 263, image=front_image)
title = canvas.create_text(400, 140, text="Title", font=("Arial", 35, "italic"))
word = canvas.create_text(400, 263, text="Word", font=("Arial", 44, "bold"))
canvas.grid(row=1, column=1, columnspan=2)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=new_word)
wrong_button.grid(row=2, column=1)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=right)
right_button.grid(row=2, column=2)

# ------------------------ Function ----------------------------#
new_word()




window.mainloop()
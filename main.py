from pokebase import move
from tkinter import *
import requests
from PIL import Image, ImageTk

# basic Pokemon Move Finder Program
# Created by: Travis Huynh
# Using Python GUI for interactive user experience! 

def fetch_all_pokemon_move(name): 
    poke = move(name)
    result = "List of Pokemon that can acquire this move!\n"
    result += "-------------------------------------------------------------------------------------------\n"
    result += ", ".join(pokemon.name for pokemon in poke.learned_by_pokemon) + "\n"
    return result

def fetch_pokemon_id(name):
    poke = move(name)
    result = "Summary:\n"
    result += "-------------------------------------------------------------------------------------------\n"
    result += f"The {poke.type} type move {name} is a {poke.damage_class} type move that has an id of: {poke.id}\n"
    result += f"This move was first introduced in {poke.generation}\n\n"
    return result

def fetch_pokemon_power(name):
    poke = move(name)
    result = "Combat:\n"
    result += "-------------------------------------------------------------------------------------------\n"
    if poke.power < 100: 
        result += f"{name} has {poke.power} power and has {poke.pp} pp\n"
        result += "The power on this move is less than 100, wow so shit haha!\n"
        result += f"Additionally, this move has an accuracy of {poke.accuracy}\n\n"
        compare_eq = (poke.power / 100) * 100
        result += f"{name} is {compare_eq}% of Earthquake(ID: 84) in comparison to its power (because earthquake is op)\n"
    elif poke.power == 100: 
        result += f"{name} has {poke.power} power and has {poke.pp} pp\n"
        result += "WOW! I have much respect for this move! It has power that has the same power as earthquake OMG!!!\n"
        result += f"Additionally, this move has an accuracy of {poke.accuracy}\n\n"
        compare_eq = (poke.power / 100) * 100
        result += f"{name} is {compare_eq}% of Earthquake(ID: 84) in comparison to its power (because earthquake is op)\n"
    else: 
        result += f"{name} has {poke.power} power and has {poke.pp} pp\n"
        result += "Bruh, ain't no way its better than stab eq, how does it have more power :(\n"
        result += f"Additionally, this move has an accuracy of {poke.accuracy}\n\n"
        compare_eq = (poke.power / 100) * 100
        result += f"{name} is {compare_eq}% of Earthquake(ID: 84) in comparison to its power (because earthquake is op)\n"
    result += "-------------------------------------------------------------------------------------------\n\n"
    return result

def fetch_move_info_gui(name):
    output_text.delete(1.0, END) 

    try:
        poke = move(name)
    except Exception as e:
        output_text.insert(END, f"Error: {e}")
        return

    # Fetch move details
    output_text.insert(END, "Fetching " + name + ".......\n\n")
    output_text.insert(END, fetch_all_pokemon_move(name))
    output_text.insert(END, fetch_pokemon_id(name))
    output_text.insert(END, fetch_pokemon_power(name))

    # Display move image
    try:
        sprite = Image.open(f"icons/{name.lower()}.png")
        sprite = sprite.resize((100, 100))
        sprite = ImageTk.PhotoImage(sprite)
        sprite_label.config(image=sprite)
        sprite_label.image = sprite
    except Exception as e:
        sprite_label.config(image=None)
        print(f"Error loading sprite: {e}")

def main_gui():
    global root 
    root = Tk()
    root.title("Pokemon Move Finder")

    label = Label(root, text="Welcome to Pokemon Move Finder!\n Created by: Travis Huynh", font=("Arial", 16))
    label.pack(pady=10)

    entry = Entry(root, font=("Arial", 12), width=30)
    entry.pack(pady=10)

    def search_move():
        name = entry.get()
        if name:
            fetch_move_info_gui(name)

    button = Button(root, text="Search Move", command=search_move, font=("Arial", 12))
    button.pack(pady=10)

    global output_text
    output_text = Text(root, wrap=WORD, width=50, height=20, font=("Arial", 12))
    output_text.pack(pady=10)

    global sprite_label
    sprite_label = Label(root)
    sprite_label.pack(pady=10)

    custom_font = ("Helvetica", 14)
    label.configure(font=custom_font)
    entry.configure(font=custom_font)
    button.configure(font=custom_font)
    output_text.configure(font=custom_font)

    root.mainloop()

if __name__ == '__main__':
    main_gui()
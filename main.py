from pokebase import move
import webbrowser

# basic Pokemon Move Finder Program
# Created by: Travis Huynh

def fetch_pokemon_id(name):
    poke = move(name) 
    print("Summary:")
    print("-------------------------------------------------------------------------------------------------------")
    print("The " + str(poke.type) + " type move " + name + " is a " + str(poke.damage_class) + " type move that has an id of: " + str(poke.id))
    print("This move was first introduced in " + str(poke.generation))
    print("")


def fetch_all_pokemon_move(name): 
    poke = move(name)
    print("List of Pokemon that can aquire this move!")
    print("-------------------------------------------------------------------------------------------------------")
    print(*poke.learned_by_pokemon, sep = ", ")
    print("")


def fetch_pokemon_power(name):
    poke = move(name) 
    print("Combat:")
    print("-------------------------------------------------------------------------------------------------------")
    if poke.power < 100: 
        print(name + " has " + str(poke.power) + " power" + " and has " + str(poke.pp) + " pp")
        print("The power on this move is less than 100, wow so shit haha!")
        print("Additionally, this move has an accuracy of " + str(poke.accuracy))
        print("")
        compare_eq = (poke.power / 100) * 100
        print(name + " is " + str(compare_eq) + "% of Earthquake(ID: 84) in comparison to its power (because earthquake is op)")
    elif poke.power == 100: 
        print(name + " has " + str(poke.power) + " power" + " and has " + str(poke.pp) + " pp")
        print("WOW! I have much respect for this move! It has power that has the same power as earthquake OMG!!!")
        print("Additionally, this move has an accuracy of " + str(poke.accuracy))
        print("")
        compare_eq = (poke.power / 100) * 100
        print(name + " is " + str(compare_eq) + "% of Earthquake(ID: 84) in comparison to its power (because earthquake is op)")
    else: 
        print(name + " has " + str(poke.power) + " power" + " and has " + str(poke.pp) + " pp")
        print("Bruh, ain't no way its better than stab eq, how does it have more power :( ")
        print("Additionally, this move has an accuracy of " + str(poke.accuracy))
        print("")
        compare_eq = (poke.power / 100) * 100
        print(name + " is " + str(compare_eq) + "% of Earthquake(ID: 84) in comparison to its power (because earthquake is op)")
    print("-------------------------------------------------------------------------------------------------------")
    print("")

def fetch_move_info(name):
    print("Fetching " + name + ".......\n")
    fetch_all_pokemon_move(name)
    fetch_pokemon_id(name)
    fetch_pokemon_power(name)

def main(): 
    print("Create by: Travis Huynh\n")
    print("Hello! Welcome to my program that allows you to search information about a specific move in Pokemon!")
    print("This program will tell you the about the specifics about each move!")
    print("It will allow you to learn how much power it has, to how weak it is compared to Earthquake! (because I love earthquake :)")
    print("What type of move do you want to learn about in Pokemon?")
    print("-------------------------------------------------------------------------------------------------------")

    while True:
        name = input()

        if name == "":
            print("Ok! You don't care anymore! bye!")
            print("Please rerun the program again if you want to know more!")
            print("")
            break

        fetch_move_info(name)

        print("")
        print("Would you like to learn more about a specific pokemon move? Or You can enter nothing to exit this program!")
        print("")
        print("-------------------------------------------------------------------------------------------------------")

if __name__ == '__main__':
    main()
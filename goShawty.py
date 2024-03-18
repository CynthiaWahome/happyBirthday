love_emoji = "\U0001F60D" 
music_emoji = "\U0001F3B5"
glass_emoji = "\U0001F942"

def happy_birthday(name):
    for c in name:
        if ord(c) in range(32, 65) or ord(c) in range(91, 97) or ord(c) > 122:
            print("Insert Letters Only")
            return()
    if name.isdigit():
        print("Error: Please enter a valid name, not a number.")
    else:
        print('.............................')
        print(love_emoji * 11)
        print(music_emoji * 11)
        print(f"Go! Go! Go! Go! Go SHAWTY! {name},")
        print("Its your BIRTHDAY! ")
        print("We gonna party like... its your BIRTHDAY! ")
        print("We gon' sip Bacardi like... its your BIRTHDAY! ")
        print("And you know we are HAPPY for you,coz its your BIRTHDAY!!! ")
        print('.............................')
        print(f"HAPPY BIRTHDAY {name}!!!!")
        print(glass_emoji * 11)
name = input("Today is your birthday! What's your name?")
happy_birthday(name)


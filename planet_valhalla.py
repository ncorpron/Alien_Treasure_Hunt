import textwrap
import os
from game_database import GameDatabase

# Initialize database
db = GameDatabase()

# -------------------------------
# Step 0 — Friendly Alien Greeting
# -------------------------------
ascii_alien = r'''
     .-""""-.
    /        \
   /_        _\
  // \      / \\
  |\__\    /__/|
   \    ||    /
    \        /
     \  __  /
      '.__.'
       |  |
       |  |
       |__|
     👽 Friendly Alien
'''
print("\n" * 2)
print(textwrap.dedent(ascii_alien))
print("Greetings traveler! Welcome to Planet Valhalla.")
print("Your mission is to save my alien friend, Ragnar.\n")

# Show game statistics
stats = db.get_game_statistics()
print(f"\n📊 Game Statistics:")
print(f"   Total games played: {stats['total_games']}")
print(f"   Wins: {stats['total_wins']}")
print(f"   Losses: {stats['total_losses']}")
print(f"   Win rate: {stats['win_rate']}%\n")

# -------------------------------
# Pause to ensure Step 0 is seen
# -------------------------------
input("Press Enter to start your adventure...")

# -------------------------------
# Helper to clear console between scenes
# -------------------------------
def clear_screen():
    if os.name == 'nt':       # Windows
        os.system('cls')
    else:                     # Mac/Linux
        os.system('clear')

# -------------------------------
# Main game loop
# -------------------------------
while True:
    # Start new game session
    session_id = db.start_game_session()
    choices_made = []

    # Step 1 — Volcano
    clear_screen()
    ascii_volcano = r'''
                           .-.
            .-""`""-.    |(@ @)
         _/`oOoOoOoOo`\_ \ \-/
        '.-=-=-=-=-=-=-.' \/ \
    jgs   `-=.=-.-=.=-'    \ /\
             ^  ^  ^       _H_ \
    '''
    print(textwrap.dedent(ascii_volcano))
    choice_1 = input("🌋 You've reached a mega volcano spewing out hot lava.\nWhich path should you take? Type 'left' or 'right': ").lower()
    choices_made.append(f"volcano: {choice_1}")

    if choice_1 == "left":
        # Step 2 — Lake
        clear_screen()
        ascii_lake = r'''
            ~~~~~     ~~~~
        ~~~    ~~~~      ~~~
       ~~~~  ☢  ~~~~   ~~~~
        ~~~~     ~~~~~~~~
             ~~~~~~~
        '''
        print(textwrap.dedent(ascii_lake))
        choice_2 = input("💧 You've come to a bubbling green lake that looks radioactive.\nDo you 'wait' or 'swim'? ").lower()
        choices_made.append(f"lake: {choice_2}")

        if choice_2 == "swim":
            # Step 3 — Single Mushroom
            clear_screen()
            ascii_mushroom = r'''
   __
  /  \
 /    \
 \    /
  \__/ 
   ||  
   ||  
   ||  
            '''
            print(textwrap.dedent(ascii_mushroom))
            choice_3 = input("Two friendly aliens give you directions.\n"
                             "Tentacle alien says 'right' to the rocky path.\n"
                             "Rainboot alien says 'left' to the mushroom trail.\n"
                             "Which do you choose? ").lower()
            choices_made.append(f"direction: {choice_3}")

            if choice_3 == "right":
                # Step 4 — Cave vs Tree
                clear_screen()
                ascii_fork = r'''
                 /\   🌲
                /  \     🌲
               /    \      🌲
              /      \       🌲
             (  CAVE  )   🌲
              \      /
               \    /
                \__/
                '''
                print(textwrap.dedent(ascii_fork))
                choice_4 = input("You reached a fork.\nDo you go into the dark 'cave' or climb the tall 'tree'? ").lower()
                choices_made.append(f"fork: {choice_4}")

                if choice_4 == "tree":
                    # Step 5 — Ragnar Rescue
                    clear_screen()
                    ascii_orb = r'''
                     .-"      "-.
                    /            \
                   |,  .-.  .-.  ,|
                   | )(_o/  \o_)( |
                   |/     /\     \|
                   (_     ^^     _)
                    \__|IIIIII|__/
                     | \IIIIII/ |
                     \          /
                      `--------`
                      👽 Ragnar trapped!
                    '''
                    print(textwrap.dedent(ascii_orb))
                    choice_5 = input("You see Ragnar trapped in a glowing orb! Do you 'pull' the lever or 'smash' the orb? ").lower()
                    choices_made.append(f"orb: {choice_5}")

                    if choice_5 == "pull":
                        clear_screen()
                        print("🎉 Victory! The orb vanishes and Ragnar is free. You saved your alien friend!")
                        print("✨ As a bonus reward, you have also received the secret to the universe: 42 ✨")
                        db.end_game_session(session_id, "win", ", ".join(choices_made))
                    else:
                        clear_screen()
                        ascii_kaboom = r'''
_.-^^---....,,--       
_--                  --_  
<                        >)
|   💥 KABOOM! 💥        | 
\._                   _./  
'--. . , ; .--'     
| |   |           
.-=||  | |=-.   
`-=#$%&%$#=-'   
| ;  :|     
Ragnar’s orb exploded! Game Over.
                        '''
                        print(textwrap.dedent(ascii_kaboom))
                        db.end_game_session(session_id, "loss", ", ".join(choices_made))
                else:
                    clear_screen()
                    ascii_beast = r'''
                 (    )
                ((((()))
                |o\~~~/o|
                (    .    )
                 \__\_/__/
                 ( Beeeast! )
            The cave monster devours you! Game Over.
                    '''
                    print(textwrap.dedent(ascii_beast))
                    db.end_game_session(session_id, "loss", ", ".join(choices_made))
            else:
                clear_screen()
                ascii_spores = r'''
          ✧･ﾟ: *✧･ﾟ:*       *:･ﾟ✧*:･ﾟ✧
         (  @   @   @   @   @   @   @  )
          ✧･ﾟ: *✧･ﾟ:*       *:･ﾟ✧*:･ﾟ✧
              🌫 You inhale spores...
            You hallucinate forever. Game Over.
                '''
                print(textwrap.dedent(ascii_spores))
                db.end_game_session(session_id, "loss", ", ".join(choices_made))
        else:
            clear_screen()
            ascii_crater = r'''
          .      '      .
       .      .     :     .    '
         '.  :  .  .'.:.'  :  '
            '. .' .'   ' .'
              '.'   🌑   '
               ( You fell into a crater )
            Game Over.
            '''
            print(textwrap.dedent(ascii_crater))
            db.end_game_session(session_id, "loss", ", ".join(choices_made))

    elif choice_1 == "right":
        clear_screen()
        ascii_lava = r'''
            (    )
             (   ) )
              ) ( (
            _______)_
         .-'---------|  
        ( CATASTROPHE|
         `-_________|
         (🔥 Lava got you!🔥)
        '''
        print(textwrap.dedent(ascii_lava))
        db.end_game_session(session_id, "loss", ", ".join(choices_made))
    else:
        clear_screen()
        print("You were gobbled up by Oork. Game over.")
        db.end_game_session(session_id, "loss", ", ".join(choices_made))

    # Play Again Option
    replay = input("\nDo you want to play again? Type 'yes' or 'no': ").lower()
    if replay != "yes":
        clear_screen()
        print("Thanks for playing Planet Valhalla! Farewell, traveler! 👽🌌")
        break

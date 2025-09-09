import textwrap

while True:
    # Step 0 — Friendly Alien Greeting
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
    print(textwrap.dedent(ascii_alien))

    print("Greetings traveler! Welcome to Planet Valhalla.")
    print("Your mission is to save my alien friend, Ragnar.\n")

    # Step 1 — Volcano
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

    if choice_1 == "left":
        # Step 2 — Lake
        ascii_lake = r'''
            ~~~~~     ~~~~
        ~~~    ~~~~      ~~~
       ~~~~  ☢  ~~~~   ~~~~
        ~~~~     ~~~~~~~~
             ~~~~~~~
        '''
        print(textwrap.dedent(ascii_lake))

        choice_2 = input("💧 You've come to a bubbling green lake that looks radioactive.\nDo you 'wait' or 'swim'? ").lower()

        if choice_2 == "swim":
            # Step 3 — Single Mushroom
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

            if choice_3 == "right":
                # Step 4 — Cave vs Tree
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

                if choice_4 == "tree":
                    # Step 5 — Ragnar Rescue
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

                    if choice_5 == "pull":
                        print("🎉 Victory! The orb vanishes and Ragnar is free. You saved your alien friend!")
                        print("✨ As a bonus reward, you have also received the secret to the universe: 42 ✨")
                    else:
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
                else:
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

            else:
                ascii_spores = r'''
          ✧･ﾟ: *✧･ﾟ:*       *:･ﾟ✧*:･ﾟ✧
         (  @   @   @   @   @   @   @  )
          ✧･ﾟ: *✧･ﾟ:*       *:･ﾟ✧*:･ﾟ✧
              🌫 You inhale spores...
            You hallucinate forever. Game Over.
                '''
                print(textwrap.dedent(ascii_spores))

        else:
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

    elif choice_1 == "right":
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

    else:
        print("You were gobbled up by Oork. Game over.")

    # Play Again Option
    replay = input("\nDo you want to play again? Type 'yes' or 'no': ").lower()
    if replay != "yes":
        print("Thanks for playing Planet Valhalla! Farewell, traveler! 👽🌌")
        break
yes

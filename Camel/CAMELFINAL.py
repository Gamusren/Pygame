import random
done = False
print("")
print("Welcome to Camel!")
print("")
print("You have stolen a camel to make your way across the great Mobi desert.")
print("The natives want their camel back and are chasing you down! Survive your")
print("desert trek and out run the natives.")
print("The natives were 20 miles behind when they found you stolen their camel")
print("            &&/.(&/%                                                                               ")
print("    ,(#%(%%      #@&.                                                                              ")
print("  %*.,     ,%%   .&   *                                     *(&&&%%%/                              ")
print("%.                 ...,                                 ,%, .%%@.*(#&@                            ")
print("/##@#   . ,     .,  ..*.                          %%&*.               (&                          ")
print(" #%     %# /*  *     ..#                   *&&%   .      . .   ..  .    *%                        ")
print("           ,,.,.,     /                %*     ..   .    ,. . ..  .   .   &&*                    ")
print("              # ,,,     %,             #    . ....  ..  .. , ..,.. .   .    ,./%&/                ")
print("               #,,,      %.         ,#  .  .  ..    .. . ,.. ..,.. ..  ..   .,*.  #%              ")
print("                 /*,.      &.       (  .   .  ...     . ..* . ..,.  .... ... . ,,.   %             ")
print("                  ,*.        %    ,#  .,      ...        ,...  ...  ..... ..   ,,      %           ")
print("                  #*,          ./*    ,. /   ...      .  .    ...  .,. .  ,,    *        %         ")
print("                   %,.                .,.(   ...      ,        .   .. ..  ..    *         &        ")
print("                    &,,               ,,%   ....      , .     .   ..     ,,     #         #.       ")
print("                    .%..              .*(   ...       ,.,,              .,.    @          %,       ")
print("                      %&               .*/   ..        ,,,,,          .,.      &         *&*       ")
print("                        %&             *(  .         / .,.,.   ...,..      %%&         &&*       ")
print("                            ,(%.         /                               /%&%@         /       ")
print("                                    #/./#(   %                      .&%.  ##(         (@@       ")
print("                                    .(%%**/#/& .    %%(         (%/       %(         .&&@/      ")
print("                                      %%#*(/(&.,    %/   .                #*       % .%&*/      ")
print("                                     #*##/*#& *    *                      %       %  % &(,     ")
print("                                     %/(((/ % *.  .*                       &*    ,*   %../     ")
print("                                      %(%/#  &,.   #                        %,   %     &       ")
print("                                       % ,/&  %#,   %                         %%  % %    #,     ")
print("                                       %   %   %.   %                          %  ## %    *%    ")
print("                                       (   (    %    %                         %/  .( .   &   ")
print("                                       .(  %    .(   %                         #/ #&  *# ..* &  ")
print("                                        &  %     #   .(                        &  .&    # ... ( ")
print("                                        %   (     %   &                        &  ,@     # .  % ")
print("                                        &   /     /%  &                       #%   %     &.. *% ")
print("                                        #, #       %  &                       %   #/      (. %  ")
print("                                       /. .*       #. (                      (,   #      .%..%  ")
print("                                       #  &         # %                      &   &       #(.%   ")
print("                                       %  #         % %                     &*  #.       ,(.&   ")
print("                                       &  &         % %                     &  *&        ## %   ")
print("                                       @  &         ( .&                   %   %         #*,&   ")
print("                                       %  &         (  %                  %.  %          &.%,   ")
print("                                       &  &         #  */                %. /&           %.%    ")
print("                                      /#  /%         # %                %( (&            .%.%    ")
print("                                     ##*,%         % .(               %%%%%          &(,*/%     ")
print("------------------------------------")
print("The game has two difficulty, ")
print("Normal mode has lazy natives who chase you for fun. Insane mode has hungry maneaters who wants to eat you alive while riding super fast horse:( ")
difficulty = input("Now please select the game difficulty | Normal | Insane | --->")
if difficulty.lower() == "normal" or difficulty.lower() == "n":
    miles_traveled = 0
    thirst = 0
    camel_tiredness = 0
    distance_traveled_by_natives = -20
    init_canteen = 5
    user_tiredness = 0
    notify = 0
    mode = 0
    buff = 0
    hand_of_god = 0
elif difficulty.lower() == "insane" or difficulty.lower() == "hard" or difficulty.lower() == "i": 
    miles_traveled = 0
    thirst = 0
    camel_tiredness = 0
    distance_traveled_by_natives = -20
    init_canteen = 3
    user_tiredness = 0
    notify = 0
    mode = 1
    buff = 0
    hand_of_god = 0
    print("Are you ready to test your luck?")


        
        
while not done:
    if mode == 1:
        hand_of_god = random.randrange(1,14)
    if hand_of_god == 1 and not done:
        print("The generous god finds your situation, he decides to play Roshambo with you")
        userinput = 0
        user = input("rock,paper,or scissor?--->")
        if user.lower() == "rock":
            userinput = 1
        if user.lower() == "paper":
            userinput = 2
        if user.lower() == "scissor":
            userinput = 3
        random_number = random.randrange(0, 3)
        if random_number == 0 and userinput == 3:
            print("You lose!")
        if random_number == 0 and userinput == 2:
            print("You Win!")
            buff = 1
        if random_number == 0 and userinput == 1:
            print("It's a tie")

        if random_number == 1 and userinput == 3:
            print("You Win!")
            buff = 1
        if random_number == 1 and userinput == 2:
            print("It's a tie")
        if random_number == 1 and userinput == 1:
            print("You lose!")

        if random_number == 2 and userinput == 3:
            print("It's a tie")
        if random_number == 2 and userinput == 2:
            print("You Lose!")
        if random_number == 2 and userinput == 1:
            print("You Win!")
            buff = 1
        
    if buff == 1 and not done:
        dice = random.randrange(1,6)
    freeze = 0
    while buff == 1 and not done and dice == 1:
        init_canteen += 3
        buff -= 1
        print("The god gives you three bottle of canteen.")

    while buff == 1 and not done and dice == 2:
        miles_traveled += 70
        buff -= 1
        print("The god carries you over 70 miles")

    while buff == 1 and not done and dice == 3:
        camel_tiredness -= 10
        buff -= 1
        print("The god makes your camel tireless")

    while buff == 1 and not done and dice == 4:
        distance_traveled_by_natives -= 70
        buff -= 1
        print("The god pushes the natives 70 miles back")

    while buff == 1 and not done and dice == 5:
        freeze = 3
        buff -= 1
        print("The god freezes the natives for three rounds")
    print("------------------------------------")
    print("What's next?")
    print("")
    print("A. Drink from your canteen.")
    print("B. Ahead moderate speed.")
    print("C. Ahead full speed.")
    print("D. Stop for the night.")
    print("E. Status check.")
    print("Q. Quit.")
    

    oasis = random.randrange(1, 21)
    oasis_pro = random.randrange(1, 41)
    if oasis == 5 and camel_tiredness <= 8 and mode == 0:
        thirst = 0
        camel_tiredness = 0
        init_canteen = 3
        print("You found an oasis! The camel rested, and you filled all your canteens and drank the fresh water!")
    if oasis == 5 and camel_tiredness > 8 and mode == 0:
        thirst = 0
        init_canteen = 3
        user_tiredness = 0
        print("You found an oasis! You had a rest and you filled all your canteens and drank the fresh water!")
    if oasis_pro == 5 and camel_tiredness <= 8 and mode == 1:
        thirst = 0
        camel_tiredness = 0
        init_canteen = 3
        print("You found an oasis! The camel rested, and you filled all your canteens and drank the fresh water!")
    if oasis_pro == 5 and camel_tiredness > 8 and mode == 1:
        thirst = 0
        init_canteen = 3
        user_tiredness = 0
        print("You found an oasis! You had a rest and you filled all your canteens and drank the fresh water!")
    if not done and thirst > 4:
        print("You are thirsty")
    elif thirst > 6:
        print("You died of thirst!")
        done = True
    if camel_tiredness > 5 and camel_tiredness <= 8:
        print("Your camel is getting tired.")
    elif camel_tiredness > 8 and notify == 0:
        print("Your camel is dead.")
        print("you are now running by your own!")
        notify += 1
    if user_tiredness > 5 and user_tiredness <= 9:
        print("You feel really tired.")
    elif user_tiredness > 9:
        print("You are dead due to tiredness")
        print("                                    ,/###/,                                    ")
        print("                              #@@@@@@@@@@@@@@@@@%                              ")
        print("                           @@@@@@@@@@@@@@@@@@@@@@@@@                           ")
        print("                        &@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&                        ")
        print("                      @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                      ")
        print("                    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                    ")
        print("                   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@    ")
        print("                   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                   ")
        print("      @@@@@@%     &@&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@     %@@@@@@      ")
        print("    @@@@@@@@@    @@@@#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#@@@@    @@@@@@@@@     ")
        print("   /@@@@@@@@@@@,  @@@@@@&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&@@@@@  (@@@@@@@@@@@(   ")
        print("  @@@@@@@@@@@@@@@ @@@@@*@@&@@@@@@@@@@@@@@@@@@@@@@@@@@@@.@@@@@ @@@@@@@@@@@@@@@. ")
        print("  @@@@@@@@@@@@@@@ @@@@(@@@@@&@@@@@@@@@@@@@@@@@@@@@@@@@@@/@@@@ @@@@@@@@@@@@@@@  ")
        print("   @@@@@@@@@@@@@@ @@@%@@@@@@@@&@@@@@@@@@@@@@@@@@@@@@@@@@@#@@@ @@@@@@@@@@@@@@   ")
        print("    @@@@@@@@@@@@@@ @@.@@@@%      @@@@@@@@@@@@@      %@@@@,@@ @@@@@@@@@@@@@@    ")
        print("               ,@@ @,@@@           %@@@@@@@%           @@@.@ @@.               ")
        print("                   #.@&             %@@@@@&             @@,#                   ")
        print("                   .&&@             &@@@@@@             @&&  ,                 ")
        print("                  /@@@@            @@@@@&&@&            @@@@/                  ")
        print("                  ,@@&@@          &@@@&,,&.&&          @@&@& ,                 ")
        print("                    @@@@@@@@@@@@@@@@   @   @@@@@@@@@@@@@@@@                    ")
        print("                     @@@@@@@@@@@@@@.   @    @@@@@@@@@@@@@@.                    ")
        print("                       /@@@@@@@@@@@(  ,@*  /@@@@@@@@@@@,                       ")
        print("                        @@@   @@@@@@@,@@@,@@@@@@@   @@@                        ")
        print("                   #@@@ @@@,  @@@@@@@@@@@@@@@@@@@  ,@@@ @@@%                   ")
        print("            *#@@@@@@@@&,&@@@( /@(%/@@@@@@@@@/&*@( (@@@@ &@@@@@@@@#*            ")
        print("   ,@@@@@@@@@@@@@@@@@@@ @@@@@@(@&%@,@,@,@*@/@&@@(@@@@@@ @@@@@@@@@@@@@@@@@@@,   ")
        print("   @@@@@@@@@@@@@@@@@&@@  #@@@@@/@((@@@@.@@@@((@%@@@@@% ,@@@@@@@@@@@@@@@@@@@@.  ")
        print("   @@@@@@@@@@@@@@@&@      /@@@@@@/,@@%@,@%@@*/@@@@@@(      @@@@@@@@@@@@@@@@@   ")
        print("     @@@@@@@@@@@@(         @@@@@@@@&*/@ @(*&@@@@@@@@         /@@@@@@@@@@@@     ")
        print("      @@@@@@@@@(            @@@@@@@@@@@@@@@@@@@@@@@            %@@@@@@@@@.     ")
        print("      @@@@@@&@                @@@@@@@@@@@@@@@@@@@                @@@@@@@@      ")
        print("                                .@@@@@@@@@@@@@,                                ")
        done = True
    elif (miles_traveled - distance_traveled_by_natives) < 15 and not done:
        print("The natives are getting close!")
    elif (miles_traveled - distance_traveled_by_natives) < 6 and not done:
        print("You can hear the natives coming from your back!")
    if thirst <= 6:
        if miles_traveled > 200 and not done:
            print("  %%%%%%%%                  .,((((((((((((((((/((*.                  %%%%%%%%  ")
            print(" %%%%%%%%%%%%         (((((((((((((((((((((((((((((((((((((       %%%%%%%%%%%% ")
            print("%%%%%%%%%%%%%%%  ,(((((((((((((((((((((((((((((((((((((((((((((#%%%%%%%%%%%%%%#")
            print("%%%%%%%%%%%%%%%%%#(((((((((((((((((((((((((((((((((((((((((((/#&%%%%%%%%%%%%%%%")
            print("%%%%%%%%%%%%%%%%%&&&&&&%#(((((((((((((((((((((((((((((/(#%&&&&&&%%%%%%%%%%%%%%%")
            print("%%%%%%%%%%%%%%%%%&&&&&&&&&&&&&&&&&&&&&%%%%%%&&&&&&&&&&&&&&&&&&&&%%%%%%%%%%%%%%%")
            print("%%%%%%%%%%%#%%%%%&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&%%%%%%%%%%%%%%%%")
            print("%%%%%%%%%%    (%%&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&%%    %%%%%%%%%%")
            print("%%%%%%%%%&      #&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&      @%%%%%%%%%")
            print("%%%%%%%%%%       &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&      /%%%%%%%%%")
            print("%%%%%%%%%%       %&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&%      %%%%%%%%%%")
            print("%%%%%%%%%%%      @&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&      %%%%%%%%%%&")
            print(" #%%%%%%%%%%      &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&      %%%%%%%%%%# ")
            print("  %%%%%%%%%%%     &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&%     %%%%%%%%%%%  ")
            print("   %%%%%%%%%%%#    &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&    %%%%%%%%%%%%   ")
            print("    %%%%%%%%%%%#   &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&    %%%%%%%%%%%#    ")
            print("     @%%%%%%%%%%%*  %&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&  .%%%%%%%%%%%@  ")
            print("       #%%%%%%%%%%%  (&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&%  %%%%%%%%%%%&       ")
            print("         (%%%%%%%%%%  &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&   %%%%%%%%%%@         ")
            print("           (%%%%%%%%%  @&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&   %%%%%%%%%@           ")
            print("             @%%%%%%%%   %&&&&&&&&&&&&&&&&&&&&&&&&&&&    %%%%%%%%              ")
            print("               %%%%%%%%    %&&&&&&&&&&&&&&&&&&&&&&&@    %%%%%%%@        ")
            print("                 #%%%%%%     /%&&&&&&&&&&&&&&&&&&      (%%%%%#                 ")
            print("                  %%%%%%         &%&&&&&&&&&%          %%%%%%                  ")
            print("                  %%%%%@            #%%%%#             %%%%%%                  ")
            print("                 #%%%&              #%%%%%               @%%%(                 ")
            print("               ,#                   #%%%%#                    #                ")
            print("                                   .#%%%%%,                                    ")
            print("                                #&&&&&&&&&&&&&                                 ")
            print("                                %&&&&&&&&&&&&&%                                ")
            print("                                   %%&&&&&%#                                   ")
            print("                                   #%%%%%%%                                    ")
            print("                                   %%%%%%%%@                                   ")
            print("                                   %%%%%%%%#                                   ")
            print("                                  #%%%%%%%%%@                                  ")
            print("                                  %%%%%%%%%%%                                  ")
            print("                                 %%%%%%%%%%%%#                                 ")
            print("                               &&&&&&&&&&&&&&&&&&                              ")
            print("                              &&&&%%%%%%%%%%%%%&&&                             ")
            print("                You have out of the dessert, congratulations!                    ")
            done = True
    print("")
    print("------------------------------------")
    if not done:
        userchoice = input("Make your choice:---> ")
    print("---------------------------------------------------------")
    if userchoice.upper() == "Q":
        done = True
    elif userchoice.upper() == "E":
        freeze -= 1
        if freeze <= 0:
            random_progress_native = random.randrange(7, 9)
            distance_traveled_by_natives += random_progress_native
        print("Miles traveled:", miles_traveled," miles.")
        print("Drinks in canteen:", init_canteen, " bottles")
        print("The natives are", miles_traveled - distance_traveled_by_natives, " miles behind you.")
        if camel_tiredness > 8:
            print("Your tiredness:", user_tiredness)
    elif userchoice.upper() == "D":
        freeze -= 1
        if camel_tiredness <= 8 and not done:
            camel_tiredness = 0
            print("Camel is happy.")
            if freeze <= 0:
                if mode == 0:
                    random_progress_native = random.randrange(5,13)
                    distance_traveled_by_natives += random_progress_native
                if mode == 1:
                    random_progress_native = random.randrange(13,25)
                    distance_traveled_by_natives += random_progress_native
        if camel_tiredness > 8 and not done:
            user_tiredness = 0
            print("You rested a bit.")
            if freeze <= 0:
                if mode == 0:
                    random_progress_native = random.randrange(5,13)
                    distance_traveled_by_natives += random_progress_native
                if mode == 1:
                    random_progress_native = random.randrange(13, 25)
                    distance_traveled_by_natives += random_progress_native
    elif userchoice.upper() == "C":
        freeze -= 1
        if camel_tiredness <= 8 and not done:
            random_progress_user = random.randrange(15,21)
            random_tiredness = random.randrange(1,4)
            miles_traveled += random_progress_user
            thirst += 1
            camel_tiredness += random_tiredness
            if freeze <= 0:
                if mode == 0:
                    random_progress_native = random.randrange(5,13)
                    distance_traveled_by_natives += random_progress_native
                if mode == 1:
                    random_progress_native = random.randrange(13,25)
                    distance_traveled_by_natives += random_progress_native
            print("|You have traveled:", random_progress_user, " miles.|")
        if camel_tiredness > 8 and not done:
            random_progress_user = random.randrange(3, 6)
            random_user_tiredness = random.randrange(3, 5)
            miles_traveled += random_progress_user
            thirst += 4
            user_tiredness += random_user_tiredness
            if freeze <= 0:
                if mode == 0:
                    random_progress_native = random.randrange(5,13)
                    distance_traveled_by_natives += random_progress_native
                if mode == 1:
                    random_progress_native = random.randrange(13,25)
                    distance_traveled_by_natives += random_progress_native
            print("|You have traveled:", random_progress_user, " miles.|")
    elif userchoice.upper() == "B":
        freeze -= 1
        if camel_tiredness <= 8 and not done:
            random_progress_user = random.randrange(5,13)
            miles_traveled += random_progress_user
            thirst += 1
            camel_tiredness += 1
            if freeze <= 0:
                if mode == 0:
                    random_progress_native = random.randrange(5,13)
                    distance_traveled_by_natives += random_progress_native
                if mode == 1:
                    random_progress_native = random.randrange(13,25)
                    distance_traveled_by_natives += random_progress_native
            print("|You have traveled:", random_progress_user, " miles.|")
        elif camel_tiredness > 8 and not done:
            random_progress_user = random.randrange(1, 3)
            miles_traveled += random_progress_user
            thirst += 2
            if freeze <= 0:
                if mode == 0:
                    random_progress_native = random.randrange(5,13)
                    distance_traveled_by_natives += random_progress_native
                if mode == 1:
                    random_progress_native = random.randrange(13,25)
                    distance_traveled_by_natives += random_progress_native
            print("|You have traveled:", random_progress_user, " miles.|")
    elif userchoice.upper() == "A":
        freeze -= 1
        if init_canteen > 0 and not done:
            init_canteen -= 1
            thirst = 0
            print("You drank your canteen, there are ", init_canteen, "left")
            if freeze <= 0:
                random_progress_native = random.randrange(3, 7)
                distance_traveled_by_natives += random_progress_native
        elif init_canteen <= 0 and not done:
            print("Oops, No canteen left! Make your choice again.")
    if (miles_traveled == distance_traveled_by_natives or miles_traveled < distance_traveled_by_natives) and not done:
        print("                                    ,/###/,                                    ")
        print("                              #@@@@@@@@@@@@@@@@@%                              ")
        print("                           @@@@@@@@@@@@@@@@@@@@@@@@@                           ")
        print("                        &@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&                        ")
        print("                      @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                      ")
        print("                    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                    ")
        print("                   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@    ")
        print("                   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                   ")
        print("      @@@@@@%     &@&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@     %@@@@@@      ")
        print("    @@@@@@@@@    @@@@#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#@@@@    @@@@@@@@@     ")
        print("   /@@@@@@@@@@@,  @@@@@@&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&@@@@@  (@@@@@@@@@@@(   ")
        print("  @@@@@@@@@@@@@@@ @@@@@*@@&@@@@@@@@@@@@@@@@@@@@@@@@@@@@.@@@@@ @@@@@@@@@@@@@@@. ")
        print("  @@@@@@@@@@@@@@@ @@@@(@@@@@&@@@@@@@@@@@@@@@@@@@@@@@@@@@/@@@@ @@@@@@@@@@@@@@@  ")
        print("   @@@@@@@@@@@@@@ @@@%@@@@@@@@&@@@@@@@@@@@@@@@@@@@@@@@@@@#@@@ @@@@@@@@@@@@@@   ")
        print("    @@@@@@@@@@@@@@ @@.@@@@%      @@@@@@@@@@@@@      %@@@@,@@ @@@@@@@@@@@@@@    ")
        print("               ,@@ @,@@@           %@@@@@@@%           @@@.@ @@.               ")
        print("                   #.@&             %@@@@@&             @@,#                   ")
        print("                   .&&@             &@@@@@@             @&&  ,                 ")
        print("                  /@@@@            @@@@@&&@&            @@@@/                  ")
        print("                  ,@@&@@          &@@@&,,&.&&          @@&@& ,                 ")
        print("                    @@@@@@@@@@@@@@@@   @   @@@@@@@@@@@@@@@@                    ")
        print("                     @@@@@@@@@@@@@@.   @    @@@@@@@@@@@@@@.                    ")
        print("                       /@@@@@@@@@@@(  ,@*  /@@@@@@@@@@@,                       ")
        print("                        @@@   @@@@@@@,@@@,@@@@@@@   @@@                        ")
        print("                   #@@@ @@@,  @@@@@@@@@@@@@@@@@@@  ,@@@ @@@%                   ")
        print("            *#@@@@@@@@&,&@@@( /@(%/@@@@@@@@@/&*@( (@@@@ &@@@@@@@@#*            ")
        print("   ,@@@@@@@@@@@@@@@@@@@ @@@@@@(@&%@,@,@,@*@/@&@@(@@@@@@ @@@@@@@@@@@@@@@@@@@,   ")
        print("   @@@@@@@@@@@@@@@@@&@@  #@@@@@/@((@@@@.@@@@((@%@@@@@% ,@@@@@@@@@@@@@@@@@@@@.  ")
        print("   @@@@@@@@@@@@@@@&@      /@@@@@@/,@@%@,@%@@*/@@@@@@(      @@@@@@@@@@@@@@@@@   ")
        print("     @@@@@@@@@@@@(         @@@@@@@@&*/@ @(*&@@@@@@@@         /@@@@@@@@@@@@     ")
        print("      @@@@@@@@@(            @@@@@@@@@@@@@@@@@@@@@@@            %@@@@@@@@@.     ")
        print("      @@@@@@&@                @@@@@@@@@@@@@@@@@@@                @@@@@@@@      ")
        print("                                .@@@@@@@@@@@@@,                                ")
        print("                    You have been caught by the natives!                       ")
        done = True



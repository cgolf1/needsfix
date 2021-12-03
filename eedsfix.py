answer = input("How similar to Douglas are you quiz!!! Play? (y/n)")
score = 0
if answer == "y":
    print("[A]: making silly little drawings")
    print("[B]: playing a silly little rpg game")
    print("[C]: playing a silly little block game")
    print("[D]: do silly little meditation techniques")
    answer = input("What is your ideal past time? Choose from the choices above. (A/B/C/D)")
    if answer.upper() == "A":
        score = score+2
        print("[A]: purple")
        print("[B]: black")
        print("[C]: blue")
        print("[D]: maroon")
        answer = input("Which is the best color out of the choices above? (A/B/C/D)")
        if answer.upper() == "A":
            score = score+1
            print("[A]: ravioli")
            print("[B]: pasta")
            print("[C]: burger")
            print("[D]: shrimp")
            answer = input("What is your favorite food out of the choices above? (A/B/C/D)")
            if answer.upper() == "A":
                score = score + 2
                print("[A]: summer")
                print("[B]: spring")
                print("[C]: fall")
                print("[D]: winter")
                answer = input("What is your favorite season out of the choices above? (A/B/C/D)")
                if answer.upper() == "A":
                    score = score + 2
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score+2
                    elif answer.upper() == "B":
                        score = score+1
                    elif answer.upper() == "C":
                        score = score+5
                    elif answer.upper() == "D":
                        score = score+3
                elif answer.upper() == "B":
                    score = score + 1
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "C":
                    score = score + 5
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "D":
                    score = score + 3
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
            elif answer.upper() == "B":
                score = score + 1
                print("[A]: summer")
                print("[B]: spring")
                print("[C]: fall")
                print("[D]: winter")
                answer = input("What is your favorite season out of the choices above? (A/B/C/D)")
                if answer.upper() == "A":
                    score = score + 2
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score+2
                    elif answer.upper() == "B":
                        score = score+1
                    elif answer.upper() == "C":
                        score = score+5
                    elif answer.upper() == "D":
                        score = score+3
                elif answer.upper() == "B":
                    score = score + 1
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "C":
                    score = score + 5
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "D":
                    score = score + 3
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
            elif answer.upper() == "C":
                score = score + 5
                print("[A]: summer")
                print("[B]: spring")
                print("[C]: fall")
                print("[D]: winter")
                answer = input("What is your favorite season out of the choices above? (A/B/C/D)")
                if answer.upper() == "A":
                    score = score + 2
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score+2
                    elif answer.upper() == "B":
                        score = score+1
                    elif answer.upper() == "C":
                        score = score+5
                    elif answer.upper() == "D":
                        score = score+3
                elif answer.upper() == "B":
                    score = score + 1
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "C":
                    score = score + 5
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "D":
                    score = score + 3
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
            elif answer.upper() == "D":
                score = score + 3
                print("[A]: summer")
                print("[B]: spring")
                print("[C]: fall")
                print("[D]: winter")
                answer = input("What is your favorite season out of the choices above? (A/B/C/D)")
                if answer.upper() == "A":
                    score = score + 2
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score+2
                    elif answer.upper() == "B":
                        score = score+1
                    elif answer.upper() == "C":
                        score = score+5
                    elif answer.upper() == "D":
                        score = score+3
                elif answer.upper() == "B":
                    score = score + 1
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "C":
                    score = score + 5
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "D":
                    score = score + 3
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
        elif answer.upper() == "B":
            score = score+3
            print("[A]: ravioli")
            print("[B]: pasta")
            print("[C]: burger")
            print("[D]: shrimp")
            answer = input("What is your favorite food out of the choices above? (A/B/C/D)")
            if answer.upper() == "A":
                score = score + 2
                print("[A]: summer")
                print("[B]: spring")
                print("[C]: fall")
                print("[D]: winter")
                answer = input("What is your favorite season out of the choices above? (A/B/C/D)")
                if answer.upper() == "A":
                    score = score + 2
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score+2
                    elif answer.upper() == "B":
                        score = score+1
                    elif answer.upper() == "C":
                        score = score+5
                    elif answer.upper() == "D":
                        score = score+3
                elif answer.upper() == "B":
                    score = score + 1
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "C":
                    score = score + 5
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "D":
                    score = score + 3
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
            elif answer.upper() == "B":
                score = score + 1
                print("[A]: summer")
                print("[B]: spring")
                print("[C]: fall")
                print("[D]: winter")
                answer = input("What is your favorite season out of the choices above? (A/B/C/D)")
                if answer.upper() == "A":
                    score = score + 2
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score+2
                    elif answer.upper() == "B":
                        score = score+1
                    elif answer.upper() == "C":
                        score = score+5
                    elif answer.upper() == "D":
                        score = score+3
                elif answer.upper() == "B":
                    score = score + 1
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "C":
                    score = score + 5
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "D":
                    score = score + 3
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
            elif answer.upper() == "C":
                score = score + 5
                print("[A]: summer")
                print("[B]: spring")
                print("[C]: fall")
                print("[D]: winter")
                answer = input("What is your favorite season out of the choices above? (A/B/C/D)")
                if answer.upper() == "A":
                    score = score + 2
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score+2
                    elif answer.upper() == "B":
                        score = score+1
                    elif answer.upper() == "C":
                        score = score+5
                    elif answer.upper() == "D":
                        score = score+3
                elif answer.upper() == "B":
                    score = score + 1
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "C":
                    score = score + 5
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "D":
                    score = score + 3
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
            elif answer.upper() == "D":
                score = score + 3
                print("[A]: summer")
                print("[B]: spring")
                print("[C]: fall")
                print("[D]: winter")
                answer = input("What is your favorite season out of the choices above? (A/B/C/D)")
                if answer.upper() == "A":
                    score = score + 2
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score+2
                    elif answer.upper() == "B":
                        score = score+1
                    elif answer.upper() == "C":
                        score = score+5
                    elif answer.upper() == "D":
                        score = score+3
                elif answer.upper() == "B":
                    score = score + 1
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "C":
                    score = score + 5
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "D":
                    score = score + 3
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
        elif answer.upper() == "C":
            score = score+5
            print("[A]: ravioli")
            print("[B]: pasta")
            print("[C]: burger")
            print("[D]: shrimp")
            answer = input("What is your favorite food out of the choices above? (A/B/C/D)")
            if answer.upper() == "A":
                score = score + 2
                print("[A]: summer")
                print("[B]: spring")
                print("[C]: fall")
                print("[D]: winter")
                answer = input("What is your favorite season out of the choices above? (A/B/C/D)")
                if answer.upper() == "A":
                    score = score + 2
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score+2
                    elif answer.upper() == "B":
                        score = score+1
                    elif answer.upper() == "C":
                        score = score+5
                    elif answer.upper() == "D":
                        score = score+3
                elif answer.upper() == "B":
                    score = score + 1
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "C":
                    score = score + 5
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "D":
                    score = score + 3
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
            elif answer.upper() == "B":
                score = score + 1
                print("[A]: summer")
                print("[B]: spring")
                print("[C]: fall")
                print("[D]: winter")
                answer = input("What is your favorite season out of the choices above? (A/B/C/D)")
                if answer.upper() == "A":
                    score = score + 2
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score+2
                    elif answer.upper() == "B":
                        score = score+1
                    elif answer.upper() == "C":
                        score = score+5
                    elif answer.upper() == "D":
                        score = score+3
                elif answer.upper() == "B":
                    score = score + 1
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "C":
                    score = score + 5
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "D":
                    score = score + 3
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
            elif answer.upper() == "C":
                score = score + 5
                print("[A]: summer")
                print("[B]: spring")
                print("[C]: fall")
                print("[D]: winter")
                answer = input("What is your favorite season out of the choices above? (A/B/C/D)")
                if answer.upper() == "A":
                    score = score + 2
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score+2
                    elif answer.upper() == "B":
                        score = score+1
                    elif answer.upper() == "C":
                        score = score+5
                    elif answer.upper() == "D":
                        score = score+3
                elif answer.upper() == "B":
                    score = score + 1
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "C":
                    score = score + 5
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "D":
                    score = score + 3
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
            elif answer.upper() == "D":
                score = score + 3
                print("[A]: summer")
                print("[B]: spring")
                print("[C]: fall")
                print("[D]: winter")
                answer = input("What is your favorite season out of the choices above? (A/B/C/D)")
                if answer.upper() == "A":
                    score = score + 2
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score+2
                    elif answer.upper() == "B":
                        score = score+1
                    elif answer.upper() == "C":
                        score = score+5
                    elif answer.upper() == "D":
                        score = score+3
                elif answer.upper() == "B":
                    score = score + 1
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "C":
                    score = score + 5
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "D":
                    score = score + 3
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
        elif answer.upper() == "D":
            score = score+2
            print("[A]: ravioli")
            print("[B]: pasta")
            print("[C]: burger")
            print("[D]: shrimp")
            answer = input("What is your favorite food out of the choices above? (A/B/C/D)")
            if answer.upper() == "A":
                score = score + 2
                print("[A]: summer")
                print("[B]: spring")
                print("[C]: fall")
                print("[D]: winter")
                answer = input("What is your favorite season out of the choices above? (A/B/C/D)")
                if answer.upper() == "A":
                    score = score + 2
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score+2
                    elif answer.upper() == "B":
                        score = score+1
                    elif answer.upper() == "C":
                        score = score+5
                    elif answer.upper() == "D":
                        score = score+3
                elif answer.upper() == "B":
                    score = score + 1
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "C":
                    score = score + 5
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "D":
                    score = score + 3
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
            elif answer.upper() == "B":
                score = score + 1
                print("[A]: summer")
                print("[B]: spring")
                print("[C]: fall")
                print("[D]: winter")
                answer = input("What is your favorite season out of the choices above? (A/B/C/D)")
                if answer.upper() == "A":
                    score = score + 2
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score+2
                    elif answer.upper() == "B":
                        score = score+1
                    elif answer.upper() == "C":
                        score = score+5
                    elif answer.upper() == "D":
                        score = score+3
                elif answer.upper() == "B":
                    score = score + 1
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "C":
                    score = score + 5
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "D":
                    score = score + 3
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
            elif answer.upper() == "C":
                score = score + 5
                print("[A]: summer")
                print("[B]: spring")
                print("[C]: fall")
                print("[D]: winter")
                answer = input("What is your favorite season out of the choices above? (A/B/C/D)")
                if answer.upper() == "A":
                    score = score + 2
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score+2
                    elif answer.upper() == "B":
                        score = score+1
                    elif answer.upper() == "C":
                        score = score+5
                    elif answer.upper() == "D":
                        score = score+3
                elif answer.upper() == "B":
                    score = score + 1
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "C":
                    score = score + 5
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "D":
                    score = score + 3
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
            elif answer.upper() == "D":
                score = score + 3
                print("[A]: summer")
                print("[B]: spring")
                print("[C]: fall")
                print("[D]: winter")
                answer = input("What is your favorite season out of the choices above? (A/B/C/D)")
                if answer.upper() == "A":
                    score = score + 2
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score+2
                    elif answer.upper() == "B":
                        score = score+1
                    elif answer.upper() == "C":
                        score = score+5
                    elif answer.upper() == "D":
                        score = score+3
                elif answer.upper() == "B":
                    score = score + 1
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "C":
                    score = score + 5
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "D":
                    score = score + 3
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
    elif answer.upper() == "B":
        score = score+5
        print("[A]: purple")
        print("[B]: black")
        print("[C]: blue")
        print("[D]: maroon")
        answer = input("Which is the best color out of the choices above? (A/B/C/D)")
        if answer.upper() == "A":
            score = score + 1
            print("[A]: ravioli")
            print("[B]: pasta")
            print("[C]: burger")
            print("[D]: shrimp")
            answer = input("What is your favorite food out of the choices above? (A/B/C/D)")
            if answer.upper() == "A":
                score = score + 2
                print("[A]: summer")
                print("[B]: spring")
                print("[C]: fall")
                print("[D]: winter")
                answer = input("What is your favorite season out of the choices above? (A/B/C/D)")
                if answer.upper() == "A":
                    score = score + 2
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score+2
                    elif answer.upper() == "B":
                        score = score+1
                    elif answer.upper() == "C":
                        score = score+5
                    elif answer.upper() == "D":
                        score = score+3
                elif answer.upper() == "B":
                    score = score + 1
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "C":
                    score = score + 5
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "D":
                    score = score + 3
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
            elif answer.upper() == "B":
                score = score + 1
                print("[A]: summer")
                print("[B]: spring")
                print("[C]: fall")
                print("[D]: winter")
                answer = input("What is your favorite season out of the choices above? (A/B/C/D)")
                if answer.upper() == "A":
                    score = score + 2
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score+2
                    elif answer.upper() == "B":
                        score = score+1
                    elif answer.upper() == "C":
                        score = score+5
                    elif answer.upper() == "D":
                        score = score+3
                elif answer.upper() == "B":
                    score = score + 1
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "C":
                    score = score + 5
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "D":
                    score = score + 3
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
            elif answer.upper() == "C":
                score = score + 5
                print("[A]: summer")
                print("[B]: spring")
                print("[C]: fall")
                print("[D]: winter")
                answer = input("What is your favorite season out of the choices above? (A/B/C/D)")
                if answer.upper() == "A":
                    score = score + 2
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score+2
                    elif answer.upper() == "B":
                        score = score+1
                    elif answer.upper() == "C":
                        score = score+5
                    elif answer.upper() == "D":
                        score = score+3
                elif answer.upper() == "B":
                    score = score + 1
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "C":
                    score = score + 5
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "D":
                    score = score + 3
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
            elif answer.upper() == "D":
                score = score + 3
                print("[A]: summer")
                print("[B]: spring")
                print("[C]: fall")
                print("[D]: winter")
                answer = input("What is your favorite season out of the choices above? (A/B/C/D)")
                if answer.upper() == "A":
                    score = score + 2
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score+2
                    elif answer.upper() == "B":
                        score = score+1
                    elif answer.upper() == "C":
                        score = score+5
                    elif answer.upper() == "D":
                        score = score+3
                elif answer.upper() == "B":
                    score = score + 1
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "C":
                    score = score + 5
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "D":
                    score = score + 3
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
        elif answer.upper() == "B":
            score = score + 3
            print("[A]: ravioli")
            print("[B]: pasta")
            print("[C]: burger")
            print("[D]: shrimp")
            answer = input("What is your favorite food out of the choices above? (A/B/C/D)")
            if answer.upper() == "A":
                score = score + 2
                print("[A]: summer")
                print("[B]: spring")
                print("[C]: fall")
                print("[D]: winter")
                answer = input("What is your favorite season out of the choices above? (A/B/C/D)")
                if answer.upper() == "A":
                    score = score + 2
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score+2
                    elif answer.upper() == "B":
                        score = score+1
                    elif answer.upper() == "C":
                        score = score+5
                    elif answer.upper() == "D":
                        score = score+3
                elif answer.upper() == "B":
                    score = score + 1
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "C":
                    score = score + 5
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "D":
                    score = score + 3
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
            elif answer.upper() == "B":
                score = score + 1
                print("[A]: summer")
                print("[B]: spring")
                print("[C]: fall")
                print("[D]: winter")
                answer = input("What is your favorite season out of the choices above? (A/B/C/D)")
                if answer.upper() == "A":
                    score = score + 2
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score+2
                    elif answer.upper() == "B":
                        score = score+1
                    elif answer.upper() == "C":
                        score = score+5
                    elif answer.upper() == "D":
                        score = score+3
                elif answer.upper() == "B":
                    score = score + 1
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "C":
                    score = score + 5
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "D":
                    score = score + 3
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
            elif answer.upper() == "C":
                score = score + 5
                print("[A]: summer")
                print("[B]: spring")
                print("[C]: fall")
                print("[D]: winter")
                answer = input("What is your favorite season out of the choices above? (A/B/C/D)")
                if answer.upper() == "A":
                    score = score + 2
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score+2
                    elif answer.upper() == "B":
                        score = score+1
                    elif answer.upper() == "C":
                        score = score+5
                    elif answer.upper() == "D":
                        score = score+3
                elif answer.upper() == "B":
                    score = score + 1
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "C":
                    score = score + 5
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "D":
                    score = score + 3
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
            elif answer.upper() == "D":
                score = score + 3
                print("[A]: summer")
                print("[B]: spring")
                print("[C]: fall")
                print("[D]: winter")
                answer = input("What is your favorite season out of the choices above? (A/B/C/D)")
                if answer.upper() == "A":
                    score = score + 2
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score+2
                    elif answer.upper() == "B":
                        score = score+1
                    elif answer.upper() == "C":
                        score = score+5
                    elif answer.upper() == "D":
                        score = score+3
                elif answer.upper() == "B":
                    score = score + 1
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "C":
                    score = score + 5
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "D":
                    score = score + 3
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
        elif answer.upper() == "C":
            score = score + 5
            print("[A]: ravioli")
            print("[B]: pasta")
            print("[C]: burger")
            print("[D]: shrimp")
            answer = input("What is your favorite food out of the choices above? (A/B/C/D)")
            if answer.upper() == "A":
                score = score + 2
                print("[A]: summer")
                print("[B]: spring")
                print("[C]: fall")
                print("[D]: winter")
                answer = input("What is your favorite season out of the choices above? (A/B/C/D)")
                if answer.upper() == "A":
                    score = score + 2
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score+2
                    elif answer.upper() == "B":
                        score = score+1
                    elif answer.upper() == "C":
                        score = score+5
                    elif answer.upper() == "D":
                        score = score+3
                elif answer.upper() == "B":
                    score = score + 1
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "C":
                    score = score + 5
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "D":
                    score = score + 3
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
            elif answer.upper() == "B":
                score = score + 1
                print("[A]: summer")
                print("[B]: spring")
                print("[C]: fall")
                print("[D]: winter")
                answer = input("What is your favorite season out of the choices above? (A/B/C/D)")
                if answer.upper() == "A":
                    score = score + 2
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score+2
                    elif answer.upper() == "B":
                        score = score+1
                    elif answer.upper() == "C":
                        score = score+5
                    elif answer.upper() == "D":
                        score = score+3
                elif answer.upper() == "B":
                    score = score + 1
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "C":
                    score = score + 5
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "D":
                    score = score + 3
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
            elif answer.upper() == "C":
                score = score + 5
                print("[A]: summer")
                print("[B]: spring")
                print("[C]: fall")
                print("[D]: winter")
                answer = input("What is your favorite season out of the choices above? (A/B/C/D)")
                if answer.upper() == "A":
                    score = score + 2
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score+2
                    elif answer.upper() == "B":
                        score = score+1
                    elif answer.upper() == "C":
                        score = score+5
                    elif answer.upper() == "D":
                        score = score+3
                elif answer.upper() == "B":
                    score = score + 1
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "C":
                    score = score + 5
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "D":
                    score = score + 3
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
            elif answer.upper() == "D":
                score = score + 3
                print("[A]: summer")
                print("[B]: spring")
                print("[C]: fall")
                print("[D]: winter")
                answer = input("What is your favorite season out of the choices above? (A/B/C/D)")
                if answer.upper() == "A":
                    score = score + 2
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score+2
                    elif answer.upper() == "B":
                        score = score+1
                    elif answer.upper() == "C":
                        score = score+5
                    elif answer.upper() == "D":
                        score = score+3
                elif answer.upper() == "B":
                    score = score + 1
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "C":
                    score = score + 5
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "D":
                    score = score + 3
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
        elif answer.upper() == "D":
            score = score + 2
            print("[A]: ravioli")
            print("[B]: pasta")
            print("[C]: burger")
            print("[D]: shrimp")
            answer = input("What is your favorite food out of the choices above? (A/B/C/D)")
            if answer.upper() == "A":
                score = score + 2
                print("[A]: summer")
                print("[B]: spring")
                print("[C]: fall")
                print("[D]: winter")
                answer = input("What is your favorite season out of the choices above? (A/B/C/D)")
                if answer.upper() == "A":
                    score = score + 2
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score+2
                    elif answer.upper() == "B":
                        score = score+1
                    elif answer.upper() == "C":
                        score = score+5
                    elif answer.upper() == "D":
                        score = score+3
                elif answer.upper() == "B":
                    score = score + 1
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "C":
                    score = score + 5
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "D":
                    score = score + 3
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
            elif answer.upper() == "B":
                score = score + 1
                print("[A]: summer")
                print("[B]: spring")
                print("[C]: fall")
                print("[D]: winter")
                answer = input("What is your favorite season out of the choices above? (A/B/C/D)")
                if answer.upper() == "A":
                    score = score + 2
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score+2
                    elif answer.upper() == "B":
                        score = score+1
                    elif answer.upper() == "C":
                        score = score+5
                    elif answer.upper() == "D":
                        score = score+3
                elif answer.upper() == "B":
                    score = score + 1
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "C":
                    score = score + 5
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "D":
                    score = score + 3
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
            elif answer.upper() == "C":
                score = score + 5
                print("[A]: summer")
                print("[B]: spring")
                print("[C]: fall")
                print("[D]: winter")
                answer = input("What is your favorite season out of the choices above? (A/B/C/D)")
                if answer.upper() == "A":
                    score = score + 2
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score+2
                    elif answer.upper() == "B":
                        score = score+1
                    elif answer.upper() == "C":
                        score = score+5
                    elif answer.upper() == "D":
                        score = score+3
                elif answer.upper() == "B":
                    score = score + 1
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "C":
                    score = score + 5
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "D":
                    score = score + 3
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
            elif answer.upper() == "D":
                score = score + 3
                print("[A]: summer")
                print("[B]: spring")
                print("[C]: fall")
                print("[D]: winter")
                answer = input("What is your favorite season out of the choices above? (A/B/C/D)")
                if answer.upper() == "A":
                    score = score + 2
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score+2
                    elif answer.upper() == "B":
                        score = score+1
                    elif answer.upper() == "C":
                        score = score+5
                    elif answer.upper() == "D":
                        score = score+3
                elif answer.upper() == "B":
                    score = score + 1
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "C":
                    score = score + 5
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "D":
                    score = score + 3
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
    elif answer.upper() == "C":
        score = score+3
        print("[A]: purple")
        print("[B]: black")
        print("[C]: blue")
        print("[D]: maroon")
        answer = input("Which is the best color out of the choices above? (A/B/C/D)")
        if answer.upper() == "A":
            score = score + 1
            print("[A]: ravioli")
            print("[B]: pasta")
            print("[C]: burger")
            print("[D]: shrimp")
            answer = input("What is your favorite food out of the choices above? (A/B/C/D)")
            if answer.upper() == "A":
                score = score + 2
                print("[A]: summer")
                print("[B]: spring")
                print("[C]: fall")
                print("[D]: winter")
                answer = input("What is your favorite season out of the choices above? (A/B/C/D)")
                if answer.upper() == "A":
                    score = score + 2
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score+2
                    elif answer.upper() == "B":
                        score = score+1
                    elif answer.upper() == "C":
                        score = score+5
                    elif answer.upper() == "D":
                        score = score+3
                elif answer.upper() == "B":
                    score = score + 1
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "C":
                    score = score + 5
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "D":
                    score = score + 3
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
            elif answer.upper() == "B":
                score = score + 1
                print("[A]: summer")
                print("[B]: spring")
                print("[C]: fall")
                print("[D]: winter")
                answer = input("What is your favorite season out of the choices above? (A/B/C/D)")
                if answer.upper() == "A":
                    score = score + 2
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score+2
                    elif answer.upper() == "B":
                        score = score+1
                    elif answer.upper() == "C":
                        score = score+5
                    elif answer.upper() == "D":
                        score = score+3
                elif answer.upper() == "B":
                    score = score + 1
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "C":
                    score = score + 5
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "D":
                    score = score + 3
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
            elif answer.upper() == "C":
                score = score + 5
                print("[A]: summer")
                print("[B]: spring")
                print("[C]: fall")
                print("[D]: winter")
                answer = input("What is your favorite season out of the choices above? (A/B/C/D)")
                if answer.upper() == "A":
                    score = score + 2
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score+2
                    elif answer.upper() == "B":
                        score = score+1
                    elif answer.upper() == "C":
                        score = score+5
                    elif answer.upper() == "D":
                        score = score+3
                elif answer.upper() == "B":
                    score = score + 1
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "C":
                    score = score + 5
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "D":
                    score = score + 3
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
            elif answer.upper() == "D":
                score = score + 3
                print("[A]: summer")
                print("[B]: spring")
                print("[C]: fall")
                print("[D]: winter")
                answer = input("What is your favorite season out of the choices above? (A/B/C/D)")
                if answer.upper() == "A":
                    score = score + 2
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score+2
                    elif answer.upper() == "B":
                        score = score+1
                    elif answer.upper() == "C":
                        score = score+5
                    elif answer.upper() == "D":
                        score = score+3
                elif answer.upper() == "B":
                    score = score + 1
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "C":
                    score = score + 5
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "D":
                    score = score + 3
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
        elif answer.upper() == "B":
            score = score + 3
            print("[A]: ravioli")
            print("[B]: pasta")
            print("[C]: burger")
            print("[D]: shrimp")
            answer = input("What is your favorite food out of the choices above? (A/B/C/D)")
            if answer.upper() == "A":
                score = score + 2
                print("[A]: summer")
                print("[B]: spring")
                print("[C]: fall")
                print("[D]: winter")
                answer = input("What is your favorite season out of the choices above? (A/B/C/D)")
                if answer.upper() == "A":
                    score = score + 2
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score+2
                    elif answer.upper() == "B":
                        score = score+1
                    elif answer.upper() == "C":
                        score = score+5
                    elif answer.upper() == "D":
                        score = score+3
                elif answer.upper() == "B":
                    score = score + 1
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "C":
                    score = score + 5
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "D":
                    score = score + 3
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
            elif answer.upper() == "B":
                score = score + 1
                print("[A]: summer")
                print("[B]: spring")
                print("[C]: fall")
                print("[D]: winter")
                answer = input("What is your favorite season out of the choices above? (A/B/C/D)")
                if answer.upper() == "A":
                    score = score + 2
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score+2
                    elif answer.upper() == "B":
                        score = score+1
                    elif answer.upper() == "C":
                        score = score+5
                    elif answer.upper() == "D":
                        score = score+3
                elif answer.upper() == "B":
                    score = score + 1
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "C":
                    score = score + 5
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "D":
                    score = score + 3
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
            elif answer.upper() == "C":
                score = score + 5
                print("[A]: summer")
                print("[B]: spring")
                print("[C]: fall")
                print("[D]: winter")
                answer = input("What is your favorite season out of the choices above? (A/B/C/D)")
                if answer.upper() == "A":
                    score = score + 2
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score+2
                    elif answer.upper() == "B":
                        score = score+1
                    elif answer.upper() == "C":
                        score = score+5
                    elif answer.upper() == "D":
                        score = score+3
                elif answer.upper() == "B":
                    score = score + 1
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "C":
                    score = score + 5
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "D":
                    score = score + 3
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
            elif answer.upper() == "D":
                score = score + 3
                print("[A]: summer")
                print("[B]: spring")
                print("[C]: fall")
                print("[D]: winter")
                answer = input("What is your favorite season out of the choices above? (A/B/C/D)")
                if answer.upper() == "A":
                    score = score + 2
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score+2
                    elif answer.upper() == "B":
                        score = score+1
                    elif answer.upper() == "C":
                        score = score+5
                    elif answer.upper() == "D":
                        score = score+3
                elif answer.upper() == "B":
                    score = score + 1
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "C":
                    score = score + 5
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "D":
                    score = score + 3
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
        elif answer.upper() == "C":
            score = score + 5
            print("[A]: ravioli")
            print("[B]: pasta")
            print("[C]: burger")
            print("[D]: shrimp")
            answer = input("What is your favorite food out of the choices above? (A/B/C/D)")
            if answer.upper() == "A":
                score = score + 2
                print("[A]: summer")
                print("[B]: spring")
                print("[C]: fall")
                print("[D]: winter")
                answer = input("What is your favorite season out of the choices above? (A/B/C/D)")
                if answer.upper() == "A":
                    score = score + 2
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score+2
                    elif answer.upper() == "B":
                        score = score+1
                    elif answer.upper() == "C":
                        score = score+5
                    elif answer.upper() == "D":
                        score = score+3
                elif answer.upper() == "B":
                    score = score + 1
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "C":
                    score = score + 5
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "D":
                    score = score + 3
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
            elif answer.upper() == "B":
                score = score + 1
                print("[A]: summer")
                print("[B]: spring")
                print("[C]: fall")
                print("[D]: winter")
                answer = input("What is your favorite season out of the choices above? (A/B/C/D)")
                if answer.upper() == "A":
                    score = score + 2
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score+2
                    elif answer.upper() == "B":
                        score = score+1
                    elif answer.upper() == "C":
                        score = score+5
                    elif answer.upper() == "D":
                        score = score+3
                elif answer.upper() == "B":
                    score = score + 1
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "C":
                    score = score + 5
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "D":
                    score = score + 3
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
            elif answer.upper() == "C":
                score = score + 5
                print("[A]: summer")
                print("[B]: spring")
                print("[C]: fall")
                print("[D]: winter")
                answer = input("What is your favorite season out of the choices above? (A/B/C/D)")
                if answer.upper() == "A":
                    score = score + 2
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score+2
                    elif answer.upper() == "B":
                        score = score+1
                    elif answer.upper() == "C":
                        score = score+5
                    elif answer.upper() == "D":
                        score = score+3
                elif answer.upper() == "B":
                    score = score + 1
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "C":
                    score = score + 5
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "D":
                    score = score + 3
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
            elif answer.upper() == "D":
                score = score + 3
                print("[A]: summer")
                print("[B]: spring")
                print("[C]: fall")
                print("[D]: winter")
                answer = input("What is your favorite season out of the choices above? (A/B/C/D)")
                if answer.upper() == "A":
                    score = score + 2
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score+2
                    elif answer.upper() == "B":
                        score = score+1
                    elif answer.upper() == "C":
                        score = score+5
                    elif answer.upper() == "D":
                        score = score+3
                elif answer.upper() == "B":
                    score = score + 1
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "C":
                    score = score + 5
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "D":
                    score = score + 3
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
        elif answer.upper() == "D":
            score = score + 2
            print("[A]: ravioli")
            print("[B]: pasta")
            print("[C]: burger")
            print("[D]: shrimp")
            answer = input("What is your favorite food out of the choices above? (A/B/C/D)")
            if answer.upper() == "A":
                score = score + 2
                print("[A]: summer")
                print("[B]: spring")
                print("[C]: fall")
                print("[D]: winter")
                answer = input("What is your favorite season out of the choices above? (A/B/C/D)")
                if answer.upper() == "A":
                    score = score + 2
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score+2
                    elif answer.upper() == "B":
                        score = score+1
                    elif answer.upper() == "C":
                        score = score+5
                    elif answer.upper() == "D":
                        score = score+3
                elif answer.upper() == "B":
                    score = score + 1
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "C":
                    score = score + 5
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "D":
                    score = score + 3
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
            elif answer.upper() == "B":
                score = score + 1
                print("[A]: summer")
                print("[B]: spring")
                print("[C]: fall")
                print("[D]: winter")
                answer = input("What is your favorite season out of the choices above? (A/B/C/D)")
                if answer.upper() == "A":
                    score = score + 2
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score+2
                    elif answer.upper() == "B":
                        score = score+1
                    elif answer.upper() == "C":
                        score = score+5
                    elif answer.upper() == "D":
                        score = score+3
                elif answer.upper() == "B":
                    score = score + 1
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "C":
                    score = score + 5
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "D":
                    score = score + 3
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
            elif answer.upper() == "C":
                score = score + 5
                print("[A]: summer")
                print("[B]: spring")
                print("[C]: fall")
                print("[D]: winter")
                answer = input("What is your favorite season out of the choices above? (A/B/C/D)")
                if answer.upper() == "A":
                    score = score + 2
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score+2
                    elif answer.upper() == "B":
                        score = score+1
                    elif answer.upper() == "C":
                        score = score+5
                    elif answer.upper() == "D":
                        score = score+3
                elif answer.upper() == "B":
                    score = score + 1
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "C":
                    score = score + 5
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "D":
                    score = score + 3
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
            elif answer.upper() == "D":
                score = score + 3
                print("[A]: summer")
                print("[B]: spring")
                print("[C]: fall")
                print("[D]: winter")
                answer = input("What is your favorite season out of the choices above? (A/B/C/D)")
                if answer.upper() == "A":
                    score = score + 2
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score+2
                    elif answer.upper() == "B":
                        score = score+1
                    elif answer.upper() == "C":
                        score = score+5
                    elif answer.upper() == "D":
                        score = score+3
                elif answer.upper() == "B":
                    score = score + 1
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "C":
                    score = score + 5
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "D":
                    score = score + 3
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
    elif answer.upper() == "D":
        score = score+1
        print("[A]: purple")
        print("[B]: black")
        print("[C]: blue")
        print("[D]: maroon")
        answer = input("Which is the best color out of the choices above? (A/B/C/D)")
        if answer.upper() == "A":
            score = score + 1
            print("[A]: ravioli")
            print("[B]: pasta")
            print("[C]: burger")
            print("[D]: shrimp")
            answer = input("What is your favorite food out of the choices above? (A/B/C/D)")
            if answer.upper() == "A":
                score = score + 2
                print("[A]: summer")
                print("[B]: spring")
                print("[C]: fall")
                print("[D]: winter")
                answer = input("What is your favorite season out of the choices above? (A/B/C/D)")
                if answer.upper() == "A":
                    score = score + 2
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score+2
                    elif answer.upper() == "B":
                        score = score+1
                    elif answer.upper() == "C":
                        score = score+5
                    elif answer.upper() == "D":
                        score = score+3
                elif answer.upper() == "B":
                    score = score + 1
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "C":
                    score = score + 5
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "D":
                    score = score + 3
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
            elif answer.upper() == "B":
                score = score + 1
                print("[A]: summer")
                print("[B]: spring")
                print("[C]: fall")
                print("[D]: winter")
                answer = input("What is your favorite season out of the choices above? (A/B/C/D)")
                if answer.upper() == "A":
                    score = score + 2
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score+2
                    elif answer.upper() == "B":
                        score = score+1
                    elif answer.upper() == "C":
                        score = score+5
                    elif answer.upper() == "D":
                        score = score+3
                elif answer.upper() == "B":
                    score = score + 1
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "C":
                    score = score + 5
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "D":
                    score = score + 3
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
            elif answer.upper() == "C":
                score = score + 5
                print("[A]: summer")
                print("[B]: spring")
                print("[C]: fall")
                print("[D]: winter")
                answer = input("What is your favorite season out of the choices above? (A/B/C/D)")
                if answer.upper() == "A":
                    score = score + 2
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score+2
                    elif answer.upper() == "B":
                        score = score+1
                    elif answer.upper() == "C":
                        score = score+5
                    elif answer.upper() == "D":
                        score = score+3
                elif answer.upper() == "B":
                    score = score + 1
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "C":
                    score = score + 5
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "D":
                    score = score + 3
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
            elif answer.upper() == "D":
                score = score + 3
                print("[A]: summer")
                print("[B]: spring")
                print("[C]: fall")
                print("[D]: winter")
                answer = input("What is your favorite season out of the choices above? (A/B/C/D)")
                if answer.upper() == "A":
                    score = score + 2
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score+2
                    elif answer.upper() == "B":
                        score = score+1
                    elif answer.upper() == "C":
                        score = score+5
                    elif answer.upper() == "D":
                        score = score+3
                elif answer.upper() == "B":
                    score = score + 1
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "C":
                    score = score + 5
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "D":
                    score = score + 3
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
        elif answer.upper() == "B":
            score = score + 3
            print("[A]: ravioli")
            print("[B]: pasta")
            print("[C]: burger")
            print("[D]: shrimp")
            answer = input("What is your favorite food out of the choices above? (A/B/C/D)")
            if answer.upper() == "A":
                score = score + 2
                print("[A]: summer")
                print("[B]: spring")
                print("[C]: fall")
                print("[D]: winter")
                answer = input("What is your favorite season out of the choices above? (A/B/C/D)")
                if answer.upper() == "A":
                    score = score + 2
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score+2
                    elif answer.upper() == "B":
                        score = score+1
                    elif answer.upper() == "C":
                        score = score+5
                    elif answer.upper() == "D":
                        score = score+3
                elif answer.upper() == "B":
                    score = score + 1
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "C":
                    score = score + 5
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "D":
                    score = score + 3
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
            elif answer.upper() == "B":
                score = score + 1
                print("[A]: summer")
                print("[B]: spring")
                print("[C]: fall")
                print("[D]: winter")
                answer = input("What is your favorite season out of the choices above? (A/B/C/D)")
                if answer.upper() == "A":
                    score = score + 2
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score+2
                    elif answer.upper() == "B":
                        score = score+1
                    elif answer.upper() == "C":
                        score = score+5
                    elif answer.upper() == "D":
                        score = score+3
                elif answer.upper() == "B":
                    score = score + 1
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "C":
                    score = score + 5
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "D":
                    score = score + 3
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
            elif answer.upper() == "C":
                score = score + 5
                print("[A]: summer")
                print("[B]: spring")
                print("[C]: fall")
                print("[D]: winter")
                answer = input("What is your favorite season out of the choices above? (A/B/C/D)")
                if answer.upper() == "A":
                    score = score + 2
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score+2
                    elif answer.upper() == "B":
                        score = score+1
                    elif answer.upper() == "C":
                        score = score+5
                    elif answer.upper() == "D":
                        score = score+3
                elif answer.upper() == "B":
                    score = score + 1
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "C":
                    score = score + 5
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "D":
                    score = score + 3
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
            elif answer.upper() == "D":
                score = score + 3
                print("[A]: summer")
                print("[B]: spring")
                print("[C]: fall")
                print("[D]: winter")
                answer = input("What is your favorite season out of the choices above? (A/B/C/D)")
                if answer.upper() == "A":
                    score = score + 2
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score+2
                    elif answer.upper() == "B":
                        score = score+1
                    elif answer.upper() == "C":
                        score = score+5
                    elif answer.upper() == "D":
                        score = score+3
                elif answer.upper() == "B":
                    score = score + 1
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "C":
                    score = score + 5
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "D":
                    score = score + 3
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
        elif answer.upper() == "C":
            score = score + 5
            print("[A]: ravioli")
            print("[B]: pasta")
            print("[C]: burger")
            print("[D]: shrimp")
            answer = input("What is your favorite food out of the choices above? (A/B/C/D)")
            if answer.upper() == "A":
                score = score + 2
                print("[A]: summer")
                print("[B]: spring")
                print("[C]: fall")
                print("[D]: winter")
                answer = input("What is your favorite season out of the choices above? (A/B/C/D)")
                if answer.upper() == "A":
                    score = score + 2
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score+2
                    elif answer.upper() == "B":
                        score = score+1
                    elif answer.upper() == "C":
                        score = score+5
                    elif answer.upper() == "D":
                        score = score+3
                elif answer.upper() == "B":
                    score = score + 1
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "C":
                    score = score + 5
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "D":
                    score = score + 3
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
            elif answer.upper() == "B":
                score = score + 1
                print("[A]: summer")
                print("[B]: spring")
                print("[C]: fall")
                print("[D]: winter")
                answer = input("What is your favorite season out of the choices above? (A/B/C/D)")
                if answer.upper() == "A":
                    score = score + 2
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score+2
                    elif answer.upper() == "B":
                        score = score+1
                    elif answer.upper() == "C":
                        score = score+5
                    elif answer.upper() == "D":
                        score = score+3
                elif answer.upper() == "B":
                    score = score + 1
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "C":
                    score = score + 5
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "D":
                    score = score + 3
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
            elif answer.upper() == "C":
                score = score + 5
                print("[A]: summer")
                print("[B]: spring")
                print("[C]: fall")
                print("[D]: winter")
                answer = input("What is your favorite season out of the choices above? (A/B/C/D)")
                if answer.upper() == "A":
                    score = score + 2
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score+2
                    elif answer.upper() == "B":
                        score = score+1
                    elif answer.upper() == "C":
                        score = score+5
                    elif answer.upper() == "D":
                        score = score+3
                elif answer.upper() == "B":
                    score = score + 1
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "C":
                    score = score + 5
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "D":
                    score = score + 3
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
            elif answer.upper() == "D":
                score = score + 3
                print("[A]: summer")
                print("[B]: spring")
                print("[C]: fall")
                print("[D]: winter")
                answer = input("What is your favorite season out of the choices above? (A/B/C/D)")
                if answer.upper() == "A":
                    score = score + 2
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score+2
                    elif answer.upper() == "B":
                        score = score+1
                    elif answer.upper() == "C":
                        score = score+5
                    elif answer.upper() == "D":
                        score = score+3
                elif answer.upper() == "B":
                    score = score + 1
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "C":
                    score = score + 5
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "D":
                    score = score + 3
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
        elif answer.upper() == "D":
            score = score + 2
            print("[A]: ravioli")
            print("[B]: pasta")
            print("[C]: burger")
            print("[D]: shrimp")
            answer = input("What is your favorite food out of the choices above? (A/B/C/D)")
            if answer.upper() == "A":
                score = score + 2
                print("[A]: summer")
                print("[B]: spring")
                print("[C]: fall")
                print("[D]: winter")
                answer = input("What is your favorite season out of the choices above? (A/B/C/D)")
                if answer.upper() == "A":
                    score = score + 2
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score+2
                    elif answer.upper() == "B":
                        score = score+1
                    elif answer.upper() == "C":
                        score = score+5
                    elif answer.upper() == "D":
                        score = score+3
                elif answer.upper() == "B":
                    score = score + 1
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "C":
                    score = score + 5
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "D":
                    score = score + 3
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
            elif answer.upper() == "B":
                score = score + 1
                print("[A]: summer")
                print("[B]: spring")
                print("[C]: fall")
                print("[D]: winter")
                answer = input("What is your favorite season out of the choices above? (A/B/C/D)")
                if answer.upper() == "A":
                    score = score + 2
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score+2
                    elif answer.upper() == "B":
                        score = score+1
                    elif answer.upper() == "C":
                        score = score+5
                    elif answer.upper() == "D":
                        score = score+3
                elif answer.upper() == "B":
                    score = score + 1
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "C":
                    score = score + 5
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "D":
                    score = score + 3
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
            elif answer.upper() == "C":
                score = score + 5
                print("[A]: summer")
                print("[B]: spring")
                print("[C]: fall")
                print("[D]: winter")
                answer = input("What is your favorite season out of the choices above? (A/B/C/D)")
                if answer.upper() == "A":
                    score = score + 2
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score+2
                    elif answer.upper() == "B":
                        score = score+1
                    elif answer.upper() == "C":
                        score = score+5
                    elif answer.upper() == "D":
                        score = score+3
                elif answer.upper() == "B":
                    score = score + 1
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "C":
                    score = score + 5
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "D":
                    score = score + 3
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
            elif answer.upper() == "D":
                score = score + 3
                print("[A]: summer")
                print("[B]: spring")
                print("[C]: fall")
                print("[D]: winter")
                answer = input("What is your favorite season out of the choices above? (A/B/C/D)")
                if answer.upper() == "A":
                    score = score + 2
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score+2
                    elif answer.upper() == "B":
                        score = score+1
                    elif answer.upper() == "C":
                        score = score+5
                    elif answer.upper() == "D":
                        score = score+3
                elif answer.upper() == "B":
                    score = score + 1
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "C":
                    score = score + 5
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3
                elif answer.upper() == "D":
                    score = score + 3
                    print("[A]: europe")
                    print("[B]: antarctica")
                    print("[C]: africa")
                    print("[D]: asia")
                    answer = input("What is your favorite continent out of the choices above? (A/B/C/D)")
                    if answer.upper() == "A":
                        score = score + 2
                    elif answer.upper() == "B":
                        score = score + 1
                    elif answer.upper() == "C":
                        score = score + 5
                    elif answer.upper() == "D":
                        score = score + 3




else:
    print("ok")

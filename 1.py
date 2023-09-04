import random


def question():
    while True:
        number = input("How many times do you want to play? A maximum of 5 times: ") 
        if number.isnumeric():
            if 1 <= int(number) <= 5:
                return int(number)
        print("just type number between 1 and 5")
        
def report(user, cpu):
    real_name = {
        "s": "scissor",
        "r": "rock",
        "p": "paper",
    }
    return f'your choice was {real_name[user]} and computer was {real_name[cpu]}'

def final_result(score_user, score_cpu, draw_game):
    return f"you won {score_user} times and you lose {score_cpu} times and The game has been tied {draw_game} times"


def game():
    user = question()
    win_user = win_cpu = draw_game = 0
    
    for _ in range(user):
        while True:
            global ask
            ask = input("enter p(paper) or r(rock) or s(scissor): ")
            if ask in("p", "r", "s"):
                break
            print("just type (s) or (p) or (r)\n")
        
        choices = ["r", "p", "s"]
        cpu = random.choice(choices)
        
        if (ask == "p" and cpu == "r") or (ask == "s" and cpu == "p") or (ask == "r" and cpu == "s"):
            print("you win")
            print(report(ask, cpu))
            win_user += 1

        if (ask == "r" and cpu == "p") or (ask == "p" and cpu == "s") or (ask == "s" and cpu == "r"):
            print("you lose")
            print(report(ask, cpu))
            win_cpu += 1

        if ask == cpu:
            print("draw")
            print(report(ask, cpu))
            draw_game += 1
            
    if win_user == win_cpu:
        print("final draw")
        return final_result(win_user, win_cpu, draw_game)
    
    if win_user > win_cpu:
        print("final winner")
        return final_result(win_user, win_cpu, draw_game)
    
    print("final Failed")
    return final_result(win_user, win_cpu, draw_game)
         

print(game())

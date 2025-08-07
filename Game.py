from random import choice
mydict = {"s":1,"p":-1,"c":0}
comdict = {1:"stone",-1:"paper",0:"ceaser"}

print("🎮 Welcome to Stone-Paper-Ceaser Game 🎮\n")
print("🔹 Type 's' for Stone")
print("🔹 Type 'p' for Paper")
print("🔹 Type 'c' for Ceaser\n")

while True:
    player = input("👉 Enter Your Choice (s/p/c): ").lower()
    computer = choice([-1,1,0])

    if player not in mydict:
            print("❌ Invalid Choice. Please type 's', 'p', or 'c'.\n")
            continue
    else:
        me = mydict[player]

        print("\n🔁 Result:")
        print("════════════════════════════════════")
        
        if computer == me:
                print("🤝 It's a Draw!")

        else:
                if computer == 1 and me == 0:
                    print("😞 You Lose!")
                elif computer == 1 and me == -1:
                    print("🎉 You Win!")
                elif computer == -1 and me == 1:
                    print("😞 You Lose!")
                elif computer == -1 and me == 0:
                    print("🎉 You Win!")
                elif computer == 0 and me == 1:
                    print("😞 You Lose!")
                elif computer == 0 and me == -1:
                    print("🎉 You Win!")
                else:
                    print("Somethin Went Wrong...")
        
                print(f"\n🧍 You Chose      → {comdict[me]}")
                print(f"🤖 Computer Chose → {comdict[computer]}")
                print("════════════════════════════════════\n")

        ask = input("🔁 Do You Want To Play Again? (y/n): ").lower()
        if ask != "y":
             print("\n👋 Thanks For Playing! See you next time!")
             break
        

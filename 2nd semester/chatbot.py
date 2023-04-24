import random
print("Welcome to Mo's Chatbot. What's on your mind today?")
doExit = False
topic = "*something*"
topiclist = ["cereal", "salad"]
while doExit == False:
    print("> ", end="")
    choice = input().lower().split(" ")
    if choice == "quit":
        doExit = True
        break

    #listen and respond to feelings
    if "sad" in choice or "feeling down" in choice or "upset" in choice or "angry" in choice :
        print("I'm sorry to hear you're feeling that way.")
    elif "happy" in choice or "glad" in choice or "excited" in choice or "looking forward" in choice :
        print("That's great!")
    elif "i'm" in choice: #these next three lines let you repeat the word after "I'm" back in a sentence
        next_word = choice[choice.index("i'm") + 1] #find the word after "I'm"
        if next_word == "a":
            next_word = choice[choice.index("i'm") + 1]
        print("Why are you", next_word+ "?") #repeat it back 
        topic = next_word
        # NOTE: it would be good to add an if statement here checking if the next word was "a" 
        #so if someone says "I'm a frog", it doesn't say back, "Why are you a?"
    elif "not much" in choice or "no" in choice:
        print(f"Maybe you're thinking about {topic}?")
    #listen and respond to specific topics
    elif "mom" in choice or "dad" in choice or "brother" in choice or "sister" in choice :
        print("Tell me more about your family.")
        topic = "your family"

    elif "dog" in choice or "cat" in choice or "fish" in choice or "bird" in choice :
        print("I'd like to hear more about this pet.")
        topic = "your pet"

    else: #randomize last statement so it's not too repetetive 
        num = random.random()
        if num < 0.5:
            print("Can you tell me more?")
            topic = "cereal"
        else:
            print("What does that suggest to you?")
            topic = "salad"
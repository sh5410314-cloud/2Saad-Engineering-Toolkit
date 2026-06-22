print("CEO Saad LLM v1.0 চালু CEO! 🤖")
print("আমাকে কিছু জিজ্ঞেস করো Boss!")

while True:
    q = input("You: ").lower()
    
    if "jog" in q or "add" in q or "+" in q:  # ← প্রথমে IF CEO!
        a = int(input("Number 1: "))
        b = int(input("Number 2: "))
        print(f"CEO Saad LLM: উত্তর = {a+b} CEO!")
        
    elif "biyog" in q or "minus" in q or "-" in q:  # ← তারপর ELIF CEO!
        a = int(input("Number 1: "))
        b = int(input("Number 2: "))
        print(f"CEO Saad LLM: উত্তর = {a-b} CEO!")
        
    elif "gun" in q or "multiply" in q or "*" in q:  # ← তারপর ELIF CEO!
        a = int(input("Number 1: "))
        b = int(input("Number 2: "))
        print(f"CEO Saad LLM: উত্তর = {a*b} CEO!")
        
    elif "vag" in q or "divide" in q or "/" in q:  # ← তারপর ELIF CEO!
        a = int(input("Number 1: "))
        b = int(input("Number 2: "))
        if b != 0:
            print(f"CEO Saad LLM: উত্তর = {a/b} CEO!")
        else:
            print("CEO Saad LLM: Zero দিয়া ভাগ হারাম CEO!")
        
    elif "bye" in q or "exit" in q:  # ← ELIF CEO!
        print("CEO Saad LLM: আল্লাহ হাফেজ Boss CEO!")
        break
        
    else:  # ← শেষে ELSE CEO!
        print("CEO Saad LLM: সরি Boss, আমি এখনো ছোট CEO!")
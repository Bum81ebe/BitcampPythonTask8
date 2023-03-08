#greeting #bank #money

greeting = input("How do you start a conversation? ")

if greeting.lower().startswith("hello"):
    print("$0")
elif "h" in greeting.lower():
    print("$20")
else:
    print("$100")

#greeting #bank #money

greeting = input("How do you start a conversation? ")

if greeting == "Hello":
    print("$0")
elif "H" in greeting and greeting != "Hello":
    print("20")
else:
    print("100$")
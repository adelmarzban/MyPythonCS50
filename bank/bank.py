name = input("Greeting: ")

if name.strip().lower().__contains__("hello") or name.strip().lower().__contains__("hi"):
        print("$0")
elif name.strip().lower().startswith("h"):
        print("$20")
else: print("$100")
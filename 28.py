extensions = ['txt', 'jpg', 'gif', 'html']

request = input("type any extension: ")

if request in extensions:
    print("OK")
else:
    print("extension not found")
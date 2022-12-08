import webbrowser
while True:
    user=input("Enter the website : ")
    if user=="exit":
        exit()
    else:
        webbrowser.open("https//www"+user+".com")
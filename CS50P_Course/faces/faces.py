def faces():
    user_input = input()
    text = user_input.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    print(text)


faces()

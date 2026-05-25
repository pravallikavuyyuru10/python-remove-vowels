def remove_vowels(text):
    result =  ""
    for i in text:
        if i.lower() not in "aeiou":
            result = result + i
    print(result)
remove_vowels("Python")
    

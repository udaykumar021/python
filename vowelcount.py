def vowel(n):
    s = n.lower()
    c = 0
    for i in s:
        if i in 'aeiou':
            c+=1
    return c
string = str(input("Enter a valid string: "))
print(f"no.of vowels are {vowel(string)}")
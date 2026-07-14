def vowels(s):
    vowels = set("aeiou")
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count
s = input("enter string :")
s = s.lower()
result = vowels(s)
print(result)

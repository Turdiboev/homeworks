s = input("Soʻzni kiriting: ").lower()

a = "aeiou"
unli = 0
undosh = 0

for ch in s:
    if ch.isalpha():
        if ch in vowels:
            unli += 1
        else:
            undosh += 1

print("Unlilar: ", unli)
print("Undoshlar: ", undosh)
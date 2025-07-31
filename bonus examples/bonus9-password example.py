password_input = input("Enter new password")
result = {}

if len(password_input) >= 8:
    result["PasswordLength"] = True
else:
    result["PasswordLength"] = False

isdigit = False
for element in password_input:
    if element.isdigit():
        isdigit = True

result["Digits"] = isdigit


isUpper = False
for element in password_input:
    if element.isupper():
        isUpper = True

result["HasUpperCaseLetter"] = isUpper

if all(result.values()):
    print("Strong password")
else:
    print("Weak password")
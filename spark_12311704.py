print("Hello, Python!")

name = "Alice"
age = 20
score = 95

print("name:", name)
print("age:", age)
print("score:", score)

if score >= 60:
    print("考试通过")
else:
    print("考试未通过")

numbers = [1, 2, 3, 4, 5]
total = 0

for number in numbers:
    total += number

print("列表总和:", total)


def greet(user_name):
    return f"你好, {user_name}!"


print(greet(name))

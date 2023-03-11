import random

print(chr(ord('a')+25))

lower_alph = [chr(ord('a') + x) for x in range(26)]
upper_alph = [chr(ord('A') + x) for x in range(26)]
number = [str(x) for x in range(10)]

length = 9

password_case = lower_alph + upper_alph + number

generated_password = "".join(random.sample(password_case, length))

print(generated_password)
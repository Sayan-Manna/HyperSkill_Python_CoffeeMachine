str_ = input()
new = str_.replace("!", "")
x = new.replace(".", "")
y = x.replace(",", "")
z = y.replace("?", "")
print(z.lower())

# Solution Using Loops :

# input_text = input()
# lower_text = input_text.lower()
# punct = ",.!?"
# for i in punct:
#   lower_text = lower_text.replace(i, "")

# print(lower_text)

from pythainlp import word_tokenize

text = "รัฐบาลแจกเงินหมื่นดิจิทัลวอลเล็ต"
tokens = word_tokenize(text)

print(tokens)

for token in tokens:
    if token == "ก้าวไกล":
        print("ก้าวไกลหรือก้าวกามวะเนี้ย")
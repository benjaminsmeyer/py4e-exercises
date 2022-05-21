# Exercise 6.5
# 6.5 Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below. 
# Convert the extracted value to a floating point number and print it out.

text = "X-DSPAM-Confidence:    0.8475"
atPosition = text.find(":")
newText = text[atPosition + 1:]
stripNewText = newText.strip()
convertTextToFloat = float(stripNewText)
num = convertTextToFloat

# Short: num = float(text[text.find(":") + 1:].strip())

print(num)
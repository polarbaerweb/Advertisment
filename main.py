# FIRST TASK to find a year, weeks and days

# def calcullateDates(num):
#     year = num // 365
#     weeks = 0
#     day = 0
#     if num - (365 * year) > 7:
#         weeks = (num - (365 * year)) // 7
#     if weeks:
#         day = (num - ((365 * year) + (7 * weeks)))
#     elif not year:
#         day = num
#     elif year and not weeks:
#         day = num - (365 * year)
#     print(year, weeks, day)


# while True:
#     try:
#         num = int(input("Enter days: "))
#     except ValueError:
#         print("Days should in integer format*")
#     else:
#         calcullateDates(num)

# SECOND TASK to find a word that is exist

# def findSubString(word, string):
#     array = string.split(" ")
#     if word in array:
#         return word
#     return "There is not such kind of word"


# while True:
#     string = input("Enter something: ")
#     findWord = input("Which word do you want to find >> ")
#     print(findSubString(findWord, string))


# THIRD TASK to detremine is this word a pangram

# def detremine(s):
#     alphabet = "abcdefghijklmnopqrstuvwxyz"
#     lowercase = s.lower().replace(" ", "")

#     for i in range(len(alphabet)):
#         if lowercase.index(alphabet[i]) == -1:
#             return "not pangram"

#     return "pangram"


# print(detremine('The quick brown fox jumps over the lazy dog'))

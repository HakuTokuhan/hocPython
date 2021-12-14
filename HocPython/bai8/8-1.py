print(r"Haizz, \neu mot ngay nao do")

strA = "HowKteam.com"
strB = "Free education"
'strC = strA*5'
strC = strA + "\n" + strB
print(strC)

strA = "HowKteam.com"
strB = "k"
strC = strB in strA
print(strC)

strA = "HowKteam"
strB = strA[-5]
strC = strB in strA
print(strB)

strA = "HowKteam"
strB = strA[None:None:2]
strC = strB in strA
print(strB)

strA = float("69")
print(strA)

strA = "HowKteam.com"
strA = strA[None:1] + "0" + strA[2:None]
print(strA)
print(hash(strA))
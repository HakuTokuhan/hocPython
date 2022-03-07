# practise 1-4 solution
def input_personal_info():
    person_infor = {}
    person_infor['name'] = input("Hãy nhập tên của bạn: ")
    person_infor['gender'] = input("Hãy nhập giới tính của bạn (nam/nữ): ")
    person_infor['age'] = int(input("Hãy nhập tuổi của bạn: "))
    person_infor['experience'] = int(input("Hãy nhập số năm kinh nghiệm của bản trong ngành dịch vụ: "))
    person_infor['height'] = float(input("Hãy nhập chiều cao của bạn (theo mét): "))
    person_infor['weight'] = float(input("Hãy nhập cân nặng của bạn (theo kg): "))
    return person_infor


def isQualified(person):

    def printQualifiedMessage():
        print("Xin chúc mừng bạn đã trúng tuyển")

    def printNotQualifiedMessage():
        print("Xin lỗi bạn không hợp lệ")

    if person['gender'] == "nữ":
        if 30 <= person['age'] <= 40:
            if person['experience'] >= 5 and person['height'] >= 1.55 and person['weight'] <= 45:
                printQualifiedMessage()
            elif person['experience'] >= 2 and person['height'] >= 1.6 and person['weight'] <= 50:
                printQualifiedMessage()
            else:
                printNotQualifiedMessage()
        elif 18 <= person['age'] < 30:
            if person['height'] >= 1.6 and person['weight'] <= 50:
                printQualifiedMessage()
            else:
                printNotQualifiedMessage()
        else:
            printNotQualifiedMessage()
    else:
        printNotQualifiedMessage()

person = input_personal_info()
print(person)
isQualified(person)
INPUT_STOP = 'STOP'

products = [['chăn', 300000], ['ga', 50000], ['gối', 75000], ['đệm', 500000]]


def product_list_info():
    print('Product List Buyer:')
    for i in range(len(products)):
        print(products[i][0], ": ", products[i][1])

shopping_car = []


def save_shopping_car():
    check = True
    print('If break input: STOP')
    while check:
        product_name = input("Your buy product name: ")
        if product_name == INPUT_STOP:
            check = False
            shopping_car.append(product_name)


def caculator_shopping_car():
    total_price = 0
    print("List Product Buy:")
    for i in shopping_car:
        for j in range(len(products)):
            if i == products[j][0]:
                print(products[j][0], ": ", products[j][1])
                total_price += products[j][1]
    print('------------')
    print("Total Price: ", total_price)

product_list_info()
save_shopping_car()
caculator_shopping_car()
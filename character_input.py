import time

def one_hundred_years(age):
    current_year = time.localtime().tm_year

    return current_year + (100 - age)

def run():
    name = input('Input your name: ')
    age = int(input('input your age: '))
    copies = int(input('How many copies do you want of this message?: '))

    year_one_hundred = one_hundred_years(age)

    print(f'Your name is {name} and you will turn 100 in {year_one_hundred}\n'*copies)





if __name__ == '__main__':
    run()
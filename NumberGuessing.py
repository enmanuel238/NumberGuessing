from random import randint


def number_to_guess(x):
    number = 0
    guess = randint(1, x)

    while number != guess:
        number = int(input(f'Ingrese un numero del 1 al {x}: '))

        if number < guess:
            print(f'El numero {number} es muy pequeño')
        elif number > guess:
            print(f'El numero {number} es muy grande')
        else:
            print('Adivinaste!!')

def main():
    number_to_guess(10)

if __name__ == '__main__': 
    main()
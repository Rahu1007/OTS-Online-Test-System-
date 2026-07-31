import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from OTS.models import Question

def seed():
    # Remove existing class_7 questions to prevent duplication on multiple runs
    Question.objects.filter(category='class_7').delete()
    print("Cleaned up existing Class 7th Test questions.")

    questions = [
        # Question 1 (Coding)
        Question(
            que="program to perform addition ,substraction and multiplication , division .",
            category="class_7",
            is_coding=True,
            sample_solution=(
                "# Python program to perform addition, subtraction, multiplication, and division\n"
                "num1 = float(input('Enter first number: '))\n"
                "num2 = float(input('Enter second number: '))\n\n"
                "print('Addition:', num1 + num2)\n"
                "print('Subtraction:', num1 - num2)\n"
                "print('Multiplication:', num1 * num2)\n"
                "if num2 != 0:\n"
                "    print('Division:', num1 / num2)\n"
                "else:\n"
                "    print('Division by zero error')"
            )
        ),
        # Question 2 (MCQ)
        Question(
            que="what is use of Modulus % in programing .",
            category="class_7",
            is_coding=False,
            a="Returns the quotient of two numbers",
            b="Returns the remainder of a division operation",
            c="Performs exponential multiplication",
            d="Compares two numbers for equality",
            ans="b"
        ),
        # Question 3 (Coding)
        Question(
            que="provide the example of exponetiation program code.",
            category="class_7",
            is_coding=True,
            sample_solution=(
                "# Example of exponentiation program code\n"
                "base = float(input('Enter base: '))\n"
                "exponent = float(input('Enter exponent: '))\n"
                "result = base ** exponent\n"
                "print(f'{base} raised to the power of {exponent} is {result}')"
            )
        ),
        # Question 4 (MCQ)
        Question(
            que="arrange the operator based on there prority /precedence. == , != , < , > , <= , =>",
            category="class_7",
            is_coding=False,
            a="< , > , <= , => have higher precedence than == , !=",
            b="== , != have higher precedence than < , > , <= , =>",
            c="All have the same precedence",
            d="None of the above",
            ans="a"
        ),
        # Question 5 (MCQ)
        Question(
            que="what will be the output of the following erpression ? 22 %3 =?",
            category="class_7",
            is_coding=False,
            a="7",
            b="1",
            c="0",
            d="3",
            ans="b"
        ),
        # Question 6 (Coding)
        Question(
            que="what is use of int and float write a code ?",
            category="class_7",
            is_coding=True,
            sample_solution=(
                "# int is used for integers (whole numbers), float is used for decimal numbers\n"
                "my_int = 10\n"
                "my_float = 20.5\n"
                "print('Integer:', my_int, 'Type:', type(my_int))\n"
                "print('Float:', my_float, 'Type:', type(my_float))"
            )
        ),
        # Question 7 (MCQ)
        Question(
            que="a=4.5\nb=2\nprint(a//b)",
            category="class_7",
            is_coding=False,
            a="2",
            b="2.0",
            c="2.25",
            d="2.5",
            ans="b"
        ),
        # Question 8 (Coding)
        Question(
            que="write a program to compare two number using if -else statements .",
            category="class_7",
            is_coding=True,
            sample_solution=(
                "# Program to compare two numbers using if-else\n"
                "num1 = float(input('Enter first number: '))\n"
                "num2 = float(input('Enter second number: '))\n\n"
                "if num1 > num2:\n"
                "    print(f'{num1} is greater than {num2}')\n"
                "elif num1 < num2:\n"
                "    print(f'{num1} is less than {num2}')\n"
                "else:\n"
                "    print('Both numbers are equal')"
            )
        ),
        # Question 9 (Coding)
        Question(
            que="make a program of check even number or odd number ?",
            category="class_7",
            is_coding=True,
            sample_solution=(
                "# Program to check even or odd\n"
                "num = int(input('Enter an integer: '))\n"
                "if num % 2 == 0:\n"
                "    print(f'{num} is even')\n"
                "else:\n"
                "    print(f'{num} is odd')"
            )
        ),
        # Question 10 (Coding)
        Question(
            que="make a own program/ any type of program you can write in this question ?",
            category="class_7",
            is_coding=True,
            sample_solution=(
                "# A simple user-defined program that prints a greeting\n"
                "name = input('Enter your name: ')\n"
                "print(f'Hello, {name}! Welcome to the coding platform.')"
            )
        ),
    ]

    Question.objects.bulk_create(questions)
    print(f"Successfully seeded {len(questions)} Class 7th Test questions!")

if __name__ == '__main__':
    seed()

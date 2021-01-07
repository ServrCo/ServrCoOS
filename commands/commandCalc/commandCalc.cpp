// Hello there! This is the Servr Co Command Line Calculator, made by Servr Co.

#include "maths.hpp"
#include <iostream>
#include <string>
std::string operation;
int firstInt;
int secondInt;
int result;

int main(int argc, char *argv[]) {
    try {
        std::cout << "Enter the operation you want to use: divide, multiply, add, or subtract. ";
        std::cin >> operation;
        std::cout << "\n" << "Enter the first integar: ";
        std::cin >> firstInt;
        std::cout << "\n" << "Enter the second integar: ";
        std::cin >> secondInt;
    }
    catch (...) {
        return 0;
    }


    if (operation == "divide") {
        result = divide(firstInt, secondInt);
    }

    else if (operation == "multiply") {
        result = multiply(firstInt, secondInt);
    }

    else if (operation == "add") {
        result = add(firstInt, secondInt);
    }

    else if (operation == "subtract") {
        result = subtract(firstInt, secondInt);
    }

    else {
        std::cout << "\n Error: Invalid Operation. Please try again.";
    }

    std::cout << "The result is: " << result << ". Have a nice day! \n";
}
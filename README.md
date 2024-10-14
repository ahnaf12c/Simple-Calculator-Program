# Simple-Calculator-Program

## Description
This project is a calculator that evaluates mathematical expressions consisting of addition, substraction, multiplication, division, exponentiation and also brackets. It allows users to input mathematical expressions using numbers and operators, evaluates the expression using a stack-based algorithm, and outputs the result. The calculator can handle both integer and floating-point numbers and provides basic error handling for invalid expressions and operations.

## Features
- **Expression Evaluation**: Supports basic arithmetic operations: addition, subtraction, multiplication, division, and exponentiation.
- **Error Handling**: Detects syntax errors, division by zero, and invalid characters.
- **User Commands**:
  - `'q'`: Exit the calculator
  - `'clr'`: Clear the current answer
  - `'ans'`: Show the answer of the last operation
  - `'h'`: Display help instructions

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/repository-name.git
   cd repository-name
2. Ensure you have Python 3.x installed
3. Run the executable in the 'dist' folder

## Usage
1. Start the program, and you will be prompted to enter a mathematical expression.
2. Enter your expression (e.g., 3 + 4).
3. The result will be displayed, or an error message will be shown if the expression is invalid.
4. Use the commands for additional functionality.

## Example
```
Please enter a postfix expression ('q' to exit, 'h' for help): 3 + 4
Result: 7.0
```

## Version
 - Version: Release 1.0.0

## Algorithm and the Working Logic behind the Calculator:
- At first it takes the expression as an input in the infix notation
- Then it converts the infix notation to Postfix notation, also known as Reverse Polish Notation
- Then it tokenizes and evaluates the Postfix notation
- Shows the Result or Error if the input was invalid

## Support
For any questions or issues, please create an issue in the GitHub repository or contact me via ahnaf101109@gmail.com

## Acknowledgments
- This project was inspired by my interest in the Postfix notation and the overall workings of a calculator.
- Special thanks to the online programming community and the internet for their valuable resources and support.
- **Links**:
  - https://en.wikipedia.org/wiki/Infix_notation
  - https://en.wikipedia.org/wiki/Reverse_Polish_notation
  - https://en.wikipedia.org/wiki/Polish_notation

## License
This project is licensed under the GNU GPL v3.0 License - see the LICENSE file for details.


# test_calculater - Simple Desktop Calculator

A basic calculator application built with Python and Tkinter. Performs arithmetic operations and includes a clear function.

## 📌 Features
- Basic arithmetic operations: `+`, `-`, `*`, `/`
- Exponentiation support (`^` is converted to `**`)
- Clear input field functionality (`C` button)
- Responsive GUI layout with grid system
- Error handling for invalid inputs

## 📦 Requirements
- Python 3.x
- Tkinter (included with standard Python installations)

## 🚀 How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/test_calculater.git
   ```
2. Navigate to the project directory:
   ```bash
   cd test_calculater
   ```
3. Run the application:
   ```bash
   python3 calculator.py
   ```

## 📝 Usage
- Click number buttons to input values
- Use operator buttons (`+`, `-`, `*`, `/`) to perform calculations
- Press `=` to see the result
- Press `C` to clear the input field

## ⚠️ Safety Note
The calculator uses Python's `eval()` function for expression evaluation. While this is convenient, it can execute arbitrary code. The implementation includes:
- Input sanitization through `^` → `**` conversion
- Basic error handling for invalid expressions
- No network or file system access

## 📄 License
This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

## 🛠️ Contributing
1. Fork the repository
2. Create a new branch for your feature/fix
3. Commit your changes
4. Push to your fork
5. Submit a pull request

## 📌 ToDo
- Add history of previous calculations
- Implement keyboard input support
- Add dark/light theme toggle
- Include unit tests
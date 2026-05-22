```markdown
# Employee Payroll & Management CLI

A robust command-line application for tracking employee data and processing payroll calculations with high financial precision. It leverages an Object-Oriented architecture to manage distinct pay structures for both full-time and part-time staff while maintaining an automated audit log of all system modifications.

## 🛠️ Tech Stack
- `Python 3.8+`
- `decimal` (Standard Library)
- `datetime` (Standard Library)

## 🚀 Key Features
- **Precision Financial Calculations**: Utilizes Python's `decimal` module to eliminate floating-point inaccuracies during gross pay, tax withholding, and benefit deduction computations.
- **Polymorphic Architecture**: Implements a clean class hierarchy with a base employee model and specialized derived classes tailored for salaried (Full-Time) and hourly (Part-Time) workers.
- **Automated Audit Logging**: Persists system state changes by recording timestamped entries for every added or updated employee to an external `employee_log.txt` file.
- **Interactive Data Management**: Features a resilient CLI menu with built-in input validation, allowing users to seamlessly add personnel, update compensation rates, and instantly recalculate net pay.

## 📦 Installation & Setup

```bash
# Clone the repository
git clone [https://github.com/your-username/employee-payroll-cli.git](https://github.com/your-username/employee-payroll-cli.git)

# Navigate to the project directory
cd employee-payroll-cli

# Execute the application (no external dependencies required)
python main.py

```

## 📝 License

MIT License

Copyright (c) 2026

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

```

```

# Smart Electricity Bill Generator Using Variadic Functions

## 1. Project Overview

The **Smart Electricity Bill Generator** is a web-based application developed to automate the calculation and generation of electricity bills. The system uses the C programming language and variadic functions to calculate total electricity consumption, while Python Flask handles backend processing and HTML and CSS provide an interactive user interface.

The project aims to demonstrate the integration of C programming with web technologies to develop a simple, efficient, and user-friendly electricity billing system.

## 2. Objectives

- To automate electricity bill calculation.
- To implement variadic functions using `stdarg.h` in C.
- To calculate total electricity consumption from multiple entries.
- To apply a predefined electricity tariff structure.
- To generate a detailed and printable electricity bill.
- To integrate C programming with Python Flask and web technologies.

## 3. Technologies Used

| Technology | Purpose |
|---|---|
| C Language | Electricity consumption and bill calculations |
| `stdarg.h` | Implementation of variadic functions |
| Python | Backend processing |
| Flask | Web application framework |
| HTML5 | Structure of the user interface |
| CSS3 | Styling and layout |
| GCC | Compilation of C program |

## 4. Main Features

- Customer information input.
- Electricity consumption entry.
- Variadic function-based total unit calculation.
- Automatic electricity charge calculation.
- Fixed charge and tax calculation.
- Detailed bill generation.
- Input validation and error handling.
- Printable electricity bill.

## 5. Electricity Tariff Structure

The project uses the following illustrative tariff rates:

| Units Consumed | Rate per Unit |
|---|---|
| 0–100 | ₹2.00 |
| 101–200 | ₹3.50 |
| 201–500 | ₹5.00 |
| Above 500 | ₹7.00 |

Additional charges:
- Fixed Charge: ₹50
- Tax: 5% of the subtotal.

*Note: These are sample tariff rates used for academic demonstration and do not represent an official electricity provider's tariff.*

## 6. Project Structure

```text
Smart-Electricity-Bill-Generator/
│
├── bill.c
├── main.py
├── requirements.txt
├── README.md
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
```

## 7. Working of the Project

1. The user enters customer details and electricity consumption.
2. The HTML form sends the information to the Flask backend.
3. Python processes the submitted information and communicates with the C executable.
4. The C program uses variadic functions to calculate total electricity units.
5. The program calculates energy charges according to the predefined tariff.
6. Fixed charges and applicable tax are added.
7. The final electricity bill is displayed on the web interface.

## 8. Installation and Execution

### Prerequisites
- Python 3
- GCC Compiler
- Flask
- Web Browser

### Installation

Install Flask:

```bash
pip install -r requirements.txt
```

### Compile the C Program

```bash
gcc bill.c -o billcalc
```

On Windows, use:

```bash
gcc bill.c -o billcalc.exe
```

### Run the Application

```bash
python main.py
```

Open the following address in your browser:

```text
http://127.0.0.1:3000
```

## 9. Future Enhancements

- Database integration for storing customer records.
- Monthly electricity consumption history.
- User authentication and account management.
- Downloadable PDF electricity bills.
- Integration with real electricity tariff data.

## 10. Conclusion

The Smart Electricity Bill Generator demonstrates how C programming concepts, particularly variadic functions, can be integrated with modern web technologies. It provides an automated approach to electricity bill calculation and generation while offering a simple and interactive user interface.

---

**Project Type:** MCA Mini Project  
**Domain:** Web Application Development  
**Core Concept:** Variadic Functions in C
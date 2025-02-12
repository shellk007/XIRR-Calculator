**XIRR Calculator**
**Description**
*This project is a simple GUI-based calculator built with Python and Tkinter that allows users to calculate the Extended Internal Rate of Return (XIRR) for a series of investments and a return amount. The user enters multiple investments with dates, and the calculator computes the XIRR based on these inputs.

**Features**
*User-friendly Tkinter GUI.
*Input for multiple investments and their respective dates.
*Input for return amount and calculation of XIRR.
*Display of investment details along with the calculated XIRR.

**Prerequisites**
Before running the application, ensure you have the following software and libraries installed:

*Python 3.6+ or above

**Required Python libraries:**
*tkinter (usually comes pre-installed with Python)
*scipy (for numerical methods)

**Installation Instructions**
**Step 1:Install Python (if not already installed)**
*Download and install Python from the official site: https://www.python.org/downloads/
*Ensure to check the option to add Python to your system PATH during installation.
**Step 2:Install the required libraries**
*To install the necessary Python libraries, use the following commands in your terminal/command prompt:**

pip install scipy
**Step 3:Download the project files**
*You can either clone this repository using Git or download the ZIP of the project from GitHub.

**To clone the repository:**

git clone https://github.com/your-username/xirr-calculator.git
**Step 4:Run the Application**
*Once the files are downloaded and the libraries installed, you can run the application with the following command:

python xirr_calculator.py
*This will launch the Tkinter-based GUI, and you can start entering your investments and returns.

**Usage Instructions**
*Investment Entry: When you run the application, it will prompt you to enter an investment. You can enter the amount and date of each investment.
*Return Amount: After entering all investments, you will be prompted to enter the return amount, which will be considered as the final cash flow.
*XIRR Calculation: Once the return amount is entered, the application will calculate the XIRR and display the result in a new window.
*Exit: You can exit the application by closing the main window.
**Example**
*Investment 1: $1,000 on 2021-01-01
*Investment 2: $1,500 on 2022-01-01
*Return Amount: $3,000 on 2025-01-01
*The app will calculate and display the XIRR based on these values.

**Error Handling**
*If any input is invalid (e.g., a non-numeric amount or an incorrect date format), an error message will be shown.
*If the XIRR calculation fails (e.g., no solution found), the app will display an error message.
**Contributing**
Contributions are welcome! To contribute to this project, follow these steps:

*Fork the repository.
*Create a new branch (git checkout -b feature-branch).
*Make your changes and commit them (git commit -am 'Add new feature').
*Push to the branch (git push origin feature-branch).
*Open a pull request.

**License**
This project is open-source and available under the MIT License. See the LICENSE file for more details.

**Contact Information**
Author: Shailesh Kaushik
Linkedin: https://www.linkedin.com/in/shailesh-kaushik-3262602a/
Youtube: https://www.youtube.com/@shaileshkaushik/featured

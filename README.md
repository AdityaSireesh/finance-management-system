# finance-management-system


# 💰 Finance Management System (FMS)

A Python-based desktop application for automated management of monthly household finances. This Finance Management System helps users track income, categorize expenses, monitor loans, observe savings and achieve budget.

---
## 🔑 Key Features
- Store and track balance amount and monthly income
- Categorize expenses (Food, Bills, Transport, Miscellaneous)
- Manage loans and repayment periods
- Set and monitor monthly savings
- Visualize financial summaries with charts

---

## Features

### 🔐 User Authentication
- Sign-up/login functionality with user-specific data files
- Passwords stored securely in binary files

### 🧾 Profile Setup
- Input and store:
  - Monthly salary
  - Budget goals
  - Initial balance

### 📊 Dashboard Overview
Displays:
- Current balance
- Total monthly expenses
- Budget goals
- Bar graph showing expense breakdown across:
  - Food
  - Transport
  - Bills
  - Miscellaneous
  - Loans

### 📉 Expense Tracking
- Categorize and log expenses for:
  - Food
  - Transportation
  - Bills
  - Miscellaneous
- Auto calculates total expenses and updates balance

### 💸 Loan Management
- Track loan type, amount and end date
- Automatically calculates monthly loan payments
- Expired loans are removed from the list automatically

### 📅 Monthly Summary
List of past months’:
- Total expenses
- Closing balance

### 📝 Update Profile
- Edit salary, budget goals and add/update current balance.

---

## 🖥️ Tech

| Component      | Technology                     |
|----------------|--------------------------------|
| GUI  | `customtkinter` module|
| Chart       | `matplotlib` module |
| Data Storage   | `pickle` module       |
| Time Handling  | `datetime` module              |

---

## 📂 File Structure
┣ 📄 FMS_main.py &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Main program
<br>
┣ 📄 MainFolder.dat &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Stores username-password pairs
<br>
┣ 📄 <user>.dat &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Stores per-user details

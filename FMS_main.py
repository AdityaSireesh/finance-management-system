import customtkinter as ctk
import tkinter
from tkinter import messagebox as m
import pickle
from datetime import datetime as dt
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def store(u):
    global m_user, m_salary, m_goal, m_balance, m_transactions, m_loans, m_month, m_year, m_expenses, m_loan_amt, n_month

    m_user = u
    u += ".dat"

    with open(u, "rb") as f1:
        sgb = pickle.load(f1)
        t = pickle.load(f1)
        l = pickle.load(f1)

    m_salary = float(sgb[0])
    m_goal = float(sgb[1])
    m_balance = float(sgb[2])
    m_expenses = 0.0
    m_transactions = t
    m_loans = l

    m_month = dt.now().strftime("%B")
    n_month = dt.now().month
    m_year = dt.now().year

    flag = True
    for i in t:
        if m_year in i.values() and m_month in i.values():
            flag = False
            dic_expense = i["expenses"]
            for j in dic_expense.values():
                m_expenses += j
    if flag:
        m_transactions.append(
            {"month": m_month, "year": m_year, "expenses": {"food": 0.0, "transport": 0.0, "bills": 0.0, "misc": 0.0},
             "total": 0.0, "bal": m_balance})
        month_change()

    m_loan_amt = 0.0
    for i in m_loans:
        m_loan_amt += i["amount"]
    m_expenses += m_loan_amt


def disp_error(e):
    error = ctk.CTkTextbox(app1, text_color="red")
    error.place(relx=0.5, rely=0.27, anchor=tkinter.CENTER)
    error.insert("0.0", e)
    error.configure(width=200, height=10, state="disabled")


def login_fun():
    u = user.get()
    p = pw.get()
    user_list = ""
    if u != "":
        try:
            with open("MainFolder.dat", "rb") as f1:
                user_list = pickle.load(f1)
        except:
            disp_error("No accounts found")
            return

        if u in user_list.keys():
            if p == user_list[u]:
                store(u)
                overview_ui()
            else:
                disp_error("Incorrect Password")
        else:
            disp_error("Username does not exist")


def login_ui():
    global app1, user, pw

    app1.destroy()

    app1 = ctk.CTkFrame(app, fg_color="transparent")
    app1.pack(fill="both", expand=True)

    login_frame = ctk.CTkFrame(app1, width=300, height=290, corner_radius=10)
    login_frame.place(relx=0.5, rely=0.5, anchor="center")
    login_frame.grid_propagate(False)

    user = ctk.CTkEntry(login_frame, width=260, placeholder_text="Username")
    user.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="ew")

    pw = ctk.CTkEntry(login_frame, width=260, placeholder_text="Password", show="*")
    pw.grid(row=1, column=0, padx=20, pady=(10, 20), sticky="ew")

    ctk.CTkButton(login_frame, text="Log in", command=login_fun).grid(row=2, column=0, padx=20, pady=(10, 40))

    ctk.CTkLabel(login_frame, text="Don't have an account?").grid(row=3, column=0, padx=20, pady=10)

    ctk.CTkButton(login_frame, text="Sign up", command=signup_ui).grid(row=4, column=0, padx=20, pady=(0, 20))


def signup_ui():
    global app1, name, pw

    app1.destroy()

    app1 = ctk.CTkFrame(app, fg_color="transparent")
    app1.pack(fill="both", expand=True)

    signup_frame = ctk.CTkFrame(app1, width=300, height=290, corner_radius=10)
    signup_frame.place(relx=0.5, rely=0.5, anchor="center")
    signup_frame.grid_propagate(False)

    name = ctk.CTkEntry(signup_frame, width=260, placeholder_text="Username")
    name.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="ew")

    pw = ctk.CTkEntry(signup_frame, width=260, placeholder_text="Password", show="*")
    pw.grid(row=1, column=0, padx=20, pady=(10, 20), sticky="ew")

    ctk.CTkButton(signup_frame, text="Sign up", command=sign_up).grid(row=4, column=0, padx=20, pady=(125, 20))


def sign_up():
    global sign_user

    N = name.get()
    if N != "":
        sign_user = N
        n = N + ".dat"

        try:
            with open("MainFolder.dat", "rb") as f1:
                user_list = pickle.load(f1)
        except:
            with open("MainFolder.dat", "wb") as f1:
                a = {}
                pickle.dump(a, f1)

        f1 = open("MainFolder.dat", "rb")
        user_list = pickle.load(f1)
        f1.close()
        if N in user_list.keys():
            disp_error("User already exists")
        else:
            password = pw.get()
            f2 = open("MainFolder.dat", "wb")
            user_list[N] = password
            pickle.dump(user_list, f2)
            with open(n, "wb") as f3:
                sgb = ["", "", ""]
                pickle.dump(sgb, f3)
                t = []
                pickle.dump(t, f3)
                l = []
                pickle.dump(l, f3)
            f2.close()
            details_ui()


def save_fun():
    s = salary.get()
    g = goal.get()
    b = balance.get()

    if "" not in [s, g, b]:
        details_user = sign_user
        details_user += ".dat"

        f1 = open(details_user, "rb")
        sgb = pickle.load(f1)
        t = pickle.load(f1)
        l = pickle.load(f1)
        f1.close()
        f1 = open(details_user, "wb")
        sgb = [s, g, b]
        pickle.dump(sgb, f1)
        pickle.dump(t, f1)
        pickle.dump(l, f1)
        f1.close()
        app1.destroy()
        login_ui()


def details_ui():
    global app1, salary, goal, balance

    app1.destroy()

    app1 = ctk.CTkFrame(app, fg_color="transparent")
    app1.pack(fill="both", expand=True)

    details_frame = ctk.CTkFrame(app1, width=300, height=290, corner_radius=10)
    details_frame.place(relx=0.5, rely=0.5, anchor="center")
    details_frame.grid_propagate(False)

    salary = ctk.CTkEntry(details_frame, width=260, placeholder_text="Monthly salary")
    salary.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="ew")

    goal = ctk.CTkEntry(details_frame, width=260, placeholder_text="Budget goal")
    goal.grid(row=1, column=0, padx=20, pady=(10, 10), sticky="ew")

    balance = ctk.CTkEntry(details_frame, width=260, placeholder_text="Current balance")
    balance.grid(row=2, column=0, padx=20, pady=(10, 20), sticky="ew")

    ctk.CTkButton(details_frame, text="Save", command=save_fun).grid(row=4, column=0, padx=20, pady=(80, 20))


def update_details_ui():
    global app1, update_salary_entry, update_goal_entry, add_balance, update_balance_entry

    app1.destroy()

    app1 = ctk.CTkFrame(app, fg_color="transparent")
    app1.pack(fill="both", expand=True)

    sidebar_ui()

    content = ctk.CTkFrame(app1, fg_color="transparent")
    content.pack(fill="both", expand=True)

    big_font = ("Arial", 36)
    normal_font = ("Arial", 20)

    ctk.CTkLabel(content, text=f"{m_user}", font=big_font).pack(anchor="nw", pady=(30, 0), padx=30)
    ctk.CTkLabel(content, text=f"{m_month} {m_year}", font=("Arial", 26)).pack(anchor="nw", pady=(5, 0), padx=30)

    salary_frame = ctk.CTkFrame(content, height=160, corner_radius=10)
    salary_frame.pack(fill="x", padx=30, pady=(30, 0))
    salary_frame.pack_propagate(False)

    salary_left = ctk.CTkFrame(salary_frame, fg_color="transparent")
    salary_left.pack(side="left", expand=True, fill="both", padx=10, pady=10)

    ctk.CTkLabel(salary_left, text="Current Salary:", font=normal_font, anchor="w").pack(anchor="nw")
    ctk.CTkLabel(salary_left, text=f"₹{m_salary}", font=big_font, anchor="w").pack(anchor="nw", pady=(5, 0))

    salary_right = ctk.CTkFrame(salary_frame, fg_color="transparent")
    salary_right.pack(side="right", expand=True, fill="both", padx=10, pady=10)

    update_salary_entry = ctk.CTkEntry(salary_right, placeholder_text="Update Monthly Salary", font=("Arial", 16),
                                       width=180, height=30)
    update_salary_entry.pack(pady=(15, 8))
    ctk.CTkButton(salary_right, text="Update", font=("Arial", 16), width=180, height=30, command=update_fun).pack()

    goal_frame = ctk.CTkFrame(content, height=160, corner_radius=10)
    goal_frame.pack(fill="x", padx=30, pady=(30, 0))
    goal_frame.pack_propagate(False)

    goal_left = ctk.CTkFrame(goal_frame, fg_color="transparent")
    goal_left.pack(side="left", expand=True, fill="both", padx=10, pady=10)

    ctk.CTkLabel(goal_left, text="Monthly Goal:", font=normal_font, anchor="w").pack(anchor="nw")
    ctk.CTkLabel(goal_left, text=f"₹{m_goal}", font=big_font, anchor="w").pack(anchor="nw", pady=(5, 0))

    goal_right = ctk.CTkFrame(goal_frame, fg_color="transparent")
    goal_right.pack(side="right", expand=True, fill="both", padx=10, pady=10)

    update_goal_entry = ctk.CTkEntry(goal_right, placeholder_text="Update Monthly Goal", font=("Arial", 16), width=180,
                                     height=30)
    update_goal_entry.pack(pady=(15, 8))
    ctk.CTkButton(goal_right, text="Update", font=("Arial", 16), width=180, height=30, command=update_fun).pack()

    balance_frame = ctk.CTkFrame(content, height=200, corner_radius=10)
    balance_frame.pack(fill="x", padx=30, pady=(30, 30))
    balance_frame.pack_propagate(False)

    balance_left = ctk.CTkFrame(balance_frame, fg_color="transparent")
    balance_left.pack(side="left", expand=True, fill="both", padx=10, pady=10)

    ctk.CTkLabel(balance_left, text="Monthly Balance:", font=normal_font, anchor="w").pack(anchor="nw")
    ctk.CTkLabel(balance_left, text=f"₹{m_balance}", font=big_font, anchor="w").pack(anchor="nw", pady=(5, 0))

    balance_right = ctk.CTkFrame(balance_frame, fg_color="transparent")
    balance_right.pack(side="right", expand=True, fill="both", padx=10, pady=10)

    add_balance_frame = ctk.CTkFrame(balance_right, fg_color="transparent")
    add_balance_frame.pack(pady=(10, 10))

    add_balance = ctk.CTkEntry(add_balance_frame, placeholder_text="Add Balance", font=("Arial", 16), width=120,
                               height=30)
    add_balance.pack(side="left", padx=(0, 5))

    ctk.CTkButton(add_balance_frame, text="+", font=("Arial", 16), width=50, height=30, command=update_fun).pack(
        side="left")

    update_balance_entry = ctk.CTkEntry(balance_right, placeholder_text="Update Balance", font=("Arial", 16), width=180,
                                        height=30)
    update_balance_entry.pack(pady=(10, 8))
    ctk.CTkButton(balance_right, text="Update", font=("Arial", 16), width=180, height=30, command=update_fun).pack()



def update_fun():
    global m_salary, m_goal, m_balance

    new_s = update_salary_entry.get()
    if (new_s != ""):
        m_salary = float(new_s)
        update_salary_entry.delete(0, "end")

    new_g = update_goal_entry.get()
    if (new_g != ""):
        print("Goal")
        m_goal = float(new_g)
        update_goal_entry.delete(0, "end")

    new_b = add_balance.get()
    if (new_b != ""):
        m_balance += float(new_b)
        add_balance.delete(0, "end")

    newbalance = update_balance_entry.get()
    if (newbalance != ""):
        m_balance = float(newbalance)
        update_balance_entry.delete(0, "end")

    overview_ui()


def sidebar_ui():
    left = ctk.CTkFrame(app1, width=300, height=900, corner_radius=0)
    left.pack(side="left", fill="y", padx=(0, 10))
    left.pack_propagate(False)

    ctk.CTkButton(left, text="Overview", width=200, height=35, command=overview_ui).pack(padx=50, pady=(50, 0))
    ctk.CTkButton(left, text="Expenses", width=200, height=35, command=expenses_ui).pack(padx=50, pady=(50, 0))
    ctk.CTkButton(left, text="Monthly Summary", width=200, height=35, command=months_ui).pack(padx=50, pady=(50, 0))
    ctk.CTkButton(left, text="Loans", width=200, height=35, command=loans_ui).pack(padx=50, pady=(50, 0))
    ctk.CTkButton(left, text="Update Profile", width=200, height=35, command=update_details_ui).pack(side="bottom",
                                                                                                     padx=50,
                                                                                                     pady=(10, 50))
    ctk.CTkLabel(left, text=m_user, font=("Arial", 20)).pack(side="bottom", padx=50, pady=(10, 0))


def overview_ui():
    global app1

    app1.destroy()

    app1 = ctk.CTkFrame(app, fg_color="transparent")
    app1.pack(fill="both", expand=True)

    sidebar_ui()

    content = ctk.CTkFrame(app1, fg_color="transparent")
    content.pack(fill="both", expand=True)

    ctk.CTkLabel(content, text=f"Overview | {m_month} {m_year}", font=("Arial", 30)).pack(anchor="nw", pady=30, padx=30)

    top_frame = ctk.CTkFrame(content, fg_color="transparent")
    top_frame.pack(fill="both", expand=True, padx=30)
    top_frame.grid_columnconfigure((0, 1, 2), weight=1)
    top_frame.grid_rowconfigure(0, weight=1)

    box1 = ctk.CTkFrame(top_frame, corner_radius=10)
    box1.grid(row=0, column=0, padx=(0, 30), sticky="news")
    box1.grid_propagate(False)
    ctk.CTkLabel(box1, text="Total Expense", font=("Arial", 20)).pack(anchor="w", padx=10, pady=10)
    ctk.CTkLabel(box1, text=f"₹ {m_expenses}", font=("Arial", 60), text_color="green").pack(side="bottom", anchor="se",
                                                                                            padx=20, pady=10)

    box2 = ctk.CTkFrame(top_frame, corner_radius=10)
    box2.grid(row=0, column=1, padx=0, sticky="news")
    box2.grid_propagate(False)
    ctk.CTkLabel(box2, text="Balance", font=("Arial", 20)).pack(anchor="w", padx=10, pady=10)
    if m_balance > 0:
        ctk.CTkLabel(box2, text=f"₹ {m_balance}", font=("Arial", 60), text_color="green").pack(side="bottom", anchor="se",
                                                                                           padx=20, pady=10)
    else:
        ctk.CTkLabel(box2, text=f"₹ {m_balance}", font=("Arial", 60), text_color="red").pack(side="bottom",
                                                                                               anchor="se",
                                                                                               padx=20, pady=10)

    box3 = ctk.CTkFrame(top_frame, corner_radius=10)
    box3.grid(row=0, column=2, padx=(30, 0), sticky="news")
    box3.grid_propagate(False)
    ctk.CTkLabel(box3, text="Budget Goal", font=("Arial", 20)).pack(anchor="w", padx=10, pady=10)
    ctk.CTkLabel(box3, text=f"₹ {m_goal}", font=("Arial", 60), text_color="green").pack(side="bottom", anchor="se",
                                                                                        padx=20, pady=10)

    bottom = ctk.CTkFrame(content, height=600, corner_radius=10, )
    bottom.pack(fill="both", expand=True, padx=30, pady=30, anchor="s")
    bottom.pack_propagate(False)

    sectors = ["Food", "Transportation", "Bills", "Miscellaneous", "Loans"]
    amounts = []
    for i in m_transactions:
        if m_year in i.values() and m_month in i.values():
            dic_expense = i["expenses"]
            for j in dic_expense.values():
                amounts.append(j)
    loan_total = 0.0
    for i in m_loans:
        loan_total += i["amount"]
    amounts.append(loan_total)

    fig, ax = plt.subplots(figsize=(10, 4))
    bars = ax.bar(sectors, amounts, color="gold")
    ax.set_xlabel("Sectors")
    ax.set_ylabel("Values")
    ax.set_title("Expenses")
    ax.bar_label(bars, padding=-2)

    canvas = FigureCanvasTkAgg(fig, master=bottom)
    canvas.draw()
    canvas.get_tk_widget().pack(pady=150)

    app.protocol("WM_DELETE_WINDOW", plt.close(fig))


def food_fun():
    global m_expenses, m_balance
    f = food.get()

    if f != "" and float(f) > 0:
        food.delete(0, "end")
        for i in m_transactions:
            if m_year in i.values() and m_month in i.values():
                i["expenses"]["food"] += float(f)
        m_expenses += float(f)
        m_balance -= float(f)
        update_total()

    else:
        m.showinfo("Error", "Invalid Input              ")


def transport_fun():
    global m_expenses, m_balance
    t = transport.get()
    if t != "" and float(t) > 0:
        transport.delete(0, "end")
        for i in m_transactions:
            if m_year in i.values() and m_month in i.values():
                i["expenses"]["transport"] += float(t)
        m_expenses += float(t)
        m_balance -= float(t)
        update_total()

    else:
        m.showinfo("Error", "Invalid Input              ")


def bills_fun():
    global m_expenses, m_balance
    b = bills.get()
    if b != "" and float(b) > 0:
        bills.delete(0, "end")
        for i in m_transactions:
            if m_year in i.values() and m_month in i.values():
                i["expenses"]["bills"] += float(b)
        m_expenses += float(b)
        m_balance -= float(b)
        update_total()
    else:
        m.showinfo("Error", "Invalid Input              ")


def misc_fun():
    global m_expenses, m_balance
    m = misc.get()
    if m != "" and float(m) > 0:
        misc.delete(0, "end")
        for i in m_transactions:
            if m_year in i.values() and m_month in i.values():
                i["expenses"]["misc"] += float(m)
        m_expenses += float(m)
        m_balance -= float(m)
        update_total()

    else:
        m.showinfo("Error", "Invalid Input              ")


def expenses_ui():
    global app1, exp1, exp2, exp3, exp4, food, transport, bills, misc, food_total, transport_total, bills_total, misc_total

    app1.destroy()

    app1 = ctk.CTkFrame(app, fg_color="transparent")
    app1.pack(fill="both", expand=True)

    sidebar_ui()

    content = ctk.CTkFrame(app1, fg_color="transparent")
    content.pack(fill="both", expand=True)

    ctk.CTkLabel(content, text=f"Expenses | {m_month} {m_year}", font=("Arial", 30)).pack(anchor="nw", pady=30, padx=30)

    grid_frame = ctk.CTkFrame(content, fg_color="transparent")
    grid_frame.pack(fill="both", expand=True, padx=30, pady=(0, 30))
    grid_frame.grid_rowconfigure((0, 1), weight=1)
    grid_frame.grid_columnconfigure((0, 1), weight=1)

    exp1 = ctk.CTkFrame(grid_frame, corner_radius=10)
    exp1.grid(row=0, column=0, padx=(0, 15), pady=15, sticky="nsew")

    exp2 = ctk.CTkFrame(grid_frame, corner_radius=10)
    exp2.grid(row=0, column=1, padx=(15, 0), pady=15, sticky="nsew")

    exp3 = ctk.CTkFrame(grid_frame, corner_radius=10)
    exp3.grid(row=1, column=0, padx=(0, 15), pady=150, sticky="nsew")

    exp4 = ctk.CTkFrame(grid_frame, corner_radius=10)
    exp4.grid(row=1, column=1, padx=(15, 0), pady=150, sticky="nsew")

    ctk.CTkLabel(exp1, text="Food", font=ctk.CTkFont(size=30), text_color="lightgreen").place(relx=0.05, rely=0.1)
    ctk.CTkLabel(exp2, text="Transportation", font=ctk.CTkFont(size=30), text_color="orange").place(relx=0.05, rely=0.1)
    ctk.CTkLabel(exp3, text="Bills", font=ctk.CTkFont(size=30)).place(relx=0.05, rely=0.1)
    ctk.CTkLabel(exp4, text="Miscellaneous", font=ctk.CTkFont(size=30), text_color="yellow").place(relx=0.05, rely=0.1)

    ctk.CTkButton(exp1, text="+", font=ctk.CTkFont(size=20), width=30, corner_radius=50, command=food_fun).place(
        relx=0.8, rely=0.68)
    ctk.CTkButton(exp2, text="+", font=ctk.CTkFont(size=20), width=30, corner_radius=50, command=transport_fun).place(
        relx=0.8, rely=0.68)
    ctk.CTkButton(exp3, text="+", font=ctk.CTkFont(size=20), width=30, corner_radius=50, command=bills_fun).place(
        relx=0.8, rely=0.68)
    ctk.CTkButton(exp4, text="+", font=ctk.CTkFont(size=20), width=30, corner_radius=50, command=misc_fun).place(
        relx=0.8, rely=0.68)

    food = ctk.CTkEntry(exp1, width=250, placeholder_text="Enter Amount")
    food.place(relx=0.05, rely=0.7)

    transport = ctk.CTkEntry(exp2, width=250, placeholder_text="Enter Amount")
    transport.place(relx=0.05, rely=0.7)

    bills = ctk.CTkEntry(exp3, width=250, placeholder_text="Enter Amount")
    bills.place(relx=0.05, rely=0.7)

    misc = ctk.CTkEntry(exp4, width=250, placeholder_text="Enter Amount")
    misc.place(relx=0.05, rely=0.7)

    update_total()


def update_total():
    for i in m_transactions:
        if m_year in i.values() and m_month in i.values():
            global food_total, transport_total, bills_total, misc_total

            food_total = ctk.CTkLabel(exp1, text=f"Total: Rs.{i['expenses']['food']}", font=ctk.CTkFont(size=30),
                                      text_color="lightgreen")
            food_total.place(relx=0.05, rely=0.4)

            transport_total = ctk.CTkLabel(exp2, text=f"Total: Rs.{i['expenses']['transport']}",
                                           font=ctk.CTkFont(size=30), text_color="orange")
            transport_total.place(relx=0.05, rely=0.4)

            bills_total = ctk.CTkLabel(exp3, text=f"Total: Rs.{i['expenses']['bills']}", font=ctk.CTkFont(size=30))
            bills_total.place(relx=0.06, rely=0.4)

            misc_total = ctk.CTkLabel(exp4, text=f"Total: Rs.{i['expenses']['misc']}", font=ctk.CTkFont(size=30),
                                      text_color="yellow")
            misc_total.place(relx=0.05, rely=0.4)


def months_ui():
    global app1, m_transactions

    app1.destroy()

    app1 = ctk.CTkFrame(app, fg_color="transparent")
    app1.pack(fill="both", expand=True)

    sidebar_ui()

    content = ctk.CTkFrame(app1, fg_color="transparent")
    content.pack(fill="both", expand=True)

    ctk.CTkLabel(content, text="Monthly Summary", font=("Arial", 30)).pack(anchor="nw", pady=(30, 0), padx=30)

    top = ctk.CTkFrame(content, height=600, corner_radius=10)
    top.pack(fill="both", expand=True, padx=30, pady=30)
    top.pack_propagate(False)

    summary_scroll = ctk.CTkScrollableFrame(top, corner_radius=10)
    summary_scroll.pack(fill="both", expand=True, padx=20, pady=20)
    summary_scroll.grid_columnconfigure(0, weight=1)

    for data in m_transactions:
        summary_frame = ctk.CTkFrame(summary_scroll, height=100, corner_radius=10)
        summary_frame.pack(fill="x", padx=10, pady=10)

        ctk.CTkLabel(summary_frame, text=f"{data['month']} {data['year']}", font=("Arial", 20, "bold")).pack(anchor="w",
                                                                                                             pady=(
                                                                                                             10, 5),
                                                                                                             padx=10)

        ctk.CTkLabel(summary_frame, text=f"Expenses: ₹{data['total']}  |  Balance: ₹{data['bal']}",
                     font=("Arial", 18)).pack(anchor="w", padx=10)


def newloan_fun():
    global m_expenses, m_balance, m_loan_amt
    type_loan = loan_type_option.get()
    amt_loan = amtl_e.get()
    end_loan = endl_e.get()

    if "" not in [type_loan, amt_loan, end_loan]:
        if float(amt_loan) > 0:
            mm, yy = end_loan.split("/")
            if int(mm) > 0 and int(mm) < 13:
                if (int(yy) == m_year and int(mm) >= n_month) or int(yy) > m_year:
                    amtl_e.delete(0, "end")
                    endl_e.delete(0, "end")
                    loan_data = {"type": type_loan, "amount": float(amt_loan), "end": end_loan}
                    m_loans.append(loan_data)
                    m_expenses += float(amt_loan)
                    m_balance -= float(amt_loan)
                    m_loan_amt += float(amt_loan)

                    update_loan()
                else:
                    m.showinfo("Error", "Invalid Input              ")
            else:
                m.showinfo("Error", "Invalid Input              ")
        else:
            m.showinfo("Error", "Invalid Input              ")


def loans_ui():
    global app1, loan_type_option, amtl_e, endl_e, loan_scroll

    app1.destroy()

    app1 = ctk.CTkFrame(app, fg_color="transparent")
    app1.pack(fill="both", expand=True)

    sidebar_ui()

    content = ctk.CTkFrame(app1, fg_color="transparent")
    content.pack(fill="both", expand=True)

    ctk.CTkLabel(content, text=f"Loans | {m_month} {m_year}", font=("Arial", 30)).pack(anchor="nw", pady=(30, 0),
                                                                                       padx=30)

    top = ctk.CTkFrame(content, height=450, corner_radius=10)
    top.pack(fill="both", padx=30, pady=(30, 0))
    top.pack_propagate(False)

    loan_scroll = ctk.CTkScrollableFrame(top, corner_radius=10)
    loan_scroll.pack(fill="both", expand=True, padx=20, pady=20)
    loan_scroll.grid_columnconfigure(0, weight=1)

    for data in m_loans:
        loanlist_frame = ctk.CTkFrame(loan_scroll, height=100, corner_radius=10)
        loanlist_frame.pack(fill="x", padx=10, pady=10)
        ctk.CTkLabel(loanlist_frame, text=f"{data['type']} Loan", font=("Arial", 20, "bold")).pack(anchor="w",
                                                                                                   pady=(10, 5),
                                                                                                   padx=10)
        ctk.CTkLabel(loanlist_frame, text=f"Amount: ₹{data['amount']} | End date: {data['end']}",
                     font=("Arial", 18)).pack(anchor="w", padx=10)


    bottom = ctk.CTkFrame(content, height=300, corner_radius=10)
    bottom.pack(fill="both", padx=30, pady=30)
    bottom.pack_propagate(False)

    typel_frame = ctk.CTkFrame(bottom, corner_radius=10)
    typel_frame.place(relx=0.05, rely=0.1, relwidth=0.25, relheight=0.5)

    amtl_frame = ctk.CTkFrame(bottom, corner_radius=10)
    amtl_frame.place(relx=0.375, rely=0.1, relwidth=0.25, relheight=0.5)

    endl_frame = ctk.CTkFrame(bottom, corner_radius=10)
    endl_frame.place(relx=0.7, rely=0.1, relwidth=0.25, relheight=0.5)

    ctk.CTkLabel(typel_frame, text="Type of Loan:", font=("Arial", 18)).pack(pady=(10, 5))
    loan_type_option = ctk.CTkOptionMenu(typel_frame, values=["Vehicle", "Home", "Education", "Personal"],
                                         font=("Arial", 18), width=300, height=30)
    loan_type_option.set("Vehicle")
    loan_type_option.pack(pady=5)

    ctk.CTkLabel(amtl_frame, text="Amount per Month:", font=("Arial", 18)).pack(pady=(10, 5))
    amtl_e = ctk.CTkEntry(amtl_frame, placeholder_text="₹", font=("Arial", 18), width=300, height=30)
    amtl_e.pack(pady=5)

    ctk.CTkLabel(endl_frame, text="End Date:", font=("Arial", 18)).pack(pady=(10, 5))
    endl_e = ctk.CTkEntry(endl_frame, placeholder_text="MM/YYYY", font=("Arial", 18), width=300, height=30)
    endl_e.pack(pady=5)

    loan_b = ctk.CTkButton(bottom, text="Add", font=("Arial", 18), width=300, height=40, command=newloan_fun)
    loan_b.place(relx=0.4, rely=0.75)


def update_loan():
    for widget in loan_scroll.winfo_children():
        widget.destroy()

    for data in m_loans:
        loanlist_frame = ctk.CTkFrame(loan_scroll, height=100, corner_radius=10)
        loanlist_frame.pack(fill="x", padx=10, pady=10)
        ctk.CTkLabel(loanlist_frame, text=f"{data['type']} Loan", font=("Arial", 20, "bold")).pack(anchor="w",
                                                                                                   pady=(10, 5),
                                                                                                   padx=10)
        ctk.CTkLabel(loanlist_frame, text=f"Amount: ₹{data['amount']} | End date: {data['end']}",
                     font=("Arial", 18)).pack(anchor="w", padx=10)


def month_change():
    global m_balance, m_salary, m_transactions, m_loans, m_loan_amt, m_month, m_year

    m_balance += m_salary

    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
              "November", "December"]
    x_month = ""
    x_year = m_year
    for i in range(len(months)):
        if months[i] == m_month:
            x_month = months[i - 1]
    if x_month == "December":
        x_year -= 1

    c = 0
    length = len(m_loans)
    while c < length:
        z = m_loans[c]
        z = z["end"]
        z = z.split("/")
        z1 = int(z[0])
        z2 = int(z[1])
        if x_year == z2 and x_month == months[z1 - 1]:
            del m_loans[c]
            length -= 1
            continue
        c += 1

    m_loan_amt = 0.0
    for i in m_loans:
        m_loan_amt += i["amount"]

    m_balance -= m_loan_amt

def start_ui():
    global app1

    app1 = ctk.CTkFrame(app, fg_color="transparent")
    app1.pack(fill="both", expand=True)

    name1 = ctk.CTkLabel(app1, text="Finance Management System", text_color="skyblue", font=("Arial Black", 50))
    name1.place(relx=0.5, rely=0.45, anchor=tkinter.CENTER)
    name2 = ctk.CTkLabel(app1, text="by Aditya", text_color="gold", font=("Courier New", 30))
    name2.place(relx=0.5, rely=0.52, anchor=tkinter.CENTER)

    app1.after(3000, login_ui)



global m_user, m_salary, m_goal, m_balance, m_transactions, m_loans, m_year, m_month, m_expenses

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

app = ctk.CTk()
app.title("FMS")
app.geometry("1910x1080")

start_ui()

app.mainloop()


try:
    with open(m_user + ".dat", "wb") as file:
        m_sgb = [m_salary, m_goal, m_balance]
        for i in m_transactions:
            if m_year in i.values() and m_month in i.values():
                i["total"] = m_expenses
                i["bal"] = m_balance

        pickle.dump(m_sgb, file)
        pickle.dump(m_transactions, file)
        pickle.dump(m_loans, file)
except:
    print("")
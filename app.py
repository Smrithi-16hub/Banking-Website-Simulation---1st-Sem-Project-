from flask import Flask, render_template, request, redirect, url_for, flash
import banking  # import your original banking.py file

app = Flask(__name__)
app.secret_key = "super-cute-secret"  # needed for flash messages

@app.route("/")
def index():
    # Overview stats
    total_accounts = len(banking.accounts)
    next_acc = banking.next_account_number
    highest = None
    if banking.accounts:
        highest = max(banking.accounts, key=lambda a: a["balance"])
    return render_template("index.html", total_accounts=total_accounts, next_acc=next_acc, highest=highest)

@app.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        name = request.form.get("holder_name", "").strip()
        balance_raw = request.form.get("initial_balance", "0").strip()
        try:
            balance = float(balance_raw)
            if balance < 0:
                raise ValueError("Balance cannot be negative.")
        except ValueError:
            flash("Please enter a valid non-negative amount.", "error")
            return redirect(url_for("create"))
        if not name:
            flash("Account holder name is required.", "error")
            return redirect(url_for("create"))
        banking.create_account(name, balance)
        flash(f"Account created for {name}! 🎉", "success")
        return redirect(url_for("accounts"))
    return render_template("create.html")

@app.route("/check", methods=["GET", "POST"])
def check():
    account = None
    if request.method == "POST":
        acc_raw = request.form.get("account_number", "").strip()
        try:
            acc_num = int(acc_raw)
        except ValueError:
            flash("Please enter a valid account number.", "error")
            return redirect(url_for("check"))
        account = banking.find_account(acc_num)
        if not account:
            flash("Account not found.", "error")
        else:
            flash(f"Balance fetched for {account['holder_name']} 💫", "info")
    return render_template("check.html", account=account)

@app.route("/deposit", methods=["GET", "POST"])
def deposit():
    if request.method == "POST":
        acc_raw = request.form.get("account_number", "").strip()
        amt_raw = request.form.get("amount", "").strip()
        try:
            acc_num = int(acc_raw)
            amount = float(amt_raw)
            if amount <= 0:
                raise ValueError("Amount must be positive.")
        except ValueError:
            flash("Enter a valid account number and positive amount.", "error")
            return redirect(url_for("deposit"))

        account = banking.find_account(acc_num)
        if not account:
            flash("Account not found.", "error")
            return redirect(url_for("deposit"))
        banking.deposit_money(acc_num, amount)
        flash(f"Deposited {amount} to Acc {acc_num} ✨", "success")
        return redirect(url_for("accounts"))
    return render_template("deposit.html")

@app.route("/withdraw", methods=["GET", "POST"])
def withdraw():
    if request.method == "POST":
        acc_raw = request.form.get("account_number", "").strip()
        amt_raw = request.form.get("amount", "").strip()
        try:
            acc_num = int(acc_raw)
            amount = float(amt_raw)
            if amount <= 0:
                raise ValueError("Amount must be positive.")
        except ValueError:
            flash("Enter a valid account number and positive amount.", "error")
            return redirect(url_for("withdraw"))

        account = banking.find_account(acc_num)
        if not account:
            flash("Account not found.", "error")
            return redirect(url_for("withdraw"))
        if account["balance"] < amount:
            flash("Insufficient balance.", "error")
            return redirect(url_for("withdraw"))

        banking.withdraw_money(acc_num, amount)
        flash(f"Withdrawn {amount} from Acc {acc_num} 🌸", "success")
        return redirect(url_for("accounts"))
    return render_template("withdraw.html")

@app.route("/accounts")
def accounts():
    return render_template("accounts.html", accounts=banking.accounts)

@app.route("/highest")
def highest():
    highest_acc = None
    if banking.accounts:
        highest_acc = max(banking.accounts, key=lambda a: a["balance"])
    return render_template("highest.html", highest=highest_acc)

if __name__ == "__main__":
    app.run(debug=True)

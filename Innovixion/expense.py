class ExpenseSharingApp:
    def __init__(self):
        self.expenses = {}

    def add_expense(self, payer, amount, recipients):
        if payer not in self.expenses:
            self.expenses[payer] = {}
        for recipient in recipients:
            if recipient not in self.expenses[payer]:
                self.expenses[payer][recipient] = 0
            self.expenses[payer][recipient] += amount / len(recipients)

    def split_bill(self, payer, total_amount, recipients):
        split_amount = total_amount / len(recipients)
        for recipient in recipients:
            if recipient != payer:
                self.add_expense(payer, split_amount, [recipient])

    def display_balance(self):
        print("Expense Balance:")
        for payer, recipients in self.expenses.items():
            for recipient, amount in recipients.items():
                print("{} owes {} ${}".format(recipient, payer, amount))

def main():
    app = ExpenseSharingApp()
    while True:
        print("\n1. Add Expense")
        print("2. Split Bill")
        print("3. Display Balance")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            payer = input("Enter payer's name: ")
            amount = float(input("Enter the total amount: "))
            recipients = input("Enter comma-separated recipients' names: ").split(',')
            app.add_expense(payer, amount, recipients)
        elif choice == '2':
            payer = input("Enter payer's name: ")
            total_amount = float(input("Enter the total bill amount: "))
            recipients = input("Enter comma-separated recipients' names: ").split(',')
            app.split_bill(payer, total_amount, recipients)
        elif choice == '3':
            app.display_balance()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()

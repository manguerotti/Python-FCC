class Category:
    def __init__(self,name):
        self.ledger = []
        self.name = name

    def deposit(self, amount, description=""):
           self.ledger.append({"amount": amount, "description" : description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False      

    def get_balance(self):
        balance = 0
        for item in self.ledger:
            balance += item["amount"]
        return balance

    def check_funds(self, amount):
        if self.get_balance() >= amount:
            return True
        else:
            return False
        
    def __str__(self):
        total=0
        output = ""

        title = f"**************{self.name}*************\n"
        output += title.center(30," ") + "\n"
        for item in self.ledger:
            description = item["description"][:23].ljust(23)
            amount = format(item["amount"], ".2f").rjust(7)[:7]
            output += f"{description}{amount}\n"
            total += item["amount"]
        output += f"Total: {format(total, '.2f')}\n"
        
        return output


def create_spend_chart(categories):
    # Calculate percentage spent in each category
    withdrawals = []
    category_names = []
    for category in categories:
        withdrawals.append(sum(item["amount"] for item in category.ledger if item["amount"] < 0))
        category_names.append(category.name)
    total_withdrawals = sum(withdrawals)
    percentages = [withdrawal / total_withdrawals * 100 for withdrawal in withdrawals]

    # Create chart
    chart = "Percentage spent by category\n"
    for i in range(100, -10, -10):
        chart += str(i).rjust(3) + "| "
        for percentage in percentages:
            if percentage >= i:
                chart += "o  "
            else:
                chart += "   "
        chart += "\n"
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    # Find longest category name
    max_length = max([len(name) for name in category_names])

    # Add category names to chart
    for i in range(max_length):
        chart += "     "
        for name in category_names:
            if i < len(name):
                chart += name[i] + "  "
            else:
                chart += "   "
        if i < max_length - 1:
            chart += "\n"

    return chart


food_category = Category("Food")
food_category.deposit(1000, "initial deposit")
food_category.withdraw(10.15, "groceries")
food_category.withdraw(15.89, "restaurant and more food for dessert")
food_category.withdraw(23.50, "more groceries")
food_category.withdraw(50.95, "some nice restaurants")
clothing_category = Category("Clothing")
clothing_category.deposit(500, "initial deposit")
clothing_category.withdraw(25.55, "shirt")
clothing_category.withdraw(100, "pants")
auto_category = Category("Auto")
auto_category.deposit(1000, "initial deposit")
auto_category.withdraw(15, "insurance")
auto_category.withdraw(50, "gasoline")
categories = [food_category, clothing_category, auto_category]

print(create_spend_chart(categories))

         
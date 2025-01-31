from . import Expense
import collections
import matplotlib.pyplot as plt

expences = Expense.Expenses()
expences.read_expenses('data\spending_data.csv')

spending_categories = []

for expence in expences.list:
    spending_categories.append(expence.category)

spending_counter = collections.Counter(spending_categories)
top5 = spending_counter.most_common(5)

categories, count = zip(*top5)

fig = plt.figure()
plt.bar(categories, count, width=0.4)
plt.title('# of Purchases by Category')
plt.show()
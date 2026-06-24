import numpy as np
import matplotlib.pyplot as plt

# plt.grid(True)
# plt.show()

# =np.linspace(0,10,100)
# y =np.sin(x)

# plt.plot(x,y, label='sin(x)',color='red', linestyle='--')
# plt.title="sin values"
# plt.xlabel='X-axis'
# plt.ylabel('Y-axis')
# plt.legend()

# x = np.random.rand(50)
# y = np.random.rand(50)
# plt.scatter(x,y)
# plt.show()


# categories = ["A","B","C","D"]
# values = [10,20,4,30]

# plt.bar(categories,values, color = "red")
# plt.title("bar graph")
# plt.xlabel("categories")
# plt.ylabel("values")
# plt.show()

labels = ["pyhton","java","c","ruby"]
size = [50,30,15,5]
plt.pie(size,labels=labels,autopct='%1.1f%%',startangle=140)
plt.show()
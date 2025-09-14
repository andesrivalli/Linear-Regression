import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
x=np.array([[1],[2],[3],[4],[5]])
y=np.array([30,40,50,60,70])
model=LinearRegression()
model.fit(x,y)
pred=model.predict([[6]])
print(pred)
plt.scatter(x,y,color='hotpink')
plt.plot(x,model.predict(x),color='green')
plt.xlabel('Study Hours')
plt.ylabel('Marks')
plt.title('Linear Regresion')
plt.show()
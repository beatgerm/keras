# 1. 데이터

import numpy as np
x_train = np.array([1,2,3,4,5,6,7,8,9,10])
y_train = np.array([1,2,3,4,5,6,7,8,9,10])
x_test = np.array([11,12,13,14,15,16,17,18,19,20]) 
y_test = np.array([11,12,13,14,15,16,17,18,19,20])
x_val = np.array([101,102,103,104,105])
y_val = np.array([101,107,103,204,1115])

# 2. 모델 구성

from keras.models import Sequential
from keras.layers import Dense
model = Sequential()



# x_predict = np.array([21,22,23,24,25])


# model.add(Dense(500, input_dim=1, activation='relu'))
model.add(Dense(5, input_shape=(1, ), activation='relu'))
model.add(Dense(1000))
model.add(Dense(3))
model.add(Dense(1000))
model.add(Dense(4))
model.add(Dense(1))

# model.summary()
#3. 훈련
model.compile(loss='mse', optimizer='adam', metrics=['mse'])#metrics=['accuracy'])

model.fit(x_train,y_train, epochs=100, batch_size=1, validation_data=(x_val, y_val))

#4. 평가 예측
loss, mse = model.evaluate(x_test, y_test, batch_size=1) # a[0], a[1]
print("mse : ", mse)
print("loss : ", loss)

y_predict = model.predict(x_test)
print(y_predict)

# RMSE 구하기
from sklearn.metrics import mean_squared_error
def RMSE(y_test, y_predict ):
    return np.sqrt(mean_squared_error(y_test, y_predict))
print("RMSE : ", RMSE(y_test, y_predict))

# R2 구하기
from sklearn.metrics import r2_score
r2_y_predict = r2_score(y_test, y_predict)
print("R2 : ", r2_y_predict)

#문제 1. R2 값을 0.5 이하로 줄이시오
# 레이어는 input 과 output 포함 5개 이상, 노드는 각 레이어당 5개 이상
# batch_size = 1
# epochs = 100 이상
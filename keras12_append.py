# 1. 데이터

import numpy as np

x = np.array([range(100), range(311,411), range(100), range(100,200), range(311,411), range(100,200)])
y = np.array([range(501,601), range(711,811), range(100), range(501,601), range(711,811), range(100)])

# x2 = np.array([range(100,200), range(311,411), range(100,200)])
# y2 = np.array([range(501,601), range(711,811), range(100)])

x = np.transpose(x)
y = np.transpose(y)
# x1 = np.transpose(x1)
# y1 = np.transpose(y1)
# x2 = np.transpose(x2)
# y2 = np.transpose(y2)

print(x.shape) 
print(y.shape)
# print(x1.shape) # (100,3)
# print(y1.shape) # (100,3)
# print(x2.shape) # (100,3)
# print(y2.shape) # (100,3)

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=33, test_size=0.4, shuffle=False)
x_val, x_test, y_val, y_test = train_test_split(x_test, y_test, random_state=33, test_size=0.5, shuffle=False)

x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=33, test_size=0.4, shuffle=False)
x_val, x_test, y_val, y_test = train_test_split(x_test, y_test, random_state=33, test_size=0.5, shuffle=False)

# from sklearn.model_selection import train_test_split
# x1_train, x1_test, y1_train, y1_test = train_test_split(x1, y1, random_state=33, test_size=0.4, shuffle=False)
# x1_val, x1_test, y1_val, y1_test = train_test_split(x1_test, y1_test, random_state=33, test_size=0.5, shuffle=False)

# x2_train, x2_test, y2_train, y2_test = train_test_split(x2, y2, random_state=33, test_size=0.4, shuffle=False)
# x2_val, x2_test, y2_val, y2_test = train_test_split(x2_test, y2_test, random_state=33, test_size=0.5, shuffle=False)

#print(x_test.shape)

# 2. 모델 구성

from keras.models import Sequential
from keras.layers import Dense
model = Sequential()
model.add(Dense(4, input_dim=6, activation='relu'))
model.add(Dense(6, activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(x, y, epochs=5, batch_size=10)

y_predict = model.predict_classes(x)


from keras.models import Sequential, Model
from keras.layers import Dense, Input
#model = Sequential()

input1 = Input(shape=(6, ))
dense1 = Dense(5, activation='relu')(input1)
dense2 = Dense(3)(dense1)
dense3 = Dense(4)(dense2)
middle1 = Dense(3)(dense3)

# input2 = Input(shape=(6, ))
# xx = Dense(5, activation='relu')(input2)
# xx = Dense(1000)(xx)
# xx = Dense(5)(xx)
# middle2 = Dense(3)(xx)

# concatenate

from keras.models import Sequential
from keras.layers import Dense
models = middle1

output1 = Dense(30)(middle1)
output1 = Dense(13)(output1)
output1 = Dense(3)(output1)

# output2 = Dense(15)(merge1)
# output2 = Dense(32)(output2)
# output2 = Dense(3)(output2)



model = Model(inputs = input1, outputs = output1)
model.summary()
'''
#3. 훈련
model.compile(loss='mse', optimizer='adam', metrics=['mse']) # metrics=['accuracy'])

model.fit(x_train,y_train, epochs=502, batch_size=1, validation_data=(x_val, y_val))

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
'''
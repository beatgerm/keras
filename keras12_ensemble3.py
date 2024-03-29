# 1. 데이터

import numpy as np

x1 = np.array([range(100), range(311,411), range(100)])
x2 = np.array([range(501,601), range(711,811), range(100)])

y1 = np.array([range(100,200), range(311,411), range(100,200)])


x1 = np.transpose(x1)
y1 = np.transpose(y1)
x2 = np.transpose(x2)


print(x1.shape) # (100,3)
print(y1.shape) # (100,3)
print(x2.shape) # (100,3)


from sklearn.model_selection import train_test_split
x1_train, x1_test, y1_train, y1_test = train_test_split(x1, y1, random_state=33, test_size=0.4, shuffle=False)
x1_val, x1_test, y1_val, y1_test = train_test_split(x1_test, y1_test, random_state=33, test_size=0.5, shuffle=False)

x2_train, x2_test = train_test_split(x2, random_state=33, test_size=0.4, shuffle=False)
x2_val, x2_test = train_test_split(x2_test, random_state=33, test_size=0.5, shuffle=False)




print(x2_test.shape)
print(x1_test.shape)
print(y1_test.shape)

# 2. 모델 구성

from keras.models import Sequential, Model
from keras.layers import Dense, Input
#model = Sequential()

input1 = Input(shape=(3, ))
dense1 = Dense(5, activation='relu')(input1)
dense2 = Dense(3)(dense1)
dense3 = Dense(4)(dense2)
middle1 = Dense(3)(dense3)

input2 = Input(shape=(3, ))
xx = Dense(5, activation='relu')(input2)
xx = Dense(1000)(xx)
xx = Dense(5)(xx)
middle2 = Dense(3)(xx)

# concatenate

from keras.layers.merge import concatenate
merge1 = concatenate([middle1, middle2])

output1 = Dense(30)(merge1)
output1 = Dense(13)(output1)
output1 = Dense(3)(output1)

model = Model(inputs = [input1, input2], 
              outputs = [output1])
model.summary()

#3. 훈련
# model.compile(loss='mse', optimizer='adam', metrics=['mse']) # metrics=['accuracy'])

# model.fit(x_train,y_train, epochs=502, batch_size=1, validation_data=(x_val, y_val))
model.compile(loss='mse', optimizer='adam', metrics=['mse']) # metrics=['accuracy'])

model.fit([x1_train, x2_train], [y1_train], epochs=5, batch_size=1, validation_data=([x1_val, x2_val], [y1_val]))

#4. 평가 예측
mse = model.evaluate([x1_test, x2_test], [y1_test], batch_size=1) # a[0], a[1]
print("mse : ", mse)



y1_predict = model.predict([x1_test, x2_test])
print([y1_predict])

# RMSE 구하기
from sklearn.metrics import mean_squared_error
def RMSE(xxx, yyy):
    return np.sqrt(mean_squared_error(xxx, yyy))
RMSE1 = RMSE(y1_test, y1_predict)
print("RMSE1 : ", RMSE1)

print("RMSE : ", (RMSE1)/1)


# R2 구하기
from sklearn.metrics import r2_score
r2_y1_predict = r2_score(y1_test, y1_predict)

#print("R2_1 : ", r2_y1_predict)

print("R2 : ", (r2_y1_predict))

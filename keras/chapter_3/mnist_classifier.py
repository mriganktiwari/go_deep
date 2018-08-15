import tensorflow as tensorflow
from keras.utils import to_categorical
from keras import layers, models

mnist=tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

x_train = tf.keras.utils.normalize(x_train, axis=1)
x_test = tf.keras.utils.normalize(x_test, axis=1)

model = models.Sequential()
model.add(layers.Dense(32, activation='relu'))
model.add(layers.Dense(10, activation='softmax'))

model.compile(optimizer='sgd',
  loss='categorical_crossentropy',
  metrics=['accuracy'])

history = model.fit(x_train, y_train, epochs=7, validation_split=0.2)

results = model.evaluate(x_test, y_test)
print(results)

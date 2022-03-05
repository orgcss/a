# install tensorflow on python3.8 on ubuntu18.04

```bash
    python3.8 -m venv ai
    source ai/bin/activate
    pip install numpy scipy --only-binary=:all:
    (download tensorflow whl from official website)
    mv tensorflow*.whl tensorflow-2.8.0-py3-none-any.whl
    pip install tensorflow*.whl
```
400+MB whl file and 1.2G in package/tensorflow folder.

## tf example:
```python
import tensorflow as tf
mnist = tf.keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(10)
])
loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)

model.compile(optimizer='adam',
              loss=loss_fn,
              metrics=['accuracy'])
model.fit(x_train, y_train, epochs=5)
model.evaluate(x_test,  y_test, verbose=2)
```

## sk example:
```
from sklearn.neural_network import MLPClassifier
X = [[0., 0.], [1., 1.]]
y = [0, 1]
clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1)

clf.fit(X, y)

res=clf.predict([[2., 2.], [-1., -2.]])
print(res)
```

from tflearn import DNN
from tflearn.layers.core import input_data, fully_connected
from tflearn.layers.estimator import regression

"""
Ref:
    https://towardsdatascience.com/tflearn-soving-xor-with-a-2x2x1-feed-forward-neural-network-6c07d88689ed
"""

# input data
X = [[0, 0], [0, 1], [1, 0], [1, 1]]
Y = [[0], [1], [1], [0]]


# model
input_layer = input_data(shape=[None, 2])
hidden_layer = fully_connected(input_layer, 2, activation='tanh')
output_layer = fully_connected(hidden_layer, 1, activation='tanh')

regression = regression(
    output_layer,
    optimizer='sgd',
    loss='binary_crossentropy',
    learning_rate=5
)
model = DNN(regression)
model.fit(X, Y, n_epoch=5000, show_metric=True)

# predict one
print(model.predict([X[0]]) > 0)

# predict all
prediction = [i[0] > 0 for i in model.predict(X)]
print(prediction)

print("")

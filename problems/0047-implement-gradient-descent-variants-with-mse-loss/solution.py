import numpy as np

def gradient_descent(X, y, weights, learning_rate, n_epochs, batch_size=1, method='batch'):
    for i in range(n_epochs):
        if method == "batch":
            y_pred = X @ weights
            mse = np.sum((y - y_pred)**2)/len(y)
            gradient = (2 / len(y)) * X.T @ (y_pred - y)
            weights = weights - learning_rate * gradient
        if method == "stochastic":
            for i in range(len(y)):
                xi = X[i:i+1]
                yi = y[i:i+1]
                y_pred = xi @ weights
                mse = np.sum((yi - y_pred)**2)
                gradient = 2 * xi.T @ (y_pred - yi)
                weights = weights - learning_rate * gradient
        if method == "mini_batch":
            for i in range(0,len(y),batch_size):
                xi = X[i:i+batch_size]
                yi = y[i:i+batch_size]
                b = len(yi)
                y_pred = xi @ weights
                mse = np.sum((yi - y_pred)**2)/b
                gradient = (2/b) * xi.T @ (y_pred - yi)
                weights = weights - learning_rate * gradient

    return weights

import math
import numpy as np
def single_neuron_model(features: list[list[float]], labels: list[int], weights: list[float], bias: float) -> (list[float], float):
	
	features = np.array(features, dtype=np.float32)
	labels = np.array(labels, dtype=np.float32)
	weights = np.array(weights, dtype=np.float32)
	z = weights @ features.T + bias
	probabilities = [1/(1+math.exp(-float(x))) for x in z]
	mse = sum((labels[i] - probabilities[i])**2 for i in range(len(labels)))/len(labels)
	return probabilities, mse
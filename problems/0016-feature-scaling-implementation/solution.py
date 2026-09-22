import numpy as np
def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):
	x_mean = np.mean(data, axis=0)
	x_std = np.std(data, axis=0)
	standardized_data = (data - x_mean) / x_std

	min_val = np.min(data, axis=0, keepdims=True)
	max_val = np.max(data, axis=0, keepdims=True)
	normalized_data = (data - min_val) / (max_val - min_val)
	return standardized_data, normalized_data
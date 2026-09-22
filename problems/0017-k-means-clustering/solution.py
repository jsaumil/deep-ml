import numpy as np
def distance(x1,x2):
	x1 = np.array(x1)
	x2 = np.array(x2)
	return np.sqrt(np.sum((x2-x1)**2))
def k_means_clustering(points: list[tuple[float, ...]], k: int, initial_centroids: list[tuple[float, ...]], max_iterations: int) -> list[tuple[float, ...]]:

	centroids = initial_centroids

	for _ in range(max_iterations):
		assigned = []
		for point in points:
			distances = [distance(point, centroid) for centroid in centroids]
			cluster = np.argmin(distances)
			assigned.append(cluster)

		new_centroid = []
		for i in range(k):
			cluster_points = [point for point, cluster in zip(points,assigned) if cluster == i]
			if len(cluster_points) == 0:
				new_centroid.append(centroids[i])
				continue
			mean = np.mean(cluster_points, axis=0)
			new_centroid.append(tuple(mean))
		centroids = new_centroid
	return centroids
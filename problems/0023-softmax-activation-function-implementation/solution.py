import math

def softmax(scores: list[float]) -> list[float]:
    max_score = max(scores)
    exp_s = [math.exp(x-max_score) for x in scores]
    total = sum(exp_s)
    for j in range(len(exp_s)):
        exp_s[j] = exp_s[j]/total
    return exp_s
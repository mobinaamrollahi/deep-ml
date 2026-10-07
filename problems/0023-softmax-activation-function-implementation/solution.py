import math

def softmax(scores: list[float]) -> list[float]:
    sum_ = 0
    output = []
    max_ = max(scores)
    for i in range(len(scores)):
        sum_ += math.exp(scores[i] - max_)

    for i in range(len(scores)):
        output.append((math.exp(scores[i] - max_))/sum_)
    return output
import numpy as np

def normalize_scores(scores: list[list[int]]) -> float:
    # Your code here
    scores_np=np.array(scores)
    n_row,c_col=scores_np.shape
    sum=np.sum(scores_np,axis=0)
    sum_mean=sum/n_row
    normalized_scores=scores_np-sum_mean
    mean=np.mean(normalized_scores)
    rounded_mean=np.round(mean,2)
    return rounded_mean


scores=[[80, 75, 90], [85, 88, 92], [78, 82, 85], [90, 91, 88]]
result=normalize_scores(scores)
print(result)
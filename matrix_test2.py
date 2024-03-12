import numpy as np

#Example 2
criteria_names=["C1", "C2", "C3"]
alternative_names=["A1", "A2", "A3"]


criteria1 = np.array([[1,1/9,1],[9,1,7],[1,1/7,1]])
criteria2 = np.array([[1,9,8],[1/9,1,1],[1/8,1,1]])
criteria3 = np.array([[1,1/2,8],[2,1,9],[1/8,1/9,1]])

matrix_per_criteria=np.array([criteria1, criteria2, criteria3])

criteria_comparison=np.array([1/3,1/3,1/3])
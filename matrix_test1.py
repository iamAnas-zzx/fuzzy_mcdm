#the most important thing is I should have the name of criteria and the alternatives

#Example 1
import fuzzy_mcdm as fz
import numpy as np

criteria_names=["Experience", "Education", "Charisma", "Age"]
alternative_names=["Tom", "Dick", "Harry"]


criteria1 = np.array([[1,1/4,0],[4,1,9],[1/4,1/9,1]])
criteria2 = np.array([[1,3,1/5],[1/3,1,1/7],[5,7,1]])
criteria3 = np.array([[1,5,9],[1/5,1,4],[1/9,1/4,1]])
criteria4 = np.array([[1,1/3,5],[3,1,9],[1/5,1/9,1]])


matrix_per_criteria=np.array([criteria1, criteria2, criteria3, criteria4]) #list of matrix containing alternative to alternative comparision for every single criteria
criteria_comparison=np.array([[1,4,3,7], [1/4,1,1/3,3], [1/3,3,1,5],[1/7,1/3,1/5,1]])

fz.matrix_validate(criteria_names, alternative_names, matrix_per_criteria, criteria_comparison)

# print(t)``
# part-A #

import numpy as np

from sklearn.decomposition import PCA

# stu_1=np.array([78,98,67])
# stu_2=np.array([89,56,78])

# print("Student 1 Vector:", stu_1)
# print("Student 2 Vector:", stu_2)

# # norm 1 #
# n1=np.linalg.norm(stu_1,ord=1)
# n2=np.linalg.norm(stu_2,ord=1)

# print("Norm-1 of Student 1:",n1)
# print("Norm-2 of student 2",n2)

# # norm 2 #
# n11=np.linalg.norm(stu_1,ord=2)
# n21=np.linalg.norm(stu_2,ord=2)

# print("Norm-1 of Student 1:", n11)
# print("Norm-2 of Student 2:", n21)

# # dot #
# dot_product=np.dot(stu_1,stu_2)
# print("Dot Product:", dot_product)

# # angle #

# cos_theta=dot_product/n11*n21
# angle = np.degrees(np.arccos(cos_theta))

# print("Angle between vectors:", angle)

# # cross #

# cross_product=np.cross(stu_1,stu_2)
# print("Cross Product:", cross_product)

# # projection #

# projection = (np.dot(stu_1, stu_2) / np.dot(stu_2, stu_2)) * stu_2

# print("Projection of Student1 onto Student2:")
# print(projection)

# part B #

# A = np.array([[80, 75],
#               [70, 85]
# ])

# B = np.array([[90, 88],
#               [60, 95]
# ])

# print("matrix A",A)
# print("matrix B",B)

# add=A + B
# print("addition of two matrix is",add)

# mul=A * B
# print("mul of two matrix is",mul)

# Tra=A.T
# print("tran =",Tra)

# inv=np.linalg.inv(A)
# print("inverse of a=",inv)

# det=np.linalg.det(A)
# print("determin of a=",det)

# part c #

# print("1D = Line")
# print("2D = Plane")
# print("3D or higher = Hyperplane")

# # 2D point
# point_2d = np.array([3, 4])

# # 3D point
# point_3d = np.array([3, 4, 5])

# # Higher dimension
# point_hd = np.array([3, 4, 5, 6, 7])

# print("2D Point:", point_2d)
# print("3D Point:", point_3d)
# print("Higher Dimension Point:", point_hd)

# part D #

# 1 #

# a=np.array([[2,4],
#             [6,8]])

# print(a)

# e_vector,e_value=np.linalg.eig(a)

# print("eigenvector is=",e_vector)
# print("eigenvalue is=",e_value)

# # 2 #

# from scipy.linalg import lu

# p,l,u=lu(a)

# print("\np matrix",p)

# print("\nl matrix",l)

# print("\nu matrix",u)

# # 3 #

# U, S, VT = np.linalg.svd(a)

# print("U Matrix:")
# print(U)

# print("\nSingular Values:")
# print(S)

# print("\nVT Matrix:")
# print(VT)

# part E #
# pca #

# data = np.array([
#     [80, 75, 90],
#     [70, 85, 88],
#     [60, 78, 95],
#     [90, 92, 85]
# ])

# pca = PCA(n_components=2)

# reduced = pca.fit_transform(data)

# print("Reduced Data:")
# print(reduced)

# lda #

# from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

# # Student marks
# X = np.array([
#     [80, 75],
#     [70, 85],
#     [60, 78],
#     [90, 92]
# ])
# # Categories
# # 1 = Above Average
# # 0 = Below Average
# y = np.array([1, 0, 0, 1])

# lda = LinearDiscriminantAnalysis(n_components=1)

# result = lda.fit_transform(X, y)
# print(result)


import invertible_matrix.invertible_matrix as inv_mat
import logging as log
log.basicConfig(filename="invert_matrix.log",
                filemode="w", level=log.DEBUG)

print(inv_mat.matrix_to_str(inv_mat.invert_matrix([[1, 2], [3, 4]])))
print(len(inv_mat.invert_matrix([[1, 2], [3, 4]])))
print(len([[6], [8]]))
print(inv_mat.invert_matrix_slay_calc([[1, 2], [3, 4]], [[6], [8]]))

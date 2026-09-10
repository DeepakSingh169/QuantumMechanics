import numpy as np

def hamiltonian_matrix(delta_x,potential_values):
  potential_values = np.asarray(potential_values,dtype=float)
  if delta_x <=0:
    raise ValueError("detla_x must be greater than 0")
  if potential_values.ndim != 1:
    raise ValueError("potential_values must be a one-dimensional array.")
  if potential_values.size == 0:
    raise ValueError("potential_values cannot be empty.")

  interior_points = len(potential_values)

  main_diag = 1/(delta_x**2) + potential_values
  off_diag = np.full(interior_points-1,-1/(2*(delta_x**2)))

  hamiltonian = (np.diag(main_diag) + np.diag(off_diag,k=1) + np.diag(off_diag,k=-1))

  return hamiltonian
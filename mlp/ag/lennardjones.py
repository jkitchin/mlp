"""A periodic Lennard Jones potential."""


import autograd.numpy as np
from autograd import elementwise_grad
from mlp.ag.neighborlist import get_distances


def energy(params, positions, cell, strain=np.zeros((3, 3))):
    """Compute the energy of a Lennard-Jones system.

    Parameters
    ----------

    params : dictionary of paramters.
      Defaults to {'sigma': 1.0, 'epsilon': 1.0}

    positions : array of floats. Shape = (natoms, 3)

    cell: array of unit cell vectors. Shape = (3, 3)

    strain: array of strains to apply to cell. Shape = (3, 3)

    Returns
    -------
    energy : float
    """

    sigma = params.get('sigma', 1.0)
    epsilon = params.get('epsilon', 1.0)

    rc = 3 * sigma

    e0 = 4 * epsilon * ((sigma / rc)**12 - (sigma / rc)**6)

    r2 = get_distances(positions, cell, rc, 0.01, strain)**2

    zeros = np.equal(r2, 0.0)
    adjusted = np.where(zeros, np.ones_like(r2), r2)

    c6 = np.where((r2 <= rc**2) & (r2 > 0.0),
                  (sigma**2 / adjusted)**3, np.zeros_like(r2))
    c6 = np.where(zeros, np.zeros_like(r2), c6)
    energy = -e0 * (c6 != 0.0).sum()
    c12 = c6**2
    energy += np.sum(4 * epsilon * (c12 - c6))

    # get_distances double counts the interactions, so we divide by two.
    return energy / 2


def forces(params, positions, cell):
    """Compute the forces of a Lennard-Jones system.

    Parameters
    ----------

    params : dictionary of paramters.
      Defaults to {'sigma': 1.0, 'epsilon': 1.0}

    positions : array of floats. Shape = (natoms, 3)

    cell: array of unit cell vectors. Shape = (3, 3)

    Returns
    -------
    forces : an array of forces. Shape = (natoms, 3)

    """
    dEdR = elementwise_grad(energy, 1)
    return -dEdR(params, positions, cell)


def stress(params, positions, cell, strain=np.zeros((3, 3))):
    """Compute the stress on a Lennard-Jones system.

    Parameters
    ----------

    params : dictionary of paramters.
      Defaults to {'sigma': 1.0, 'epsilon': 1.0}

    positions : array of floats. Shape = (natoms, 3)

    cell: array of unit cell vectors. Shape = (3, 3)

    Returns
    -------
    stress : an array of stress components. Shape = (6,)
    [sxx, syy, szz, syz, sxz, sxy]

    """
    dEdst = elementwise_grad(energy, 3)

    volume = np.abs(np.linalg.det(cell))

    der = dEdst(params, positions, cell, strain)
    result = (der + der.T) / 2 / volume
    return np.take(result, [0, 4, 8, 5, 2, 1])

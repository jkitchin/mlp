"""A neighborlist."""
import autograd.numpy as np

def get_distances(positions, cell, cutoff_radius, skin=0.01, strain=np.zeros((3, 3))):
    """Get distances to atoms that are in unit cells that tile a spherical volume of
cutoff_radius.

    positions: array-like (natoms, 3)
    cell: array-like (3, 3)
    cutoff_radius: float
    skin: float
    strain: array-like (3, 3)

    This returns an array of dimension (atom_i, atom_j, distance) The shape is
    (natoms, natoms, nunitcells) where nunitcells is the total number of unit
    cells required to tile the space to be sure all neighbors will be found. The
    atoms that are outside the cutoff radius are zeroed.

    """ 
    strain_tensor = np.eye(3) + strain
    cell = np.dot(strain_tensor, cell.T).T    
    positions = np.dot(strain_tensor, positions.T).T

    inverse_cell = np.linalg.inv(cell)
    num_repeats = cutoff_radius * np.linalg.norm(inverse_cell, axis=0)

    fractional_coords = np.dot(positions, inverse_cell) % 1
    mins = np.min(np.floor(fractional_coords - num_repeats), axis=0) 
    maxs = np.max(np.ceil(fractional_coords + num_repeats), axis=0) 
    
    # Now we generate a set of cell offsets
    v0_range = np.arange(mins[0], maxs[0])
    v1_range = np.arange(mins[1], maxs[1])
    v2_range = np.arange(mins[2], maxs[2])

    xhat = np.array([1, 0, 0])
    yhat = np.array([0, 1, 0])
    zhat = np.array([0, 0, 1])

    v0_range = v0_range[:, None] * xhat[None, :]
    v1_range = v1_range[:, None] * yhat[None, :]
    v2_range = v2_range[:, None] * zhat[None, :]

    offsets = v0_range[:, None, None] + v1_range[None, :, None] + v2_range[None, None, :]
    offsets = offsets.reshape(-1, 3)
    
    # Now we have a vector of unit cell offsets (offset_index, 3)
    # We convert that to cartesian coordinate offsets
    cart_offsets = np.dot(offsets, cell)

    # we need to offset each coord by each offset.
    # This array is (atom_index, offset, 3)
    shifted_cart_coords = positions[:, None] + cart_offsets[None, :]

    # Next, we subtract each position from the array of positions
    # (atom_i, atom_j, positionvector, xhat)
    pv =  shifted_cart_coords - positions[:, None, None]

    # This is the distance squared
    # (atom_i, atom_j, distance_ij)
    d2 = np.sum(pv**2, axis=3)
 
    # The gradient of sqrt is nan at r=0, so we do this round about way to avoid that.
    zeros = np.equal(d2, 0.0)
    adjusted = np.where(zeros, np.ones_like(d2), d2)
    d = np.where(zeros, np.zeros_like(d2), np.sqrt(adjusted))
    
    return np.where(d <= cutoff_radius + skin, d, np.zeros_like(d))

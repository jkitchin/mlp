"""Tensorflow utilities.

"""

import tensorflow as tf


def tri(N, M=None, k=0, dtype=tf.float64):
    """
    An array with ones at and below the given diagonal and zeros elsewhere.

    Parameters
    ----------
    N : int
        Number of rows in the array

    M : int, optional
        Number of columns in the array. Defaults to number of rows.

    k : The subdiagonal at and below which the array is filled, optional


    Returns
    -------
    out : tensor of shape (N, M)

    Modeled after pydoc:numpy.tri.
    """

    if M is None:
        M = N

    r1 = tf.range(N)
    r2 = tf.range(-k, M - k)
    return tf.greater_equal(r1[:, None], r2[None, :])


def triu_indices(n, k=0, m=None):
    """Return indices for upper triangle of an (n, m) array.

    Parameters
    ----------
    n : int
      number of rows in the array.

    k : int, optional
      diagonal offset.

    m : int, optional
      number of columns in the array. Defaults to `n`.

    Returns
    -------
    inds : a tensor, shape = (None, 2)
      column 0 is one set of indices, column 1 is the other set.

    modeled after pydoc:numpy.triu_indices.
    """

    result = tf.where(tf.logical_not(tri(n, m, k=k - 1)))
    return result[:, 0], result[:, 1]


def triu_indices_from(arr, k=0):
    """Return the indices for the upper-triangle of arr.

    Parameters
    ----------
    arr : tensor or array.
    k : diagonal.

    see pydoc:numpy.triu_indices_from.
    """
    tensor = tf.convert_to_tensor(arr)
    shape = tensor.get_shape().as_list()
    if len(shape) != 2:
        raise ValueError("Tensor must be 2d")
    return triu_indices(shape[-2], k=k, m=shape[-1])


def tril_indices(n, k=0, m=None):
    """Return indices for lower triangle of an (n, m) array.

    Parameters
    ----------
    n : int
      number of rows in the array.

    k : int, optional
      diagonal offset.

    m : int, optional
      number of columns in the array. Defaults to `n`.

    Returns
    -------
    inds : a tensor, shape = (None, 2)
      column 0 is one set of indices, column 1 is the other set.

    modeled after pydoc:numpy.tril_indices.
    """

    result = tf.where(tri(n, m, k=k))
    return result[:, 0], result[:, 1]


def tril_indices_from(arr, k=0):
    """Return the indices for the lower-triangle of arr.

    Parameters
    ----------
    arr : tensor or array.
    k : diagonal.

    see pydoc:numpy.tril_indices_from.
    """
    tensor = tf.convert_to_tensor(arr)
    shape = tensor.get_shape().as_list()
    if len(shape) != 2:
        raise ValueError("Tensor must be 2d")
    return tril_indices(shape[-2], k=k, m=shape[-1])

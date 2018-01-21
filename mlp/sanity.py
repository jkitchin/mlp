"""A sanity module.

This contains simple functions that should work.
"""

import ase
import tensorflow as tf


def sanity0():
    """Sanity check function to make sure we are running tests."""
    from ase.build import bulk
    print(ase.version)
    atoms = bulk('Cu', 'fcc', a=3.6).repeat((2, 1, 1))
    atoms.get_volume()
    # This sanity function just returns 2
    return 2


def sanity1():
    a = tf.constant(1)
    return 2 * a

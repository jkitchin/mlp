import ase

def sanity0():
    """Sanity check function to make sure we are running tests."""
    from ase.build import bulk
    atoms = bulk('Cu', 'fcc', a=3.6).repeat((2, 1, 1))
    return 2

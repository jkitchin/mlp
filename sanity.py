import ase

def sanity0():
    from ase.build import bulk
    atoms = bulk('Cu', 'fcc', a=3.6).repeat((2, 1, 1))
    return len(atoms)

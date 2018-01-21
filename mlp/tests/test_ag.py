import unittest
import autograd.numpy as np
from ase.build import bulk
from ase.neighborlist import NeighborList
from ase.calculators.lj import LennardJones

from mlp.ag.neighborlist import get_distances
from mlp.ag.lennardjones import energy, forces, stress



class TestNeighborList(unittest.TestCase):

    def test0(self):
        a = 3.6
        for cutoff_radius in np.linspace(a / 2, 5 * a, 10):
            for rep in ((1, 1, 1),
                        (2, 1, 1),
                        (1, 2, 1),
                        (1, 1, 2),
                        (1, 2, 2),
                        (2, 1, 1),
                        (2, 2, 1),                        
                        (2, 2, 2),
                        (1, 2, 3)):
                atoms = bulk('Cu', 'fcc', a=a).repeat(rep)

                nl = NeighborList([cutoff_radius / 2] * len(atoms), skin=0.01,
                                  self_interaction=False, bothways=True)
                nl.update(atoms)      
                nns_ase = [len(nl.get_neighbors(i)[0]) for i in range(len(atoms))]

                d = get_distances(atoms.positions, atoms.cell, cutoff_radius)
                inds = (d <= (cutoff_radius + 0.01)) & (d > 0.00)
                nns = inds.sum((1, 2))
                
                self.assertTrue(np.all(nns_ase == nns))


class TestLennardJones(unittest.TestCase):
    def test_energy(self):

        atoms = bulk('Cu', 'fcc', a=3.7).repeat((2, 2, 1))
        atoms.rattle(0.02)
        atoms.set_calculator(LennardJones())

        ase_energy = atoms.get_potential_energy()
        lj_energy = energy({}, atoms.positions, atoms.cell)

        self.assertAlmostEqual(ase_energy, lj_energy)

        lj_forces = forces({}, atoms.positions, atoms.cell)
        self.assertTrue(np.allclose(atoms.get_forces(),
                                     lj_forces))

        lj_stress = stress({}, atoms.positions, atoms.cell)
        
        self.assertTrue(np.allclose(atoms.get_stress(),
                                     lj_stress))



        
        

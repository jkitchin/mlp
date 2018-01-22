"""Tests for tensorflow module."""

import numpy as np
import tensorflow as tf

from mlp.tf.utils import (tri, triu_indices, tril_indices,
                          triu_indices_from, tril_indices_from)


class TestTFUtils_tri(tf.test.TestCase):

    def test_tri(self):
        npt = np.tri(3, dtype=np.bool)
        tft = tri(3)
        with self.test_session():
            self.assertTrue(np.all(npt == tft.eval()))

    def test_above(self):
        npt = np.tri(3, k=1, dtype=np.bool)
        tft = tri(3, k=1)
        with self.test_session():
            self.assertTrue(np.all(npt == tft.eval()))

    def test_below(self):
        npt = np.tri(3, k=-1, dtype=np.bool)
        tft = tri(3, k=-1)
        with self.test_session():
            self.assertTrue(np.all(npt == tft.eval()))

    def test_notsquare(self):
        npt = np.tri(3, 4, dtype=np.bool)
        tft = tri(3, 4)
        with self.test_session():
            self.assertTrue(np.all(npt == tft.eval()))

    def test_notsquare_above(self):
        npt = np.tri(3, 4, k=1, dtype=np.bool)
        tft = tri(3, 4, k=1)
        with self.test_session():
            self.assertTrue(np.all(npt == tft.eval()))

    def test_notsquare_below(self):
        npt = np.tri(3, 4, k=-1, dtype=np.bool)
        tft = tri(3, 4, k=-1)
        with self.test_session():
            self.assertTrue(np.all(npt == tft.eval()))


class TestTFUtils_triu(tf.test.TestCase):
    def test_triu(self):
        npu = np.triu_indices(3)
        r0, r1 = triu_indices(3)
        with self.test_session():
            self.assertTrue(np.all(npu[0] == r0.eval()))
            self.assertTrue(np.all(npu[1] == r1.eval()))

    def test_triu_k_over(self):
        npu = np.triu_indices(3, k=1)
        r0, r1 = triu_indices(3, k=1)
        with self.test_session():
            self.assertTrue(np.all(npu[0] == r0.eval()))
            self.assertTrue(np.all(npu[1] == r1.eval()))

    def test_triu_k_under(self):
        npu = np.triu_indices(3, k=-1)
        r0, r1 = triu_indices(3, k=-1)
        with self.test_session():
            self.assertTrue(np.all(npu[0] == r0.eval()))
            self.assertTrue(np.all(npu[1] == r1.eval()))

    def test_triu_nonsquare(self):
        npu = np.triu_indices(3, m=4)
        r0, r1 = triu_indices(3, m=4)
        with self.test_session():
            self.assertTrue(np.all(npu[0] == r0.eval()))
            self.assertTrue(np.all(npu[1] == r1.eval()))

    def test_triu_nonsquare_long(self):
        npu = np.triu_indices(3, m=2)
        r0, r1 = triu_indices(3, m=2)
        with self.test_session():
            self.assertTrue(np.all(npu[0] == r0.eval()))
            self.assertTrue(np.all(npu[1] == r1.eval()))


class TestTFUtils_tril(tf.test.TestCase):
    def test_tril(self):
        npu = np.tril_indices(3)
        r0, r1 = tril_indices(3)
        with self.test_session():
            self.assertTrue(np.all(npu[0] == r0.eval()))
            self.assertTrue(np.all(npu[1] == r1.eval()))

    def test_tril_k_over(self):
        npu = np.tril_indices(3, k=1)
        r0, r1 = tril_indices(3, k=1)
        with self.test_session():
            self.assertTrue(np.all(npu[0] == r0.eval()))
            self.assertTrue(np.all(npu[1] == r1.eval()))

    def test_tril_k_under(self):
        npu = np.tril_indices(3, k=-1)
        r0, r1 = tril_indices(3, k=-1)
        with self.test_session():
            self.assertTrue(np.all(npu[0] == r0.eval()))
            self.assertTrue(np.all(npu[1] == r1.eval()))

    def test_tril_nonsquare(self):
        npu = np.tril_indices(3, m=4)
        r0, r1 = tril_indices(3, m=4)
        with self.test_session():
            self.assertTrue(np.all(npu[0] == r0.eval()))
            self.assertTrue(np.all(npu[1] == r1.eval()))

    def test_tril_nonsquare_long(self):
        npu = np.tril_indices(3, m=2)
        r0, r1 = tril_indices(3, m=2)
        with self.test_session():
            self.assertTrue(np.all(npu[0] == r0.eval()))
            self.assertTrue(np.all(npu[1] == r1.eval()))


class TestTFUtils_triu_indices_from(tf.test.TestCase):
    def test_triu_indices_from(self):

        a = np.zeros((3, 3))
        ref1, ref2 = np.triu_indices_from(a)

        tref1, tref2 = triu_indices_from(a)
        with self.test_session():
            self.assertTrue(np.all(ref1 == tref1.eval()))
            self.assertTrue(np.all(ref2 == tref2.eval()))

    def test_triu_indices_from_kover(self):

        a = np.zeros((3, 3))
        ref1, ref2 = np.triu_indices_from(a, k=1)

        tref1, tref2 = triu_indices_from(a, k=1)
        with self.test_session():
            self.assertTrue(np.all(ref1 == tref1.eval()))
            self.assertTrue(np.all(ref2 == tref2.eval()))

    def test_triu_indices_from_kunder(self):

        a = np.zeros((3, 3))
        ref1, ref2 = np.triu_indices_from(a, k=-1)
        tref1, tref2 = triu_indices_from(a, k=-1)
        with self.test_session():
            self.assertTrue(np.all(ref1 == tref1.eval()))
            self.assertTrue(np.all(ref2 == tref2.eval()))


class TestTFUtils_tril_indices_from(tf.test.TestCase):
    def test_tril_indices_from(self):

        a = np.zeros((3, 3))
        ref1, ref2 = np.tril_indices_from(a)

        tref1, tref2 = tril_indices_from(a)
        with self.test_session():
            self.assertTrue(np.all(ref1 == tref1.eval()))
            self.assertTrue(np.all(ref2 == tref2.eval()))

    def test_tril_indices_from_kover(self):

        a = np.zeros((3, 3))
        ref1, ref2 = np.tril_indices_from(a, k=1)

        tref1, tref2 = tril_indices_from(a, k=1)
        with self.test_session():
            self.assertTrue(np.all(ref1 == tref1.eval()))
            self.assertTrue(np.all(ref2 == tref2.eval()))

    def test_tril_indices_from_kunder(self):

        a = np.zeros((3, 3))
        ref1, ref2 = np.tril_indices_from(a, k=-1)
        tref1, tref2 = tril_indices_from(a, k=-1)
        with self.test_session():
            self.assertTrue(np.all(ref1 == tref1.eval()))
            self.assertTrue(np.all(ref2 == tref2.eval()))

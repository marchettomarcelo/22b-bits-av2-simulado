#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from myhdl import *
from .componentes import *

vec_exe1 = ["1101", "1111", "0111", "0100", "0010", "1010"]


def test_exe1():
    @instance
    def stimulus():
        for t in vec_exe1:
            a.next = int(t[0])
            b.next = int(t[1])
            c.next = int(t[2])
            yield delay(1)
            assert q == int(t[3])

    a, b, c, q = [Signal(bool(0)) for i in range(4)]
    dut = exe1(a, b, c, q)
    sim = Simulation(dut, stimulus)
    sim.run()


vec_exe2 = ["0001", "0011", "1000", "1010", "1111"]


def test_exe2():
    @instance
    def stimulus():
        for t in vec_exe2:
            p.next = int(t[0])
            q.next = int(t[1])
            r.next = int(t[2])
            yield delay(1)
            assert s == int(t[3])

    p, q, r, s = [Signal(bool(0)) for i in range(4)]
    dut = exe2(p, q, r, s)
    sim = Simulation(dut, stimulus)
    sim.run()


def test_exe3():
    @instance
    def stimulus():
        for i in range(4):
            for j in range(4):
                _x = bin(i, 2)
                _y = bin(j, 2)
                x1.next = int(_x[0])
                x0.next = int(_x[1])
                y1.next = int(_y[0])
                y0.next = int(_y[1])
                yield delay(1)
                _z = bin(i * j, 4)
                print("----------")
                print(_x)
                print(_y)
                print(_z)
                print("{}{}{}{}".format(int(z3), int(z2), int(z1), int(z0)))
                assert int(_z[0]) == z3
                assert int(_z[1]) == z2
                assert int(_z[2]) == z1
                assert int(_z[3]) == z0

    x1, x0, y1, y0, z3, z2, z1, z0 = [Signal(bool(0)) for i in range(8)]
    dut = exe3(x1, x0, y1, y0, z3, z2, z1, z0)
    sim = Simulation(dut, stimulus)
    sim.run()


def test_exe4_ula():
    @instance
    def stimulus():
        b.next = 5
        a.next = 3
        inverte_a.next = 0
        inverte_b.next = 0

        selecao.next = 0
        yield delay(1)
        assert resultado == (a & b)

        selecao.next = 1
        yield delay(1)
        assert resultado == (a | b)

        selecao.next = 1
        inverte_a.next = 1
        inverte_b.next = 1
        yield delay(1)
        assert resultado == ((not a) or (not b))

        selecao.next = 2
        inverte_a.next = 0
        inverte_b.next = 0
        yield delay(1)
        assert resultado == (a + b)

        selecao.next = 2
        c_in.next = 1
        yield delay(1)
        assert resultado == (a + b + 1)

        selecao.next = 3
        yield delay(1)
        assert resultado == 0

    a, b, resultado = [Signal(modbv(0)[32:]) for i in range(3)]
    inverte_a, inverte_b, c_in, c_out, zero = [Signal(bool(0)) for i in range(5)]
    selecao = Signal(modbv(0)[2:])

    dut = exe4_ula(a, b, inverte_a, inverte_b, c_in, c_out, selecao, zero, resultado)
    sim = Simulation(dut, stimulus)
    sim.run()

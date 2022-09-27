#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""


from myhdl import *
from .ula_aux import *


def exe1(a, b, c, q):
    @always_comb
    def comb():
        q.next = (a and b) or ((b and c ) and (b or c))

    return instances()


def exe2(p, q, r, s):
    @always_comb
    def comb():
        s.next = (not p) or (q and r)

    return instances()


def exe3(x1, x0, y1, y0, z3, z2, z1, z0):
    @always_comb
    def comb():
        z0.next = ((not x1) and x0 and (not y1) and  y0)  or   ((not x1) and x0 and y1 and  y0)  or ( x1 and x0 and (not y1) and  y0)  or  ( x1 and x0 and y1 and  y0)
        
        z1.next =  ((not x1) and x0 and y1 and (not y0))    or   ((not x1) and x0 and y1 and y0 )     or   ( x1 and (not x0) and (not y1) and y0 )      or   ( x1 and (not x0) and y1 and y0 )     or   ( x1 and x0 and (not y1) and y0 )      or   ( x1 and x0 and  y1 and (not y0) )

        z2.next = (x1 and (not x0) and y1 and (not y0))     or     (x1 and (not x0) and y0 and y1)     or     (x1 and x0 and y1 and (not y0))
        z3.next = x1 and x0 and y0 and y1

    return instances()


def exe4_ula(a, b, inverte_a, inverte_b, c_in, c_out, selecao, zero, resultado):
    
    a_pos_inversor, b_pos_inversor = [Signal(modbv(0)[32:]) for i in range(2)]
    a_invertido, b_invertido = [Signal(modbv(0)[32:]) for i in range(2)]
    or_out, and_out, add_out = [Signal(modbv(0)[32:]) for i in range(3)]
    mux_out = Signal(modbv(0)[32:])

    inversor_a = mux2way(a_pos_inversor, a, a_invertido, inverte_a)
    inversor_b = mux2way(b_pos_inversor, b, b_invertido, inverte_b)

    
    
    add_comp = adder(add_out,c_out, a_pos_inversor, b_pos_inversor,  c_in) 

    mux4_comp = mux4way(mux_out, and_out, or_out, add_out, 0  ,selecao)


    @always_comb
    def comb():
        resultado.next = mux_out
        
        a_invertido.next = not a
        b_invertido.next = not b

        or_out.next = a_pos_inversor or b_pos_inversor
        and_out.next = a_pos_inversor and b_pos_inversor

        
        zero_ = False
        for i in range(len(mux_out)):
            zero_ = zero_ or mux_out[i]
        zero.next = not zero_
        
        # zero.next = not str(mux_out).count("0") == len(str(mux_out))



    return instances()

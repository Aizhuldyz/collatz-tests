#!/usr/bin/env python3

# ----------------------------
# cs373-collatz/TestCollatz.py
# Copyright (C) 2015
# Parker L. Berg
# Some content retrieved from
# author Glenn P. Downing
# ----------------------------

# -------
# imports
# -------

from io       import StringIO
from unittest import main, TestCase

from Collatz import collatz_read, cycle_length, collatz_eval, collatz_print, collatz_solve

# -----------
# TestCollatz
# -----------

class TestCollatz (TestCase) :
    # ----
    # read
    # ----

    def test_read_1 (self) :
        s    = "1 10\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  1)
        self.assertEqual(j, 10)

    def test_read_2 (self) :
        s    = "210 1\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 210)
        self.assertEqual(j, 1)

    # ------------
    # cycle_length
    # ------------

    def test_cycle_length_1 (self) :
        v = cycle_length(1)
        self.assertEqual(v, 1)

    def test_cycle_length_2 (self) :
        v = cycle_length(2)
        self.assertEqual(v, 2)

    def test_cycle_length_3 (self) :
        v = cycle_length(10)
        self.assertEqual(v, 7)

    # ----
    # eval
    # ----

    def test_eval_1 (self) :
        v = collatz_eval(1, 10)
        self.assertEqual(v, 20)

    def test_eval_2 (self) :
        v = collatz_eval(100, 200)
        self.assertEqual(v, 125)

    def test_eval_3 (self) :
        v = collatz_eval(201, 210)
        self.assertEqual(v, 89)

    def test_eval_4 (self) :
        v = collatz_eval(900, 1000)
        self.assertEqual(v, 174)

    def test_eval_5 (self) :
        v = collatz_eval(1, 1)
        self.assertEqual(v, 1)

    def test_eval_6 (self) :
        v = collatz_eval(2,2)
        self.assertEqual(v, 2)

    def test_eval_7 (self) :
        v = collatz_eval(1, 210)
        self.assertEqual(v, 125)

    # -----
    # print
    # -----

    def test_print_1 (self) :
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    def test_print_2 (self) :
        w = StringIO()
        collatz_print(w, 24, 7, 365)
        self.assertEqual(w.getvalue(), "24 7 365\n")

    # -----
    # solve
    # -----

    def test_solve_1 (self) :
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2 (self) :
        r = StringIO("205 5\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "205 5 125\n")

    def test_solve_3 (self) :
        r = StringIO("1 1\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 1 1\n")

    def test_solve_4 (self) :
        r = StringIO("")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "")

# ----
# main
# ----

if __name__ == "__main__" :
    main()

""" #pragma: no cover
% coverage3 run --branch TestCollatz.py >  TestCollatz.out 2>&1

% coverage3 report -m                   >> TestCollatz.out

% cat TestCollatz.out
..................
----------------------------------------------------------------------
Ran 18 tests in 0.052s

OK
Name          Stmts   Miss Branch BrMiss  Cover   Missing
---------------------------------------------------------
Collatz          32      0     12      0   100%   
TestCollatz      74      0      0      0   100%   
---------------------------------------------------------
TOTAL           106      0     12      0   100%   
"""

#!/usr/bin/env python3

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2014
# Glenn P. Downing
# -------------------------------

# -------
# imports
# -------

from io       import StringIO
from unittest import main, TestCase

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, cycle_length

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
        s = "100 200\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 100)
        self.assertEqual(j, 200)

    def test_read_3 (self) :
        s = "201 210\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 201)
        self.assertEqual(j, 210)

    # ------------
    # cycle_length
    # ------------

    def test_cycle_length_1 (self) :
        v = cycle_length(10)
        self.assertEqual(v, 7)

    def test_cycle_length_2 (self) :
        v = cycle_length(1)
        self.assertEqual(v, 1)

    def test_cycle_length_3 (self) :
        v = cycle_length(500000)
        self.assertEqual(v, 152)

    def test_cycle_length_4 (self) :
        v = cycle_length(999999)
        self.assertEqual(v, 259)

    def test_cycle_length_5 (self) :
        v = cycle_length(1000000)
        self.assertEqual(v, 153)

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
        v = collatz_eval(10, 1)
        self.assertEqual(v, 20)

    def test_eval_6 (self) :
        v = collatz_eval(1000000, 1)
        self.assertEqual(v, 525)

    # -----
    # print
    # -----

    def test_print_1 (self) :
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    def test_print_2 (self) :
        w = StringIO()
        collatz_print(w, 100, 200, 125)
        self.assertEqual(w.getvalue(), "100 200 125\n")

    def test_print_3 (self) :
        w = StringIO()
        collatz_print(w, 201, 210, 89)
        self.assertEqual(w.getvalue(), "201 210 89\n")

    # -----
    # solve
    # -----

    def test_solve_1 (self) :
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2 (self) :
        r = StringIO("268 544\n996 998\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "268 544 144\n996 998 50\n")

    def test_solve_3 (self) :
        r = StringIO("11111 12345\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "11111 12345 263\n")

# ----
# main
# ----

if __name__ == "__main__" :
    main()

""" #pragma: no cover
aero$ coverage3 run --branch TestCollatz.py > TestCollatz.out 2>&1
aero$ coverage3 report -m >> TestCollatz.out
aero$ cat TestCollatz.out
....................
----------------------------------------------------------------------
Ran 20 tests in 4.690s

OK
Name          Stmts   Miss Branch BrMiss  Cover   Missing
---------------------------------------------------------
Collatz          55      0     26      1    99%
TestCollatz      81      0      0      0   100%
---------------------------------------------------------
TOTAL           136      0     26      1    99%
"""

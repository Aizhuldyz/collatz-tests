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

from Collatz import collatz_read,collatz_cycle_length, collatz_eval, collatz_print, collatz_solve

# -----------
# TestCollatz
# -----------

class TestCollatz (TestCase) :
    # ----
    # read
    # ----

    def test_read (self) :
        s    = "1 10\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  1)
        self.assertEqual(j, 10)

    # ----
    # cycle_length
    # ----

    def test_cycle_length_1 (self) :
        v = collatz_cycle_length(1)
        self.assertEqual(v, 1)

    def test_cycle_length_2 (self) :
        v = collatz_cycle_length(2)
        self.assertEqual(v, 2)

    def test_cycle_length_3 (self) :
        v = collatz_cycle_length(837799)
        self.assertEqual(v, 525)

    def test_cycle_length_4 (self) :
        v = collatz_cycle_length(100)
        self.assertEqual(v, 26)

    def test_cycle_length_5 (self) :
        v = collatz_cycle_length(200)
        self.assertEqual(v, 27)

    def test_cycle_length_6 (self) :
        i = 1
        c = 1
        while i < 1000000 :
            v = collatz_cycle_length(i)
            self.assertEqual(v, c)
            i *= 2
            c += 1

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
        v = collatz_eval(15000, 20000)
        self.assertEqual(v, 279)

    # -----
    # print
    # -----

    def test_print_1 (self) :
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    def test_print_2 (self) :
        w = StringIO()
        collatz_print(w, 10, 1, 20)
        self.assertEqual(w.getvalue(), "10 1 20\n")

    # -----
    # solve
    # -----

    def test_solve (self) :
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

# ----
# main
# ----

if __name__ == "__main__" :
    main()

""" #pragma: no cover
% coverage3 run --branch TestCollatz.py >  TestCollatz.out 2>&1



% coverage3 report -m                   >> TestCollatz.out



% cat TestCollatz.out
.......
----------------------------------------------------------------------
Ran 7 tests in 0.001s

OK
Name          Stmts   Miss Branch BrMiss  Cover   Missing
---------------------------------------------------------
Collatz          18      0      6      0   100%
TestCollatz      33      1      2      1    94%   79
---------------------------------------------------------
TOTAL            51      1      8      1    97%
"""

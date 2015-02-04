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

from Collatz import collatz_read, collatz_eval, collatz_eval_helper, collatz_print, collatz_solve

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
        s    = "10 1\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  10)
        self.assertEqual(j, 1)

    def test_read_3 (self) :
        s    = "999999 1\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  999999)
        self.assertEqual(j, 1)

    def test_read_4 (self) :
        s    = "9 9\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 9)
        self.assertEqual(j, 9)

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
        v = collatz_eval(9, 9)
        self.assertEqual(v, 20)

    def test_eval_7 (self) :
        v = collatz_eval(10, 1)
        self.assertEqual(v, 20)

    def test_eval_8 (self) :
        v = collatz_eval(19502, 30759)
        self.assertEqual(v, 308)

    def test_eval_8 (self) :
        v = collatz_eval(1, 999999)
        self.assertEqual(v, 525)

    # ----
    # eval_helper
    # ----

    def test_eval_helper_1(self) :
        v = collatz_eval_helper(1)
        self.assertEqual(v, 1)

    def test_eval_helper_2(self) :
        v = collatz_eval_helper(999999)
        self.assertEqual(v, 259)

    def test_eval_helper_3(self) :
        v = collatz_eval_helper(500)
        self.assertEqual(v, 111)

    def test_eval_helper_4(self) :
        v = collatz_eval_helper(643876)
        self.assertEqual(v, 80)

    def test_eval_helper_5(self) :
        v = collatz_eval_helper(123456)
        self.assertEqual(v, 62)

    def test_eval_helper_6(self) :
        v = collatz_eval_helper(987654)
        self.assertEqual(v, 184)

    # -----
    # print
    # -----

    def test_print_1 (self) :
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    def test_print_2 (self) :
        w = StringIO()
        collatz_print(w, 1, 999999, 525)
        self.assertEqual(w.getvalue(), "1 999999 525\n")

    def test_print_3 (self) :
        w = StringIO()
        collatz_print(w, 0, 0, 0)
        self.assertEqual(w.getvalue(), "0 0 0\n")

    # -----
    # solve
    # -----

    def test_solve_1 (self) :
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2 (self) :
        r = StringIO("1 10\n10 1\n1 999999\n700000 999999\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 10 20\n10 1 20\n1 999999 525\n700000 999999 525\n")

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

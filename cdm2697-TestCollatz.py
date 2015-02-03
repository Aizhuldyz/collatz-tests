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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, eval_range

# -----------
# TestCollatz
# -----------

class TestCollatz (TestCase) :
    # ----
    # read
    # ----

    def test_read1 (self) :
        s    = "1 10\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  1)
        self.assertEqual(j, 10)

    def test_read2 (self) :
        s    = "100 1000\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  100)
        self.assertEqual(j, 1000)

    def test_read3 (self) :
        s    = "1 1\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  1)
        self.assertEqual(j, 1)
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
        v = collatz_eval(99, 9999)
        self.assertEqual(v, 262)

    def test_eval_6 (self) :
        v = collatz_eval(5, 6)
        self.assertEqual(v, 9)

    def test_eval_7 (self) :
        v = collatz_eval(10, 10)
        self.assertEqual(v, 7)

    def test_eval_8 (self) :
        v = collatz_eval(1, 113200)
        self.assertEqual(v, 354)

    # ----
    # eval_range
    # ----

    # def test_evalr_1 (self) :
    #     v = eval_range(1, 10)
    #     self.assertEqual(v, 20)

    # def test_evalr_2 (self) :
    #     v = eval_range(100, 200)
    #     self.assertEqual(v, 125)

    # def test_evalr_3 (self) :
    #     v = eval_range(201, 210)
    #     self.assertEqual(v, 89)

    # def test_evalr_4 (self) :
    #     v = eval_range(900, 1000)
    #     self.assertEqual(v, 174)

    # def test_evalr_5 (self) :
    #     v = eval_range(99, 9999)
    #     self.assertEqual(v, 262)

    # def test_evalr_6 (self) :
    #     v = eval_range(5, 6)
    #     self.assertEqual(v, 9)

    # def test_evalr_7 (self) :
    #     v = eval_range(10, 10)
    #     self.assertEqual(v, 7)

    # def test_evalr_8 (self) :
    #     v = eval_range(1, 113211)
    #     self.assertEqual(v, 354)
    # -----
    # print
    # -----

    def test_print1 (self) :
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    def test_print2 (self) :
        w = StringIO()
        collatz_print(w, 10, 10, 1)
        self.assertEqual(w.getvalue(), "10 10 1\n")

    def test_print3 (self) :
        w = StringIO()
        collatz_print(w, 0, 0, 0)
        self.assertEqual(w.getvalue(), "0 0 0\n")

    def test_print4 (self) :
        w = StringIO()
        collatz_print(w, 1, 113200, 354)
        self.assertEqual(w.getvalue(), "1 113200 354\n")

    # -----
    # solve
    # -----

    def test_solve1 (self) :
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    # Reversed
    def test_solve2 (self) :
        r = StringIO("10 1\n20 10\n210 201\n1000 900\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "10 1 20\n20 10 21\n210 201 89\n1000 900 174\n")

    def test_solve3 (self) :
        r = StringIO("40 50\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "40 50 110\n")

    def test_solve4 (self) :
        r = StringIO("434 343\n400 400\n27 72\n1 1\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "434 343 134\n400 400 28\n27 72 113\n1 1 1\n")

# ----
# main
# ----

if __name__ == "__main__" :
    main()

"""
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

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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve

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

    def test_read1 (self) :
        s    = "99 9999\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 99)
        self.assertEqual(j, 9999)

    def test_read2 (self) :
        s    = "10000 10\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  10000)
        self.assertEqual(j, 10)

    def test_read3 (self) :
        s    = "99 100\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  99)
        self.assertEqual(j, 100)

    # eval
    # ----

    def test_eval_1 (self) :
        v = collatz_eval(34, 67)
        self.assertEqual(v, 113)

    def test_eval_2 (self) :
        v = collatz_eval(90, 99)
        self.assertEqual(v, 119)

    def test_eval_3 (self) :
        v = collatz_eval(300, 500)
        self.assertEqual(v, 144)

    def test_eval_4 (self) :
        v = collatz_eval(900, 1000)
        self.assertEqual(v, 174)

    # -----
    # print
    # -----

    def test_print (self) :
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    def test_print1 (self) :
        w = StringIO()
        collatz_print(w, 1, 1, 1)
        self.assertEqual(w.getvalue(), "1 1 1\n")

    def test_print2 (self) :
        w = StringIO()
        collatz_print(w, 1, 999999, 525)
        self.assertEqual(w.getvalue(), "1 999999 525\n")

    def test_print3 (self) :
        w = StringIO()
        collatz_print(w, 100, 200, 125)
        self.assertEqual(w.getvalue(), "100 200 125\n")

    # -----
    # solve
    # -----

    def test_solve (self) :
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve1 (self) :
        r = StringIO("1 1\n3 3\n2 2\n4 4\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 1 1\n3 3 8\n2 2 2\n4 4 3\n")

    def test_solve2 (self) :
        r = StringIO("150 290\n99 1000\n123 1234\n333 444\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "150 290 128\n99 1000 179\n123 1234 182\n333 444 134\n")

    
    def test_solve3 (self) :
        r = StringIO("999990 999999\n123445 123\n1 99999\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "999990 999999 259\n123445 123 354\n1 99999 351\n")
    
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

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
        s    = "101 200\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 101)
        self.assertEqual(j, 200)

    def test_read_3 (self) :
        s    = "1001 2000\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 1001)
        self.assertEqual(j, 2000)

    def test_read_4 (self) :
        s    = "10001 20000\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 10001)
        self.assertEqual(j, 20000)

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
        v = collatz_eval(500, 83)
        self.assertEqual(v, 144)

    def test_eval_6 (self) :
        v = collatz_eval(2083, 7028)
        self.assertEqual(v, 262)

    def test_eval_7 (self) :
        v = collatz_eval(19502, 30759)
        self.assertEqual(v, 308)

    def test_eval_8 (self) :
        v = collatz_eval(102850, 104829)
        self.assertEqual(v, 310)

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

    def test_print_4 (self) :
        w = StringIO()
        collatz_print(w, 900, 1000, 174)
        self.assertEqual(w.getvalue(), "900 1000 174\n")
        
    # -----
    # solve
    # -----

    def test_solve (self) :
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    # -----
    # cycle_length
    # -----

    def test_cycle_length_1 (self) :
      n = cycle_length(5)
      self.assertEqual(n, 6)
   
    def test_cycle_length_2 (self) :
      n = cycle_length(44503)
      self.assertEqual(n, 71)

    def test_cycle_length_3 (self) :
      n = cycle_length(13954)
      self.assertEqual(n, 33)

    def test_cycle_length_4 (self) :
      n = cycle_length(88215)
      self.assertEqual(n, 165)

    def test_cycle_length_5 (self) :
      n = cycle_length(24136)
      self.assertEqual(n, 44)

# ----
# main
# ----

if __name__ == "__main__" :
    main()

"""
#pragma: no cover
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

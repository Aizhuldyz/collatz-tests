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

    def test_read_1 (self) :
        s    = "200 300\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 200)
        self.assertEqual(j, 300)

    def test_read_2 (self) :
        s    = "303 101\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 303)
        self.assertEqual(j, 101)

    def test_read_3 (self) :
        s    = "1000 1001\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 1000)
        self.assertEqual(j, 1001)

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
        v = collatz_eval(1234567890, 1234567890)
        self.assertEqual(v, 352)

    def test_eval_switched_args_1 (self) :
        v = collatz_eval(10000, 30)
        self.assertEqual(v, 262)

    def test_eval_switched_args_2 (self) :
        v = collatz_eval(100, 1)
        self.assertEqual(v, 119)

    # -----
    # print
    # -----

    def test_print (self) :
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    def test_print_1 (self) :
        w = StringIO()
        collatz_print(w, 3, 20, 21)
        self.assertEqual(w.getvalue(), "3 20 21\n")

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

    def test_solve (self) :
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_1 (self) :
        r = StringIO("1 2\n34 56\n789 1011\n1213 1415\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 2 2\n34 56 113\n789 1011 179\n1213 1415 177\n")

    def test_solve_2 (self) :
        r = StringIO("1 1000\n3 10000\n1 1\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 1000 179\n3 10000 262\n1 1 1\n")        

    def test_solve_3 (self) :
        r = StringIO("7 900\n999 999\n8000 800\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "7 900 179\n999 999 50\n8000 800 262\n")
# ----
# main
# ----

if __name__ == "__main__" :
    main()

""" #pragma: no cover
% coverage3 run --branch TestCollatz.py >  TestCollatz.out 2>&1



% coverage3 report -m                   >> TestCollatz.out



% cat TestCollatz.out
...................
----------------------------------------------------------------------
Ran 19 tests in 2.215s

OK
Name          Stmts   Miss Branch BrMiss  Cover   Missing
---------------------------------------------------------
Collatz          31      0     10      0   100%   
TestCollatz      83      0      0      0   100%   
---------------------------------------------------------
TOTAL           114      0     10      0   100%   
"""

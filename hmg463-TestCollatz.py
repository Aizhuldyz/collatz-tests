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
        s = "100 200\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  100)
        self.assertEqual(j, 200)

    def test_read_2 (self) :
        s = "201 210\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  201)
        self.assertEqual(j, 210)
    
    def test_read_3 (self) :
        s = "25 10 37\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 25)
        self.assertEqual(j, 10)

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
        v = collatz_eval(1000, 900)
        self.assertEqual(v, 174)

    def test_eval_6 (self) :
        v = collatz_eval(1, 1)
        self.assertEqual(v, 1)

    def test_eval_7 (self) :
        v = collatz_eval(50000, 3526)
        self.assertEqual(v, 324)

    # -----
    # print
    # -----

    def test_print (self) :
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    def test_print_1 (self) :
        w = StringIO()
        collatz_print(w, 100, 200, 125)
        self.assertEqual(w.getvalue(), "100 200 125\n")

    def test_print_2 (self) :
        w = StringIO()
        collatz_print(w, 50000, 3526, 324)
        self.assertEqual(w.getvalue(), "50000 3526 324\n")

    # -----
    # solve
    # -----

    def test_solve (self) :
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n1000 900\n1 1\n50000 3526\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n1000 900 174\n1 1 1\n50000 3526 324\n")

    def test_solve_2 (self) :
        r = StringIO("2 4\n50 9\n101 100\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "2 4 8\n50 9 112\n101 100 26\n")

    def test_solve_3 (self) :
        r = StringIO("1 1\n2 2\n10 1\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 1 1\n2 2 2\n10 1 20\n")

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

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

from Collatz import collatz_read, collatz_length, collatz_eval, collatz_print, collatz_solve

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


    # 3 test_read's by Charlina
    def test_read_1 (self) :
        s    = "0 0\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 0)
        self.assertEqual(j, 0)

    def test_read_2 (self) :
        s    = "10 1\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 10)
        self.assertEqual(j, 1)

    def test_read_3 (self) :
        s    = "99999 -5" 
        i, j = collatz_read(s)
        self.assertEqual(i, 99999)
        self.assertEqual(j, -5)

    # ------
    # length
    # ------

    def test_length_1 (self) :
        k = collatz_length(1)
        self.assertEqual(k, 1)

    def test_length_2 (self) :
        k = collatz_length(10)
        self.assertEqual(k, 7)

    def test_length_3 (self) :
        k = collatz_length(2)
        self.assertEqual(k, 2)

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

    # 3 test_eval's by Charlina
    def test_eval_5 (self) :
        v = collatz_eval(1, 1)
        self.assertEqual(v, 1)

    def test_eval_6 (self) :
        v = collatz_eval(10, 1)
        self.assertEqual(v, 20)

    def test_eval_7 (self) :
        v = collatz_eval(400000, 500000)
        self.assertEqual(v, 449)

    # -----
    # print
    # -----

    def test_print (self) :
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    # 3 test_print's by Charlina
    def test_print_1 (self) :
        w = StringIO()
        collatz_print(w, 0, 0, 0)
        self.assertEqual(w.getvalue(), "0 0 0\n")

    def test_print_2 (self) :
        w = StringIO()
        collatz_print(w, 0, 1, -5)
        self.assertEqual(w.getvalue(), "0 1 -5\n")

    def test_print_3 (self) :
        w = StringIO()
        collatz_print(w, 999, 9999, 99999)
        self.assertEqual(w.getvalue(), "999 9999 99999\n")

    # -----
    # solve
    # -----

    def test_solve (self) :
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    # 3 test_solve's by Charlina
    def test_solve_1 (self) :
        r = StringIO("1 1\n2 2\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 1 1\n2 2 2\n")

    def test_solve_2 (self) :
        r = StringIO("10 1\n 10 10\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "10 1 20\n10 10 7\n")

    def test_solve_3 (self) :
        r = StringIO("5000 6000\n9995 10000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "5000 6000 236\n9995 10000 180\n")

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

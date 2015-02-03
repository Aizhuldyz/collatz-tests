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

    def test_read_1 (self) :
        s    = "1 10\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  1)
        self.assertEqual(j, 10)

    def test_read_2 (self) :
        s    = "-1 1\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  -1)
        self.assertEqual(j, 1)

    def test_read_3 (self) :
        s    = "1000 10\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  1000)
        self.assertEqual(j, 10)

    def test_read_4 (self) :
        s    = "5 5\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  5)
        self.assertEqual(j, 5)

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
        v = collatz_eval(2, 1)
        self.assertEqual(v, 2)

    def test_eval_7 (self) :
        v = collatz_eval(200, 100)
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

    def test_solve_1 (self) :
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2 (self) :
        r = StringIO("34049 77051\n69684 79045\n15230 15203\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "34049 77051 351\n69684 79045 351\n15230 15203 147\n")

    def test_solve_3 (self) :
        r = StringIO("56373 85619\n76617 63495\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "56373 85619 351\n76617 63495 325\n")

    def test_solve_4 (self) :
        r = StringIO("54795 1628\n2568 71968\n67803 78309\n75143 37635\n70146 70228\n12380 14196\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "54795 1628 340\n2568 71968 340\n67803 78309 351\n75143 37635 340\n70146 70228 219\n12380 14196 276\n")

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

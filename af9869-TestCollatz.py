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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, collatz_cycle_length

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
        s    = "00 0\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  0)
        self.assertEqual(j,  0)

    def test_read2 (self) :
        s    = "-9999 -99999\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  -9999)
        self.assertEqual(j, -99999)

    def test_read3 (self) :
        s    = "1 10\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  1)
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
        v = collatz_eval(10, 100)
        self.assertEqual(v, 119)


    # Also check reverse ordering 
    def test_eval_6 (self) :
        v = collatz_eval(1000, 900)
        self.assertEqual(v, 174)

    def test_eval_7 (self) :
        v = collatz_eval(200, 100)
        self.assertEqual(v, 125)

    def test_eval_8 (self) :
        v = collatz_eval(10, 1)
        self.assertEqual(v, 20)


    # ------------
    # cycle_length
    # ------------

    # TODO: Check for failing assertions 
    def test_cycle_length(self) :
        n = collatz_cycle_length(1)
        self.assertEqual(n, 1)

    def test_cycle_length1(self) :
        n = collatz_cycle_length(99)
        self.assertEqual(n, 26)

    def test_cycle_length2(self) :
        n = collatz_cycle_length(100)
        self.assertEqual(n, 26)

    def test_cycle_length3(self) :
        n = collatz_cycle_length(1000)
        self.assertEqual(n, 112)

    def test_cycle_length4(self) :
        n = collatz_cycle_length(2)
        self.assertEqual(n, 2)

    # -----
    # print
    # -----

    def test_print (self) :
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    def test_print1 (self) :
        w = StringIO()
        collatz_print(w, 100, 100, 100)
        self.assertEqual(w.getvalue(), "100 100 100\n")

    def test_print2 (self) :
        w = StringIO()
        collatz_print(w, 0, 0, 0)
        self.assertEqual(w.getvalue(), "0 0 0\n")

    def test_print3 (self) :
        w = StringIO()
        collatz_print(w, 99999, 99, -1)
        self.assertEqual(w.getvalue(), "99999 99 -1\n")

    # -----
    # solve
    # -----

    def test_solve (self) :
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve1 (self) :
        r = StringIO("9945 55412\n211 2444\n2145 4154\n900 19980\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "9945 55412 340\n211 2444 183\n2145 4154 238\n900 19980 279\n")

    def test_solve3 (self) :
        r = StringIO("6227 4816\n7644 4843\n8698 9482\n177 5354\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "6227 4816 262\n7644 4843 262\n8698 9482 260\n177 5354 238\n")


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

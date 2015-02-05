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

from Collatz import *

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

    def test_read_2(self) : 
        s = "1 10 20\n"
        i, j  = collatz_read(s)
        self.assertEqual(i, 1)
        self.assertEqual(j, 10)

    def test_read_3(self) : 
        s = "1 10 test test"
        i, j = collatz_read(s)
        self.assertEqual(i, 1)
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
        v = collatz_eval(20, 20)
        self.assertEqual(v, 8)
    def test_eval_6 (self) : 
        v = collatz_eval(10, 1)
        self.assertEqual(v, 20)

    # -----
    # check_cache
    # -----

    def test_check_cache_1(self) :
        add_cache(1, 1)
        v = check_cache(1)
        self.assertEqual(v, 1)
        cache.clear()

    def test_check_cache_2(self) :
        v = check_cache(2)
        self.assertEqual(v, 0)
        cache.clear()

    def test_check_cache_3(self) : 
        add_cache(1, 1)
        add_cache(1, 2)
        v = check_cache(1)
        self.assertEqual(v, 2)
        cache.clear()

    # -----
    # add_cache
    # -----

    def test_add_cache_1(self) :
        global cache
        add_cache(1, 1)
        self.assertEqual(cache.get(1, 0), 1)
        cache.clear()
    def test_add_cache_2(self) : 
        global cache
        add_cache(1000, 1)
        self.assertEqual(cache.get(1000, 0), 1)
        cache.clear()


        


    # -----
    # print
    # -----

    def test_print (self) :
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")
    def test_print_2 (self) : 
        w = StringIO()
        collatz_print(w, 999999, 999999, 999999)

    # -----
    # solve
    # -----

    def test_solve (self) :
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")
    def test_solve_2 (self) :
        r = StringIO("1 999999\n999999 999999\n20 20\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 999999 525\n999999 999999 259\n20 20 8\n")
    def test_solve_3 (self) : 
        r = StringIO("10 100\n 100 10\n500 499\n499 500\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "10 100 119\n100 10 119\n500 499 49\n499 500 49\n")

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

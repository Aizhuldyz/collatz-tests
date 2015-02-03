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
        self.assertEqual(i, 1)
        self.assertEqual(j, 10)

    #Additional Tests
    
    def test_read_1 (self) :
        s    = "1 1\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 1)
        self.assertEqual(j, 1)  

    def test_read_2 (self) :
        s    = "10 10\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 10)
        self.assertEqual(j, 10)
        
    def test_read_3 (self) :
        s    = "10 1\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 10)
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

    # Additional Tests
    def test_eval_5 (self) :
        v = collatz_eval(1, 1)
        self.assertEqual(v, 1)

    def test_eval_6 (self) :
        v = collatz_eval(10, 1)
        self.assertEqual(v, 20)    

    def test_eval_7 (self) :
        v = collatz_eval(1, 100)
        self.assertEqual(v, 119)

    def test_eval_8 (self) :
        v = collatz_eval(51, 100)
        self.assertEqual(v, 119)

    def test_eval_9 (self) :
        v = collatz_eval(5, 5)
        self.assertEqual(v, 6)

    def test_eval_10 (self) :
        v = collatz_eval(99, 100)
        self.assertEqual(v, 26)            

    # -----
    # print
    # -----

    def test_print_1 (self) :
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    # Additional Tests
    def test_print_2 (self) :
        w = StringIO()
        collatz_print(w, 1, 1, 1)
        self.assertEqual(w.getvalue(), "1 1 1\n")

    def test_print_3 (self) :
        w = StringIO()
        collatz_print(w, 1, 100, 119)
        self.assertEqual(w.getvalue(), "1 100 119\n")  

    def test_print_4 (self) :
        w = StringIO()
        collatz_print(w, 51, 100, 119)
        self.assertEqual(w.getvalue(), "51 100 119\n")       

    # -----
    # solve
    # -----

    def test_solve (self) :
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    #Additional Tests

    def test_solve_1 (self) :
        r = StringIO("1 1\n5 5\n10 10\n20 20\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 1 1\n5 5 6\n10 10 7\n20 20 8\n")

    def test_solve_2 (self) :
        r = StringIO("15 25\n1 100\n51 100\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "15 25 24\n1 100 119\n51 100 119\n")

    def test_solve_3 (self) :
        r = StringIO("10 20\n14 20\n15 20\n16 20\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "10 20 21\n14 20 21\n15 20 21\n16 20 21\n")

    def test_solve_4 (self) :
        r = StringIO("20 10\n20 14\n15 20\n16 20\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "20 10 21\n20 14 21\n15 20 21\n16 20 21\n")           

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

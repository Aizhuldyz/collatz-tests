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
		
    def test_read_2 (self)    :
        s = "2 20\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 2)
        self.assertEqual(j, 20)
		
    def test_read_3 (self) :
        s = "3 30\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 3)
        self.assertEqual(j, 30)
		

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
        v = collatz_eval(210, 201)
        self.assertEqual(v, 89)

    # -----
    # print
    # -----

    def test_print_1 (self) :
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")
		
    def test_print_2 (self) : 
        w = StringIO()
        collatz_print(w, 1, 1, 1)
        self.assertEqual(w.getvalue(), "1 1 1\n")
		
    def test_print_3 (self) :
        w = StringIO()
        collatz_print(w, 0, 0, 0)
        self.assertEqual(w.getvalue(), "0 0 0\n")

    # -----
    # solve
    # -----

    def test_solve_1 (self) :
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")
		
    def test_solve_2 (self) :
        r = StringIO("1 1\n2 2\n3 3\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 1 1\n2 2 2\n3 3 8\n")
		
    def test_solve_3 (self) : 
        r = StringIO("1 2\n2 3\n3 4\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 2 2\n2 3 8\n3 4 8\n")
        
    # ------------
    # cycle_length
    # ------------
    
    def test_cycle_length_1 (self) :
        n = cycle_length(1)
        self.assertEqual(n, 1)
       
    def test_cycle_length_2 (self) :
        n = cycle_length(333)
        self.assertEqual(n, 113)
       
    def test_cycle_length_3 (self) :
        n = cycle_length(34567)
        self.assertEqual(n, 174)

# ----
# main
# ----

if __name__ == "__main__" :
    main()

""" #pragma: no cover
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
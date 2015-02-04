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

        s    = "956666 999999\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 956666)
        self.assertEqual(j, 999999)

        s    = "9564 9900\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  9564)
        self.assertEqual(j, 9900)

        
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
        v = collatz_eval(9564, 9900)
        self.assertEqual(v, 242)

    def test_eval_7 (self) :
        v = collatz_eval(10, 1)
        self.assertEqual(v, 20)

    def test_eval_8 (self) :
        v = collatz_eval(956666, 999999)
        self.assertEqual(v, 458)

    def test_eval_9 (self) :
        self.assertRaises(AssertionError, collatz_eval,500000, 1000000)
        
    def test_eval_10 (self) :
        self.assertRaises(AssertionError, collatz_eval,1000000, 500000)

    def test_eval_12 (self) :
        self.assertRaises(AssertionError, collatz_eval,0,50)

    def test_eval_13 (self) :
        self.assertRaises(AssertionError, collatz_eval,50,0)

    def test_eval_14 (self) :
       self.assertRaises(AssertionError, collatz_eval,0,0)
       
    

    # -----
    # print
    # -----

    def test_print (self) :
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

        w = StringIO()
        collatz_print(w, 956666, 999999, 458)
        self.assertEqual(w.getvalue(), "956666 999999 458\n")

        w = StringIO()
        collatz_print(w, 9564, 9900, 242)
        self.assertEqual(w.getvalue(), "9564 9900 242\n")

        

    # -----
    # solve
    # -----

    def test_solve (self) :
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n1 1\n 9564 9900\n10 1\n956666 999999\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n1 1 1\n9564 9900 242\n10 1 20\n956666 999999 458\n")
        
# ----
# main
# ----

if __name__ == "__main__" :
    main()

"""
# pragma: no cover
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

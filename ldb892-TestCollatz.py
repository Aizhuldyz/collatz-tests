#/usr/bin/env python3

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
    
    def test_read2 (self) :
        s    = "3004 86"
        i, j = collatz_read(s)
        self.assertEqual(i,  3004)
        self.assertEqual(j, 86)

    # ----
    # eval
    # ----

    #Correcting for actual implementation (1/27)
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
    
    #Tests for bad range where b<a, rearrange and return input
    def test_eval_5 (self) :
        v = collatz_eval(5, 4)
        self.assertEqual(v, 6)
    
    #Tests for the possibility that a = b, which should return just the cycle val of a
    def test_eval_6 (self) :
        v = collatz_eval(4, 4)
        self.assertEqual(v, 3)

    #Tests an intermediate range
    def test_eval_7 (self) :
        v = collatz_eval(1, 90000)
        self.assertEqual(v, 351)

    #Tests to handle the full range
    def test_eval_8 (self) :
        v = collatz_eval(1, 999999)
        self.assertEqual(v, 525)
    
    # -----
    # print
    # -----

    def test_print_1 (self) :
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")
    
    def test_print_2 (self) :
        w = StringIO()
        collatz_print(w, 1, 345, 387)
        self.assertEqual(w.getvalue(), "1 345 387\n")

    def test_print_3 (self) :
        w = StringIO()
        collatz_print(w, 100, 200, 125)
        self.assertEqual(w.getvalue(), "100 200 125\n")
    
    def test_print_4 (self) :
        w = StringIO()
        collatz_print(w, 201, 210, 89)
        self.assertEqual(w.getvalue(), "201 210 89\n")
    
    def test_print_5 (self) :
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
        r = StringIO("34 50\n978 10909\n888888 999999\n1 2\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "34 50 110\n978 10909 262\n888888 999999 507\n1 2 2\n")

    def test_solve_3 (self) :
        r = StringIO("1 1\n9688 8000\n8989 8988\n7777 7777\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 1 1\n9688 8000 260\n8989 8988 79\n7777 7777 84\n")


# ----
# main
# ----

if __name__ == "__main__" :
    main()

"""#pragma: no cover
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

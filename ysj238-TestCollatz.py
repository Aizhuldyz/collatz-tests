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

from Collatz import collatz_read, collatz_eval, collatz_calculate, collatz_print, collatz_solve

# -----------
# TestCollatz
# -----------

class TestCollatz (TestCase) :
    # ----
    # read
    # ----

    def test_read (self) :
        s    = "1 10\n"
        i, j = collatz_read (s)
        self.assertEqual (i,  1)
        self.assertEqual (j, 10)

    # My collatz_read () tests begin.
    def test_read_1 (self):
        s = "1 20\n"
        i, j = collatz_read (s)
        self.assertEqual (i, 1)
        self.assertEqual (j, 20)

    def test_read_2 (self):
        s = "999 1000\n"
        i, j = collatz_read (s)
        self.assertEqual (i, 999)
        self.assertEqual (j, 1000)

    def test_read_3 (self):
        s = "123 22\n"
        i, j = collatz_read (s)
        self.assertEqual (i, 123)
        self.assertEqual (j, 22)
    # My collatz_read () tests end.

    # ----
    # eval
    # ----

    def test_eval_1 (self) :
        v = collatz_eval (1, 10)
        self.assertEqual (v, 20)

    def test_eval_2 (self) :
        v = collatz_eval (100, 200)
        self.assertEqual (v, 125)

    def test_eval_3 (self) :
        v = collatz_eval (201, 210)
        self.assertEqual (v, 89)

    def test_eval_4 (self) :
        v = collatz_eval (900, 1000)
        self.assertEqual (v, 174)

    # My collatz_eval () tests begin.
    def test_eval_5 (self):
        v = collatz_eval (1, 1000)
        self.assertEqual (v, 179)

    def test_eval_6 (self):
        v = collatz_eval (1, 2000)
        self.assertEqual (v, 182)

    def test_eval_7 (self):
        v = collatz_eval (10000, 500)
        self.assertEqual (v, 262)
    # My collatz_eval () tests end.

    # -----------------
    # collatz_calculate
    # -----------------

    # My collatz_calculate () tests start.
    def test_calculate_1 (self):
        c = collatz_calculate (10)
        self.assertEqual (c, 7)

    def test_calculate_2 (self):
        c = collatz_calculate (200)
        self.assertEqual (c, 27)

    def test_calculate_3 (self):
        c = collatz_calculate (10000)
        self.assertEqual (c, 30)
    # My collatz_calculate () tests end.

    # -----
    # print
    # -----

    def test_print (self) :
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue (), "1 10 20\n")

    # My collatz_print () tests begin.
    def test_print_1 (self):
        w = StringIO ()
        collatz_print (w, 1, 1000, 179)
        self.assertEqual (w.getvalue (), "1 1000 179\n")

    def test_print_2 (self):
        w = StringIO ()
        collatz_print (w, 1, 2000, 182)
        self.assertEqual (w.getvalue (), "1 2000 182\n")

    def test_print_3 (self):
        w = StringIO ()
        collatz_print (w, 10000, 500, 262)
        self.assertEqual (w.getvalue (), "10000 500 262\n")
    # My collatz_print () tests end.

    # -----
    # solve
    # -----

    def test_solve (self) :
        r = StringIO ("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO ()
        collatz_solve (r, w)
        self.assertEqual (w.getvalue (), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    # My collatz_solve () tests begin.
    def test_solve_1 (self):
        r = StringIO ("1 100\n200 200\n500 1000\n")
        w = StringIO ()
        collatz_solve (r, w)
        self.assertEqual (w.getvalue (), "1 100 119\n200 200 27\n500 1000 179\n")

    def test_solve_2 (self):
        r = StringIO ("10000 10000\n10000 9999\n500 1\n")
        w = StringIO ()
        collatz_solve (r, w)
        self.assertEqual (w.getvalue (), "10000 10000 30\n10000 9999 92\n500 1 144\n")

    def test_solve_3 (self):
        r = StringIO ("123456 123456\n1 100000\n9876 4321\n")
        w = StringIO ()
        collatz_solve (r, w)
        self.assertEqual (w.getvalue (), "123456 123456 62\n1 100000 351\n9876 4321 262\n")
    # My collatz_solve () tests end.

# ----
# main
# ----

if __name__ == "__main__" :
    main ()

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

from Collatz import collatz_read, collatz_eval, cycle_length, collatz_print, collatz_solve

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
		s    = "100 200\n"
		i, j = collatz_read(s)
		self.assertEqual(i,  100)
		self.assertEqual(j, 200)
		
	def test_read_3 (self) :
		s    = "201 210\n"
		i, j = collatz_read(s)
		self.assertEqual(i,  201)
		self.assertEqual(j, 210)
		
	def test_read_4 (self) :
		s    = "900 1000\n"
		i, j = collatz_read(s)
		self.assertEqual(i,  900)
		self.assertEqual(j, 1000)

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

	# ------------
	# cycle_length
	# ------------
	def test_cycle_length_1(self):
		self.assertEqual(cycle_length(1),1)
		
	def test_cycle_length_2(self):
		self.assertEqual(cycle_length(5),6)
		
	def test_cycle_length_3(self):
		self.assertEqual(cycle_length(10),7)

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
		
	def test_print_5 (self) :
		w = StringIO()
		collatz_print(w, 1000, 900, 174)
		self.assertEqual(w.getvalue(), "1000 900 174\n") 


	# -----
	# solve
	# -----

	def test_solve_1 (self) :
		r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
		w = StringIO()
		collatz_solve(r, w)
		self.assertEqual(w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

	def test_solve_2 (self) :
		r = StringIO("1 1\n5 5\n10 10\n20 20\n")
		w = StringIO()
		collatz_solve(r, w)
		self.assertEqual(w.getvalue(), "1 1 1\n5 5 6\n10 10 7\n20 20 8\n")

	def test_solve_3 (self) :
		r = StringIO("10 1\n200 100\n210 201\n1000 900\n")
		w = StringIO()
		collatz_solve(r, w)
		self.assertEqual(w.getvalue(), "10 1 20\n200 100 125\n210 201 89\n1000 900 174\n")
		
	def test_solve_4 (self) :
		r = StringIO("200 101\n101 200\n")
		w = StringIO()
		collatz_solve(r, w)
		self.assertEqual(w.getvalue(), "200 101 125\n101 200 125\n")

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

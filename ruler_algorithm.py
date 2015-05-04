import sys

def ruler_algorithm(n1, n2):
	"""
	Ruler Algorithm yani Cetvel Algoritmasi. Verilen aralik ikiye bolundugunde
	her alt parca da devamli olarak ikiye bolunmekte. Alt parcalarin uzunlugu
	onceden verilen degere erisinceye kadar devam edilir.
	"""
	dot = (n1+n2)/2
	if abs((n2-n1)) < 2:
		return
	print("[%s]" % dot, end=' ')
	ruler_algorithm(n1, dot)
	ruler_algorithm(dot, n2)

def ruler_algorithm_main():
	sys.stdout.write("Ruler Algorithm: ")
	ruler_algorithm(0,20000)

ruler_algorithm_main()

# profiling result for 20.000 numbers

# profile: python -m profile ruler_algorithm.py

"""
          147457 func
tion calls (114691 primitive calls) in 0.998 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    32767    0.125    0.000    0.125    0.000 :0(abs)
    32767    0.125    0.000    0.125    0.000 :0(charmap_encode)
        1    0.000    0.000    0.998    0.998 :0(exec)
    16383    0.265    0.000    0.484    0.000 :0(print)
        1    0.000    0.000    0.000    0.000 :0(setprofile)
        1    0.000    0.000    0.000    0.000 :0(write)
    32767    0.094    0.000    0.218    0.000 cp857.py:18(encode)
        1    0.000    0.000    0.998    0.998 profile:0(<code object <module> at
 0x01E1C2A0, file "ruler_algorithm.py", line 1>)
        0    0.000             0.000          profile:0(profiler)
        1    0.000    0.000    0.998    0.998 ruler_algorithm.py:1(<module>)
        1    0.000    0.000    0.998    0.998 ruler_algorithm.py:16(ruler_algori
thm_main)
  32767/1    0.390    0.000    0.998    0.998 ruler_algorithm.py:3(ruler_algorit
hm)
"""
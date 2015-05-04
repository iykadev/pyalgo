def golden_ratio(n):
	s = 1
	t = 1
	for i in range(2,n):
		c = s + t
		s = t
		t = c
		sum = (t * 1.0 / s)
		print(sum)

def golden_ratio_main(n):
	golden_ratio(n)

golden_ratio_main(1476)

# profiling result for 1476 numbers

# profile: python -m profile golden_ratio.py

"""
         7376 function calls in 0.125 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
     2948    0.031    0.000    0.031    0.000 :0(charmap_encode)
        1    0.000    0.000    0.125    0.125 :0(exec)
     1474    0.078    0.000    0.125    0.000 :0(print)
        1    0.000    0.000    0.000    0.000 :0(setprofile)
     2948    0.016    0.000    0.047    0.000 cp857.py:18(encode)
        1    0.000    0.000    0.125    0.125 golden_ratio.py:1(<module>)
        1    0.000    0.000    0.125    0.125 golden_ratio.py:1(golden_ratio)
        1    0.000    0.000    0.125    0.125 golden_ratio.py:11(golden_ratio_ma
in)
        1    0.000    0.000    0.125    0.125 profile:0(<code object <module> at
 0x01DCC2A0, file "golden_ratio.py", line 1>)
        0    0.000             0.000          profile:0(profiler)
"""
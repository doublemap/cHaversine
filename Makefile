cHaversine.so: cHaversine/cHaversine.c
	python setup.py build_ext --inplace

cHaversine/cHaversine.c: cHaversine/cHaversine.pyx
	cython $<

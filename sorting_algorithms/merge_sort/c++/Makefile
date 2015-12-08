.PHONY: clean all test

mergesort: mergesort.cpp mergesort.h
	clang++ $< -std=c++11 -o $@ -O2 -g -Wall -Wextra -pedantic

test: mergesort
	./mergesort 10 12

clean:
	rm -f *.o mergesort

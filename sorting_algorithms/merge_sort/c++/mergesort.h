#ifndef MERGESORT
#define MERGESORT

#include <vector>
#include <cstddef>

template<typename T>
void printVector(std::vector<T> input);
template<typename Generator>
void getrands(std::vector<double>&, Generator&, unsigned);

class MergeSort{
public:
	static std::vector<uint64_t> mergeSort(
		std::vector<uint64_t> &inputlist, size_t start = 0, size_t stop = 0);
	static std::vector<double> mergeSort(
		std::vector<double> &inputVector, size_t start = 0, size_t stop = 0);
private:
	template<typename T> static std::vector<T>  mergeSort_internal(std::vector<T> &inputlist);
};

#endif

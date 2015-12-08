#include "mergesort.h"
#include <algorithm> // For sort()
#include <iostream> // For cout
#include <functional> // for ref()
#include <iterator> // For next()
#include <vector> // For vector and advance
#include <cstdlib> // For srand
#include <ctime> // for time


std::vector<uint64_t> MergeSort::mergeSort(std::vector<uint64_t> &inputVector, size_t start, size_t stop){
	size_t size = inputVector.size();

	if (0 == stop){
		stop = size;
	}

	// If start and stop denote less than one element
	if (stop-start < 1 ||
	// or if inputVector contains less elements than start and stop say it has
		size < stop-start){
		// return a vector of equal size, filled with zeroes
		std::vector<uint64_t> newVec(size, 0);
		return newVec;
	}

	// Iterators for sub-vector of inputvector
	std::vector<uint64_t>::iterator it_stop = std::next(inputVector.begin(), stop);
	std::vector<uint64_t>::iterator it_start = std::next(inputVector.begin(), start);

	std::vector<uint64_t> resultVector(it_start, it_stop);

	return MergeSort::mergeSort_internal(inputVector);
}


std::vector<double> MergeSort::mergeSort(std::vector<double> &inputVector, size_t start, size_t stop){
	size_t size = inputVector.size();

	if (0 == stop){
		stop = size;
	}

	// If start and stop denote less than one element
	if (stop-start < 1 ||
	// or if inputVector contains less elements than start and stop say it has
		size < stop-start){
		// return a vector of equal size, filled with zeroes
		std::vector<double> newVec(size, 0.0);
		return newVec;
	}

	// Iterators for sub-vector of inputvector
	std::vector<double>::iterator it_stop = std::next(inputVector.begin(), stop);
	std::vector<double>::iterator it_start = std::next(inputVector.begin(), start);

	std::vector<double> resultVector(it_start, it_stop);

	return MergeSort::mergeSort_internal(inputVector);
}

template<typename T>
std::vector<T>  MergeSort::mergeSort_internal(std::vector<T> &inputVector){
	size_t size = inputVector.size();

	if (size < 2){
		// Basecase of just one element left in list
		return inputVector;
	}

	// Floor division of list midpoint
	size_t midpoint = size/2;

	// iterator for midpoint to ease copying
	typename std::vector<T>::iterator it_midpoint = inputVector.begin();
	std::advance(it_midpoint, midpoint);

	// Copy-creation of lower/upper halves
	std::vector<T> lower_half(inputVector.begin(), it_midpoint);
	std::vector<T> upper_half(it_midpoint, inputVector.end());

	// Recursive call (divide step in divide & conquer)
	lower_half = MergeSort::mergeSort_internal(lower_half);
	upper_half = MergeSort::mergeSort_internal(upper_half);

	// Conquer section
	size_t i = 0, j = 0, k = 0;
	while(i < lower_half.size() && j < upper_half.size()){
		if (upper_half[j] < lower_half[i]){
			inputVector[k++] = upper_half[j++];
		} else{
			inputVector[k++] = lower_half[i++];
		}
	}

	// If upper half emptied first in above while-loop
	while (i < lower_half.size()){
		inputVector[k++] = lower_half[i++];
	}

	// If lower half emptied first in first while-loop
	while (j < upper_half.size()){
		inputVector[k++] = upper_half[j++];
	}

	return inputVector;
}


template<typename T> void printVector(std::vector<T> input){
	std::cout << "[";
	for (size_t i = 0; i < input.size()-1; ++i){
		std::cout << input[i] << ", ";
	}
	std::cout << input[input.size()-1] << "]" << std::endl;
}

// http://stackoverflow.com/a/21695168
template<typename Generator>
void getrands(std::vector<double>& x, Generator& gen, unsigned num){
	generate_n(std::back_inserter(x), num, std::ref(gen));
}

template<typename T>
bool areVectorsIdentical(std::vector<T> vecA, std::vector<T> vecB){
	bool identical = true;

	size_t size = vecA.size();
	if (vecB.size() != size){
		return false;
	}

	for (size_t i = 0; i < size; ++i){
		if (vecA[i] != vecB[i]){
			identical = false;
		}
	}

	return identical;
}


int main(int argc, char const *argv[]){

	if (argc < 3){
		std::cout <<
		"Too few commandline arguments! ./executable <size of list> <max value in list>"
		<< std::endl;
	}

	uint64_t maxValueOfElement = (unsigned) atol(argv[1]);
	size_t maxAmountOfElements = (unsigned) atol(argv[2]);
	size_t amountOfElements = (rand() % maxAmountOfElements) + 1;

	// Use current time as seed for random number generator
	std::srand(std::time(0));

	std::vector<uint64_t> randomVector;
	for (size_t i = 0; i < amountOfElements; ++i){
		int element = (rand() % maxValueOfElement) + 1;
		randomVector.push_back(element);
	}

	std::cout << "Original int-vector:" << std::endl;
	printVector(randomVector);

	std::vector<uint64_t> sortedList = MergeSort::mergeSort(randomVector);

	std::sort(randomVector.begin(), randomVector.end());
	std::cout << "\nsort() -sorted int-vector:" << std::endl;
	printVector(randomVector);

	std::cout << "Merge-Sorted int-vector:" << std::endl;
	printVector(sortedList);

	if (areVectorsIdentical(randomVector, sortedList)){
		std::cout << "\nInteger-Vector was correctly sorted!!" << std::endl;
	} else{
		std::cout << "\nInteger-Vector was incorrectly sorted!!" << std::endl;
	}

	// From: http://stackoverflow.com/a/21695168
	std::uniform_real_distribution<double> unif(0.0, static_cast<double>(maxValueOfElement));
	std::mt19937 re(std::random_device{}());
	auto generator = std::bind(unif, std::ref(re));

	std::vector<double> randomDoubles;

	getrands(randomDoubles, generator, amountOfElements);
	std::cout << "\n\nOriginal double-vector:" << std::endl;
	printVector(randomDoubles);

	std::vector<double> sortedDoubles = MergeSort::mergeSort(randomDoubles);

	std::sort(randomDoubles.begin(), randomDoubles.end());
	std::cout << "\nsort() -sorted double-vector:" << std::endl;
	printVector(randomDoubles);

	std::cout << "Merge-sorted double-vector:" << std::endl;
	printVector(sortedDoubles);

	if(areVectorsIdentical(randomDoubles, sortedDoubles)){
		std::cout << "\nDouble-Vector was correctly sorted!!" << std::endl;
	} else{
		std::cout << "\nDouble-Vector was incorrectly sorted!!" << std::endl;
	}

	return 0;
}

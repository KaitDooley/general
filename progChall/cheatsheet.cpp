// cheatsheet.cpp

#include <iostream>
#include <vector>

using std::cout;
using std::endl;
using std::vector;

int main(int argc, char *argv[]) {
	// create a dynamic array
	vector<int> v = {1, 2, 3};

	// append
	v.push_back(4);

	// prepend
	v.insert(v.begin(), 0);

	// display number of elements
	cout << v.size() << endl;

	// traverse elements
	for (auto e : v) {
		cout << e << endl;
	}

	// traverse elements with index
	for (size_t i = 0; i < v.size(); i++) {
		cout << i << ". " << v[i] << endl;
	}

	return 0;
}

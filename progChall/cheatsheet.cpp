// cheatsheet.cpp

#include <iostream>
#include <vector>
#include <map> 
// #include <unordered_map> 

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




	// create map
	map<char, int> table = {
		{'a', 0},
		{'b', 1},
		{'c', 2},
	};
	// add pair to map
	table['d'] = 3;

	// access value
	cout << table['b'] << endl;
	// cout << table['e'] << endl; // adds value if not there, default 0
	cout << table.at('e') << endl;


	// display number of pairs
	cout << table.size() << endl;

	// traverse pairs
	for (auto pair : table) {
		cout << pair.first << " " << pair.second << endl; // .first is ket, .second is value
	}

	// search
	cout << table.count('b') << endl;
	cout << table.find('b')->second << endl;

	return 0;
}

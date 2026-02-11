// Exercise 08-A: Palindromic Permutations

#include <iostream>
#include <string>
#include <unordered_set>

using namespace std;

// Functions

bool is_palindromic(string &s) {
	unordered_map<char, size_t> counts;
	
	for (auto c : s) {
		counts[tolower(c)++];
	}

	size_t odds = 0;
	for (auto pait : counts) {
		odds += pair.second % 2;
	}

    return odds <= 1;
}

// Main execution

int main(int argc, char *argv[]) {
    string word;

    while (cin >> word) {
    	cout << (is_palindromic(word) ? "Yes" : "No") << endl;
    }

    return 0;
}

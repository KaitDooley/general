#include <algorithm>
#include <iostream>
#include <set>
#include <string>

using namespace std;

// Functions

void permutations(string &p, set<char> &c) {
	// p: Current permutation we are building
	// c: Candidates we can choose
	
	if (c.empty()) {
		cout << p << endl;
	} else {
		auto n = c;
		for (auto candidates : n) {
			// Add candiidate to permutation
			p.push_back(candidate);
			// Remove candidate from candidates
			c.erase(candidate);

			permutations(p, c);  // Recursive call

			// Add candidate to candidates 
			// and remove from permutation
			c.insert(candidate)
			p.pop_back();
		}
	}
}

// Main Execution
int main(int argc, char * argv[]) {
	string p = "";
    set<char> c = {'A', 'B', 'C'};

    permutations(p, c);
    return 0;
}


/* Easy version

// permutations.cpp

#include <algorithm>
#include <iostream>
#include <string>

using namespace std;

// Main execution

int main(int argc, char *argv[]) {
    string s = "ABC";

    sort(s.begin(), s.end());
    do {
    	cout << s << endl;
    } while (next_permutation(s.begin(), s.end()));

    return 0;
}
*/

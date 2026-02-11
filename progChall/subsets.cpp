size_t subsets(vector<int> &s, vector<int> &c, size_t k) {
	if (k == c.size()) {			// Base: have complete subset
		return (accumulate(s.begin(), s.end(), 0) % 3 == 0) ? 1 : 0;
	}

	size_t count = 0;
	count += subsets(s, c, k + 1);	// Recursive: skip current

	s.push_back(c[k]);
	count += subsets(s, c, k + 1);	// Recursive: with current
	s.pop_back();					// Reset subset

	return count;
}                       


int main(int argc, char *argv[]) {
	vector<int> subset;
	vector<int> numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};

	size_t      count   = subsets(subset, numbers, 0, count);
	cout << count << endl;

	return 0;
}


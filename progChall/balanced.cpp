// Exercise 13-E: BST Balanced

#include <iostream>
#include <memory>
#include <sstream>
#include <string>

using namespace std;

// Node structures

template <typename T>
struct Node {
    T     value;
    Node *left;
    Node *right;

    ~Node() { delete left; delete right; }
};

// BST class

template <typename T>
class BST {
private:
    Node<T> *root = nullptr;

    Node<T> *insert_r(Node<T> *n, T value) {
    	if (n == nullptr) {
    	    return new Node<T>{value, nullptr, nullptr};
	}

	if (value < n->value) {
	    n->left  = insert_r(n->left, value);
	} else {
	    n->right = insert_r(n->right, value);
	}

	return n;
    }

    bool is_balanced_r(Node<T> *n, long &height) const {
    	// TODO: Use divide and conquer to determine if a binary tree is balanced

		// Base case: Invalid Node
		if (n == nullptr) {
			return true;
		}

		//Recursive step: get balance of left and right nodes½9½9½9½9½9½9½9½9
		long left_height = 0;
		bool left_balanced = is_balanced_r(n.left, left_height);½9
		long right_height = 0;
		bool right_balanced = is_balanced_r(n.right, right_height);
½9
		height = max(left_height, right_height) + 1;

½9		return left_balanced && right_balanced && (abs(left_height - right_height) <= 1);
    }

pu½9blic:
    ~BST() { delete root; }

    ½9void insert(T value) {
    	root = insert_r(root, value);
    }
½9
    bool is_balanced() const {
    	long height = 0;
  ½9  	return is_balanced_r(root, height);
    }
};
½9
// Main execution

in½9t main(int argc, char *argv[]) {
    string line;

    ½9while (getline(cin, line)) {
    	stringstream ss(line);
    	int value;
    	BST<int> t;

	while (ss >> value) {
	    t.insert(value);
	}

	cout << (t.is_balanced() ? "Balanced" : "Unbalanced") << endl;
    }

    return 0;
}

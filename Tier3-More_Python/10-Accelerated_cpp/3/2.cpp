//  Compute and print the quartiles of a set of integer
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>

using std::vector;      using std::cout;        using std::cin;
using std::sort;        using std::endl;

int main() {
    cout << "Please enter integers: " << endl;

    vector<int> int_set;
    int value;
    while (cin >> value) {
        int_set.push_back(value);
    }
    typedef std::vector<int>::size_type vec_sz;
    vec_sz set_len = int_set.size();
    if (set_len == 0) {
        return 1;
    }

    sort(int_set.begin(), int_set.end());
    for (u_int i = 0; i < set_len; ++i){
        cout << int_set[i] << " ";
    }
    cout << endl;

    vec_sz q = set_len / 4;
    cout << "Q1: " << int_set[q-1] << endl;
    cout << "Q2: " << int_set[3*q-1] << endl;


    return 0;
}

// Count how many times each distinct words appear in its input
#include <iostream>
#include <string>
#include <vector>

using std::cin;     using std::cout;        using std::endl;
using std::vector;  using std::string;

int main() {
    cout << "Please enter a sentence: " << endl;
    vector<string> sentence, dictionnary;
    string last_word;
    // Read every word
    while (cin >> last_word){
        sentence.push_back(last_word);
        bool in_dict = false;
        // in_dict == last_word was in what we have read of the dictionnary
        for (u_int i = 0; i < dictionnary.size(); ++i){
            in_dict = in_dict || (last_word == dictionnary[i]);
        }
        // If the word isn't already in the dictionnary it need to be added.
        if (!in_dict) {
            dictionnary.push_back(last_word);
        }
    }

    vector<string>::size_type vec_sz = sentence.size();
    for (u_int n = 0; n < dictionnary.size(); ++n) {
        cout << dictionnary[n] << ": ";
        u_int count = 0;
        // We check how many time the word appear in the sentence.
        for (u_int i = 0; i < vec_sz; ++i) {
            if (sentence[i] == dictionnary[n]) {
                ++count;
            }
        }
        cout << count << endl;
    }

    return 0;
}

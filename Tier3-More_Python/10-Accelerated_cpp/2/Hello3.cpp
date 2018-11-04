#include <iostream>
#include <string>

using std::cin;
using std::endl;
using std::cout;
using std::string;

int main() {
    cout << "Please enter your name: ";

    string name;
    cin >> name;

    const string greetings = "Hello, " + name + "!";

    const int PAD = 1;
    const int rows = PAD * 2 + 3;
    const string::size_type cols = greetings.size() + PAD * 2 + 2;

    for (int r = 0; r < rows; ++r){
        string::size_type c = 0;
        while (c != cols) {
            if (r == PAD + 1 && c == PAD + 1) {
                cout << greetings;
                c += greetings.size();
            } else {
                if (r == 0 || r == rows - 1 || c == 0 || c == cols - 1) {
                    cout << '*';
                } else {
                    cout << " ";
                }
                ++c;
            }
        }
        cout << endl;
    }
    return 0;
}

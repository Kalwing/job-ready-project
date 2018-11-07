#include <iostream>
#include <string>

int main() {
    std::cout << "Enter your sentence: " << std::endl;
    std::string last_word;
    std::string shortest;
    std::string longest;

    std::cin >> last_word;
    shortest = last_word;
    longest = last_word;
    while (std::cin >> last_word) {
        if (last_word.length() > longest.length()) {
            longest = last_word;
        }
        if (last_word.length() < shortest.length()) {
            shortest = last_word;
        }
    }
    std::cout << longest << " is the longest: " << longest.length() << std::endl;
    std::cout << shortest << " is the shortest: " << shortest.length() << std::endl;

    return 0;
}

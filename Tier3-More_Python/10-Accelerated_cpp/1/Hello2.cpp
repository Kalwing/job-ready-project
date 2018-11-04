#include <iostream>
#include <string>

int main() {
    std::cout << "Please enter your name: ";

    std::string name;
    std::cin >> name;

    const std::string greetings = "Hello, " + name + "!";

    const std::string spaces(greetings.size(), ' ');
    const std::string space_line = "* " + spaces + " *";
    const std::string delimitation(space_line.size(), '*');

    std::cout << delimitation << std::endl;
    std::cout << space_line << std::endl;
    std::cout << "* " + greetings + " *" << std::endl;
    std::cout << space_line << std::endl;
    std::cout << delimitation << std::endl;

    return 0;
}

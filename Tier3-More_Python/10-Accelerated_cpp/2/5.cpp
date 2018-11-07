#include <iostream>
#include <string>

int main(){
    const int width = 12;
    const int height = 7;
    // Square
    for (int y = 0; y < height; ++y) {
        for (int x = 0; x < height; ++x) {
            std::cout << '*';
        }
        std::cout << std::endl;
    }
    // Rectangle
    std::cout << std::endl;
    for (int y = 0; y < height; ++y) {
        for (int x = 0; x < width; ++x) {
            std::cout << '*';
        }
        std::cout << std::endl;
    }
    // Triangle
    std::cout << std::endl;
    const float top_x = width/2;
    const float coeff_up = (top_x) / (height);
    const float coeff_down = (width - top_x) / (-height);
    for (int y = 0; y < height; ++y) {
        for (int x = 0; x < width; ++x) {
            if (x < top_x) {
                if (x > coeff_up * (height - y)) {
                    std::cout << '*';
                } else {
                    std::cout << '-';
                }
            } else {
                if (x < coeff_down * (height - y) + ((width - top_x)*top_x + height*height)/height) {
                    std::cout << '*';
                } else {
                    std::cout << '-';
                }
            }

        }
        std::cout << std::endl;
    }

    return 0;
}

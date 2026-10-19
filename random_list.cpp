#include <iostream>
#include <fstream>
#include <string>
#include "class_random.h"

int main() {
    myRandom random_number;
    std::vector<double> numbers = random_number.random(10);

    std::cout<<random_number.random()<<std::endl;
    
    std::ofstream outputfile;

    outputfile.open("random_numbers_list.txt");
    
    for(int i=0;i<10;i++){
        outputfile << i+1 << " " << numbers[i] <<std::endl;
        std::cout << i+1 << " " << numbers[i] <<std::endl;
    }
}
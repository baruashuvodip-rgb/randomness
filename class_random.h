#ifndef _MY_RANDOM_
#define _MY_RANDOM_

#include <vector>
#include <ctime> // For random seed
#include <cmath> // For pow function
#include <stdexcept>

class myRandom{
    long long A, c, modulus, x_0;
    double a, b;
    public:
        myRandom(double a = 0.0, double b = 1.0) {
        this->a = a;
        this->b = b;
        this->A = 1664525;
        this->c = 1013904223;
        this->modulus = std::pow(2.0,32);
        this->x_0 = time(0);
        }   

    double random() {
        this->x_0 = (this->A*this->x_0 + this->c) % this->modulus;
        return (this->b-this->a)*(this->x_0/(this->modulus-1.0)) + this->a;
    }

    std::vector<double> random(int N){
        if (N < 0){
            throw std::runtime_error("N must be a positive integer");
        }
        std::vector<double> rans;
        for (int i = 0; i < N; ++i) {
            rans.push_back(this->random());
        }
        return rans;
    }
};

#endif
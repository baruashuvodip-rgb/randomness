#include <iostream>
#include <random>

int main() {
    
    std::random_device seeder; //<random> library object. uses system entropy to generate one truly random number
    std::mt19937_64 gen(seeder()); //Mersenne Twister algorithm; will use seeder to generate pseudo random numbers
    std::uniform_real_distribution<double> dist(0.0, 1.0); //changes here change the distribution. the other lines remain unchanged.
    //two possible alternatives:
    //std::uniform_int_distribution<int> dist(a, b); // Uniform ints between a and b
    //std::normal_distribution<double> dist(mu, sigma); // Gaussian distribution
    
    std::cout.precision(15);
   
    for (int i = 0; i < 10; ++i) {
        std::cout << dist(gen) << std::endl;
    }
    
    return 0;
}
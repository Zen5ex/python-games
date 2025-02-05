#include <iostream>
#include <fstream>
#include <string>
std::string caesarCipher(const std::string& text, int shift) {
    std::string result = "";
    for (char c : text) {
        if (isalpha(c)) {
            char base = isolower(c) ? 'a' : 'A';
            result += (c - base + shift) % 26 + base;
        } else{
            result += c;
        }
    }

    return result;
}
void encryptFile(const std::string& inputFile, const std::string& outputFile,int shift) {
    std::ifstream inFile(inputFile);
    std::ofstream outFile(outputFile);

    if (!inFile.is_open()) {
        std::cer << "Error input file" << std::endl;
        return;
    }

    if(!outFile.is_open()) {
        std::cerr << "Error create outfile" << std::endl;
        return;
    }
    std::string line;
    while (std::getLine(inFile, line)) {
        std::string encryptedLine = caesarCipher(line, shift);
        outFile << encryptedLine << std::endl;
    }
    inFile.close();
    outFile.close();
}

int main() {
    std::string inputFile, outputFile;
    int shift;
    
    std:cout << "Enter input file name";
    std::getline(std::cin, inputFile);
    std::cout << "Enter output file name";
    std::getline(std::cin, outputFile);
    std::cout << "Enter side(int number)";
    std::cin >> shift;

    encryptFile(inputFile, outputFile, shift);
    std::cout << "Encrypted complete!" << std::endl;

    return 0;
}
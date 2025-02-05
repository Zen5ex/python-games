#include <iostream>
#include <fstream>
#include <string>

std::string caesarCipher(const std::string& text, int shift) {
    std::string result = "";

    for (char c : text) {
        // Шифруем только буквы
        if (isalpha(c)) {
            char base = islower(c) ? 'a' : 'A';
            // Сдвигаем букву и обрабатываем переполнение
            result += (c - base + shift) % 26 + base;
        } else {
            // Не шифруем символы, которые не являются буквами
            result += c;
        }
    }

    return result;
}

void encryptFile(const std::string& inputFile, const std::string& outputFile, int shift) {
    std::ifstream inFile(inputFile);
    std::ofstream outFile(outputFile);

    if (!inFile.is_open()) {
        std::cerr << "Ошибка при открытии входного файла!" << std::endl;
        return;
    }

    if (!outFile.is_open()) {
        std::cerr << "Ошибка при создании выходного файла!" << std::endl;
        return;
    }

    std::string line;
    while (std::getline(inFile, line)) {
        std::string encryptedLine = caesarCipher(line, shift);
        outFile << encryptedLine << std::endl;
    }

    inFile.close();
    outFile.close();
}

int main() {
    std::string inputFile, outputFile;
    int shift;

    std::cout << "Введите имя входного файла: ";
    std::getline(std::cin, inputFile);
    std::cout << "Введите имя выходного файла: ";
    std::getline(std::cin, outputFile);
    std::cout << "Введите сдвиг (целое число): ";
    std::cin >> shift;

    encryptFile(inputFile, outputFile, shift);
    std::cout << "Шифрование завершено!" << std::endl;

    return 0;
}

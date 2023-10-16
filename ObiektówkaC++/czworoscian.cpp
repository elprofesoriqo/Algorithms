#include <iostream>
#include <cmath>

class Trojkat {
private:
    double x;

public:
    Trojkat(double bok) : x(bok) {}

    // Metoda do pobierania wartości pola x.
    double pobierzBok() const {
        return x;
    }

    // Metoda do obliczania pola powierzchni trójkąta.
    double obliczPolePowierzchni() const {
        // Zakładamy, że trójkąt jest równoboczny.
        return (sqrt(3.0) / 4.0) * x * x;
    }
};

class CzworoscianForemny : public Trojkat {
public:
    CzworoscianForemny(double bok) : Trojkat(bok) {}

    // Metoda do obliczania pola powierzchni całkowitej czworościanu foremnego.
    double obliczPolePowierzchniCzworoscianu() const {
        double poleTrojkata = obliczPolePowierzchni();
        return 4 * poleTrojkata;
    }
};

int main() {
    double dlugoscBoku = 5.0; // Długość boku trójkąta

    // Tworzenie obiektu klasy CzworoscianForemny
    CzworoscianForemny czworoscian(dlugoscBoku);

    // Obliczanie i wyświetlanie pola powierzchni całkowitej czworościanu
    double poleCzworoscianu = czworoscian.obliczPolePowierzchniCzworoscianu();
    std::cout << "Pole powierzchni całkowitej czworościanu foremnego: " << poleCzworoscianu << std::endl;

    return 0;
}
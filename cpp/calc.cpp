#include "calc.h"

class Calculator
{
public:
    int sub(int a, int b)
    {
        return a - b;
    }
};

int sub(int a, int b)
{
    return Calculator().sub(a, b);
}
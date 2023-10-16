#include <iostream>

using namespace std;

class Figura
{
public:
    Figura(float ax=0, float ay=0);
    void Pisz();
    void Przesun(float dx, float dy);
private:
    float x, y;
};

Figura::Figura(float ax, float ay)
{
    x=ax;
    y=ay;
}
void Figura::Pisz()
{
    cout<<"x = "<<x<<endl;
    cout<<"y = "<<y<<endl;
}
void Figura::Przesun(float dx, float dy)
{
    float p=dx;
    float q=dy;
    x=x-p;
    y=y+q;
}
class Okrag:public Figura
{
public:
    Okrag(float ar=1, float ax=0, float ay=0);
    void Pisz();
    void Obwod();
private:
    float r;
};

Okrag::Okrag(float ar, float ax, float ay):Figura(ax,ay)
{
    if (ar>0) r=ar;
    else r=1;
}

void Okrag::Pisz()
{
    Figura::Pisz();
    cout<<"r = "<<r<<endl;
}
void Okrag::Obwod()
{
    float PI=3.14;
    float obwod=0;
    obwod=2*PI*r;
    cout<<obwod<<endl;
}

int main()
{
    Okrag o(10,3,5);
    cout<<"Polozenie i promien okregu:"<<endl;
    o.Pisz();
    cout<<"Obwod: ";o.Obwod();
    o.Przesun(2,3);
    cout<<"Dane okregu po przesunieciu:"<<endl;
    o.Pisz();
    return 0;

};
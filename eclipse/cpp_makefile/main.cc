#include <iostream>
#include "add2.hh"
#include "add4.hh"

using std::cout;
using std::endl;

int main(int argc, char* argv[])
{
  cout << add2(1, 2) << endl;
  cout << add2(1.0, 2.0) << endl;
  cout << add4(1, 2, 3, 4) << endl;
  return 0;
}
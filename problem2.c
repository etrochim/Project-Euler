#include <stdio.h>

int main() {
  int a = 1;
  int b = 2;
  int sum = 2;
  int result = 0;
  while(result < 4000000) {
    result = a + b;
    if(result % 2 == 0) {
      sum += result;
    }
    a = b;
    b = result;
  }
  printf("The sum is %d", sum);
}

#include <stdio.h>

int sizex = 4;
int sizey = 4;
unsigned long long int paths = 0;

void increment(int x, int y) {
  if(x == sizex && y == sizey) {
    paths++;
    return;
  }

  if(sizex != x) {
    increment(x+1, y);
  }
  if(sizey != y) {
    increment(x, y+1);
  }
}

int main() {
  for(int i = 20; i <= 20; i++) {
    sizex=i;
    sizey=i;
    paths=0;
    increment(0,0);
    printf("paths for %dx%d: %llu\n", sizex, sizey, paths);
  }
}

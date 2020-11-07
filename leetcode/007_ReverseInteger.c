// 7. Reverse Integer
// Difficulty: Easy
// URL: https://leetcode.com/problems/reverse-integer/

// Given a 32-bit signed integer, reverse digits of an integer.
// Note:
// Assume we are dealing with an environment that could only store integers 
// within the 32-bit signed integer range: [−231,  231 − 1]. 
// For the purpose of this problem, assume that your function returns 0 when the
// reversed integer overflows.

// Example 1:
// Input: x = 123
// Output: 321

#include <stdio.h>
#include <stdbool.h>

int MAX_NEG_INT = -2147483648;
int MAX_INT     =  2147483647;

int reverse(int x){

  if (x < 10 && x > -10) return x;
  if (x < MAX_NEG_INT) return false;
  if (x > MAX_INT) return false;

  long digits = 1;
  long y = x/10;

  while (y >= 1 || y <= -1){
    y /= 10;
    digits *= 10;
  };

  long rev = 0;
  long dig = 0;
  long i = 1;

  while(x > 1 || x < -1){
    dig = (x % (i*10)) / (i);

    if (x > 0 && dig * digits/i > MAX_INT - rev) return 0;
    if (x < 0 && dig * digits/i < MAX_NEG_INT - rev) return 0;
    rev += dig * digits/i;

    x -= dig * (i);
    i *= 10;
  }

  return rev;
}

int main (){
  printf("%d\n", reverse(123));
  printf("%d\n", reverse(900000));
  printf("%d\n", reverse(1534236469));
  printf("%d\n", reverse(-2147483412));
}
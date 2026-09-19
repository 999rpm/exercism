#include "grains.h"
#include <inttypes.h>
#include <stdint.h>
#include <stdio.h>
uint64_t square(uint8_t index) {
  return (index < 1 || index > 64) ? 0: (uint64_t)1 << (index - 1);
}
uint64_t total(void) {
  uint64_t sum = 0;
  for (uint8_t i = 0; i <= 64; ++i) {
    sum += square(i);
  }
  return sum;
}
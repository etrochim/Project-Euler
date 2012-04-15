#!/usr/bin/perl

use strict;
use warnings;

my $x = 2;
my $num = 1;
for(; ;) {
  $num += $x++;
  if(factorize($num) > 500) {
    print $num, "\n";
    last;
  }
}

sub factorize {
  my $num = shift;

  my $sqrt = sqrt($num);
  my $factors = 1;
  for(my $x = 2; $x < $sqrt; $x++) {
    if($num % $x == 0) {
      $factors++;
    }
  }

  return $factors * 2;
}

#!/usr/bin/perl

my $a = 1;
my $b = 2;
my $sum = 2;
my $result = 0;

while($result < 4000000) {
  $result = $a + $b;
  if($result % 2 == 0) {
    $sum += $result;
  }
  $a = $b;
  $b = $result;
}

print "The sum is $sum\n";

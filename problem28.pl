#!/usr/bin/perl

my $sum = 1;
my $step = 2;
my $number = 1;

my $limit = 1002001;

while(1) {
  for(1..4) {
    $number += $step;
    if($number > $limit) {
      print "$sum\n";
      exit;
    }
    $sum += $number;
  }
  $step += 2;
}

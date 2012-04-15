#!/usr/bin/perl

use strict;
use warnings;
use List::Util qw(max);

my $triangle = [];
open my $fh, '<', '/Users/etrochim/Documents/Problem 67/datafile'
  or die "Failed to open datafile: $!";
while(<$fh>) {
  chomp;
  push @$triangle, [ split / / ];
}
close $fh;

foreach(my $x = 1; $x < scalar(@$triangle); $x++) {
  foreach(my $y = 0; $y < scalar(@{$triangle->[$x]}); $y++) {
    if($y == 0) {
      $triangle->[$x]->[$y] += $triangle->[$x-1]->[$y];
    }
    elsif($y == $#{$triangle->[$x]}) {
      $triangle->[$x]->[$y] += $triangle->[$x-1]->[$y-1]; 
    }
    else {
      $triangle->[$x]->[$y] = max($triangle->[$x]->[$y] + $triangle->[$x-1]->[$y],
                                  $triangle->[$x]->[$y] + $triangle->[$x-1]->[$y-1]);
    }
  }
  print join ' ', @{$triangle->[$x]}, "\n";
}

print max(@{$triangle->[-1]}), "\n";

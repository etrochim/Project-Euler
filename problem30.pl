#!/usr/bin/perl

use List::Util qw(sum);

my $sum = 0;
for(my $i = 100; $i < 1000000; $i++) {
  if($i == sum(map { $_ ** 5 } split('', $i))) {
    print "Found $i\n";
    $sum += $i;
  }
}
print "Sum $sum\n";

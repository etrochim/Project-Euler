#!/usr/bin/perl

use strict;
use warnings;

use List::Util qw(min);

open my $fh, '<', 'matrix.txt' or die "Failed to open matrix.txt: $!";
my $matrix = [];
while(my $line = <$fh>) {
    chomp $line;
    push @$matrix, [ split(',', $line) ];
}
close $fh;

for(my $x = 0; $x < scalar(@$matrix); $x++) {
    for(my $y = 0; $y < scalar(@{$matrix->[$x]}); $y++) {
        if($x > 0 and $y > 0) {
            $matrix->[$x]->[$y] = min($matrix->[$x]->[$y-1] + $matrix->[$x]->[$y],
                                        $matrix->[$x-1]->[$y] + $matrix->[$x]->[$y]);
        }
        elsif($y > 0) {
            $matrix->[$x]->[$y] += $matrix->[$x]->[$y-1];
        }
        elsif($x > 0) {
            $matrix->[$x]->[$y] += $matrix->[$x-1]->[$y];
        }
    }
}

print "Sum: " . $matrix->[$#{$matrix}]->[$#{$matrix->[0]}]. "\n";

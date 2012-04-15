#!/usr/bin/perl

my $string = '';
foreach (1..1000000) {
  $string .= $_;
}

print substr($string, 0, 50), "\n";

print substr($string, 1-1, 1) * 
      substr($string, 10-1, 1) *
      substr($string, 100-1, 1) *
      substr($string, 1000-1, 1) *
      substr($string, 10000-1, 1) *
      substr($string, 100000-1, 1) *
      substr($string, 1000000-1, 1);


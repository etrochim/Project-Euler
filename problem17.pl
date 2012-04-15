#!/usr/bin/perl

use POSIX qw(floor);
use strict;
use warnings;

my %numbers = (
  1 => 'one',
  2 => 'two',
  3 => 'three',
  4 => 'four',
  5 => 'five',
  6 => 'six',
  7 => 'seven',
  8 => 'eight',
  9 => 'nine',
  10 => 'ten',
  11 => 'eleven',
  12 => 'twelve',
  13 => 'thirteen',
  14 => 'fourteen',
  15 => 'fifteen',
  16 => 'sixteen',
  17 => 'seventeen',
  18 => 'eighteen',
  19 => 'nineteen',
  20 => 'twenty',
  30 => 'thirty',
  40 => 'forty',
  50 => 'fifty',
  60 => 'sixty',
  70 => 'seventy',
  80 => 'eighty',
  90 => 'ninety',
  100 => 'hundred',
  1000 => 'onethousand'
);

my $string = '';
foreach my $i (1..1000) {
  if(floor($i/1000%10)) {
    $string .= $numbers{1000};
  }
  if(my $hundreds_place = floor($i/100%10)) {
    $string .= $numbers{$hundreds_place} . $numbers{100};
    if($i%100 != 0) {
      $string .= 'and';
    }
  }
  if(my $tens_place = floor($i/10%10)) {
    if($tens_place == 1) {
      $string .= $numbers{$i%100};
      print "$string\n";
      next;
    }
    else {
      $string .= $numbers{$tens_place * 10}
    }
  }
  if(my $ones_place = floor($i%10)) {
    $string .= $numbers{$ones_place};
  }

}

print length($string);

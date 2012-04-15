#!/usr/bin/perl

my $paths = 0;
my $size_x = 15;
my $size_y = 15;

sub increment {
  my ($x, $y) = @_;

  if($x == $size_x and $y == $size_y) {
    $paths++;
    return;
  }

  unless($size_x == $x)  {
    increment($x+1, $y);
  }
  unless($size_y == $y) {
    increment($x, $y+1);
  }
}

increment(0, 0);

print "paths: $paths\n";

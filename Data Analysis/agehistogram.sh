#!/usr/bin/env bash

INPUT="age_counts.csv"
OUT="age_distribution.png"

gnuplot <<EOF
set terminal pngcairo size 800,600
set output "$OUT"

set datafile separator ","

set style fill solid
set boxwidth 10   # adjust depending on your bin spacing

set xlabel "Age"
set ylabel "Count"
set title "Age Distribution"

set grid ytics
set xtics 0,10,100

plot "$INPUT" using 1:2 with boxes notitle
EOF

echo "Saved plot to $OUT"
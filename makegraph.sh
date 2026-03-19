#!/usr/bin/env bash

INPUT="clinical_data.csv"
TMP="sex_counts.dat"
OUT="sex_distribution.png"

# Extract counts (skip header automatically)
awk -F, '
NR > 1 {
    gsub(/^[ \t]+|[ \t]+$/, "", $4)   # trim spaces
    if ($4 == "Male") m++
    else if ($4 == "Female") f++
}
END {
    total = m + f
    if (total == 0) {
        print "Error: no valid Male/Female data found" > "/dev/stderr"
        exit 1
    }
    printf "Male %.0f\n", 100*m/total
    printf "Female %.0f\n", 100*f/total
}' "$INPUT" > "$TMP"

# Plot with gnuplot
gnuplot <<EOF
set terminal pngcairo size 800,600
set output "$OUT"

set style data histograms
set style fill solid
set boxwidth 0.5
set title "Patient Sex Distribution Percentage"

unset ytics
set yrange [0:100]

plot "$TMP" using 2:xtic(1) with boxes notitle, \
     "" using 0:2:2 with labels offset 0,1 notitle
EOF

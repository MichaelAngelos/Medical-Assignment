#!/usr/bin/env bash

INPUT="clinical_data.csv"
TMP="ages_clean.dat"
OUT="age_hist.png"

# Step 1: extract minimum age per patient
awk -F, '
NR > 1 {
    id = $1
    age = $3 + 0

    if (!(id in min_age) || age < min_age[id]) {
        min_age[id] = age
    }
}
END {
    for (id in min_age) {
        print min_age[id]
    }
}' "$INPUT" > "$TMP"

# Step 2: plot histogram
gnuplot <<EOF
set terminal pngcairo size 800,600
set output "$OUT"

binwidth = 10
bin(x,width) = width * floor(x/width)

set boxwidth binwidth
set style fill solid

set xlabel "Age"
set ylabel "Count"
set title "Age Distribution"

# Light grid for reference
set grid ytics lc rgb "#cccccc" lw 1

# Strong vertical bin lines (every 5 years)
do for [x=0:100:5] {
    set arrow from x,0 to x,graph 1 nohead lc rgb "black" lw 1
}

plot "$TMP" using (bin(\$1,binwidth)):(1.0) smooth freq with boxes notitle
EOF

echo "Saved histogram to $OUT"
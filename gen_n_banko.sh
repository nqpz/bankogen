#!/bin/sh

set -e
mkdir -p gen

N="$1"

for i in $(seq 0 $(expr $N - 1)); do
    fname=gen/bankoplade_$i.svg
    ./bankogen.py > $fname
    ./svg2pdf.sh $fname
done

pdfjoin -o bankoplader.pdf gen/*.pdf

#!/bin/sh
fullsvgname="$1"
dirname=$(dirname "$fullsvgname")
svgname=$(basename "$fullsvgname")
basename=${svgname%.*}
pdfname="$basename.pdf"
fullpdfname="$dirname/$pdfname"
echo "Converting $svgname to $pdfname..."
inkscape "--export-pdf=$fullpdfname" "$fullsvgname"

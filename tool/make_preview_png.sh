for p in resource/*.svg
do
    echo $p
    inkscape -b white -w 512 -p $p -o ${p::${#p}-4}_preview.png
done

# pip install scour

for p in resource/*.svg
do
    scour -i $p -o ${p}_tmp
    mv ${p}_tmp $p
done

for p in demo/*.py
do
    PYTHONPATH=. python $p
done

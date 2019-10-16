problem=$1

curr_in=".in"
curr_out=".ans"

tn=0
for a in "" `seq 0 9`;
do
    for b in "" `seq 0 9`;
    do
        for c in `seq 0 9`;
        do
            fin=$problem/$a$b$c$curr_in
            if [ -e $fin ]
            then
                ((tn++))
                echo $fin
                mv $fin $problem/`printf '%03d' $tn`
            fi

            fout=$problem/$a$b$c$curr_out
            if [ -e $fout ]
            then
                echo $fout
                mv $fout $problem/`printf '%03d.a' $tn`
            fi
        done
    done
done


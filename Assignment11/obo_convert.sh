egrep "\[Term\]|\[Typedef\]|^id:|^name:|^def:|^namespace:" goslim_plant.obo  | sed 's/\[Term\]/||/g' | sed 's/\[Typedef\]/==/g'  | sed 's/id: /--/g' | sed 's/name: /--/g' | sed 's/def: /--/g' | sed 's/namespace: /--/g' | sed ':a;N;$!ba;s/\n//g' | sed 's/||/\n/g' | sed 's/==/\n==/g' | sed 's/--/\t/g' | grep -v '^==' | sed 's/^\t//'  > goslim_GOterms.txt


echo Votre nombre:
read nombre
if [[ $nombre -lt 10 ]]
then
    echo nombre a 1 chiffre
fi
if [[ $nombre -lt 100 ]] && [[ $nombre -gt 10 ]] ; then
    echo nombre a 2 chiffre
fi
if [[ $nombre -lt 1000 ]] && [[ $nombre -gt 100 ]]; then
    echo nombre a 3  chiffre
fi

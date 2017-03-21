#train.sh
rm vw.model vw.cache predictions.txt
vw -f vw.model --passes=10 --cache_file=vw.cache --kill_cache --l2 1 < train

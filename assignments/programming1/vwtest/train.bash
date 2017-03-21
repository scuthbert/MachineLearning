#train.sh
rm iris.model iris.cache predictions.txt
vw -f iris.model --passes=1000 --cache_file=iris.cache --kill_cache  --oaa 3 --nn 3 < iris.train.vw

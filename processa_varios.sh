#Incompleto
#Não executar
echo "Processa tweets"

echo "Processando de 0 a 10000"
python processa_json_tweets_parallel.py tweets_debateband_20180809_02.txt 0 10000
echo ""

echo "Processando de 10001 a 20000"
python processa_json_tweets_parallel.py tweets_debateband_20180809_02.txt 10001 20000
echo ""

echo "Processando de 20001 a 30000"
python processa_json_tweets_parallel.py tweets_debateband_20180809_02.txt 20001 30000
echo ""

echo "Processando de 30001 a 40000"
python processa_json_tweets_parallel.py tweets_debateband_20180809_02.txt 30001 40000
echo ""

echo "Processando de 40001 a 50000"
python processa_json_tweets_parallel.py tweets_debateband_20180809_02.txt 40001 50000
echo ""

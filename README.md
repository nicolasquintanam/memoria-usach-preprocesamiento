### Instalación Linux para Preprocesamiento

```

sudo apt-get update
apt install python3-pip zip unzip -y &&
pip3 install --upgrade pip
pip3 install nltk
pip3 install spacy
pip3 install pandas
pip3 install xlsxwriter
pip3 install sklearn
python3 -m spacy download es_core_news_md
python3
import nltk
nltk.download('punkt')
nltk.download('stopwords')
exit()
git clone https://github.com/nicolasquintanam/memoria-usach-preprocesamiento
cd memoria-usach-preprocesamiento
nohup python3 -u main.py &

```

### Instalación Linux para Entrenamiento

```

sudo apt-get update
apt install python3-pip zip unzip -y &&
pip3 install --upgrade pip
pip3 install nltk
pip3 install spacy
pip3 install pandas
pip3 install xlsxwriter
pip3 install sklearn
python3 -m spacy download es_core_news_md
python3
import nltk
nltk.download('punkt')
nltk.download('stopwords')
exit()
git clone https://github.com/nicolasquintanam/memoria-usach-preprocesamiento
cd memoria-usach-preprocesamiento
cd entrenamiento

# ---- Flujo base -----
wget --load-cookies /tmp/cookies.txt "https://drive.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://drive.google.com/uc?export=download&id=10WzxojnH1CxRC_vHCQt0fUV3TgiZIaLQ' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=10WzxojnH1CxRC_vHCQt0fUV3TgiZIaLQ" -O flujo_base.zip && rm -rf /tmp/cookies.txt
unzip flujo_base.zip
pyhton3 split2.py --input flujo_base
python3 entrenamiento.py --input flujo_base

# ---- Flujo experimental 1 -----
wget --load-cookies /tmp/cookies.txt "https://drive.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://drive.google.com/uc?export=download&id=1C_QUG6RpYTTM0scoQvF45v8PrNyZk_b2' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=1C_QUG6RpYTTM0scoQvF45v8PrNyZk_b2" -O flujo_experimental_1.zip && rm -rf /tmp/cookies.txt
unzip flujo_experimental_1.zip
pyhton3 split2.py --input flujo_experimental_1
python3 entrenamiento.py --input flujo_experimental_1

# ---- Flujo experimental 2 -----
wget --load-cookies /tmp/cookies.txt "https://drive.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://drive.google.com/uc?export=download&id=14APS8v7_Rsh0n33i6FDE4JOVAxSTnew7' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=14APS8v7_Rsh0n33i6FDE4JOVAxSTnew7" -O flujo_experimental_2.zip && rm -rf /tmp/cookies.txt
unzip flujo_experimental_2.zip
pyhton3 split2.py --input flujo_experimental_2
python3 entrenamiento.py --input flujo_experimental_2

# ---- Flujo experimental 3 -----
wget --load-cookies /tmp/cookies.txt "https://drive.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://drive.google.com/uc?export=download&id=1dkZCkRUpqN6J8E80YNxV9Rew7uHdjCv9' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=1dkZCkRUpqN6J8E80YNxV9Rew7uHdjCv9" -O flujo_experimental_3.zip && rm -rf /tmp/cookies.txt
unzip flujo_experimental_3.zip
pyhton3 split2.py --input flujo_experimental_3
python3 entrenamiento.py --input flujo_experimental_3

# ---- Flujo experimental 4 -----
wget --load-cookies /tmp/cookies.txt "https://drive.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://drive.google.com/uc?export=download&id=1iQlrkUpnjX-kXnLtOfijuamN3VrdPaT3' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=1iQlrkUpnjX-kXnLtOfijuamN3VrdPaT3" -O flujo_experimental_4.zip && rm -rf /tmp/cookies.txt
unzip flujo_experimental_4.zip
pyhton3 split2.py --input flujo_experimental_4
python3 entrenamiento.py --input flujo_experimental_4

# ---- Flujo experimental 5 -----
wget --load-cookies /tmp/cookies.txt "https://drive.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://drive.google.com/uc?export=download&id=1OY3AucIPOpUlFjcZ5m-xuhmcijgG0rza' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=1OY3AucIPOpUlFjcZ5m-xuhmcijgG0rza" -O flujo_experimental_5.zip && rm -rf /tmp/cookies.txt
unzip flujo_experimental_5.zip
pyhton3 split2.py --input flujo_experimental_5
python3 entrenamiento.py --input flujo_experimental_5

# ---- Flujo experimental 6 -----
wget --load-cookies /tmp/cookies.txt "https://drive.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://drive.google.com/uc?export=download&id=IDDDDD' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=IDDDDD" -O flujo_experimental_6.zip && rm -rf /tmp/cookies.txt
unzip flujo_experimental_6.zip
pyhton3 split2.py --input flujo_experimental_6
python3 entrenamiento.py --input flujo_experimental_6

# ---- Flujo experimental 7 -----
wget --load-cookies /tmp/cookies.txt "https://drive.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://drive.google.com/uc?export=download&id=1oEn8DvCJcjXrWLwTA7SQicxq_B071XHg' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=1oEn8DvCJcjXrWLwTA7SQicxq_B071XHg" -O flujo_experimental_7.zip && rm -rf /tmp/cookies.txt
unzip flujo_experimental_7.zip
pyhton3 split2.py --input flujo_experimental_7
python3 entrenamiento.py --input flujo_experimental_7

# ---- Flujo experimental 8 -----
wget --load-cookies /tmp/cookies.txt "https://drive.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://drive.google.com/uc?export=download&id=1EQr-1BJkOzQrezxGEMs8bnjQEyA6ouJb' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=1EQr-1BJkOzQrezxGEMs8bnjQEyA6ouJb" -O flujo_experimental_8.zip && rm -rf /tmp/cookies.txt
unzip flujo_experimental_8.zip
pyhton3 split2.py --input flujo_experimental_8
python3 entrenamiento.py --input flujo_experimental_8

# ---- Flujo experimental 9 -----
wget --load-cookies /tmp/cookies.txt "https://drive.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://drive.google.com/uc?export=download&id=1ZrKZzSSLXAqjFciHdLnVQujKiyQEE7ul' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=1ZrKZzSSLXAqjFciHdLnVQujKiyQEE7ul" -O flujo_experimental_9.zip && rm -rf /tmp/cookies.txt
unzip flujo_experimental_9.zip
pyhton3 split2.py --input flujo_experimental_9
python3 entrenamiento.py --input flujo_experimental_9

# ---- Flujo experimental 10 -----
wget --load-cookies /tmp/cookies.txt "https://drive.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://drive.google.com/uc?export=download&id=1_MQ2DxkWKO5fZmBc61E6YitaEMDN8ryk' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=1_MQ2DxkWKO5fZmBc61E6YitaEMDN8ryk" -O flujo_experimental_10.zip && rm -rf /tmp/cookies.txt
unzip flujo_experimental_10.zip
pyhton3 split2.py --input flujo_experimental_10
python3 entrenamiento.py --input flujo_experimental_10

```

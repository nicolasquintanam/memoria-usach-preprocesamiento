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
mkdir abstract

# ---- Flujo base -----
wget --load-cookies /tmp/cookies.txt "https://drive.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://drive.google.com/uc?export=download&id=10WzxojnH1CxRC_vHCQt0fUV3TgiZIaLQ' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=10WzxojnH1CxRC_vHCQt0fUV3TgiZIaLQ" -O flujo_base.zip && rm -rf /tmp/cookies.txt
unzip flujo_base.zip
mkdir flujo_base
mv flujo_base_* flujo_base
python3 split.py --input flujo_base
python3 entrenamiento.py --input flujo_base
rm -r flujo_base
rm flujo_base.zip

# ---- Flujo experimental 1 -----
wget --load-cookies /tmp/cookies.txt "https://drive.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://drive.google.com/uc?export=download&id=1C_QUG6RpYTTM0scoQvF45v8PrNyZk_b2' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=1C_QUG6RpYTTM0scoQvF45v8PrNyZk_b2" -O flujo_experimental_1.zip && rm -rf /tmp/cookies.txt
unzip flujo_experimental_1.zip
mkdir flujo_experimental_1
mv flujo_experimental_1_* flujo_experimental_1
python3 split.py --input flujo_experimental_1
python3 entrenamiento.py --input flujo_experimental_1
rm -r flujo_experimental_1
rm flujo_experimental_1.zip

# ---- Flujo experimental 2 -----
wget --load-cookies /tmp/cookies.txt "https://drive.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://drive.google.com/uc?export=download&id=14APS8v7_Rsh0n33i6FDE4JOVAxSTnew7' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=14APS8v7_Rsh0n33i6FDE4JOVAxSTnew7" -O flujo_experimental_2.zip && rm -rf /tmp/cookies.txt
unzip flujo_experimental_2.zip
mkdir flujo_experimental_2
mv flujo_experimental_2_* flujo_experimental_2
python3 split.py --input flujo_experimental_2
python3 entrenamiento.py --input flujo_experimental_2
rm -r flujo_experimental_2
rm flujo_experimental_2.zip

# ---- Flujo experimental 3 -----
wget --load-cookies /tmp/cookies.txt "https://drive.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://drive.google.com/uc?export=download&id=1dkZCkRUpqN6J8E80YNxV9Rew7uHdjCv9' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=1dkZCkRUpqN6J8E80YNxV9Rew7uHdjCv9" -O flujo_experimental_3.zip && rm -rf /tmp/cookies.txt
unzip flujo_experimental_3.zip
mkdir flujo_experimental_3
mv flujo_experimental_3_* flujo_experimental_3
python3 split.py --input flujo_experimental_3
python3 entrenamiento.py --input flujo_experimental_3
rm -r flujo_experimental_3
rm flujo_experimental_3.zip

# ---- Flujo experimental 4 -----
wget --load-cookies /tmp/cookies.txt "https://drive.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://drive.google.com/uc?export=download&id=1iQlrkUpnjX-kXnLtOfijuamN3VrdPaT3' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=1iQlrkUpnjX-kXnLtOfijuamN3VrdPaT3" -O flujo_experimental_4.zip && rm -rf /tmp/cookies.txt
unzip flujo_experimental_4.zip
mkdir flujo_experimental_4
mv flujo_experimental_4_* flujo_experimental_4
python3 split.py --input flujo_experimental_4
python3 entrenamiento.py --input flujo_experimental_4
rm -r flujo_experimental_4
rm flujo_experimental_4.zip

# ---- Flujo experimental 5 -----
wget --load-cookies /tmp/cookies.txt "https://drive.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://drive.google.com/uc?export=download&id=1OY3AucIPOpUlFjcZ5m-xuhmcijgG0rza' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=1OY3AucIPOpUlFjcZ5m-xuhmcijgG0rza" -O flujo_experimental_5.zip && rm -rf /tmp/cookies.txt
unzip flujo_experimental_5.zip
mkdir flujo_experimental_5
mv flujo_experimental_5_* flujo_experimental_5
python3 split.py --input flujo_experimental_5
python3 entrenamiento.py --input flujo_experimental_5
rm -r flujo_experimental_5
rm flujo_experimental_5.zip

# ---- Flujo experimental 6 -----
wget --load-cookies /tmp/cookies.txt "https://drive.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://drive.google.com/uc?export=download&id=1OjPPi_VGm72OpfrqCPDQUyOBajbE_Ymo' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=1OjPPi_VGm72OpfrqCPDQUyOBajbE_Ymo" -O flujo_experimental_6.zip && rm -rf /tmp/cookies.txt
unzip flujo_experimental_6.zip
mkdir flujo_experimental_6
mv flujo_experimental_6_* flujo_experimental_6
python3 split.py --input flujo_experimental_6
python3 entrenamiento.py --input flujo_experimental_6
rm -r flujo_experimental_6
rm flujo_experimental_6.zip

# ---- Flujo experimental 7 -----
wget --load-cookies /tmp/cookies.txt "https://drive.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://drive.google.com/uc?export=download&id=1oEn8DvCJcjXrWLwTA7SQicxq_B071XHg' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=1oEn8DvCJcjXrWLwTA7SQicxq_B071XHg" -O flujo_experimental_7.zip && rm -rf /tmp/cookies.txt
unzip flujo_experimental_7.zip
mkdir flujo_experimental_7
mv flujo_experimental_7_* flujo_experimental_7
python3 split.py --input flujo_experimental_7
python3 entrenamiento.py --input flujo_experimental_7
rm -r flujo_experimental_7
rm flujo_experimental_7.zip

# ---- Flujo experimental 8 -----
wget --load-cookies /tmp/cookies.txt "https://drive.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://drive.google.com/uc?export=download&id=1EQr-1BJkOzQrezxGEMs8bnjQEyA6ouJb' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=1EQr-1BJkOzQrezxGEMs8bnjQEyA6ouJb" -O flujo_experimental_8.zip && rm -rf /tmp/cookies.txt
unzip flujo_experimental_8.zip
mkdir flujo_experimental_8
mv flujo_experimental_8_* flujo_experimental_8
python3 split.py --input flujo_experimental_8
python3 entrenamiento.py --input flujo_experimental_8
rm -r flujo_experimental_8
rm flujo_experimental_8.zip

# ---- Flujo experimental 9 -----
wget --load-cookies /tmp/cookies.txt "https://drive.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://drive.google.com/uc?export=download&id=1ZrKZzSSLXAqjFciHdLnVQujKiyQEE7ul' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=1ZrKZzSSLXAqjFciHdLnVQujKiyQEE7ul" -O flujo_experimental_9.zip && rm -rf /tmp/cookies.txt
unzip flujo_experimental_9.zip
mkdir flujo_experimental_9
mv flujo_experimental_9_* flujo_experimental_9
python3 split.py --input flujo_experimental_9
python3 entrenamiento.py --input flujo_experimental_9
rm -r flujo_experimental_9
rm flujo_experimental_9.zip

# ---- Flujo experimental 10 -----
wget --load-cookies /tmp/cookies.txt "https://drive.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://drive.google.com/uc?export=download&id=1_MQ2DxkWKO5fZmBc61E6YitaEMDN8ryk' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=1_MQ2DxkWKO5fZmBc61E6YitaEMDN8ryk" -O flujo_experimental_10.zip && rm -rf /tmp/cookies.txt
unzip flujo_experimental_10.zip
mkdir flujo_experimental_10
mv flujo_experimental_10_* flujo_experimental_10
python3 split.py --input flujo_experimental_10
python3 entrenamiento.py --input flujo_experimental_10
rm -r flujo_experimental_10
rm flujo_experimental_10.zip

```

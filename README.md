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
wget --load-cookies /tmp/cookies.txt "https://drive.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://drive.google.com/uc?export=download&id=1eOAW08rCSIv-iQKpSCy5_E2xruieCKvO' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=1eOAW08rCSIv-iQKpSCy5_E2xruieCKvO" -O flujo-base.zip && rm -rf /tmp/cookies.txt
unzip flujo-base.zip
pyhton3 split2.py --input flujo_base
python3 entrenamiento.py --input flujo_base

```

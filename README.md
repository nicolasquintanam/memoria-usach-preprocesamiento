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
pyhton3 split2.py
python3 entrenamiento.py

```
from requestutil import *
import logging
from fastai.core import *


## Common Data Util methods

def downloaderV1(url, fname=None, folder=None):
    """
    Retirve the url content & save into file name {fname}
    """
    if not fname:
        fname = url.split("/")[-1]
    resp = GetRaw(url)
    try:
        if folder: 
            p = Path(folder); p.mkdir(exist_ok=True)
            if not str(folder).endswith("/"):
                folder = folder + "/"
            fname = folder + fname
        with open(fname, 'wb') as f: f.write(resp.content)
    except Exception as e:
        print("something went wrong while writing.")
        print(e)
        
def plotword_cloud(word_dict, figsz=(10,5)):
    """
    Plot wordcloud:
    Inputs: filename | list | frequency_dict
    """
    if isinstance(word_dict, dict):
        pass
    elif isinstance(word_dict, list):
        word_dict = Counter(data)
    elif isinstance(word_dict, str):
        fname = word_dict
        with open(fname) as f:
            data = f.read().split()
            word_dict = Counter(data)
    else:
        raise Exception("expected dict")
    wc = WordCloud()
    wc_img = wc.generate_from_frequencies(word_dict)
    plt.figure(figsize=figsz)
    plt.imshow(wc_img, interpolation="bilinear")
    plt.axis('off')
    plt.show()
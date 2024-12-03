import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

from controller.nlp_tools.smith_waterman import smith_waterman

def simulacaoSmithWaterman():
    # magalu = ['Abaixo de 8GB','8GB','16GB','32GB','64GB','128GB','256GB','1TB']
    
    # amazon = ['Até 3,9 GB','4 GB','8 GB','16 GB','32 GB','64 GB','128 GB','256 GB','512 GB ou mais']
    
    # amazon =  ['Abaixo de 8GB','8GB','16GB','32GB','64GB','128GB','256GB','1TB']
    
    # mercadolivre = ["Menos de 5,5", "5,5 a 6,1", "6,2 a 6,43", "6,53 a 6,6", "6,7 ou mais"] 
    
    # magalu = ["Abaixo de 5", "5 a 5.9", "6 a 6.9", "7 a 7.9", "8 a 8.9", "Acima de 10"]
    
      
    # # resultado = smith_waterman(amazon, magalu, match=-10, mismatch=-1, gap=20)
    
        
    # resultado = smith_waterman(mercadolivre, magalu)
    
    
    
    amazon = [
        "Motorola",
        "SAMSUNG",
        "Xiaomi",
        "Apple",
        "Multilaser",
        "realme",
        "Positivo",
        "Infinix",
        "Nokia",
        "Poco",
        "Redmi",
        "Geonav",
        "Gshield",
        "I2GO",
        "NO2PROBLEMS",
        "intelbras",
        "JBL",
        "Basike",
        "ONYK",
        "Danet",
        "Coibeu",
        "CASETiFY",
        "LAGUS IMP.",
        "ULANZI",
        "NANU SHOP",
        "Utilibrox",
        "GameSir",
        "Verbatim",
        "Ipega",
        "Baseus",
        "Zhiyun",
        "Hmaston",
        "Dpofirs",
        "COMP",
        "PROELETRONIC",
        "GTI Expressa",
        "Logitech",
        "hohem",
        "Legado Engenharia",
        "ELG"
    ]
    
    magalu = [
    "AGM",
    "Alcatel",
    "Apple",
    "Asus",
    "BlackBerry",
    "BLU",
    "Doogee",
    "Gradiente",
    "Honor",
    "Hotwav",
    "Huawei",
    "Infinix",
    "Lenovo",
    "Lenoxx",
    "LG",
    "Microsoft",
    "Motorola",
    "Multi",
    "Multilaser",
    "Nokia",
    "Nubia",
    "Philco",
    "POCO",
    "Positivo",
    "Realme",
    "Red Mobile",
    "Redmagic",
    "Redmi",
    "Samsung",
    "Samsung",
    "Samsung",
    "Semp",
    "Siemens",
    "Sony",
    "Sony Ericsson",
    "TCL",
    "Tecno",
    "Tectoy",
    "Xiaomi",
    "ZTE"
]

    
    resultado = smith_waterman(amazon, magalu, match=1, mismatch=0, gap=-1)
    
    print(resultado)
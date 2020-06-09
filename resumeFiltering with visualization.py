import PyPDF2
from os import listdir
from os.path import isfile, join
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import docx

path = "/home/prajith_v/Documents/new"

folder = listdir(path)
fin_dict = {"budgeting":2,
"cash":1,
"financial":2,
"finance":3,
"gaap":2,
"ledger":1,
"reconciliations":1,
"reconciling":1, 
"tax":2,
"filing":1,
"economize":1,
"economics":2,
"forecasting":1,
"prioritization":1,
"fiscal":1,
"strategic":1,
"strategy":1,
"valuations":1,
"hyperion":1,
"mba":2,
"sales":1,
"taxation":1,
"marketing":1,
"investment":2,
"stock":2,
"commerce":2,
"accounting":1,
"ifrs":1}

cs_dict = {"python":2,
"mysql":1,
"developer":1,
"android":1,
"app":1,
"docker":1,
"google":1,
"tensorflow":2,
"datascience":2,
"flutter":2,
"visualization":1,
"javascript":2,
"js":2,
"java":2,
"nodejs":2,
"ui":1,
"linux":1,
"opensource":1,
"ml":2,
"ai":2,
"server":1,
"backend":1,
"frontend":1,
"recognition":1,
"detection":1,
"ar":1,
"neural":2,
"vr":2,
"jsp":1,
"servlet":1,
"springboot":1,
"spring":2,
"html":2,
"css":2,
"bootstrap":2,
"kotlin":2,
"swift":2,
"golang":2,
"algorithm":1,
"datastructures":1,
"computer":1,
"vision":1,
"nlp":2,
"unsupervised":2,
"supervised":2,
"networking":1,
"devops":2,
"mlops":2,
"jenkins":1,
"ansible":1,
"github":2,
"git":2,
"bigdata":2,
"spark":2,
"apache":1,
"hive":2,
"hadoop":2,
"adobe":2,
"scala":1,
"c":1,
"r":2,
"agile":1,
"flask":2,
"django":2,
"php":2,
"gsoc":1,
"gcp":2,
"azure":2,
"aws":2
}

eee_dict = {"plc":1,
"analog":1,
"electrical":2,
"electronics":1,
"pcb":1,
"gen":1,
"cad":1,
"circuit":1,
"motor":1,
"ieee":1,
"hmi":1,
"hardware":1,
"micro":1,
"processor":1,
"microprocessor":1,
"signal":1,
"firmware":1,
"robot":1,
"matlab":1,
"raspberry":2,
"mems":1,
"soldering":1,
"etching":1,
"mcb":1,
"semiconductors":1,
"pcc":1,
"mcc":1,
"power":1,
"iot":1,
"wiring":1,
"embedded":2,
"microcontroller":1,
"arduino":1}

mech_dict = {"mathcad":2,
"matlab":1,
"mechanicalc":2,
"cad":2,
"fea":2,
"vba":1,
"crank":1,
"cylinder":1,
"dynamics":2,
"elasticity":1,
"elongation":1,
"engine":2,
"entropy":2,
"thermodynamics":1,
"friction":1,
"fulcrum":1,
"gear":1,
"grinder":1,
"hydraulics":1,
"combustion":1,
"kinetic":1,
"lathe":1,
"lever":1,
"machine":1,
"machinery":1,
"milling":1,
"piston":2,
"sprocket":1,
"mechanical":3,
"heat":1,
"mechanics":2,
"pressure":1,
"fluid":1,
"drawing":1,
"molding":2,
"sheeting":2,
"welding":2,
"mold":2,
"cooling":1,
"motors":1,
"conveyer":1,
"drawings":1
}

chm_dict = {"chemical":2,
"chemists":2,
"reaction":1,
"drugs":2,
"acid":1,
"base":1,
"icheme":2,
"polymers":1,
"chemistry":2,
"chemcad":2,
"comsol":2,
"aspen":2,
"hysys":2,
"ansys":2,
"distillation":1,
"reactor":1,
"fluid":1,
"corrosion":1,
"oxidation":1,
"pollution":1,
"compounds":1,
"sustainibility":1,
"pharmaceuticals":2,
"pharmaceutical":2,
"petrochemicals":2,
"petrochemical":2,
"microelectronics":2,
"microelectronic":2,
"pressure":1,
"cooling":1}

financial = ["budgeting cash financial finance gaap ledger reconciliations reconciling tax filing economize economics forecasting prioritization fiscal strategic strategy valuations hyperion mba sales taxation marketing investment stock commerce accounting ifrs"]

computsci = ["python mysql developer android app docker google tensorflow datascience flutter visualization javascript js java nodejs ui linux opensource ml ai server backend frontend recognition detection ar neural vr jsp servlet springboot spring html css bootstrap kotlin swift go algorithm datastructures computer vision nlp unsupervised supervised networking devops mlops jenkins ansible github git bigdata spark apache hive hadoop adobe scala c r agile flask django php gsoc gcp azure aws"]

chemist = ["chemical chemists reaction drugs acid base icheme polymers chemistry chemcad comsol aspen hysys ansys distillation reactor fluid corrosion oxidation pollution compounds sustainibility pharmaceuticals pharmaceutical petrochemicals petrochemical microelectronics microelectronic pressure cooling"]

eee = ["plc analog electrical electronics pcb gen cad circuit motor ieee hmi hardware micro processor microprocessor signal firmware robot matlab raspberry mems soldering etching mcb semiconductors pcc mcc power iot wiring embedded microcontroller arduino"]

mech = ["mathcad matlab mechanicalc cad fea vba crank cylinder dynamics elasticity elongation engine entropy thermodynamics friction fulcrum gear grinder hydraulics combustion kinetic lathe lever machine machinery milling piston sprocket mechanical heat mechanics pressure fluid drawing molding sheeting welding mold cooling motors conveyer drawings"]


def read_pdf(file_name):
    tokenizer = Tokenizer()
    fr_obj = PyPDF2.PdfFileReader(file_name)
    pages = fr_obj.numPages
    s=""
    count=0
    while count<=pages-1:

        page =fr_obj.getPage(count)
        s=s+page.extractText()
        count+=1  
    #word_index = tokenizer.fit_on_texts([s])
    return s
    
def read_docx(file_name):
    file = docx.Document(file_name)
    s =""
    for para in file.paragraphs:
        s= s+para.text
    print("docx")
    return s
    
def predict(f,c,e,m,cs):
    labels = ["finance","E&E","CS","mech","chemical"]
    values = [f,e,cs,m,c]
    colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
    plt.pie(values,labels=labels,colors=colors)
    plt.show()
    x = (f+e+cs+m+c)
    li = [f/x,e/x,cs/x,m/x,c/x]
    if max(li)<0.3:
        return 0
    else:
        return 1
    

tokenizer = Tokenizer()
tokenizer.fit_on_texts(financial)
k = tokenizer.word_index
lis_fin = []
for i in k:
    lis_fin.append(i)
tokenizer = Tokenizer()
tokenizer.fit_on_texts(computsci)
k = tokenizer.word_index
lis_cs = []
for i in k:
    lis_cs.append(i)
tokenizer = Tokenizer()
tokenizer.fit_on_texts(eee)
k = tokenizer.word_index
lis_eee = []
for i in k:
    lis_eee.append(i)
tokenizer = Tokenizer()
tokenizer.fit_on_texts(mech)
k = tokenizer.word_index
lis_mech = []
for i in k:
    lis_mech.append(i)
tokenizer = Tokenizer()
tokenizer.fit_on_texts(chemist)
k = tokenizer.word_index
lis_chm = []
for i in k:
    lis_chm.append(i)
    
def calc_score(l,s):
    if s=="f":
        score=0
        for i in l[0]:
            score = score + fin_dict[lis_fin[i-1]]
        return score
    elif s=="cs":
        score=0
        for i in l[0]:
            score = score + cs_dict[lis_cs[i-1]]
        return score
    elif s=="ch":
        score=0
        for i in l[0]:
            score = score + chm_dict[lis_chm[i-1]]
        return score
    elif s=="me":
        score=0
        for i in l[0]:
            score = score + mech_dict[lis_mech[i-1]]
        return score
    elif s=="e":
        score=0
        for i in l[0]:
            score = score + eee_dict[lis_eee[i-1]]
        return score

tokenizer = Tokenizer()
for files in folder:
    folder1 = listdir(path+'/'+files)
    f=cs=c=e=m=0
    for res in folder1:

        print((join(path,join(files,res))))
        if res[-3:]=="pdf":
            s = read_pdf(join(path,join(files,res)))
        elif res[-4:]=="docx":
            s = read_docx(join(path,join(files,res)))
        
        ##for financial
        tokenizer = Tokenizer()
        tokenizer.fit_on_texts(financial)
        l = tokenizer.texts_to_sequences([s])
        f = calc_score(l,"f")
        print(str(f)+": finance")

        #print("finance",m)
        #print()
        
        ##for chemists
        tokenizer = Tokenizer()
        tokenizer.fit_on_texts(chemist)
        l= tokenizer.texts_to_sequences([s])
        c = calc_score(l,"ch")
        print(str(c)+": chem")
        #print("chem","  ", l)
        
        ##for eee
        tokenizer = Tokenizer()
        tokenizer.fit_on_texts(eee)
        l= tokenizer.texts_to_sequences([s])
        e =calc_score(l,"e")
        print(str(e)+": eee")
        #print("eee","  ", l)
        
        ##for mech
        tokenizer = Tokenizer()
        tokenizer.fit_on_texts(mech)
        l= tokenizer.texts_to_sequences([s])
        m=calc_score(l,"me")
        print(str(m)+": mech")
        
         ##for cs
        tokenizer = Tokenizer()
        tokenizer.fit_on_texts(computsci)
        l= tokenizer.texts_to_sequences([s])
        cs =calc_score(l,"cs")
        print(str(cs)+": cs")
        
        ##now predicting the section
        x = predict(f,c,e,m,cs)
        if x==0:
            print("there is no clear difference between two or more categories")
        
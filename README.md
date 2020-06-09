# resume_filtering_jss Team JSS (PEC hackathon)
Problem statement :

    To develop a resume filter  that can categorise a resume out of different domains.
   
Domains are:
    Finance , Electrical and Electronics ,Computer science , Mechanical ,Chemical.

## Tools and libraries used

python

PyPDF2

docx

NLP techniques

Tensorflow API

## Approach

Firstly, we collected the datasets with respect to skills.
We assigned the values to the skills in priority. So, that we can get accurate solution.
 Then we started with extracting text from pdf and .docx document.
We used keras api for text cleaning.
We then started with pharse matching to see , how many values are repeating in our created resume.
We calculated the score for each domain for each pdf/docx present in that folder
The highest scored term will be the domain of that resume.


## To run this code on your PC

step 0:  Install all the libraries required(mentioned above)


step 1 : Download the code(resume_fil_final_updated.py)

step 2:  open the code and modify the variable 'path' with your folder path ,containing the resumes.

step 3: Run the modified code to get the results of each file.

## challenges faced
As we all know that  collecting data is the major challenge and after collecting it , how to process it becomes another challenge. So, that caused us the major  time.

Relative scoring was the major concern in our model, as we focussed to get greater accuracy.

 we had some system issues.
We actually have ideas with implementing  this more accurately but lack of computing and internet was a bane and also had shortage of time.(w.r.t hackathon)


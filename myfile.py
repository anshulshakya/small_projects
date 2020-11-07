'''import os
os.chdir('/home/anshul/Videos/Python')
#print(os.getcwd())
for f in os.listdir():
    #print(f)
    f_name, f_ext = os.path.splitext(f)
    f_title, f_title1, f_num= f_name.split('-')
    
    f_num= f_num.strip()[16:18].zfill(2)
    f_title= f_title.strip()
    f_title= f_title1.strip() 
    f_ext= f_ext.strip()
    
    print('{}-{}-{}{}'.format(f_num, f_title, f_title1 ,f_ext))'''












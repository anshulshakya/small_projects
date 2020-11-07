import os

'''giving the path of current working directory where we are going to rename the files'''
os.chdir('/home/anshul/Videos/Python')
#print(os.getcwd())

''' iterate over the files'''
for f in os.listdir('/home/anshul/Videos/Python'):
    #print(f)

    '''split the file name and extension'''
    f_name, f_ext = os.path.splitext(f)

    '''split '-' separated string'''
    f_title, f_title1, f_num= f_name.split('-')


    '''strip() method to avoid unwanted spaces in naming'''
    f_num= f_num.strip()[16:18].zfill(2)
    f_title= f_title.strip()
    f_title= f_title1.strip() 
    f_ext= f_ext.strip()
    

    print('{}-{}-{}{}'.format(f_num, f_title, f_title1 ,f_ext))
    
    
    '''rename the files at the specified location'''
    #os.rename(f, '{}-{}-{}{}'.format(f_num, f_title, f_title1 ,f_ext))












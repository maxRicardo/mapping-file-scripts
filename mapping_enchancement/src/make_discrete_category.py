#!usr/bin/python2.7


#================================================
__author__ =  "Max R. Berrios"
__date__= "Jan 10, 2014"
__email__ = "max.berrios@upr.edu"
__version__= "0.1"
#================================================


#script to add field to mapping file

from qiime.parse import parse_mapping_file as pmf



#======================= range function 
 #the field to be "range-to" should be of numeric type
    
def make_category_range(mapping_fp,category):
    #parsing the map 
    mapp,head,comm = pmf(open(mapping_fp,"U"))

    #determine the position of the category

    try:
        category_position = head.index(category)
    except ValueError:
        raise Exception(" Category not in mapping file!")
    
    #creating numeric range:
    
    category_field = []
    
    for value in mapp:
        category_field.apppend(value)
        
    gama_value = (max(category_field) - min(category_field))/4 
    #4 is the number of quantile at 25% , this should be an option soon !
    
    #Calculate the position in range:
    new_cat_list = map(lambda x: int(4.*((float(x) - max(category_field))/(max(category_field)-min(category_field)))),category_field)
    
    #writing to doc
    
    doc = open(category+".txt","w")
    count = 0
    
    for line in new_cat_list:
        if count == 0:
            doc.write(category+"TO_DESCRETE,")
            flag = False
        elif count < len(new_cat_list):
            doc.write(line+",")
        else:
            doc.write(line)
            
    doc.close()
        
        
     
    
    

    

    
    
     
        
    
        

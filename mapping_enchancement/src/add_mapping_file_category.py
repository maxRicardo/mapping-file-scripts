

#================================================
__author__ =  "Max R. Berrios"
__date__= "Jan 10, 2014"
__email__ = "max.berrios@upr.edu"
__version__= "0.1"
#================================================

#!usr/bin/python2.7


#scrip to add field to mapping file

from qiime.parse import parse_mapping_file as pmf
#from qiime.check_id_map import write_corrected_mapping as write_map



#==================== Script methods & Functions

def add_field_to_map(field_fp,mapping_fp):
    #still some test needed in term of the
    #logic to stop posible errors to be raise
    #through execution.
    
    #reading file with new column
    mapping_cat,category = parse_category_from_file(field_fp)
        
    # Reading and parsing the mapping file
    mapp,head,comm = pmf(open(mapping_fp,"U"))

    #adding field to headers

    temp = head.pop()
    head.append(category)
    head.append(temp)

    #adding field value in mapping

    for position in len(mapp):
        temp = mapp.pop()
        mapp.append(mapping_cat(position))
        mapp.append(temp)


    return mapp,head,comm

#convert the list from the cat file 
#to a mapping,head format like 

def parse_cat_from_list(cat_list):
    mapping = []
    head = None
    for value in cat_list:
        if head is None:
            head = value
        else :
            mapping.append()


#parse the category from a file 
#then return mapping and header for the cat
def parse_category_from_file(cat_fp):
    return parse_cat_from_list(list(open(cat_fp,"U")))





#=============================== Test

def test_parse_cat_from_list():
    pass

def test_add_field_to_map():
    pass


#============================= Main Method
def main():
    pass
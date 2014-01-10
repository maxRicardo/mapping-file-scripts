

#================================================
__author__ =  "Max R. Berrios"
__date__= "Jan 10, 2014"
__email__ = "max.berrios@upr.edu"
__version__= "0.1"
#================================================

#!usr/bin/python2.7


#scrip to add field to mapping file

from qiime.parse import parse_mapping_file as pmf
from qiime.check_id_map import write_corrected_mapping as write_map



#==================== adding field function

def add_field_to_map(field_fp,mapping_fp,separator=","):
    #still some test needed in term of the
    #logic to stop posible errors to be raise
    #through execution.
    
    #reading the column
    field_file = open(field_fp,"r")
    field_list = []
    field_head = None
    flag = True

    #parsing the new field into list
    for value in field_file.split(","):
        if flag:
            field_head = value
            flag = False
        else:
            field_list.append(value)
        
    # Reading and parsing the mapping file
    mapp,head,comm = pmf(open(mapping_fp,"U"))

    #adding field to headers

    temp = head.pop()
    head.append(field_head)
    head.append(temp)

    #adding field value in mapping

    for position in len(mapp):
        temp = mapp.pop()
        mapp.append(field_list(position))
        mapp.append(temp)

    #Writing the new file    
    output_fp = mapping_fp.split(".txt")+"_with_"+field_fp+".txt"
    write_map(output_fp,head,comm,mapp)
    #file should be out with the new field camp added

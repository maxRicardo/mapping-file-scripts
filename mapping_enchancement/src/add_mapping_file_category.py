

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
    
    if len(cat_list)< 2:
        raise Exception,"Trouble in paradise!"
    
    for value in cat_list:
        if head is None:
            head = value.rstrip()
        else :
            mapping.append(value.rstrip())
    return mapping,head

#parse the category from a file 
#then return mapping and header for the cat
def parse_category_from_file(cat_fp):
    if cat_fp is None:
        raise "Argument should not be NoneType"
    return parse_cat_from_list(list(open(cat_fp,"U")))





#=============================== Test

import unittest
class Test(unittest.TestCase):
    
    cat_fp = "test/cat_file.csv"
    print cat_fp
    
    cat_mapping,category_head = parse_category_from_file(cat_fp)
    
    
        
    def test_parse_cat_from_list(self):
        #contains test:
        self.assertIsNotNone(self.cat_mapping,"Category file seems to have no fields!")
        self.assertIsNotNone(self.category_head,"Field seems to have no header!")
        #Type verification
        self.assertTrue(type(self.cat_mapping)== list," Something weird with the format of the mapping")
        self.assertTrue(type(self.category_head)== str,"Something is quite odd with the header")
        
        test_list = ["cat","cow","sheep","crow","dog"]
        head_test  = "Animals" 
        
        self.assertEqual(head_test,self.category_head, "reading problems again")
        self.assertListEqual(test_list, self.cat_mapping, "None equal somethings wrong with the parsing")
        pass

    def test_add_field_to_map(self):
        pass


#============================= Main Method
def main():
    pass

if __name__ == "__main__":
    unittest.main()
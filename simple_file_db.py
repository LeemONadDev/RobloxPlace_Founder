import os
def get_float_value_from_db(filename):
    filename = "db\\"+filename
    f = open(filename,"r",encoding="utf-8")
    float_value_result = float(f.read())
    f.close()
    return float_value_result

def write_float_value_to_db(filename,value):
    filename = "db\\"+filename
    f = open(filename,"w",encoding="utf-8")
    f.write(str(value))
    f.close()

def create_db(filename):
    filename = "db\\"+filename
    f = open(filename,"x",encoding="utf-8")
    f.close()

def write_string_to_db(filename,string,end="\n"):
    filename = "db\\"+filename
    string = string + end
    f = open(filename,'a+',encoding="utf-8")
    f.write(string)
    f.close()

def change_string_in_db(filename,string):
    filename = "db\\"+filename
    f = open(filename,"w",encoding="utf-8")
    f.write(string)
    f.close()

def get_string_value_from_db(filename):
    filename = "db\\"+filename
    f = open(filename,"r",encoding="utf-8")
    string_value_result = f.read()
    f.close()
    return string_value_result

def make_db_dir(filename):
    filename = filename
    temp_command_data_tmp = "mkdir "+filename
    os.system(temp_command_data_tmp)
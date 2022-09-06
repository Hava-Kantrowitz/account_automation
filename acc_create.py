#!/usr/bin/env python3

import argparse
import pdfplumber
from PyPDF2 import PdfFileReader
import re 

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("file")
    args = parser.parse_args()
    file = args.file 
    return file

def process_company(page):
    comp = page.split("ORGANIZATION")[1]
    comp = comp.split("3.")[0]
    if "N/A" in comp: 
        return comp.split("N/A")[1]
    elif "n/a" in comp: 
        return comp.split("n/a")[1]
    else: 
        comp_list = comp.split(" ") 
        for x in [0, 1]:
            del comp_list[0]
        if len(comp_list[0]) == 1: 
            del comp_list[0] 
        return comp_list

def process_email(page): 
    email = page.split("GRADE/RANK")[1]
    email = email.split("7.")[0]
    email = email.split(" ")[0]
    return email

def process_name(page): 
    name = page.split("ACCOUNT CODE")[1]
    name = name.split("DOMAIN")[0]
    name = name.split(" ")[-1]
    return name

def process_app(page):
    app = page.split("Mission System:")[1]
    app = app.split("\n")[0]
    return app  

def process_env(page): 
    env = page.split("Environment:")[1]
    env = env.split("\n")[0]
    return env

def process_zone(page):
    zone = page.split("Zones:")[1]
    zone = zone.split("\n")[0]
    zone = zone.split(",")
    return zone 

def process_role(page): 
    role = page.split("Roles:")[1]
    role = role.split("\n")[0]
    return role 

def space_upper(text): 
    split= re.split('(?=[A-Z])', text)
    for val in split:  
        if len(val) == 0:
            split.remove(val) 
    upper_split = " ".join(split)
    return upper_split

def process_text(ex_text): 
    if type(ex_text) is list: 
        ex_text = "".join(ex_text)
    ex_text = ex_text.replace("\n", "") 
    if ex_text.startswith(" "):
        ex_text = ex_text[1:]
    return ex_text

def map_role(old_role): 
    if "Auditor" in old_role: 
        return "sa-auth" 
    elif "Functionl Tester" in old_role: 
        return "xacta" 
    elif "CCE" in old_role: 
        if "Privileged" in old_role: 
            return "sa-priv"
        elif "Authorized" in old_role:
            return "sa-auth"
    else: 
        if "Privileged" in old_role:
            return "priv" 
        elif "Authorized" in old_role: 
            return "auth" 
        else: 
            print("Error. Role " + old_role + " not recognized")
            exit(1) 


def process_pdf(file): 
    with pdfplumber.open(file) as pdf: 
        page_one = pdf.pages[0]
        page_one = page_one.extract_text()
        page_two = pdf.pages[1]
        page_two = page_two.extract_text()
        company = space_upper(process_text(process_company(page_one)))
        email = process_text(process_email(page_one))
        name = process_text(process_name(page_two)) 
        new_text = page_one.split("JUSTIFICATION FOR ACCESS")[1]
        new_text = new_text.split("TYPE OF ACCESS")[0]
        app = process_text(process_app(new_text))
        env = process_text(process_env(new_text))
        zones = process_zone(new_text)
        role = map_role(process_text(process_role(new_text)))
        return [name, email, company, app, role, env, zones] 

def pretty_print(file_vals): 
    info_dict = {}
    info_dict["Name"] = file_vals[0]
    info_dict["Email"] = file_vals[1]
    info_dict["Company"] = file_vals[2]
    info_dict["App"] = file_vals[3]
    info_dict["Access"] = file_vals[4]
    print(info_dict) 

#TO DO - do this properly with form field extraction instead of string parsing
# PDF itself is having CBC IV length issues which I am not in the mood to debug
# so string parsing it is for now 

def main(): 
    file = parse_args()
    file_vals = process_pdf(file)
    pretty_print(file_vals)


main()

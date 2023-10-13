import requests
from bs4 import BeautifulSoup
import json

def sorter(s):
    maxyear = 0
    for i in s:
        if "present" in i:
            return 3000
        year = int(i.split()[-1][:-1])
        if year>maxyear:
            maxyear = year
    return maxyear

html = requests.get("https://clubs.iiit.ac.in/clubs/hacking.club/members").content
soup = BeautifulSoup(html, "lxml")

scripts = soup.findAll("script")
members = []
for i in scripts:
    if "profile" in str(i.contents):
        dada = str(i.contents).split("self.__next_f.push([1,\"")[1]
        dada = dada.split("""\\\\n"])']""")[0].replace("\\\\", "")
        dada = dada.split(":", 1)[1]
        res = json.loads(dada)
        link = "https://clubs.iiit.ac.in" + res[3]["children"][3]["href"]
        name = res[3]["children"][3]["children"][1][3]["children"].title()
        roles = ""
        rolearray = res[3]["children"][3]["children"][3]
        for role in rolearray:
            role = role[3]["children"]
            roles += role[0][3]["children"] + " "
            for j in role[1][3]["children"]:
                roles += str(j)
            roles += "\n"
        roles = roles.splitlines()
        members.append([link, name, roles, sorter(roles)])
        # print(link, "\n", name,"\n", roles, sep="")

members.sort(key=lambda x: x[3], reverse=True)
print("""---
layout: page
permalink: /members
permalink_name: /members
title: Events
---

""")
print("# Current Members\n")
index = 0
for i in range(len(members)):
    member = members[i]
    if member[3] != 3000:
        index = i
        break
    print(f"- [{member[1]}]({member[0]})")
    for role in member[2]:
        print(f"\t- {role}")
    # print(member[0], "\n", member[1],"\n", member[2], sep="")
print("\n# Past Members")
curryear = members[index][3]
print("\n##", curryear, "\n")
for i in range(index, len(members)):
    member = members[i]
    if curryear != member[3]:
        curryear = member[3]
        print("\n##", curryear, "\n")
    print(f"- [{member[1]}]({member[0]})")
    for role in member[2]:
        print(f"\t- {role}")
    # print(member[0], "\n", member[1],"\n", member[2], sep="")
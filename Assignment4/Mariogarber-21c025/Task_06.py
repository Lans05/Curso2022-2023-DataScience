# -*- coding: utf-8 -*-
"""Copia de Task06.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MyNaKdsFHvDLGCBgNqGrfl6BkjpIYLdg

**Task 06: Modifying RDF(s)**
"""

github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2021-2022/master/Assignment4/course_materials"

"""Leemos el fichero RDF de la forma que lo hemos venido haciendo"""

from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS
g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
g.namespace_manager.bind('vcard', Namespace("http://www.w3.org/2001/vcard-rdf/3.0#"), override=False)
g.parse(github_storage+"/rdf/example5.rdf", format="xml")

"""Create a new class named Researcher"""

ns = Namespace("http://somewhere#")
g.add((ns.Researcher, RDF.type, RDFS.Class))
for s, p, o in g:
  print(s,p,o)

"""**TASK 6.1: Create a new class named "University"**

"""

# TO DO
g.add((ns.University, RDF.type, RDFS.Class))
# Visualize the results
for s, p, o in g:
  print(s,p,o)

"""**TASK 6.2: Add "Researcher" as a subclass of "Person"**"""

# TO DO
g.add((ns.Researcher, RDF.type, ns.Person))
# Visualize the results
for s, p, o in g:
  print(s,p,o)

"""**TASK 6.3: Create a new individual of Researcher named "Jane Smith"**"""

# TO DO
JaneURI=ns.JaneSmith

g.add((JaneURI, RDF.type, ns.Researcher))

# Visualize the results
for s, p, o in g:
  print(s,p,o)

"""**TASK 6.4: Add to the individual JaneSmith the fullName, given and family names**"""

# TO DO
VCARD = Namespace("http://www.w3.org/2001/vcard-rdf/3.0#")
fullName=Literal("Jane Smith")
g.add((JaneURI, VCARD.FN, fullName))
g.add((JaneURI, VCARD.Given, Literal("Jane")))
g.add((JaneURI, VCARD.Family, Literal("Smith")))
# Visualize the results
for s, p, o in g:
  print(s,p,o)

"""**TASK 6.5: Add UPM as the university where John Smith works**"""

# TO DO
LinkedData=Namespace("http://www.exampleLinkedData.com/ontology/")
UPMURI=ns.UPM
g.add((UPMURI, RDF.type, ns.University))
g.add((ns.JohnSmith, LinkedData.worksAt, ns.UPM))
# Visualize the results
for s, p, o in g:
  print(s,p,o)

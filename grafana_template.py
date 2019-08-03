#!/usr/bin/python
import os
from jinja2 import Environment, FileSystemLoader
title = os.environ['title']
namespace = os.environ['namespace']
alert = os.environ['alert']
print(title)
print(namespace)
#title = raw_input("Enter title: ")
#namespace = raw_input("Enter namespace: ")

file_loader = FileSystemLoader('template')
env = Environment(loader=file_loader)

template = env.get_template('main.txt.j2')


output = template.render(title=title, namespace=namespace, alert=alert)
with open(title, 'w') as f:
	f.write(output)
#print(output)

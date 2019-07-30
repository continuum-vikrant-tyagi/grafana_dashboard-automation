#!/usr/bin/python

from jinja2 import Environment, FileSystemLoader
title = raw_input("Enter title: ")
namespace = raw_input("Enter namespace: ")

file_loader = FileSystemLoader('template')
env = Environment(loader=file_loader)

template = env.get_template('sample.txt.j2')


output = template.render(title=title, namespace=namespace)
with open(title, 'w') as f:
	f.write(output)
#print(output)

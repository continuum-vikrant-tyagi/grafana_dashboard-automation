#!/usr/bin/python
import os
from jinja2 import Environment, FileSystemLoader
title = os.environ['title']
namespace = os.environ['namespace']
consumergroup = os.environ['consumergroup']
topics = os.environ['topics']
memoryalert = os.environ['memoryalert']
cpualert = os.environ['cpualert']
cg_lagalert = os.environ['cg_lagalert']

print(title)
print(namespace)
print(consumergroup)
print(topics)


# file_loader = FileSystemLoader('template')
# env = Environment(loader=file_loader)

# template = env.get_template('main.txt.j2')


output = template.render(title=title, namespace=namespace, consumergroup=consumergroup, topics=topics, memoryalert=memoryalert, cpualert=cpualert, cg_lagalert=cg_lagalert)
# with open(title, 'w') as f:
# 	f.write(output)
print(output)

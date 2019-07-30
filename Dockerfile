FROM python:alpine AS dashboard-generator
RUN pip install grafanalib
RUN pip install jinja2
RUN apk add --no-cache bash

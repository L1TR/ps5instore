ARG STORES=["Sony","Walmart","Target","GameStop","BestBuy"]

FROM python:3

ADD src /

RUN pip install bs4
RUN pip install requests

ENTRYPOINT [ "python", "./runner.py" ]
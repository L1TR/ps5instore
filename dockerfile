FROM python:3

COPY src /src
COPY assets /assets

RUN pip install bs4
RUN pip install requests
RUN pip install tqdm
RUN pip install selenium
RUN pip install webdriverdownloader

ENV TELEGRAM_TOKEN=""
ENV TELEGRAM_CHATID=""
ENV BESTBUY_DEVKEY=""
ENV DEFAULT_RETURN_ON_FAULT=False
ENV STORES_TO_CHECK="0,1,2,3"

ENTRYPOINT [ "python", "src/runner.py" ]
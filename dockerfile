# base image
FROM python:3.8

# streamlit-specific commands
RUN mkdir -p /root/.streamlit
RUN bash -c 'echo -e "\
[general]\n\
email = \"\"\n\
" > /root/.streamlit/credentials.toml'
RUN bash -c 'echo -e "\
[server]\n\
enableCORS = false\n\
" > /root/.streamlit/config.toml'

# exposing default port for streamlit
EXPOSE 8501

COPY . ./

RUN pip install -r requirements.txt

WORKDIR /app

ENTRYPOINT [ "streamlit", "run" ]

CMD [ "main.py" ]
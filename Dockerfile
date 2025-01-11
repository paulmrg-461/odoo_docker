FROM odoo:16

USER root
RUN apt-get update && apt-get install -y \
    build-essential \
    libxml2-dev libxslt1-dev libldap2-dev libsasl2-dev \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Instalar psycopg2 (o psycopg2-binary) desde pip
RUN pip3 install psycopg2-binary

USER odoo
ENV ODOO_EXTRA_ARGS="-i base"

version: "3.7"

services:
  db:
    image: postgres:13
    container_name: odoo_db
    environment:
      - POSTGRES_DB=odoo
      - POSTGRES_USER=odoo
      - POSTGRES_PASSWORD=odoo
    volumes:
      - "D:\\dev_projects\\oddo_docker\\postgres_data:/var/lib/postgresql/data"
    restart: always

  odoo:
    # En vez de image: odoo:16, definimos build:
    build:
      context: .
      dockerfile: Dockerfile   # (Si se llama Dockerfile y está en la misma carpeta, no hace falta especificar)
    container_name: odoo_server
    depends_on:
      - db
    ports:
      - "8069:8069"
    environment:
      - DB_HOST=db
      - DB_PORT=5432
      - DB_USER=odoo
      - DB_PASSWORD=odoo
      - DB_NAME=odoo
      # ODOO_EXTRA_ARGS lo puedes poner en el Dockerfile o aquí:
      # - ODOO_EXTRA_ARGS=-i base
    volumes:
      - "D:\\dev_projects\\oddo_docker\\odoo_data:/var/lib/odoo"
    restart: always

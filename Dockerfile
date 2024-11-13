# Dockerfile
FROM odoo:18.0

LABEL maintainer="kevin@gmail.com"

# Instalar dependencias adicionales si son necesarias
USER root
RUN apt-get update && apt-get install -y \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Copia el archivo de configuración
COPY ./odoo.conf /etc/odoo/

# Crear directorio para addons personalizados
RUN mkdir -p /mnt/extra-addons && chown -R odoo:odoo /mnt/extra-addons

# Copiar los addons personalizados desde extra_addons
COPY --chown=odoo:odoo ./extra_addons /mnt/extra-addons

USER odoo

EXPOSE 8069 8071 8072
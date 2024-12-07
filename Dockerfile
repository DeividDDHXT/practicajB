FROM python:3.10-slim

# Establecer el directorio de trabajo
WORKDIR /monitoreo

# Copiar el código de la aplicación
COPY . .

# Instalar dependencias
RUN pip install -r requirements.txt

# Exponer el puerto de la aplicación Django
EXPOSE 8000

# Comando para ejecutar la aplicación Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

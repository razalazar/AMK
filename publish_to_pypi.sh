#!/bin/bash
# Script de publicación para evomem

# Detener el script si hay algún error
set -e

echo "==========================================="
echo "   PREPARANDO COMPILACIÓN DE EVOMEM        "
echo "==========================================="

# Asegurar que las herramientas de construcción e instalación estén actualizadas
echo "Instalando/Actualizando 'build' y 'twine'..."
python3 -m pip install --upgrade build twine

# Limpiar compilaciones anteriores para evitar conflictos
echo "Limpiando compilaciones anteriores (build/, dist/, *.egg-info)..."
rm -rf build/ dist/ *.egg-info

# Compilar el paquete (genera source distribution y wheel)
echo "Compilando el paquete evomem..."
python3 -m build

echo ""
echo "==========================================="
echo "   VERIFICANDO COMPILACIÓN CON TWINE       "
echo "==========================================="
# Verifica que la descripción y metadatos sean válidos para PyPI
python3 -m twine check dist/*

echo ""
echo "==========================================="
echo "   ¿DESEAS SUBIR EL PAQUETE A PyPI?        "
echo "==========================================="
echo "Esto subirá el paquete de forma permanente a pypi.org."
echo "Requiere que tengas una cuenta en PyPI."
echo ""
read -p "¿Deseas subir el paquete ahora? (s/N): " -r respuesta

if [[ "$respuesta" =~ ^[Ss]$ ]]; then
    echo "Subiendo a PyPI mediante twine..."
    python3 -m twine upload dist/*
    echo "¡Proceso terminado con éxito!"
else
    echo "Publicación cancelada. El paquete compilado está disponible localmente en la carpeta 'dist/'."
fi

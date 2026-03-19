# Forja Nova - Web de Estado

Pequeña web estática de una base de operaciones creativa.

## Archivos

- `index.html` : Página principal
- `styles.css`: Estilos visuales dark/tech
- `script.js` : Comportamiento mínimo (animación de status)

## Uso local

  1. Abrir `index.html` en un navegador.
  2. O usar un servidor local:
     - `python -m http.server 8080` y abrir `http://localhost:8080`

## Subir a GitHub

1. Iniciar repo (ya se creó localmente):
   `git init`
   `git add .`
   `git commit -m "Inicializar web Forja Nova"`

2. Crear repositorio remoto (en GitHub):
   - URL de ejemplo: `https://github.com/<tu_usuario>/forja-nova-web.git`
   - `git remote add origin https://github.com/<tu_usuario>/forja-nova-web.git`
   - `git push -u origin main`

Si quieres, colocamos un script `create_github_repo.py` y creamos remoto directamente con token.

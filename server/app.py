from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os

# Configurações básicas
app = Flask(__name__)

# Caminho base para a pasta de upload
# BASE_DIR = 'shared_data'
app.config['UPLOAD_FOLDER'] = os.getenv('UPLOAD_FOLDER', '/shared_data')

# verifica se o diretório de upload existe
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

# Função para listar arquivos e diretórios em um caminho dado
def list_files_in_directory(path):
    try:
        # Listar arquivos e diretórios
        items = os.listdir(path)
        files = []
        directories = []

        for item in items:
            full_path = os.path.join(path, item)
            if os.path.isdir(full_path):
                directories.append(item)
            else:
                files.append(item)

        return directories, files
    except FileNotFoundError:
        return [], []

# Página principal com navegação por diretórios
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    full_path = os.path.join(app.config['UPLOAD_FOLDER'], path)
    
    if not os.path.exists(full_path):
        return 'Diretório não encontrado.', 404

    # Listar diretórios e arquivos
    directories, files = list_files_in_directory(full_path)

    # Retorna a página com os arquivos e subdiretórios
    return render_template('index.html', directories=directories, files=files, current_path=path)

# Rota para download de arquivos
@app.route('/uploads/<path:path>/<filename>')
@app.route('/uploads/<filename>', defaults={'path': ''})
def download_file(path, filename):
    full_path = os.path.join(app.config['UPLOAD_FOLDER'], path)
    return send_from_directory(full_path, filename)

# Rota para deletar um arquivo

# Rota para fazer upload de arquivos
@app.route('/upload', methods=['POST'])
def upload_file():
    current_path = request.form.get('path', '')  # Captura o caminho atual do diretório
    if 'file' not in request.files:
        return 'Nenhum arquivo encontrado.'
    file = request.files['file']
    if file.filename == '':
        return 'Nenhum arquivo selecionado.'
    if file:
        # Caminho completo para salvar o arquivo no diretório atual
        upload_path = os.path.join(app.config['UPLOAD_FOLDER'], current_path)
        file.save(os.path.join(upload_path, file.filename))
        return redirect(url_for('index', path=current_path))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)

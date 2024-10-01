from flask import Flask, request, render_template
from lexer_parser.lexer import lexico
from lexer_parser.parser import sintactico  # Importar el parser

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    text = ''
    tokens = None
    line_info = None
    error_message = None
    sintactic_result = None
    sintactic_error = None

    if request.method == 'POST':
        text = request.form['text']
        try:
            # Llamamos al análisis léxico
            tokens, line_info = lexico(text)

            # Llamamos al análisis sintáctico
            sintactic_result, sintactic_error = sintactico(text)

        except Exception as e:
            error_message = str(e)

    # Renderizamos la plantilla con los datos
    return render_template('index.html', text=text, tokens=tokens, line_info=line_info,
                           sintactic_result=sintactic_result, sintactic_error=sintactic_error, error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True)

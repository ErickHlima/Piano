from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QLabel,
    QTextEdit,
    QDoubleSpinBox,
    QPushButton
)
import time
import pyautogui
import subprocess

def front():
    app = QApplication([])

    window = QWidget()
    layout = QVBoxLayout(window)

    layout.addWidget(QLabel("Partitura"))
    partitura = QTextEdit()
    layout.addWidget(partitura)
    
    layout.addWidget(QLabel("Delay"))
    delay = QDoubleSpinBox()
    delay.setRange(0.01 , 5.0)
    delay.setSingleStep(0.01)
    delay.setValue(0.5)
    layout.addWidget(delay)

    botao = QPushButton("Iniciar")
    layout.addWidget(botao)

    result = {"musica": "", "intervalo": 0.5}

    def on_start():
        texto = partitura.toPlainText()
        # Normaliza espaços e quebras de linha para uma única linha
        musica = " ".join(texto.split())
        intervalo = float(delay.value())
        result["musica"] = musica
        result["intervalo"] = intervalo
        app.quit()

    botao.clicked.connect(on_start)

    window.show()
    app.exec()

    return result["musica"], result["intervalo"]

pyautogui.PAUSE = 0


CONTAGEM_REGRESSIVA = 5

# Teclas válidas (as mesmas do Virtual Piano)
TECLAS_VALIDAS = set(
    "1234567890qwertyuiopasdfghjklzxcvbnm"
    "!@#$%^&*()QWERTYUIOPASDFGHJKLZXCVBNM"
)


def tocar_token(token: str):
    # Pressiona uma nota isolada ou um acorde entre colchetes.
    token = token.strip()
    if not token:
        return

    if token.startswith("[") and token.endswith("]"):
        teclas = [c for c in token[1:-1] if c in TECLAS_VALIDAS]
    else:
        teclas = [c for c in token if c in TECLAS_VALIDAS]
    if not teclas:
        return

    if len(teclas) == 1:
        pyautogui.press(teclas[0])
    else:
        # Acorde: pressiona todas juntas, segura um instante, solta todas
        for tecla in teclas:
            pyautogui.keyDown(tecla)
        time.sleep(0.08)
        for tecla in teclas:
            pyautogui.keyUp(tecla)


def tocar_musica(musica: str, intervalo: float):
    eventos = 0
    i = 0
    tamanho = len(musica)

    while i < tamanho:
        caractere = musica[i]

        if caractere.isspace():
            while i < tamanho and musica[i].isspace():
                i += 1
            time.sleep(0.2)
            continue

        if caractere == "[":
            fim = musica.find("]", i + 1)
            if fim == -1:
                token = musica[i:]
                i = tamanho
            else:
                token = musica[i : fim + 1]
                i = fim + 1

            tocar_token(token)
            eventos += 1
            time.sleep(intervalo)
            continue

        tocar_token(caractere)
        eventos += 1
        i += 1
        time.sleep(intervalo)

    print(f"Vou tocar {eventos} notas/acordes...")


if __name__ == "__main__":
    MUSICA, INTERVALO = front()
    # Local do executavel do navegador
    subprocess.Popen([r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe","https://virtualpiano.net/"])

    for i in range(CONTAGEM_REGRESSIVA, 0, -1):
        print(f"Começando em {i}...")
        time.sleep(1)

    tocar_musica(MUSICA, INTERVALO)
    print("Fim da música!")

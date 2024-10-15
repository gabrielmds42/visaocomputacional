import cv2
from colorama import Fore, Back, Style, init

# Inicializa a biblioteca colorama
init(autoreset=True)

def load_image(image_path):
    # Carregar imagens em tons de cinza
    return cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

def resize_image(image, new_width=150):
    # Calcular a proporção entre a nova largura e a antiga e ajustar a altura de acordo
    ratio = new_width / image.shape[1]
    new_height = int(image.shape[0] * ratio)
    return cv2.resize(image, (new_width, new_height))

def get_color(pixel_value):
    # Definir cores com base no nível de cinza (0-255)
    if pixel_value < 64:
        return Fore.RED  # Cores escuras para pixels de baixa intensidade
    elif pixel_value < 128:
        return Fore.YELLOW  # Média intensidade
    elif pixel_value < 192:
        return Fore.GREEN  # Mais claro
    else:
        return Fore.WHITE  # Cor mais clara para os pixels mais brilhantes

def pixel_to_ascii(image):
    # Usar mais caracteres ASCII para mais nuances
    ascii_chars = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
    new_image = []
    for row in image:
        line = ""
        for pixel in row:
            # Obter o caractere ASCII correspondente
            char = ascii_chars[pixel // 4]
            # Adicionar a cor correspondente ao caractere
            colored_char = get_color(pixel) + char
            line += colored_char
        new_image.append(line)
    return "\n".join(new_image)

if __name__ == "__main__":
    image_path_ = input("Digite o caminho para o arquivo de imagem:")
    image_ = load_image(image_path_)
    if image_ is None:
        print("Erro ao carregar a imagem")
    else:
        image_ = resize_image(image_)
        ascii_art = pixel_to_ascii(image_)
        print(ascii_art)

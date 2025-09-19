# Importation de la biliathèque
from PIL import Image

# Ouverture de l'image
image = Image.open("projet1/linkdin.png")

# Redimensionnement de l'image
icone = image.resize((64, 64))

# Sauvegarde de l'icône
icone.save("projet1/linkdin_icone.ico")

# Affichage de l'icône
icone.show()
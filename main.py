import ctypes
import os
import time

WALLPAPER_FOLDER = r"C:\Users\nguye\OneDrive\Desktop\Hack Club stuff\President Wallpaper Rotator\presidents_pics" 
STATE_FILE = os.path.join(WALLPAPER_FOLDER, "wallpaper_index.txt")
VALID_EXTENSIONS = (".png", ".jpg", ".jpeg")

SPI_SETDESKWALLPAPER = 20 
SPIF_UPDATEINFILE = 0x01
SPIF_SENDWININICHANGE = 0x02
PRESIDENTS = ["georgewashington.png",
              "johnadams.png",
              "thomasjefferson.png",
              "jamesmadison.png",
              "jamesmonroe.png",
              "johnquincyadams.png",
              "andrewjackson.png",
              "martinvanburen.png",
              "williamhenryharrison.png",
              "johntyler.png",
              "jamesdpolk.png",
              "zacharytaylor.png",
              "millardfillmore.png",
              "franklinpierce.png",
              "jamesbuchanan.png",
              "abrahamlincoln.png",
              "andrewjohnson.png",
              "ulyssessgrant.png",
              "rutherfordbhayes.png",
              "jamesagarfield.png",
              "chesteraauthor.png",
              "grovercleveland.png",
              "benjaminharrison.png",
              "williammckinley.png",
              "theodoreroosevelt.png",
              "williamhowardtaft.png",
              "woodrowwilson.png",
              "warrengharding.png",
              "calvincoolidge.png",
              "herberthoover.png",
              "franklindroosevelt.png",
              "harrystruman.png",
              "dwightdeisenhower.png",
              "johnfkennedy.png",
              "lyndonbjohnson.png",
              "richardmnixon.png",
              "geraldrford.png",
              "jimmycarter.png",
              "ronaldreagan.png",
              "georgehwbush.png",
              "williamjclinton.png",
              "georgewbush.png",
              "barackobama.png",
              "donaldtrump.png",
              "josephrbidenjr.png",
]

def set_wallpaper(image_path):
    abs_path = os.path.abspath(image_path)
    ctypes.windll.user32.SystemParametersInfoW(
        SPI_SETDESKWALLPAPER,
        0,
        abs_path,
        SPIF_UPDATEINFILE | SPIF_SENDWININICHANGE
    )

def next_wallpaper():
    images = [
        os.path.join(WALLPAPER_FOLDER, f)
        for f in PRESIDENTS
        if os.path.exists(os.path.join(WALLPAPER_FOLDER, f))
    ]

    if not images:
        print ("No valid images found, check format maybeh...")
        return

    current_index = 0 
    if os.path.exists(STATE_FILE):
        with open (STATE_FILE, "r") as f:
            content = f.read().strip()
            if content.isdigit():
                current_index = int(content)

    if current_index >= len(images):
        current_index = 0

    selected_image = images[current_index]
    set_wallpaper(selected_image)
    print(f"Image set yay!! :3")

    next_index = (current_index + 1) % len(images)
    with open (STATE_FILE, "w") as f:
        f.write(str(next_index))

if __name__ == "__main__":
    next_wallpaper()
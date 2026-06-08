# Scrape wiki pages to extract reagent names and effects

import re
import time

import requests
from bs4 import BeautifulSoup as bs

# Source URLs:
urls = [
    "https://en.uesp.net/wiki/Lore:Alchemy_A",
    "https://en.uesp.net/wiki/Lore:Alchemy_B",
    "https://en.uesp.net/wiki/Lore:Alchemy_C",
    "https://en.uesp.net/wiki/Lore:Alchemy_D",
    "https://en.uesp.net/wiki/Lore:Alchemy_E",
    "https://en.uesp.net/wiki/Lore:Alchemy_F",
    "https://en.uesp.net/wiki/Lore:Alchemy_G",
    "https://en.uesp.net/wiki/Lore:Alchemy_H",
    "https://en.uesp.net/wiki/Lore:Alchemy_I",
    "https://en.uesp.net/wiki/Lore:Alchemy_J",
    "https://en.uesp.net/wiki/Lore:Alchemy_K",
    "https://en.uesp.net/wiki/Lore:Alchemy_L",
    "https://en.uesp.net/wiki/Lore:Alchemy_M",
    "https://en.uesp.net/wiki/Lore:Alchemy_N",
    "https://en.uesp.net/wiki/Lore:Alchemy_O",
    "https://en.uesp.net/wiki/Lore:Alchemy_P",
    "https://en.uesp.net/wiki/Lore:Alchemy_R",
    "https://en.uesp.net/wiki/Lore:Alchemy_S",
    "https://en.uesp.net/wiki/Lore:Alchemy_T",
    "https://en.uesp.net/wiki/Lore:Alchemy_U",
    "https://en.uesp.net/wiki/Lore:Alchemy_V",
    "https://en.uesp.net/wiki/Lore:Alchemy_W",
    "https://en.uesp.net/wiki/Lore:Alchemy_Y",
    "https://en.uesp.net/wiki/Lore:Alchemy_Z",
]

headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36"
    }

skip_headings = {"References", "See also", "External links"}  # Non-reagent headings to ignore
effect_classes = {"EffectNeg", "EffectPos", "EffectOther", "EffectMix"}  # Target classes to extract effects

for url in urls:
    r = requests.get(url, headers=headers)

    soup = bs(r.content, "html.parser")
    tags = soup.find_all(class_=re.compile("mw-headline|Effect(Neg|Pos|Other|Mix)"))  # Select headings and effect elements

    with open("data/01_parsed.txt", "a") as file:  # Open file in append mode for continuous writing
        for tag in tags:
            if "mw-headline" in tag["class"]:  # Filter reagent name headings
                reagent = tag.get_text().strip()
                if reagent in skip_headings:
                    continue
                print(reagent + " NAME")

                file.write(reagent + " NAME\n")  # Append 'NAME' to distinguish reagents from effects

                
                seen_effects = set()  # Track seen effects to avoid duplicates

                
            elif any(
                c in effect_classes for c in tag["class"]  # Identify effect elements
            ):
                effects = tag.get_text(separator="\n").strip()  # Separate text nodes
                for effect in effects.split("\n"):  # Split text nodes
                    effect = effect.strip()  # Retrieve single node (reagent / effect name)
                    if effect in seen_effects:
                        continue
                    else:
                        seen_effects.add(effect)
                        print("    " + effect)
                        file.write(
                            "    " + effect + "\n"  # Keep each effect on its own line
                        )

    time.sleep(1.2)  # Rate limiting between requests (respectful scraping practice)
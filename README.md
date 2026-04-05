### **The Elder Scrolls Alchemy Effects Parser**
A custom data-cleaning script created to process and unify alchemy reagent data scraped from the [Unofficial Elder Scrolls Pages](https://en.uesp.net/wiki/Lore:Alchemy_A), as part of a personal role-playing experience in The Elder Scrolls universe.

### **Features**
 * Scrapes all alchemy reagent pages from A–Z
 * Distinguishes reagent names from effect names
 * Normalizes effect names using a consistent naming scheme
 * Removes duplicates while maintaining the original order

The output is a cleaner, unified list of effects per reagent.

#### Example transformation:

##### Input (raw):
```text
Aloe Vera Leaves
    Heal Health
    Heal Health
    Restore Health
    Restore Health
    Restore Fatigue
    Restore Health
    Damage Magicka
    Invisibility
    Restore Health
    Restore Stamina
    Damage Magicka
    Invisibility
```
##### Output (cleaned):
```text
Aloe Vera Leaves
    Health Restoration
    Fatigue Restoration
    Magicka Damage
    Invisibility
    Stamina Restoration
```
## Motivation
Originally built for a richer and easier role-play experience for me and my friend. Together, we designed the naming convention for the alchemy related magical effects across all the games in the series. After that, I wrote the script to implement that.

The .txt file with the end result is added, so if you are, too, a member of TES role-play community and have interest in alchemy, feel free to use it!


## Disclaimer
This project is not actively maintained. The scripts were designed based on the UESP alchemy pages at the time of creation. New reagents or effects added to the website may not be captured or normalized correctly by the scripts.

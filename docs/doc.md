# Documentação

## Data Preparation

Data Source:  https://developer.riotgames.com/docs/lol#data-dragon -> https://ddragon.leagueoflegends.com/cdn/dragontail-11.22.1.tgz

Data Language: EN-US

Data Format: JSON

### Data subsets:
* Champions (stats, abilities, lore)

Fields:

type;key;name;title;skinsname;skinschromas;lore;allytips;enemytips;tags;partype;info(attack;defense;magic;dificulty);stats(hp;hpperlevel;mp;mpperlevel;movespeed;armor;armorperlevel;spellblock;spellblockperlevel;attackrange;hpregen;hpregenperlevel;mpregen;mpregenperlevel;crit;critperlevel;attackdamage;attackdamageperlevel;attackspeedperlevel;attackspeed);spells(id;name;description;tooltip;leveltip(label));passive(name;description);

* Items

Fields:

name;plaintext;gold(base;purchasable;total;sell;);tags;stats(includesmanystatmods);

### TODO

* Knowledge graphs extract relations
* UML -> Eleminar leveltip (dar colapse cm label)

### Pipeline

* Convert JSON to CSV

* Determine desired atributes

* Eliminate columns of undesired atributes

* Convert columns into rows using python scripts

* Add new atributes derived from others (TODO , stats at 11 and 18)



## Information Retrieval

## Search System

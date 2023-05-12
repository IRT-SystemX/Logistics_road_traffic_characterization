# Introduction
Dépôt ayant pour objectif de contenir l'ensemble des codes à mettre en open source lié au tracking de véhicules logistiques et issus du projet LEAD.

## Blocs fonctionnels 
Ces codes sont répartis en plusieurs blocs fonctionnels pouvant être exécutés séparément ou bien via un appel unique exécutant tout le pipeline de comptage de véhicules logistiques issus de flux caméras.

Ces blocs fonctionnels sont au nombre de quatre et comprennent :
    - Une partie d'anonymisation des données (issus d'un fork du dépot https://github.com/understand-ai/anonymizer) 
    - Une partie de tracking des différents véhicules (issus du dépot https://github.com/mikel-brostrom/Yolov5_StrongSORT_OSNet/tree/v5.0)
    - Une partie de classification des véhicules identifiés
    - Une partie de comtage et d'analyse des résultats.

# Anonymisation
Issus du dépot https://github.com/understand-ai/anonymizer, ce dépot contient les codes permettant d'anonymiser les plaques d'immatriculation et personnes se trouvant sur des images et vidéos.

# Tracking
Issus du dépot https://github.com/mikel-brostrom/Yolov5_StrongSORT_OSNet/tree/v5.0, ce dépot permet d'identifier chaque véhicule sur chaque frame d'une vidéo et d'assigner un id unique pour chaque véhicule. 

# Classification
Ce dépot permet de d'associer une classe à chaque véhicule identifier.

# Comptage 
Ce dépot permet l'analyse des résulats de la classification.

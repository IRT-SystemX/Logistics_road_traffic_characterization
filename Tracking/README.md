# logistic_vehicles_detection
## Introduction
Ce dépôt contient le code des expériences menées pour réaliser l'annotation des catégories de véhicules logistique.
Ces expérimentations sont basées sur les méthodes suivantes : 
1. Sélection d'imagettes de véhicules
    - Méthodes mobilisées : détection + suivi de véhicules
    - Sorties : 
        - Imagettes de tous les véhicules présents sur toutes les frames des vidéos avec un identifiant unique de véhicule
        - Dossiers : 
            - (DeepSORT) `echantillons_2021-03-21/yolov5l6_osnet_ibn_x1_0_MSMT172`
            - (DeepSORT - pour tous les SP-CAM) `campagne/SPxx-CAM-xx/anonymized/yolov5m_osnet_ibn_x1_0_MSMT17`
            - (StrongSORT - pour tous les SP-CAM) `campagne/SPxx-CAM-xx/anonymized/StrongSORT_yolov5l6_osnet_x0_25_msmt17`
            - (StrongSORT) `campagne/SP01-CAM-03/anonymized/StrongSORT_yolov5l6_osnet_ibn_x1_0_msmt17`
    - Code associé : 
        - Lancement des expériences : cf. section [Sélection d'images de véhicules](#sélection-dimages-de-véhicules)
        - Notebook d'analyse: [jupyter/paris2connect/annotation/1_crops_statistics.ipynb](jupyter/paris2connect/annotation/1_crops_statistics.ipynb)
2. Reduction de la redondance des imagettes de véhicules
    - Méthodes mobilisées : feature extraction (VGG16) + clustering (agglomerative - Ward)
    - Sorties : 
        - Imagettes de tous les véhicules dans des positions variées sur les vidéos avec un identifiant unique de véhicule
        - Dossiers : 
            - (Echantillons - Selection DeepSORT) : `echantillons_2021-03-21/yolov5l6_osnet_ibn_x1_0_MSMT172/tracking_selection_sc`
            - (Campagne - Selection DeepSORT) : `campagne/tracking_selection_sc/DeepSORT_yolov5m_osnet_ibn_x1_0_MSMT17`
            - (Campagne - Selection StrongSORT) : `campagne/tracking_selection_sc/StrongSORT_yolov5l6_osnet_x0_25_msmt17`
    - Code associé : [jupyter/paris2connect/annotation/2_crops_selection.ipynb](jupyter/paris2connect/annotation/2_crops_selection.ipynb)
3. Features Extraction à partir de modèles entrainés
    - Méthodes mobilisées : extraction des features sur une couche d'un réseau de neurone pré-entrainé (pytorch) sur ImageNet
    - Sorties : 
        - Matrices composées de features pour chaque image présentes dans les datasets issus de l'étape 2.
        - Dossier : `results/features/pretrained_models`
    - Code associé : 
        - Modèles pré-entrainés disponibles dans torchvision : [jupyter/paris2connect/annotation/3_feature_extraction__pytorch_models.ipynb](jupyter/paris2connect/annotation/3_feature_extraction__pytorch_models.ipynb)
        - Modèle SimMIM : [jupyter/paris2connect/annotation/3_feature_extraction__SimMIM.ipynb](jupyter/paris2connect/annotation/3_feature_extraction__SimMIM.ipynb)
        - Modèle MoBy - SWIN : [jupyter/paris2connect/annotation/3_feature_extraction__transformer_ssl.ipynb](jupyter/paris2connect/annotation/3_feature_extraction__transformer_ssl.ipynb)
4. Feature Learning sur le dataset Paris2Connect
- Méthodes mobilisées : Self-Supervised Learning pour l'entrainement de représentation via les approches MoCoV2 et MoBY + extraction de features
    - Sorties : 
        - Matrices composées de features pour chaque image présentes dans les datasets issus de l'étape 2.
        - Dossiers : 
            - MoCoV2 : Model in `moco224`, features in `embedding224`
                - (VGG16 backbone - ImageNet init) `results/spice/results/paris2connect/vgg16/imagenet_initialization`
                - (VGG16 backbone - random init) `results/spice/results/paris2connect/vgg16/random_initialization`
                - (ResNet18 backbone) `results/spice/results/paris2connect/true_resnet18`
            - MoBy : 
                - model in `results/transformer_ssl/moby__swin_tiny__patch4_window7_224__odpr02_tdpr0_cm099_ct02_queue4096_proj2_pred2/queue1152`
                - features exported in `results/features/pretrained_models`
    - Code associé : 
        - MoCov2 : Lancement de l'apprentissage du modèle + export des features : cf. section [Feature Learning MoCov2](#feature-learning-mocov2)
        - MoBY : 
            - Lancement de l'apprentissage de modèle : cf. section [Feature Learning MoBY](#feature-learning-moby)
            - Export des features : [jupyter/paris2connect/annotation/3_feature_extraction__transformer_ssl.ipynb](jupyter/paris2connect/annotation/3_feature_extraction__transformer_ssl.ipynb)
5. Clustering sur les différents dataset de features
    - Méthodes mobilisées : 
        - Clustering hiérarchique avec le critère de Ward : appliqué sur tous les datasets de features
        - Clustering via l'approche SPICE : appliqué sur les features apprises avec MoCoV2
    - Sorties : 
        - Arbre hiérachique du clustering + métriques d'évaluation / Modèle de clustering SPICE
        - Dossiers : 
            - Clustering hiérarchique : `results/clustering`
            - Clustering SPICE : `results/spice/results/paris2connect/true_resnet18/spice_self224`
    - Code associé : 
        - Clustering hiérarchique : 
            - Calcul du clustering + visualisation des résultats : [jupyter/paris2connect/annotation/4_clustering__agglomerative.ipynb](jupyter/paris2connect/annotation/4_clustering__agglomerative.ipynb)
            - Comparaison des features évaluées via les métriques du clustering : [jupyter/paris2connect/annotation/4_clustering__features_comparison.ipynb](jupyter/paris2connect/annotation/4_clustering__features_comparison.ipynb)
        - Clustering SPICE : 
            - Entrainement du modèle : cf. section [Clustering SPICE](#clustering-spice)
            - Export des résultats de modèle + évaluation des résultats : [jupyter/paris2connect/annotation/4_clustering__spice.ipynb](jupyter/paris2connect/annotation/4_clustering__spice.ipynb)


## Lancement des expériences
### Requirements
Pour lancer les notebooks décrits ci-dessus, il est nécessaire de créer un environnement virtuel contenant les dépendances listées dans le fichier `requirements.txt` du dépôt.

Remarques:
- Pour le notebook `3_feature_extraction__pytorch_models.ipynb` les premières expériences ont été lancé avec `torchvision==0.12.0` qui ne disposait pas de la nouvelle API mettant à disposition un plus grand nombre de modèles pré-entrainés. Pour extraire les features sur la totalité des modèles listés, il faut une version de torchvision `torchvision>=0.13.0`.
- Pour certaines expériences, il est nécessaire de créer un environnement virtuel spécifique contenant en priorité les dépendances propres aux dépôt de codes externes mobilisés. Se reférer aux sections suivantes pour savoir quels dépendances installer.


### Sélection d'images de véhicules
La sélection d'images de véhicules sur les vidéos se fait en appliquant des algorithmes de détection + suivi de véhicules
(les mêmes algorithmes qui pourraient être utilisés in fine pour le comptage). Cette étape se fait entièrement sur la base de code existant: 
 - DeepSORT : https://github.com/mikel-brostrom/Yolov5_StrongSORT_OSNet/tree/v5.0 (**Le tag 5.0 est important**)​
 - StrongSORT : https://github.com/mikel-brostrom/Yolov5_StrongSORT_OSNet/tree/v6.0  (**Le tag 6.0 est important**)​

 Pour lancer les expériences les étapes suivantes doivent être appliquées : 
 1. Cloner les dépôts listés ci-dessus pour récupérer les versions de code de DeepSORT et StrongSTRONG en prenant bien soin de rester sur le tag spécifié.
 2. Créer un environnement virtuel en installant les dépendances listées dans dépôt
 3. Lancer une des commandes suivantes pour reproduire les résultats disponibles pour le disque `lead_disk`: 
    - Tracking DeepSORT : 
        ```
        python track.py --source /home/pytorch/lead_disk/campagne/SP01-CAM-03/anonymized --output /home/pytorch/lead_disk/campagne/SP01-CAM-03/anonymized --imgsz 1920 --device 1 --save-vid --save-bbox --save-crop --classes 1 2 3 5 7
        ```
    - Tracking StrongSORT : 
        ```
        python track.py --yolo-weights yolov5l6.pt --source /home/pytorch/lead_disk/campagne/SP01-CAM-03/anonymized --out-dir /home/pytorch/lead_disk/campagne/SP01-CAM-03/anonymized/StrongSORT/ --imgsz 1920 --device 1 --save-bbox --save-crop --classes 2 5 7 --name StrongSORT_yolov5l6_osnet_x0_25_msmt17
        ```

### Feature Learning MoCov2
L'entrainement des modèles de representation learning avec le framework MoCov2 a été réalisé en utilisant le code disponible dans le dépôt https://git.irt-systemx.fr/lead/camera_task/spice (fork du dépôt [SPICE](https://github.com/niuchuangnn/SPICE)). 


Les étapes pour lancer la partie representation learning sont les suivantes : 
1. Cloner le dépôt https://git.irt-systemx.fr/lead/camera_task/spice
2. Se positionner sur la branche `develop` qui contient les adaptations avec l'ajout de la source de données Paris2Connect
3. Créer un environnement virtuel avec les dépendances nécessaires listées dans ce dépôt
4. Pour entrainer le modèle de feature learning, lancer la commande : 
    ```
    python tools/train_moco.py --data_type paris2connect --data /home/pytorch/lead_disk/campagne/tracking_selection_sc --img_size 224 --save_folder /home/pytorch/lead_disk/campagne/tracking_selection_sc/spice/results/paris2connect/moco224 --save-freq 10 --arch true_resnet18 --batch-size 130 --resume /home/pytorch/lead_disk/campagne/tracking_selection_sc/spice/results/paris2connect/moco224/checkpoint_last.pth.tar --moco-k 2600 --all 0
    ```
    Remarques : 
    - Le choix du backbone se fait avec le paramètre `--arch`
    - Pour lancer l'entrainemennt en repartant des poids initiaux d'ImageNet ``--resume` à partir des poids téléchargés

5. Pour exporter les features, lancer la commande : 
    ```
    python tools/pre_compute_embedding.py --config-file ./configs/paris2connect/embedding.py
    ```
    Remarque : le choix du dataset sur lequel calculer les features se fait en modifiant le fichier de config `./configs/paris2connect/embedding.py`

### Feature Learning MoBY
L'entrainement du modèle de représentation learning avec le framework MoBY et le backbone SWIN a été réalisé en utilisant le code disponible dans le dépôt https://git.irt-systemx.fr/lead/camera_task/transformer-ssl (fork du dépôt [Transformer-SSL](https://github.com/SwinTransformer/Transformer-SSL)).

Les étapes pour lancer la partie representation learning sont les suivantes : 
1. Cloner le dépôt https://git.irt-systemx.fr/lead/camera_task/transformer-ssl
2. Se positionner sur la branche `develop` qui contient les adaptations avec l'ajout de la source de données Paris2Connect
3. Créer un environnement virtuel avec les dépendances nécessaires listées dans ce dépôt
4. Pour entrainer le modèle de feature learning, lancer la commande : 
    ```
    python -m torch.distributed.launch --nproc_per_node 2 --master_port 12345 moby_main.py --cfg configs/moby_swin_tiny.yaml --data-path /home/pytorch/lead_disk/campagne/tracking_selection_sc/StrongSORT_yolov5l6_osnet_x0_25_msmt17 --batch-size 64 --output /home/pytorch/lead_disk/results/transformer_ssl --tag from_imagenet1k_queue1152
    ```

5. Pour exporter les features, utiliser le notebook : `jupyter/paris2connect/annotation/3_feature_extraction__transformer_ssl.ipynb`

### Clustering SPICE
L'entrainement des modèles de representation learning avec le framework MoCov2 a été réalisé en utilisant le code disponible dans le dépôt https://git.irt-systemx.fr/lead/camera_task/spice (fork du dépôt [SPICE](https://github.com/niuchuangnn/SPICE)). 


Les étapes pour lancer la partie representation learning sont les suivantes : 
1. Cloner le dépôt https://git.irt-systemx.fr/lead/camera_task/spice
2. Se positionner sur la branche `develop` qui contient les adaptations avec l'ajout de la source de données Paris2Connect
3. Créer un environnement virtuel avec les dépendances nécessaires listées dans ce dépôt
4. Pour entrainer le modèle de feature learning, lancer la commande : 
     ```
    python tools/train_moco.py --data_type paris2connect --data /home/pytorch/lead_disk/campagne/tracking_selection_sc --img_size 224 --save_folder /home/pytorch/lead_disk/campagne/tracking_selection_sc/spice/results/paris2connect/moco224 --save-freq 10 --arch true_resnet18 --batch-size 130 --resume /home/pytorch/lead_disk/campagne/tracking_selection_sc/spice/results/paris2connect/moco224/checkpoint_last.pth.tar --moco-k 2600 --all 0
    ```
    Remarques : 
    - Le choix du backbone se fait avec le paramètre `--arch`
    - Pour lancer l'entrainemennt en repartant des poids initiaux d'ImageNet ``--resume` à partir des poids téléchargés
5. Exporter les features, lancer la commande : 
    ```
    python tools/pre_compute_embedding.py --config-file ./configs/paris2connect/embedding.py
    ```
    Remarque : le choix du dataset sur lequel calculer les features se fait en modifiant le fichier de config `./configs/paris2connect/embedding.py`
6. Entrainement de la tête de clustering pour obtenir des pseudo labels
    - Train Clustering Head wih fixed representation learning model
    ```
    python tools/train_self_v2.py --config-file ./configs/paris2connect/spice_self.py --all 0
    ```

    - Export Pseudo Reliable labels
    ```
    python tools/local_consistency.py --config-file ./configs/paris2connect/eval.py --embedding /home/pytorch/lead_disk/campagne/tracking_selection_sc/spice/results/paris2connect/embedding224/feas_moco_512_l2.npy
    ```
7. Entrainement conjoint des features et de la tête de clustering 
    ```
    python ./tools/train_semi.py --save_dir /home/pytorch/lead_disk/echantillons_2021-03-21/spice/results/paris2connect/ --epoch 300 --num_labels 180 --batch_size 16 --uratio 7 --net true_resnet18 --data_dir /home/pytorch/lead_disk/echantillons_2021-03-21/yolov5l6_osnet_ibn_x1_0_MSMT172/tracking_selection_sc --dataset paris2connect --label_file /home/pytorch/lead_disk/echantillons_2021-03-21/spice/results/paris2connect/eval224/labels_reliable_-1.000000_180.npy --num_classes 10 --num_train_iter 16384 --eval_batch_size 50 --num_eval_iter 100 --save_name spice_semi_v2 --load_path /home/pytorch/lead_disk/echantillons_2021-03-21/spice/results/paris2connect/spice_semi_v2
    ```

"# BadProjectAI" 

- Les conventions de nommage:
  
  1. Noms de fichiers:
     
     * Les fichiers Python doivent être nommés en minuscules avec des traits de soulignement (_) pour séparer les mots. Par exemple : my_module.py
     * Les fichiers de modèles de données Django (contenant des classes de modèle) doivent généralement être nommés models.py

  2. Noms de variables :

      * Utilisez des noms de variables descriptifs en minuscules avec des traits de soulignement pour séparer les mots. Par exemple : my_variable, user_name.
      * Évitez les noms de variables non explicites comme temp, foo, bar, etc.

  3. Noms de fonctions et de méthodes :
  
      * Utilisez des noms de fonctions et de méthodes en minuscules avec des traits de soulignement pour séparer les mots. Par exemple : calculate_total(), get_user_profile().
      * Les noms de méthodes de classe devraient également suivre cette convention.

  4. Noms de classes :

      * Utilisez le style CamelCase pour nommer les classes, avec la première lettre de chaque mot en majuscule, sans traits de soulignement. Par exemple : MyClass, UserProfile, ArticleDetail.
      * Les noms de classes modèles dans Django doivent être des noms de singulier descriptifs. Par exemple : User, Article, Comment.

  5. Noms de champs de modèle :

      * Les champs de modèle devraient être en minuscules, avec des traits de soulignement pour séparer les mots si nécessaire. Par exemple : first_name, created_at.
      * Évitez les noms de champs non descriptifs comme fld1, fld2, etc.
      
  6. Noms de URLs :
    
      * Les noms de routes dans les fichiers de configuration des URL (urls.py) doivent être en minuscules avec des traits
        de soulignement ou des tirets pour séparer les mots. Par exemple : my_view, article_detail, user_profile.

  7. Noms de templates :

      * Les noms de fichiers de templates doivent être en minuscules avec des traits de soulignement pour séparer les mots. Par exemple : base_template.html, article_detail.html.
    

- Le préquis pour Django:

        * Django est un framework web écrit en Python, donc la première étape est d'installer Python sur votre système. Django prend en charge Python 3.6 ou version ultérieure.
  
        *  Pip est le gestionnaire de paquets de Python qui vous permet d'installer et de gérer les bibliothèques Python  Assurez-vous d'avoir pip installé sur votre système. Vous pouvez vérifier en exécutant la   
         commande suivante dans votre terminal ou votre invite de commande : pip --version
  
        * Environnement virtuel (recommandé) : Bien qu'il ne soit pas strictement nécessaire, il est fortement recommandé d'utiliser un environnement virtuel pour isoler votre projet Django
         et ses dépendances des autres projets Python sur votre système. Vous pouvez créer un environnement virtuel à l'aide de l'outil : python3 -m venv myenv
  
        * Une fois que vous avez Python et pip installés, vous pouvez installer Django à l'aide de pip. Il est recommandé d'installer Django dans votre environnement virtuel.
          Vous pouvez l'installer en exécutant la commande suivante : pip install django


- Pour lancer le serveur Django : py manage.py runserver
           

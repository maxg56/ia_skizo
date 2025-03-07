# ia_skizo

Ce projet implémente un système d'intelligences artificielles capables de répondre aux questions et d'engager une conversation en posant systématiquement une nouvelle question.

## **Fonctionnalités**
- Utilisation de différentes personnalités IA.
- Reconnaissance et transcription audio.
- Génération de réponses via une IA.
- Lecture des réponses à haute voix.
- Boucle interactive pour une conversation fluide.

## **Installation**
### **Prérequis**
- Python 3.x
- Bibliothèques requises :
  - `from ai import generate_response`
  - `from speak import speak`
  - `from son import record_audio, transcribe_audio`
  - `re` (inclus dans Python)

### **Installation des dépendances**
Si certaines bibliothèques ne sont pas encore installées, assure-toi d'avoir les fichiers correspondants (`ai.py`, `speak.py`, `son.py`), ou installe les dépendances requises.

## **Utilisation**
1. **Lancer le programme** :  
   ```bash
   install_mobillama.sh
   ```
   ou 
   ```
   make
   ```
2. **Déroulement de la conversation** :
   - L'utilisateur parle (via microphone).
   - L'IA transcrit l'audio en texte.
   - Une réponse est générée en fonction du contexte et de la personnalité choisie.
   - L'IA pose toujours une nouvelle question pour maintenir la conversation.
   - L'interaction continue jusqu'à ce que l'utilisateur dise "stop", "quitte" ou "exit".

## **Structure du Code**
- `get_last_question(text: str)`: Extrait la dernière question d'un texte donné.
- `main()`: Gère la boucle de conversation avec plusieurs personnalités.
  - Enregistre et transcrit l'audio (désactivé pour l'instant).
  - Génère une réponse en fonction du contexte.
  - Pose toujours une nouvelle question.

## **Améliorations possibles**
- Implémentation d’un vrai système de personnalités avec des styles de réponse distincts.
- Ajout d’un système de mémoire pour améliorer la cohérence des conversations.
- Activation de la reconnaissance vocale et des entrées/sorties audio.

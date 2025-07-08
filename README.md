# Desenvolvendo sua Primeira API com FastAPI, Python e Docker

# Ambiente virtual 
Cria ambiente
   - ```sh
     pyenv virtualenv 3.11.4 workoutapi
     ```
Entra no ambiente
   - ```sh
     pyenv activate workoutapi
     ```
ou
   - ```sh
     source ~/.pyenv/versions/workoutapi/bin/activate
     ```
Primeiro acesso
   - ```sh
     pip install -r requirements.txt
     ```
Subir servidor
   - ```sh
     make run
     ```
 ou
   - ```sh
     uvicorn workout_api.main:app --reload
     ```




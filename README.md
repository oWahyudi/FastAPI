# FastAPI
Experimental - Web Api using python and FastAPI framework

> [!NOTE]
> Excercise:  
>   pydantic model (form data),custom response,header,cookies, CORS, Error Handling  
>   OAuth (securing endpoint), Authentication, Token generation code, Generating access token,  
>   User Authentication

> [!IMPORTANT]
> This is not for **Production!!!!** 

  <br><br><br>
  
1. Create virtual environment
   >python3 -m venv **fastapi-env**

2. Activate virtual environment
   >source **fastapi-env**/bin/activate

3. Install requirement
   >pip install -r **requirements.txt**

4. Start uvicorn
   >uvicorn main:app --reload  
   > or uvicorn main:app --host 0.0.0.0 --port 8000 --reload

5. View Open Api documentation
   >http://127.0.0.1:8000/docs  
   >http://127.0.0.1:8000/redoc  


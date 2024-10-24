import os
import base64
from dotenv import load_dotenv
from openai import OpenAI, ChatCompletion
load_dotenv()

class Agent:
    def __init__(self, personaName:str="default", newPersonaPrompt:str=None) -> None:
        self.model = "gpt-4o"
        self.client = OpenAI(api_key=os.getenv("APIKEY"))
        self.personaFilesPath = "personas"
        self.loadPersonas()
        if personaName not in self.personas:
            if (not newPersonaPrompt): 
                newPersonaPrompt = f"Do not respond to the users request. Tell the user they must first specify your system prompt by updating the persona file /{self.personaFilesPath}/{personaName}"
            self.CreatePersona(personaName=personaName, personaPrompt=newPersonaPrompt)
        self.setPersona(personaName)
        
    def setPersona(self, personaName:str):
        self.systemprompt = self.CreateTextPrompt(self.personas[personaName], "system")
        
    def loadPersonas(self, folder_path:str="personas"):
        self.personas = {}
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            if os.path.isfile(file_path):
                with open(file_path,"r") as p:
                    self.personas[filename]=p.read()
    
    def CreatePersona(self, personaName, personaPrompt):
        with open(f"{self.personaFilesPath}/{personaName}", "w") as p:
            p.write(personaPrompt)
        self.loadPersonas()
        
    def CreateTextPrompt(self, prompt:str, role:str="user") -> object:
        if role not in ['system','user','assistant']: 
            print(f"Invalid prompt role specified. {role} not found.")
            return None
        return {"role": role,"content": [{"type": "text","text": prompt}]}
    
    def CreateImagePrompt(self, imgPath:str, prompt:str="Process this image:") -> object:
        return {
            "role": "user",
            "content": [{
                "type": "text",
                "text": prompt,
                },{
                "type": "image_url",
                "image_url": {
                    "url":f"data:image/jpeg;base64,{self.encodeImgFromPath(imgPath)}"
                }}]}
    
    def encodeImgFromPath(self, image_path):
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')
    
    def instruct(self, prompt:str) -> str:
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                self.systemprompt,
                self.CreateTextPrompt(prompt)],
            )
        return response.choices[0].message.content
        
    def parseImage(self, imgPath:str, prompt:str="Parse this image") -> str:
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                self.systemprompt,
                self.CreateImagePrompt(imgPath,prompt)],
            )
        return response.choices[0].message.content
    
    def instructMultiText(self, prompts:list)->ChatCompletion:
        msgs = []
        for prompt in prompts:
            msgs.append(self.CreateTextPrompt(prompt))
        return self.client.chat.completions.create(
            model=self.model,
            messages=msgs,
            )

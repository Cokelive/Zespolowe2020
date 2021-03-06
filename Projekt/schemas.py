from typing import List
from pydantic import BaseModel
from pydantic import EmailStr

from fastapi import File, UploadFile

import os
from dotenv import load_dotenv, find_dotenv

class Settings(BaseModel):
    authjwt_secret_key: str = os.environ.get("KEY")
    # authjwt_token_location: set = {"cookies"}
    # authjwt_cookie_csrf_protect: bool = False

class User(BaseModel):
    email: EmailStr
    username: str

class User_creation(User):
    password: str

class User_DB(User):
    hashed_password: str

class Reset_pass_form(BaseModel):
    token: str
    new_password: str

class Reset_pass_request(BaseModel):
    email: EmailStr

class User_login(BaseModel):
    email: EmailStr
    password: str

class File_download(BaseModel):
    file_name: str

class File_delete(BaseModel):
    file_name: str

class File_rename(BaseModel):
    old_file_name: str
    new_file_name: str

class Folder_create(BaseModel):
    folder_name: str

class Folder_delete(BaseModel):
    folder_name: str

class Folder_rename(BaseModel):
    old_folder_name: str
    new_folder_name: str

class Create_sharing_link(BaseModel):
    folder_name: str

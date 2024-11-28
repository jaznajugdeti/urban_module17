# В модуле user.py напишите APIRouter с префиксом '/user' и тегом 'user',
# а также следующие маршруты, с пустыми функциями:
from fastapi import APIRouter
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from backend.db_depends import get_db
from typing import Annotated
from models import User
# from schemes import CreateUser, UpdateUser
from sqlalchemy import insert, select, update, delete
import slugify

router = APIRouter(prefix='/user', tags=['user'])

# get '/' с функцией all_users.
@router.get('/')
async def all_users(db: Annotated[Session, Depends(get_db)]:
    users = db.scalars(select(User)).all()
    return users

# get '/user_id' с функцией user_by_id.
@router.get('/user_id')
async def user_by_id(db: Annotated[Session, Depends(get_db)], user_id: int):
    users = db.scalar(select(User).where(User.id == user_id))
    for user in users:
        if user is not None:
            return user
        else:
            raise HTTPException(status_code=404, detail='User was not found')

# post '/create' с функцией create_user.
@router.post('/create')
async def create_user(db: Annotated[Session, Depends(get_db)], create_user_model: CreateUser):
    db.execute(insert(User).values(username=create_user_model.username,
                    firstname= create_user_model.firstname,
                                   lasrname= create_user_model.lastname,
                                   age=create_user_model.age,
                                   slug=create_user_model.slug))
    db.commit()
    return{{'status_code': status.HTTP_201_CREATED, 'transaction': 'Successful'}}
# put '/update' с функцией update_user.
@router.put('/update')
async def update_user(db: Annotated[Session, Depends(get_db)], user_id: int,
                      update_user_model: UpdateUser):
    users = db.scalar(select(User).where(User.id == user_id))
    for user in users:
        if user is not None:
            db.execute(insert(User).values(
                                           firstname=update_user_model.firstname,
                                           lasrname=update_user_model.lastname,
                                           age=update_user_model.age,
                                           ))
            db.commit()
            return {{'status_code': status.HTTP_200_OK,
                     'transaction': 'User update is successful!'}}
        else:
            raise HTTPException(status_code=404, detail='User was not found')


# delete '/delete' с функцией delete_user.
@router.delete('/delete')
async def delete_user(db: Annotated[Session, Depends(get_db)], user_id: int):
    users = db.scalar(select(User).where(User.id == user_id))
    for user in users:
        if user is not None:
            db.execute(delete(User).where(User.id == user_id))
            db.commit()
            return {{    'status_code': status.HTTP_200_OK,
                          'transaction': 'User delete is successful!'   }}
        else:
            raise HTTPException(status_code=404, detail='User was not found')

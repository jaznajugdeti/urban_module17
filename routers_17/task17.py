# Маршруты:
# В модуле task.py напишите APIRouter с префиксом '/task' и тегом 'task',
# а также следующие маршруты, с пустыми функциями:

from fastapi import APIRouter

router = APIRouter(prefix='/task', tags=['task'])

# get '/' с функцией all_tasks.
@router.get('/')
async def all_tasks():
    pass

# get '/task_id' с функцией task_by_id.
@router.get('/task_id')
async def task_by_id():
    pass
# post '/create' с функцией create_task.
@router.post('/create')
async def create_task():
    pass

# put '/update' с функцией update_task.
@router.put('/update')
async def update_task():
    pass
# delete '/delete' с функцией delete_task.
@router.delete('/delete')
async def delete_task():
    pass
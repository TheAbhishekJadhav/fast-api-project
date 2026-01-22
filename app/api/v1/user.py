from fastapi import APIRouter, Depends, HTTPException

from app.db.schema import SessionLocal
from app.models.user import UserCreate, UserRead
from app.services.user_service import UserService
from app.services.user_service_interface import UserServiceInterface


router = APIRouter()

def get_user_service() -> UserServiceInterface:
    return UserService(session=SessionLocal())

@router.get("/users", response_model=list[UserRead])
def list_users(user_service: UserServiceInterface = Depends(get_user_service)):
    return user_service.list_users()

@router.get("/users/{user_id}")
def get_user(user_id: int, user_service: UserServiceInterface = Depends(get_user_service)):
    user = user_service.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.post("/users", response_model=UserRead)
def create_user(user: UserCreate, user_service: UserServiceInterface = Depends(get_user_service)):
    return user_service.create_user(user.name)

@router.put("/users/{user_id}", response_model=UserRead)
def update_user(user_id: int, user: UserCreate, user_service: UserServiceInterface = Depends(get_user_service)):
    updated_user = user_service.update_user(user_id, user.name)
    if not updated_user:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user

@router.delete("/users/{user_id}")
def delete_user(user_id: int, user_service: UserServiceInterface = Depends(get_user_service)):
    success = user_service.delete_user(user_id)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
    return {"Success": True}

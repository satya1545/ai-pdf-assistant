from fastapi import APIRouter, Depends

from schemas.user import UserResponse
from utils.dependencies import get_current_user

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.get(
    "/me",
    response_model=UserResponse
)
def get_profile(
    current_user=Depends(get_current_user)
):
    return current_user
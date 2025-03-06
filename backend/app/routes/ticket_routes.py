from fastapi import APIRouter

router = APIRouter()
@router.get("/tickets")
def get_tickets():
    return {"tickets": "Here we will fetch tickets"}

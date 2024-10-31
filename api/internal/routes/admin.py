from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from database.db_mysql import async_db_session, scoped_session_dependency, get_db
from sqlalchemy import select
from models.users import User_site
from models.others import Lab

router = APIRouter(
    prefix='/admin'
)


@router.get('/login')
async def get_all_users(db: AsyncSession = Depends(get_db)):
    stmt = select(Lab)  
    result = await db.execute(stmt)
    labs = result.scalars().all()  
    
    labs_list = [dict(lab.__dict__) for lab in labs] 
    
    for lab in labs_list:
        lab.pop('_sa_instance_state', None)
 
    return {
        "labs": labs_list  
    }


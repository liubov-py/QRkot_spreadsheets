from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.core.user import current_superuser, current_user
from app.crud.donation import donation_crud
from app.models import User
from app.schemas.donation import DonationCreate, DonationDB, DonationGet
from app.services.investment_process import investment

router = APIRouter()


@router.post(
    '/',
    response_model=DonationGet,
    response_model_exclude_none=True,
)
async def create_donation(
        donation: DonationCreate,
        user: User = Depends(current_user),
        session: AsyncSession = Depends(get_async_session),
):
    new_donation = await donation_crud.create(
        donation, user, session
    )
    return await investment(session, new_donation)


@router.get(
    '/',
    response_model=list[DonationDB],
    response_model_exclude_none=True,
    dependencies=[Depends(current_superuser)],
)
async def get_all_donation(
        session: AsyncSession = Depends(get_async_session)
) -> list[str]:
    return await donation_crud.get_multi(session)


@router.get(
    '/my',
    response_model=list[DonationGet],
    response_model_exclude={'user_id'},
)
async def get_my_donation(
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_user),
) -> list[str]:
    return await donation_crud.get_by_user(
        session=session, user=user
    )

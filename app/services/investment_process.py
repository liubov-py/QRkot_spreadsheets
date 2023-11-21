from datetime import datetime

from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.donation import donation_crud


async def investment(
        session: AsyncSession,
        object,
):
    project, donation = await donation_crud.get_open_object(session)

    if not project or not donation:
        await session.commit()
        await session.refresh(object)
        return object

    project_summ = project.full_amount - project.invested_amount
    donation_summ = donation.full_amount - donation.invested_amount

    if project_summ == donation_summ:
        await item_data(project, donation_summ)
        await item_data(donation, donation_summ)

    elif project_summ > donation_summ:
        project.invested_amount += donation_summ
        await item_data(donation, donation_summ)

    elif project_summ < donation_summ:
        donation.invested_amount += project_summ
        await item_data(project, project_summ)

    session.add(project)
    session.add(donation)
    await session.commit()
    await session.refresh(project)
    await session.refresh(donation)
    await investment(session, object)
    return object


async def item_data(item, summ) -> None:
    item.invested_amount += summ
    item.fully_invested = True
    item.close_date = datetime.now()

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.base.services.healthcheck import HealthCheckService
from core.db.accessor import get_db_session


async def get_healthcheck_service(
    session: AsyncSession = Depends(get_db_session),
) -> HealthCheckService:
    return HealthCheckService(_session=session)

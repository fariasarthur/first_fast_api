from sqlalchemy import select
from sqlalchemy.orm import Session

from first_fast_api.models import User, table_registry


def test_create_user(session):
    
    user = User(username='art', email='art@gmail.com', password='senha1')

    session.add(user)
    session.commit()
    result = session.scalar(
        select(User).where(user.username == 'art')
    )

    assert result.username == 'art'

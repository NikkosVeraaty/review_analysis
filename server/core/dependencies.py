from fastapi import Depends, Request

from repositories.reviews import ReviewSQLiteRepository


def get_review_repository(request: Request):
    return ReviewSQLiteRepository(connection=request.app.state.connection)


review_repository = Depends(get_review_repository)

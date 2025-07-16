from typing import Annotated, Sequence

from fastapi import APIRouter, Depends, Query, status

from core.schemas.reviews import ReviewCreateSchema, ReviewResponseSchema
from services.reviews import ReviewServiceProtocol, ReviewService


router = APIRouter(prefix="/reviews", tags=["Reviews"])

review_service = Depends(ReviewService)


@router.post(
    path="",
    summary="Sentiment analysis in a `review`",
    responses={
        status.HTTP_201_CREATED: {
            "model": ReviewResponseSchema,
            "description": "The review has been analyzed and saved",
        },
    },
)
async def sentiment_analysis_in_review(
    review: ReviewCreateSchema,
    service: Annotated[ReviewServiceProtocol, review_service],
):
    analyzed_review = service.create(review=review)

    return analyzed_review


@router.get(
    path="",
    summary="Get a `rewiews` by santiment",
    responses={
        status.HTTP_200_OK: {
            "model": Sequence[ReviewResponseSchema],
            "description": "Ok Response",
        },
    },
)
async def get_rewiews_by_sentiment(
    sentiment: Annotated[str, Query()],
    service: Annotated[ReviewServiceProtocol, review_service],
):
    reviews = service.get_by_sentiment(sentiment=sentiment)
    
    return reviews 

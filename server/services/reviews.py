import re
from datetime import datetime, timezone
from typing import Annotated, Protocol, Self, Sequence

from core.dependencies import review_repository
from core.schemas.reviews import ReviewCreateSchema, ReviewResponseSchema
from repositories.reviews import ReviewRepositoryProtocol
from utils.sentiment_words import words


class ReviewServiceProtocol(Protocol):
    def create(
        self: Self,
        review: ReviewCreateSchema,
    ) -> ReviewResponseSchema: ...

    def get_by_sentiment(
        self: Self,
        sentiment: str,
    ) -> Sequence[ReviewResponseSchema]: ...


class ReviewService:
    def __init__(
        self: Self,
        review_repository: Annotated[
            ReviewRepositoryProtocol,
            review_repository,
        ],
    ) -> None:
        self.review_repository = review_repository

    def create(
        self: Self,
        review: ReviewCreateSchema,
    ) -> ReviewResponseSchema:
        text = review.text
        created_at = datetime.now(timezone.utc).isoformat()

        sentiment = "neutral"
        for word, sent in words.items():
            if re.search(word, text):
                sentiment = sent
                break

        review_id = self.review_repository.create(
            text=text,
            created_at=created_at,
            sentiment=sentiment,
        )

        return ReviewResponseSchema.model_validate(
            {
                "id": review_id,
                "text": text,
                "sentiment": sentiment,
                "created_at": created_at,
            },
        )

    def get_by_sentiment(
        self: Self,
        sentiment: str,
    ) -> Sequence[ReviewResponseSchema]:
        reviews = self.review_repository.get_by_sentiment(sentiment=sentiment)

        return [ReviewResponseSchema.model_validate(
            {
                "id": rev[0],
                "text": rev[1],
                "sentiment": rev[2],
                "created_at": rev[3],
            },
        ) for rev in reviews]

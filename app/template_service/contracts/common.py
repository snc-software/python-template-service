import typing
from pydantic import BaseModel, Field


class ProblemDetails(BaseModel):
    title: str = Field(...,
                       description="A short, human-readable summary of the problem.")
    status: int = Field(..., description="The HTTP status code.")


class ValidationProblemDetails(ProblemDetails):
    extensions: typing.Optional[typing.Dict[str, typing.Any]] = Field(
        None, description="Additional fields providing more context about the error."
    )

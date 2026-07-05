from ..contracts.common import ProblemDetails

NOT_FOUND = {
    404: {"model": ProblemDetails, "description": "Resource not found"}
}

SERVER_ERROR = {
    500: {"model": ProblemDetails, "description": "Internal server error"}
}

from awesome_exception.exceptions import (
    BadRequest,
    InternalServerError,
    NotFound,
    ResourceGone,
    Unauthorized,
    UnprocessableEntity,
    Forbidden,
    NotImplemented,
    ServiceUnavailable,
)


def test_exception_format():
    assert BadRequest("msg").status_code == 400
    assert Unauthorized("msg").status_code == 401
    assert Forbidden("msg").status_code == 403
    assert NotFound("msg").status_code == 404
    assert ResourceGone("msg").status_code == 410
    assert UnprocessableEntity("msg").status_code == 422
    assert InternalServerError("msg").status_code == 500
    assert NotImplemented("msg").status_code == 501
    assert ServiceUnavailable("msg").status_code == 503

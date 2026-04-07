from app.dependencies import get_order_repository


def test_get_order_repository_returns_same_instance():
    repo1 = get_order_repository()
    repo2 = get_order_repository()
    assert repo1 is repo2

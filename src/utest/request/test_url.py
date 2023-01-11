from src.Talos.request.url import Url


def test_build_url_with_path_params():
    url = Url(protocol="https",
              host="localhost",
              port="8080",
              path="product/{productId}",
              path_params={'productId': '1234'})

    assert url.build() == "https://localhost:8080/product/1234"


def test_build_url_with_query_params():
    url = Url(protocol="https",
              host="localhost",
              port="8080",
              path="product",
              query_params={'productName': 'Hobbit', 'productCategory': 'Fiction'})

    assert url.build() == "https://localhost:8080/product?productName=Hobbit&productCategory=Fiction"


def test_build_url_with_fragment():
    url = Url(protocol="https",
              host="localhost",
              port="8080",
              path="product",
              query_params={'productName': 'Hobbit', 'productCategory': 'Fiction'},
              fragment="productpage=2")

    assert url.build() == "https://localhost:8080/product?productName=Hobbit&productCategory=Fiction#productpage=2"

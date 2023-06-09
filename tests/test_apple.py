from selene import browser, have


def test_apple():
    browser.open('/shop/buy-mac/macbook-air/13-inch-m1')
    browser.element('#root').should(have.text('Choose your new MacBook Air.'))

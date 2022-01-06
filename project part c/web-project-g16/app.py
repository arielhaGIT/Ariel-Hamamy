from flask import Flask ,session


###### App setup
app = Flask(__name__)
app.config.from_pyfile('settings.py')

###### Pages
## Homepage
from pages.homepage.homepage import homepage
app.register_blueprint(homepage)

## About
from pages.about.about import about
app.register_blueprint(about)

## Profile
from pages.profile.profile import profile
app.register_blueprint(profile)

## Shop
from pages.shop.shop import shop
app.register_blueprint(shop)

## Sign In
from pages.SignIn.SignIn import SignIn
app.register_blueprint(SignIn)

## Sign Up
from pages.SignUp.SignUp import SignUp
app.register_blueprint(SignUp)

## payment
from pages.payment.payment import payment
app.register_blueprint(payment)

## cart
from pages.cart.cart import cart
app.register_blueprint(cart)

## returns
from pages.returns.returns import returns
app.register_blueprint(returns)

## gallery
from pages.gallery.gallery import gallery
app.register_blueprint(gallery)


## Page error handlers
from pages.page_error_handlers.page_error_handlers import page_error_handlers
app.register_blueprint(page_error_handlers)


###### Components
# Footer
from components.footer.footer import footer
app.register_blueprint(footer)

# Header
from components.header.header import header
app.register_blueprint(header)

## LogOut
from pages.LogOut.LogOut import LogOut
app.register_blueprint(LogOut)

## update details
from pages.UpdateDetails.UpdateDetails import UpdateDetails
app.register_blueprint(UpdateDetails)

## editShop details
from pages.editShop.editShop import editShop
app.register_blueprint(editShop)

## new_product details
from pages.new_product.new_product import new_product
app.register_blueprint(new_product)

from pages.confirmationOrder.confirmationOrder import confirmationOrder
app.register_blueprint(confirmationOrder)
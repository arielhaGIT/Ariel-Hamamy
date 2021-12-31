
function sendMethodToApi(method,url, payload,cb) {
    fetch(url, {
        method: method,
        headers: {
            'Accept': 'application/json, text/plain, */*',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(payload)
    }).then(res => res.json())
        .then(res => cb(res));
}

function getShoppingCartItems(url, cb) {
    fetch(url).then(res => res.json())
        .then(res => cb(res));
}

//Initiate
var QuantityFromIceCream = []; //Saves quantity from each Ice Cream for OneKg and HalfKg in an array
const iceCreams = []; //IceCreams names
var SpecificIceCream=[];
var cartID=-1;
iceCreams[0] = "Vanila";
iceCreams[1] = "Chocolate";
iceCreams[2] = "Pistachio";
iceCreams[3] = "Strawberry";
iceCreams[4] = "Pretzel";
iceCreams[5] = "Pecan";
iceCreams[6] = "Candies";
iceCreams[7] = "White";
var brandPrices = {
    Vanila:{halfKGPrice:12,KgPrice:20},
    Chocolate:{halfKGPrice:12,KgPrice:20},
    Pistachio:{halfKGPrice:14,KgPrice:24},
    Strawberry:{halfKGPrice:12,KgPrice:20},
    Pretzel:{halfKGPrice:2,KgPrice:3},
    Pecan:{halfKGPrice:1,KgPrice:2},
    Candies:{halfKGPrice:2,KgPrice:3},
    White:{halfKGPrice:3,KgPrice:4}
};
for (var i = 0; i < 8; i++) {
    QuantityFromIceCream.push({
        brand: iceCreams[i],
        Onekg: 0,
        Halfkg: 0
    })
}

function getFromStorage(key){
    const glidali = JSON.parse(localStorage.getItem('glidali'))
    if(glidali){
        return glidali[key];
    }
    return null;
}

function updateShoppingCart(){
    var userID = +getFromStorage("userID");

    if(cartID!==-1){
        sendMethodToApi('PUT','http://localhost:3000/updateShoppingCart',{
            cartID:cartID,
            userID:userID,
            selectedProducts:QuantityFromIceCream
        },function(results){
            console.log(results);
        })
    } else{
        sendMethodToApi('POST','http://localhost:3000/createShoppingCart',{
            userID:userID,
            selectedProducts:QuantityFromIceCream
        },function(results){
            cartID=results;
        })
    }
}
function loadShoppingCartItemsByUser(){
const params = new URLSearchParams(window.location.search)

if (params.has('userID') || getFromStorage('userID')) {
    let userID = getFromStorage('userID') || +params.get('userID');
    localStorage.setItem('glidali',JSON.stringify({userID:userID}));


getShoppingCartItems('http://localhost:3000/getShoppingCartByUser?userID=' + userID, function (results) {
    if (results.length > 0) { // if user has shopping cart already 
        console.log(results);
        cartID = results[0].id;
        SpecificIceCream = JSON.parse(results[0].selectedProducts);
        for (var i = 0; i < 8; i++) {
            const OneKg = SpecificIceCream[i].Onekg;
            const HalfKg = SpecificIceCream[i].Halfkg;
            QuantityFromIceCream[i]={
                brand: iceCreams[i],
                Onekg: OneKg,
                Halfkg: HalfKg
            };
        }
        if(window.page=='shoppingCart'){
            addItemToCart();
            document.getElementsByClassName('cartTotaPrice')[0].innerText = updateTotalPriceData() + '$';
        } else {
            UpdateFromLastCart();
        }
        
    }
})
}
}


//Navigation bar
function openNav() {
    document.getElementById("sideNavigationBar").style.width = "250px";
    document.getElementById("main").style.marginLeft = "-250px";
    document.getElementById("main").style.marginRight = "200px";
}
//Incresing amount of specific ice cream and specific weight by 1
function increaseValue(brand, quantity1, totalPrice, price, sign, OneOrHalf) {
    var value = parseInt(document.getElementById(quantity1).value, 10);
    value = isNaN(value) ? 0 : value;
    value++;
    document.getElementById(quantity1).value = value;
    updateTotalPrice(totalPrice, price, sign);
    updateCartItems(brand, value, OneOrHalf);
   
}
//Decreasing amount of specific ice cream and specific weight by 1
function decreaseValue(brand, quantity1, totalPrice, price, sign, OneOrHalf) {
    var value = parseInt(document.getElementById(quantity1).value, 10);
    value = isNaN(value) ? 0 : value;
    if (value < 1)
        return;
    value--;
    document.getElementById(quantity1).value = value;
    updateTotalPrice(totalPrice, price, sign);
    updateCartItems(brand, value, OneOrHalf);
}
//Updating total price 
function updateTotalPrice(totalPrice, price, sign) {
    var value = parseInt(document.getElementById(totalPrice).value, 10);
    if (sign == '-')
        value = value - price;
    else {
        value = value + price;
    }
    if (value <= 0)
        document.getElementById(totalPrice).value = 0;
    else
        document.getElementById(totalPrice).value = value;
}
//Updating the array of the items and setting the local storage 
function updateCartItems(ItemName, quantity, OneOrHalf) {
    for (var i = 0; i < 8; i++) {
        if (QuantityFromIceCream[i].brand == ItemName) {
            if (OneOrHalf == 1) {
                QuantityFromIceCream[i].Onekg = quantity;
            } else {
                QuantityFromIceCream[i].Halfkg = quantity;
            }
        }
    }
    var JSONreadyUsers = JSON.stringify(QuantityFromIceCream);
   // localStorage.setItem('QuantityFromIceCream', JSONreadyUsers);
    updateShoppingCart();
}

//Adding divs to the cart item by the array was made in 'Our Products' page
function addItemToCart() {
    for (var i = 0; i < 8; i++) {
        var SpecificIceCream = QuantityFromIceCream;
        OneKg = SpecificIceCream[i].Onekg;
        HalfKg = SpecificIceCream[i].Halfkg;
        if (OneKg != 0 || HalfKg != 0) {
            var cartRow = document.createElement('div');
            var cartItems = document.getElementsByClassName('products')[0];
            if (QuantityFromIceCream[i].brand == 'Vanila') {
                var cartRowContents = `
        <div class="product">
        <img src="../image/Vanilla.jpeg">
        <div class="product-info">
                <h3 class="product-name">Vanila</h3>
                <h2 class="product-price-1kg">20.00$ - 1KG</h2>
                <p class="product-quantity-1kg">Qnt: <input class="product-quantity-1kg-input" type="number" min="1" id="${i + 'Onekg'}" onclick="UpdateCart(true,this,'Onekg',${i})">
                <h2 class="product-price-Halfkg">12.00$ - 0.5KG</h2>
                <p class="product-quantity-Halfkg">Qnt: <input class="product-quantity-Halfkg-input" type="number" min="1" id="${i + 'Halfkg'}" onclick="UpdateCart(true,this,'Halfkg',${i})" >
                <div class="product-remove">
                    <i class="fa fa-trash" aria-hidden="true"></i>
                    <button class="remove" onclick=RemoveBTM()>Remove</button>
                </div>
            </div>
        </div>`
            }
            if (QuantityFromIceCream[i].brand == 'Chocolate') {
                var cartRowContents = `
          <div class="product">
          <img src="../image/chocolate.jpeg">
          <div class="product-info">
                  <h3 class="product-name">Chocolate</h3>
                  <h2 class="product-price-1kg">20.00$ - 1KG</h2>
                  <p class="product-quantity-1kg">Qnt: <input class="product-quantity-1kg-input" type="number" min="1" id="${i + 'Onekg'}"  onclick="UpdateCart(true,this,'Onekg',${i})">
                  <h2 class="product-price-Halfkg">12.00$ - 0.5KG</h2>
                  <p class="product-quantity-Halfkg">Qnt: <input class="product-quantity-Halfkg-input"  type="number" min="1" id="${i + 'Halfkg'}"  onclick="UpdateCart(true,this,'Halfkg'${i})">
                  <div class="product-remove">
                      <i class="fa fa-trash" aria-hidden="true"></i>
                      <button class="remove" onclick=RemoveBTM()>Remove</button>
                  </div>
              </div>
          </div>`
            }

            if (QuantityFromIceCream[i].brand == 'Pistachio') {
                var cartRowContents =
                    `<div class="product">
        <img src="../image/pistachio.jpeg">
        <div class="product-info">
                <h3 class="product-name">Pistachio</h3>
                <h2 class="product-price-1kg">24.00$ - 1KG</h2>
                <p class="product-quantity-1kg">Qnt: <input class="product-quantity-1kg-input"  type="number" min="1" id="${i + 'Onekg'}"  onclick="UpdateCart(true,this,'Onekg',${i})">
                <h2 class="product-price-Halfkg">14.00$ - 0.5KG</h2>
                <p class="product-quantity-Halfkg">Qnt: <input class="product-quantity-Halfkg-input" type="number" min="1" id="${i + 'Halfkg'}"  onclick="UpdateCart(true,this,'Halfkg',${i})">
                <div class="product-remove">
                    <i class="fa fa-trash" aria-hidden="true"></i>
                    <button class="remove" onclick=RemoveBTM()>Remove</button>
                </div>
            </div>
        </div>`
            }
            if (QuantityFromIceCream[i].brand == 'Strawberry') {
                var cartRowContents =
                    `<div class="product">
          <img src="../image/strawberry.jpeg">
          <div class="product-info">
              <h3 class="product-name">Strawberry</h3>
                  <h2 class="product-price-1kg">20.00$ - 1KG</h2>
                  <p class="product-quantity-1kg">Qnt: <input class="product-quantity-1kg-input" type="number" min="1" id="${i + 'Onekg'}"  onclick="UpdateCart(true,this,'Onekg',${i})">
                  <h2 class="product-price-Halfkg">12.00$ - 0.5KG</h2>
                  <p class="product-quantity-Halfkg">Qnt: <input class="product-quantity-Halfkg-input" type="number" min="1" id="${i + 'Halfkg'}"  onclick="UpdateCart(true,this,'Halfkg',${i})">
                  <div class="product-remove">
                      <i class="fa fa-trash" aria-hidden="true"></i>
                      <button class="remove" onclick=RemoveBTM()>Remove</button>
                  </div>
              </div>
          </div>`
            }
            if (QuantityFromIceCream[i].brand == 'Pretzel') {
                var cartRowContents =
                    `<div class="product">
          <img src="../image/sauce2.jpeg">
          <div class="product-info">
              <h3 class="product-name">Pretzel</h3>
                  <h2 class="product-price-1kg">2.00$ - 30ML</h2>
                  <p class="product-quantity-1kg">Qnt: <input class="product-quantity-1kg-input" type="number" min="1" id="${i + 'Onekg'}"  onclick="UpdateCart(true,this,'Onekg',${i})">
                  <h2 class="product-price-Halfkg">3.00$ - 50ML</h2>
                  <p class="product-quantity-Halfkg">Qnt: <input class="product-quantity-Halfkg-input" type="number" min="1" id="${i + 'Halfkg'}"  onclick="UpdateCart(true,this,'Halfkg',${i})">
                  <div class="product-remove">
                      <i class="fa fa-trash" aria-hidden="true"></i>
                      <button class="remove" onclick=RemoveBTM()>Remove</button>
                  </div>
              </div>
          </div>`
            }
            if (QuantityFromIceCream[i].brand == 'Pecan') {
                var cartRowContents =
                    ` <div class="product">
          <img src="../image/pecan.jpg">
          <div class="product-info">
              <h3 class="product-name">Pecan</h3>
                  <h2 class="product-price-1kg">1.00$ - 20GR</h2>
                  <p class="product-quantity-1kg">Qnt: <input class="product-quantity-1kg-input" type="number" min="1" id="${i + 'Onekg'}"  onclick="UpdateCart(true,this,'Onekg',${i})">
                  <h2 class="product-price-Halfkg">2.00$ - 50GR</h2>
                  <p class="product-quantity-Halfkg">Qnt: <input class="product-quantity-Halfkg-input" type="number" min="1" id="${i + 'Halfkg'}"  onclick="UpdateCart(true,this,'Halfkg',${i})">
                  <div class="product-remove">
                      <i class="fa fa-trash" aria-hidden="true"></i>
                      <button class="remove" onclick=RemoveBTM()>Remove</button>
                  </div>
              </div>
          </div>`
            }
            if (QuantityFromIceCream[i].brand == 'Candies') {
                var cartRowContents =
                    `<div class="product">
          <img src="../image/candys.jpg">
          <div class="product-info">
              <h3 class="product-name">Candies</h3>
                  <h2 class="product-price-1kg">1.00$ - 20GR</h2>
                  <p class="product-quantity-1kg">Qnt: <input class="product-quantity-1kg-input" type="number" min="1" id="${i + 'Onekg'}"  onclick="UpdateCart(true,this,'Onekg',${i})">
                  <h2 class="product-price-Halfkg">2.00$ - 50GR</h2>
                  <p class="product-quantity-Halfkg">Qnt: <input class="product-quantity-Halfkg-input" type="number" min="1" id="${i + 'Halfkg'}"  onclick="UpdateCart(true,this,'Halfkg',${i})">
                  <div class="product-remove">
                      <i class="fa fa-trash" aria-hidden="true"></i>
                      <button class="remove" onclick=RemoveBTm()>Remove</button>
                  </div>
              </div>
          </div>`
            }
            if (QuantityFromIceCream[i].brand == 'White') {
                var cartRowContents =
                    `<div class="product">
          <img src="../image/white chocolate.jpg">
          <div class="product-info">
              <h3 class="product-name">White</h3>
                  <h2 class="product-price-1kg">2.00$ - 30GR</h2>
                  <p class="product-quantity-1kg">Qnt: <input class="product-quantity-1kg-input" type="number" min="1" id="${i + 'Onekg'}"  onclick="UpdateCart(true,this,'Onekg',${i})">
                  <h2 class="product-price-Halfkg">3.00$ - 50GR</h2>
                  <p class="product-quantity-Halfkg">Qnt: <input class="product-quantity-Halfkg-input" type="number" min="1" id="${i + 'Halfkg'}"  onclick="UpdateCart(true,this,'Halfkg',${i})">
                  <div class="product-remove">
                      <i class="fa fa-trash" aria-hidden="true"></i>
                      <button class="remove" onclick=RemoveBTM()>Remove</button>
                  </div>
              </div>
          </div>`
            }
            cartRow.innerHTML = cartRowContents
            cartItems.append(cartRow)
            cartRow.getElementsByClassName('product-remove')[0].addEventListener('click', removeCartItem)
            document.getElementById(i + 'Onekg').value = OneKg;
            document.getElementById(i + 'Halfkg').value = HalfKg;
           // document.getElementById(i + 'Onekg').click();
        }
    }
}
//Initiating 'Our Products' page by stored values
function initiateProducts() {
    document.addEventListener('load', loadShoppingCartItemsByUser())
}
//Initiating 'My Cart' page by stored values
function initiateCart() {
   window.page='shoppingCart';
    if (document.readyState == 'loading') {
        document.addEventListener('DOMContentLoaded', RemoveBTM)
        document.addEventListener('DOMContentLoaded', addItemToCart)
    } else {
        var quantityInputs1KG = document.getElementsByClassName('product-quantity-1kg-input')
    for (var i = 0; i < quantityInputs1KG.length; i++) {
        var input = quantityInputs1KG[i]
        input.addEventListener('change', quantityChanged)
    }
    loadShoppingCartItemsByUser();
        RemoveBTM()
       
    }
}
//Restores values from stored array to the html content
function UpdateFromLastCart() {
    
    for (var i = 0; i < 8; i++) {
        const OneKg = SpecificIceCream[i].Onekg;
        const HalfKg = SpecificIceCream[i].Halfkg;
        document.getElementById('quantity' + (2 * i + 1)).value = OneKg;
        document.getElementById('quantity' + (2 * i + 2)).value = HalfKg;
    }
    document.getElementById('totalPriceText').value = updateTotalPriceData();
}
//Removing items from cart main function
function RemoveBTM() {
    var removeCartBtm = document.getElementsByClassName('remove')
    for (var i = 0; i < removeCartBtm.length; i++) {
        var button = removeCartBtm[i]
        button.addEventListener("click", removeCartItem)
    }
    
}
//Removing items from cart by event clicked
function removeCartItem(event) {
    var buttonClicked = event.target
    var iceCreamRemoved = buttonClicked.parentElement.parentElement.children[0].innerText
    for (var i = 0; i < 8; i++) {
        if (QuantityFromIceCream[i].brand == iceCreamRemoved) {
            QuantityFromIceCream[i].Onekg = 0
            QuantityFromIceCream[i].Halfkg = 0
            var JSONreadyUsers = JSON.stringify(QuantityFromIceCream);
            localStorage.setItem('QuantityFromIceCream', JSONreadyUsers);
        }
    }
    buttonClicked.parentElement.parentElement.parentElement.remove()
    updateShoppingCart()
    UpdateCart()
}
//Changing quantity in 'My Cart' page
function quantityChanged(event) {
    var input = event.target
    if (input.value <= 0 || isNaN(input.value)) {
        input.value = 1
    }
   
    
}
function updateTotalPriceData(){
    var sum1 = 0;
    sum1 = QuantityFromIceCream.reduce((sum,item) =>{
       return  sum + (brandPrices[item.brand].KgPrice * item.Onekg) + (brandPrices[item.brand].halfKGPrice* item.Halfkg)
    },0)
    console.log(sum1);
    return sum1;
}
//Update cart in 'My Cart'
function UpdateCart(quantityChanged,target,type,idx) {
    var cartContainer = document.getElementsByClassName('products')[0];
    var allproducts = cartContainer.getElementsByClassName('product');
    var totalprice = 0;
    for (var i = 0; i < allproducts.length; i++) {
        var CartProduct = allproducts[i];
        var price1kgProduct = CartProduct.getElementsByClassName('product-price-1kg')[0];
        var quantity1kgProduct = CartProduct.getElementsByClassName('product-quantity-1kg-input')[0];
        var price1kgNumber = parseFloat(price1kgProduct.innerText.replace('$ - 1KG', ''));
        var quantity1kg = quantity1kgProduct.value;
        var priceHalfkgProduct = CartProduct.getElementsByClassName('product-price-Halfkg')[0];
        var quantityHalfkgProduct = CartProduct.getElementsByClassName('product-quantity-Halfkg-input')[0];
        var priceHalfkgNumber = parseFloat(priceHalfkgProduct.innerText.replace('$ - 0.5KG', ''));
        var quantityHalfkg = quantityHalfkgProduct.value;
        totalprice = totalprice + (price1kgNumber * quantity1kg) + (priceHalfkgNumber * quantityHalfkg);
    }
    totalprice = Math.round(totalprice * 100) / 100
    document.getElementsByClassName('cartTotaPrice')[0].innerText = updateTotalPriceData() + '$';
    localStorage.setItem('CartTotalPrice', totalprice);
    if(quantityChanged){
        console.log(target);
        QuantityFromIceCream[idx][type]=+target.value;
        updateShoppingCart();
    }
    //()
    
}
// Find out the cart items from localStorage
$(document).ready(function () {

    if (localStorage.getItem('cart') == null) {
        var cart = {};
    } else {
        cart = JSON.parse(localStorage.getItem('cart'));
        updateCart(cart);
    }


    // If the add to cart button is clicked, add/increment the item
    $('.cart').click(function () {
        var idstr = this.id.toString();
        if (cart[idstr] != undefined) {
            cart[idstr] = cart[idstr] + 1;
        } else {
            cart[idstr] = 1;
        }
        updateCart(cart);

    });
    //Add Popover to cart
    $('#popcart').popover();
    updatePopover(cart)


    function updatePopover(cart) {
        // console.log('we are inside pop over function')
        var popstr = "";
        var i = 1
        popstr = popstr + "<h5>Cart for your items in my shopping cart</h5>"
        for (var item in cart) {
            popstr = popstr + "<b>" + i + "</b>" + " "
            popstr = popstr + "<u>" + document.getElementById('name' + item).innerHTML + "</u>" + " " + 'Qty:' + cart[item] + '<br>';
            i = i + 1;
        }
        // console.log('popstr')
        popstr = popstr + "<a href='/shop/checkout'><button class='btn btn-primary' id = 'cheackout'>CheckOut</button></a>  <button class='btn btn-primary' onclick='clearCart()' id = 'clearCart'>Clear-Cart</button> "
        document.getElementById("popcart").setAttribute('data-content', popstr);
        $('#popover').popover('show');
    }

    function clearCart() {
        cart = JSON.parse(localStorage.getItem('cart'));
        // console.log("Hello:"+ cart);

        for (var item in cart) {
            // console.log(item)
            // document.getElementById('div' + item).innerHTML = 'hi';  
            document.getElementById('div' + item).innerHTML = '<button id="' + item + '" class="btn btn-primary cart">Add To Cart</button>'
        }
        localStorage.clear();
        cart = {};
        updateCart(cart);
    }


    function updateCart(cart) {
        var sum = 0;
        for (var item in cart) {
            sum = sum + cart[item];
            document.getElementById('div' + item).innerHTML = "<button id='minus" + item + "' class='btn btn-primary minus'>-</button> <span id='val" + item + "''>" + cart[item] + "</span> <button id='plus" + item + "' class='btn btn-primary plus'> + </button>";
        }
        localStorage.setItem('cart', JSON.stringify(cart));
        document.getElementById('cart').innerHTML = sum;
        // console.log(cart);
        updatePopover(cart)

    }
    // If plus or minus button is clicked, change the cart as well as the display value
    $('.divpr').on("click", "button.minus", function () {
        a = this.id.slice(7,);
        cart['pr' + a] = cart['pr' + a] - 1;
        cart['pr' + a] = Math.max(0, cart['pr' + a]);
        document.getElementById('valpr' + a).innerHTML = cart['pr' + a];
        updateCart(cart);
    });
    $('.divpr').on("click", "button.plus", function () {
        a = this.id.slice(6,);
        cart['pr' + a] = cart['pr' + a] + 1;
        document.getElementById('valpr' + a).innerHTML = cart['pr' + a];
        updateCart(cart);
    });
});
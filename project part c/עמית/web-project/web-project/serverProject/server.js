const express = require("express");
const bodyParser = require("body-parser");
const app = express();
const connection = require('./db')

// parse requests of content-  type: application/json  app.use(bodyParser.json());
// parse requests of content-type: application/x-www-form-urlencoded  
app.use(bodyParser.urlencoded({
    extended: true
}));
app.use(bodyParser.json());
app.use(express.static('public'));
// simple route
app.get("/", (req, res) => {
    res.json({ message: "Welcome to web course  example application." });
});

app.post('/login',function (req, res) {
    try {
        const { email, password } = req.body;
        console.log(req.body);
        const sql = `SELECT * FROM users where email=? and password=?`;   
        connection.query(sql,[email,password],function (err,result,fields){
                if(err){
                    res.status(500).json({status:500,error:err});
                    return;
                }
                if(result.length === 0 ){
                    res.redirect('/HTML/Log_In_Page.html?message=UserNotFound')
                   // res.status(403).json({status:403,error:'USER NOT FOUND'});
                    return;
                }
                res.redirect('/HTML/Our%20Menu.html?userID='+result[0].id);
            })
    } catch (error) {
        res.send({ status: 400, error: error });
    }
});

app.post('/createShoppingCart',function(req,res){   
    try {
        let { userID, selectedProducts } = req.body;
        console.log(req.body);
        selectedProducts = JSON.stringify(selectedProducts);
        const sql = `INSERT INTO shopping_cart (userID,selectedProducts) VALUES (?,?)`;   
        connection.query(sql,[userID,selectedProducts],function (err,result,fields){
            if(err){
                res.send({status:400,error:err});
                return;
            }
            res.json(result.insertId)
        })
    } catch (error) {
        res.send({ status: 400, error: error });
    }
});

app.put('/updateShoppingCart',function(req,res){
    try {
        let { userID, cartID,selectedProducts } = req.body;
        selectedProducts = JSON.stringify(selectedProducts);
        const sql = `UPDATE shopping_cart SET selectedProducts=? WHERE userID=? AND id=?;`;
        connection.query(sql,[selectedProducts,userID,cartID],function (err,result,fields){
            if(err){
                res.json({status:400,error:err});
                return;
            }
            res.json(cartID);

        });

    } catch (error) {
        
    }
})

app.get('/getShoppingCartByUser',function (req,res){
    try {
        let { userID } = req.query;
        console.log(userID)
        const sql = `SELECT * FROM shopping_cart WHERE userID=?`;   
        connection.query(sql,[userID],function (err,result,fields){
            if(err){
                res.send({status:400,error:err});
                return;
            }
            res.send(result)
        })
        
    } catch (error) {
        
    }
})





app.post('/createUser', function (req, res) {
    try {
        const { email, password, firstName, lastName, phone } = req.body;
        console.log(req.body);
        const sql = `INSERT INTO users (email,password,firstName,lastName,phone) VALUES (?,?,?,?,?)`;   
        connection.query(sql,[email,password,firstName,lastName,phone],function (err,result,fields){
                if(err){
                    res.send({status:400,error:err});
                    return;
                }
                res.send("ok")
            })
    } catch (error) {
        res.send({ status: 400, error: error });
    }
});


// set port, listen for requests
app.listen(3000, () => {
    console.log("Server is running on port 3000."
    );
});

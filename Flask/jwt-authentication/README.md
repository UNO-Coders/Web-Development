## JWT Authentication in Flask

* What is JWT?

    > JSON Web Token is a proposed Internet standard for creating data with optional signature and/or optional encryption whose payload holds JSON that asserts some number of claims. The tokens are signed either using a private secret or a public/private key.

* How is it used?

    > Generally when an user logs in a webpage, the client requests a JWT token based on the user credentials.

    > The Server generates the token and sends it back to the client.

    > The Client then uses this token to request any resource from the API.

    > Without the token the Server marks all requests to protected routes as unauthorized.

* How can the client send the token for each request?

    > The Recommended practice is to use the `Authorization` header while requesting the resource.

    > Example: `Authorization: Bearer <token_here>`


### Usage
```
SERVER SIDE

# Install the necessary packages
pip install -r requirements.txt

# Run the flask app
python app.py
```

```
CLIENT SIDE

headers = {
    "Authorization": "Bearer "+token
}

axios.get(protected_url, headers=headers)
        .then(data => {
            console.log(data);
        })
        .catch(error => {
            console.log(error);
        })
```
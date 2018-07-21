# alienchain

Today's blockchain frameworks are built with assets/tokens in mind thereby making it difficult for non-asset based project to integrate.
AlienChain seeks to change this by introducing a non-asset based blockchain framework with APIs to make developer work easier.

### Instructions to run

We have a simple chat app you will love to play around with

 - Install Dependencies,

    ```sh
    >>> pip3 install -r requirements.txt
    ```

- Start a blockchain node server,

    ```sh
    >>> python server/node_server.py
    ```

- Run our application,

    ```sh
    >>> python client/run_app.py
    ```

The application should be up and running at [http://localhost:5000](http://localhost:5000).
# TODO 
 - Adding tags to transactions for easy grouping :heavy_check_mark:
 - Implement logging :heavy_check_mark:
 - Integrate Mongo DB :heavy_check_mark:
 - Create SDKs

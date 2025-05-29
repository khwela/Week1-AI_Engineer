crypto_data = {
    "Bitcoin": {
        "price": 45000,
        "market_cap": 850000000000,
        "volume": 30000000000,
        "description": "Bitcoin is a decentralized digital currency, without a central bank or single administrator, that can be sent from user to user on the peer-to-peer bitcoin network without the need for intermediaries."
    },
    "Ethereum": {
        "price": 3000,
        "market_cap": 350000000000,
        "volume": 20000000000,
        "description": "Ethereum is a decentralized platform that enables smart contracts and decentralized applications to be built and run without any downtime, fraud, control, or interference."
    },
    "dogecoin": {
        "price": 0.25,
        "market_cap": 32000000000,
        "volume": 1500000000,
        "description": "Dogecoin is a cryptocurrency that started as a joke but has gained a large following and is used for tipping and charitable donations."
    },
    "Litecoin": {
        "price": 150,
        "market_cap": 10000000000,
        "volume": 500000000,
        "description": "Litecoin is a peer-to-peer cryptocurrency that enables instant, near-zero cost payments to anyone in the world."
    },
    "Ripple": {
        "price": 0.5,
        "market_cap": 25000000000,
        "volume": 1000000000,
        "description": "Ripple is a digital payment protocol that operates as a real-time gross settlement system, currency exchange, and remittance network."
    },
    "Cardano": {
        "price": 1.2,
        "market_cap": 40000000000,
        "volume": 2000000000,
        "description": "Cardano is a blockchain platform for smart contracts, aiming to provide a more secure and scalable way to build decentralized applications."
    },
    "Polkadot": {
        "price": 25,
        "market_cap": 30000000000,
        "volume": 1000000000,
        "description": "Polkadot is a multi-chain network that enables different blockchains to transfer messages and value in a trust-free fashion."
    }
}

print("Welcome to the Crypto Chatbot!")
print("--------------------------------------------------------------------")
def get_crypto_info(crypto_name):
    crypto_name = crypto_name.capitalize()
    if crypto_name in crypto_data:
        data = crypto_data[crypto_name]
        return (f"{crypto_name}:\n"
                f"Price: ${data['price']}\n"
                f"Market Cap: ${data['market_cap']}\n"
                f"Volume: ${data['volume']}\n"
                f"Description: {data['description']}")
    else:
        return "Sorry, I don't have information on that cryptocurrency."
    
    
while True:
    crypto_name = input("Enter a cryptocurrency name (or type 'exit' to quit): ").strip()
    print("--------------------------------------------------------------------")
    if crypto_name.lower() == 'exit':
        print("Goodbye!")
        break
    response = get_crypto_info(crypto_name)
    print(response)
    
    print("--------------------------------------------------------------------")
    if crypto_name in crypto_data:
        coin = crypto_data[crypto_name]
        print(f"{crypto_name.capitalize()} is a popular cryptocurrency with a current price of ${coin['price']}.")
        print(f"About {crypto_name.capitalize()}: {coin['description']}")
    else:
        matched = False
        for name in crypto_data:
            if crypto_name.lower() in name.lower():  # Case-insensitive partial match
                coin = crypto_data[name]
                print(f"Did you mean {name.capitalize()}?")
                print(f"{name.capitalize()} is a popular cryptocurrency with a current price of ${coin['price']}.")
                print(f"About {name.capitalize()}: {coin['description']}")
                matched = True
                break
        if not matched:  # This block should only execute if no match is found
            print("Sorry, I couldn't find any information on that cryptocurrency. Try 'Bitcoin', 'Ethereum', 'Dogecoin', 'Litecoin', 'Ripple', 'Cardano', or 'Polkadot'.")
import functions




def main():
    S = 100
    K = 105
    T = .5
    r = 0.02
    vol = 0.2
    call_price = functions.black_scholes_call(S,K,T,r,vol)
    print(call_price)


if __name__ == "__main__":
    main()
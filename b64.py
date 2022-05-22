import argparse
import base64
import textwrap


def encode(input, urlsafe=False):
    print(input)
    if urlsafe:
        res = base64.urlsafe_b64decode(input.encode()).decode()
    else:
        res = base64.b64encode(input.encode()).decode()
    return res


def decode(input, urlsafe=False):
    input = input + '=' * (-len(input) % 4)
    if urlsafe:
        res = base64.urlsafe_b64decode(input).decode()
    else:
        res = base64.b64decode(input).decode()
    return res


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Base64 encode/decode',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent(
            '''Example:
            '''
        )
    )
    parser.add_argument('input', type=str, help='Input')
    parser.add_argument('-e', '--encode', action='store_true', help='Encode input')
    parser.add_argument('-d', '--decode', action='store_true', help='Decode input')
    parser.add_argument('-u', '--urlsafe', action='store_true', help='URL safe mode')

    args = parser.parse_args()

    if args.encode:
        print(':::::base64 Encode:::::')
        try:
            encoded = encode(args.input, urlsafe=args.urlsafe)
            print(encoded)
        except Exception as e:
            print('[!] Error')
            print(e)

    if args.decode:
        print(':::::base64 Decode:::::')
        try:
            decoded = decode(args.input, urlsafe=args.urlsafe)
            print(decoded)
        except Exception as e:
            print('[!] Error')
            print(e)





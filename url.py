import argparse
import textwrap
import urllib.parse as parse


def encode(input):
    res = parse.quote(input)
    return res


def decode(input):
    res = parse.unquote(input)
    return res


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='URL encode/decode',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent(
            '''Example:
            '''
        )
    )
    parser.add_argument('input', type=str, help='Input')
    parser.add_argument('-e', '--encode', action='store_true', help='Encode input')
    parser.add_argument('-d', '--decode', action='store_true', help='Decode input')

    args = parser.parse_args()

    if args.encode:
        print(':::::URL Encode:::::')
        try:
            encoded = encode(args.input)
            print(encoded)
        except Exception as e:
            print('[!] Error')
            print(e)

    if args.decode:
        print(':::::URL Decode:::::')
        try:
            decoded = decode(args.input)
            print(decoded)
        except Exception as e:
            print('[!] Error')
            print(e)





import argparse
import binascii
import textwrap


def encode(input, codec='utf-8'):
    res = binascii.hexlify(input.encode(codec)).decode()
    return res


def decode(input, codec='utf-8'):
    res = binascii.unhexlify(input.encode(codec)).decode()
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
    parser.add_argument('-c', '--codec', type=str, default='utf-8', help='Codec to use')
    parser.add_argument('-e', '--encode', action='store_true', help='Encode input')
    parser.add_argument('-d', '--decode', action='store_true', help='Decode input')

    args = parser.parse_args()

    if args.encode:
        print(':::::hex Encode:::::')
        try:
            encoded = encode(args.input, args.codec)
            print(encoded)
        except Exception as e:
            print('[!] Error')
            print(e)

    if args.decode:
        print(':::::hex Decode:::::')
        try:
            decoded = decode(args.input, args.codec)
            print(decoded)
        except Exception as e:
            print('[!] Error')
            print(e)





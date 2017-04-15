# Phonetic
A 5-minute-created program to speak using the phonetic alphabet

## Usage

```
./phonetic.py -e '<text to encode>'
./phonetic.py -d '<text to decode>'
```

## Encode

Input:

```
python phonetic.py -e "Hello My Friend"
```

Output:

```
Hotel Echo Lima Lima Oscar - Mike Yankee - Foxtrot Romeo India Echo November Delta
```

## Decode

Input:

```
python phonetic.py -d "Hotel Echo Lima Lima Oscar - Mike Yankee - Foxtrot Romeo India Echo November Delta"
```

Output:

```
HELLO - MY - FRIEND
```

## Testing

The directory *test* contains a script which Tests the most basic properties:

* Decode(Encode(x)) = x
* Encode(Decode(x)) = x

As an example:

```
./testing.sh "Hello My Friend" "Hotel Echo Lima Lima Oscar"
Decoding the encode of : Hello My Friend
Encode : Hotel Echo Lima Lima Oscar - Mike Yankee - Foxtrot Romeo India Echo November Delta
Decode : HELLO - MY - FRIEND
Encoding the decode of ; Hotel Echo Lima Lima Oscar
Decode : HELLO
Encode : Hotel Echo Lima Lima Oscar
```

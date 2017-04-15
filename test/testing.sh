encode()
{
	python ../phonetic.py -e "$1"
}

decode()
{
	python ../phonetic.py -d "$1"
}

usage()
{
	echo "testing.sh <clear message> <decoded_message>"
}

[ $# -lt 2 ] && usage && exit;

echo "Decoding the encode of : ""$1"

e=`encode "$1"`;
d=`decode "$e"`;

echo "Encode : ""$e"
echo "Decode : ""$d"

echo "Encoding the decode of ; ""$2"
d=`decode "$2"`;
e=`encode "$d"`;
echo "Decode : ""$d"
echo "Encode : ""$e"

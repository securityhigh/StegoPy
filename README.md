# StegoPy
**Статья со скриншотами на OverNull - https://onull.nl/stegopy**

## English

###### Theory
StegoPy - Steganography with Python3 LSB algorithm with some improvements.
The cryptography algorithm can choose the balance itself.
A blue channel of pixels is used for encoding. Pixels are used, from x|y = 0 and from left to right.

**Balance** - the number of least significant bits of the pixel that are involved in the encoding. The maximum is 4, the minimum is 1. With increasing cryptographic strength and the number of pixels involved decreases. Therefore, I advise you to use 1. And if the text does not fit, but you still want to cram the large text into a small image, then you can use 2 or 3.

The peculiarity of the balance system is that for a certain text, balance 3 can be more stable than 1. I also examine balances on the same text, I noticed that often the pixels do not even change, mainly with a balance of 1. But it also depends on the text.

When encoding text in an image, it is pre-encrypted with the DES algorithm, so no matter how you try, you cannot encode the same text with the same key.

After encoding, the key will be saved in the ** key.dat ** file, the image with the text in the file ** out.png **
The key consists of three parts, for example:
**2$400$KJhkiGlGKkghk/FffdD=**

Shared by the character '$'. First - 2 is the balance. The second - 400 is the number of pixels involved and at the end is the key to the DES cipher. Over time, pixel randomization will be added, which will make the algorithm even more stable, as well as change the structure of the key.


###### Install
Requirements:
```
> git clone https://github.com/eBind/StegoPy
> cd StegoPy
> pip3 install -r requirements.txt
```

Started in Linux:
```
> ./stegopy.py [arguments]
```

In Windows or Termux:
```
> python3 stegopy.py [arguments]
```

###### Encoding
```
> ./stegopy.py -e in.jpg data.txt
```

_-e_ - action type, encoding
_in.jpg_ - target image
_data.txt_ - file with your text

Enter a need balance.
Out image _out.png_, key in _key.dat_

###### Deconding
```
> ./stegopy.py -d out.png
```

_-d_ - action type, decoding
_out.png_ - encoded image

Enter a key.
Decoded data saved in _out.txt_

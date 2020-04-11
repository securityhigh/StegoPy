# StegoPy
## Русский, English on down

**Статья со скриншотами на OverNull - https://onull.nl/stegopy**

###### Теория
StegoPy - Стеганография с Python3 алгоритмом LSB некоторыми улучшениями.
Особенность моей реализации алгоритма в том, что криптограф может сам выбирать баланс, которым будет кодироваться текст в изображение.
Для кодирования используется голубой канал пикселя. Используются пиксели, от x/y = 0 и последовательно слева направо.

**Balance** - количество младших битов пикселя, которые задействуются в кодировании. Максимум - 4, минимум - 1. С увеличением снижается криптостойкость и количество задействованных пикселей. Поэтому я советую использовать 1. И если текст не вмещается, а таки хочется запихать большой текст в маленькое изображение, то можно использовать 2 или 3.

Особенность системы баласнов заключается в том, что для определенного текста баланс 3 может быть более стойким, нежели 1. Также исследую балансы на одном и том же тексте, я заметил, что зачастую пиксели даже не изменяются, в основном при балансе равным 1. Но все равно это зависит от текста.

При кодировании текста в изображении, он предварительно шифруется алгоритмом DES, поэтому как бы вы не пытались, вы не сможете один и тот же текст закодировать с одним и тем же ключом.

После кодирования ключ будет сохранен в файле **key.dat**, изображение с текстом в файле **out.png**
Ключ состоит из трех частей, например:
**2$400$KJhkiGlGKkghk/FffdD=**

Делится символом '$'. Первая - 2 это баланс. Второе - 400 это количество задействованных пикселей и в конце это ключ от шифра DES. Со временем будет добавлена рандомизация пикселей, что сделает алгоритм еще более стойким, а также изменит строение ключа.


###### Установка
Зависимости:
```
> git clone https://github.com/eBind/StegoPy
> cd StegoPy
> pip3 install -r requirements.txt
```

Запуск в Linux:
```
> ./stegopy.py [arguments]
```

В Windows, Termux:
```
> python3 stegopy.py [arguments]
```

###### Кодирование
```
> ./stegopy.py -e in.jpg data.txt
```

_-e_ - тип действия
_in.jpg_ - целевое изображение
_data.txt_ - файл с данными, которые нужно закодировать в изображение выше

Далее вводим нужный баланс.
Выходное изображение _out.png_, ключ в _key.dat_

###### Декодирование
```
> ./stegopy.py -d out.png
```

_-d_ - тип действия
_out.png_ - целевое изображение

Далее вводим ключ.
Декодированные данные будут сохранены в _out.txt_



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

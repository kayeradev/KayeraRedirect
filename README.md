
![KayeraOkey](https://i.pinimg.com/originals/31/24/73/312473c90b9906c7bcea7d820b9e5705.gif)

# KayeraRedirect

https://kayera.software/discord

### Nedir?

Discord sunucunuzda, moderasyon ekibinize mümkün olan en iyi seviyede yardımcı olacak bir tooldur. Discord botunuzu kullanır. Temel amaç, yanlış kanal kullanımını minimum düzeye indirmektir.

## Özellikler

- Python 3.0+
- Discord'un kendi Python kütüphanelerini kullanır.
- Geliştirilmesi ve değiştirilmesi kolay.
- Anlaşılabilir ve detaysız olmasına karşın şık bir tasarım mevcut.
- Koddaki çoğu kısım not satırı şeklinde açıklandı, yani öğrenmek için birebir.
- Özel emoji destekler.
- Tamamen customizable.
- Mümkün olduğunca az watermark kullanıldı.


- https://kayera.uk/ kısımlarını değiştirmeden kullanmanızı rica ediyorum.

## Nasıl indirilir?

```bash
$ git clone https://github.com/kayeradev/KayeraRedirect.git
$ dir KayeraRedirect
$ pip install -r requirements.txt
$ python3 main.py
```

## Bot nasıl oluşturacağım?

- **BOT_TOKENINIZ** yazan kısma, herhangi bir botunuzun TOKEN değerini girmeniz gerekiyor. Bunu almak için aşağıdaki adımları takip edebilirsiniz:
```bash
1- https://discord.com/developers/applications adresine giriş yapın.
2- Eğer bir uygulamanız var ise üstüne tıklayın, eğer yok ise sağ üstten oluşturabilirsiniz.
3- Sol taraftan Bot kısmına gelin ve eğer bot oluşturmadıysanız oluşturun.
4- Reset Token'a basın.
5- Token'ı kopyalayın ve 5. satırdaki "BOT_TOKENINIZ" bölümüne yazın. Unutmayın, başında ve sonunda tırnak işareti olmalı.
(Tokenınız KAYERA diyelim. DISCORD_TOKEN = "KAYERA" şeklinde gözükmeli.
```

## Botu nasıl davet edeceğim?

```bash
1- https://discord.com/developers/applications adresine giriş yapın.
2- Oluşturduğunuz aplikasyonu seçin.
3- Sol taraftan OAuth2 kısmına gelin.
4- Biraz aşağı inin ve "bot" seçeneğini aktifleştirin.
5- Aşağı inin ve aşağıdakileri aktifleştirin:
Send Messages (Mesaj Gönder)
Manage Messages (Mesajları Yönet)
Send Messages in Threads (Başlıklara Mesaj Gönder)
6- Aşağı inin ve sayfanın en altındaki linki kopyalayın.
7- Tarayıcınıza yapıştırın ve davet edeceğiniz sunucuyu seçip botu davet edin. 
8- Artık kodu sunucunuzda veya localde çalıştırdıktan sonra botu kullanabilirsiniz.
```

## Nasıl kullanılır?

Sistemi kullanacak yetkilinin **Mesajları Yönetme** yetkisine sahip olması gereklidir. Mesajları yöentme yetkisine sahip olan yetkili, herhangi bir kanalda gönderilen bir mesajı yanıtlayarak, sadece belirtilen emojiyi gönderirse ve hemen ardından bir kanal etiketlerse, yanıtlanan mesaj, belirtilen kanala yönlendirilir.

![Bir Örnek](https://cdn.discordapp.com/attachments/1238418123179425793/1300135809365839932/image.png?ex=671fbd54&is=671e6bd4&hm=54dd289e5b2d618a57fe506446463d8ee84eefb186c84a2a8d2d35ff1ea9f047&)

## License

The MIT License (MIT)

Copyright (c) 2024-2025 Kayera

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

# <ruby>JavaScript<rt>ジャバスクリプト</rt></ruby>を<ruby>始<rt>はじ</rt></ruby>める<ruby>前<rt>まえ</rt></ruby>に

**<ruby>留学生<rt>りゅうがくせい</rt></ruby>のためのJavaScript<ruby>学習<rt>がくしゅう</rt></ruby>ガイド：Webを<ruby>動<rt>うご</rt></ruby>かす<ruby>魔法<rt>まほう</rt></ruby>を<ruby>学<rt>まな</rt></ruby>ぼう**

<ruby>留学生<rt>りゅうがくせい</rt></ruby>のみなさん、こんにちは！ プログラミングの<ruby>世界<rt>せかい</rt></ruby>へようこそ。

みなさんが<ruby>毎日<rt>まいにち</rt></ruby><ruby>使<rt>つか</rt></ruby>っているスマートフォンやパソコンの<ruby>画面<rt>がめん</rt></ruby>。ボタンを<ruby>押<rt>お</rt></ruby>すとメニューが<ruby>出<rt>で</rt></ruby>てきたり、<ruby>地図<rt>ちず</rt></ruby>が<ruby>動<rt>うご</rt></ruby>いたりしますね。これはすべて「JavaScript（ジャバスクリプト）」という<ruby>言葉<rt>ことば</rt></ruby>が<ruby>命令<rt>めいれい</rt></ruby>を<ruby>出<rt>だ</rt></ruby>して<ruby>動<rt>うご</rt></ruby>かしています。

このガイドでは、<ruby>自分<rt>じぶん</rt></ruby>でウェブページを<ruby>動<rt>うご</rt></ruby>かせるようになるための<ruby>基礎<rt>きそ</rt></ruby>をやさしく<ruby>解説<rt>かいせつ</rt></ruby>します。それがJavaScriptの<ruby>基本<rt>きほん</rt></ruby>だからです。

> (<ruby>参考<rt>さんこう</rt></ruby>) <ruby>現在<rt>げんざい</rt></ruby>のJavaScriptは、ウェブページの<ruby>操作<rt>そうさ</rt></ruby>だけでなく、いろいろな<ruby>用途<rt>ようと</rt></ruby>に使えるプログラム<ruby>言語<rt>げんご</rt></ruby>になっています。しかし、<ruby>今<rt>いま</rt></ruby>でも、ブラウザ<ruby>上<rt>じょう</rt></ruby>で<ruby>活躍<rt>かつやく</rt></ruby>しています。

***

## I. <ruby>私<rt>わたし</rt></ruby>たちの<ruby>舞台<rt>ぶたい</rt></ruby>：WWW（ワールド・ワイド・ウェブ）

まず、javaScriptの<ruby>活躍<rt>かつやく</rt></ruby>の<ruby>舞台<rt>ぶたい</rt></ruby>、WWW（ワールド・ワイド・ウェブ）とは<ruby>何<rt>なに</rt></ruby>かについて、<ruby>説明<rt>せつめい</rt></ruby>しましょう。

**WWW（ワールド・ワイド・ウェブ）** は、<ruby>世界中<rt>せかいじゅう</rt></ruby>のコンピュータが「クモの<ruby>巣<rt>す</rt></ruby>（Web）」のようにつながって、<ruby>情報<rt>じょうほう</rt></ruby>を<ruby>共有<rt>きょうゆう</rt></ruby>する<ruby>仕組<rt>しく</rt></ruby>みのことです。

これを、**「<ruby>図書館<rt>としょかん</rt></ruby>」** に<ruby>例<rt>たと</rt></ruby>えて、やさしく<ruby>説明<rt>せつめい</rt></ruby>しますね。

### 1. 3つの<ruby>大切<rt>たいせつ</rt></ruby>な「<ruby>道具<rt>どうぐ</rt></ruby>」

WWWを<ruby>動<rt>うご</rt></ruby>かすために、3つの<ruby>主役<rt>しゅやく</rt></ruby>がいます。

* **Webブラウザ（お<ruby>客<rt>きゃく</rt></ruby>さん）**  
  ChromeやSafariなど、<ruby>私<rt>わたし</rt></ruby>たちがサイトを<ruby>見<rt>み</rt></ruby>るためのソフトです。「<ruby>本<rt>ほん</rt></ruby>を<ruby>読<rt>よ</rt></ruby>みたい<ruby>人<rt>ひと</rt></ruby>」です。
* **Webサーバ（<ruby>図書館<rt>としょかん</rt></ruby>のスタッフ）**   <ruby>世界中<rt>せかいじゅう</rt></ruby>のどこかにある、24<ruby>時間<rt>じかん</rt></ruby><ruby>動<rt>うご</rt></ruby>いているコンピュータです。「<ruby>本<rt>ほん</rt></ruby>を<ruby>管理<rt>かんり</rt></ruby>している<ruby>人<rt>ひと</rt></ruby>」です。
* **HTML（<ruby>本<rt>ほん</rt></ruby>の<ruby>内容<rt>ないよう</rt></ruby>）**  
  ウェブサイトに<ruby>書<rt>か</rt></ruby>いてある<ruby>文章<rt>ぶんしょう</rt></ruby>や<ruby>写真<rt>しゃしん</rt></ruby>のデータです。これが「<ruby>本<rt>ほん</rt></ruby>」そのものです。

### 2. ウェブサイトが<ruby>表示<rt>ひょうじ</rt></ruby>されるまでの「4つのステップ」

あなたがブラウザでURLを<ruby>入力<rt>にゅうりょく</rt></ruby>してから、<ruby>画面<rt>がめん</rt></ruby>が<ruby>出<rt>で</rt></ruby>るまでの<ruby>流<rt>なが</rt></ruby>れを<ruby>見<rt>み</rt></ruby>てみましょう。

1. **リクエスト（<ruby>注文<rt>ちゅうもん</rt></ruby>）：**  
   あなたが「このページを<ruby>見<rt>み</rt></ruby>たい！」とURLをクリックします。これは<ruby>図書館<rt>としょかん</rt></ruby>のスタッフに「あの<ruby>本<rt>ほん</rt></ruby>を<ruby>貸<rt>か</rt></ruby>してください」と<ruby>頼<rt>たの</rt></ruby>むのと<ruby>同<rt>おな</rt></ruby>じです。

2. **<ruby>住所<rt>じゅうしょ</rt></ruby>の<ruby>確認<rt>かくにん</rt></ruby>（DNS）：**  
   インターネットの<ruby>世界<rt>せかい</rt></ruby>では、`google.com`のような<ruby>名前<rt>なまえ</rt></ruby>ではなく、<ruby>数字<rt>すうじ</rt></ruby>の<ruby>住所<rt>じゅうしょ</rt></ruby>（IPアドレス 例えば、"142.251.223.46" みたいな）で<ruby>場所<rt>ばしょ</rt></ruby>を<ruby>探<rt>さが</rt></ruby>します。

3. **レスポンス（<ruby>返事<rt>へんじ</rt></ruby>）：**  
   サーバがあなたのリクエストを<ruby>受<rt>う</rt></ruby>けて、HTMLなどのデータをあなたのブラウザに<ruby>送<rt>おく</rt></ruby>り<ruby>返<rt>かえ</rt></ruby>します。「はい、どうぞ！」と<ruby>本<rt>ほん</rt></ruby>を<ruby>渡<rt>わた</rt></ruby>してくれるイメージです。

4. **レンダリング（<ruby>組<rt>く</rt></ruby>み<ruby>立<rt>た</rt></ruby>て）：**  
   ブラウザが、<ruby>届<rt>とど</rt></ruby>いたHTMLデータを<ruby>読<rt>よ</rt></ruby>み<ruby>取<rt>と</rt></ruby>って、きれいなデザインに<ruby>組<rt>く</rt></ruby>み<ruby>立<rt>た</rt></ruby>てて<ruby>表示<rt>ひょうじ</rt></ruby>します。

### 3. WWWで<ruby>使<rt>つか</rt></ruby>われる「<ruby>魔法<rt>まほう</rt></ruby>の<ruby>言葉<rt>ことば</rt></ruby>」

ウェブの<ruby>世界<rt>せかい</rt></ruby>には、<ruby>共通<rt>きょうつう</rt></ruby>のルール（プロトコル）があります。

* **HTTP / HTTPS：**   <ruby>情報<rt>じょうほう</rt></ruby>をやり<ruby>取<rt>と</rt></ruby>りするときの「<ruby>言葉<rt>ことば</rt></ruby>のルール」です。
* **URL：**  
  ウェブサイトの「<ruby>住所<rt>じゅうしょ</rt></ruby>」です。<ruby>世界<rt>せかい</rt></ruby>に<ruby>一<rt>ひと</rt></ruby>つしかありません。

### まとめテーブル

| ITの<ruby>言葉<rt>ことば</rt></ruby> | <ruby>図書館<rt>としょかん</rt></ruby>での<ruby>例<rt>たと</rt></ruby>え                     | <ruby>役割<rt>やくわり</rt></ruby>                                                           |
| ------------------------------ | ------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------- |
| **クライアント**                     | <ruby>本<rt>ほん</rt></ruby>を<ruby>読<rt>よ</rt></ruby>みたい<ruby>人<rt>ひと</rt></ruby> | ブラウザでリクエストを<ruby>送<rt>おく</rt></ruby>る                                                  |
| **サーバ**                        | <ruby>図書館<rt>としょかん</rt></ruby>のスタッフ                                            | データを<ruby>保管<rt>ほかん</rt></ruby>して、<ruby>送<rt>おく</rt></ruby>り<ruby>返<rt>かえ</rt></ruby>す |
| **HTML**                       | <ruby>本<rt>ほん</rt></ruby>のページ                                                  | <ruby>文字<rt>もじ</rt></ruby>や<ruby>写真<rt>しゃしん</rt></ruby>のデータ                            |
| **URL**                        | <ruby>本<rt>ほん</rt></ruby>の<ruby>整理番号<rt>せいりばんごう</rt></ruby>                    | サイトがどこにあるか<ruby>教<rt>おし</rt></ruby>える                                                  |

いかがでしょうか？「<ruby>注文<rt>ちゅうもん</rt></ruby>して、<ruby>送<rt>おく</rt></ruby>ってもらって、<ruby>組<rt>く</rt></ruby>み<ruby>立<rt>た</rt></ruby>てる」。このシンプルな<ruby>流<rt>なが</rt></ruby>れがWWWの<ruby>正体<rt>しょうたい</rt></ruby>です。

「WWWは、<ruby>世界中<rt>せかいじゅう</rt></ruby>の<ruby>情報<rt>じょうほう</rt></ruby>をだれでも、どこでも<ruby>見<rt>み</rt></ruby>られるようにしたすごい<ruby>発明<rt>はつめい</rt></ruby>なんです。

***

## II. ウェブページを<ruby>作<rt>つく</rt></ruby>る「3つの<ruby>力<rt>ちから</rt></ruby>」：HTML・CSS・JavaScriptの<ruby>役割<rt>やくわり</rt></ruby>

ウェブページは、3つの<ruby>技術<rt>ぎじゅつ</rt></ruby>がチームワークを<ruby>発揮<rt>はっき</rt></ruby>してできています。これを「<ruby>家<rt>いえ</rt></ruby>づくり」に<ruby>例<rt>たと</rt></ruby>えてみましょう。

| 技術名        | 役割（やくわり）                                                  | 家づくりに例えると？                                                                                                       |
| ---------- | --------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| HTML       | <ruby>骨組<rt>ほねぐ</rt></ruby>み・<ruby>構造<rt>こうぞう</rt></ruby> | <ruby>柱<rt>はしら</rt></ruby>、<ruby>壁<rt>かべ</rt></ruby>、<ruby>床<rt>ゆか</rt></ruby>                                   |
| CSS        | <ruby>見<rt>み</rt></ruby>た<ruby>目<rt>め</rt></ruby>・デザイン    | ペンキの<ruby>色<rt>いろ</rt></ruby>、インテリア、<ruby>壁<rt>かべ</rt></ruby>に<ruby>貼<rt>は</rt></ruby>る<ruby>紙<rt>かみ</rt></ruby> |
| JavaScript | <ruby>動<rt>うご</rt></ruby>き・<ruby>機能<rt>きのう</rt></ruby>    | <ruby>電気<rt>でんき</rt></ruby>、<ruby>機械装置<rt>きかいそうち</rt></ruby>                                                     |

### JavaScriptの<ruby>役割<rt>やくわり</rt></ruby>：<ruby>電気<rt>でんき</rt></ruby>を<ruby>通<rt>とお</rt></ruby>すこと

HTMLとCSSだけでは、<ruby>家<rt>いえ</rt></ruby>は<ruby>完成<rt>かんせい</rt></ruby>しても「<ruby>電気<rt>でんき</rt></ruby>が<ruby>通<rt>とお</rt></ruby>っていない」<ruby>状態<rt>じょうたい</rt></ruby>です。HTMLとCSSだけのウェブページは、ただ<ruby>情報<rt>じょうほう</rt></ruby>を<ruby>表示<rt>ひょうじ</rt></ruby>するだけの、<ruby>動<rt>うご</rt></ruby>きのない「<ruby>紙<rt>かみ</rt></ruby>のポスター」のようなものです。

JavaScriptという<ruby>電気<rt>でんき</rt></ruby>が<ruby>通<rt>とお</rt></ruby>ることで、スイッチを<ruby>押<rt>お</rt></ruby>せばライトがつき、ドアの<ruby>前<rt>まえ</rt></ruby>に<ruby>立<rt>た</rt></ruby>てば<ruby>自動<rt>じどう</rt></ruby>ドアが<ruby>開<rt>ひら</rt></ruby>き、ボタンを<ruby>押<rt>お</rt></ruby>せばエレベーターが<ruby>動<rt>うご</rt></ruby>くようになります。ウェブページはユーザーと「<ruby>対話<rt>たいわ</rt></ruby>」ができる<ruby>便利<rt>べんり</rt></ruby>な<ruby>道具<rt>どうぐ</rt></ruby>に<ruby>変<rt>か</rt></ruby>わるのです。

***

## III. イベントとは

### 1. 「きっかけ」を<ruby>待<rt>ま</rt></ruby>っているコンピューター

<ruby>普段<rt>ふだん</rt></ruby>、ウェブページはただじっとしているだけに<ruby>見<rt>み</rt></ruby>えますが、<ruby>実<rt>じつ</rt></ruby>はあなたの<ruby>操作<rt>そうさ</rt></ruby>を **「<ruby>今<rt>いま</rt></ruby>か<ruby>今<rt>いま</rt></ruby>かと<ruby>待<rt>ま</rt></ruby>っている」** <ruby>状態<rt>じょうたい</rt></ruby>です。

例えば、あなたがこんな<ruby>動<rt>うご</rt></ruby>きをしたとき、それがすべて「イベント」になります。

* ボタンを **カチッ（クリック）** としたとき。
* キーボードで **<ruby>文字<rt>もじ</rt></ruby>を<ruby>入力<rt>にゅうりょく</rt></ruby>** したとき。
* <ruby>画面<rt>がめん</rt></ruby>を **<ruby>上下<rt>じょうげ</rt></ruby>に<ruby>動<rt>うご</rt></ruby>かした（スクロール）** とき。

このように、**「ユーザーが<ruby>何<rt>なに</rt></ruby>かをした！」** という<ruby>出来事<rt>できごと</rt></ruby>のことを、JavaScriptでは「イベント」と<ruby>呼<rt>よ</rt></ruby>びます。

***

### 2. 「もし〜したら、〜する」という<ruby>約束<rt>やくそく</rt></ruby>

イベントの<ruby>考<rt>かんが</rt></ruby>え<ruby>方<rt>かた</rt></ruby>は、<ruby>皆<rt>みな</rt></ruby>さんの<ruby>日常<rt>にちじょう</rt></ruby>にある **「センサー」** と<ruby>同<rt>おな</rt></ruby>じです。

* **<ruby>自動<rt>じどう</rt></ruby>ドア：** 「<ruby>人<rt>ひと</rt></ruby>が<ruby>前<rt>まえ</rt></ruby>に<ruby>来<rt>き</rt></ruby>たら（イベント）、ドアを<ruby>開<rt>あ</rt></ruby>ける」
* **<ruby>目覚<rt>めざ</rt></ruby>まし<ruby>時計<rt>どけい</rt></ruby>：** 「<ruby>朝<rt>あさ</rt></ruby>の7<ruby>時<rt>じ</rt></ruby>になったら（イベント）、<ruby>音<rt>おと</rt></ruby>を<ruby>鳴<rt>な</rt></ruby>らす」
* **ウェブサイト：** 「ボタンが<ruby>押<rt>お</rt></ruby>されたら（イベント）、メッセージを<ruby>出<rt>だ</rt></ruby>す」

JavaScriptを<ruby>学<rt>まな</rt></ruby>ぶと、この **「もし〜が<ruby>起<rt>お</rt></ruby>きたら、この<ruby>仕事<rt>しごと</rt></ruby>をやってね！」** というマニュアルを<ruby>書<rt>か</rt></ruby>けるようになります。

***

### 3. <ruby>留学生<rt>りゅうがくせい</rt></ruby>への<ruby>導入<rt>どうにゅう</rt></ruby>メッセージ

> 「<ruby>今<rt>いま</rt></ruby>はまだ、<ruby>難<rt>むずか</rt></ruby>しい<ruby>魔法<rt>まほう</rt></ruby>の<ruby>言葉<rt>ことば</rt></ruby>を<ruby>覚<rt>おぼ</rt></ruby>える<ruby>必要<rt>ひつよう</rt></ruby>はありません。   <ruby>画面<rt>がめん</rt></ruby>の<ruby>中<rt>なか</rt></ruby>で<ruby>起<rt>お</rt></ruby>きる **『クリック』や『<ruby>入力<rt>にゅうりょく</rt></ruby>』などの<ruby>変化<rt>へんか</rt></ruby>の<ruby>一<rt>ひと</rt></ruby>つひとつに、<ruby>名前<rt>なまえ</rt></ruby>（イベント）がついているんだな** 、ということだけ<ruby>覚<rt>おぼ</rt></ruby>えておいてください。   <ruby>皆<rt>みな</rt></ruby>さんが『<ruby>何<rt>なに</rt></ruby>か』をしたときに、サイトが『<ruby>反応<rt>はんのう</rt></ruby>』するのは、このイベントのおかげなんですよ！」

***

### まとめ

| <ruby>言葉<rt>ことば</rt></ruby>      | イメージ                                                                                                                                         |
| -------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| **イベント**                         | 「<ruby>何<rt>なに</rt></ruby>かが<ruby>起<rt>お</rt></ruby>きた！」という<ruby>合図<rt>あいず</rt></ruby>                                                       |
| **きっかけ**                         | ユーザーがマウスやキーボードを<ruby>動<rt>うご</rt></ruby>かすこと                                                                                                 |
| **<ruby>反応<rt>はんのう</rt></ruby>** | <ruby>画面<rt>がめん</rt></ruby>の<ruby>色<rt>いろ</rt></ruby>が<ruby>変<rt>か</rt></ruby>わったり、<ruby>窓<rt>まど</rt></ruby>が<ruby>開<rt>あ</rt></ruby>いたりすること |

***

「ウェブページを<ruby>生<rt>い</rt></ruby>きているように<ruby>動<rt>うご</rt></ruby>かすための『スイッチ』」。それがイベントです。

## IV. オブジェクトとは

<ruby>皆<rt>みな</rt></ruby>さんがこれから<ruby>学<rt>まな</rt></ruby>ぶのは、**ウェブページを<ruby>動<rt>うご</rt></ruby>かす<ruby>方法<rt>ほうほう</rt></ruby>** です。ウェブページを<ruby>動<rt>うご</rt></ruby>かすためには、**ウェブページを<ruby>表示<rt>ひょうじ</rt></ruby>しているブラウザに「これこれこういうことをしなさい」と<ruby>命令<rt>めいれい</rt></ruby>する** ことが<ruby>必要<rt>ひつよう</rt></ruby>です。

### 1. オブジェクトとはどんなもの？

HTMLやCSSという<ruby>設計図<rt>せっけいず</rt></ruby>に<ruby>従<rt>したが</rt></ruby>って、ブラウザはそれをウェブページとして<ruby>作<rt>つく</rt></ruby>り<ruby>上<rt>あ</rt></ruby>げてくれます。JavaScriptは<ruby>出来上<rt>できあ</rt></ruby>がったウェブページの<ruby>部品<rt>ぶひん</rt></ruby>を **「オブジェクト」** としてとらえ、それに<ruby>対<rt>たい</rt></ruby>して『これこれこういうことをしなさい』と<ruby>命令<rt>めいれい</rt></ruby>します。

さまざまな<ruby>人<rt>ひと</rt></ruby>が<ruby>集<rt>あつ</rt></ruby>まって<ruby>会社<rt>かいしゃ</rt></ruby>ができているのと<ruby>同<rt>おな</rt></ruby>じように、ウェブページももさまざまなオブジェクトから<ruby>構成<rt>こうせい</rt></ruby>されています。そして、「<ruby>会社<rt>かいしゃ</rt></ruby>に<ruby>何<rt>なに</rt></ruby>かをしてもらう」というのは、<ruby>実際<rt>じっさい</rt></ruby>には「その<ruby>会社<rt>かいしゃ</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>に<ruby>何<rt>なに</rt></ruby>かをしてもらう」ことです。<ruby>同<rt>おな</rt></ruby>じように、**「ウェブページを<ruby>動<rt>うご</rt></ruby>かす」というのは「ウェブページのオブジェクトに<ruby>何<rt>なに</rt></ruby>かをしてもらう」** ということです。

![](img/object\_waiting2.JPG)

### 2. あいまいさのない<ruby>命令<rt>めいれい</rt></ruby>：「<ruby>誰<rt>だれ</rt></ruby>が」「<ruby>何<rt>なに</rt></ruby>をする」

JavaScripはマニュアルですから、「みんなで<ruby>協力<rt>きょうりょく</rt></ruby>して、こういうことをやりなさい」とぼんやりした<ruby>命令<rt>めいれい</rt></ruby>をするのではなく、「Aさんはこれをして」「Bさんはあれをして」と<ruby>一人<rt>ひとり</rt></ruby>ひとりの<ruby>作業<rt>さぎょう</rt></ruby>を<ruby>正確<rt>せいかく</rt></ruby>に<ruby>伝<rt>つた</rt></ruby>えなければなりません。 **「<ruby>誰<rt>だれ</rt></ruby>が」「<ruby>何<rt>なに</rt></ruby>をする」のかを、だれが<ruby>読<rt>よ</rt></ruby>んでもわかるように<ruby>書<rt>か</rt></ruby>く** ことが<ruby>大事<rt>だいじ</rt></ruby>です。

この「Aさん」「Bさん」がJavaScriptでは **「オブジェクト」** にあたります。

「オブジェクト」という<ruby>言葉<rt>ことば</rt></ruby>は、<ruby>皆<rt>みな</rt></ruby>さんには<ruby>聞<rt>き</rt></ruby>きなれないものかもしれませんが、とりあえず、<ruby>次<rt>つぎ</rt></ruby>のようなイメージを<ruby>頭<rt>あたま</rt></ruby>に<ruby>思<rt>おも</rt></ruby>い<ruby>描<rt>えが</rt></ruby>いてください。

* **ウェブページの<ruby>中<rt>なか</rt></ruby>には、たくさんのオブジェクトと<ruby>呼<rt>よ</rt></ruby>ばれるものがいて、JavaScriptを<ruby>使<rt>つか</rt></ruby>って、<ruby>彼<rt>かれ</rt></ruby>らに<ruby>命令<rt>めいれい</rt></ruby>すれば、<ruby>仕事<rt>しごと</rt></ruby>をしてくれるらしい**

![](img/objects\_waiting2.JPG)

<ruby>今<rt>いま</rt></ruby>は、それだけで<ruby>十分<rt>じゅうぶん</rt></ruby>です。「オブジェクトの<ruby>中身<rt>なかみ</rt></ruby>がどうなっているのか？」や「それに<ruby>仕事<rt>しごと</rt></ruby>をしてもらうためのマニュアルをどう<ruby>書<rt>か</rt></ruby>けばよいのか？」については、これから<ruby>少<rt>すこ</rt></ruby>しずつ、<ruby>何度<rt>なんど</rt></ruby>かに<ruby>分<rt>わ</rt></ruby>けて<ruby>説明<rt>せつめい</rt></ruby>します。

### 3. HTMLとCSS

では、JavaScriptで<ruby>扱<rt>あつか</rt></ruby>うオブジェクトとは<ruby>具体的<rt>ぐたいてき</rt></ruby>には、どんなものでしょうか？

ブラウザはサーバーからのレスポンスを<ruby>受<rt>う</rt></ruby>け<ruby>取<rt>と</rt></ruby>ります。そのレスポンスのうち「HTML」と「CSS」がウェブページという「<ruby>家<rt>いえ</rt></ruby>」の<ruby>柱<rt>はしら</rt></ruby>、<ruby>壁<rt>かべ</rt></ruby>、<ruby>床<rt>ゆか</rt></ruby>、あるいはペンキ、インテリア、<ruby>壁紙<rt>かべがみ</rt></ruby>、といった<ruby>部品<rt>ぶひん</rt></ruby>になるのは、<ruby>前<rt>まえ</rt></ruby>に<ruby>説明<rt>せつめい</rt></ruby>した<ruby>通<rt>とお</rt></ruby>りです。

<ruby>実<rt>じつ</rt></ruby>は、この「ウェブページの<ruby>部品<rt>ぶひん</rt></ruby>」こそが、JavaScriptの **オブジェクト** です。

したがって、JavaScriptでウェブページを<ruby>操<rt>あやつ</rt></ruby>るためには、まずウェブページの<ruby>部品<rt>ぶひん</rt></ruby>そのものについて、<ruby>理解<rt>りかい</rt></ruby>しなければなりません。

<ruby>次<rt>つぎ</rt></ruby>のステップでは、ウェブページの<ruby>設計図<rt>せっけいず</rt></ruby>である **HTML** と **CSS** について<ruby>説明<rt>せつめい</rt></ruby>します。

***

## このセクションのまとめ

JavaScriptが<ruby>動<rt>うご</rt></ruby>く<ruby>順番<rt>じゅんばん</rt></ruby>をイラストで<ruby>描<rt>えが</rt></ruby>くとこんな<ruby>風<rt>ふう</rt></ruby>になります。

![](img/obj\_working2.JPG)

つまり、JavaScriptでウェブページを<ruby>動<rt>うご</rt></ruby>かすために

* 「<ruby>何<rt>なに</rt></ruby>が<ruby>起<rt>お</rt></ruby>きたら」（どのイベントに<ruby>反応<rt>はんのう</rt></ruby>させるか？）
* 「<ruby>誰<rt>だれ</rt></ruby>に」（どのオブジェクトに<ruby>仕事<rt>しごと</rt></ruby>をさせるか？）
* 「どういう<ruby>仕事<rt>しごと</rt></ruby>をさせるか？」（プログラムの<ruby>内容<rt>ないよう</rt></ruby>）

を<ruby>考<rt>かんが</rt></ruby>えておく<ruby>必要<rt>ひつよう</rt></ruby>があります。「プログラムの<ruby>内容<rt>ないよう</rt></ruby>」そのものだけではなく、その **プログラムをを<ruby>動<rt>うご</rt></ruby>かすきっかけ（イベント）** と、**<ruby>実際<rt>じっさい</rt></ruby>に<ruby>動<rt>うご</rt></ruby>くもの（オブジェクト）** の<ruby>関係<rt>かんけい</rt></ruby>が<ruby>大事<rt>だいじ</rt></ruby>なのです。

***

それでは、まずウェブページの<ruby>骨組<rt>ほねぐ</rt></ruby>みである、「HTML」について、<ruby>詳<rt>くわ</rt></ruby>しく<ruby>見<rt>み</rt></ruby>てみましょう！

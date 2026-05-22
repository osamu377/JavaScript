## JavaScriptを<ruby>始<rt>はじ</rt></ruby>める<ruby>前<rt>まえ</rt></ruby>に

**<ruby>留学生<rt>りゅうがくせい</rt></ruby>のためのJavaScript<ruby>学習<rt>がくしゅう</rt></ruby>ガイド：Webを<ruby>動<rt>うご</rt></ruby>かす<ruby>魔法<rt>まほう</rt></ruby>を<ruby>学<rt>まな</rt></ruby>ぼう**  
<ruby>留学生<rt>りゅうがくせい</rt></ruby>のみなさん、こんにちは！プログラミングの<ruby>世界<rt>せかい</rt></ruby>へようこそ。  

みなさんが<ruby>毎日<rt>まいにち</rt></ruby><ruby>使<rt>つか</rt></ruby>っているスマートフォンやパソコンの<ruby>画面<rt>がめん</rt></ruby>。ボタンを<ruby>押<rt>お</rt></ruby>すとメニューが<ruby>出<rt>で</rt></ruby>てきたり、<ruby>地図<rt>ちず</rt></ruby>が<ruby>動<rt>うご</rt></ruby>いたりしますね。これはすべて「JavaScript」という<ruby>言葉<rt>ことば</rt></ruby>が<ruby>命令<rt>めいれい</rt></ruby>を<ruby>出<rt>だ</rt></ruby>して<ruby>動<rt>うご</rt></ruby>かしています。  

このガイドでは、<ruby>自分<rt>じぶん</rt></ruby>でウェブページを<ruby>動<rt>うご</rt></ruby>かせるようになるための<ruby>基礎<rt>きそ</rt></ruby>をやさしく<ruby>解説<rt>かいせつ</rt></ruby>します。それがJavaScriptの<ruby>基本<rt>きほん</rt></ruby>だからです。  

(<ruby>参考<rt>さんこう</rt></ruby>)  
現在のJavaScriptは、ウェブページの<ruby>操作<rt>そうさ</rt></ruby>だけでなく、いろいろな<ruby>用途<rt>ようと</rt></ruby>に<ruby>使<rt>つか</rt></ruby>えるプログラム<ruby>言語<rt>げんご</rt></ruby>になっています。しかし、<ruby>今<rt>いま</rt></ruby>でも、ブラウザ<ruby>上<rt>じょう</rt></ruby>で<ruby>活躍<rt>かつやく</rt></ruby>しています。

---

### I. <ruby>私<rt>わたし</rt></ruby>たちの<ruby>舞台<rt>ぶたい</rt></ruby>：WWW（ワールド・ワイド・ウェブ）

まず、JavaScriptの<ruby>活躍<rt>かつやく</rt></ruby>の<ruby>舞台<rt>ぶたい</rt></ruby>、WWW（ワールド・ワイド・ウェブ）とは<ruby>何<rt>なに</rt></ruby>かについて、<ruby>説明<rt>せつめい</rt></ruby>しましょう。  

**WWW（ワールド・ワイド・ウェブ）** は、<ruby>世界中<rt>せかいじゅう</rt></ruby>のコンピュータが「クモの<ruby>巣<rt>す</rt></ruby>（Web）」のようにつながって、<ruby>情報<rt>じょうほう</rt></ruby>を<ruby>共有<rt>きょうゆう</rt></ruby>する<ruby>仕組<rt>しく</rt></ruby>みのことです。  

これを、**「<ruby>図書館<rt>としょかん</rt></ruby>」** に<ruby>例<rt>たと</rt></ruby>えて、やさしく<ruby>説明<rt>せつめい</rt></ruby>しますね。

#### 1. 3つの<ruby>大切<rt>たいせつ</rt></ruby>な「<ruby>道具<rt>どうぐ</rt></ruby>」

WWWを<ruby>動<rt>うご</rt></ruby>かすために、3つの<ruby>主役<rt>しゅやく</rt></ruby>がいます。

- **Webブラウザ（お<ruby>客<rt>きゃく</rt></ruby>さん）**  
  ChromeやSafariなど、<ruby>私<rt>わたし</rt></ruby>たちがサイトを<ruby>見<rt>み</rt></ruby>るためのソフトです。「<ruby>本<rt>ほん</rt></ruby>を<ruby>読<rt>よ</rt></ruby>みたい<ruby>人<rt>ひと</rt></ruby>」です。

- **Webサーバ（<ruby>図書館<rt>としょかん</rt></ruby>のスタッフ）**  
  <ruby>世界中<rt>せかいじゅう</rt></ruby>のどこかにある、24<ruby>時間<rt>じかん</rt></ruby><ruby>動<rt>うご</rt></ruby>いているコンピュータです。「<ruby>本<rt>ほん</rt></ruby>を<ruby>管理<rt>かんり</rt></ruby>している<ruby>人<rt>ひと</rt></ruby>」です。

- **HTML（<ruby>本<rt>ほん</rt></ruby>の<ruby>内容<rt>ないよう</rt></ruby>）**  
  ウェブサイトに<ruby>書<rt>か</rt></ruby>いてある<ruby>文章<rt>ぶんしょう</rt></ruby>や<ruby>写真<rt>しゃしん</rt></ruby>のデータです。これが「<ruby>本<rt>ほん</rt></ruby>」そのものです。

#### 2. ウェブサイトが<ruby>表示<rt>ひょうじ</rt></ruby>されるまでの「4つのステップ」

あなたがブラウザでURLを<ruby>入力<rt>にゅうりょく</rt></ruby>してから、<ruby>画面<rt>がめん</rt></ruby>が<ruby>出<rt>で</rt></ruby>るまでの<ruby>流<rt>なが</rt></ruby>れを<ruby>見<rt>み</rt></ruby>てみましょう。

- **リクエスト（<ruby>注文<rt>ちゅうもん</rt></ruby>）**：  
  あなたが「このページを<ruby>見<rt>み</rt></ruby>たい！」とURLをクリックします。

- **<ruby>住所<rt>じゅうしょ</rt></ruby>の<ruby>確認<rt>かくにん</rt></ruby>（DNS）**：  
  <ruby>数字<rt>すうじ</rt></ruby>の<ruby>住所<rt>じゅうしょ</rt></ruby>（IPアドレス）で<ruby>場所<rt>ばしょ</rt></ruby>を<ruby>探<rt>さが</rt></ruby>します。

- **レスポンス（<ruby>返事<rt>へんじ</rt></ruby>）**：  
  サーバがリクエストを<ruby>受<rt>う</rt></ruby>けてデータを<ruby>送<rt>おく</rt></ruby>り<ruby>返<rt>かえ</rt></ruby>します。

- **レンダリング（<ruby>組<rt>く</rt></ruby>み<ruby>立<rt>た</rt></ruby>て）**：  
  ブラウザがHTMLを<ruby>読<rt>よ</rt></ruby>んで<ruby>表示<rt>ひょうじ</rt></ruby>します。

#### 3. WWWで<ruby>使<rt>つか</rt></ruby>われる「<ruby>魔法<rt>まほう</rt></ruby>の<ruby>言葉<rt>ことば</rt></ruby>」

- HTTP / HTTPS：<ruby>情報<rt>じょうほう</rt></ruby>をやり<ruby>取<rt>と</rt></ruby>りする<ruby>規則<rt>きそく</rt></ruby>  
- URL：ウェブサイトの<ruby>住所<rt>じゅうしょ</rt></ruby>  

---

### II. ウェブページを<ruby>作<rt>つく</rt></ruby>る「3つの<ruby>力<rt>ちから</rt></ruby>」

ウェブページは3つの<ruby>技術<rt>ぎじゅつ</rt></ruby>でできています。

（※ 表構造は保持）

---

### III. イベントとは

#### 「きっかけ」

- ボタンを<ruby>押<rt>お</rt></ruby>す
- <ruby>文字<rt>もじ</rt></ruby>を<ruby>入力<rt>にゅうりょく</rt></ruby>
- <ruby>画面<rt>がめん</rt></ruby>を<ruby>動<rt>うご</rt></ruby>かす  

これらはすべて「イベント」と<ruby>呼<rt>よ</rt></ruby>ばれます。

---

### IV. オブジェクトとは

ウェブページの<ruby>部品<rt>ぶひん</rt></ruby>＝オブジェクトです。

JavaScriptはオブジェクトに<ruby>命令<rt>めいれい</rt></ruby>します。

- 「<ruby>誰<rt>だれ</rt></ruby>が」
- 「<ruby>何<rt>なに</rt></ruby>をする」

を<ruby>明確<rt>めいかく</rt></ruby>にします。

---

### <ruby>この<rt>この</rt></ruby>セクションの<ruby>まとめ<rt>まとめ</rt></ruby>

- 「<ruby>何<rt>なに</rt></ruby>が<ruby>起<rt>お</rt></ruby>きたら」
- 「<ruby>誰<rt>だれ</rt></ruby>に」
- 「どうするか」

これがJavaScript<ruby>設計<rt>せっけい</rt></ruby>の<ruby>基本<rt>きほん</rt></ruby>です。



# 🧠 JavaScriptの<ruby>記述<rt>きじゅつ</rt></ruby>ルール（<ruby>初心者<rt>しょしんしゃ</rt></ruby><ruby>向け<rt>むけ</rt></ruby>まとめ）

## I. <ruby>文<rt>ぶん</rt></ruby>の<ruby>終わり<rt>おわり</rt></ruby>にはセミコロン（`;`）をつける

* <ruby>命令<rt>めいれい</rt></ruby>の<ruby>終わり<rt>おわり</rt></ruby>にセミコロンをつけることで、コードの<ruby>区切り<rt>くぎり</rt></ruby>が<ruby>明確<rt>めいかく</rt></ruby>になります。

```javascript
let name = "Taro";
```

***

## II. <ruby>変数<rt>へんすう</rt></ruby>の<ruby>宣言<rt>せんげん</rt></ruby>には `let` や `const` を<ruby>使う<rt>つかう</rt></ruby>

* `let`：<ruby>変更<rt>へんこう</rt></ruby><ruby>可能<rt>かのう</rt></ruby>な<ruby>変数<rt>へんすう</rt></ruby>
* `const`：<ruby>変更<rt>へんこう</rt></ruby><ruby>不可<rt>ふか</rt></ruby>の<ruby>定数<rt>ていすう</rt></ruby>

```javascript
let age = 20;
const birthYear = 2005;
```

***

## III. <ruby>文字列<rt>もじれつ</rt></ruby>は `" "` または `' '` で<ruby>囲む<rt>かこむ</rt></ruby>

* どちらでもOKですが、<ruby>統一<rt>とういつ</rt></ruby>して<ruby>使う<rt>つかう</rt></ruby>のが<ruby>良い<rt>よい</rt></ruby><ruby>習慣<rt>しゅうかん</rt></ruby>です。

```javascript
let greeting = "こんにちは";
```

***

## IV. インデント（<ruby>字下げ<rt>じさげ</rt></ruby>）でコードを<ruby>見やすく<rt>みやすく</rt></ruby>する

* <ruby>通常<rt>つうじょう</rt></ruby>はスペース2つまたは4つで<ruby>揃えます<rt>そろえます</rt></ruby>。

```javascript
function sayHello() {
  console.log("こんにちは！");
}
```

***

## V. コメントを<ruby>使って<rt>つかって</rt></ruby><ruby>説明<rt>せつめい</rt></ruby>を<ruby>書く<rt>かく</rt></ruby>

* `//` を<ruby>使って<rt>つかって</rt></ruby>コードの<ruby>説明<rt>せつめい</rt></ruby>を<ruby>記述<rt>きじゅつ</rt></ruby>できます。

```javascript
// これは挨拶を表示する関数です
function sayHello() {
  console.log("こんにちは！");
}
```

***

## VI. <ruby>命名<rt>めいめい</rt></ruby>はわかりやすく、<ruby>英語<rt>えいご</rt></ruby>で<ruby>書く<rt>かく</rt></ruby>

* <ruby>変数<rt>へんすう</rt></ruby>や<ruby>関数名<rt>かんすうめい</rt></ruby>は<ruby>意味<rt>いみ</rt></ruby>のある<ruby>英語<rt>えいご</rt></ruby>で<ruby>書く<rt>かく</rt></ruby>のが<ruby>一般的<rt>いっぱんてき</rt></ruby>です。

```javascript
let userName = "Taro";
function showMessage() {
  console.log("ようこそ！");
}
```

***

## VII. <ruby>大文字<rt>おおもじ</rt></ruby>と<ruby>小文字<rt>こもじ</rt></ruby>は<ruby>区別<rt>くべつ</rt></ruby>される

* `Name` と `name` は<ruby>別<rt>べつ</rt></ruby>の<ruby>変数<rt>へんすう</rt></ruby>として<ruby>扱われます<rt>あつかわれます</rt></ruby>。

```javascript
let name = "Taro";
let Name = "Hanako";  // ← 別の変数
```

***

***

## VIII. ⚠️ 留学生への重要アドバイス：<ruby>文字列<rt>もじれつ</rt></ruby>やコメント<ruby>以外<rt>いがい</rt></ruby>は<ruby>半角文字<rt>はんかくもじ</rt></ruby>で<ruby>記述<rt>きじゅつ</rt></ruby>する

日本のパソコンやスマホを使うとき、最初にびっくりするのが **「文字の大きさ（幅）」** の違いだと思います。

簡単に言うと、**「スリムな文字」** と **「<ruby>太<rt>ふと</rt></ruby>っちょな文字」** の2種類があります。

これは日本だけではなく、漢字やハングルを使う東アジアの国々（CJK：China, Japan, Korea）に共通する特徴です。

### 1. <ruby>全角<rt>ぜんかく</rt></ruby>と <ruby>半角<rt>はんかく</rt></ruby>の違い

イメージは「箱」のサイズです。

* **<ruby>全角<rt>ぜんかく</rt></ruby> (Full-width):** 正方形の箱。漢字やひらがなと同じ大きさ。
* **<ruby>半角<rt>はんかく</rt></ruby> (Half-width):** <ruby>全角<rt>ぜんかく</rt></ruby>の半分の細い箱。アルファベットや数字に使われます。

| 種類 | <ruby>見<rt>み</rt></ruby>た<ruby>目<rt>め</rt></ruby> | 特徴 |
| --- | --- | --- |
| **<ruby>半角<rt>はんかく</rt></ruby> (Half)** | `A B C 1 2 3 ! ?` | スリム。世界中で使われる標準サイズ。 |
| **<ruby>全角<rt>ぜんかく</rt></ruby> (Full)** | `Ａ Ｂ Ｃ １ ２ ３ ！ ？` | 横に広い。日本の漢字やひらがなと仲良しサイズ。 |

### 2. なぜこれが大事なの？

日本のウェブサイト（銀行、学校の<ruby>登録<rt>とうろく</rt></ruby>、ネットショッピングなど）では、**「ここは<ruby>半角<rt>はんかく</rt></ruby>で書いてください」「ここは<ruby>全角<rt>ぜんかく</rt></ruby>で！」** というルールがとても厳しいです。

* **メールアドレス・パスワード:** ほとんどが **「<ruby>半角<rt>はんかく</rt></ruby>」** です。<ruby>全角<rt>ぜんかく</rt></ruby>で打つとエラーになります。
* **名前（フリガナ）:** 銀行などでは **「<ruby>全角<rt>ぜんかく</rt></ruby>」** を求められることが多いです。

> [!IMPORTANT]
> **よくあるミス：**
> スペース（空白）にも「<ruby>全角<rt>ぜんかく</rt></ruby>」と「<ruby>半角<rt>はんかく</rt></ruby>」があります。
> パスワードの間に「<ruby>全角<rt>ぜんかく</rt></ruby>スペース」が入ってしまうと、<ruby>見<rt>み</rt></ruby>た<ruby>目<rt>め</rt></ruby>では気づけないのでログインできなくて困ることがあります。注意しましょう！

**コードはすべて「<ruby>半角<rt>はんかく</rt></ruby>（half-width）」で書きます** 

JavaScriptなどのプログラムを書くときは、<ruby>画面<rt>がめん</rt></ruby>に日本語で<ruby>表示<rt>ひょうじ</rt></ruby>する言葉や、コメントなどを除いて、<ruby>半角<rt>はんかく</rt></ruby>文字で書きます。

特に「<ruby>全角<rt>ぜんかく</rt></ruby>スペース」や「<ruby>全角<rt>ぜんかく</rt></ruby>のセミコロン **；** 」、「<ruby>全角<rt>ぜんかく</rt></ruby>のカッコ **（ ）** 」が混じると、プログラムは<ruby>動<rt>うご</rt></ruby>きません。日本語<ruby>入力<rt>にゅうりょく</rt></ruby>（IME）を使っているときは、常に<ruby>半角<rt>はんかく</rt></ruby>になっているか確認しましょう。

また、ほとんどのプログラミング言語（Python, JavaScript, Java, C++ など）は、英語をベースに作られています。そのため、コンピュータは「<ruby>全角<rt>ぜんかく</rt></ruby>スペース」をスペースとして認識できず、「ナゾの記号」だと思ってしまいます。

### 3. どうやって<ruby>使<rt>つか</rt></ruby>い<ruby>分<rt>わ</rt></ruby>けるの？

キーボードの「<ruby>半角<rt>はんかく</rt></ruby>/<ruby>全角<rt>ぜんかく</rt></ruby>」キー以外にも、便利なショートカットがあります（Windowsの場合）。

1. 文字を<ruby>入力<rt>にゅうりょく</rt></ruby>して、確定する（Enterを押す）前に…
2. **F8キー** を押すと、一瞬で **<ruby>半角<rt>はんかく</rt></ruby>** になります。
3. **F9キー** を押すと、一瞬で **<ruby>全角<rt>ぜんかく</rt></ruby>アルファベット** になります。

最初は少し面倒に感じるかもしれませんが、「日本の文字（漢字）は大きいから、<ruby>専用<rt>せんよう</rt></ruby>の広い席が必要なんだな」と思えばOKです！

***


## IX. まとめ：JavaScript学習のルールと習慣

**JavaScriptの<ruby>書<rt>か</rt></ruby>き<ruby>方<rt>かた</rt></ruby>：これだけは守りたい8つのルール**

最後に、ミスを防ぐための大切なルールをまとめました。

たとえば<ruby>飲食<rt>いんしょく</rt></ruby>店でアルバイトをする場合も、わかりやすく書かれたマニュアルを見れば、ミスをすることなく作業することができます。マニュアルは、誰が読んでも同じ意味にとれるように、あいまいさのない、はっきり書かれたものでなければなりません。

プログラミングは世界共通のルールです。なぜ英語（えいご）で名前を付けるのか？ それは世界中のプログラマーが共通して使う「<ruby>公用<rt>こうよう</rt>></ruby>の言葉」だからです。

以下のルールを「チェックリスト」として使いましょう。

1. 文の終わりにはセミコロン（;）： 命令の<ruby>区切<rt>くぎ</rt></ruby>りをはっきりさせます。
2. <ruby>変数<rt>へんすう</rt></ruby>の<ruby>宣言<rt>せんげん</rt></ruby>（せんげん）は let と const： 値を入れる「箱（はこ）」を作ります。
    * const：一度決めたら変えられない 「箱に貼った固定ラベル」 です。基本はこちらを使います。
    * let：あとで中身を<ruby>入<rt>い</rt></ruby>れ<ruby>替<rt>かえ</rt></ruby>られる箱です。
3. 文字列は " " または ' ' で囲む： 「こんにちは」などの言葉は<ruby>引用符<rt>いんようふ</rt></ruby>（いんようふ）で囲みます。
4. インデント（字下げ）： コードの行の最初をスペースで<ruby>揃<rt>そろ</rt></ruby>えて、見やすくします。
5. コメント（//）： 自分のためのメモです。コンピュータは無視します。
6. 名前は英語（えいご）で付ける： let namae ではなく let userName と書くのがプロのルールです。
7. 命名にキャメルケース (camelCase)： 2つ目の単語を大文字にします（<ruby>例<rt>れい</rt></ruby>：userName）。
8. 大文字と小文字を分ける： MyName と myname は、コンピュータには違う箱に見えます。
9. コメントを書きましょう： `//` のあとにメモを書きます。自分の母国語でメモを残すと学習がはかどります。
10. コードはすべて「<ruby>半角<rt>はんかく</rt></ruby>（half-width）」で書きます： これが一番大切です。文字列の中とコメント以外で 「<ruby>全角<rt>ぜんかく</rt></ruby>」を使うと、コードは絶対に<ruby>動<rt>うご</rt></ruby>きません。

***


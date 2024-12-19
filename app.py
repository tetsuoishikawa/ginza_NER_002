import spacy
from spacy import displacy
import streamlit as st
import base64

# GiNZAモデルの読み込み
nlp = spacy.load("ja_ginza")

# Streamlitの設定
st.title("日本語テキストのエンティティ抽出")
st.write("テキストを入力して、エンティティを抽出します。")

# テキスト入力欄
input_text = st.text_area("テキストを入力してください：")

# 変換ボタン
if st.button("解析開始"):
    # テキストの解析
    doc = nlp(input_text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]

    # displacyで表示する内容をHTMLとして保存
    html = displacy.render(doc, style="ent", jupyter=False)

    # HTMLをファイルに書き込む
    output_filename = "output_entities.html"
    with open(output_filename, "w", encoding="utf-8") as f:
        f.write(html)

    # HTMLファイルのダウンロードリンクを作成
    def download_link(object_to_download, download_filename, download_link_text):
        b64 = base64.b64encode(object_to_download.encode()).decode()
        return f'<a href="data:file/txt;base64,{b64}" download="{download_filename}">{download_link_text}</a>'

    download_html = download_link(html, output_filename, "解析結果をダウンロード")
    st.markdown(download_html, unsafe_allow_html=True)

    st.write("エンティティの情報が解析されました。以下のリンクからダウンロードできます。")


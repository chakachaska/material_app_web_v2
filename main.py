import streamlit as st
import pandas as pd

# ✅ ページ設定（オプション）
st.set_page_config(page_title="材料選定アプリ", layout="centered")

# ✅ キャッシュクリア（明示）
st.cache_data.clear()

# ✅ データ読み込み関数
def load_data():
    file_path = "250629material_select_input_data.xlsx"
    df = pd.read_excel(file_path, sheet_name="material condition table", dtype=str)
    df = df.apply(pd.to_numeric, errors='ignore')  # 数値だけ変換、他は文字列のまま
    df["材料名"] = df["材料名"].str.upper()
    return df

# ✅ データ読込
df = load_data()

# ✅ 材料選択UI
selected_name = st.selectbox("🧪 素材を選択してください", df["材料名"].unique())

# ✅ 実行ボタン（押さないと表示されない）
if st.button("📊 材料特性を表示"):
    selected_material = df[df["材料名"] == selected_name]

    if not selected_material.empty:
        st.success(f"✅ 選択中の材料（内部処理）: {selected_name}")
        st.markdown("---")
        st.markdown("📄 **材料特性一覧:**")

        for col in selected_material.columns:
            if col != "材料名":
                val = selected_material[col].values[0]
                st.write(f"**{col}** : {val}")
    else:
        st.warning("⚠ 該当する材料データが見つかりません。")

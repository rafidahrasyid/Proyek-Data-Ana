try:
    import streamlit
    print("streamlit terinstal. Versi:", streamlit.__version__)
except ImportError:
    print("streamlit belum terinstal.")

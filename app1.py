
import streamlit as st
import ssl
import socket

def check_tls_version(url):
    try:
        ctx = ssl.create_default_context()
        with ctx.wrap_socket(socket.socket(), server_hostname=url) as s:
            s.connect((url, 443))
            return s.version()
    except Exception as e:
        return f"Error: {e}"

def main():
    st.title('TLS Version Checker')
    st.write('Enter URLs to check their TLS versions.')

    # Text area for input
    urls = st.text_area("Enter URLs (one per line):").split('\n')

    # Check button
    if st.button('Check TLS Versions'):
        if urls:
            results = {url: check_tls_version(url) for url in urls}
            st.write(results)
        else:
            st.warning("Please enter at least one URL.")

if __name__ == '__main__':
    main()

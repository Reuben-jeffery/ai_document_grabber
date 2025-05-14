import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ai_document_grabber.downloader import download_ai_document


def test_download_ai_document(tmp_path):
    # Use a small test file from the web (or your own hposted file)
    
    test_url ="https://raw.githubusercontent.com/github/gitignore/main/README.md"
    test_filename = tmp_path / "sample.pdf"
    
    download_ai_document(test_url, str(test_filename))
    
    assert test_filename.exists()
    assert test_filename.stat().st_size > 0
import gettext
import os

def init_translation():
    """
    Initialize translation
    """
    # Directory to place translation files
    path_to_locale_dir = os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            './locale'
        )
    )

    # 翻訳用クラスの設定
    translater = gettext.translation(
        'messages',                   # domain: name of dictionary file
        localedir=path_to_locale_dir, # Directory to place translation files
        fallback=True                 # If .mo file is not found, output untranslated string
    )

    # Bind a function called _ to Python's built-in global area
    translater.install()


import os
import html
# from itertools import zip_longest
# from pprint import pp

# import anki
import aqt
from aqt.utils import showInfo
from aqt.qt import Qt
from aqt.editor import Editor

os.environ['PYPINYIN_NO_PHRASES'] = '1'
os.environ['PYPINYIN_NO_DICT_COPY'] = '1'

from ._vendor import pypinyin


dict_has_loaded = False


def rubify(editor: Editor):
    selected_text: str = editor.web.selectedText()

    if not selected_text:
        showInfo("""You must select some text first""",
                 parent=editor.widget,
                 title='Simple Mandarin Ruby')
        return

    try:
        editor.mw.app.setOverrideCursor(Qt.WaitCursor)
        global dict_has_loaded
        if not dict_has_loaded:
            from .data.custom_phrases_dict import phrases_dict
            pypinyin.load_phrases_dict(phrases_dict)
            dict_has_loaded = True

        pinyins = pypinyin.lazy_pinyin(selected_text,
                                       style=pypinyin.Style.TONE,
                                       errors=lambda chars: list(chars))

        if len(pinyins) != len(selected_text):
            raise IndexError("""Generated pinyin list didn't match string length""")

        pairs = zip(selected_text, pinyins)
        output = pairs_to_html(pairs)

        # Uses document.execCommand('insertHTML', ...) in JS under the hood:
        editor.doPaste(output, internal=False, extended=True)
    finally:
        editor.mw.app.restoreOverrideCursor()


def pairs_to_html(pairs):
    output = ''
    for character, pinyin in pairs:
        if pinyin == character:
            output += html.escape(character, quote=False)
        else:
            output += f'<ruby>{html.escape(character, quote=False)}<rt>{html.escape(pinyin, quote=False)}</rt></ruby>'
    return output


def add_buttons(buttons, editor: Editor):
    this_path = os.path.dirname(__file__)
    icon_path = os.path.abspath(os.path.join(this_path, 'resources', 'ruby.svg'))

    button = editor.addButton(
        # icon='qrc:///icons/anki.png',
        icon=icon_path,
        cmd='smr_rubify',
        func=rubify,
        tip="""Add pinyin ruby to selection""",
        # label='Ruby',
    )
    buttons.append(button)


aqt.gui_hooks.editor_did_init_buttons.append(add_buttons)

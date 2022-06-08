import re


def clear(input):
    print('Method clear()')
    print('  input string:', input)
    output = re.sub('[() -]', '', input)
    print('  output string:', output)
    return output


def merge_phones_like_on_home_page(contact):
    print('Method merge_phones_like_on_home_page()')
    print('  contact:', contact)

    merged = '\n'.join(
        filter(
            lambda x: x != '',
            map(
                lambda x: clear(x),
                filter(
                    lambda x: x is not None,
                    [contact.homephone, contact.mobilephone, contact.workphone, contact.secondaryphone]
                )
            )
        )
    )

    print('merged:')
    print(merged)
    return merged


def test_phones_on_home_page(app):
    print("\n\n********** Test phones on home page **********")
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)

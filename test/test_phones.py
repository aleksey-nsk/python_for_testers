import re


def clear(input):
    print('Method clear()')
    print('  input string:', input)
    output = re.sub('[() -]', '', input)
    print('  output string:', output)
    return output


def test_phones_on_home_page(app):
    print("\n\n********** Test phones on home page **********")

    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)

    assert contact_from_home_page.homephone == clear(contact_from_edit_page.homephone)
    assert contact_from_home_page.workphone == clear(contact_from_edit_page.workphone)
    assert contact_from_home_page.mobilephone == clear(contact_from_edit_page.mobilephone)
    assert contact_from_home_page.secondaryphone == clear(contact_from_edit_page.secondaryphone)


def test_phones_on_contact_view_page(app):
    print("\n\n****** Test phones on contact view page ******")

    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)

    assert contact_from_view_page.homephone == contact_from_edit_page.homephone
    assert contact_from_view_page.workphone == contact_from_edit_page.workphone
    assert contact_from_view_page.mobilephone == contact_from_edit_page.mobilephone
    assert contact_from_view_page.secondaryphone == contact_from_edit_page.secondaryphone

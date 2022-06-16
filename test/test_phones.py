import logging.config
import re

logging.config.fileConfig('../log.conf')
log = logging.getLogger('simple')


def clear(input):
    log.debug('Method clear()')
    log.debug('  input string: ' + str(input))
    output = re.sub('[() -]', '', input)
    log.debug('  output string: ' + str(output))
    return output


def merge_phones_like_on_home_page(contact):
    log.debug('Method merge_phones_like_on_home_page()')
    log.debug('  contact: ' + str(contact))

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

    log.debug('merged:')
    log.debug(merged)
    return merged


def test_phones_on_home_page(app):
    log.debug("********** Test phones on home page **********")
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)

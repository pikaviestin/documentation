import re
SCHOOL_DOMAINS = ["kotka.opit.fi", "edu.turku.fi", "eduouka.fi"]
EDU_DOMAINS = SCHOOL_DOMAINS + ["helsinki.fi", "turkuamk.fi", "edu.turkuamk.fi", "jyu.fi", "*.jamk.fi", "tuni.fi",
                                "*.utu.fi", "ekami.fi", "edu.ekami.fi", "aalto.fi", "paivola.fi"]
RY_DOMAINS = ["kapsi.fi", "hacklab.fi", "nullroute.fi", 'iki.fi', "fixme.fi", "far.fi"]
ISP_DOMAINS = ["*.inet.fi", "kolumbus.fi", "elisanet.fi", "saunalahti.fi", "netti.fi", "nic.fi", "netikka.fi", "sci.fi",
               "anvianet.fi", "kymp.net", "jippii.fi", "kotinet.com", "eunet.fi", "welho.com", "mailsuomi.com"]
CITY_DOMAINS = ["hel.fi", "vaasa.fi", "tampere.fi", "*.ouka.fi", "turku.fi"]
OTHER_DOMAINS = ["assembly.org"]

ALLOWED_DOMAINS = EDU_DOMAINS + RY_DOMAINS + ISP_DOMAINS + CITY_DOMAINS + OTHER_DOMAINS

regular_exp = r'@(\S+)$'
top_domain_regex = r'[(a-zA-Z)]*[.][(a-zA-Z)]*?$'


def validate_email_domain(email):
 try:
    email_domain = re.search(regular_exp, email).group(1)
    top_level_domain = re.search(top_domain_regex, email).group(0)
    if email_domain in ALLOWED_DOMAINS:
        return True
    elif email_domain not in ALLOWED_DOMAINS and f"*.{top_level_domain}" in ALLOWED_DOMAINS:
        return True
    else:
        ak_logger.info(f"The denied email domain was: {top_level_domain}")
        ak_message("Sähköpostiosoite ei ole valkoisella listalla, pääsy evätty.")
        return False
 except Exception as e:
        ak_logger.failure(f"The email validation has occurred an exception during execution. The exception: {e}")
        ak_message("Sähköpostiosoitteen validoinnissa tapahtui odottamaton virhe.")
        return False


return validate_email_domain(context['email'])
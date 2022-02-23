import re
SCHOOL_DOMAINS = ["kotka.opit.fi"]
EDU_DOMAINS = SCHOOL_DOMAINS + ['prakticum.fi', 'aalto.fi', 'abo.fi', 'arcada.fi', 'bc.fi', 'centria.fi', 'cou.fi',
                                'diak.fi', 'edu.bc.fi', 'edu.espoo.fi', 'edu.hel.fi', 'edu.hyria.fi', 'edu.kokkola.fi',
                                'edu.kotka.fi', 'edu.kuopio.fi', 'edu.lahti.fi', 'edu.redu.fi', 'edu.lohja.fi',
                                'edu.loimaa.fi', 'edu.nivala.fi', 'edu.novia.fi', 'edu.raseko.fi', 'edu.riveria.fi',
                                'edu.siikalatva.fi', 'edu.turku.fi', 'edu.tuusula.fi', 'edu.ylojarvi.fi', 'eduespoo.fi',
                                'eduouka.fi', 'eduvammalanlukio.fi', 'evtek.fi', 'gradia.fi', 'haaga-helia.fi',
                                'hamk.fi', 'hanken.fi', 'helsinki.fi', 'hive.fi', 'hkkk.fi', 'hut.fi', 'jamk.fi',
                                'jedu.fi', 'joensuu.fi', 'student.jyu.fi', 'jyu.fi', 'kamk.fi', 'karelia.fi', 'kauniaistenlukio.fi',
                                'kktavastia.fi', 'koudata.fi', 'koulut.kaarina.fi', 'kuva.fi', 'kyamk.fi', 'lamk.fi',
                                'lapinamk.fi', 'lappee.fi', 'laurea.fi', 'lut.fi', 'lyk.fi', 'mamk.fi', 'mayk.fi',
                                'metropolia.fi', 'munkka.fi', 'oamk.fi', 'omnia.fi', 'opp.eduvantaa.fi',
                                'oppilas.eduhat.fi', 'oppilas.hyvinkaa.fi', 'student.oulu.fi','oulu.fi', 'puv.fi', 'ramk.fi', 'redu.fi',
                                'roiedu.fi', 'saimia.fi', 'salpaus.fi', 'samk.fi', 'sasky.fi', 'edu.savonia.fi','savonia.fi', 'scp.fi',
                                'seamk.fi', 'shh.fi', 'siba.fi', 'student.lab.fi', 'student.vaasa.fi', 'syk.fi',
                                'taitajantie.fi', 'tamk.fi', 'teak.fi', 'tiedenorssi.fi', 'tpu.fi', 'tukkk.fi',
                                'tuni.fi', '*.turkuamk.fi', 'tut.fi', 'tyk.fi', 'uef.fi', 'uku.fi', 'ulapland.fi',
                                'uniarts.fi', 'uta.fi', 'utu.fi', 'uwasa.fi', 'vamk.fi', 'xamk.fi', 'edu.tampere.fi']
RY_DOMAINS = ["kapsi.fi", "hacklab.fi", "nullroute.fi", 'iki.fi', "fixme.fi", "far.fi", "modeemi.fi", "jkry.org"]
ISP_DOMAINS = ["*.inet.fi", "kolumbus.fi", "elisanet.fi", "saunalahti.fi", "netti.fi", "nic.fi", "netikka.fi", "sci.fi",
               "anvianet.fi", "kymp.net", "jippii.fi", "kotinet.com", "eunet.fi", "welho.com", "mailsuomi.com", "japo.fi"]
CITY_DOMAINS = ["hel.fi", "vaasa.fi", "tampere.fi", "*.ouka.fi", "turku.fi", "kaarina.fi", "kokkola.fi", "hyvinkaa.fi",
                "jarvenpaa.fi", "toivakka.fi", "jyvaskyla.fi", "kuopio.fi"]

PRESS_DOMAINS = ["skrolli.fi", "mikrobitti.fi", "almamedia.fi", "tivi.fi", "siivet.fi", "aamulehti.fi", "helsinginsanomat.fi", "almatalent.fi"]

OTHER_DOMAINS = ["assembly.org", "tek.fi", "ideavideo.fi", "gov.fi"]

ALLOWED_DOMAINS = EDU_DOMAINS + RY_DOMAINS + ISP_DOMAINS + CITY_DOMAINS + PRESS_DOMAINS + OTHER_DOMAINS

regular_exp = r'@(\S+)$'
top_domain_regex = r'[(a-zA-Z)]*[.][(a-zA-Z)]*?$'


def check_if_exists(email):
  if ak_user_by(email=email):
    ak_logger.info(f"Someone tried to register with the same email address as one user already exists, {email}")
    ak_message("Tällä sähköpostiosoitteella on jo olemassa käyttäjä. Et voi luoda kuin yhden käyttäjän per sähköpostiosoite.")
    return False
  else:
    return validate_email_domain(email)

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
        ak_message("Sähköpostiosoite ei ole valkoisella listalla, pääsy evätty. Ota tarvittaessa yhteys yllapito@pikaviestin.fi mikäli koet tämän olevan virhe.")
        return False
 except Exception as e:
        ak_logger.failure(f"The email validation has occurred an exception during execution. The exception: {e}")
        ak_message("Sähköpostiosoitteen validoinnissa tapahtui odottamaton virhe.")
        return False

return check_if_exists(context['email'])

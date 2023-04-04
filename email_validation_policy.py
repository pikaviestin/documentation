import re
SCHOOL_DOMAINS = ["kotka.opit.fi"]
EDU_DOMAINS = SCHOOL_DOMAINS + ['prakticum.fi', 'aalto.fi', 'abo.fi', 'arcada.fi', 'bc.fi', 'centria.fi', 'cou.fi',
                                'diak.fi', 'edu.bc.fi', 'edu.espoo.fi', 'edu.hel.fi', 'edu.hyria.fi', 'edu.kokkola.fi',
                                'edu.kotka.fi', 'edu.kuopio.fi', 'edu.lahti.fi', 'edu.redu.fi', 'edu.lohja.fi',
                                'edu.loimaa.fi', 'edu.nivala.fi', 'edu.nokiankaupunki.fi', 'edu.novia.fi', 'edu.raseko.fi', 'edu.riveria.fi',
                                'edu.siikalatva.fi', 'edu.turku.fi', 'edu.tuusula.fi', 'edu.ylojarvi.fi', 'edu.keuda.fi', 'keuda.fi', 'eduespoo.fi',
                                'eduouka.fi', 'eduvammalanlukio.fi', 'evtek.fi', 'gradia.fi', 'haaga-helia.fi',
                                'hamk.fi', 'hanken.fi', 'helsinki.fi', 'hive.fi', 'hkkk.fi', 'hut.fi', 'jamk.fi',
                                'jedu.fi', 'joensuu.fi', 'student.jyu.fi', 'jyu.fi', 'kamk.fi', 'karelia.fi', 'kauniaistenlukio.fi',
                                'kktavastia.fi', 'koudata.fi', 'koulut.kaarina.fi', 'kuva.fi', 'kyamk.fi', 'lamk.fi',
                                'lapinamk.fi', 'lappee.fi', 'laurea.fi', 'lut.fi', 'lyk.fi', 'mamk.fi', 'mayk.fi',
                                'metropolia.fi', 'munkka.fi', 'oamk.fi', 'omnia.fi', 'opp.eduvantaa.fi',
                                'oppilas.eduhat.fi', 'oppilas.hyvinkaa.fi', 'student.oulu.fi', 'oulu.fi', 'puv.fi', 'ramk.fi', 'redu.fi',
                                'roiedu.fi', 'saimia.fi', 'salpaus.fi', 'samk.fi', 'sasky.fi', 'edu.savonia.fi','savonia.fi', 'scp.fi',
                                'seamk.fi', 'shh.fi', 'siba.fi', 'student.lab.fi', 'student.vaasa.fi', 'syk.fi',
                                'taitajantie.fi', 'tamk.fi', 'teak.fi', 'tiedenorssi.fi', 'tpu.fi', 'tukkk.fi',
                                'tuni.fi', '*.turkuamk.fi', 'tut.fi', 'tyk.fi', 'uef.fi', 'uku.fi', 'ulapland.fi',
                                'uniarts.fi', 'uta.fi', 'utu.fi', 'uwasa.fi', 'vamk.fi', 'xamk.fi', 'edu.tampere.fi', 'students.oamk.fi',
                                'viikinnormaalikoulu.fi']
LEADER_DOMAINS = [ "aisapari.net", "aktion.fi",
                   "emory.fi",
                   "jetina.fi", "joensuunseudunleader.fi", "jokivarsi.fi", "joutsentenreitti.fi", "jyvasriihi.fi",
                   "kainuuleader.fi", "kalakukkory.fi", "kantriry.fi", "karhuseutu.fi", "karkileader.fi", "keskipisteleader.fi",
                   "koillismaanleader.fi", "kuudestaan.net",
                   "leaderlansisaimaa.fi", "leadersuupohja.fi", "liiveri.net", "linnaseutu.fi", "lounaplussa.fi",
                   "mansikkary.fi",
                   "nousevarannikkoseutu.fi",
                   "oulujarvileader.fi", "oulunseudunleader.fi", "outokaira.fi",
                   "paijanne-leader.fi", "perapohjola.fi", "pirityiset.fi", "pirkanhelmi.fi", "pll.fi", "pohjois-kymenkasvu.fi",
                   "pokory.fi", "pomovast.fi", "pyhajarviseutu.fi",
                   "rajupusuleader.fi", "ravakka.fi", "rieskaleader.fi",
                   "sameboat.fi", "sepra.fi", "silmu.info",
                   "tunturileader.fi",
                   "varsinhyva.fi", "veejjakaja.fi", "vesuri-ryhma.fi",
                   "yhyres.fi", "ykkosakseli.fi", "ylasavonveturi.fi"]
VILLAGE_DOMAINS = [ "suomenkylat.fi", "hameenkylat.fi", "kainuunnuotta.net", "kaustisenseutukunta.fi", "keskisuomenkylat.fi", "kostiry.fi",
                 "kylat.fi", "kymenlaaksonkylat.fi", "lappilaisetkylat.fi", "phkylat.fi", "pirkankylat.fi", "pohjois-savonkylat.fi", "ppkylat.fi",
                 "uudenmaankylat.fi", "vskylat.fi",
                 "pinsioseura.fi"]
RY_DOMAINS = ["kapsi.fi", "hacklab.fi", "nullroute.fi", 'iki.fi', "fixme.fi", "far.fi", "modeemi.fi", "jkry.org", "testausserveri.fi",
              "ellipsis.fi"] + LEADER_DOMAINS + VILLAGE_DOMAINS
ISP_DOMAINS = ["*.inet.fi", "kolumbus.fi", "elisanet.fi", "saunalahti.fi", "netti.fi", "nic.fi", "netikka.fi", "sci.fi",
               "anvianet.fi", "kymp.net", "jippii.fi", "kotinet.com", "eunet.fi", "welho.com", "mailsuomi.com", "japo.fi", 
               "cuitunet.fi", "telemail.fi", "viesti.net", "meili.fi", "baari.net", "hyrynsalmi.net", "kajaani.net",
               "k-maa.net", "kuhmo.net", "paltamo.net", "phnet.fi", "pkarjala.net", "puolanka.net", "ristijarvi.net", "sotkamo.net",
               "suomussalmi.net", "tutka.net", "mail.tutka.net", "vaala.net", "vuokatti.net", "vuolijoki.net"]
CITY_DOMAINS = ["hel.fi", "vaasa.fi", "tampere.fi", "*.ouka.fi", "turku.fi", "kaarina.fi", "kokkola.fi", "hyvinkaa.fi",
                "hankasalmi.fi","kankaanpaa.fi","lieksa.fi","nokiankaupunki.fi","saarijarvi.fi","savonlinna.fi","sodankyla.fi",
                "jarvenpaa.fi", "toivakka.fi", "jyvaskyla.fi", "kuopio.fi"]

PRESS_DOMAINS = ["skrolli.fi", "mikrobitti.fi", "almamedia.fi", "tivi.fi", "siivet.fi", "aamulehti.fi", "helsinginsanomat.fi", "almatalent.fi", "is.fi", "iltalehti.fi"]

LABOR_UNION_DOMAINS = ["akava.fi", "tek.fi", "mal-liitto.fi", "agronomiliitto.fi", "akavanerityisalat.fi", "taja.fi", "ayr.fi", "akiliitot.fi",
                       "dtl.fi", "diff.fi", "yty.fi", "ilry.fi", "knt.fi", "ktk-ry.fi", "kuntoutusala.fi", "loimu.fi", "mma.fi",
                       "oaj.fi", "professoriliitto.fi", "paallystoliitto.fi", "talentia.fi", "saval.fi", "safa.fi", "ekonomit.fi",
                       "sell.fi", "farmasialiitto.fi", "suomenfysioterapeutit.fi", "hammaslaakariliitto.fi", "juristiliitto.fi",
                       "laakariliitto.fi", "psyli.fi", "puheterapeuttiliitto.fi", "terveydenhoitajaliitto.fi", "toimintaterapeuttiliitto.fi",
                       "tieteentekijat.fi", "tradenomi.fi", "upseeriliitto.fi", "yka.fi", "tyoterveyshoitajat.fi", "sak.fi", "aliupseeriliitto.fi",
                       "jhl.fi", "pam.fi", "rtu.fi", "sjry.fi", "sllpilots.fi", "muusikkojenliitto.fi", "teme.fi", "teollisuusliitto.fi", "iau.fi",
                       "esimiesliitto.com", "akt.fi", "smu.fi", "paperiliitto.fi", "pau.fi", "rakennusliitto.fi", "raury.fi", "selry.fi",
                       "sahkoliitto.fi", "tulliliitto.fi", "vankilavirkailija.fi", "sttk.fi", "jytyliitto.fi", "kthliitto.fi", 
                       "proliitto.fi", "kirkonalat.fi", "mvl.fi", "luva.fi", "metsaasiantuntijat.fi", "ria.fi", "konepaallystoliitto.fi",
                       "superliitto.fi", "seacommand.fi", "spal.fi", "tehy.fi", "erto.fi"]

SCIENTIFIC_INSTITUTION_DOMAINS = ["labore.fi", "ptt.fi", "etla.fi"]

OTHER_DOMAINS = ["assembly.org", "ideavideo.fi", "tux.fi", "maaseutu.fi",
                 "gov.fi", "ohops.net", "somby.fi", "kela.fi"] + LABOR_UNION_DOMAINS + SCIENTIFIC_INSTITUTION_DOMAINS

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
        ak_logger.error(f"The email validation has occurred an exception during execution. The exception: {e}")
        ak_message("Sähköpostiosoitteen validoinnissa tapahtui odottamaton virhe.")
        return False

return check_if_exists(context['prompt_data']['email'])

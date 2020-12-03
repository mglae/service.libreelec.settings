# SPDX-License-Identifier: GPL-2.0
# Copyright (C) 2020-present Team LibreELEC
import config
import os
import subprocess

REGDOM_CONF = os.path.join(config.CONFIG_CACHE, 'regdomain.conf')
REGDOM_DEFAULT = 'NOT SET (DEFAULT)'
REGDOM_LIST = [
    REGDOM_DEFAULT,
    "GLOBAL (00)",
    "Afghanistan (AF)",
    "Albania (AL)",
    "Algeria (DZ)",
    "American Samoa (AS)",
    "Andorra (AD)",
    "Anguilla (AI)",
    "Argentina (AR)",
    "Armenia (AM)",
    "Aruba (AW)",
    "Australia (AU)",
    "Austria (AT)",
    "Azerbaijan (AZ)",
    "Bahamas (BS)",
    "Bahrain (BH)",
    "Bangladesh (BD)",
    "Barbados (BB)",
    "Belarus (BY)",
    "Belgium (BE)",
    "Belize (BZ)",
    "Bermuda (BM)",
    "Bhutan (BT)",
    "Bolivia (BO)",
    "Bosnia and Herzegovina (BA)",
    "Brazil (BR)",
    "Brunei Darussalam (BN)",
    "Bulgaria (BG)",
    "Burkina Faso (BF)",
    "Cambodia (KH)",
    "Canada (CA)",
    "Cayman Islands (KY)",
    "Central African Republic (CF)",
    "Chad (TD)",
    "Chile (CL)",
    "China (CN)",
    "Christmas Island (CX)",
    "Colombia (CO)",
    "Costa Rica (CR)",
    "Côte d'Ivoire (CI)",
    "Croatia (HR)",
    "Cyprus (CY)",
    "Czechia (CZ)",
    "Denmark (DK)",
    "Dominica (DM)",
    "Dominican Republic (DO)",
    "Ecuador (EC)",
    "Egypt (EG)",
    "El Salvador (SV)",
    "Estonia (EE)",
    "Ethiopia (ET)",
    "Finland (FI)",
    "France (FR)",
    "French Guiana (GF)",
    "French Polynesia (PF)",
    "Georgia (GE)",
    "Germany (DE)",
    "Ghana (GH)",
    "Greece (GR)",
    "Greenland (GL)",
    "Grenada (GD)",
    "Guadelope (GP)",
    "Guam (GU)",
    "Guatemala (GT)",
    "Guyana (GY)",
    "Haiti (HT)",
    "Honduras (HN)",
    "Hong Kong (HK)",
    "Hungary (HU)",
    "Iceland (IS)",
    "India (IN)",
    "Indonesia (ID)",
    "Iran (IR)",
    "Ireland (IE)",
    "Israel (IL)",
    "Italy (IT)",
    "Jamaica (JM)",
    "Japan (JP)",
    "Jordan (JO)",
    "Kazakhstan (KZ)",
    "Kenya (KE)",
    "Korea (North) (KP)",
    "Korea (South) (KR)",
    "Kuwait (KW)",
    "Latvia (LV)",
    "Lebanon (LB)",
    "Lesotho (LS)",
    "Liechtenstein (LI)",
    "Lithuania (LT)",
    "Luxembourg (LU)",
    "Macao (MO)",
    "Malawi (MW)",
    "Malaysia (MY)",
    "Malta (MT)",
    "Marshall Islands (MH)",
    "Martinique (MQ)",
    "Mauritania (MR)",
    "Mauritius (MU)",
    "Mayotte (YT)",
    "Mexico (MX)",
    "Micronesian (FM)",
    "Moldova (MD)",
    "Monaco (MC)",
    "Mongolia (MN)",
    "Montenegro (ME)",
    "Morocco (MA)",
    "Nepal (NP)",
    "Netherlands (NL)",
    "New Zealand (NZ)",
    "Nicaragua (NI)",
    "North Macedonia (MK)",
    "Northern Mariana Islands (MP)",
    "Norway (NO)",
    "Oman (OM)",
    "Pakistan (PK)",
    "Palau (PW)",
    "Panama (PA)",
    "Papua New Guinea (PG)",
    "Paraguay (PY)",
    "Peru (PE)",
    "Philipines (PH)",
    "Poland (PL)",
    "Portugal (PT)",
    "Puerto Rico (PR)",
    "Qatar (QA)",
    "Réunion (RE)",
    "Romania (RO)",
    "Russian Federation (RU)",
    "Rwanda (RW)",
    "Saint Barthélemy (BL)",
    "Saint Kitts and Nevis (KN)",
    "Saint Lucia (LC)",
    "Saint Martin (MF)",
    "Saint Pierre and Miquelon (PM)",
    "Saint Vincent and the Grenadines (VC)",
    "Saudi Arabia (SA)",
    "Senegal (SN)",
    "Serbia (RS)",
    "Singapore (SG)",
    "Slovakia (SK)",
    "Slovenia (SI)",
    "South Africa (ZA)",
    "Spain (ES)",
    "Sri Lanka (LK)",
    "Suriname (SR)",
    "Sweden (SE)",
    "Switzerland (CH)",
    "Syria (SY)",
    "Taiwan (TW)",
    "Thailand (TH)",
    "Togo (TG)",
    "Trinidan and Tobago (TT)",
    "Tunisia (TN)",
    "Turkey (TR)",
    "Turks and Caicos Islands (TC)",
    "Uganda (UG)",
    "Ukraine (UA)",
    "United Arab Emirates (AE)",
    "United Kingdom (GB)",
    "United States (US)",
    "Uraguay (UY)",
    "Uzbekistan (UZ)",
    "Vanuatu (VU)",
    "Venzuela (VE)",
    "Vietnam (VN)",
    "Virgin Islands (VI)",
    "Wallis and Futuna (WF)",
    "Yemen (YE)",
    "Zimbabwe (ZW)"
]

def get_regdom():
    if not os.path.isfile(REGDOM_CONF):
        return REGDOM_DEFAULT
    conf = open(REGDOM_CONF).readline().rstrip()
    code = conf[-2:]
    regdom = next((l for l in REGDOM_LIST if code in l), REGDOM_DEFAULT)
    return regdom

def set_regdom(regdom):
    if regdom == REGDOM_DEFAULT:
        code = '00'
        if os.path.isfile(REGDOM_CONF):
            os.remove(REGDOM_CONF)
    else:
        code = regdom[-3:-1]
        with open(REGDOM_CONF, 'w') as file:
            file.write(f'REGDOMAIN={code}\n')
    subprocess.check_output(f'iw reg set {code}'.split())

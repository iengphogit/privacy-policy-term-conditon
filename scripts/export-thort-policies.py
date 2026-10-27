#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Export Thort's bundled policy text plus web/contact disclosures as static HTML."""
import argparse
import html
import json
import plistlib
import re
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument('app_root', type=Path, help='Thort source checkout (internal UnifyCAM directory)')
args = parser.parse_args()
root = Path(__file__).resolve().parent.parent
app = args.app_root
source = (app / 'UnifyCAM/Views/AboutView.swift').read_text()
khmer = json.loads((app / 'Localization/legal-km.json').read_text())
with (app / 'UnifyCAM/Resources/Info.plist').open('rb') as f:
    info = plistlib.load(f)
version = info['CFBundleShortVersionString']
updated = {'en': 'Updated: October 27, 2026', 'km': 'កែប្រែថ្ងៃទី 27 តុលា 2026'}
contact = '<a href="mailto:iengpho@gmail.com">iengpho@gmail.com</a>'
github = '<a href="https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement">GitHub General Privacy Statement</a>'
eula = '<a href="https://www.apple.com/legal/internet-services/itunes/dev/stdeula/">Apple Standard EULA</a>'

def esc(text):
    return html.escape(text, quote=True)

def sections(kind, language):
    block = re.search(r'case \.' + kind + r': \[(.*?)\n        \]', source, re.S)
    if not block:
        raise ValueError(f'Missing bundled {kind} content')
    result = []
    for title, body in re.findall(r'\.init\(title: "([^"]+)", text: "([^"]+)"\)', block.group(1)):
        if language == 'km':
            title, body = khmer[title]
        result.append((title, esc(body)))
    assert len(result) >= 7
    return result

labels = {
    'en': {'privacy': 'Privacy Policy', 'terms': 'Terms & Conditions', 'home': 'Thort documents', 'locale': 'ភាសាខ្មែរ · KH'},
    'km': {'privacy': 'គោលការណ៍ឯកជនភាព', 'terms': 'លក្ខខណ្ឌប្រើប្រាស់', 'home': 'ឯកសារ Thort', 'locale': 'English · EN'},
}
filenames = {'privacy': 'thort-privacy-policy.html', 'terms': 'thort-terms-and-conditions.html'}

common = {
 'en': [
  ('Developer and contact', 'Thort (ថត) is an independent iPhone camera, composition and video-editing app developed by PHO IENG, an individual developer in Cambodia. These documents describe version ' + esc(version) + '. Bundle ID: <code>space.iengpho.thort</code>. For support or privacy questions, contact ' + contact + '.'),
 ],
 'km': [
  ('អ្នកអភិវឌ្ឍ និងទំនាក់ទំនង', 'Thort (ថត) ជាកម្មវិធីកាមេរ៉ា រៀបចំប្លង់ និងកែវីដេអូឯករាជ្យសម្រាប់ iPhone ដែលអភិវឌ្ឍដោយ PHO IENG អ្នកអភិវឌ្ឍឯករាជ្យនៅកម្ពុជា។ ឯកសារទាំងនេះពន្យល់អំពីកំណែ ' + esc(version) + '។ Bundle ID៖ <code>space.iengpho.thort</code>។ សម្រាប់ជំនួយ ឬសំណួរឯកជនភាព សូមទាក់ទង ' + contact + '។'),
 ],
}
privacy_extra = {
 'en': [
  ('Connection choices', 'You choose the MJPEG or HLS stream address to connect to. HTTP is limited to local network addresses and names by the app, and is unencrypted. Use HTTPS for internet endpoints and whenever the camera supports it. Camera credentials authenticate to that camera or stream provider; they are not a Thort user account. The app does not include public CCTV addresses, camera passwords, or a developer-operated video relay.'),
  ('Support correspondence', 'If you contact PHO IENG, the developer receives the email address, message and attachments you voluntarily send and uses them to handle your request. Correspondence is kept only as needed to respond, maintain relevant support records, or meet applicable obligations. You can request access, correction or deletion by emailing ' + contact + '; applicable obligations may limit a request. Do not send passwords, private stream URLs, access tokens or unnecessary private footage. The developer has no automatic copy of your local recordings to retrieve or delete.'),
  ('This public website', 'These pages are hosted by GitHub Pages. They use locally hosted fonts and contain no advertising, analytics scripts, forms, or tracking cookies added by the developer. GitHub processes website visitor information separately, including connection and usage information, under its ' + github + '. Opening this website is separate from local camera recording. The app also includes offline policy text; viewing the offline copy does not send your recordings to GitHub.'),
 ],
 'km': [
  ('ជម្រើសការភ្ជាប់', 'អ្នកជ្រើសអាសយដ្ឋានវីដេអូ MJPEG ឬ HLS ដែលត្រូវភ្ជាប់។ កម្មវិធីអនុញ្ញាត HTTP តែសម្រាប់អាសយដ្ឋាន និងឈ្មោះក្នុងបណ្ដាញមូលដ្ឋាន ហើយវាមិនអ៊ិនគ្រីបទេ។ ប្រើ HTTPS សម្រាប់ប្រភពនៅលើអ៊ីនធឺណិត និងនៅពេលកាមេរ៉ាគាំទ្រ។ ព័ត៌មានចូលប្រើកាមេរ៉ាប្រើដើម្បីផ្ទៀងផ្ទាត់ជាមួយកាមេរ៉ា ឬអ្នកផ្ដល់វីដេអូនោះ មិនមែនជាគណនីអ្នកប្រើ Thort ទេ។ កម្មវិធីមិនភ្ជាប់អាសយដ្ឋាន CCTV សាធារណៈ ពាក្យសម្ងាត់កាមេរ៉ា ឬម៉ាស៊ីនបញ្ជូនវីដេអូរបស់អ្នកអភិវឌ្ឍទេ។'),
  ('សារស្នើជំនួយ', 'បើអ្នកទាក់ទង PHO IENG អ្នកអភិវឌ្ឍទទួលអាសយដ្ឋានអ៊ីមែល សារ និងឯកសារភ្ជាប់ដែលអ្នកផ្ញើដោយស្ម័គ្រចិត្ត ដើម្បីដោះស្រាយសំណើរបស់អ្នក។ សារទាំងនេះរក្សាទុកតែដរាបណាចាំបាច់សម្រាប់ឆ្លើយតប រក្សាកំណត់ត្រាជំនួយដែលពាក់ព័ន្ធ ឬបំពេញកាតព្វកិច្ចដែលអនុវត្ត។ អ្នកអាចស្នើចូលមើល កែតម្រូវ ឬលុបតាម ' + contact + '។ កាតព្វកិច្ចដែលអនុវត្តអាចកំណត់សំណើមួយចំនួន។ កុំផ្ញើពាក្យសម្ងាត់ អាសយដ្ឋានវីដេអូឯកជន សោចូលប្រើ ឬវីដេអូឯកជនដែលមិនចាំបាច់។ អ្នកអភិវឌ្ឍគ្មានច្បាប់ចម្លងវីដេអូក្នុងឧបករណ៍របស់អ្នកដោយស្វ័យប្រវត្តិសម្រាប់យកមកវិញ ឬលុបទេ។'),
  ('គេហទំព័រសាធារណៈនេះ', 'ទំព័រទាំងនេះបង្ហោះនៅ GitHub Pages។ វាប្រើពុម្ពអក្សរដែលបង្ហោះនៅគេហទំព័រនេះ និងគ្មានការផ្សាយពាណិជ្ជកម្ម ស្គ្រីបវិភាគ ទម្រង់បំពេញ ឬខូគីតាមដានដែលបន្ថែមដោយអ្នកអភិវឌ្ឍទេ។ GitHub ដំណើរការព័ត៌មានអ្នកចូលមើលគេហទំព័រដោយឡែក រួមទាំងព័ត៌មានភ្ជាប់ និងការប្រើប្រាស់ តាម ' + github + '។ ការបើកគេហទំព័រនេះដាច់ដោយឡែកពីការថតកាមេរ៉ាក្នុងឧបករណ៍។ កម្មវិធីក៏មានអត្ថបទគោលការណ៍សម្រាប់អានក្រៅបណ្ដាញដែរ។ ការមើលច្បាប់ចម្លងក្រៅបណ្ដាញមិនផ្ញើវីដេអូរបស់អ្នកទៅ GitHub ទេ។'),
 ],
}
terms_extra = {
 'en': [
  ('External cameras and other services', 'Connect to a camera or stream only when you own it or have permission from its operator to access and record it. A reachable address or publicly visible camera webpage alone does not establish that permission. Respect the operator\'s conditions and the rights of people shown. You are responsible for the stream addresses and credentials you provide. Thort does not supply third-party footage or promise that a particular camera service will remain available.'),
  ('Current IP-camera scope', 'This version receives HTTP(S) MJPEG and HLS video. Direct RTSP, USB cameras, ONVIF discovery, remote lens controls and PTZ are not supported. An RTSP source needs a separately configured relay. IP-stream sound is not recorded; audio comes from the selected iPhone microphone. Network delay and buffering mean different sources are not synchronized at exposure time. Network loss may stop a take; reconnection does not automatically restart recording.'),
  ('Privacy and help', 'The <a href="thort-privacy-policy.html">Privacy Policy</a> explains local processing, permissions, IP connections, storage and exports. Questions about these terms or the app can be sent to ' + contact + '. For an App Store distribution, see ' + eula + '. These pages do not state that the app has been approved or released on the App Store.'),
 ],
 'km': [
  ('កាមេរ៉ាខាងក្រៅ និងសេវាផ្សេង', 'ភ្ជាប់ទៅកាមេរ៉ា ឬប្រភពវីដេអូតែពេលអ្នកជាម្ចាស់ ឬមានការអនុញ្ញាតពីអ្នកគ្រប់គ្រងដើម្បីចូលមើល និងថត។ អាសយដ្ឋានដែលអាចចូលបាន ឬគេហទំព័រកាមេរ៉ាដែលអាចមើលជាសាធារណៈតែឯង មិនមានន័យថាមានការអនុញ្ញាតនោះទេ។ គោរពលក្ខខណ្ឌអ្នកគ្រប់គ្រង និងសិទ្ធិមនុស្សដែលបង្ហាញក្នុងវីដេអូ។ អ្នកទទួលខុសត្រូវចំពោះអាសយដ្ឋាន និងព័ត៌មានចូលប្រើដែលអ្នកផ្ដល់។ Thort មិនផ្ដល់វីដេអូភាគីទីបី ឬធានាថាសេវាកាមេរ៉ាណាមួយនឹងនៅតែអាចប្រើបានទេ។'),
  ('ដែនកំណត់កាមេរ៉ា IP បច្ចុប្បន្ន', 'កំណែនេះទទួលវីដេអូ HTTP(S) MJPEG និង HLS។ RTSP ផ្ទាល់ កាមេរ៉ា USB ការស្វែងរក ONVIF ការបញ្ជាឡេនពីចម្ងាយ និង PTZ មិនត្រូវបានគាំទ្រទេ។ ប្រភព RTSP ត្រូវការម៉ាស៊ីនបញ្ជូនដែលកំណត់ដោយឡែក។ សំឡេងពីប្រភព IP មិនត្រូវបានថតទេ។ សំឡេងមកពីមីក្រូហ្វូន iPhone ដែលអ្នកជ្រើស។ ការយឺតបណ្ដាញ និងការរក្សាទិន្នន័យបណ្ដោះអាសន្នធ្វើឱ្យប្រភពផ្សេងៗមិនថតនៅពេលដូចគ្នាពិតប្រាកដទេ។ ការដាច់បណ្ដាញអាចបញ្ឈប់ការថត ហើយការភ្ជាប់ឡើងវិញមិនចាប់ផ្ដើមថតដោយស្វ័យប្រវត្តិទេ។'),
  ('ឯកជនភាព និងជំនួយ', '<a href="thort-privacy-policy.html">គោលការណ៍ឯកជនភាព</a> ពន្យល់អំពីដំណើរការក្នុងឧបករណ៍ សិទ្ធិ ការភ្ជាប់ IP ការផ្ទុក និងការនាំចេញ។ សំណួរអំពីលក្ខខណ្ឌនេះ ឬកម្មវិធីអាចផ្ញើទៅ ' + contact + '។ សម្រាប់ការចែកចាយតាម App Store សូមមើល ' + eula + '។ ទំព័រទាំងនេះមិនបញ្ជាក់ថាកម្មវិធីបានទទួលការអនុម័ត ឬចេញផ្សាយលើ App Store ទេ។'),
 ],
}

def css(prefix):
    return '''@font-face{font-family:Nokora;src:url("''' + prefix + '''fonts/Nokora-Regular.ttf") format("truetype");font-weight:400;font-display:swap}@font-face{font-family:Nokora;src:url("''' + prefix + '''fonts/Nokora-Bold.ttf") format("truetype");font-weight:700;font-display:swap}*{box-sizing:border-box}body{margin:0;background:#f4f7fb;color:#17283b;font:17px/1.8 system-ui,-apple-system,sans-serif}html[lang=km] body,[lang=km]{font-family:Nokora,system-ui,sans-serif}main{max-width:850px;margin:40px auto;padding:36px;background:#fff;border:1px solid #dce5ef;border-radius:16px}nav{display:flex;flex-wrap:wrap;gap:12px 24px;font-size:15px}a{color:#145acb;text-underline-offset:3px;overflow-wrap:anywhere}a:focus-visible{outline:3px solid #145acb;outline-offset:4px}h1{font-size:clamp(29px,5vw,40px);line-height:1.45;margin:24px 0 12px}h2{font-size:22px;line-height:1.6;margin:30px 0 10px}p{margin:10px 0}code{overflow-wrap:anywhere;font-size:.92em}.eyebrow{color:#145acb;font-weight:700;margin-top:24px}.updated,footer{color:#526174;font-size:15px}footer{border-top:1px solid #dce5ef;margin-top:36px;padding-top:20px}.links{padding-left:24px}.links li{margin:14px 0}@media(max-width:600px){main{margin:0;border:0;border-radius:0;padding:24px 20px}}@media print{body{background:white}main{border:0;margin:0;padding:0}nav{display:none}a{color:inherit}}'''

def page(kind, language):
    prefix = '../' if language == 'km' else ''
    filename = filenames[kind]
    alternate = '../' + filename if language == 'km' else 'km/' + filename
    label = labels[language]
    body = common[language] + sections(kind, language)
    present = {title for title, _ in body}
    body += [(title, text) for title, text in (privacy_extra if kind == 'privacy' else terms_extra)[language] if title not in present]
    content = '\n'.join('<section><h2>' + esc(title) + '</h2><p>' + text + '</p></section>' for title, text in body)
    return f'''<!doctype html>
<html lang="{language}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="referrer" content="no-referrer"><meta http-equiv="Content-Security-Policy" content="default-src 'none'; style-src 'unsafe-inline'; font-src 'self'; base-uri 'none'; form-action 'none'">
<title>Thort (ថត) — {esc(label[kind])}</title><style>{css(prefix)}</style></head><body><main>
<nav aria-label="Thort"><a href="{prefix}thort.html">{esc(label['home'])}</a><a href="{filenames['privacy']}">{esc(label['privacy'])}</a><a href="{filenames['terms']}">{esc(label['terms'])}</a><a href="{alternate}" lang="{'en' if language == 'km' else 'km'}">{label['locale']}</a></nav>
<p class="eyebrow">Thort (ថត)</p><h1>{esc(label[kind])}</h1><p class="updated">{updated[language]} · {esc(version)}</p>
{content}
<footer>© 2026 PHO IENG · Cambodia<br>Nokora · Copyright 2019 The Nokora Project Authors · <a href="{prefix}licenses/Nokora-OFL-1.1.txt">SIL Open Font License 1.1</a></footer>
</main></body></html>
'''

for language in ['en', 'km']:
    directory = root if language == 'en' else root / 'km'
    directory.mkdir(exist_ok=True)
    for kind, filename in filenames.items():
        (directory / filename).write_text(page(kind, language))

hub = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="referrer" content="no-referrer"><meta http-equiv="Content-Security-Policy" content="default-src 'none'; style-src 'unsafe-inline'; font-src 'self'; base-uri 'none'; form-action 'none'"><title>Thort (ថត) — Privacy & Terms</title><style>{css('')}</style></head><body><main>
<p class="eyebrow">Thort@Cambodia</p><h1>Thort (ថត)</h1><p>Camera composition and recording for iPhone. Developed by PHO IENG.</p><p class="updated">Documents for version {esc(version)} · October 27, 2026<br>Bundle ID: <code>space.iengpho.thort</code></p>
<section lang="en"><h2>English</h2><ul class="links"><li><a href="thort-privacy-policy.html">Privacy Policy</a></li><li><a href="thort-terms-and-conditions.html">Terms &amp; Conditions</a></li></ul></section>
<section lang="km"><h2>ភាសាខ្មែរ</h2><ul class="links"><li><a href="km/thort-privacy-policy.html">គោលការណ៍ឯកជនភាព</a></li><li><a href="km/thort-terms-and-conditions.html">លក្ខខណ្ឌប្រើប្រាស់</a></li></ul></section>
<p>Support and privacy: {contact}</p><p class="updated">These documents describe the app’s current behavior. Publication does not indicate an App Store release or approval.</p>
<footer>© 2026 PHO IENG · Cambodia<br>Nokora · Copyright 2019 The Nokora Project Authors · <a href="licenses/Nokora-OFL-1.1.txt">SIL Open Font License 1.1</a></footer>
</main></body></html>
'''
(root / 'thort.html').write_text(hub)
print('Generated Thort document hub and four EN/KH policy pages.')

# SketchPORT legal documents

Public HTML copies of the bundled EN/KM documents for SketchPORT 0.18. Operator: PHO ieng, an individual developer in Cambodia. Support and privacy: iengpho@gmail.com.

The documents describe the current app: educational use for ages 13+, local projects, optional direct DeepSeek requests, protected API-key storage, consent, retention/deletion and hardware safety. They do not advertise future PRO features. Publication does not certify legal compliance or Play approval.

## Hosting and synchronization

GitHub Pages: main branch, root folder.

Privacy URL: https://iengphogit.github.io/privacy-policy-term-conditon/sketch-port-privacy-policy.html

Khmer privacy URL: https://iengphogit.github.io/privacy-policy-term-conditon/km/sketch-port-privacy-policy.html

Generate the six HTML pages from the app assets with `scripts/export-store-policies.py` in the app repository, then copy the exported pages, fonts and licenses here. Keep the app copy, web copy and Play Data Safety declaration consistent. App code, signing materials and credentials do not belong in this repository.

Primary filenames use the `sketch-port-` prefix. Older privacy.html, terms.html and education.html addresses redirect to those filenames.

Nokora Regular/Bold are bundled unmodified under SIL Open Font License 1.1, with the original copyright and full license in `licenses/Nokora-OFL-1.1.txt`. Fonts load from this site only. No advertising or analytics scripts are included.

## AirZcreen Desktop

AirZcreen Desktop 0.1.0 is a separate free macOS app by PHO IENG, an individual developer in Cambodia. Its documents describe owned-virtual-display streaming, transient local processing, no SMS or analytics, local HTTP limitations, and voluntary support correspondence.

- [AirZcreen Desktop Privacy Policy](https://iengphogit.github.io/privacy-policy-term-conditon/airzcreen-desktop-privacy-policy.html)
- [AirZcreen Desktop Support](https://iengphogit.github.io/privacy-policy-term-conditon/airzcreen-desktop-support.html)

These two static pages use system fonts, contain no JavaScript, trackers, forms, or external assets, and disclose GitHub Pages hosting separately from the local app. Existing SketchPORT documents remain specific to SketchPORT.

To synchronize these pages, run `python3 scripts/export-store-pages.py <policy-repository>` in the AirZcreen Desktop source checkout. The privacy content comes from `Sources/AirZcreenDesktop/Legal/privacy.txt`, also packaged offline in the app. Support content comes from `Support/AppStore/support.txt`. Last synchronized: October 26, 2026. Publication does not indicate App Store approval.

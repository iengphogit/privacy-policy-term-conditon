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
- [AirZcreen Desktop User Disclaimer](https://iengphogit.github.io/privacy-policy-term-conditon/airzcreen-desktop-disclaimer.html)

These three static pages use system fonts, contain no JavaScript, trackers, forms, or external assets, and disclose GitHub Pages hosting separately from the local app. Existing SketchPORT documents remain specific to SketchPORT.

To synchronize these pages, run `python3 scripts/export-store-pages.py <policy-repository>` in the AirZcreen Desktop source checkout. The privacy and disclaimer content come from `Sources/AirZcreenDesktop/Legal/privacy.txt` and `Sources/AirZcreenDesktop/Legal/disclaimer.txt`, also packaged offline in the app. Support content comes from `Support/AppStore/support.txt`. Last synchronized: October 26, 2026. Publication does not indicate App Store approval.

## Thort (ថត)

Thort 0.1.0 is an independent iPhone camera, composition and video-editing app by PHO IENG, Cambodia. Bundle ID: `space.iengpho.thort`. Support and privacy: iengpho@gmail.com.

- [Thort document hub](https://iengphogit.github.io/privacy-policy-term-conditon/thort.html)
- [Privacy Policy](https://iengphogit.github.io/privacy-policy-term-conditon/thort-privacy-policy.html)
- [Terms & Conditions](https://iengphogit.github.io/privacy-policy-term-conditon/thort-terms-and-conditions.html)
- [Khmer Privacy Policy](https://iengphogit.github.io/privacy-policy-term-conditon/km/thort-privacy-policy.html)
- [Khmer Terms & Conditions](https://iengphogit.github.io/privacy-policy-term-conditon/km/thort-terms-and-conditions.html)

These static pages explain local camera/microphone processing, clips and exports, selected IP camera connections, device-only Keychain credentials, deletion, responsible recording and device/network limitations. Support correspondence and GitHub Pages hosting are disclosed separately. The pages contain no JavaScript, forms or analytics and use the repository's local Nokora fonts and licence. Other projects' policies remain unchanged. Publication does not imply App Store release or approval.

To regenerate after a reviewed app policy update:

```sh
python3 scripts/export-thort-policies.py /path/to/Thort-source-checkout
```

The internal app source directory is `UnifyCAM`. Core text comes from `UnifyCAM/Views/AboutView.swift` and `Localization/legal-km.json`; the exporter adds web/contact and external-camera-use disclosures. Review both languages and update the exporter date before publishing. Last synchronized: October 27, 2026.

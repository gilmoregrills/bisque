# Changelog

## [0.0.4](https://github.com/gilmoregrills/bisque/compare/v0.0.3...v0.0.4) (2025-12-19)


### Bug Fixes

* add build-base and linux-headers deps ([93d66ea](https://github.com/gilmoregrills/bisque/commit/93d66ead5b50f44cf83f9be6ed5892b3b5021fd2))
* add deps for building psutil ([e83ae69](https://github.com/gilmoregrills/bisque/commit/e83ae6946179517cef82f8a8b31c48002339a079))
* add psutil ([0259859](https://github.com/gilmoregrills/bisque/commit/0259859a5f6ee1fa33aa23d0e6e7196dd9b16fea))
* apk not apt-get oops ([9ba90e2](https://github.com/gilmoregrills/bisque/commit/9ba90e2fe7af2d5c9b8daa6ee49a9f5020684439))
* check process.returncode not error_code ([d4bfb6b](https://github.com/gilmoregrills/bisque/commit/d4bfb6b1a13c4344bf43613fca38abc20ec8068f))
* config file path ([036c773](https://github.com/gilmoregrills/bisque/commit/036c77304e5c7d01236c274bd5b4d956423b6526))
* lint ([b13b4b1](https://github.com/gilmoregrills/bisque/commit/b13b4b17b02e7a8f70b03fda5e42b8edff14bc0f))
* move to subprocess.run to simplify ([60ed820](https://github.com/gilmoregrills/bisque/commit/60ed820afd643176b31a3543995bf951105190c3))
* point at beets config explicitly ([313bcfa](https://github.com/gilmoregrills/bisque/commit/313bcfa89bb30db907e91bb43efb4c127018f20f))
* remove comments, update messages, lint ([051062b](https://github.com/gilmoregrills/bisque/commit/051062b812b38fc681c35f675fc8544f3329c93b))
* remove workdir ([20034a0](https://github.com/gilmoregrills/bisque/commit/20034a0765cbbff8fd3046a1f4c80843725f5da9))
* subprocess.Popen() again so the pid attr is available ([279763e](https://github.com/gilmoregrills/bisque/commit/279763e5b734ed75f18c1034dce7a48ac9a830ed))
* try installing psutil from apk ([4cbbe9c](https://github.com/gilmoregrills/bisque/commit/4cbbe9c668efa551a16ba8627b3c1c1fa4a67ecf))
* try to fire-and-forget beets ([b5958a2](https://github.com/gilmoregrills/bisque/commit/b5958a24cfc3cd2d40f29cd1179154165456ba06))
* try watching for beet subprocesses ([2f44076](https://github.com/gilmoregrills/bisque/commit/2f44076b7409555aff1ecfc39c1b903b35206916))

## [0.0.3](https://github.com/gilmoregrills/bisque/compare/v0.0.2...v0.0.3) (2025-12-18)


### Bug Fixes

* block until beet is complete before responding ([7c9acd1](https://github.com/gilmoregrills/bisque/commit/7c9acd1065253aec5684831959d2cee5e1e6458b))

## [0.0.2](https://github.com/gilmoregrills/bisque/compare/v0.0.1...v0.0.2) (2025-12-18)


### Bug Fixes

* wait for subprocess to finish ([3101efd](https://github.com/gilmoregrills/bisque/commit/3101efd9040308a16a5ce1bb95c797adf09e43b3))

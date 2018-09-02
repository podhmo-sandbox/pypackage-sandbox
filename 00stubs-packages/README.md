see: https://github.com/ethanhs/pep-561

## typed-packagesとstub-package

- typed-packagesは型定義が含まれたパッケージのこと
- stub-packageは対象とするパッケージに対するスタブファイル(型情報)を提供するパッケージのこと

## subs-packages

- .pyiしか使えない
- パッケージ名の"<package name>-stubs" という名前が重要
- setup.pyでpackage_dataの指定が必要


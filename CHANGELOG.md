# Changelog

<!--next-version-placeholder-->

## v0.8.3 (2023-04-10)
### Fix
* Change enqueue and requeue to use different logic ([`c0cd21b`](https://github.com/obscuritylabs/dramatiq-mongodb/commit/c0cd21b0fb1743e1bbe76a6319b76085e4ce2db8))

## v0.8.2 (2023-04-10)
### Fix
* Turns out python3.7 doesn't have = in f-strings ([`caf8b48`](https://github.com/obscuritylabs/dramatiq-mongodb/commit/caf8b48abbd93b5ae632e3c3ea796b1e4005f3df))
* Convert enqueue back to replace with better edge case detection ([`d15ad01`](https://github.com/obscuritylabs/dramatiq-mongodb/commit/d15ad01a44136c5ba4d2db89ded3af4bc729d022))

## v0.8.1 (2023-04-10)
### Fix
* Convert enqueue to insert ([`25a4f71`](https://github.com/obscuritylabs/dramatiq-mongodb/commit/25a4f719f51867b011865d32f14acdcfa1265bc9))

## v0.8.0 (2023-04-10)
### Feature
* Bump dramatic version ([`5235637`](https://github.com/obscuritylabs/dramatiq-mongodb/commit/5235637d64edb0caa63a4890d8ce6f3acd17b99a))

### Fix
* Resolve typing issues from updating dramatiq version ([`5039aca`](https://github.com/obscuritylabs/dramatiq-mongodb/commit/5039aca9e80345ce5e0873010decbd9a1a23f35b))

## v0.7.1 (2023-04-10)
### Fix
* Add exception logging to any mongodb update failure to catch non-atomic operations ([`b5355d6`](https://github.com/obscuritylabs/dramatiq-mongodb/commit/b5355d6b5d93a14393e86b73a1df9df8dec519bf))

## v0.7.0 (2022-12-27)
### Feature
* Add python 3.11 support to CI ([`3744ad8`](https://github.com/obscuritylabs/dramatiq-mongodb/commit/3744ad8bf0b33fc5f44cd73d980324c33e1defc1))

## v0.6.3 (2022-08-22)
### Fix
* Close mongo client connection when broker is closed ([`263ef66`](https://github.com/obscuritylabs/dramatiq-mongodb/commit/263ef6656e437e109c3faabba8e87ebd64fcef3c))

## v0.6.2 (2022-08-16)
### Fix
* Update type hints for new pymongo stubs ([`f4d24c8`](https://github.com/obscuritylabs/dramatiq-mongodb/commit/f4d24c83eeabb4bc86bfb34386042f3e956a3145))

### Documentation
* Update from taskipy to makefile ([`a68824a`](https://github.com/obscuritylabs/dramatiq-mongodb/commit/a68824ab54db6c7dd2d2c1643192972525b95b48))

## v0.6.1 (2022-06-12)
### Fix
* Clean handling of no remaining tasks on queue ([`cfa4de5`](https://github.com/obscuritylabs/dramatiq-mongodb/commit/cfa4de540b3f704bdbbf4d57cc033c44657b473f))

## v0.6.0 (2022-03-31)
### Feature
* Downgrade pymongo to support latest motor client as well ([`65b38f4`](https://github.com/obscuritylabs/dramatiq-mongodb/commit/65b38f422528560c4006cac61d2aa95486073a9f))

## v0.5.1 (2022-01-14)
### Fix
* Match version in git tag ([`70f6625`](https://github.com/obscuritylabs/dramatiq-mongodb/commit/70f6625c3a11e6b741496aa5c2ee3c1992c2fe40))
* Add pyproject.toml version back into release pipeline ([`62894c1`](https://github.com/obscuritylabs/dramatiq-mongodb/commit/62894c1d9ce071406399d79f119b8219db97295c))

## v0.5.0 (2022-01-14)
### Feature
* Split out the different stages by event type ([`e22765a`](https://github.com/obscuritylabs/dramatiq-mongodb/commit/e22765ac7266854aca83d6c3b43a979c1bb80a59))
* Combine CI and CD pipelines ([`999b67e`](https://github.com/obscuritylabs/dramatiq-mongodb/commit/999b67efc206a3392c39a9fdfcb325587c59384c))

### Fix
* Change conditional for CD pipeline trigger ([`d90b9a1`](https://github.com/obscuritylabs/dramatiq-mongodb/commit/d90b9a13923ad8e2dfa0a7364cec5014d1ff88cc))
* Fix conditional on triggering CD pipeline ([`dae2cb0`](https://github.com/obscuritylabs/dramatiq-mongodb/commit/dae2cb0afb813556d8676901532f04963df058d8))

### Documentation
* Update badge for CI / CD pipeline ([`fd32be2`](https://github.com/obscuritylabs/dramatiq-mongodb/commit/fd32be25a4d870844f3f40fef823ac789ae403cf))

## v0.4.0 (2022-01-14)
### Feature
* Add extra pypi metadata to pyproject.toml ([`fc45455`](https://github.com/obscuritylabs/dramatiq-mongodb/commit/fc45455bf1fbd9823d561ef0070ed408bf55b006))
* Add status badges to README ([`0593e23`](https://github.com/obscuritylabs/dramatiq-mongodb/commit/0593e23fff163a236c178ac5b071480d5c494cda))

### Fix
* Remove signed push from GPG task in CD pipeline ([`9d498fe`](https://github.com/obscuritylabs/dramatiq-mongodb/commit/9d498feda6d0ebd846be987d9c6ed272a3a4490f))

## v0.3.0 (2022-01-14)
### Feature
* Add status badges to README ([#42](https://github.com/obscuritylabs/dramatiq-mongodb/issues/42)) ([`9bc9565`](https://github.com/obscuritylabs/dramatiq-mongodb/commit/9bc9565f62291666b8cb676e180d223b84a9307c))

## v0.2.0 (2022-01-13)
### Feature
* Add mongomock to development dependencies ([#27](https://github.com/obscuritylabs/dramatiq-mongodb/issues/27)) ([`f32874d`](https://github.com/obscuritylabs/dramatiq-mongodb/commit/f32874d8ed4af25e4f98e651526cb702ced17f26))
* Bring over initial MVP code from local prototype ([`2621cfc`](https://github.com/obscuritylabs/dramatiq-mongodb/commit/2621cfc9da0840a75a1cfd9c0eba7e61dc60c8ae))
* **boilerplate:** Create pyproject.toml scaffolding with additional requirements ([`a0ba5f0`](https://github.com/obscuritylabs/dramatiq-mongodb/commit/a0ba5f0f9179e72006e03ae827b62961f43c0dbc))
* **boilerplate:** Initialize repository with boilerplate for new project ([`307b2b7`](https://github.com/obscuritylabs/dramatiq-mongodb/commit/307b2b73b679400ef32bc45e074a42ca220e9244))

### Fix
* Main is the main branch, master is a deprecated term ([#34](https://github.com/obscuritylabs/dramatiq-mongodb/issues/34)) ([`95f83ff`](https://github.com/obscuritylabs/dramatiq-mongodb/commit/95f83ff3d50d8dfc2cede6e67a05bfa9b33c29b8))
* Clean up development setup ([`5a34b64`](https://github.com/obscuritylabs/dramatiq-mongodb/commit/5a34b648ff3ec7c67ffd5a1c5accb19572b7cf41))
* Remove extra settings file I added by accident ([`dc4c0c7`](https://github.com/obscuritylabs/dramatiq-mongodb/commit/dc4c0c7d16e2c7e9d73a0f2f5c18cd04fe58d438))
* Remove TypeAlias as 3.10 exclusive feature ([`6eed8f2`](https://github.com/obscuritylabs/dramatiq-mongodb/commit/6eed8f25bf40ee6b31cbe66fd89e298241def74e))

### Documentation
* Add Bug Report and Feature Request Templates ([#31](https://github.com/obscuritylabs/dramatiq-mongodb/issues/31)) ([`363e0f3`](https://github.com/obscuritylabs/dramatiq-mongodb/commit/363e0f3d3391397029f64f0fd8478988c1e1e651))
* Format Obscurity Labs LLC Vulnerability Disclosure Policy ([#21](https://github.com/obscuritylabs/dramatiq-mongodb/issues/21)) ([`180326f`](https://github.com/obscuritylabs/dramatiq-mongodb/commit/180326f6e929e34985164ce1bfd6c669ffd7cf33))
* Add contribution instructions ([`c8aaa21`](https://github.com/obscuritylabs/dramatiq-mongodb/commit/c8aaa216262d4b5d24e041c2a23b1b9500d8a7e0))

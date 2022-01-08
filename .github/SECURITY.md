# Obscurity Labs LLC Vulnerability Disclosure Policy

## Introduction

Obscurity Labs LLC welcomes feedback from security researchers and the general public to help improve our security. If you believe you have discovered a vulnerability, privacy issue, exposed data, or other security issues in any of our assets, we want to hear from you. This policy outlines steps for reporting vulnerabilities to us, what we expect, what you can expect from us. bscurity Labs takes security serious to ensure we protect our customers, services, ecosystems and our development community. We ask you to follow responsible disclosure of vulnerabilities outlined in this document.  

## Systems in Scope

This policy applies to any digital assets owned, operated, or maintained by Obscurity Labs LLC.

## Out of Scope

- Assets or other equipment not owned by parties participating in this policy. 

Vulnerabilities discovered or suspected in out-of-scope systems should be reported to the appropriate vendor or applicable authority.

## Our Commitments

When working with us, according to this policy, you can expect us to:

- Respond to your report promptly, and work with you to understand and validate your report;
- Strive to keep you informed about the progress of a vulnerability as it is processed;
- Work to remediate discovered vulnerabilities in a timely manner, within our operational constraints; and
- Extend Safe Harbor for your vulnerability research that is related to this policy.

## Our Expectations

In participating in our vulnerability disclosure program in good faith, we ask that you:

- Play by the rules, including following this policy and any other relevant agreements. If there is any inconsistency between this policy and any other applicable terms, the terms of this policy will prevail;
- Report any vulnerability you’ve discovered promptly;
- Avoid violating the privacy of others, disrupting our systems, destroying data, and/or harming user experience;
- Use only the Official Channels to discuss vulnerability information with us;
- Provide us a reasonable amount of time (at least 90 days from the initial report) to resolve the issue before you disclose it publicly;
- Perform testing only on in-scope systems, and respect systems and activities which are out-of-scope;
- If a vulnerability provides unintended access to data: Limit the amount of data you access to the minimum required for effectively demonstrating a Proof of Concept; and cease testing and submit a report immediately if you encounter any user data during testing, such as Personally Identifiable Information (PII), Personal Healthcare Information (PHI), credit card data, or proprietary information;
- You should only interact with test accounts you own or with explicit permission from the account holder; and
- Do not engage in extortion.  

## Safe Harbor

When conducting vulnerability research, according to this policy, we consider this research conducted under this policy to be:

- Authorized concerning any applicable anti-hacking laws, and we will not initiate or support legal action against you for accidental, good-faith violations of this policy;
- Authorized concerning any relevant anti-circumvention laws, and we will not bring a claim against you for circumvention of technology controls;
- Exempt from restrictions in our Terms of Service (TOS) and/or Acceptable Usage Policy (AUP) that would interfere with conducting security research, and we waive those restrictions on a limited basis; and
- Lawful, helpful to the overall security of the Internet, and conducted in good faith.

You are expected, as always, to comply with all applicable laws. If legal action is initiated by a third party against you and you have complied with this policy, we will take steps to make it known that your actions were conducted in compliance with this policy.

If at any time you have concerns or are uncertain whether your security research is consistent with this policy, please submit a report through one of our Official Channels before going any further.

> Note that the Safe Harbor applies only to legal claims under the control of the organization participating in this policy, and that the policy does not bind independent third parties.

## Official Channels

Please report security issues via mailto:security@obscuritylabs.com, providing all relevant information. The more details you provide, the easier it will be for us to triage and fix the issue.


### Securely Messaging Obscurity Labs
Obscurity Labs uses gpg2 to encrypt and sign messages when necessary. You can find our verifed keybase account here: https://keybase.io/obscuritylabs. The following can be used to ensure you have the proper GPG key:

#### curl + gpg pro tip: import obscuritylabs's keys

```bash
curl https://keybase.io/obscuritylabs/pgp_keys.asc | gpg --import
```

#### The Keybase app can push to gpg keychain, too

```bash
keybase pgp pull obscuritylabs
```

#### Obscurity Labs Key Data

```text
fingerprint:	FE93328EAE28281603777D503336F731A4B04998
64-bit:	3336F731A4B04998

-----BEGIN PGP PUBLIC KEY BLOCK-----

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
=LV1J
-----END PGP PUBLIC KEY BLOCK-----
```

## Security Policy Technical Bits

### Full Vulnerability Disclosure Policy 

Version 2021.1

### Security.txt
Security.txt provides a machine-readable file which defines core attributes or your VDP, and is designed to be hosted on websites.

The security.txt file should be placed under the /.well-known/ path (/.well-known/security.txt) on websites. It can also be placed in the root directory (/security.txt) of a website, especially if the /.well-known/ directory cannot be used for technical reasons or as a fallback. The file can be placed in both locations of a website at the same time.

For more information visit https://securitytxt.org and the associated RFC8615.

### DNS Security.txt

The DNS Security TXT standard provides machine-readable records that define core attributes of your VDP, and is designed to be hosted using DNS TXT records in your domain/s.

Just as security.txt can be deployed into either the root or the .well-known directory of a webserver, DNS Security TXT can be deployed to either the apex of a domain, or under a specially created _security.<domain.com> subdomain. This approach allows organizations to decide the approach that suits them best.

For more information visit https://dnssecuritytxt.org.

| Record name          | Record type  | Value                                                |
|----------------------|--------------|------------------------------------------------------|
| _security.domain.com | TXT          | "security_contact=mailto:security@obscuritylabs.com" |
| _security.domain.com | TXT          | "security_policy=https://obscuritylabs.com/security" |
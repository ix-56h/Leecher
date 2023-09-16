# Leecher - Automated Security Audit Scanner

Disclaimer : Leecher is currently not actively maintained. However, we have plans to revive and enhance it in the near future. Your patience and support are greatly appreciated during this period.

**Leecher** is a potent Python-based security audit scanner, meticulously crafted to empower you with the ability to unearth vulnerabilities and security weaknesses in web applications and websites. This open-source tool combines the prowess of Sublist3r, headless Chrome drivers, CMSScraper, WPScan, and custom tests, transforming the laborious task of subdomain enumeration, permission checks, directory listing scans, and CMS technology detection into a seamless, automated process.

```
     ##                               ##
     ##                               ##
    ##     #####    #####    #####   ##        #####    #####
    ##    #####    #####     ##      ######   #####    ##  ##
   ##    ##       ##        ##      ###  ##  ##        ##
 #####   #######  #######   ######  ##  ##   #######  ##


                        Automated Security Audit

usage: leecher.py [-h] [-t TARGET] [--full-check] [-s] [-v]

options:
  -h, --help            show this help message and exit
  -t TARGET, --target TARGET
                        Set the target
  --full-check          Make a recursive check for all subdomains for all CMS
  -s, --silent          Disable modules output
  -v, --verbose         Verbose mod
```

## Key Features

- **Subdomain Enumeration**: Leecher relies on Sublist3r to diligently uncover subdomains associated with the target domain, providing you with a holistic view of potential entry points.

- **Web Application Scanning**: With the power of headless Chrome drivers, Leecher interacts with web applications, identifying potential vulnerabilities and issues that warrant further investigation.

- **CMS Detection**: Leecher seamlessly identifies the Content Management System (CMS) used by target websites, a crucial step in pinpointing known CMS-specific vulnerabilities.

- **WordPress Vulnerability Scanning**: For WordPress sites, Leecher goes the extra mile by inspecting the CMS version and installed plugins for known vulnerabilities, allowing you to prioritize critical issues.

- **Custom Tests**: Leecher includes meticulously crafted, hand-written tests to check for basic file permission issues, directory listing exposure, and more.

- **Full Check Option**: Deploy the `--full-check` option for a comprehensive security audit, encompassing all available tests in one go.

## Usage

To unleash the power of Leecher, execute `leecher.py` with the following options:

```shell
python leecher.py [-h] [-t TARGET] [--full-check] [-s] [-v]
```

**Options**:

- `-h, --help`: Display the help message and gracefully exit.
- `-t TARGET, --target TARGET`: Set the target domain you wish to scan.
- `--full-check`: Embark on an exhaustive security audit adventure, including all available tests.
- `-s, --silent`: Disable module output for a quieter experience.
- `-v, --verbose`: Increase verbosity for more detailed output.

## Getting Started

1. Begin your journey by cloning the Leecher repository to your local machine:

   ```shell
   git clone https://github.com/yourusername/leecher.git
   ```

2. Next, install the necessary dependencies:

   ```shell
   pip install -r requirements.txt
   ```

3. Now, you're ready to harness the power of Leecher. Run Leecher with your desired options:

   ```shell
   python leecher.py -t example.com --full-check
   ```

## Contributors

Leecher is a collaborative effort, and we're grateful for the contributions from our main contributors:

- [ix-56h](https://github.com/ix-56h)
- [bbellavi](https://github.com/bbellavi)

## Contributing

We wholeheartedly welcome contributions from the community to enhance Leecher's capabilities and keep it in sync with the latest security practices. Whether you want to report issues, submit pull requests, or offer suggestions for improvements, your input is invaluable.

## Disclaimer

Please exercise responsibility and use Leecher only on websites and applications for which you have explicit permission to scan. Unauthorized scanning may violate the law, and the tool should always be employed in compliance with applicable regulations.

## License

Leecher is distributed under the MIT License. Refer to the [LICENSE](LICENSE) file for detailed licensing information.

## Acknowledgments

Leecher wouldn't be possible without the invaluable contributions from the open-source tools it relies on, including Sublist3r, CMSScraper, WPScan, and many others. We extend our heartfelt thanks to the developers and maintainers of these projects for their dedication to the security community.

---

Unlock the potential of Leecher and embark on your journey to secure web applications with confidence. If you encounter any issues or have suggestions for improvements, don't hesitate to reach out. Happy auditing!
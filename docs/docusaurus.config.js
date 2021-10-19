// @ts-check
// Note: type annotations allow type checking and IDEs autocompletion

const lightCodeTheme = require('prism-react-renderer/themes/github');
const darkCodeTheme = require('prism-react-renderer/themes/dracula');

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'py-polymorphic-list',
  tagline: 'Dinosaurs are cool',
  url: 'https://keshprad.github.io/',
  baseUrl: '/py-polymorphic-list/',
  trailingSlash: true,
  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',
  favicon: 'https://keshprad.github.io/my-portfolio/favicon.ico',
  organizationName: 'keshprad', // Usually your GitHub org/user name.
  projectName: 'py-polymorphic-list', // Usually your repo name.

  presets: [
    [
      '@docusaurus/preset-classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          sidebarPath: require.resolve('./sidebars.js'),
          // Please change this to your repo.
          editUrl:
            'https://github.com/keshprad/py-polymorphic-list/edit/main/docs/',
          sidebarCollapsed: false,
        },
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      }),
    ],
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      colorMode: {
        defaultMode: 'dark',
      },
      navbar: {
        title: 'py-polymorphic-list',
        items: [
          {
            type: 'doc',
            docId: 'intro',
            position: 'left',
            label: 'Docs',
          },
          {
            href: 'https://github.com/keshprad/py-polymorphic-list/',
            label: 'GitHub',
            position: 'right',
          },
          {
            href: 'https://pypi.org/project/py-polymorphic-list/',
            label: 'PyPI',
            position: 'right',
          },
        ],
      },
      footer: {
        style: 'dark',
        links: [
          {
            title: 'Docs',
            items: [
              {
                label: 'Intro',
                to: '/docs/intro',
              },
              {
                label: 'Installation',
                to: '/docs/getting-started/installation/',
              },
            ],
          },
          {
            title: 'More',
            items: [
              {
                label: 'PyPI',
                href: 'https://pypi.org/project/py-polymorphic-list/',
              },
              {
                label: 'GitHub',
                href: 'https://github.com/keshprad/py-polymorphic-list',
              },
            ],
          },
        ],
        copyright: `<a href="https://keshprad.ml" target="_blank">keshprad</a> — ${new Date().getFullYear()}. Built with Docusaurus.`,
      },
      prism: {
        theme: lightCodeTheme,
        darkTheme: darkCodeTheme,
      },
    }),
};

module.exports = config;

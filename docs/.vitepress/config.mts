import { defineConfig } from 'vitepress'
import mathjax3 from 'markdown-it-mathjax3';

export default defineConfig({
  title: "My_Torch",
  description: "Documentation officielle du projet My_Torch",
  
  // Configuration pour activer les Maths (LaTeX)
  markdown: {
    config: (md) => {
      md.use(mathjax3);
    }
  },

  themeConfig: {
    sidebar: [
      {
        text: 'Introduction',
        collapsed: false, // Optionnel : garde le menu ouvert par défaut
        items: [
          { text: 'Présentation du Projet', link: '/guide/introduction' },
          { text: 'Benchmarks & Résultats', link: '/benchmarks' },
          { text: 'Installation', link: '/guide/installation' },
          { text: 'Premier Pas', link: '/guide/getting-started' },
          { text: 'Configuration JSON', link: '/guide/configuration' }
        ]
      },
      {
        text: 'Référence',
        collapsed: true, // Optionnel : ferme le menu par défaut pour gagner de la place
        items: [
          { text: 'Command Line Interface', link: '/reference/com_args' },
          { text: 'API Python', link: '/reference/api' }
        ]
      },
      {
        text: 'Comprendre le Moteur',
        collapsed: true,
        items: [
          { text: 'Architecture Globale', link: '/concepts/architecture' },
          { text: 'Mathématiques', link: '/concepts/mathematics' },
          { text: 'Données & Échecs', link: '/concepts/data-processing' }
        ]
      }
    ]
  }
})
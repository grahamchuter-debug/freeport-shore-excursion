tailwind.config = {
  safelist: [
    'h-40', 'h-44', 'grid', 'gap-6', 'gap-12',
    'sm:grid-cols-2', 'lg:grid-cols-3', 'lg:grid-cols-4',
    'card-hover', 'card-media', 'btn-ocean', 'btn-primary', 'btn-outline',
    'rounded-3xl', 'shadow-md', 'border-pr-50', 'border-pr-100',
    'text-ocean-600', 'bg-sand-50', 'bg-amber-50', 'bg-white',
    'aspect-[4/3]', 'aspect-[21/9]',
  ],
  theme: {
    extend: {
      colors: {
        ocean: {
          50:  '#eff6ff',
          100: '#dbeafe',
          200: '#bfdbfe',
          300: '#93c5fd',
          400: '#60a5fa',
          500: '#3b82f6',
          600: '#2563eb',
          700: '#1d4ed8',
          800: '#1e40af',
          900: '#1e3a8a',
        },
        teal: {
          400: '#2dd4bf',
          500: '#14b8a6',
          600: '#0d9488',
        },
        sand: {
          50:  '#fff7ed',
          100: '#ffedd5',
          200: '#fed7aa',
        },
        pr: {
          50:  '#fff7ed',
          100: '#ffedd5',
          200: '#fed7aa',
          300: '#fdba74',
          400: '#fb923c',
          500: '#f97316',
          600: '#ea580c',
          700: '#c2410c',
          800: '#9a3412',
          900: '#7c2d12',
        }
      },
      fontFamily: {
        display: ['Outfit', 'system-ui', 'sans-serif'],
        body:    ['Source Sans 3', 'system-ui', 'sans-serif'],
      },
    }
  }
};

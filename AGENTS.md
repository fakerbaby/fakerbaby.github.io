# Repository Guidelines

## Project Structure & Module Organization
This repository is a Jekyll academic site deployed with GitHub Pages. Content lives in collection folders such as `_pages`, `_posts`, `_talks`, `_teaching`, `_portfolio`, and `_publications`. Shared templates are in `_layouts` and `_includes`; styles live in `_sass` and compile through `assets/css/main.scss`. JavaScript source is `assets/js/_main.js`, and the committed bundle is `assets/js/main.min.js`. Static files belong in `images/`, `cv.pdf`, `talkmap/`, or `files/` if you add downloadable assets.

## Build, Test, and Development Commands
Install Ruby dependencies with `bundle install` and Node tooling with `npm install`. Run the site locally with `bundle exec jekyll serve --config _config.yml,_config.dev.yml`; `_config.dev.yml` switches the URL to `http://localhost:4000` and disables analytics. Rebuild the minified JS bundle with `npm run build:js` after editing `assets/js/_main.js` or plugin files. Use `bundle exec jekyll build` as the main validation step before pushing.

## Coding Style & Naming Conventions
Preserve the existing Jekyll conventions: YAML front matter first, then Markdown or HTML content. Use 2-space indentation in YAML, SCSS, and JavaScript to match the current files. Keep post- and talk-style filenames date-prefixed, for example `_posts/2026-04-20-my-update.md` and `_talks/2026-04-20-talk-title.md`. Use lowercase, hyphen-separated slugs and descriptive front matter keys such as `title`, `permalink`, and `author_profile`.

## Testing Guidelines
There is no separate unit-test suite in this repo. Treat a clean `bundle exec jekyll build` as the required check, and manually verify changed pages in the local server before opening a PR. If you update generated content in `markdown_generator/`, review the emitted Markdown files as part of the same change.

## Commit & Pull Request Guidelines
Recent history uses short, imperative commit subjects like `Update about.md` and `Update _config.yml`; follow that pattern and keep each commit focused. PRs should summarize the user-visible change, list affected directories, and include screenshots for layout or styling updates. If the PR changes shared template or theme code, follow `CONTRIBUTING.md` and link the related closed issue tagged `code change`.

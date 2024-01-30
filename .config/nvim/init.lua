
-- ███╗   ██╗██╗   ██╗ █████╗ ██╗   ██╗██╗███╗   ███╗
-- ████╗  ██║╚██╗ ██╔╝██╔══██╗██║   ██║██║████╗ ████║
-- ██╔██╗ ██║ ╚████╔╝ ███████║██║   ██║██║██╔████╔██║
-- ██║╚██╗██║  ╚██╔╝  ██╔══██║╚██╗ ██╔╝██║██║╚██╔╝██║
-- ██║ ╚████║   ██║   ██║  ██║ ╚████╔╝ ██║██║ ╚═╝ ██║
-- NEOVIM CONFIG BY KIEFCIMAN

require('lazypath')
require('vim-options')
require('lazy').setup('plugins')
require('theme')

vim.cmd('hi LineNr guibg=none guifg=#d9d0ee')

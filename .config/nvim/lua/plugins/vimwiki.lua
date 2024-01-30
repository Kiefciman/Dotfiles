return {
    'vimwiki/vimwiki',
    config = function()
        vim.g.vimwiki_list = {
            {
                path = '~/Documents/vimwiki/',
                syntax = 'markdown',
                ext = '.md'
            }
        }
    end
}

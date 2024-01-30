return { 
    'nvim-treesitter/nvim-treesitter',
    build = ':TSUpdate',
    config = function()
        local configs = require 'nvim-treesitter.configs'
        configs.setup {
            ensure_installed = { "c", "lua", "vim", "vimdoc", "query", "python" },
            sync_install = false,
            auto_install = true,
            ignore_install = {},
            highlight = {
                enable = true,
                disable = {},
                disable = function(lang, buf)
                local max_filesize = 10000 * 1024
                local ok, stats = pcall(vim.loop.fs_stat, vim.api.nvim_buf_get_name(buf))
                if ok and stats and stats.size > max_filesize then
                    return true
                end
            end,
            additional_vim_regex_highlighting = false,
            },
        }
    end
}


return { 
    {
        'williamboman/mason.nvim',
        config = function()
            require('mason').setup()
        end
    },
    {
        'williamboman/mason-lspconfig.nvim',
        config = function()
            require('mason-lspconfig').setup({
                ensure_installed = {
                    'bashls',
                    'clangd',
                    'cssls',
                    'gopls',
                    'html',
                    'jsonls',
                    'tsserver',
                    'lua_ls',
                    'marksman',
                    'jedi_language_server',
                    'yamlls',
                }
            })
        end
    },
    {
        'neovim/nvim-lspconfig',
        config = function()
            -- local capabilities = require('cmp_nvim_lsp').default_capabilities()
            local lspconfig = require('lspconfig')
            lspconfig.bashls.setup({
            --    capabilities = capabilities
            })
            lspconfig.clangd.setup({
            --    capabilities = capabilities
            })
            lspconfig.cssls.setup({
            --    capabilities = capabilities
            })
            lspconfig.gopls.setup({
            --    capabilities = capabilities
            })
            lspconfig.html.setup({
            --    capabilities = capabilities
            })
            lspconfig.jsonls.setup({
            --    capabilities = capabilities
            })
            lspconfig.tsserver.setup({
            --    capabilities = capabilities
            })
            lspconfig.lua_ls.setup({
            --    capabilities = capabilities
            })
            lspconfig.marksman.setup({
            --    capabilities = capabilities
            })
            lspconfig.jedi_language_server.setup({
            --    capabilities = capabilities
            })
            lspconfig.yamlls.setup({
            --    capabilities = capabilities
            })
            vim.keymap.set('n', '<leader>?', vim.lsp.buf.hover, {})
            vim.keymap.set('n', '<leader>.?', vim.lsp.buf.definition, {})
            vim.keymap.set('n', '<leader>..', vim.lsp.buf.code_action, {})
        end
    }
}

return {
    'neoclide/coc.nvim',
    ranch = 'release', -- working, don't touch it!!!!!!
    config = function()
        local opts = {
            silent = true,
            noremap = true,
            expr = true,
            replace_keycodes = false 
        }
        vim.keymap.set("i", "<CR>", function()
            if vim.fn['coc#pum#visible']() == 1 then
                return vim.fn['coc#pum#confirm']();
            end
            return "\r"
        end, opts)
    end
}

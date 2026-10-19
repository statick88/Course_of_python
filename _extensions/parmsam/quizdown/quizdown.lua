local function ensureHtmlDeps()
  quarto.doc.add_html_dependency({
    name = 'quizdown',
        version = '0.6.0',
    scripts = { 
      'assets/quizdown.js',
      'assets/quizdownKatex.js',
      'assets/quizdownHighlight.js',
      'assets/quizdown-init.js'
    }
  })
end

local function escapeHtml(text)
  return text:gsub('&', '&amp;'):gsub('<', '&lt;'):gsub('>', '&gt;')
end

local function quizdownMarkdown(block)
  local normalized = block:walk({
    HorizontalRule = function()
      -- Quizdown reserves `---` for YAML; code-block text is left intact.
      return pandoc.RawBlock('markdown', '***')
    end,
    RawInline = function(inline)
      -- Normalize authored HTML code tags, never literal text inside Code nodes.
      if inline.format == 'html' then
        if inline.text == '<code>' or inline.text == '</code>' then
          return pandoc.RawInline('markdown', '`')
        end
        local text = inline.text:match('^<code>(.-)</code>$')
        if text then return pandoc.Code(text) end
      end
    end
  })
  return pandoc.write(pandoc.Pandoc(normalized.content), 'markdown')
end

function Div(block)
  if block.classes:includes('quizdown') then
    if not quarto.doc.is_format('html') then
      return block
    end
    ensureHtmlDeps()
    return pandoc.RawBlock(
      'html',
      '<div class="quizdown">\n' .. escapeHtml(quizdownMarkdown(block)) .. '\n</div>'
    )
  end
end

function CodeBlock(block)
  if block.classes:includes('{quizdown}') or block.classes:includes('quizdown') then
    ensureHtmlDeps()
    local quizdown_content = block.text
    runScript = pandoc.RawBlock('html', '<div class="quizdown">\n' .. quizdown_content .. '\n</div>')
    return { runScript }
  end
end

if quarto.doc.is_format("html:js") then
  ensureHtmlDeps()
end
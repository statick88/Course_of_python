-- Resolve the homepage compilation date while Pandoc renders the document.
function Meta(meta)
  meta.date = pandoc.MetaString(os.date("%Y-%m-%d"))
  return meta
end

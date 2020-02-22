import os, string, re, unicodedata

def Start():pass

def GetParentDir(directories):
  parent_dirs = {}
  for d in directories:
    try:
      parent = os.path.split(d)[0]
      parent_dirs[parent] = True
    except:pass
  
  if parent_dirs.has_key(''):
    del parent_dirs['']
  return parent_dirs
  
def FindSummary(metadata, paths):
  for path in paths:
    for f in os.listdir(path):
      (fn, ext) = os.path.splitext(f)
      if(fn == 'summary' and not fn.startswith('.') and ext[1:] == "txt"):
        summary_file = os.path.join(path, f)
        c = Core.storage.load(summary_file)
        
        metadata.summary = ' '.join(str(c).split())
        Log("Summary loaded from file %s", summary_file)
  
	

class AnimeMeta(Agent.TV_Shows):
  contributes_to = ['com.plexapp.agents.none','com.plexapp.agents.localmedia']
  #accepts_from =['com.plexapp.agents.none','com.plexapp.agents.localmedia']
  primary_provider = False
  persist_stored_files = False
  name = "Anime Resumen Metadata"
  
  def search(self, results, media, lang):
    results.Append(MetadataSearchResult(id = 'null', name=media.show, score = 100))
    return
    
  def update(self, metadata, media, lang, child_guid=None):
    Log(metadata.summary)
    dirs = {}
    
    for a in media.seasons:
      for t in media.seasons[a].episodes:
        track = media.seasons[a].episodes[t].items[0]
        dirs[os.path.dirname(track.parts[0].file)] = True
    
    Show = GetParentDir(dirs)
    ## Assumes folder structure of
    #     * Artist
    #         * summary.txt
    #         * Album
    #           * summary.txt
    #           * audio tracks
    #     ... etc.
    
    #Log(artist_dir) #debug
    
    FindSummary(metadata, Show) # searches for summary.txt in Artist folder and adds the contents of the text file to the Artist biography
    
    Log("finished")
    return
    

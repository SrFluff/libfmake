# libfmake
fmake's config parser written as a library.

# Functions

`readConfig(configName)` - Returns the values of a config file in a tuple (cc,src,out,msg,say,run)\
`genConfig(configName,overwrite,cc,src,out,msg,say,run)` - Generates a new fmake config with the specified values

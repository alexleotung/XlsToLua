class GlobalCost:
    LUA_HEADER_CONST = """--- this file is generated by program!
--- don't change it manually.
--- source file: %s
--- created at: %s

local _localization_config={
"""
    LUA_END_CONST = """ };
return _localization_config;"""
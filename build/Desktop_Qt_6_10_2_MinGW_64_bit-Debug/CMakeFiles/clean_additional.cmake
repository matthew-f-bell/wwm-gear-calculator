# Additional clean files
cmake_minimum_required(VERSION 3.16)

if("${CONFIG}" STREQUAL "" OR "${CONFIG}" STREQUAL "Debug")
  file(REMOVE_RECURSE
  "CMakeFiles\\wwm-gear-calculator_autogen.dir\\AutogenUsed.txt"
  "CMakeFiles\\wwm-gear-calculator_autogen.dir\\ParseCache.txt"
  "wwm-gear-calculator_autogen"
  )
endif()

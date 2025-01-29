# Detect presence of systemd's sd-daemon

AC_DEFUN([RRA_LIB_SYSTEMD], [
  AC_MSG_CHECKING([whether to enable systemd integration])
  have_systemd="no"

  # Check header first
  AC_CHECK_HEADER([systemd/sd-daemon.h],
    [
      # If the header is present, check for sd_notify symbol in libsystemd
      AC_CHECK_LIB([systemd], [sd_notify], 
        [
          AC_DEFINE([HAVE_SYSTEMD], [1],
            [Define if systemd's sd-daemon is available])
          have_systemd="yes"
        ],
        [
          AC_MSG_WARN([
            libsystemd found, but sd_notify symbol is missing.
            Disabling systemd support.
          ])
        ]
      )
    ],
    [
      AC_MSG_WARN([systemd/sd-daemon.h not found; disabling systemd support.])
    ]
  )

  # If we found and can link systemd, set the library flag
  AS_IF([test "x$have_systemd" = "xyes"], [
    SYSTEMD_LIBS="-lsystemd"
  ], [
    SYSTEMD_LIBS=""
  ])

  # Export for use in Makefiles
  AC_SUBST([SYSTEMD_LIBS])

  # Provide an Automake conditional for conditional compilation
  AM_CONDITIONAL([WITH_SYSTEMD], [test "x$have_systemd" = "xyes"])

  AC_MSG_RESULT([$have_systemd])
])

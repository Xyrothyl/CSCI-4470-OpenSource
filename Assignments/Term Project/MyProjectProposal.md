Linux Kernel
===========
[git repo](https://git.kernel.org/)

[torvalds git hub](https://github.com/torbalds/linux)

Overview
--------
I've decided to work on the linux kernel as my project in order to take advantage of this learning opportunity on some super low level systems at the same time as I'm taking operating systems. Low level programming is one of my biggest interests in computer science and just to start writing a patch requires one to dig around in the kernel and figure out how things work.

As a titan of open source itself, Linux will continue to grow and develop regardless of any contribution I may make. However, beyond academic reasons, my intentions with taking on this project are primarily to learn more about the kernel and how it works by playing around with it.

Semester Plan
-------------
It seems difficult to have a patch accepted in the timeframe we have so my plan should at least try to incorporate tasks throughout the canonical workflow. Aside from the coding itself, I mean to set up and tune the development environment for the kernel, as the toolchain is important in maintaining the codebase at scale.

A (seemingly) endlessly available task that will be involved is research, especially introductory information. Fortunately, there are a variety of such sources available online; this [tutorial](https://kernelnewbies.org/FirstKernelPatch) offers much guidance in the initial setup. The other area for me to explore is the community itself with a goal of productively engaging with its members.

Technology
----------

Kernel Compilation
| Program | Minimal version | Purpose |
|:------:|:-------:|:------:|
| GNU C | 5.1 | compiler |
| Make | 3.81 | build |
| Bash | 4.2 | scripts |
| Binutils | 2.23 | build  |
| pkg-config | 4.18 | used for configuration |
| Flex | 2.5.35 | lexical analysis | 
| Bison | 2.0 | parsers for build |
| Perl | 5 | build  |
| OpenSSL | - | keys |

System Utilities
| Program | Minimal version | Purpose |
|:------:|:-------:|:------:|
| Mkinitrd | - | for `/lib/modules` file tree |
| JFSutils | 1.1.3 | file system utilites |
| Xfsprogs | 2.6.0 | XFS utilites |

Kernel Documentation
| Program | Minimal version | Purpose |
|:------:|:-------:|:------:|
| Sphinx | 1.7 | documentation |

Team
----
| **Name** | **GitHub Handle** | **Email** |
|:------:|:-------:|:------:|
| Chris Carbone | xyrothyl | carboc2@rpi.edu | 

Milestones
----------
Milestones are given as weeks from project start:

- By Week 1 : Have dev environment and kernel build set up; read the community and contribution guidelines
- By Week 2 : Know what issue to focus on
- By Week 4 : Have majority of functional work done
- By Week 6 : Be in discourse with manager(s) regarding patch

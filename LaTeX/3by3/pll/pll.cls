\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{algs}[2025/06/14 Custom Rubik Cube Class]
\LoadClass{article}
\RequirePackage{tikz}
\RequirePackage{rubikcube,rubikrotation,rubikpatterns}
\newcommand{\AaPerm}{[Aa], x, Rp, U, Rp, D2, R, Up, Rp, D2, R2, xp}
\newcommand{\AbPerm}{[Ab], x, R2, D2, R, U, Rp, D2, R, Up, R, xp}
\newcommand{\EPerm}{[E],y,xp,R,Up,Rp,D,R,U,Rp,Dp,R,U,Rp,D,R,Up,Rp,Dp,x}
\newcommand{\FPerm}{[F],y,Rp,Up,Fp,R,U,Rp,Up,Rp,F,R2,Up,Rp,Up,R,U,Rp,U,R}
\newcommand{\GaPerm}{[Ga],R2,U,Rp,U,Rp,Up,R,Up,R2,D,Up,Rp,U,R,Dp}
\newcommand{\GbPerm}{[Gb],Rp,Up,R,U,Dp,R2,U,Rp,U,R,Up,R,Up,R2,D}
\newcommand{\GcPerm}{[Gc],R2,Up,R,Up,R,U,Rp,U,R2,Dp,U,R,Up,Rp,D}
\newcommand{\GdPerm}{[Gd],R,U,Rp,Up,D,R2,Up,R,Up,Rp,U,Rp,U,R2,Dp}
\newcommand{\HPerm}{[H],M2,Up,M2,U2,M2,Up,M2}
\newcommand{\JaPerm}{[Ja],y2,x,R2,F,R,Fp,R,U2,Rwp,U,Rw,U2,xp}
\newcommand{\JbPerm}{[Jb],R,U,Rp,Fp,R,U,Rp,Up,Rp,F,R2,Up,Rp}
\newcommand{\NaPerm}{[Na],Fp,R,U,Rp,Up,Rp,F,R2,F,Up,Rp,Up,R,U,Fp,Rp,}
\newcommand{\NbPerm}{[Nb],Rwp,Dp,F,Rw,Up,Rwp,Fp,D,Rw2,U,Rwp,Up,Rwp,F,Rw,Fp}
\newcommand{\RaPerm}{[Ra],L,U2,Lp,U2,L,Fp,Lp,Up,L,U,L,F,L2}
\newcommand{\RbPerm}{[Rb],Rp,U2,R,U2,Rp,F,R,U,Rp,Up,Rp,Fp,R2}
\newcommand{\TPerm}{[T],R,U,Rp,Up,Rp,F,R2,Up,Rp,Up,R,U,Rp,Fp}
\newcommand{\UaPerm}{[Ua],y2,M2,U,M,U2,Mp,U,M2}
\newcommand{\UbPerm}{[Ub],y2,M2,Up,M,U2,Mp,Up,M2}
\newcommand{\VPerm}{[V],Rp,U,Rp,Up,y,Rp,Fp,R2,Up,Rp,U,Rp,F,R,F}
\newcommand{\YPerm}{[Y],F,R,Up,Rp,Up,R,U,Rp,Fp,R,U,Rp,Up,Rp,F,R,Fp}
\newcommand{\ZPerm}{[Z],Mp,Up,M2,Up,M2,Up,Mp,U2,M2}

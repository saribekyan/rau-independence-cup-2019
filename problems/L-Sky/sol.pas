var ind,xi,yi,x,y:array[1..4] of longint;
    k:array[1..4] of real;
    i,j,m:longint;
    npe,eq,perp:longint;
begin
   for i:= 1 to 4 do
       read(xi[i],yi[i]);
   m:=1;
   for i:= 2 to 4 do begin
       if (yi[i]<yi[m]) or((yi[i]=yi[m])and(xi[i]<xi[m])) then m:=i;
   end;
   for i:= 1 to 4 do begin
       ind[i]:=i;
       if i=m then k[i]:=1000 else begin
          k[i]:=(xi[i]-xi[m])/sqrt(sqr(xi[i]-xi[m])+sqr(yi[i]-yi[m]));
       end;
   end;
   for i:= 1 to 4 do
       for j:= 1 to 3 do begin
           if k[ind[j]]<k[ind[j+1]] then begin
              eq:=ind[j];
              ind[j]:=ind[j+1];
              ind[j+1]:=eq;
           end;
       end;
   for i:= 1 to 4 do begin
       x[i]:=xi[ind[i]];
       y[i]:=yi[ind[i]];
   end;
   {}
   npe:=0;
   if (x[1]-x[2])*(y[3]-y[4])-(y[1]-y[2])*(x[3]-x[4])=0 then inc(npe);
   if (x[2]-x[3])*(y[4]-y[1])-(y[2]-y[3])*(x[4]-x[1])=0 then inc(npe);
   if npe=0 then begin
      writeln('Quadrangle');
   end else if npe=1 then begin
      writeln('Trapezium');
   end else begin
       eq:=1;
       if (sqr(x[1]-x[2])+sqr(y[1]-y[2]))<>(sqr(x[2]-x[3])+sqr(y[2]-y[3])) then eq:=0;
       perp:=0;
       if (x[1]-x[2])*(x[3]-x[2])+(y[1]-y[2])*(y[3]-y[2]) =0 then perp:=1;
       if (eq=1)and(perp=1) then writeln('Square');
       if (eq=1)and(perp=0) then writeln('Rhomb');
       if (eq=0)and(perp=1) then writeln('Rectangle');
       if (eq=0)and(perp=0) then writeln('Parallelogram');
   end;
end.
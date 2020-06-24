clc;
clear all;
close all;
load handel.mat
filename='taki.wav';
clear y;
[y,Fs] = audioread('taki.wav');
dt=1/Fs;    
t = 0:dt:(length(y)*dt)-dt; 
n=2205;  
y_index=1;
h=zeros([round(length(y)/n) 12]);
Y=y(:,1);
file=fopen('taki.txt','wt');
for r = 1:941     %time = 2205 units total widths = (2077883)//2205 = 942. For clear image,run till 941.                                                      
       X=fftshift(fft(Y(r*n:(r+1)*n),n));
       X=abs(X);
       l=length(X);
       X=X(1:(round(l/2)+1));
       x_index=1;
       for c = [1 100 250 300 330 350 450 500 650 775 950 1000]   
           if c==1
               d=1;
           end
           h(y_index,x_index)= max(X(d:c));
           x_index=x_index+1;
       end
       y_index=y_index+1;
       
       cc=zeros([12 12]);  %cc is a 2-D matrix which divides amplitude into 1's and 0's so as to show the same output in the sculpture.
       for i = 1:12
           if (h(r,i)>=0.1)  
               cc(12,i)=1; 
           else
               cc(12,i)=0;
           end
           if (h(r,i)>=0.3)   
               cc(11,i)=1; 
           else
               cc(11,i)=0;
           end           
           if (h(r,i)>=0.5)  
               cc(10,i)=1; 
           else
               cc(10,i)=0;
           end
           if (h(r,i)>=1.25) 
               cc(9,i)=1; 
           else
               cc(9,i)=0;
           end
           if (h(r,i)>=1.75) 
               cc(8,i)=1; 
           else
               cc(8,i)=0;
           end
           if (h(r,i)>=2) 
               cc(7,i)=1; 
           else
               cc(7,i)=0;
           end  
           if (h(r,i)>=3.5) 
               cc(6,i)=1; 
           else
               cc(6,i)=0;
           end      
           if (h(r,i)>=4.6) 
               cc(5,i)=1;
           else
               cc(5,i)=0;
           end
           if (h(r,i)>=6)  
               cc(4,i)=1;
           else
               cc(4,i)=0;
           end
           if (h(r,i)>=8)  
               cc(3,i)=1; 
           else
               cc(3,i)=0;
           end
           if (h(r,i)>=20)  
               cc(2,i)=1; 
           else
               cc(2,i)=0;
           end
           if (h(r,i)>=30 && h(r,i)<=800)  %This is an approximate maximum to prevent additional errors.
               cc(1,i)=1;
           else
               cc(1,i)=0;
           end
       end  
       
       m=zeros([12 12]);   % m is another 2-D matrix which changes positions of columns in cc matrix to make the fft look better. 
       nn=zeros([12 12 8]);
       
           m(:,1)=cc(:,1);
           m(:,2)=cc(:,3);
           m(:,3)=cc(:,5);
           m(:,4)=cc(:,7);
           m(:,5)=cc(:,9);
           m(:,6)=cc(:,11);
           m(:,7)=cc(:,12);
           m(:,8)=cc(:,10);
           m(:,9)=cc(:,8);
           m(:,10)=cc(:,6);
           m(:,11)=cc(:,4);
           m(:,12)=cc(:,2); 
       
       nn(:,:,:)=cat(3,m,m,m,m,m,m,m,m);  %nn is a 3-D matrix which extents the fft to all the 8 layers.
       abcd=zeros([12 12]);
       tempo=0;
        for j=1:4                                                   % 4 times to make sure a stable picture of each pattern is shown.
            for col=1:12
                for row=1:12
                    for lay=1:8 
                        tempo=(nn(row,col,lay)*(2^(lay-1)))+tempo;
                    end
                    abcd(row,col)=tempo;
                    tempo=0;
                end
            end
            for v=1:8
                 fprintf(file,'%03X%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X\n',2^(v+3),abcd(v,:));
            end
            for w=9:12
                 fprintf(file,'%03X%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X\n',2^(w-9),abcd(w,:));
            end
       end  
end
 fclose(file);
     
for o = 1:size(h,1)      % This 'for loop' is to check the output in a bar graph and written for verification purpose.
        bar(h(o,:));
        ylim([0,15]);
        xlim([0,13]);
        pause(0.1); 
end

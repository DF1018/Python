這是我人生第一次寫的C語言
是在
```
#include <stdio.h>
#include <stdlib.h>
#include<string.h>
#include<ctype.h>
char eng[5000],fir[2000];
char filename[30],outfile[30];
static int letter[26],letterCount[500];
static int k,length,option1,option2;
int all=0;
int f,poss;
char sec[5000];


void Encrynum();
void printstar();
void count();
void Decrypt();
void DecryptALL();


int main()
{
 
   FILE*JJ;


   do{
   printf("Please Input File name : ");
   gets(filename);
   printstar();


     if((JJ=fopen (filename,"r"))==NULL){
       printf("This file can't open!\n");
       printstar();


   }else
   {
     printf("IF you want to Encrypt File ? Please enter 1\nIF you want to Decrypt File ? Please enter 2\nYour option? : ");
    scanf("%d",&option1);
       break;
   };
   }while(1);


   while(fgets(fir,2000,JJ)!=NULL)
       strcat(eng,fir);
       printf("");
       printstar();
    printf("length= ");
    size_t length = strlen(eng);
    printf("%d\n",length);


    printstar();


  switch(option1)
  {
   case 1:


   if(length<200)
   {
       printf("This file word count less than 200 word , can't Encryption!!!!");
       exit(1);
   };
       printf("FILE: %s",eng);
       printf("\n");


       printstar();
       printf("Encryption Key: ");
       scanf("%d",&k);


       Encrynum(k);


       printstar();


       printf("\nEncryption: ");


   for(int g=0;g<length;g++)
   {
      printf("%c",eng[g]);
   };


   printf("\n");
   printstar();
   count();
   printstar();


   fclose(JJ);
   break;


   case 2:
   printf("FILE: %s",eng);
   printf("\n");
   printstar();
   printf("\n");


   printf("Please input the K , If you don't know about the K , Please enter 0 : ");
   scanf("%d",&all);


   if(all!=0)
   {
   printf("\n");
   printstar();
   printf("\n");


   Decrypt(all);


   for(int g=0;g<length;g++)
   {
      printf("%c",eng[g]);
   };


   printf("\n");
   printstar();
   printf("\n");
   }
  
   else
   {
     printf("\n");
     printstar();
     printf("\n");


     for(f=1;f<27;f++){


     DecryptALL();


     printf("The Decrypt Possibility %d\n\n",f);


      for(int g=0;g<length;g++)
        {
          printf("%c",sec[g]);
        };
     printf("\n");
     printstar();
     printf("\n");
     };


    printf("which Possibility you want to input : ");
    scanf("%d",&poss);
    Decrypt(poss);


    printf("\n");
    printstar();
    printf("\n");


    
   };


   break;
 };


do{
 printf("Do you want to output this to file ?\n[Yes] enter 1\n[No] enter 2\nYour option? : ");
 scanf("%d",&option2);
 FILE*OUT;


 switch(option2)
 {
 case 1:


   do{
   printf("\nwhich file you want to OUT_put : ");
   scanf("%s",outfile);


   printf("\n");


   OUT=fopen(outfile,"w");
   fputs(eng,OUT);


   if((OUT=fopen (outfile,"r"))==NULL){
       printstar();
       printf("This file can't INPUT!");
       exit(1);
   }else
   {
       printstar();
       printf("\nINPUT Successful!!!\n");
       printstar();
       exit(1);
   }


   }while(1);
   break;
   fclose(OUT);
    case 2:
   exit(1);
   break;
  
    default:
   printf("Please choose your option !\n");
   break;
 }
 }while(1);


printf("\n");
system("PAUSE");
return 0;
}


void Encrynum(int w)
{
    for(int g=0;g<5000;g++)
   {
     eng[g]=toupper(eng[g]);


      if(eng[g]<91 && eng[g]>64)
          {
            eng[g]=eng[g]+w;
          };


          if(eng[g]>90)
          {
            eng[g]=eng[g]-26;
          };
   };
}


void printstar()
{
   int i;
   printf("\n");
   for(i=1;i<=50;i++)
   {
       printf("*");
   }
   printf("\n");
   printf("\n");
}


void count()
{
 for (int x = 0; x < 26; x++)
  {
   int c = 0;
   letter[x] = x + 65;
   for (int i = 0; i < 5000; i++)
   {
     if (letter[x] == eng[i])
     {
       ++c;
       letterCount[x] = c;
     }
   }
   if (letterCount[x]>=1)
     {
       printf("%c %d\n", letter[x], letterCount[x]);
     }  


   }
}


void Decrypt(int q)
{
     for(int e=0;e<5000;e++)
   {
     eng[e]=toupper(eng[e]);
      if(eng[e]<91 && eng[e]>64)
          {
            eng[e]=eng[e]-q;
            if(eng[e]<65)
          {
            eng[e]=eng[e]+26;
          };
          };
         
   };
}
 void DecryptALL()
 {
   for(int e=0;e<5000;e++)
   {
     eng[e]=toupper(eng[e]);
     sec[e]=eng[e];


      if(eng[e]<91 && eng[e]>64)
          {
            sec[e]=eng[e]-f;
            if(sec[e]<65)
          {
            sec[e]=sec[e]+26;
          };
          };
         
   };
     
  }
```








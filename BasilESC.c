/*
-Created as a personal project by smithdepazd@wit.edu
-Last updated on 4/19/2018
-Designed to be run on the Online GBD Compiler
-While does work on other C compilers it's not optimized for them
-Written in C code
-If you find yourself reading this please give me any feedback on anything you have on it
*/


//KNOWN BUGS
/*
FIXED!!
PHANTOM PORTAL
If the player collects a portal and dies on the same level.
The portal appears to still be in the level upon re-loading.
If the player attempts to collects the portal again, nothing will happen.

Figure out how to stop the portal from being re-loaded
*/ 

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <conio.h>
#define OFF 0
#define ON 1


//delay function/////////
void delay(int wait){//input time in millisecons
clock_t start, diff;
start = clock();
int msec;
for(;;){
    diff = clock()-start;
    msec = diff*1000/ CLOCKS_PER_SEC;
    if(wait<msec){
        break;
    }
}
}
////////////////////////
//defines data types of elements/////
typedef enum element 
    {
    EMPTY,//space with nothing in it
    WALL,//standard wall
    PC,//player space
    GOAL,//exit space
    ENEMY,//standard enemy space
    WARP,//portal space
    BENEMY//boss enemy space
    }ELEMENT;
/////////////////////////////////////    
//all items have to be placed somewhere//
typedef struct item
    {
    int x;
    int y;
    } ITEM;
////////////////////////////////////////    
//random number generator function//
int randy(double size){
    double temp;
    int out;
    temp = (rand());
    out = temp/RAND_MAX*size;
    return out;
 }
///////////////////////////////////
//main//
int main(void){
//Prompts and saves player's character//
printf("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n        You wake to find yourself trapped in a dark enviornment.\n        There appears to be a Basilisk that thinks you're pretty tasty.\n        You don't speak Basilisk, so you can't inform it of how not-tasty you are.\n");
printf("        Run, dodge, and smash your way to each EXIT in an effort to evade the Basilisk's advances.\n");
printf("        Can you can you survive this language-barrier-induced odyssey?\n        PRESS ANY KEY TO CONTINUE\n        ^\n        |\n        |\n        |\n        |\n        ^\n        |\n        |\n        |\n        |\n        ^Please adjust the console to fit the text above^\n");
getch();
printf("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n        CHOOSE YOUR CHARACTER\n\n\n");
char pcpeice;
pcpeice = getch();
printf("        YOU SELECTED '%c'\n\n",pcpeice);
delay(500);
//////////////////////////////////////
BEGINING://goto here if the player wants to play again //REWRITE WITHOUT GOTO STATEMENT
srand(time(NULL));//seeds the random function based on time

/////print the initial instructions to the console for the player to not read/////

printf("        PRESS ANY KEY FOR THE NEXT LINE OF INFO\n\n");   
getch();
printf("        INSTRUCTIONS:\n\n");   

printf("         Use WASD to input directions\n\n");
getch();
printf("         Please only tap the keys you wish to input\n         Holding down any keys will result in the game not behaving properly\n\n");
getch();
printf("         You play as the character you entered\n\n");
getch();
printf("         Your goal is to reach the '><' before the '#' kills you\n\n");
getch();
printf("         Use '@' in special situations\n\n");
getch();
printf("         Walls are destructable \n\n\n");
getch();
printf("        PRESS ANY KEY TO BEGIN\n");
getch();
printf("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n");



//initialize inportant variables
int levelnum = 1;//starting value should be 1
int portnum= 0;//starting value should be 0
int numlives= 3;// starting val should be 3
int nummoves=0;// starting val should be 0
double grade= 0;
double avgmoves;
int bossbrain=OFF;
//Main game code////////////////////////
for(;;){  
    //activate enemy AI    
    int brain=ON;
    //set map size
    int mapx = 32;//this number should be 32
    int mapy = 16;//this number should be 16
    //crate a matrix(map) sightly bigger than what the player can see so there are no(fewer) segmentation faults
    ELEMENT map[mapy+2][mapx+2];
    ELEMENT bacmap[mapy+2][mapx+2];
    //initialize all of the game peices
    ITEM player,playold,xit,bogey,prevplayer,prevbogey,portal;
    ITEM boss,prevboss;
    //player starts at a random point on the map//
    player.x = 1+randy(mapx-2);//+1 because the x and y values at 0 are supposed to be walls
    player.y = 1+randy(mapy-2);//-2 because the visible mape goes to mapx-1 and there's supossed to be walls there
    playold.x = player.x;//initalize playold so no funny bussiness happens
    playold.y = player.y;//initalize playold so no funny bussiness happens
    prevplayer.x = player.x;//store's the player's initial x position
    prevplayer.y = player.y;//store's the player's initial y position
    /////////////////////////////////////////////
    //exit is placed at a random point in the map
    xit.x = 1+randy(mapx-2);//same deal    
    xit.y = 1+randy(mapy-2);//same deal
    /////////////////////////////////////////////
    //Enemy is placed at a random point on the map
    bogey.x = 1+randy(mapx-2); //same deal
    bogey.y = 1+randy(mapy-2); //same deal
    prevbogey.x = bogey.x;//store's the bogey's initial x position
    prevbogey.y = bogey.y;//store's the bogey's initial y position
    //////////////////////////////////////////////
    //boss is put into cold storage//
    //since this peice has to exist somewhere the player can't get to it is placed out of reach
    boss.x = mapx+1;
    boss.y = mapy+1;
    if(levelnum>10){
        boss.x = 1+randy(mapx-2);
        boss.y = 1+randy(mapy-2);
    }
    prevboss.x = boss.x;
    prevboss.y = boss.y;
    //Portal is placed at edge of map and out of view to start;
    portal.x = mapx+1;
    portal.y = mapy+1;
    ///////////////////////////////////////////////////////////
    //checks for a random empty spot to place the portal
    int rx;
    int ry;
    rx = randy(mapx-2);
    ry = randy(mapy-2);
    if((map[ry][rx] == EMPTY)&&(levelnum>3)){
        portal.x = rx;
        portal.y = ry;
    }
    ///////////////////////////////////////////////////
    //nested loops draw the initial map/////////////////////////////////////////////
    int i,j,k,l;
        for(i=0;i<mapy;i++){
            for(j=0;j<mapx;j++){
                //assign every spot with empty
                map[i][j] = EMPTY;
                //assign all of the borders as walls
                if((0 == i)||(0==j)||((mapy-1)==i)||((mapx-1)==j)) {
                    map[i][j] = WALL;
                    map[mapy][j] = EMPTY;
                    map[i][mapx] = EMPTY;
                }
                //////////code for random maps////////////////////////////////////
                k = randy(mapx);
                l = randy(mapy);
                
                if(((levelnum!=10)&&(levelnum!=2))&&(map[l][k] == EMPTY)&&((i*j%(40/(levelnum)))==0)) {//edit this line to change map generation
                    map[i][j] = WALL;
                    
                } 
                //level 2//
                if((levelnum==2)&&((j==mapx/2)||(i==mapy/2))){
                    map[i][j] = WALL;
                    player.y = mapy/4;
                    player.x = mapx/4;
                    prevplayer.x = player.x;
                    prevplayer.y = player.y;
                    
                    xit.y = (mapy/4)*3;
                    xit.x = (mapx/4)*3;
                    bogey.y = (mapy/4);
                    bogey.x = (mapx/4)*3;
                    prevbogey.x = bogey.x;
                    prevbogey.y = bogey.y;
                }
                //boss level code//
                if((levelnum%10==0)&&((i*j%8)==0)){
                    map[i][j] = WALL;
                    player.y = mapy/2;
                    player.x = mapx/2;
                    prevplayer.x = player.x;
                    prevplayer.y = player.y;
                    
                    bogey.y = mapy-2;
                    bogey.x = mapx-2;
                    prevbogey.x = bogey.x;
                    prevbogey.y = bogey.y;
                    
                    boss.y = 1;
                    boss.x = 1;
                    prevboss.x = boss.x;
                    prevboss.y = boss.y;
                    
                    portal.x = mapx;
                    portal.y = mapy;
                    bossbrain = ON;
                }
                
                
                //plot all objects//////////////
                map[portal.y][portal.x] = WARP;
                map[xit.y][xit.x] = GOAL;
                map[bogey.y][bogey.x] = ENEMY;
                map[boss.y][boss.x] = BENEMY;
                map[player.y][player.x] = PC;
                ///////////////////////////////
                //create a backup map
                bacmap[i][j] = map[i][j];
                //print the map/////////
                switch(map[i][j]){
                case EMPTY:printf("  ");
                break;
                case WALL:printf("||");
                break;
                case PC:printf(" %c",pcpeice);
                break;
                case GOAL:printf("><");
                break;
                case ENEMY:printf(" #");
                break;
                case BENEMY:printf(" #");
                break;
                case WARP:printf(" @");
                break;
                default:;
                }
        }
        printf("\n");
    }
    
    
    //////////////////////////////////////////////////////////////////
    ///CURRENT LEVEL ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

char con,pcon;
int xdis,ydis;
for(;;){
    //keeps track of player's previous position//
    playold.x = player.x;
    playold.y = player.y;
    /////////////////////////////////////////////
    
    //grabs WASD inputs////////////////////////////////
    
    con = getch();
    nummoves++;
    
    switch(con){
        case 'w':
        case 'W': player.y += -1;
        break;
        case 'd':
        case 'D':player.x += 1;
        break;
        case 'a':
        case 'A':player.x += -1;
        break;
        case 's':
        case 'S':player.y += 1;
        break;
        default:;
    }
     //////////////////////////////////////////////////
     //stops the player from going out of bounds//
     if(player.y>mapy){
         player.y = mapy;
     }
     if(player.x>mapx){
         player.x = mapx;
     }
     if(player.y<0){
         player.y = 0;
     }
     if(player.x<0){
         player.x = 0;
     }
    ////////////////////////////////////////////
    //stops player from going through the WALLs//
    if(map[player.y][player.x] == WALL ){
        player.x = playold.x;
        player.y = playold.y;
    }
    /////////////////////////////////////////////
    //checks if player has run over a portal//   
    if((player.y == portal.y)&&(player.x == portal.x) ){
        portnum++;
        portal.x = mapx+1;
        portal.y = mapy+1;
    }
    //////////////////////////////////////////  
    
    printf("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n");
    
    // displays number of portals left//
    if(portnum>0){
        if('@'==con){
                 player.x = 1+randy(mapx-2);
                 player.y = 1+randy(mapy-2);
                 portnum --;
        }
        printf("Number of Portals:%d\n",portnum); 
    }
    ///////////////////////////////////
    //WALL REMOVAL mechanics!/////////////////////////////////
    if((player.x == playold.x)&&(player.y==playold.y)){
        switch(con){
            case 'w':playold.x = player.x+1;
                     playold.y = player.y-1;
                   break; 
            case 'a':playold.x = player.x-1;
                   playold.y = player.y-1;
                   break;
            case 's':playold.x = player.x-1;
                     playold.y = player.y+1;
                   break; 
            case 'd':playold.x = player.x+1;
                   playold.y = player.y+1;
                   break;
            default:;
        }     
           
    }
    //////////////////////////////////////////////////////////
    //Code to turn the bogey off for testing//
    if(con == '#'){
        brain = OFF;
    }
    //////////////////////////////////////////
    //AI for Bogey//////////////////
    if(ON == brain){
        if(player.x > bogey.x){
            bogey.x+= 1 + randy(-2);
        }
        if(player.y > bogey.y){
            bogey.y+= 1 + randy(-2);
        }
        if(player.x < bogey.x){
            bogey.x+= -1 + randy(2);
        }
        if(player.y < bogey.y){
            bogey.y+= -1+ randy(2);
        }
    }   
    ////////////////////////////////
    //AI for boss/////////
    if(ON == bossbrain){
       xdis = player.x - boss.x;
       ydis = player.y - boss.y;
       
       if(player.x > boss.x){
            boss.x+=  randy(2) + randy(-1);
        }
        if(player.y > boss.y){
            boss.y+= randy(2) + randy(-1);
        }
        if(player.x < boss.x){
            boss.x+= randy(-2) + randy(1);
        }
        if(player.y < bogey.y){
            boss.y+= randy(-2)+ randy(1);
        }
        if(player.x == boss.x){
            boss.y+= randy(2) + randy(-1);
        }
        if(player.y == boss.y){
            boss.x+= randy(2) + randy(-1);
        }
        
    } 
    
    //checks if Bogey has run over a portal///////////   
    if((bogey.y == portal.y)&&(bogey.x == portal.x) ){
        map[portal.y][portal.x]=EMPTY;
        portal.x = mapx;
        portal.y = mapy;
        bogey.x = 1+randy(mapx-2);    
        bogey.y = 1+randy(mapy-2);
        map[bogey.y][bogey.x] = ENEMY;
    }    
    /////////////////////////////////////////////////
    ///WIN SCREEN/////
    if(map[player.y][player.x] == GOAL ){
        printf("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n");
        printf("         You reached the exit!!\n\n\n\n\n\n\n\n\n");
        
        
        if(levelnum == 15){
            printf("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n");
            printf("         GAME COMPLETE!!\n\n\n\n\n\n\n\n\n");
            delay(800);
            printf("         STATS:\n\n         total moves: %d\n",nummoves);
             avgmoves = nummoves/levelnum;
            printf("         Average moves per level: %f\n",avgmoves);
            printf("         Grade:");
            grade = avgmoves-numlives;
            if(grade<=20){
                printf("A#\n         You turned off the Snake didn't you?\n");
            }
            if((grade>20)&&(grade<=26)){
                printf("A++\n");
            }
            if((grade>26)&&(grade<=33)){
                printf("A\n");
            }
            if((grade>33)&&(grade<=40)){
                printf("B#\n");
            }
            if((grade>40)&&(grade<=46)){
                printf("B++\n");
            }
            if((grade>40)&&(grade<=46)){
                printf("B\n");
            }
            if((grade>46)&&(grade<=53)){
                printf("C#\n");
            }
            if((grade>53)&&(grade<=60)){
                printf("C++\n");
            }
            if((grade>60)&&(grade<=70)){
                printf("C\n");
            }
            if((grade>70)&&(grade<=75)){
                printf("D\n");
            }
            if(grade>75){
                printf("F\n         An F? Yikes...");
            }
            //avgmoves
            //nummoves
            //numlives
            //levelnum
            
            return 0;
        }
        levelnum++;
        delay(600);
        
        printf("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n         level: %d\n\n\n\n\n\n\n\n\n",levelnum);
        delay(600);
        printf("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n         %c = %d\n\n\n\n\n\n\n\n\n",pcpeice,numlives);
        delay(600);
        //make sure the display is clean
        printf("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n");
        //takes the code out of the current level code
        break;
    }
    /////////////////////////END win//
    // code for the player to die screen/////////////////////
    if((map[player.y][player.x] == ENEMY)||(map[player.y][player.x] == BENEMY)||((player.x==bogey.x)&&(player.y==bogey.y))||((player.x==boss.x)&&(player.y==boss.y)) ){
        printf("\n\n\n\n\n\n\n\n\n\n\n\n\n");
        //print map//
        for(i=0;i<mapy;i++){
        for(j=0;j<mapx;j++){
            map[playold.y][playold.x] = EMPTY;
            map[portal.y][portal.x] = WARP;
            map[player.y][player.x] = map[i][j];
            map[boss.y][boss.x] = BENEMY;
            map[bogey.y][bogey.x] = ENEMY;
            map[xit.y][xit.x] = GOAL;
            //print the map/////////////
                switch(map[i][j]){
                case EMPTY:printf("  ");
                break;
                case WALL:printf("||");
                break;
                case PC:printf(" %c",pcpeice);
                break;
                case GOAL:printf("><");
                break;
                case ENEMY:printf(" #");
                break;
                case BENEMY:printf(" #");
                break;
                case WARP:printf(" @");
                break;
                default:;
                }
            ///////////////////////////
        }
        printf("\n");
    }
        
        printf("\n\n\n         YOU DIED\n\n\n");
        delay(600);
        numlives--;
        //if the player has more than 0 lives REPLAY the level   
        if(0 < numlives){
                
            printf("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n         level: %d\n\n\n\n\n\n\n\n\n",levelnum);
            delay(600);
            printf("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n         %c = %d\n\n\n\n\n\n\n\n\n",pcpeice,numlives);
            delay(600);
            //make sure the display is clean
            printf("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n");
            //redraws the map based on the backup map/////// 
            for(i=0;i<mapy;i++){
                for(j=0;j<mapx;j++){
                    map[i][j] = bacmap[i][j];   
                    map[player.y][player.x]=EMPTY;
                    map[bogey.y][bogey.x]=EMPTY;
                    map[boss.y][boss.x]=EMPTY;
                    if (map[i][j] == WARP) map[i][j] = EMPTY;
                    
                }
                
            }
            ////////////////////////////////////////////
            //sets items to their initial locations
            player.x = prevplayer.x;
            player.y = prevplayer.y;
            bogey.x = prevbogey.x;
            bogey.y = prevbogey.y;
            boss.x = prevboss.x;
            boss.y = prevboss.y;
            ///////////////////////////////////////////
        }
        ////////////////////////////////////////////////////////
        //code for the player to lose//
        if(0 >= numlives){
            
            printf("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n         GAME OVER\n\n\n\n\n\n\n");
            delay(1000);
            printf("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n         STATS:\n\n         total moves: %d\n\n",nummoves);
            delay(800);
            printf("\n\n         level: %d\n\n         Hit 'E' to play again\n         Hit 'Q'to quit\n\n\n\n",levelnum);
            for(;;){
                con = getch();
                switch(con){
                    case 'E':
                    case 'e':
                    goto BEGINING;//edit out
                    break;  
                    case 'Q':
                    case 'q':return 0;
                    default:printf("\n\n\n\n         Hit 'E' to play again\n         Hit 'Q'to quit\n");
                }
            }
        }
        /////////////////////////////
    } 
    /////////////////DEATH STUFF///////////////////////////////////////
    
    
    
    //Map updates/////////////////////
    map[playold.y][playold.x] = EMPTY;
    map[portal.y][portal.x] = WARP;
    map[player.y][player.x] = PC;
    map[boss.y][boss.x] = BENEMY;
    map[bogey.y][bogey.x] = ENEMY;
    map[xit.y][xit.x] = GOAL;
    //REDRAW MAP/////////////////////////////////////////
    for(i=0;i<mapy;i++){
        for(j=0;j<mapx;j++){
            //print the map/////////////
                switch(map[i][j]){
                case EMPTY:printf("  ");
                break;
                case WALL:printf("||");
                break;
                case PC:printf(" %c",pcpeice);
                break;
                case GOAL:printf("><");
                break;
                case ENEMY:printf(" #");
                break;
                case BENEMY:printf(" #");
                break;
                case WARP:printf(" @");
                break;
                default:;
                }
            ///////////////////////////
        }
        printf("\n");
    }
    /////////////////////////////////////////////////////
}//////////////////End of current level loop/////////////////
}/////////////////End of main game code/////////////////////
  
}//End of main()














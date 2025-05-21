#include<stdio.h>
#include<conio.h>
#define max 30

int main()
{
    int i,j,n,temp,p[max], bt[max], wt[max], tat[max];
    float awt = 0, atat = 0;
    printf("Enter the No. of Process: ");
    scanf("%d", &n);
    printf("Enter the Process Number: ");
    for(i=0;i<n;i++)
    {
        scanf("%d", &p[i]);
    }
    printf("Enter the Burst time of the process: ");
    for(i=0;i<n;i++)
    {
        scanf("%d", &bt[i]);
    }

    for(i=0;i<n;i++)
    {
        for(j=0;j<n-i-1;j++)
        {
            if(bt[i] > bt[j+1])
            {
                temp = bt[j];
                bt[j] = bt[j+1];
                bt[j+1]= temp;

                temp = p[j];
                p[j] = p[j+1];
                p[j+1]= temp;
            }
        }
    }

    printf("process \t burst time \t waiting time \t turn arount time\n");
    for(i=0;i<n;i++)
    {
        wt[i] = 0;
        tat[i] = 0;
        for(j=0;j<i;j++)
        {
            wt[i] = wt[i] + bt[j];
        }
        tat[i] = wt[i]+bt[i];
        awt = awt + wt[i];
        atat = atat+tat[i];
        printf("%d\t\t %d\t\t %d\t\t %d\t\t\n", p[i],bt[i],wt[i],tat[i]);
    }

    awt=awt/n;
    atat = atat/n;
    printf("Average wating time = %f\n", awt);
    printf("Average tuen around time = %f\n", atat);
    return 0;
}

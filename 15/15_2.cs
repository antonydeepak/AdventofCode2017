using System;
using System.Threading.Tasks;

// Python is very slow for iterations of large numbers
namespace Program
{
   class Program
   {
       static void Main(string[] args)
       {
            long cap = 2147483647;
            long max = 5000000;
            long bits = 65535;

            Task<long> judge = Judge(cap, max, bits);
            Console.WriteLine(judge.Result);
       }

       static Task<long> Judge(long cap, long max, long bits)
       {
            long seedA = 516;
            long seedB = 190;

            long mulA = 16807;
            long mulB = 48271;
            long divA = 4;
            long divB = 8;

            long[] a = new long[max];
            long[] b = new long[max];
            
            int computei = 0;
            int ai = 0;
            int bi = 0;
            long count = 0;
            object mutex =  new object();

            Action<long> onGenA = (long gena) => {a[ai++] = gena; TryCompute(); };
            Action<long> onGenB = (long genb) => {b[bi++] = genb; TryCompute(); };

            Task[] tasks = new Task[2];
            tasks[0] = Task.Run(() => { Gen(seedA, mulA, cap, divA, max, onGenA); });
            tasks[1] = Task.Run(() => { Gen(seedB, mulB, cap, divB, max, onGenB); });

            return Task<long>.Factory.ContinueWhenAll(tasks, ts => {
                Console.WriteLine(ts[0].Exception);
                return count;
            });
            
            void TryCompute()
            {
                lock(mutex)
                {
                    if (ai>computei && bi>computei)
                    {
                        count += Convert.ToInt64((a[computei]&bits) == (b[computei]&bits));
                        computei++;
                    }
                }
            }
       }

       static void Gen(long seed, long multiplier, long cap, long div, long max, Action<long> onGeneration)
       {
            long cur = seed;

            for(int _=0; _<max; _++)
            {
                do
                {
                    cur = Compute(cur, multiplier, cap);
                } while((cur%div) != 0);

                onGeneration(cur);
            }
       }

       static long Compute(long value, long multiplier, long cap)
       {
            return (value * multiplier) % cap;
       }
   } 
}
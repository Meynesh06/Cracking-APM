# HR Questions(Common for all roles)

1. Give a short intro about yourself?
2. Why MBA after XX years of work ex in IT?
3. Why do you want to get into a Systems career after MBA?(IDC, Marketing, Business Development etc)?
4. Why do you want to join the firm? What are your expectations from the internship?
5. What do you know about the role?
6. Why are you interested in this role and why do you think you’ll be a good fit?
7. Questions on previous work experience, work and responsibilities?
8. Describe your daily schedule at IIMA?
9. Tell me about your hobbies?
10. Describe your Strengths, Weaknesses & ambitions?
11. Favorite subject in IIM and why?

# Tech Questions

## Tech Sales and Marketing (Google, SAP, Microsoft)

1. How does Google make money? (Google)

From Adwords and Adsense.

Adwords: Google AdWords is Google's Pay-Per-Click (PPC) program that allows advertisers to create ads and have them displayed on Google SERPs when corresponding keywords are entered by a user. Google AdWords also integrates with Google affiliate websites through its Google AdSense program.

Using the AdWords control panel, advertisers can enter keywords, domain names, topics, and demographic targeting preferences, and Google places the ads on what they see as relevant sites within their content network.

Adsense: AdSense is an ad serving application run by Google Inc. Website owners can enroll in this program to enable text, image, and video advertisements on their websites. These advertisements are administered by Google and generate revenue on either a per-click or per-impression basis

1. Make a sales pitch for Adsense (a Google product)? (Google)

* Find out the goal of your client(like whether to create awareness of their product, increase the sales of their product)
* Find out the target customers of the client
* Devise a strategy accordingly using Adsense

1. Make a sales pitch to ICICI Marketing manager?(Gave me 3 issues which the ICICI manager faced, which as to be resolved)(Google)

Same as question 2

1. Who is the main competitor of Google? (Google)

Facebook- Advertising and social media, Apple- Mobile Market iOS, Microsoft- Search and Mobile OS market, Yahoo- Mail and Search, Amazon, IBM and Twitter – Advertising and Social media

1. How will you design an online marketing campaign for Pepsi? (Google)

Same as question 2

1. Discussion on Google+, why Google+ can’t reach the stage of Facebook ? (Google)

* Switching cost will be greater as people will have to learn using google+ from scratch
* Like is much easy to understand than +1. The idea of +1 as a rating of support has been a point of head scratching and mild snickering.
* Social media is already cluttered with many players like Twitter, Skype, AIM, MSN, forums, a blog, email, the phone which has resulted in user’s fatigue

1. A case on Adwords publicity and launch in SMB hotel industry?(Google)

Same as question 2

1. Guesstimate on number of Gmail users in India?(Google)

* Find out the number of the internet users in India say 120 million
* Then let’s say 10-15% of the users would be less than age of 15 who were interested in mostly playing games in internet, and so most probably would not be requiring Gmail account
* Then there may might be 5-10% of users who started using internet at the early stage of penetration in India and therefore would be having mail accounts in yahoo and hotmail.
* The rest 75-80%i.e. 96-100 million should be having gmail account.

1. Guesstimate where I was asked to calculate the number of bags that arrive at Ahmedabad airport?(Google)

* Let’s say the number of passengers arriving in Ahmedabad airport a day is 100000
* And also assume 10% would be business class travelers who would be most probably having a single bag at most
* The rest 90% economy class travelers would be having at most 2-4 bags. So let’s take the average 3 per person
* So the total comes to 280000

1. What are CPC (Cost per click), CTR (Click through rate), CR (Conversion rate)?(Google)

CPC - advertisers pay the publisher (Google) when the ad is clicked

CTR - The clickthrough rate of an advertisement is defined as the number of clicks on an ad divided by the number of times the ad is shown ([impressions](http://en.wikipedia.org/wiki/Impression_%28online_media%29)), expressed as a percentage. For example, if a [banner ad](http://en.wikipedia.org/wiki/Banner_ad) is delivered 100 times (100 impressions) and receives one click, then the clickthrough rate for the advertisement would be 1%.

CR -  How often a click on the ad resulted in a conversion, a meaningful action like a sale, lead, or sign-up.

1. Technical questions about virtualization, cloud computing, and SAP (SAP)
   * Cloud computing: Cloud computing is the use of computing resources (hardware and software) that are delivered as a service over a network (typically the Internet).

Software as a service (SaaS): In this model, cloud providers install and operate application software in the cloud and cloud users access the software from cloud clients. The cloud users do not manage the cloud infrastructure and platform on which the application is running. This eliminates the need to install and run the application on the cloud user's own computers simplifying maintenance and support.

Platform as a service (PaaS): In the PaaS model, cloud providers deliver a computing platform typically including operating system, programming language execution environment, database, and web server.

Infrastructure as a service (IaaS): In this most basic cloud service model, cloud providers offer computers, as physical or more often as virtual machines, and other resources.

* + Virtualization is a framework or methodology of dividing the resources of a computer into multiple execution environments, by applying one or more concepts or technologies such as hardware and software partitioning, time-sharing, partial or complete machine simulation, emulation, quality of service, and many others.

## Program Manager Role (Microsoft IDC, Yahoo)

1. How would you design a spam filter?(Microsoft)

**Ans** – Things to look for – Logical thinking, knowledge, relevant questions asked. Spam filter - The algorithm to decide where a mail is a spam or not take multiple factors into account like **no. of red flagged “Keywords “(**e.g. – Viagra, Lottery, make money etc.), **Number of emails sent from that particular sender’s email id** to all, **Attached files with in the mails** – Scan the attachments for viruses/Trojan etc. and red flag emails with riskier attachment, **check hyperlinks in the mails** and tally them against list of safe websites, **learning mode (this is user specific) – learn about user’s preference from past activities –** types of mail user opens and given enough number of mails with certain keywords(red flagged) – remove the red flags for this particular user on these keywords and also check whether the person has opened or sent mails from/to the sender previously/person’s mail id is present in this person’s contact list or not.

1. Give an algorithm to find a substring of a string of numbers (numbers can be both +ve or –ve) having highest sum? (Microsoft)

**Ans** – Candidate should be at least able to give basic algorithm i.e. find out all possible substrings, sum them up individually and return the answer. Issue with this solution is that it is an inefficient one with O(**n2**) performance. There is one algorithm that is provides solution with O(n) performance and includes cumulative summation and certain check.

void maxSumSubArray( int \*array, int len, int \*start, int \*end, int \*maxSum )

{

int maxSumSoFar = -2147483648;

int curSum = 0;

int a = b = s = i = 0;

for( i = 0; i < len; i++ ) {

curSum += array[i];

if ( curSum > maxSumSoFar ) {

maxSumSoFar = curSum;

a = s;

b = i;

}

if( curSum < 0 ) {

curSum = 0;

s = i + 1;

}

}

\*start = a;

\*end = b;

\*maxSum = maxSumSoFar;

}

Complexity O(n)

1. Design a restaurant ordering system? (Microsoft)

**Ans** – Again check for knowledge, awareness about existing systems like ebay, zomato etc., logical thinking, relevant questions, and creativeness.

Question asked is to provide a web solution where a user can come in and check food item – menu, prices etc and order food for home delivery/pickup. The website would be used by multiple vendors/restaurants and is not one particular user specific.

Designing such and system has near endless possibilities in terms of features to be provided. Some hints – Register and login feature for users and admin (restaurant owners/manager – to maintain their prices/menu etc.), maybe option for users to order food as guest(without login), features to bring more traffic to this portal – applications for mobile phones, search feature in site – geography/ cuisine/rating based restaurant selection etc. Features for users, like posting review and raising concerns with managers etc. How to handle issues like fake order for home delivery or pickup. Additional features like discount coupon provision, payment option – COD/online payment, features for restaurant administrator in that website like update menu/prices/write details or content of a dish/add picture of that dish, generate reports on multiple dimensions – weekly/monthly/yearly sales, dishes or cuisine with maximum popularity. Maybe provide additional features to maintain payroll for employees and manage restaurant accounts.

1. Design a cookie vending machine for children. How should it look like and what should it do? (Microsoft)

**Ans** – Same as question 3, for particular inputs search online. Like marketing see features that you would incorporate to differentiate your product as well as cater to needs and handle problems of this target segment.

1. Given a word write an algorithm to find all possible sub-words within that which can be found in the Dictionary? (Microsoft)

Method(Back track)

void solve(String s, Set<String> dict, List<String> solution) {

if (s.length == 0)

return

for each prefix of s found in dict

solve(s without prefix, dict, solution + prefix)

}

List<String> solution = new List<String>()

solve(text, dict, solution)

## E-Marketing & E-Retail (Flipkart, Cleartrip, Infibeam)

1. Guesstimate for number of parking required for New Delhi International Airport(Groupon)
   1. Estimate some %age of airport staff (1K) coming by cars (assume its officers)
   2. Estimated arrivals per year (35 million), assuming distribution is not even and peaks to ‘x’ at some time
   3. Estimate 50% arrivals, 50% departures, separate percentage for parking requirements for arrivals/ departures (e.g. 40-50% for arrivals and 10% for departures)
   4. Assuming waiting time is 1 hour, Little’s law (inventory = Rate of arrival \* processing time or waiting time)
2. How can you convince people that shopping online is safe?(Infibeam)
3. Cash on delivery so that users don’t have to use credit cards in online shopping
4. Promote user reviews which will increase the credibility
5. Persuade users with advertisements similar to what Flipkart did (ads with children to reinforce trust)
6. Show trust in handling credit card data (SSL certification, Put up a sign that indicates customers transaction will be %100 secured and safe)
7. Have a clear privacy policy
8. What is the growth potential of the eRetail sector? (Infibeam)
   1. Currently online retail account for less than 1% of the total retail market in India(~ $1 bn)
   2. It is anticipated that the online retail sector will grow at a CAGR of around 39% during FY 2013-2016
   3. Driven by changing consumer behavior towards shopping and increasing impact of social media, online retail market in India is set to explore new growth opportunities in the coming years.
   4. Internet penetration in India increased from 2.5 percent in 2007 to about 10 percent in 2011 and is expected to further rise to 30 percent by 2015, Resultantly, number of users transacting online is also projected to reach 38 million by 2015 from 11 million in 2011
   5. Another factor supporting e-commerce growth in the country is a relatively young and increasingly wealthy population. More than half of India’s 1.2 billion people are currently below 25 years of age.
   6. The main challenge in eRetail industry is the return of goods(not accepted by customer) which stands around 25%.
   7. Looking at the overall industry trend the Indian eRetail sector has high growth potential
9. What are the new avenues Infibeam should look for in the eRetail sector? (Infibeam)
   1. Sell own line products
   2. Build a two sided market where both buyers and sellers can interact (e.g. e-bay)
   3. Sell digital products (e-books, e-magazines, music etc)
10. How should Makemytrip use IRCTC’s sites inadequacies to its advantage? (Info Edge)
11. Better traffic management (more servers)
12. Continual availability of services (no network failures etc.)
13. Better payment managements system (no truncation in between, no wrongful deduction of amounts etc)
14. How would you stop fake profiles from being registered on jeevansathi.com? (Info Edge)

During registering, ask for mobile number and make a verification call to check the filled in details. Also make sure the number is unique to catch hold of duplicate accounts.

1. Suggest 5 new offerings that Makemytrip could come up with? (Info Edge)
2. Tying up with airlines, credit card companies or other businesses to provide discounts/ vouchers
3. Suggestions for cab bookings after flight to a particular city is booked
4. What should be done to improve Yahoo mail to match Gmail? (Info Edge)
5. Improve interface, reduce advertisements, Introduce search
6. Better integration of email and IM
7. Ease with attachments (yahoo opens a separate page)
8. Better Folder Organization
9. Better Size of attachments
10. Customization (themes, drag drop features etc)

## Operations (Amazon)

1. An online retailer company is experiencing high shipping costs (higher than normal). How would you diagnose the problem?
2. A work flow related problem from OM-1

You’ve just been assigned the job a setting up an electric fan assembly line with the following tasks:

![](data:image/x-wmf;base64...)

What is the Max production per day and the cycle time and the number of work stations?

Answer:

![](data:image/x-wmf;base64...)

![](data:image/x-wmf;base64...)![](data:image/x-wmf;base64...)![](data:image/x-wmf;base64...)

1. What is EOQ and EBQ?

EOQ - Economic Order Quantity. It is the order quantity that minimizes total inventory holding costs and ordering costs. The quantity at which the total cost for the inventory is the least.

Q=(2DS/H)^0.5

Q is the optimum order quantity.

D is the annual demand quantity

S is the ordering costs per order (fixed)

H the annual holding cost per unit

EBQ – Economic batch Quantity. It is a measure used to determine the quantity of units that can be produced at minimum average costs in a given batch or production run.

K = setup cost

D = demand rate

F = holding cost

T = cycle length

P = production rate

Formula: squareroot [ (2x annual demand setup costs)/(inventory carrying cost per unit)]
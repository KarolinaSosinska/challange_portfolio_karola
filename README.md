[//]: <> (Tytuł)
# :one: Task : Software configuration  

[//]: <> (Podtytuł)
## :one: Subtask: Why did I decide to take part in the Dare IT Challenge? 

Cześć, mam na imię Karolina jestem na pierwszym roku studiów informatycznych i to właśnie na jednych z zajęć usłyszałam o **Dare IT** i zaczęłam zagłębiać się w temat.</br>
Treści które przekazujecie są inspirujące. Dobra dawka przystępnej wiedzy merytorycznej, ale też uspokojenie dla takich nowicjuszy jak ja, że można też czasem czegoś nie wiedzieć i to jest normalne.😅

Zdecydowałam się wziąć udział w **Dare IT Challange**, ponieważ jestem na początku swojej przygody w IT i szukam miejsca w którym najlepiej się odnajdę.😉</br>
Zainteresowała mnie forma w której prowadzony jest kurs i jakie możliwości daje.

Moim celem jest przede wszystkim poszerzenie wiedzy, zdobycia doświadczenia w obszarze testów automatycznych i sprawdzenie w praktyce o co w tym tak naprawdę chodzi i czy to mogłaby być</br> potencjalna ścieżka kariery dla mnie.
Jestem zdeterminowana, aby ukończyć wszystkie zadania i wyciągnąć z tego projektu jak najwięcej wiedzy z której przyszłości będę mogła korzystać.</br>
Ogromnym atutem kursu według mnie jest możliwość uzyskania cennego feedbacku od ekspertów oraz kontakt z mentorami i resztą uczestników.</br>
Myślę, że challange pomoże mi rozwinąć zarówno wiedzę techniczną jak i kompetencje miękkie poprzez dodane zdania z obszaru HR.


## **<p style="text-align: right;">Karola</p>**
<br>
<br>
<br>

---

[//]: <> (Selectors)
# :two: Task: Selectors
<br>

| Element strony          |                            Selektor 1:                            |                                                                                Selektor 2: |                                                                                                                                                     Selektor 3: |
|-------------------------|:-----------------------------------------------------------------:|-------------------------------------------------------------------------------------------:|----------------------------------------------------------------------------------------------------------------------------------------------------------------:|
| Napis "Login"           |                      //*[@id="login-label"]                       |                                                                        //*[text()="Login"] |                                                                                                                      html/body/div/form/div/div[1]/div[1]/label |
| Miejsce wpisania loginu |//*[@class="MuiCardContent-root"]//following:: input[@type= "text"]|                                                    //input[@type = "text" or @id= "login"] |                                                                                                                                                //*[@id="login"] |
| Napis "Password"        |            html/body/div/form/div/div[1]/div[2]/label             |                                                                       //*[@for="password"] |                                                                                                              //label[@data-shrink= "true" and @for= "password"] |
| Miejsce wpisania hasła  |         html/body/div/form/div/div[1]/div[2]/div[1]/input         |                                                            //*/input[@value = "Test-1234"] |                                                                                                                                             //*[@id="password"] |
| Remind password         |                              //a[1]                               |                                                        //*[@id="__next"]/form/div/div[1]/a |                                                  //*[contains(@class,"MuiTypography-root MuiLink-root MuiLink-underlineHover jss4 MuiTypography-colorPrimary")] |
| Przycisk "Sign in"      |             //*[contains(@class, "MuiButton-label")]              |                                                                              //span/text() |                                                                                                                /html/body/div/form/div[1]/div[2]/button/span[1] |
| Okno wyboru języka      |               /html/body/div/form/div[1]/div[2]/div               |            //*[contains(@class,"MuiInputBase-root MuiInput-root MuiInput-underline jss6")] |                                                                                                                           //*[@id="__next"]/form/div/div[2]/div |
| Nagłówek "Scouts Panel" |//*[starts-with(@class,"MuiTypography")]|                                                                 //*[text()="Scouts Panel"] |                                                                                                                               /html/body/div/form/div/div[1]/h5 |
| Strzałka wyboru języka  |//*[contains(@class, "MuiSvgIcon-root MuiSelect-icon")]|//*[@id="__next"]//*[@viewBox="0 0 24 24"]|                                                                                                                 //*[@aria-hidden="true" and @focusable="false"] |

<br>
<br>
<br>

---

[//]: <> (Test Cases)
# :four: Task: Refactor, debugger and test cases
<br>
Link to my <a href = "https://drive.google.com/drive/folders/1rpcmPnEsfivsjWbM_BE2PjQRkhqdvCEv?usp=sharing"> Google Drive </a> folder which contains test cases :file_folder:


<br>
<br>
<br>
---

[//]: <> (Test Cases)
# :five: Task: Rrobot framework
<br>
Link to my <a href = "https://github.com/KarolinaSosinska/panelscout_robotframework"> Robot framework </a> repository :computer:


<br>
<br>
<br>
---

[//]: <> (Test Cases)
# :six: Task: Portfolio
<br>
Link to my <a href = "https://github.com/KarolinaSosinska/Portfolio"> Portfolio </a>  :page_with_curl:


<br>
<br>
<br>


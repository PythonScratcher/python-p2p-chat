### Cymraeg 
(english scroll down)
---

# Gwasanaeth Negeseu P2P

Dyma wasanaeth negeseu Peer-to-Peer (P2P) syml wedi'i weithredu yn Python. Mae'n caniatáu i ddefnyddwyr naill ai hostio gweinydd neu gysylltu â gweinydd presennol i gyfnewid negeseu mewn rhyngwyneb deallusol.

### Dechrau

1. **Rhagofynion**
   - Mae Python 3.x wedi'i osod ar eich peiriant.
   - Dealltwriaeth sylfaenol o ddefnyddio rhyngwynebau llinell orchymyn.

2. **Gosod**
   - Clofwch neu lawrlwythwch y repositori i'ch peiriant lleol.

3. **Defnyddio**

   **Hostio Gweinydd:**
   - Agor teml neu banel orchymyn.
   - Ewch i'r cyfeiriadur lle mae `chat.py` wedi'i leoli.
   - Rhedwch y sgript gyda'r dewis `--host` i ddechrau ar hostio gweinydd.
     ```bash
     python chat.py --host
     ```
   - Bydd y gweinydd yn dechrau gwrando ar bort `12392`. Gall cleientiaid gysylltu â'r gweinydd hwn gan ddefnyddio ei gyfeiriad IP.

   **Cysylltu â Gweinydd:**
   - Agor teml neu banel orchymyn.
   - Ewch i'r cyfeiriadur lle mae `chat.py` wedi'i leoli.
   - Rhedwch y sgript heb unrhyw ddewisiadau i weld y dewislen.
     ```bash
     python chat.py
     ```
   - Dewiswch yr opsiwn `2` i gysylltu â gweinydd.
   - Rhowch gyfeiriad IP y gweinydd pan gofynnir.
   - Rhowch eich enw defnyddiwr dymunol pan gofynnir.
   - Yna cewch gysylltiad â'r gweinydd a gallwch ddechrau anfon a derbyn negeseu.

4. **Ymadael**
   - I ymadael â'r sgript, dewiswch opsiwn `3` o'r brif ddewislen.

### Sylwadau

- Sicrhewch fod gennych gysylltedd rhwydwaith i gyfathrebu â chleientiaid neu weinyddion eraill.
- Mae trin gwallau wedi'i weithredu ar gyfer senarios sylfaenol, ond efallai na fydd y sgript yn trin holl achosion ymylol.

### Cymorth

Am unrhyw faterion neu awgrymiadau, agorwch fater yn y llyfrgell.


### English 
(there was welsh because some of my friends are welsh lol)
---

# P2P Messaging Service

This is a simple Peer-to-Peer (P2P) messaging service implemented in Python. It allows users to either host a server or connect to an existing server to exchange messages in a chat-like interface.

### Getting Started

1. **Prerequisites**
   - Python 3.x installed on your machine.
   - Basic understanding of using command-line interfaces.

2. **Setup**
   - Clone or download the repository to your local machine.

3. **Usage**

   **Hosting a Server:**
   - Open a terminal or command prompt.
   - Navigate to the directory where `chat.py` is located.
   - Run the script with the `--host` option to start hosting a server.
     ```bash
     python chat.py --host
     ```
   - The server will start listening on port `12392`. Clients can connect to this server using its IP address.

   **Connecting to a Server:**
   - Open a terminal or command prompt.
   - Navigate to the directory where `chat.py` is located.
   - Run the script without any options to see the menu.
     ```bash
     python chat.py
     ```
   - Choose option `2` to connect to a server.
   - Enter the IP address of the server when prompted.
   - Enter your desired username when prompted.
   - You will then be connected to the server and can start sending and receiving messages.

4. **Exiting**
   - To exit the script, choose option `3` from the main menu.

### Notes

- Ensure that you have network connectivity to communicate with other clients or servers.
- Error handling is implemented for basic scenarios, but the script may not handle all edge cases.

### Support

For any issues or suggestions, please open an issue in the repository.

---



# reVerse_$hell

# Python Reverse Shell

This repository contains a simple Python-based reverse shell implementation. The project is designed for **educational purposes only**, helping users understand how reverse shells work and the potential risks associated with them. It serves as a learning tool for cybersecurity enthusiasts and ethical hackers in controlled environments.

## Features

- **Two scripts**:
  - **Listener**: Runs on the attacker's machine to receive commands.
  - **Client**: Runs on the target's machine to execute commands and send responses.
- Bi-directional communication for command execution.
- Lightweight and easy-to-understand codebase for learning purposes.

## Usage

### Prerequisites
- Python 3.x installed on both systems.
- Ensure you have proper authorization to run this tool in your environment.

### Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/PhinehasNarh/reVerse_5hell
   cd reVerse_5hell
   ```

2. Install dependencies (if any are added in future versions).

### Running the Listener
Run the listener script on the attacker’s machine:
```bash
python listener.py
```

### Running the Client
Run the client script on the target’s machine:
```bash
python client.py
```

- Replace the `server_host` and `server_port` in the **client.py** file with the IP address and port of your listener.

### Terminating the Connection
- To terminate the session, type `exit` in the listener shell.

---

## Example Output

### Listener
```plaintext
[+] Listening on 0.0.0.0:9999
[+] Connection established with ('192.168.1.100', 54321)
Shell> ls
Desktop
Documents
Downloads
```

### Client
```plaintext
[+] Connected to the server.
```

---

## Legal and Ethical Disclaimer

This project is for **educational purposes only**. Unauthorized use of a reverse shell on any device or network is illegal and violates privacy laws. Use this tool only on systems where you have **explicit permission** or in controlled environments, such as virtual labs or test networks.

**Misuse of this tool can lead to severe legal consequences.** Always follow ethical hacking principles and obtain proper authorization before testing.

---

## Contributing

Contributions are welcome to improve the educational value of this project. Submit issues or feature requests via GitHub, or create a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgements

This project is inspired by the need for hands-on learning in ethical hacking and cybersecurity. It’s built to help learners understand the mechanics of reverse shells while promoting responsible use.


### #ph1n3y

[![logo.png](logo.png)](https://hpi.de/en/kisz/home.html)

## About us
Welcome to the MLOps Series taught by AI Services from the Hasso-Plattner-Institute. We are a publicly funded project supported by the BMBF (Federal Ministry of Education and Research). Visit [our website](https://hpi.de/kisz) to learn more about our offerings and join our [AI Maker Community on Slack](https://join.aimaker.community) to keep track of our weekly workshops and paper readings.

## About the series
In this series of workshops we dive into the basics of Docker and try to give an intuitive understanding about how it can be used. As the series progresses, we will demonstrate how Docker can be used for ML projects for local development and for serving models using an API.

## Follow along on JupyterHub
We can follow this workshop fully through our JupyterHub at [https://mlops.aihpi.de](https://mlops.aihpi.de). There is **no need to install software locally**, but we also provide the instructions for a local installation as an option.

## Local Installation Guide
This guide provides instructions for installing and setting up all the tools and environments you need to participate in the workshop.
Familiarity with opening and using a terminal is required. Here's how you can start a terminal:

- **On Windows:** Search for `cmd` or `Command Prompt` in the Start menu.
- **On Mac:** Open the `Terminal` app from the Utilities folder.
- **On Linux:** Use your distribution's default terminal.

### Step 1: Install Git
- **Purpose of Git:** Git is a version control system essential for managing code changes and collaboration.
- **How to Install:** Download and install Git by following the instructions on [Git Guides](https://github.com/git-guides/install-git).
- **Verify Installation:** In the terminal, run `git --version`. The output should display the Git version. You may need to restart your terminal before this command becomes accessible.

### Step 2: Install Docker
Please install Docker before attending the workshop. Detailed instructions are provided below.

- **Purpose of Docker:** Docker is key for creating and running containerized applications, ensuring consistency across environments.
- **How to Install:** Follow the installation instructions based on your OS:
  - [Windows](https://docs.docker.com/desktop/install/windows-install/)
  - [Mac](https://docs.docker.com/desktop/install/mac-install/)
  - [Linux](https://docs.docker.com/desktop/install/linux-install/)
- **Verify Installation:** In the terminal, run `docker --version`. The output should display the Docker version. Restarting your computer may be necessary before this command becomes accessible.

### Step 3: Install an IDE
- **What's an IDE?** An Integrated Development Environment (IDE) is a platform for coding, editing, and debugging your code. It also serves as a graphical user interface for Git.
- **Recommended IDEs:** 
  - [Visual Studio Code](https://code.visualstudio.com/) - Versatile and lightweight.
  - [PyCharm Community Edition](https://www.jetbrains.com/pycharm/download/) - Tailored for Python development.
- **Verify Installation:** You can verify your installation by cloning a GitHub repository. Please refer to the following guides:
  - [Visual Studio Code - Clone Guide](https://learn.microsoft.com/en-us/azure/developer/javascript/how-to/with-visual-studio-code/clone-github-repository?tabs=create-repo-command-palette%2Cinitialize-repo-activity-bar%2Ccreate-branch-command-palette%2Ccommit-changes-command-palette%2Cpush-command-palette#clone-repository)
  - [PyCharm - Clone Guide](https://www.jetbrains.com/help/pycharm/manage-projects-hosted-on-github.html#clone-from-GitHub)

### Troubleshooting and Support
If you encounter installation issues, consult the respective software's documentation or contact us at [kisz@hpi.de](mailto:kisz@hpi.de) for assistance.

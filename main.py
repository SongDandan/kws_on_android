if __name__ == '__main__':
    main()

~from pr_agent import cli
from pr_agent.config_loader import get_settings

def main():
    # Fill in the following values
    provider = "github" # GitHub provider
    user_token = "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"  # GitHub user token
    openai_key = "sk-vvv-IP0TrzvWgFuO4mpTcu8pT3BlbkFJ7b6Ucg7F0E7Y3Nz9DtTW"  # OpenAI key
    pr_url = "https://github.com/robin1001/kws_on_android/pull/4"   # PR URL, for example 'https://github.com/Codium-ai/pr-agent/pull/809'
    command = "/review" # Command to run (e.g. '/review', '/describe', '/ask="What is the purpose of this PR?"', ...)

    # Setting the configurations
    get_settings().set("CONFIG.git_provider", provider)
    get_settings().set("openai.key", openai_key)
    get_settings().set("github.user_token", user_token)

    # Run the command. Feedback will appear in GitHub PR comments
    cli.run_command(pr_url, command)


if __name__ == '__main__':
    main()


from pr_agent import cli
from pr_agent.config_loader import get_settings

def main():
    # Fill in the following values
    provider = "github" # GitHub provider
    user_token = "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"  # GitHub user token
    openai_key = "sk-vvv-IP0TrzvWgFuO4mpTcu8pT3BlbkFJ7b6Ucg7F0E7Y3Nz9DtTW"  # OpenAI key
    pr_url = "https://github.com/Harpsichord1207/AWSExamV2/pull/1"   # PR URL, for example 'https://github.com/Codium-ai/pr-agent/pull/809'
    command = "/review" # Command to run (e.g. '/review', '/describe', '/ask="What is the purpose of this PR?"', ...)

    # Setting the configurations
    get_settings().set("CONFIG.git_provider", provider)
    get_settings().set("openai.key", openai_key)
    get_settings().set("github.user_token", user_token)

    # Run the command. Feedback will appear in GitHub PR comments
    cli.run_command(pr_url, command)


if __name__ == '__main__':
    main()
~                  

{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyM89KIWbfmzYtGCd6uugJRa"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": 20,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 173
        },
        "id": "e7kEw7ojXCXC",
        "outputId": "57bf727f-6818-4081-c313-0ae4e0f312a6"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "                                               title  \\\n",
            "0  [\\n                            When did Islam ...   \n",
            "\n",
            "                                            question  \\\n",
            "0  [\\n            , [Question], \\n            , [...   \n",
            "\n",
            "                                              answer  \n",
            "0  [\\n\\n                , [\\n                    ...  \n",
            "ok\n"
          ]
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<IPython.core.display.Javascript object>"
            ],
            "application/javascript": [
              "\n",
              "    async function download(id, filename, size) {\n",
              "      if (!google.colab.kernel.accessAllowed) {\n",
              "        return;\n",
              "      }\n",
              "      const div = document.createElement('div');\n",
              "      const label = document.createElement('label');\n",
              "      label.textContent = `Downloading \"${filename}\": `;\n",
              "      div.appendChild(label);\n",
              "      const progress = document.createElement('progress');\n",
              "      progress.max = size;\n",
              "      div.appendChild(progress);\n",
              "      document.body.appendChild(div);\n",
              "\n",
              "      const buffers = [];\n",
              "      let downloaded = 0;\n",
              "\n",
              "      const channel = await google.colab.kernel.comms.open(id);\n",
              "      // Send a message to notify the kernel that we're ready.\n",
              "      channel.send({})\n",
              "\n",
              "      for await (const message of channel.messages) {\n",
              "        // Send a message to notify the kernel that we're ready.\n",
              "        channel.send({})\n",
              "        if (message.buffers) {\n",
              "          for (const buffer of message.buffers) {\n",
              "            buffers.push(buffer);\n",
              "            downloaded += buffer.byteLength;\n",
              "            progress.value = downloaded;\n",
              "          }\n",
              "        }\n",
              "      }\n",
              "      const blob = new Blob(buffers, {type: 'application/binary'});\n",
              "      const a = document.createElement('a');\n",
              "      a.href = window.URL.createObjectURL(blob);\n",
              "      a.download = filename;\n",
              "      div.appendChild(a);\n",
              "      a.click();\n",
              "      div.remove();\n",
              "    }\n",
              "  "
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<IPython.core.display.Javascript object>"
            ],
            "application/javascript": [
              "download(\"download_3948ecfa-1a9b-44f2-9b11-73e1020eeb50\", \"demo.csv\", 2796)"
            ]
          },
          "metadata": {}
        }
      ],
      "source": [
        "from bs4 import BeautifulSoup\n",
        "import requests\n",
        "import pandas as pd\n",
        "\n",
        "url = \"https://islamqa.info/en/categories/very-important/120/answers/10267/when-did-islam-begin-and-who-started-the-muslim-tradition\"\n",
        "response = requests.get(url)\n",
        "soup = BeautifulSoup(response.content, \"html5\")\n",
        "\n",
        "title = soup.find(class_=\"title is-4 is-size-5-touch\")\n",
        "# print(title.text)\n",
        "\n",
        "question = soup.find(class_=\"single_fatwa__question text-justified\")\n",
        "# print(question.text)\n",
        "\n",
        "answer = soup.find(class_=\"single_fatwa__answer__body text-justified _pa--0\")\n",
        "# print(answer.text)\n",
        "\n",
        "data=[[title, question, answer]]\n",
        "df=pd.DataFrame(data,columns=[\"title\",\"question\",\"answer\"])\n",
        "print(df)\n",
        "df.to_csv(\"demo.csv\")\n",
        "print(\"ok\")\n"
      ]
    }
  ]
}
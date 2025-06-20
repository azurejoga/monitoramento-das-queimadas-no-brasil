# Monitoramento de Queimadas na Amazônia

Este projeto tem como objetivo monitorar as queimadas na Amazônia e apresentar informações diárias atualizadas sobre os focos de incêndio detectados. Abaixo, você pode visualizar as queimadas mais recentes, com detalhes sobre localização, satélite que realizou a detecção, e outros fatores relevantes.

## Estrutura dos Dados

Cada entrada na tabela representa um foco de incêndio com as seguintes informações:

- **ID:** Identificador único do foco de incêndio.
- **Latitude/Longitude:** Coordenadas geográficas do foco detectado. Para visualizar o local exato, insira estas coordenadas no Google Maps ou outro aplicativo de mapas.
- **Data/Hora GMT:** Data e hora da detecção em formato GMT (Greenwich Mean Time).
- **Satélite:** Satélite responsável pela detecção do foco de incêndio.
- **Município, Estado e País:** Localização administrativa do foco detectado.
- **Dias sem Chuva:** Número de dias consecutivos sem precipitação na região, o que pode indicar um aumento no risco de incêndio.
- **Precipitação:** Quantidade de chuva (em milímetros) registrada no local.
- **Risco de Fogo:** Índice que indica a probabilidade de ocorrência de incêndio, baseado em fatores como condições climáticas e quantidade de combustível disponível.
- **Bioma:** Bioma onde o foco foi identificado, como Amazônia, Cerrado, ou Mata Atlântica.
- **FRP (Fire Radiative Power):** Potência radiativa do fogo, que mede a intensidade do incêndio. Focos com FRP mais alto indicam incêndios mais intensos.

## Visualização Gráfica

Se você deseja visualizar de forma gráfica onde as queimadas estão ocorrendo, copie as coordenadas de latitude e longitude mais recentes e cole no Google Maps. Isso permite uma compreensão espacial mais clara da distribuição dos focos de incêndio. Alternativamente, você também pode usar a descrição de localização (Município, Estado e País) para identificar a região afetada.

## Informação Adicional

As queimadas na Amazônia não apenas afetam a biodiversidade local, mas também têm implicações globais, contribuindo para o aquecimento global e a emissão de gases de efeito estufa. O monitoramento contínuo é essencial para entender e mitigar os impactos desses incêndios, além de auxiliar na gestão de políticas ambientais e ações de preservação.

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2ac1ab2a-2dc0-3141-8733-f26783a12613 | -7.89127 | -61.47357 | 2025-06-20 05:21:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7ad8b53b-166f-3f81-a72a-bc4116af2109 | -12.20481 | -49.62668 | 2025-06-20 05:21:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e5d79517-9674-319e-98da-a96867bb37d6 | -11.53199 | -56.98217 | 2025-06-20 05:21:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 01c2f74c-692d-346b-94c6-2bf81d1a8a14 | -11.94728 | -58.75007 | 2025-06-20 05:21:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 046f5e3c-2bdb-3d81-b545-60b2e4f501c6 | -10.82983 | -54.01194 | 2025-06-20 05:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 52d19d66-acc2-3390-b431-8456cd85faf3 | -10.66213 | -49.36172 | 2025-06-20 05:21:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f2b1904e-0da1-3f0c-a1ec-effac6791b6b | -11.77549 | -54.36736 | 2025-06-20 05:21:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c76a4e6f-89ae-350d-bdfa-57f49bdad146 | -12.04768 | -63.78197 | 2025-06-20 05:21:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 5.0 |
| aa722f6f-5db4-3858-bc45-467082e936e5 | -11.57397 | -47.87658 | 2025-06-20 05:21:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9d34a3ab-2ebc-3490-8ff7-57cc2235edc0 | -11.12707 | -46.67403 | 2025-06-20 05:21:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ce0650d6-99fb-308a-9b17-cde267841a94 | -14.03334 | -53.36978 | 2025-06-20 05:21:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ee745a00-28b7-34a8-9654-807c0df1df3a | -11.14933 | -46.64802 | 2025-06-20 05:21:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 3950fbd1-13d7-3325-b817-6c1a4304d65f | -12.51008 | -58.347 | 2025-06-20 05:21:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| be1c6aaf-bab4-388f-9ddf-9a8d25f788f6 | -13.10008 | -52.29498 | 2025-06-20 05:21:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 32f30758-0530-31f9-9fc8-bb2785aa0611 | -11.81743 | -54.50352 | 2025-06-20 05:21:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 41c28a5f-bb1e-3ee9-b2e9-634dd4f8fcb5 | -9.48751 | -56.08644 | 2025-06-20 05:21:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| dcee3f1f-e1a9-3390-95ba-497cdabd41ef | -12.04264 | -63.77389 | 2025-06-20 05:21:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 276796a0-0e3d-3865-b6d0-bf0da0999481 | -9.95272 | -64.99324 | 2025-06-20 05:21:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 850ef3de-ff37-342a-9586-63d352ae34e0 | -10.66877 | -56.55308 | 2025-06-20 05:21:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fffc92d7-493a-369f-ad12-9f12372e8a7d | -10.45929 | -47.05648 | 2025-06-20 05:21:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 16.3 |
| b1c2e003-31ce-3cdf-8875-bb73e37ef300 | -10.86542 | -53.75845 | 2025-06-20 05:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f77be22f-cb1b-3a8c-a2e0-7c68aeadc09a | -14.30792 | -59.89452 | 2025-06-20 05:21:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f523499e-c23c-35ae-85bf-a21d829ace9b | -11.98146 | -51.60933 | 2025-06-20 05:21:00 | NPP-375D | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6d0ac168-6cbb-3cba-9b8b-947384fce131 | -12.05211 | -63.77826 | 2025-06-20 05:21:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 5.0 |
| dad01c01-d186-3963-855d-05d28072186d | -10.46036 | -47.05937 | 2025-06-20 05:21:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 14.0 |
| b2e47543-ef52-387f-98f7-b12fa23aa781 | -14.50499 | -58.67495 | 2025-06-20 05:21:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b538a305-5ed6-3952-ab56-279601e16a73 | -10.48415 | -47.03205 | 2025-06-20 05:21:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b033a39f-1db4-3a25-9750-01b5f3dbe57f | -12.50549 | -58.35408 | 2025-06-20 05:21:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 56215a51-52ab-3c1f-8a1d-41ce05293f8c | -13.29019 | -57.08201 | 2025-06-20 05:21:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d070801d-c2b9-36db-9c4a-0f1b37bdfe16 | -11.95633 | -58.75904 | 2025-06-20 05:21:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 4712e380-4773-3f02-be31-de0715c2a47b | -10.86955 | -53.76178 | 2025-06-20 05:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7a68fcc7-37a7-3708-a691-a0c67c0dda08 | -11.6201 | -58.29226 | 2025-06-20 05:21:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 229d7a78-aa7e-3d58-bd62-f9f8fd8815c3 | -9.30256 | -47.7942 | 2025-06-20 05:21:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b27baf59-b3b9-3190-be09-2bbe5ca0347d | -10.47664 | -47.03749 | 2025-06-20 05:21:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 7dfba603-c34d-37b6-bab2-7ba140b3149c | -11.64782 | -54.54815 | 2025-06-20 05:21:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dbbaaada-0d03-3a52-96a9-35bec6ad85dc | -14.81388 | -48.46894 | 2025-06-20 05:21:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8ba02732-289b-394e-8d58-c5c1ce0554a7 | -11.14859 | -46.65461 | 2025-06-20 05:21:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b6111e96-1ba1-3aef-8073-ee888a4a233a | -13.96174 | -56.80011 | 2025-06-20 05:21:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ca43d419-517c-30e8-86d6-bede8feea405 | -14.03675 | -53.36867 | 2025-06-20 05:21:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6d4fe117-8027-3411-ab77-9c926dc37d47 | -11.98661 | -51.61008 | 2025-06-20 05:21:00 | NPP-375D | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 38b2bf83-e12e-320c-b1e1-80e7eefb52ad | -9.48137 | -56.0765 | 2025-06-20 05:21:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 54c6a955-80f6-3e30-ad71-4b6db5393f8e | -9.45694 | -57.84196 | 2025-06-20 05:21:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e24916f1-43cb-3cb7-8f11-fea59b54f3f6 | -11.53438 | -56.99115 | 2025-06-20 05:21:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0a3f9dd3-d3da-362f-af0c-2246f811d221 | -13.97383 | -58.10383 | 2025-06-20 05:21:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 73feff2b-356d-3b8c-afe2-39100c5e6e75 | -11.47208 | -47.30233 | 2025-06-20 05:21:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fa751c97-58d2-3bc2-aef3-761280d3d38d | -10.46676 | -47.05159 | 2025-06-20 05:21:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 24.2 |
| eed3033f-0010-3adc-80d3-c7e5f5bf9e6b | -11.1466 | -46.62857 | 2025-06-20 05:21:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| be196fed-70f0-3b1c-a293-7bec691085e0 | -11.14387 | -46.63355 | 2025-06-20 05:21:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6a912ef7-f515-30a0-9a4f-2494d34a3330 | -10.92618 | -49.27903 | 2025-06-20 05:21:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f3ce39fc-3a10-38fc-8116-ec832d5a88be | -12.50894 | -58.35462 | 2025-06-20 05:21:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 76e35df1-d974-38db-b5ff-d413ed77dd72 | -10.8643 | -53.76693 | 2025-06-20 05:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9b7bf07b-e668-3f86-a985-982853702a0a | -10.16255 | -48.98612 | 2025-06-20 05:21:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| be98687e-057f-3818-b691-9b5b4d66c781 | -9.45924 | -57.84995 | 2025-06-20 05:21:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a65e955d-c18b-3f73-b66a-1332b103ca44 | -10.12781 | -58.22052 | 2025-06-20 05:21:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 3206506c-5937-38e7-8346-e0f932bbf04f | -11.13315 | -46.66622 | 2025-06-20 05:21:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e28d3410-fb31-342b-a530-0f34764aa770 | -12.28133 | -57.2702 | 2025-06-20 05:21:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b4d2dc92-5019-3079-8c8c-cd6eb3fa3294 | -10.72627 | -49.5554 | 2025-06-20 05:21:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1652eb3c-e0ec-3ea1-8422-330bb366e78d | -11.45989 | -47.30194 | 2025-06-20 05:21:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ffa2cd36-5c33-3646-96a9-906ac3715e49 | -8.33425 | -55.09692 | 2025-06-20 05:21:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2c5f0bfb-b2ba-3fa6-b6dc-0c43cc554415 | -10.47425 | -47.04649 | 2025-06-20 05:21:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 4dba4fab-62ff-31d4-8ea9-09ca4b2aac6b | -9.49865 | -56.08814 | 2025-06-20 05:21:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f5786746-f1ba-3b47-bc7c-4ca5f1653291 | -10.36136 | -57.50286 | 2025-06-20 05:21:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e63eddcc-4029-3b67-a691-81457e928eb8 | -11.81798 | -54.49957 | 2025-06-20 05:21:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7c06008b-8dfb-3eff-a885-ac570ac25971 | -10.47574 | -47.0344 | 2025-06-20 05:21:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 20.6 |
| cafe4d9e-be54-3071-a1c0-54244d37fb21 | -10.67611 | -56.55423 | 2025-06-20 05:21:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 853e3b03-2f38-3a6b-95a2-423f194e085d | -10.50537 | -53.58313 | 2025-06-20 05:21:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 808692df-e9df-3cf8-b0de-86d4433522e2 | -11.94841 | -58.74269 | 2025-06-20 05:21:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 12.9 |
| fb60cdfe-6792-3864-99d2-3fa1c2c552da | -10.47499 | -47.04052 | 2025-06-20 05:21:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 20.6 |
| cc4f1065-ee61-38a4-9395-e514d07f02ab | -11.77494 | -54.37138 | 2025-06-20 05:21:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9be3f2c5-c2e3-39bf-a2b2-75ab3b265425 | -10.36078 | -57.50677 | 2025-06-20 05:21:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b4fcfc56-5271-3979-88a4-f41735458596 | -10.45361 | -47.05843 | 2025-06-20 05:21:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 0ffedd31-3457-35d9-b6c3-e2641a6c6c98 | -12.13289 | -54.66944 | 2025-06-20 05:21:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3e89d06a-3a81-3bb9-8d9a-b8c5c82b8de0 | -12.34776 | -49.30793 | 2025-06-20 05:21:00 | NPP-375D | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a3929b65-81a4-3bb1-a1e9-8aa52ce38865 | -11.84137 | -57.76059 | 2025-06-20 05:21:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 71382289-757f-3911-8ac2-ea157c21c89e | -11.53075 | -56.99061 | 2025-06-20 05:21:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c6dc325b-155b-3adc-b29e-d321d43b3278 | -14.0434 | -53.36598 | 2025-06-20 05:21:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 61f99e88-5de4-3690-a0fc-34642cc12638 | -10.66108 | -49.37012 | 2025-06-20 05:21:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 2e3f0731-bdf4-36bf-8209-dc7c4df9cba7 | -9.31444 | -47.79425 | 2025-06-20 05:21:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 63853b2a-9dc6-3e12-9dfa-a7f1542b6413 | -10.86077 | -53.76064 | 2025-06-20 05:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e13dda43-2c28-35dc-a54c-ed5531823584 | -13.36463 | -54.26116 | 2025-06-20 05:21:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 333c3560-6080-3cd1-b543-971dc24968ea | -12.05578 | -63.77891 | 2025-06-20 05:21:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 736f6941-e2da-374d-9d1f-6812853dc106 | -10.49997 | -47.01448 | 2025-06-20 05:21:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 95dd5a3a-3302-3e90-92cc-66df0a519958 | -11.46797 | -47.29071 | 2025-06-20 05:21:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 062e1cc7-ce93-3875-b930-be0a484cb1e1 | -12.34121 | -49.31164 | 2025-06-20 05:21:00 | NPP-375D | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 65d6c11e-cd86-3b36-8eed-d300413ddbf2 | -10.07512 | -52.74094 | 2025-06-20 05:21:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| df3eb7f5-8d0a-3c7b-964e-80c3418d6dd4 | -11.12693 | -46.65852 | 2025-06-20 05:21:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a5693f46-262d-37da-9814-a2c2d30f523c | -7.90109 | -61.52217 | 2025-06-20 05:21:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a989a2b9-c8e6-3b84-9a00-0ce837c93b7e | -14.16809 | -60.05725 | 2025-06-20 05:21:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9b3e7bc8-8242-3d87-8705-7b5d0a752205 | -12.04191 | -63.77827 | 2025-06-20 05:21:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2bd921a5-aa92-3ff9-82f3-b7ec93159027 | -11.37194 | -55.11389 | 2025-06-20 05:21:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a41a5d12-9b32-3a04-9c45-d861beb2998a | -12.54682 | -57.71041 | 2025-06-20 05:21:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| db0534f8-8f23-32fc-99a6-3e69fa9019ad | -9.45751 | -57.83823 | 2025-06-20 05:21:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 9a053ca2-440b-3ecd-8f85-de5224555c44 | -11.58052 | -47.87716 | 2025-06-20 05:21:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aab4b25f-89f6-383e-b397-2a04c6b4889c | -11.95519 | -58.74377 | 2025-06-20 05:21:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e9ea28f2-2e9a-3cdc-994c-02f9cae92686 | -9.3739 | -47.6377 | 2025-06-20 05:21:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 720df896-0729-3572-bb6f-4babeb019f8f | -14.4803 | -50.29305 | 2025-06-20 05:21:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 74418470-933b-3065-a904-14020ca6d691 | -14.17143 | -60.05779 | 2025-06-20 05:21:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5ace73ad-3ac2-3f5c-829c-e0ad5afa6f32 | -10.0884 | -52.74775 | 2025-06-20 05:21:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d53978f2-03ce-3a7a-bc07-5db2fd455bc0 | -10.86136 | -53.7564 | 2025-06-20 05:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 77bc5161-4d9d-392a-963e-2dfdad632ceb | -14.0327 | -53.36294 | 2025-06-20 05:21:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |


[Clique aqui para ver as próximas entradas](README26.md)

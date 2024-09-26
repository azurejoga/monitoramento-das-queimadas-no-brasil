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

## Dados Diários - Página 153

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c96f8c8b-48f5-3083-8cb2-4a5815d26452 | -7.56617 | -55.15789 | 2024-09-26 05:42:00 | AQUA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 38.7 |
| a100ebe1-7a44-374d-a969-36aaaa1afef7 | -7.56435 | -55.16958 | 2024-09-26 05:42:00 | AQUA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 35.1 |
| bba0d42d-b8bf-38ec-9327-cd2ee919527d | -7.55617 | -55.15635 | 2024-09-26 05:42:00 | AQUA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 31f8c72e-eb4e-3d32-ac2d-13d02c2f6fbd | -7.55159 | -55.12032 | 2024-09-26 05:42:00 | AQUA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| a2f1c2f1-8331-3040-ae43-2f60eb1e641e | -7.49256 | -47.07999 | 2024-09-26 05:42:00 | AQUA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 2ced1443-ab48-3641-92f2-8047dc1fe9ed | -7.49242 | -47.08517 | 2024-09-26 05:42:00 | AQUA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| f6d61fbe-08d5-3bee-8dfa-725d6dbc36c5 | -7.37098 | -55.48499 | 2024-09-26 05:42:00 | AQUA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 21.5 |
| e72dcf2b-9e5d-3190-9618-8451fb3f1d7e | -7.36902 | -55.49722 | 2024-09-26 05:42:00 | AQUA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 1cdf224a-2f57-3c69-aeaf-b99298a87eb5 | -7.36708 | -55.5093 | 2024-09-26 05:42:00 | AQUA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 158.3 |
| ceda6ae4-331e-3af9-9338-62e68bd52b45 | -7.36512 | -55.5215 | 2024-09-26 05:42:00 | AQUA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 65e4b3a9-0dd8-38ec-b958-dcf1788623c7 | -7.36124 | -55.49018 | 2024-09-26 05:42:00 | AQUA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 17.7 |
| f37a8fbb-8781-34c2-a501-666661f08575 | -7.35936 | -55.50235 | 2024-09-26 05:42:00 | AQUA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 39.1 |
| 400a25b6-da93-3ad0-83ff-b8e3f6d97409 | -7.35874 | -55.49564 | 2024-09-26 05:42:00 | AQUA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 21.8 |
| d4b135a0-2c67-3476-80ad-5bb40ce7de90 | -7.35749 | -55.51442 | 2024-09-26 05:42:00 | AQUA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 3bdba366-d02d-37ee-b455-3fafe816fd76 | -7.3568 | -55.50767 | 2024-09-26 05:42:00 | AQUA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| e01a7862-3f16-385a-8054-23818273fcca | -7.28904 | -61.0947 | 2024-09-26 05:42:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 47.1 |
| a7253641-0f42-363d-b68a-1091ba4b7687 | -7.28227 | -61.08561 | 2024-09-26 05:42:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 40.6 |
| 73ee27ce-abe6-3183-b416-1cef90392ed9 | -6.79823 | -59.29996 | 2024-09-26 05:42:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 28.2 |
| c5cd2315-faf6-329a-b461-e4e146d0a6fd | -6.78421 | -59.29768 | 2024-09-26 05:42:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 29.5 |
| aed167cc-2731-3295-b982-60bdf2fe0c2e | -6.56821 | -60.03469 | 2024-09-26 05:42:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 23.4 |
| c0ddaf94-f343-315a-8f28-665c8a8855bc | -17.9142 | -53.6648 | 2024-09-26 05:44:00 | AQUA_M-M | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8319d60e-b41c-3d7f-b25a-a7477f187d87 | -17.12314 | -56.24141 | 2024-09-26 05:44:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| ce8d2c9c-2df6-3573-8f11-7c0a9d501b98 | -17.10165 | -56.19515 | 2024-09-26 05:44:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 21.6 |
| fbfaae78-e1df-39b1-8bb0-f18e7255595a | -17.09716 | -56.3442 | 2024-09-26 05:44:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 15.2 |
| a38d6dd8-2c2d-36e4-87bb-0a1d3c884771 | -17.09549 | -56.35472 | 2024-09-26 05:44:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.3 |
| a6f33ca5-855f-3dd0-9819-e06cc32343b5 | -17.09395 | -56.18322 | 2024-09-26 05:44:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 46.6 |
| 93409f54-7624-336a-940d-1bf9679b51b2 | -17.09381 | -56.36525 | 2024-09-26 05:44:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| b4a782ea-0956-33a5-94e2-900fb32152fa | -17.0923 | -56.19354 | 2024-09-26 05:44:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 55.4 |
| 2101658b-26c9-3fa2-b02e-00b1dd8830f8 | -17.09064 | -56.20388 | 2024-09-26 05:44:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 19.4 |
| fd5a8fd9-1638-3938-a9fc-ca69c1f328a5 | -17.08792 | -56.16098 | 2024-09-26 05:44:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 53.3 |
| 4400d6b2-bbe7-32ca-9ab6-a2e3128aad2e | -17.08774 | -56.34258 | 2024-09-26 05:44:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| db3a2f87-05f9-39df-8249-1984eab6c0ba | -17.08627 | -56.1713 | 2024-09-26 05:44:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 26.5 |
| 5a5cd28e-3359-3487-8360-2904788c9089 | -17.08607 | -56.35308 | 2024-09-26 05:44:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.5 |
| f6cdf0cf-b251-3baf-864d-b1abf01a0bd9 | -17.08461 | -56.18162 | 2024-09-26 05:44:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 97.0 |
| 7d731875-bfd5-39fb-ba4c-33990fab3530 | -17.08295 | -56.19194 | 2024-09-26 05:44:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 122.5 |
| 6206b04a-c6cf-31f0-bb4b-13ab4b47b968 | -17.08129 | -56.20227 | 2024-09-26 05:44:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 33.1 |
| 35b3980e-7413-3ea5-b283-1c6da0fde719 | -17.08024 | -56.14909 | 2024-09-26 05:44:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 22.2 |
| 30282be3-917c-31ac-8991-91768e34feef | -17.07858 | -56.15939 | 2024-09-26 05:44:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 24.8 |
| 57c90abd-f12a-37a2-ae7a-c6dd1fc59ca5 | -17.07693 | -56.16969 | 2024-09-26 05:44:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 19.4 |
| efe0a1af-8713-3bb9-93ba-644b4d3e36a4 | -17.07526 | -56.18002 | 2024-09-26 05:44:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 79.1 |
| a6a11739-7041-34b7-85ae-4289b08989e4 | -17.0736 | -56.19033 | 2024-09-26 05:44:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 174.4 |
| d1a4eaba-590e-3fd7-81a6-54174f8d3b17 | -17.07194 | -56.20066 | 2024-09-26 05:44:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 44.5 |
| 3f1bc7c9-f17f-3280-8954-93c6dd8afa2a | -17.06925 | -56.15779 | 2024-09-26 05:44:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 21.8 |
| c2901a28-910e-3da2-8faf-f6c50bcee7a8 | -17.06758 | -56.16809 | 2024-09-26 05:44:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 46.3 |
| 1e6f94e9-101d-32b3-9afa-f384213b0829 | -17.06592 | -56.17841 | 2024-09-26 05:44:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 59.4 |
| 85bbc047-7c88-3f76-bb2d-2d7e3c6b3f0d | -17.06425 | -56.18873 | 2024-09-26 05:44:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 49.4 |
| ccd15d4c-0afa-37e9-bb4c-25fc60ee0d9c | -17.06258 | -56.19905 | 2024-09-26 05:44:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 14.2 |
| 2e399707-2287-380f-806c-b417de3dd047 | -17.06091 | -56.2094 | 2024-09-26 05:44:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 1f5d611a-0971-3501-8426-cb52901bc7ef | -17.05824 | -56.16648 | 2024-09-26 05:44:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 47.6 |
| 850991a7-f3d2-31ee-b7f2-195cea4ecf74 | -17.05657 | -56.17681 | 2024-09-26 05:44:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 35.0 |
| 72a885c1-8b40-31e0-91fd-485ec6a43d45 | -17.0549 | -56.18713 | 2024-09-26 05:44:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 24.9 |
| cde54564-c894-35e0-8374-ffe5ebbdef48 | -17.05323 | -56.19745 | 2024-09-26 05:44:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 10.1 |
| f3eb134b-4419-3cc5-a6fd-0e88709e2058 | -17.04555 | -56.18553 | 2024-09-26 05:44:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 17.4 |
| d1b2ab32-59e2-3082-9984-4efc95ef6482 | -17.03998 | -56.17883 | 2024-09-26 05:44:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 11.7 |
| 88a3efd3-4856-3134-ab1d-4c8f0be9f69b | -17.03834 | -56.18915 | 2024-09-26 05:44:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 18.5 |
| b2b48849-572b-3758-b6d1-52153becb743 | -17.03063 | -56.17722 | 2024-09-26 05:44:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 19.8 |
| 5da63262-9ed4-371d-8ce1-5e50e53319b3 | -17.02899 | -56.18755 | 2024-09-26 05:44:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 40.5 |
| 21772592-5c53-3468-bf28-5c6dd572af78 | -16.98991 | -56.19146 | 2024-09-26 05:44:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.7 |
| 2c955f58-699d-386f-8918-44bca6944913 | -16.93957 | -56.11254 | 2024-09-26 05:44:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 10.4 |
| 5e6bb685-8f55-309b-8e6f-9482d4cbfa23 | -16.77174 | -55.94554 | 2024-09-26 05:44:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 21.2 |
| 5cbce6a0-f2e2-33ce-8614-33707603206e | -16.77012 | -55.9557 | 2024-09-26 05:44:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 33.1 |
| 391943fe-dd62-3165-8e90-a678573a13e5 | -16.73257 | -55.54425 | 2024-09-26 05:44:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.0 |
| 43470c1d-c93e-39af-ac92-7ee830e52df0 | -16.59495 | -54.09709 | 2024-09-26 05:44:00 | AQUA_M-M | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| a4dd3951-3f3f-3aeb-8c27-e610eccc0f1c | -15.84853 | -57.38566 | 2024-09-26 05:44:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| dfb8fb0c-5083-35b0-addb-dd06c490efea | -15.84445 | -57.40987 | 2024-09-26 05:44:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 14.2 |
| d2e5280a-395f-32f9-b36e-9c7808e40b58 | -15.8422 | -57.42326 | 2024-09-26 05:44:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 6b07e5b9-51e9-38c4-9c34-fe83f1f974dc | -15.60343 | -56.94535 | 2024-09-26 05:44:00 | AQUA_M-M | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 594f2513-6868-3a9f-a9b3-d01b11830c4b | -15.60156 | -56.95678 | 2024-09-26 05:44:00 | AQUA_M-M | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| ecf34795-16cc-3fc9-b955-3e4e963459fa | -15.58546 | -56.93023 | 2024-09-26 05:44:00 | AQUA_M-M | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 1ab4a27e-faac-3aea-ab18-98e9c63b7448 | -15.57737 | -56.91727 | 2024-09-26 05:44:00 | AQUA_M-M | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 15e7f875-5743-3c5d-8963-ddd4c64f4fa2 | -15.57555 | -56.92834 | 2024-09-26 05:44:00 | AQUA_M-M | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 49e3af8b-b1f6-386a-826b-9e8d86948ba3 | -15.54588 | -56.92237 | 2024-09-26 05:44:00 | AQUA_M-M | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 537a0506-904b-30a8-994d-4ab42c0415e6 | -13.50115 | -61.23972 | 2024-09-26 05:44:00 | AQUA_M-M | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 35.9 |
| 1d136e79-9ecc-39fe-8b0a-69a636dd14f2 | -12.82562 | -62.69223 | 2024-09-26 05:44:00 | AQUA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 36.1 |
| 7b496775-0586-30d6-add3-a20f818a8600 | -22.34535 | -47.76424 | 2024-09-26 05:44:00 | AQUA_M-M | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 21.9 |
| e276a609-8406-347d-9968-ad0009200263 | -22.21209 | -47.56522 | 2024-09-26 05:44:00 | AQUA_M-M | CORUMBATAÍ | SÃO PAULO | Brasil | 3512704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 18.8 |
| dc3e70ff-3d95-3364-9aba-758ecf90d850 | -22.20817 | -47.5456 | 2024-09-26 05:44:00 | AQUA_M-M | CORUMBATAÍ | SÃO PAULO | Brasil | 3512704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 33.0 |
| c9e4aa78-8c13-3f1c-845f-952a7dfacbf5 | -22.2009 | -47.53938 | 2024-09-26 05:44:00 | AQUA_M-M | CORUMBATAÍ | SÃO PAULO | Brasil | 3512704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.9 |
| 1000853f-fa30-3e21-bc60-ee4b240b5428 | -22.19841 | -47.56352 | 2024-09-26 05:44:00 | AQUA_M-M | CORUMBATAÍ | SÃO PAULO | Brasil | 3512704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 29.1 |
| 1afe4a40-1bb2-3ad5-9bdd-2819de8fd923 | -21.95082 | -48.56033 | 2024-09-26 05:44:00 | AQUA_M-M | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 12.7 |
| ddc513f3-a046-3a5c-a052-ddc7c49aac24 | -21.94957 | -48.5549 | 2024-09-26 05:44:00 | AQUA_M-M | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 9.9 |
| e4459e89-989e-38bc-a8a1-b099381cc89c | -21.9473 | -48.57501 | 2024-09-26 05:44:00 | AQUA_M-M | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 13.8 |
| afc2d37b-7b03-3f36-acd9-9bd21b7b8491 | -21.93687 | -48.55382 | 2024-09-26 05:44:00 | AQUA_M-M | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 30.0 |
| 53c7a511-ff33-30ae-a7f3-f8e2d45d145a | -21.92548 | -48.55775 | 2024-09-26 05:44:00 | AQUA_M-M | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 8fe8873f-0848-3c2d-8f6d-8aeb1968c878 | -21.92424 | -48.55216 | 2024-09-26 05:44:00 | AQUA_M-M | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 2da6e683-70f1-3851-b592-cae6001fecfe | -21.92199 | -48.57249 | 2024-09-26 05:44:00 | AQUA_M-M | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 26.7 |
| fd07621d-9c2d-3869-ac61-944d0c8cbe82 | -21.39183 | -54.6589 | 2024-09-26 05:44:00 | AQUA_M-M | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a8c3dd7f-b1db-3864-9759-dabe513e7755 | -20.60273 | -51.49757 | 2024-09-26 05:44:00 | AQUA_M-M | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.9 |
| 34e2bf32-6dbb-392a-90b8-160b16b24e87 | -20.60119 | -51.50959 | 2024-09-26 05:44:00 | AQUA_M-M | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 101.4 |
| 7d9f08a0-8e84-3cd1-85be-6cffbaf857fa | -20.18099 | -43.5425 | 2024-09-26 05:44:00 | AQUA_M-M | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 89.7 |
| 48563dc6-2541-30e1-b419-d7bb39683a7a | -20.17958 | -43.54955 | 2024-09-26 05:44:00 | AQUA_M-M | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 133.9 |
| 5d9c9061-4d6d-36d5-b3c3-4509b2672c55 | -20.16324 | -43.53984 | 2024-09-26 05:44:00 | AQUA_M-M | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 307.6 |
| 21c811ee-632c-35dd-98d1-ffb10e54d6fb | -20.1617 | -43.54837 | 2024-09-26 05:44:00 | AQUA_M-M | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 305.0 |
| c33e445a-8738-34e2-9e9c-866db329ca0e | -20.15947 | -43.58235 | 2024-09-26 05:44:00 | AQUA_M-M | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 51.5 |
| b7892399-7e78-3367-ae64-c3195682f76b | -20.07083 | -55.52103 | 2024-09-26 05:44:00 | AQUA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 6e5d2e3f-749e-32eb-9bdd-655b12271f1f | -20.00326 | -55.48303 | 2024-09-26 05:44:00 | AQUA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 14.7 |
| c71166cd-bbea-316b-9e08-242997844eea | -20.0018 | -55.49253 | 2024-09-26 05:44:00 | AQUA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 13.2 |
| cd534d40-2c13-371f-96a0-496b235ef690 | -19.99434 | -55.48149 | 2024-09-26 05:44:00 | AQUA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 8.6 |
| cf9da321-0eaf-3edb-9f69-f982f083edfb | -19.99288 | -55.49094 | 2024-09-26 05:44:00 | AQUA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 84e135b9-2177-353c-a421-e653c92d041e | -19.99142 | -55.50048 | 2024-09-26 05:44:00 | AQUA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 5.2 |


[Clique aqui para ver as próximas entradas](README154.md)

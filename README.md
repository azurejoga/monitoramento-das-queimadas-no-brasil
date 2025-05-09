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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 56234be1-96bd-33b3-9ee7-04c53e733bb0 | -8.0889 | -43.1196 | 2025-05-09 00:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 70.5 |
| 36ca11ee-9b2d-3b8b-8209-a740d9e2ba1c | -8.07 | -43.1216 | 2025-05-09 00:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 119.3 |
| 5b03a5bd-25dc-30d5-b883-af38f53a523b | -13.3752 | -54.2538 | 2025-05-09 00:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 50.7 |
| cdda8225-9ad2-3a4d-90f7-58baec588d56 | -10.9733 | -44.441 | 2025-05-09 00:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 48.5 |
| 9d70ba1e-aecb-34c8-a4e7-9c8fbd194096 | -10.9733 | -44.441 | 2025-05-09 00:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 52.9 |
| c0a15419-84d7-33ac-a5a8-02f4c21d6321 | -8.0889 | -43.1196 | 2025-05-09 00:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 76.5 |
| d3362cac-dad6-373c-beae-f08bd0c1c461 | -8.07 | -43.1216 | 2025-05-09 00:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 98.8 |
| a505c474-d535-3f2d-b3c9-12266f4e0013 | -8.0889 | -43.1196 | 2025-05-09 00:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 62.4 |
| 2c80eb26-209b-3fa8-b441-04c1a4f65461 | -10.9733 | -44.441 | 2025-05-09 00:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 54.6 |
| 24bc889f-c347-3c04-9247-385c2733d6e7 | -8.07 | -43.1216 | 2025-05-09 00:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 104.1 |
| 75fbfd97-7cdb-31b3-88d0-e5ecd7efd3c1 | -8.07 | -43.1216 | 2025-05-09 00:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 105.6 |
| 5a2e0cfd-b091-3b93-a726-e014c010a4e4 | -10.9733 | -44.441 | 2025-05-09 00:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 51.4 |
| af6ab768-11fd-3551-bc17-4a3989cd777d | -8.0889 | -43.1196 | 2025-05-09 00:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 78.5 |
| 0ea145ce-5db8-316b-9591-a8fbdd1c5f2f | -8.07 | -43.1216 | 2025-05-09 00:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 90.5 |
| 9200cbce-62ae-3d30-a578-9b519ad51ede | -8.0889 | -43.1196 | 2025-05-09 00:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 78.2 |
| 6b905cc8-2ec5-3c57-b848-bca5abc9c47b | -8.078 | -43.1315 | 2025-05-09 00:44:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 3c2c277e-96f5-3357-b662-a93903ea166a | -6.6983 | -42.136501 | 2025-05-09 00:44:00 | METOP-C | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 302a741b-205c-35ab-b477-bec3a40a8caa | -24.9328 | -51.915501 | 2025-05-09 00:44:00 | METOP-C | SANTA MARIA DO OESTE | PARANÁ | Brasil | 4123857 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7439d9be-7118-3e27-b055-b06078a1a37d | -7.629 | -46.478699 | 2025-05-09 00:44:00 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 820f9cff-9b0d-3cd1-b78c-08fea6ad9eb5 | -13.0373 | -53.717899 | 2025-05-09 00:44:00 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c3e03ddb-42ee-3287-8ad3-316ad89d0c8c | -12.1754 | -54.237099 | 2025-05-09 00:44:00 | METOP-C | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b95211fb-51e0-38f2-9824-a98ee55550c3 | -20.063601 | -49.369099 | 2025-05-09 00:44:00 | METOP-C | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 73b142fe-86a0-3fe4-978a-03194066ddb8 | -21.7854 | -52.7547 | 2025-05-09 00:44:00 | METOP-C | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 5ec9f3a1-bbe3-3bc0-8208-141b4c430525 | -13.0395 | -53.728401 | 2025-05-09 00:44:00 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a27f80a0-6f5e-3ac7-8bd2-5e2d1ed4902b | -14.6491 | -45.1436 | 2025-05-09 00:44:00 | METOP-C | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6230daa1-f97e-35af-abcf-7d53638f26f8 | -14.2089 | -45.465698 | 2025-05-09 00:44:00 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e06aa6f8-029e-3bb4-b2e2-f549459fbf44 | -6.6173 | -48.0144 | 2025-05-09 00:44:00 | METOP-C | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0b0ce6d2-e228-34a3-b903-8f886abaece9 | -10.9816 | -44.438301 | 2025-05-09 00:44:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b97d318b-e763-3020-ba88-abac926db11a | -8.0878 | -43.1292 | 2025-05-09 00:44:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 616ce0db-3921-35e1-a8bc-b9e7e6fb3348 | -11.5721 | -47.612099 | 2025-05-09 00:44:00 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 07eb0dd9-17a1-350c-9171-519c413e3134 | -7.0776 | -44.396099 | 2025-05-09 00:44:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 26bb0612-fdc8-35d2-a7c9-bdad40159eff | -19.1579 | -47.821201 | 2025-05-09 00:44:00 | METOP-C | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 9b095b59-9e36-3f67-ba4f-7e68d2449406 | -5.168 | -45.1147 | 2025-05-09 00:44:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9e2dc641-e403-33c1-b190-9eedaed8d941 | -17.5289 | -52.127602 | 2025-05-09 00:44:00 | METOP-C | PEROLÂNDIA | GOIÁS | Brasil | 5216452 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| da1cf1bc-ff5e-3fd1-9efd-b237ead3a80c | -13.2508 | -48.406399 | 2025-05-09 00:44:00 | METOP-C | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c4c40fdc-e665-38c4-89d5-14b24b4224cb | -11.4022 | -52.9454 | 2025-05-09 00:44:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 797ac25a-3a1a-3fd8-8a45-c9e0926aa11e | -20.061899 | -49.361099 | 2025-05-09 00:44:00 | METOP-C | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 49a55411-4d26-3ece-8648-8ae735f4d4aa | -6.708 | -42.134102 | 2025-05-09 00:44:00 | METOP-C | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 2a4ef98f-c4f3-3119-ae2a-47d3f849dc65 | -14.2303 | -45.469101 | 2025-05-09 00:44:00 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 41e0e2a3-5c1f-371a-8e04-bfe41390f1de | -11.3924 | -52.947498 | 2025-05-09 00:44:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e38e93a5-e8c2-3b8e-9d07-5b72f11b9a4b | -14.643 | -45.118198 | 2025-05-09 00:44:00 | METOP-C | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| db3b5453-1d7a-3872-bbcb-630d3aebe39b | -10.9743 | -44.450901 | 2025-05-09 00:44:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4fc91380-25db-3bb0-8a00-d3af67b25138 | -17.526899 | -52.117699 | 2025-05-09 00:44:00 | METOP-C | PEROLÂNDIA | GOIÁS | Brasil | 5216452 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a789a55a-b0f5-31e8-8c20-3b8081259e38 | -14.2225 | -45.479698 | 2025-05-09 00:44:00 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| efc283d2-d24a-3c23-b2c7-cd7ca31a45ee | -10.6689 | -44.385601 | 2025-05-09 00:44:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 09855a5a-ab0e-3a59-9233-fcaca70a94eb | -13.3727 | -54.258099 | 2025-05-09 00:44:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6099867a-ad41-36d3-8585-fb3c871d4dcb | -13.0471 | -53.715801 | 2025-05-09 00:44:00 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 45dfe147-d8c4-3bf8-b871-915547940cb5 | -11.3904 | -52.9384 | 2025-05-09 00:44:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 05d328f7-8283-3831-9c57-74c2368ed883 | -6.7121 | -42.1507 | 2025-05-09 00:44:00 | METOP-C | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 60da437d-ef75-3131-85c6-642eda43660d | -14.645 | -45.126701 | 2025-05-09 00:44:00 | METOP-C | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 58f9eefd-e2a6-3197-80d0-02e12297282b | -13.6208 | -43.977798 | 2025-05-09 00:44:00 | METOP-C | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 34111d62-80fa-336f-ba0e-2f68bb9315a7 | -14.2108 | -45.4739 | 2025-05-09 00:44:00 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| fdb3210a-4b83-321e-9b33-2fa5806dbb65 | -10.6786 | -44.383202 | 2025-05-09 00:44:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b860c389-67c3-32a7-b6db-6df487123ae6 | -13.0493 | -53.726398 | 2025-05-09 00:44:00 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1e69ef35-a2f9-3996-9867-e267d45f3077 | -13.375 | -54.269699 | 2025-05-09 00:44:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 690a1b19-829b-3679-ae02-26274794e08f | -6.7024 | -42.153099 | 2025-05-09 00:44:00 | METOP-C | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d6630a55-393e-3874-8b0b-745cd731cb9f | -21.7831 | -52.742199 | 2025-05-09 00:44:00 | METOP-C | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 5cf451b5-acae-30c5-b8a4-eaa70781a8bf | -14.2069 | -45.457401 | 2025-05-09 00:44:00 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 950a66bc-40ef-3949-b50a-8d3916b5392a | -11.5624 | -47.614399 | 2025-05-09 00:44:00 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f0525737-d9b0-3a19-b09f-aff68f6f9881 | -13.2524 | -48.413399 | 2025-05-09 00:44:00 | METOP-C | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e3909a40-3355-319c-807b-d1f7091cf4dd | -11.564 | -47.621601 | 2025-05-09 00:44:00 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 114c32b2-cd70-3794-822a-6151e2749cf2 | -8.0844 | -43.115601 | 2025-05-09 00:44:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| fb9f7164-f72f-3476-834d-b21e74918284 | -13.3703 | -54.246601 | 2025-05-09 00:44:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9c8edb6e-3d4b-35b5-92f8-be7db4308210 | -11.4041 | -52.954399 | 2025-05-09 00:44:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| af6e5e8e-96b7-37d1-a844-1ff7cdfd383c | -14.2206 | -45.4715 | 2025-05-09 00:44:00 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 41823cee-9461-3490-ad82-e07f65d5c1cf | -8.0747 | -43.118 | 2025-05-09 00:44:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 4fcd2944-4777-3073-86f7-0ebed50b0741 | -14.647 | -45.135201 | 2025-05-09 00:44:00 | METOP-C | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 74b388d0-a236-3a10-8d05-fcdacd59cc46 | -8.0814 | -43.1451 | 2025-05-09 00:44:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| cc2f49f2-38af-39ed-ab80-6fe924272990 | -10.9719 | -44.440701 | 2025-05-09 00:44:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 482ea9ed-784e-3a26-b6dd-671bf21bd147 | -24.934999 | -51.928001 | 2025-05-09 00:44:00 | METOP-C | SANTA MARIA DO OESTE | PARANÁ | Brasil | 4123857 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2d03936c-c985-3cde-975b-036af2f5b0d9 | -5.1653 | -45.1036 | 2025-05-09 00:44:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b02325d6-bc00-3098-83df-0d3cccf71b69 | -19.1595 | -47.828499 | 2025-05-09 00:44:00 | METOP-C | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| c8120337-c30b-3473-a42b-298410ce67eb | -22.673201 | -49.8283 | 2025-05-09 00:47:00 | METOP-C | SÃO PEDRO DO TURVO | SÃO PAULO | Brasil | 3550506 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 200359ed-8c78-3ffa-9afe-b8b36da2dd3b | -8.07 | -43.1216 | 2025-05-09 00:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 85.3 |
| 9e525701-4c30-3e9f-8d8f-b6c7cc8c0592 | -8.0889 | -43.1196 | 2025-05-09 00:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 66.5 |
| 6f62ee53-29a2-395c-9918-d3501ef88d61 | -21.89223 | -47.19847 | 2025-05-09 00:50:00 | TERRA_M-M | SANTA CRUZ DAS PALMEIRAS | SÃO PAULO | Brasil | 3546306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 39111618-af46-3626-bb6e-b2f3ce5c7c20 | -24.9284 | -51.9071 | 2025-05-09 00:50:00 | TERRA_M-M | SANTA MARIA DO OESTE | PARANÁ | Brasil | 4123857 | 41 | 33 | nan | nan | nan | Mata Atlântica | 14.3 |
| f2ea3989-cf67-3bd7-bbb7-d44b48e77ae0 | -19.84546 | -54.22448 | 2025-05-09 00:50:00 | TERRA_M-M | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 17.9 |
| b4e36080-a70a-3a8d-82df-20e4621ab422 | -20.99976 | -48.84687 | 2025-05-09 00:50:00 | TERRA_M-M | EMBAÚBA | SÃO PAULO | Brasil | 3514957 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| e40e8a57-a921-3839-bbff-6184d4afb7c0 | -21.79013 | -52.74622 | 2025-05-09 00:50:00 | TERRA_M-M | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 22.3 |
| cf3c16bc-112e-351f-bc6e-b38fbdaad202 | -21.3985 | -48.53038 | 2025-05-09 00:50:00 | TERRA_M-M | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 359669d9-bc15-3638-85b9-bf7f642420e6 | -24.93 | -51.92196 | 2025-05-09 00:50:00 | TERRA_M-M | SANTA MARIA DO OESTE | PARANÁ | Brasil | 4123857 | 41 | 33 | nan | nan | nan | Mata Atlântica | 52.1 |
| 8090992e-989d-3111-b24c-d84c7a6faff2 | -20.06626 | -49.36049 | 2025-05-09 00:50:00 | TERRA_M-M | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.4 |
| e3522563-b731-39e7-a53c-61ef500de35e | -19.16164 | -47.81724 | 2025-05-09 00:50:00 | TERRA_M-M | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 4197c644-1388-37cc-8207-897e8dcb7708 | -22.67176 | -49.82699 | 2025-05-09 00:50:00 | TERRA_M-M | SÃO PEDRO DO TURVO | SÃO PAULO | Brasil | 3550506 | 35 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 7dc2e3ef-0f3f-3fef-9f24-29b85935aacf | -13.04584 | -53.71703 | 2025-05-09 00:52:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 3c7fc7f1-eb27-3a4e-8e42-56bfbf63feac | -17.52482 | -52.11492 | 2025-05-09 00:52:00 | TERRA_M-M | PEROLÂNDIA | GOIÁS | Brasil | 5216452 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| b8d8c2ea-f9c2-388d-8f21-2b8f9cf7e546 | -10.668 | -44.37509 | 2025-05-09 00:52:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 50.4 |
| 7b7c1310-3eae-3397-9091-036c5468905d | -13.61928 | -43.98517 | 2025-05-09 00:52:00 | TERRA_M-M | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 788315de-4062-3d86-9792-dfd182216574 | -13.05764 | -53.72813 | 2025-05-09 00:52:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 812e9d9f-a0eb-3110-8671-b53809ab9cdc | -17.53462 | -52.11342 | 2025-05-09 00:52:00 | TERRA_M-M | PEROLÂNDIA | GOIÁS | Brasil | 5216452 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 2a06fb1e-81a3-3fa3-8216-0e5d637a7879 | -13.37031 | -54.25568 | 2025-05-09 00:52:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 32.7 |
| 5a79d4aa-2f3e-3274-a78e-a14e269623e1 | -13.37204 | -54.26943 | 2025-05-09 00:52:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 17.0 |
| c29b5424-9f59-3515-8c33-f24d5d07eac2 | -13.05029 | -53.73473 | 2025-05-09 00:52:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 21710b4c-421c-34c9-9c24-7430d4965aa5 | -10.96693 | -44.43835 | 2025-05-09 00:52:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 18.6 |
| d1aa54d6-3d6d-3d66-9864-79ca9c4fa3f8 | -14.64527 | -45.11931 | 2025-05-09 00:52:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 49052b87-d9ae-36b4-858f-3bdad43c1b43 | -11.91183 | -54.40639 | 2025-05-09 00:52:00 | TERRA_M-M | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 79b67ebf-fee4-349f-ac00-f27991142fce | -13.0487 | -53.72237 | 2025-05-09 00:52:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 39.7 |
| b0fb5b49-65b6-3b74-8fe3-9592f25c8485 | -11.3855 | -52.94901 | 2025-05-09 00:52:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| d7dcdcf0-50a2-307a-8c06-283f01b8e578 | -11.56279 | -47.60958 | 2025-05-09 00:52:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |


[Clique aqui para ver as próximas entradas](README2.md)

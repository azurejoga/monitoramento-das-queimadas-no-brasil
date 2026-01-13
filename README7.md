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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 73d19904-9ffa-390f-9863-8191bdfd9fa5 | -6.98227 | -38.10958 | 2026-01-13 04:21:00 | NOAA-20 | SÃO JOSÉ DA LAGOA TAPADA | PARAÍBA | Brasil | 2514206 | 25 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 45314caf-0a21-3173-b0dd-14ae6f3df4a7 | -5.92458 | -43.32909 | 2026-01-13 04:21:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5f7b35b6-fb60-3f40-9748-d69044d8f2df | -4.91784 | -43.42521 | 2026-01-13 04:21:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 21785d76-8704-3e23-8db0-29ec33541073 | -5.09613 | -43.23495 | 2026-01-13 04:21:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 30.4 |
| 8e600b87-8701-339d-aea0-8139e6a055a5 | -3.13577 | -42.20932 | 2026-01-13 04:21:00 | NOAA-20 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3db41143-cfaf-3408-99a3-6ab09a0b67f4 | -4.35974 | -48.73358 | 2026-01-13 04:21:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 05caaa3f-02cc-3995-9f20-4456157e87f7 | -5.10115 | -43.22475 | 2026-01-13 04:21:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 32.8 |
| 086bc93f-d2f0-3b46-bd2b-8021ed438ebf | -2.62562 | -45.7314 | 2026-01-13 04:21:00 | NOAA-20 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3536395a-b3f2-39c7-bef2-fa612f1f4066 | -2.92348 | -40.59806 | 2026-01-13 04:21:00 | NOAA-20 | CAMOCIM | CEARÁ | Brasil | 2302602 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ed5944aa-54ff-35a0-a739-80e6300e8267 | -2.8678 | -45.2418 | 2026-01-13 04:21:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 96c789ce-62a2-381a-b2ea-b9fb26047342 | -0.08923 | -51.28292 | 2026-01-13 04:21:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 4.5 |
| dcdb2cab-2648-3793-9ab4-aceee1585020 | -4.73856 | -40.82867 | 2026-01-13 04:21:00 | NOAA-20 | ARARENDÁ | CEARÁ | Brasil | 2301257 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 704d0549-53ee-32c2-983f-1c3a5f957d93 | -5.32104 | -43.55976 | 2026-01-13 04:21:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c8cb7af8-9fb0-37b6-b2f6-0fe17e3448f2 | -3.60518 | -41.87178 | 2026-01-13 04:21:00 | NOAA-20 | CARAÚBAS DO PIAUÍ | PIAUÍ | Brasil | 2202539 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 78c913ba-4d68-32fb-a01c-6db341985a08 | -3.3044 | -42.54134 | 2026-01-13 04:21:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9fc3459b-13a8-3f8f-8a4e-9125c66531f0 | -3.38561 | -42.11349 | 2026-01-13 04:21:00 | NOAA-20 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| a0c8d5ab-0d64-3507-8b17-80e78d06a0d4 | -5.10171 | -43.22117 | 2026-01-13 04:21:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6fb4d262-3655-34fe-811e-dc234fb712a8 | -3.29706 | -42.5439 | 2026-01-13 04:21:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 71ec6b63-6291-3b9c-b96f-1d2e2397a716 | -0.09007 | -51.2775 | 2026-01-13 04:21:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e35c106d-3afd-3f97-837d-c40d840d0e7d | 0.05612 | -49.92757 | 2026-01-13 04:21:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b0735507-b35f-3a9b-a464-bd763eb80721 | -5.10788 | -43.22577 | 2026-01-13 04:21:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| a4cdc61b-a287-36e8-b864-a52091c4b1e9 | -5.15948 | -36.58662 | 2026-01-13 04:21:00 | NOAA-20 | MACAU | RIO GRANDE DO NORTE | Brasil | 2407203 | 24 | 33 | nan | nan | nan | Caatinga | 2.7 |
| a51d5fdb-4832-37a0-a628-64ea423f5559 | -1.94885 | -46.48965 | 2026-01-13 04:21:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| b828d9c1-4de1-39e8-bda8-c3ac3f984c7b | -3.55069 | -43.65231 | 2026-01-13 04:21:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 79c0c193-3321-3ad1-82e0-dd28c777afc5 | -3.28972 | -42.54647 | 2026-01-13 04:21:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9ad2cbfb-517f-34ac-a1d8-70762c3753c6 | -1.01576 | -48.95998 | 2026-01-13 04:21:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 310c81b2-c6b3-3329-af6a-2a5e7f51ce3b | -0.51585 | -49.12616 | 2026-01-13 04:21:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 89fb8054-f770-3957-8298-1dc55716c04d | -8.37471 | -35.39629 | 2026-01-13 04:23:00 | NOAA-20 | AMARAJI | PERNAMBUCO | Brasil | 2600906 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 1218284c-4fe1-378d-844a-b07c6d549f8c | -11.2347 | -54.00703 | 2026-01-13 04:23:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d3bf899f-2f5b-3efb-b1bd-f04bb72b165f | -8.37525 | -35.39235 | 2026-01-13 04:23:00 | NOAA-20 | AMARAJI | PERNAMBUCO | Brasil | 2600906 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 9a945efb-70ae-35d2-9d5b-48d9e446ed83 | -17.35808 | -44.90254 | 2026-01-13 04:23:00 | NOAA-20 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 220d223f-8fde-3780-9ef1-88b4448c6a36 | -18.61905 | -46.97448 | 2026-01-13 04:23:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 65ba0c89-cbf2-3e5a-b889-7b9ef4370506 | -8.53066 | -44.3304 | 2026-01-13 04:23:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 220c65f4-4e63-389d-b086-c0a6b35d10d7 | -8.37333 | -35.3917 | 2026-01-13 04:23:00 | NOAA-20 | AMARAJI | PERNAMBUCO | Brasil | 2600906 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 9bbc5754-7a7c-3c84-bf6e-ba45e1ca49b3 | -7.58058 | -37.75247 | 2026-01-13 04:23:00 | NOAA-20 | JURU | PARAÍBA | Brasil | 2508000 | 25 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7b7d693c-f029-3726-aa29-eeb576d3517c | -8.57382 | -39.5751 | 2026-01-13 04:23:00 | NOAA-20 | OROCÓ | PERNAMBUCO | Brasil | 2609808 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| bff4cf22-241b-35b3-a067-43923efdbd22 | -17.88548 | -39.768 | 2026-01-13 04:23:00 | NOAA-20 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f62092e6-9e00-3bfe-8d6b-f2bb1e3455fb | -9.78222 | -42.03641 | 2026-01-13 04:23:00 | NOAA-20 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| bef41316-d4e5-3d97-882a-ca00aba65a8e | -19.2395 | -48.67502 | 2026-01-13 04:23:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f966d969-f7e6-38f3-b323-0724005023ab | -9.78591 | -42.03697 | 2026-01-13 04:23:00 | NOAA-20 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 3dc5fd70-979d-3ad8-bfb2-182cda830eee | -11.17285 | -54.1461 | 2026-01-13 04:23:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f26cc594-059b-3405-b9d8-2eace92ce290 | -11.16792 | -54.14505 | 2026-01-13 04:23:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3077bc07-d553-3a39-b1c8-6c59cff4dc29 | -8.37282 | -35.39564 | 2026-01-13 04:23:00 | NOAA-20 | AMARAJI | PERNAMBUCO | Brasil | 2600906 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| c36b28cf-bc36-36b5-b1e0-136874b4eb96 | -17.89024 | -39.76862 | 2026-01-13 04:23:00 | NOAA-20 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| f5e630eb-09ea-34f8-88b3-5366dff2319b | -20.84441 | -51.739 | 2026-01-13 04:25:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 1e4bee1a-77d5-3f5a-a7aa-730bf53439c5 | -21.85553 | -43.07893 | 2026-01-13 04:25:00 | NOAA-20 | MAR DE ESPANHA | MINAS GERAIS | Brasil | 3139805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| ee4bf141-04d5-34de-ba3f-c175af145929 | -16.55916 | -43.79014 | 2026-01-13 04:25:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0f863cf4-cfaf-3d4f-80db-9f384e97a914 | -21.85913 | -43.08325 | 2026-01-13 04:25:00 | NOAA-20 | MAR DE ESPANHA | MINAS GERAIS | Brasil | 3139805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 47.5 |
| 3a4a86dd-7340-3bc7-9d5b-de2ff4ca15f6 | -20.84078 | -51.73826 | 2026-01-13 04:25:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 6605a35c-b182-37ee-871c-5ed56ba75d34 | -21.85876 | -43.08355 | 2026-01-13 04:25:00 | NOAA-20 | MAR DE ESPANHA | MINAS GERAIS | Brasil | 3139805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 47.8 |
| 281d14d1-9046-3079-b0ec-b2b6c313d713 | -22.6779 | -43.71074 | 2026-01-13 04:25:00 | NOAA-20 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| ad9a87bd-ff0c-37ee-a998-3c86d42dc7b0 | -21.85925 | -43.07976 | 2026-01-13 04:25:00 | NOAA-20 | MAR DE ESPANHA | MINAS GERAIS | Brasil | 3139805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| 9a058e2b-89f0-3417-98b4-3a1169e9cfbc | -21.56402 | -43.66339 | 2026-01-13 04:25:00 | NOAA-20 | SANTOS DUMONT | MINAS GERAIS | Brasil | 3160702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 746d8618-3d49-3350-af75-5656ffee4d66 | -22.67659 | -43.72115 | 2026-01-13 04:25:00 | NOAA-20 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 6ab3e10a-a8c7-38fc-bcf6-191c40745b03 | -21.85506 | -43.08275 | 2026-01-13 04:25:00 | NOAA-20 | MAR DE ESPANHA | MINAS GERAIS | Brasil | 3139805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 47.5 |
| 9251001b-ed1b-344f-abf1-87f06905c57b | -21.85959 | -43.07946 | 2026-01-13 04:25:00 | NOAA-20 | MAR DE ESPANHA | MINAS GERAIS | Brasil | 3139805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| 62c5b701-cb4f-3e48-bc00-b77616ebd3c2 | -21.85519 | -43.07923 | 2026-01-13 04:25:00 | NOAA-20 | MAR DE ESPANHA | MINAS GERAIS | Brasil | 3139805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| e4615e89-d3fc-309f-9068-f0b06f01674c | -16.0528 | -47.21659 | 2026-01-13 04:25:00 | NOAA-20 | CABECEIRA GRANDE | MINAS GERAIS | Brasil | 3109451 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c3e78405-fec3-3021-9ca4-71b156539b1d | -21.56489 | -43.6603 | 2026-01-13 04:25:00 | NOAA-20 | SANTOS DUMONT | MINAS GERAIS | Brasil | 3160702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 5885d2f8-3ba2-3f94-b7dc-8d9b4a55a016 | -21.8547 | -43.08305 | 2026-01-13 04:25:00 | NOAA-20 | MAR DE ESPANHA | MINAS GERAIS | Brasil | 3139805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 47.8 |
| af00f1ba-928c-3e9e-8e03-fedd1ab01172 | -22.68052 | -43.72188 | 2026-01-13 04:25:00 | NOAA-20 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 97e2348a-bf00-3660-a681-d54329e7833d | -29.61458 | -50.8966 | 2026-01-13 04:27:00 | NOAA-20 | NOVA HARTZ | RIO GRANDE DO SUL | Brasil | 4313060 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| ec3b5886-9e8d-36ff-8474-d8a8c7519631 | -29.88289 | -51.21428 | 2026-01-13 04:27:00 | NOAA-20 | CANOAS | RIO GRANDE DO SUL | Brasil | 4304606 | 43 | 33 | nan | nan | nan | Pampa | 0.5 |
| de0a7e27-e7da-3e40-b831-44e7cd8f3ec8 | -5.0992 | -43.2211 | 2026-01-13 04:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 177.7 |
| 878b52b0-0610-340c-9cdc-d21e14abea9a | -5.099 | -43.2444 | 2026-01-13 04:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 109.4 |
| 784f816e-b1a3-37f2-a32f-db6f7b91ca63 | -5.099 | -43.2444 | 2026-01-13 04:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 118.1 |
| c884f774-32b5-3fec-8436-b307629067ce | -5.0992 | -43.2211 | 2026-01-13 04:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 157.9 |
| 2d25ff95-d6e2-35de-82f8-64fb800a3ffa | -5.0992 | -43.2211 | 2026-01-13 04:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 146.2 |
| c141c4b2-d56b-3d7d-8393-066ea10cb4e9 | -5.099 | -43.2444 | 2026-01-13 04:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 111.5 |
| 94d3778e-6374-3dde-8a0c-51e47394d594 | -5.0992 | -43.2211 | 2026-01-13 05:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 152.3 |
| 23bc72d0-7f13-3c6b-9f98-6b400d513cab | -5.099 | -43.2444 | 2026-01-13 05:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 7f5b6b2a-23a8-39ab-8f02-38ad51648fca | -5.0992 | -43.2211 | 2026-01-13 05:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 151.0 |
| a5001f78-5f27-3a72-907f-dce71b361808 | -5.099 | -43.2444 | 2026-01-13 05:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 72987d6b-440e-325d-95e0-283b17a5aa4f | -1.42967 | -53.37826 | 2026-01-13 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 98d97097-1862-39f7-b6dd-c027e222af9a | -2.78254 | -54.16903 | 2026-01-13 05:10:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c44e5c7e-af27-3b97-8a49-7d163388a227 | -0.04894 | -51.65548 | 2026-01-13 05:10:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cd8a9670-8137-35cf-8e91-a825d1a918e0 | -2.46328 | -48.22736 | 2026-01-13 05:10:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3ee62ca3-a739-3175-92c9-0a599a732151 | -1.28825 | -53.68643 | 2026-01-13 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2b12bb59-463c-3614-8715-ae1758237d90 | -1.85461 | -54.02463 | 2026-01-13 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| eee6d2c1-79a7-33a1-b65a-2bfc53f04e6f | -0.09124 | -51.27889 | 2026-01-13 05:10:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8aa279d6-773c-33a7-8e27-2f6b3aa747dc | -1.95241 | -53.46515 | 2026-01-13 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| aea0e475-c9fa-31fc-9104-075f027ecbf5 | -1.98219 | -53.14304 | 2026-01-13 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 290bf52d-fd83-3389-a212-9cf5364a4b69 | -2.15045 | -54.39513 | 2026-01-13 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| caa49fc0-aec0-345f-b630-94e83ff27194 | -2.87572 | -45.22334 | 2026-01-13 05:10:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5d0c2413-d687-385c-8036-2f05cea2e9c5 | -1.29176 | -53.68703 | 2026-01-13 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 04ec21f4-8cf3-3ecc-9cd8-c87bc4be9d7f | -1.83816 | -54.16667 | 2026-01-13 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7f814207-a76e-3128-9f9c-76d2f558b09a | -2.88711 | -54.17233 | 2026-01-13 05:10:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| adf7afed-53e6-367f-885e-e46bd2d3abb7 | -1.93065 | -53.47174 | 2026-01-13 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4051d5cb-99e7-30eb-ae83-085e83eca6b9 | -3.24841 | -52.917 | 2026-01-13 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e12c1847-20fd-3d05-8855-782cb34bcf49 | -4.09912 | -54.42464 | 2026-01-13 05:10:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 73ecd9f3-2e26-3064-8fc6-9a17a9598406 | 0.62102 | -50.77029 | 2026-01-13 05:10:00 | NOAA-21 | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 379f4779-f333-3061-8646-458c6ab506c7 | -1.93129 | -53.46766 | 2026-01-13 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2780211d-174e-3357-9676-16d7a6b18079 | -1.61494 | -54.14204 | 2026-01-13 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8ebcf723-f777-3cfd-8363-6455232e1bd3 | -1.85583 | -54.02773 | 2026-01-13 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| dcbd47ad-6416-39af-8db8-7c20d2f656dc | -1.29527 | -53.68764 | 2026-01-13 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7ec7b40d-a4a3-3a87-9408-2cc889270312 | -1.91991 | -53.47009 | 2026-01-13 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dd53bd86-53e1-33ce-8937-a48add7753b8 | 3.43504 | -60.6172 | 2026-01-13 05:10:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 71460167-473a-3c2e-9273-5854e2ee00ee | -2.87501 | -45.22827 | 2026-01-13 05:10:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 20830982-d9dc-3ff6-9cc3-16e6e4d42eec | -0.11103 | -51.43294 | 2026-01-13 05:10:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 09359fd5-666c-391e-b60e-21f4ed30e2b3 | -1.98286 | -53.1388 | 2026-01-13 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |


[Clique aqui para ver as próximas entradas](README8.md)

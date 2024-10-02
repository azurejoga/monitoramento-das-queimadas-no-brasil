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

## Dados Diários - Página 167

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b2e29e30-3545-3708-9a50-a159c595a050 | -9.00049 | -67.35078 | 2024-10-02 05:33:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 70aaa972-38da-3acd-ace4-9b97c8f5b392 | -8.99979 | -67.35493 | 2024-10-02 05:33:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1ee66334-3e04-3ef6-aa13-2230bd723567 | -8.99953 | -67.4454 | 2024-10-02 05:33:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 552460cb-c1ee-354a-adde-355716b386f5 | -8.99883 | -67.4496 | 2024-10-02 05:33:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 85d4ed3a-512c-3b64-8f66-c68a7508e16b | -8.99806 | -67.81718 | 2024-10-02 05:33:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1ec7aa01-f01e-3e89-872b-cb2b7955303e | -8.99619 | -67.35431 | 2024-10-02 05:33:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5e004c60-b801-364c-baab-a18ec0bc2039 | -8.9926 | -67.3537 | 2024-10-02 05:33:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e14a9891-7f62-3d95-8b2a-7824d161053b | -8.989 | -67.35309 | 2024-10-02 05:33:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5b853575-2b56-35a8-bb4b-8fb31053c1bf | -8.98859 | -67.42191 | 2024-10-02 05:33:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 30532a08-e434-3d01-af1a-97ac648bd647 | -9.41333 | -68.24293 | 2024-10-02 05:33:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2e538cda-77b3-3a32-8aa6-478b754ddd71 | -9.40648 | -68.26053 | 2024-10-02 05:33:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4fd144d9-03d6-3ac0-8566-1bbdbfaef544 | -9.39868 | -68.30661 | 2024-10-02 05:33:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 3b0ef28b-3fee-33c7-aff1-c79bb504dd5e | -9.39145 | -68.25793 | 2024-10-02 05:33:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bf10b8b7-c6cb-3255-b1ee-186930e34bd8 | -9.39067 | -68.26252 | 2024-10-02 05:33:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5440017d-f22b-3241-a030-8eb53b5cfdaa | -9.38769 | -68.2573 | 2024-10-02 05:33:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ddb0be74-e215-32bd-a214-a1010e33d69a | -9.37732 | -68.34091 | 2024-10-02 05:33:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 4.1 |
| dceaec6d-a341-39d3-9a50-79d96353b65c | -9.37653 | -68.34554 | 2024-10-02 05:33:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3e690def-29e5-335a-9280-566c1316d4fa | -9.37354 | -68.34026 | 2024-10-02 05:33:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 6da3d702-bd0d-3221-842f-6e05fe5ab7d0 | -9.31555 | -68.81882 | 2024-10-02 05:33:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9a32cc66-f10b-3e03-aeaa-6ffbf757be9a | -6.38488 | -52.71128 | 2024-10-02 05:33:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fcf5808d-ce4a-311c-8607-539cd1a37782 | -6.37888 | -52.7105 | 2024-10-02 05:33:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2cfed6e1-f49d-35ca-891c-660cb9434e0b | -11.07553 | -52.52499 | 2024-10-02 05:33:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d0cb1b0d-ce69-316d-b1cb-92c7149a979b | -11.07495 | -52.52349 | 2024-10-02 05:33:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ff31e9da-88d4-3f43-ad1d-6334810e35c5 | -11.06909 | -52.52417 | 2024-10-02 05:33:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7ae7a809-dccd-36ac-965c-e3aaf327b081 | -11.06851 | -52.5227 | 2024-10-02 05:33:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 24925627-6e12-3adf-aa3a-d67f193085e7 | -6.58 | -52.9265 | 2024-10-02 05:33:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 90c5d314-2256-3534-9202-3f0e1a825fe9 | -6.5794 | -52.93085 | 2024-10-02 05:33:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 41d45684-6a1f-3edd-9141-046d22016159 | -6.57749 | -52.92643 | 2024-10-02 05:33:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 41b0f1cf-ba49-3c44-be46-4d89a488b286 | -6.57692 | -52.93081 | 2024-10-02 05:33:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ca5de5f0-5dbd-3bee-9fe3-02d7f11228e1 | -6.57406 | -52.92579 | 2024-10-02 05:33:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c1b9153f-740d-3301-aeaa-2712034d0730 | -6.57345 | -52.93018 | 2024-10-02 05:33:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8677c2d4-ac6b-3ce7-a098-4619a3ea1df9 | -6.57097 | -52.9301 | 2024-10-02 05:33:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e1861c77-73a1-379a-a156-cb9720f4e010 | -6.2333 | -53.33462 | 2024-10-02 05:33:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 82f670f1-13f1-3ad6-8e9d-b64d1c789737 | -6.23277 | -53.33855 | 2024-10-02 05:33:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 01f9f2d2-4de0-345f-8967-3002b18bb70f | -6.07503 | -53.35968 | 2024-10-02 05:33:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a617a957-2ddf-3ea9-8650-ce0b0777ffc1 | -6.07446 | -53.36371 | 2024-10-02 05:33:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b8319faa-d1eb-32f6-a077-060072baab33 | -5.85035 | -53.56049 | 2024-10-02 05:33:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2cf99589-bf0a-3dab-897e-d54abeff840f | -5.84799 | -53.55922 | 2024-10-02 05:33:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 210e5283-5430-3c74-9357-aec2fb57d465 | -5.84748 | -53.56304 | 2024-10-02 05:33:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fc23406f-ecde-336c-a3b6-a0186d6143e3 | -10.62012 | -54.0637 | 2024-10-02 05:33:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 207ba71b-e51a-3a73-b9ab-3a8bb66230f5 | -10.6143 | -54.06295 | 2024-10-02 05:33:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a0fa1aad-0a63-361f-bc2a-2e90366f7283 | -11.43418 | -54.30959 | 2024-10-02 05:33:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 657a612d-2b5c-3647-9cb3-de28bfbf446a | -11.42839 | -54.30882 | 2024-10-02 05:33:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b596b198-7791-349b-b931-e386f51d2a5d | -11.38083 | -55.11625 | 2024-10-02 05:33:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8471c249-331f-3808-82c3-ddd17d7a3b32 | -11.38037 | -55.11989 | 2024-10-02 05:33:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9a3f24a9-8e93-3786-af3e-a16976851b45 | -11.37992 | -55.12347 | 2024-10-02 05:33:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e2f577ae-692c-34ff-a211-2b5fd6707549 | -11.37442 | -55.12288 | 2024-10-02 05:33:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a51c1728-1dfa-368f-aff8-564b7babdd70 | -11.37398 | -55.12642 | 2024-10-02 05:33:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8dbeed0b-5cc5-3041-9204-d3f9de8ad663 | -11.36547 | -55.19411 | 2024-10-02 05:33:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7f40003e-62a0-36db-81ea-ff4e65de6ddf | -11.36502 | -55.19772 | 2024-10-02 05:33:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 57b25273-7b76-30e6-a1bd-2e1de2a291c2 | -11.35954 | -55.19718 | 2024-10-02 05:33:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4ce1b065-fbd5-34e1-91c7-5a766069d3f4 | -11.35909 | -55.20076 | 2024-10-02 05:33:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1f9a0e43-b8b1-3558-a62d-ef6cb179727a | -11.29799 | -54.3136 | 2024-10-02 05:33:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ab0f05d4-9c24-3edb-88b3-b6e21469d0f9 | -11.29784 | -54.31094 | 2024-10-02 05:33:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 503ab5ea-f1b3-3ff2-8ba7-75a9df324992 | -11.29732 | -54.31509 | 2024-10-02 05:33:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b40bca03-3c49-3ebe-be0c-3201cc7220a1 | -10.62651 | -55.88031 | 2024-10-02 05:33:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3b518d62-cfac-35c0-898e-1e1ab3f43216 | -10.62611 | -55.88337 | 2024-10-02 05:33:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f0991386-ebb2-3122-9a28-15a51ce7099f | -10.62572 | -55.88643 | 2024-10-02 05:33:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 65a65a03-b9df-3065-aaed-6307dafc5ef3 | -10.62137 | -55.87949 | 2024-10-02 05:33:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1c16fcdd-f0f6-346c-81bb-ab0916e1338d | -10.62098 | -55.88251 | 2024-10-02 05:33:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 30cb8a6f-6a38-324c-954b-878c561cb447 | -10.62059 | -55.88551 | 2024-10-02 05:33:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 84c78391-7bbd-3089-a099-c9326e511570 | -10.61584 | -55.88168 | 2024-10-02 05:33:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f2959854-2052-3a34-bbf2-be99b6c90619 | -10.61545 | -55.88471 | 2024-10-02 05:33:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c6778c51-5656-3d0e-b148-5a4f19495b41 | -10.00105 | -55.39051 | 2024-10-02 05:33:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 50227842-9d28-3467-838d-7d764f1de28a | -10.00056 | -55.38986 | 2024-10-02 05:33:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9f91263a-2be1-3bbf-8c82-7eae96474da6 | -8.2549 | -71.15034 | 2024-10-02 05:33:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 5cbc9f8d-26cf-323e-b9e2-31fc81a472cf | -8.25575 | -71.14551 | 2024-10-02 05:33:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 5.8 |
| ad3cb11b-099d-3e21-b5df-1a68ce1a4b90 | -8.25708 | -71.11104 | 2024-10-02 05:33:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 939474d4-ca2e-3f30-a88a-20d1a22f33ce | -8.74557 | -69.65733 | 2024-10-02 05:33:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0c5313d9-313b-36f6-a726-1dca7baf134b | -8.75506 | -68.9184 | 2024-10-02 05:33:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 845978dc-1806-3a28-be4f-83a9a7007fbd | -8.75594 | -68.91328 | 2024-10-02 05:33:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6218e7ca-f0d5-3a4c-b9d7-44384cb38b45 | -8.75988 | -68.91398 | 2024-10-02 05:33:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| dcfc687a-a3ca-303a-897c-f91419d049bb | -7.95515 | -70.15453 | 2024-10-02 05:33:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 61622b08-3f2b-3873-b73f-459878ecd38d | -8.62238 | -70.02096 | 2024-10-02 05:33:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 73d9f0a5-610a-30b8-ae8b-3ee46678311f | -8.62662 | -70.02177 | 2024-10-02 05:33:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5105fabb-59e1-3f5a-9d6c-d0a39481ba2e | -8.62729 | -70.01781 | 2024-10-02 05:33:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b2967a6c-d454-33b8-a305-0c20cef9a79d | -8.63159 | -70.29116 | 2024-10-02 05:33:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 31ccdb92-2196-3070-b49a-b35f55011430 | -9.02257 | -69.023 | 2024-10-02 05:33:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 886ec279-0242-381d-9470-387b0e2a372d | -9.02414 | -69.02108 | 2024-10-02 05:33:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8675d5c0-e00d-3089-8b5d-cd0bb038c0b9 | -9.07927 | -69.98754 | 2024-10-02 05:33:00 | NOAA-20 | SANTA ROSA DO PURUS | ACRE | Brasil | 1200435 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f04248c9-6713-3aed-9efd-1d12be23316e | -9.07961 | -69.98713 | 2024-10-02 05:33:00 | NOAA-20 | SANTA ROSA DO PURUS | ACRE | Brasil | 1200435 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bdda06e4-da85-3a62-8f4d-c9312ba480ce | -7.45272 | -70.00044 | 2024-10-02 05:33:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d2d83395-4abf-36d2-a0af-988689496b42 | -10.3315 | -57.50875 | 2024-10-02 05:33:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 82c8fd62-c0d1-3aee-9287-bb1ceed95cda | -10.28036 | -58.20566 | 2024-10-02 05:33:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 03ab03b8-fbe6-30f2-9e6a-78a4e48c5eca | -10.13053 | -56.75939 | 2024-10-02 05:33:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 65f32069-fc78-31de-8ce7-bebcd84b6d90 | -10.13022 | -56.76864 | 2024-10-02 05:33:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c5724a58-ef08-3496-9a3a-15ec548de0c6 | -10.12985 | -56.76466 | 2024-10-02 05:33:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9719cea4-0b6c-36c7-8668-92ebb8438e9d | -9.98373 | -57.88797 | 2024-10-02 05:33:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 37a85aee-18e1-3314-a2ff-0a7fa6ebb1fa | -9.98197 | -57.89013 | 2024-10-02 05:33:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2beb6b72-c7f0-3233-8146-dc355131850b | -9.75921 | -57.79201 | 2024-10-02 05:33:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9e44084a-b695-31bd-875f-04816f703f42 | -6.98014 | -59.09874 | 2024-10-02 05:33:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a0e04da4-fb45-34fb-b8fb-45d4d21d24ab | -6.97621 | -59.09815 | 2024-10-02 05:33:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e5f09286-f555-36d7-8afe-89bcdd1e0666 | -6.97547 | -59.10314 | 2024-10-02 05:33:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1493680b-d4eb-3ed7-99cc-12f51a2737b2 | -6.97228 | -59.09756 | 2024-10-02 05:33:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b30df20f-cc69-3a22-9bb0-6726a6cf960b | -6.97154 | -59.10255 | 2024-10-02 05:33:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 407efca2-e05a-32f3-9f0f-6c7fc1f28679 | -9.31318 | -58.91311 | 2024-10-02 05:33:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 598ff2df-8662-3ee7-b7a8-c57d452034f6 | -9.1993 | -58.20866 | 2024-10-02 05:33:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2611ab34-6dd7-3d7f-837e-8fe6d4889f23 | -9.19613 | -58.19979 | 2024-10-02 05:33:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ee0c59b9-63c8-3452-8986-14b7017fbe9d | -9.19556 | -58.2039 | 2024-10-02 05:33:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d3714b83-8df4-3387-af7d-451448fa6665 | -9.195 | -58.20801 | 2024-10-02 05:33:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README168.md)

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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f291f15b-d5f8-31ad-a0e4-a9af9658ec21 | -10.51549 | -47.58247 | 2025-06-25 00:41:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 1777fbf4-854b-3418-850d-3a15eb3d2820 | -8.06739 | -43.10619 | 2025-06-25 00:41:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 21.0 |
| dd3b24a8-87b4-34f6-8f45-8fe0f33da67e | -7.20967 | -43.09003 | 2025-06-25 00:41:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 34.3 |
| dfdba310-9662-39cf-861b-abd9be810b2e | -6.17828 | -48.06796 | 2025-06-25 00:41:00 | TERRA_M-M | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 212.8 |
| b7184377-2ced-3f81-8f50-e1fd08e53011 | -8.58369 | -47.67549 | 2025-06-25 00:41:00 | TERRA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 68fc60f6-b7a8-3dcc-b5ec-bc0319842cc1 | -6.18466 | -48.0514 | 2025-06-25 00:41:00 | TERRA_M-M | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| d42cba94-3aac-3d3a-8499-7c0f9e2220f0 | -12.79558 | -48.73762 | 2025-06-25 00:41:00 | TERRA_M-M | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 28.7 |
| aa97065e-3d89-34f0-a9e7-7ffe323893d3 | -8.07026 | -43.12463 | 2025-06-25 00:41:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 14.2 |
| 4ce52a01-12fb-3211-bde3-fcaaf7ae16a8 | -9.514 | -56.09966 | 2025-06-25 00:41:00 | TERRA_M-M | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 59.7 |
| d7e197d0-74b4-3f3f-b7c4-6777f25b0bdd | -6.18089 | -48.08657 | 2025-06-25 00:41:00 | TERRA_M-M | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 3ac396c8-67f1-3075-9ba9-7a41a7864ee1 | -7.69896 | -49.31912 | 2025-06-25 00:41:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 553d5ad1-86b2-3242-b910-cf704592ace2 | -9.50032 | -56.10147 | 2025-06-25 00:41:00 | TERRA_M-M | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 38.1 |
| cff073a2-f646-3cdb-8aa4-8d3968471693 | -8.67391 | -51.46578 | 2025-06-25 00:41:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 432ed219-bcb8-3457-99e1-287747bd71eb | -6.22567 | -43.35167 | 2025-06-25 00:41:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| a5af9fab-e9c0-3a2b-a9b2-635308d1a5cf | -11.11131 | -44.52718 | 2025-06-25 00:41:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 34.5 |
| 6f85c7e8-fa1c-3a86-bae3-82363139f714 | -6.17958 | -48.07727 | 2025-06-25 00:41:00 | TERRA_M-M | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 207.8 |
| 77a73c9d-79c6-32bf-a0df-3a2df64d21f8 | -9.56821 | -49.10452 | 2025-06-25 00:41:00 | TERRA_M-M | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 53b90086-893e-3123-b810-8b2e9e826f0f | -11.18719 | -48.62432 | 2025-06-25 00:41:00 | TERRA_M-M | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 253b05cf-00ba-3b47-b2ac-aa2a2e3b639e | -10.83398 | -54.05371 | 2025-06-25 00:41:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 305b9551-743b-3809-b2ec-93bf49d56060 | -7.86534 | -50.66827 | 2025-06-25 00:41:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 39f57262-8f80-35d0-9011-ada0a052515c | -9.92523 | -52.4331 | 2025-06-25 00:41:00 | TERRA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 22.0 |
| 80c71604-7bea-33b7-b5eb-e8bbaa6256bd | -8.13926 | -50.98763 | 2025-06-25 00:41:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 024d5317-ea87-39f3-a8fe-d727fb24b903 | -11.58192 | -44.63542 | 2025-06-25 00:41:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 34.2 |
| e190616a-5e30-3f78-b42f-fb358b86fe16 | -6.1887 | -48.07957 | 2025-06-25 00:41:00 | TERRA_M-M | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 3c11afc7-411c-361d-9216-c2fe34f295a2 | -8.86817 | -47.28071 | 2025-06-25 00:41:00 | TERRA_M-M | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 5db07d23-8446-3895-9d86-d64a11a6e42a | -12.79434 | -48.72855 | 2025-06-25 00:41:00 | TERRA_M-M | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 40f3f51f-6460-3862-b8b5-657f6a29074d | -11.94095 | -48.42004 | 2025-06-25 00:41:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 16.5 |
| b1b0d3a3-58d9-3c66-b285-f4a83b01adac | -7.20069 | -43.1045 | 2025-06-25 00:41:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 265.8 |
| 1e7a5403-3029-39fd-9826-4f7b654ee6dd | -6.16788 | -48.05984 | 2025-06-25 00:41:00 | TERRA_M-M | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f7098864-3c08-3756-a203-726b156fa7ae | -8.47623 | -50.284 | 2025-06-25 00:41:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| fbb6b9ed-d1fa-3981-b1d7-9257b68806d9 | -3.61685 | -47.53843 | 2025-06-25 00:43:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 30.6 |
| 5d01ce16-31b3-3d60-b899-c732fc925849 | -4.37094 | -48.067 | 2025-06-25 00:43:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 0db51312-0fcd-365d-93a6-75526ccd2a00 | -4.2346 | -43.63308 | 2025-06-25 00:43:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| d884909f-2238-3b56-a863-2a2f35cc46b8 | -3.6154 | -47.52801 | 2025-06-25 00:43:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 7ff6b647-11ed-3b66-b1ca-c6dadc5da517 | -3.62172 | -47.54197 | 2025-06-25 00:43:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 35e7eb6e-9a7c-392a-bfce-a1897ece9f27 | -3.62021 | -47.53157 | 2025-06-25 00:43:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 24.3 |
| 498e62b6-3167-3377-bae6-00e61b9f59bb | -4.54714 | -48.00965 | 2025-06-25 00:43:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 2714a83e-141b-3aad-85d9-6c96e02d9f43 | -4.38016 | -48.06567 | 2025-06-25 00:43:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 624749b2-f296-319e-afb5-0333c67a14e8 | -7.184 | -43.0954 | 2025-06-25 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 70.0 |
| 22ebe032-f505-3785-8263-53c171966e95 | -7.2025 | -43.1171 | 2025-06-25 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 66.0 |
| 02c7aed2-1ccd-3347-a2a7-8c9ac13ee6bd | -7.0171 | -44.5725 | 2025-06-25 00:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 3c83f651-0f6a-3e43-9317-6f121ab10bc0 | -13.0408 | -48.825 | 2025-06-25 00:50:00 | GOES-19 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 129.8 |
| cf21186e-6b07-3ba2-9ef7-01b9bfd6fd76 | -7.0174 | -44.5495 | 2025-06-25 00:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 1075533f-2e64-34fb-897d-f4265a074d56 | -13.0601 | -48.8223 | 2025-06-25 00:50:00 | GOES-19 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 73.6 |
| d48041c2-8d69-3af4-9cde-94cf11ecb928 | -7.2217 | -43.0917 | 2025-06-25 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 64.1 |
| b7c47b52-e663-3773-899e-209433023855 | -7.2028 | -43.0936 | 2025-06-25 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 172.0 |
| 4c7b5c07-8afd-3b63-bda6-3f98bd582406 | -13.0405 | -48.847 | 2025-06-25 00:50:00 | GOES-19 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 4ceb0638-4c99-35dd-b691-fd0051313b40 | -9.577 | -49.107 | 2025-06-25 00:50:00 | GOES-19 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 54.2 |
| 3b644e03-a768-37ed-8f81-f520c71ac4ce | -9.518 | -56.0975 | 2025-06-25 00:50:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 52.9 |
| cb4af7e1-d576-3448-848a-e25afffd4621 | -9.4993 | -56.0988 | 2025-06-25 00:50:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 58.2 |
| b83f355a-c30f-316d-b1e9-c4e8a92baea4 | -7.0171 | -44.5725 | 2025-06-25 01:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 839bc40f-8577-398c-9590-521b808dd4f4 | -4.5243 | -48.016 | 2025-06-25 01:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 32.2 |
| e60e481c-9cfd-39f3-a630-a55c3ff15dd2 | -6.1792 | -48.0494 | 2025-06-25 01:00:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 234.5 |
| 19bc9cb7-63de-3e00-a068-b8089d6f275a | -4.5429 | -48.0151 | 2025-06-25 01:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 544c178f-b6da-3913-a6c5-5eb9228fe1db | -7.2025 | -43.1171 | 2025-06-25 01:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 75.4 |
| fe527b2d-8c3f-3982-ad13-a3176280f425 | -9.518 | -56.0975 | 2025-06-25 01:00:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 57.3 |
| e84522df-69b9-3eee-b83d-53e9ccc94235 | -6.1789 | -48.0929 | 2025-06-25 01:00:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 155.3 |
| fe217c52-121f-3545-88b0-9d4cca141f83 | -7.0174 | -44.5495 | 2025-06-25 01:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 69.5 |
| bc535add-9353-3be8-a482-e171c8ef28f5 | -6.1977 | -48.0699 | 2025-06-25 01:00:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 102.1 |
| f9eae08d-0f9d-3ff0-bebf-a0d11ac0f247 | -6.1979 | -48.0482 | 2025-06-25 01:00:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 47.0 |
| ca3bd91a-787e-3ed1-bcf6-0b0381da72f1 | -9.577 | -49.107 | 2025-06-25 01:00:00 | GOES-19 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 68.5 |
| d5362ecc-b736-3959-b5d4-68cd778be945 | -6.1791 | -48.0712 | 2025-06-25 01:00:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 583.5 |
| 5291324b-be26-3fd5-92ad-c52d93ff1808 | -6.2224 | -43.3693 | 2025-06-25 01:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 45.1 |
| de42a47a-3a39-3761-a2cc-156af14bf9f3 | -13.0601 | -48.8223 | 2025-06-25 01:00:00 | GOES-19 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 96e19ed6-9376-3c64-bf4a-10d0d92d99bf | -6.1604 | -48.0724 | 2025-06-25 01:00:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 3a4d24ca-f8a6-3324-ba6b-277116f0e905 | -13.0405 | -48.847 | 2025-06-25 01:00:00 | GOES-19 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 61be0c48-63ad-3b64-b668-4c2beb11090d | -4.543 | -47.9934 | 2025-06-25 01:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 37.7 |
| e1a1cf3b-a843-329d-9d23-e96f6c794670 | -13.0408 | -48.825 | 2025-06-25 01:00:00 | GOES-19 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 164.1 |
| 790299ff-9948-31cb-9612-8348e035cd76 | -7.2028 | -43.0936 | 2025-06-25 01:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 169.9 |
| e42a572f-12ef-319d-8bf9-32ab3d5d3785 | -4.5429 | -48.0151 | 2025-06-25 01:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 35.1 |
| f12fcb60-f1c9-3c44-a34e-e8ceaa0b1c60 | -7.0171 | -44.5725 | 2025-06-25 01:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 1ecba274-be2f-38f1-9678-8ccecf6b41e4 | -7.2028 | -43.0936 | 2025-06-25 01:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 133.8 |
| 93d0d665-43ae-3474-94c6-6e86cbcadf16 | -13.0601 | -48.8223 | 2025-06-25 01:10:00 | GOES-19 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 6304095e-308c-3b6c-8fed-09e54a60a186 | -9.5581 | -49.1089 | 2025-06-25 01:10:00 | GOES-19 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 44.1 |
| 4261d653-4bf1-3812-b821-09bac102bb19 | -9.577 | -49.107 | 2025-06-25 01:10:00 | GOES-19 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 46.0 |
| f72b44c4-e059-3ba9-8f7a-5eb16a3011e4 | -13.0408 | -48.825 | 2025-06-25 01:10:00 | GOES-19 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 128.4 |
| 7979c7e6-a769-3e2d-8bb7-126f819dde9b | -9.4993 | -56.0988 | 2025-06-25 01:10:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 352e2eb6-5410-3911-91a5-c3578f0eb255 | -7.0174 | -44.5495 | 2025-06-25 01:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 382c6d97-c60d-3ead-a9df-d6baa5c6d483 | -13.0405 | -48.847 | 2025-06-25 01:10:00 | GOES-19 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 71.3 |
| e4624ede-f888-31cc-9a67-bb922dc6cfc2 | -13.0408 | -48.825 | 2025-06-25 01:20:00 | GOES-19 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 131.5 |
| e6a4dabb-49d9-3d66-929b-153c75f45ce4 | -6.1977 | -48.0699 | 2025-06-25 01:20:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 88.7 |
| ea74749b-e3fa-3cae-82fa-728af77e6f74 | -9.518 | -56.0975 | 2025-06-25 01:20:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 12c07092-860f-3324-b892-38dc4f9176b0 | -7.2028 | -43.0936 | 2025-06-25 01:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 152.8 |
| 3c107a10-a3ed-3f45-90a9-fe8d2d6d0fd1 | -9.577 | -49.107 | 2025-06-25 01:20:00 | GOES-19 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 44.5 |
| 616fd17d-fd87-38b5-a5cb-3aa3f2e4b593 | -6.1792 | -48.0494 | 2025-06-25 01:20:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 195.1 |
| e9a9aa6d-ed6b-335d-b7eb-3d04c825a69f | -13.0405 | -48.847 | 2025-06-25 01:20:00 | GOES-19 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 8a81136b-94ca-327e-a403-b6b2ada45e9a | -6.1789 | -48.0929 | 2025-06-25 01:20:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 069d8db8-012b-30f4-8fa0-d8812e12fbd2 | -6.1791 | -48.0712 | 2025-06-25 01:20:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 509.8 |
| 284bf786-e1e4-3991-9e70-57fcf2d2275d | -6.1604 | -48.0724 | 2025-06-25 01:20:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 51.6 |
| aecc4184-a3a6-36d9-b0a3-ad0c83d2ef68 | -7.0171 | -44.5725 | 2025-06-25 01:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 64.5 |
| c1d04a8e-2098-3d3c-be34-49bc278cbde7 | -7.0174 | -44.5495 | 2025-06-25 01:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 0baa1fec-b81b-32d5-b78d-6b81847d0e55 | -7.2028 | -43.0936 | 2025-06-25 01:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 107.9 |
| 6e9118cc-57bf-3b76-a637-6687d5cfaf19 | -6.1604 | -48.0724 | 2025-06-25 01:30:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 50.5 |
| e08d989a-7da8-3301-84b0-f070edf16d08 | -6.1977 | -48.0699 | 2025-06-25 01:30:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 6191a33e-89fd-3635-9386-7f53b689fcd5 | -6.1789 | -48.0929 | 2025-06-25 01:30:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 4585853b-969e-35eb-afb5-767cbf09b5a4 | -9.518 | -56.0975 | 2025-06-25 01:30:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 43.2 |
| 61304e12-84de-34fe-ac05-a01c4dce6d99 | -6.1792 | -48.0494 | 2025-06-25 01:30:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 170.3 |
| bbf272ae-607b-3933-bdd1-c1d3cef5613a | -7.0174 | -44.5495 | 2025-06-25 01:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 70.5 |
| ad8a7a62-6ef5-349c-98c0-feb4a34d7f7d | -7.0171 | -44.5725 | 2025-06-25 01:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 68.1 |
| d96a7385-6e6d-338a-8ea2-39af4055ecad | -13.0408 | -48.825 | 2025-06-25 01:30:00 | GOES-19 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 120.2 |


[Clique aqui para ver as próximas entradas](README4.md)

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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3fca6847-cef5-39b6-8ce8-6e00dbc5ef75 | -3.6978 | -50.1225 | 2024-10-12 00:55:27 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 143.0 |
| 5752c027-f752-34cd-8e35-81190aabbd93 | -3.6979 | -50.1015 | 2024-10-12 00:55:27 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 81.1 |
| ead2ba3b-5259-3e69-a854-11c42dfc83dd | -3.7163 | -50.1219 | 2024-10-12 00:55:27 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 7abf25b7-d6c3-3b6f-8556-d7e54e7ba702 | -3.7844 | -51.3312 | 2024-10-12 00:55:28 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 2b4bf12d-7f73-3c3f-9b28-05317f84f251 | -3.7845 | -51.3104 | 2024-10-12 00:55:28 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 53be6e90-8cb2-3d1d-8606-01fb0e5edbe7 | -3.9394 | -46.445 | 2024-10-12 00:55:29 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 143.1 |
| c1daa097-f401-3b86-b1c9-edd6205f4f92 | -3.9396 | -46.4229 | 2024-10-12 00:55:29 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 129.8 |
| aa3c1b39-7fa1-30ac-9cd2-d13f030435af | -4.2665 | -50.9594 | 2024-10-12 00:55:31 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 7c0f36aa-f843-3d07-b429-7d240a64e78d | -4.285 | -50.9586 | 2024-10-12 00:55:31 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 6f3437fa-97ae-37f4-998b-11abf54a7ee8 | -4.3782 | -50.8087 | 2024-10-12 00:55:31 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 88.8 |
| 70668ac1-6e9b-3ce7-a18e-b43451b62c92 | -4.7004 | -60.8077 | 2024-10-12 00:55:33 | GOES-16 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 19fd934e-a21c-3a4b-ba90-9b737a6be9f9 | -4.7188 | -60.8072 | 2024-10-12 00:55:33 | GOES-16 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 55.9 |
| dd3b7de1-237e-399c-b2be-b3207896fbd9 | -4.7188 | -60.7882 | 2024-10-12 00:55:33 | GOES-16 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 93.1 |
| b35adc3a-f391-3921-b8db-e20fd151a961 | -4.7371 | -60.7877 | 2024-10-12 00:55:33 | GOES-16 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 024d5a43-d456-30bf-936b-adb588e8de23 | -5.1919 | -48.1756 | 2024-10-12 00:55:36 | GOES-16 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 211dcbca-dd26-33c2-8b98-d169049f3555 | -5.2105 | -48.1745 | 2024-10-12 00:55:36 | GOES-16 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 643289dc-28f7-3186-939b-cb679ab5243a | -6.0791 | -44.6276 | 2024-10-12 00:55:41 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 54.9 |
| 25523331-b816-3655-998a-9e67f397dfb3 | -6.7284 | -59.346 | 2024-10-12 00:55:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 78acf6aa-38c4-35e5-af5f-925b7842f85c | -6.7285 | -59.3267 | 2024-10-12 00:55:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 109.7 |
| 306d42e2-6d68-3a67-925d-ac30f19639a7 | -6.7469 | -59.3452 | 2024-10-12 00:55:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 198.7 |
| 9c36906f-1ad2-3c23-970c-b8be892a53a0 | -6.747 | -59.3259 | 2024-10-12 00:55:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 303.5 |
| c7369170-4a8a-347a-bddc-bfa371943ef7 | -6.7471 | -59.3067 | 2024-10-12 00:55:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.7 |
| ecba5fc2-7297-3169-a031-fa5b3cffe300 | -6.7654 | -59.3252 | 2024-10-12 00:55:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 8b172b16-e8f2-3ef0-b4ee-e4eba296316d | -6.8776 | -59.0697 | 2024-10-12 00:55:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 64a0b54d-cedb-3684-b593-a8242b1660ae | -8.2325 | -61.1823 | 2024-10-12 00:55:54 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 828790ff-2489-39ad-a0c3-abe4813ece33 | -8.4631 | -66.9783 | 2024-10-12 00:55:55 | GOES-16 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 21f05f92-9dce-389b-aaab-d6bcedf99e35 | -8.9228 | -63.5447 | 2024-10-12 00:55:58 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 01610ff6-66a0-3b93-b452-cdec9b07fff1 | -9.6594 | -56.9635 | 2024-10-12 00:56:01 | GOES-16 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 49.7 |
| ae5df9b8-43c0-371a-99eb-5b94dfa95de7 | -10.3708 | -61.232 | 2024-10-12 00:56:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 72.2 |
| a4e5a890-a924-353b-917f-634bff67e8b2 | -10.3892 | -61.2695 | 2024-10-12 00:56:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 4a75e486-499b-3c05-95ba-5618a24551a0 | -10.3895 | -61.231 | 2024-10-12 00:56:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 89c8b514-3237-351f-b62b-22afb005e15a | -10.3897 | -61.2118 | 2024-10-12 00:56:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 70cb2727-0d63-38b1-9704-3c9bd21b3867 | -10.9506 | -44.653 | 2024-10-12 00:56:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 167.4 |
| 1e762d01-4fce-30c2-b37d-c66d0c66f1e5 | -10.951 | -44.6298 | 2024-10-12 00:56:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 91a2049f-8bb3-3779-9a08-9b2aec31e923 | -10.8362 | -64.2027 | 2024-10-12 00:56:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 45.2 |
| e2b7a2ca-4cee-3b1c-ac45-53532ad7bef8 | -11.2761 | -60.5038 | 2024-10-12 00:56:11 | GOES-16 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 70.2 |
| c395349f-6138-3890-ac26-583775b761f5 | -11.2763 | -60.4844 | 2024-10-12 00:56:11 | GOES-16 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 130a1159-baef-3242-a702-04adaedc4e88 | -11.8188 | -58.8459 | 2024-10-12 00:56:14 | GOES-16 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 67.7 |
| a7372595-b347-30da-b59b-3b18cf49c0de | -11.8377 | -58.8445 | 2024-10-12 00:56:14 | GOES-16 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 138.9 |
| 91b667c7-99f6-3c0f-8405-66c7cafa63a0 | -12.5846 | -48.6014 | 2024-10-12 00:56:17 | GOES-16 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 0ea2af74-d332-348d-a812-23dc32b07120 | -12.6034 | -48.6209 | 2024-10-12 00:56:17 | GOES-16 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 57.8 |
| adcd9fcc-d8a3-3ecd-931a-d280c6bc2991 | -12.7678 | -44.8671 | 2024-10-12 00:56:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 2c4a2cb7-453a-32ac-90f4-7d18285b2927 | -12.7866 | -44.8873 | 2024-10-12 00:56:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 474.0 |
| fc8a057d-b0c0-33bd-a3fe-2208f747d0dd | -12.7871 | -44.8639 | 2024-10-12 00:56:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 975.2 |
| 05bc28fa-5b9f-3e21-a02c-83671fe24560 | -12.7875 | -44.8406 | 2024-10-12 00:56:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 143.4 |
| a5a7ec3b-e853-3169-ac8a-b30df6b9b86b | -12.806 | -44.8841 | 2024-10-12 00:56:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 159.1 |
| 3464aeaf-a33d-3fbd-96c2-0c6a975630bb | -12.8064 | -44.8608 | 2024-10-12 00:56:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 288.3 |
| 0f5c0771-c9cf-3115-95aa-43265d0e135f | -12.9464 | -53.5339 | 2024-10-12 00:56:20 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 9e9d9f81-c756-37e8-a45a-f63baf353c0b | -12.9467 | -53.5131 | 2024-10-12 00:56:20 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 65.7 |
| f5075a35-6aae-3bd6-8153-4fe947c675fe | -12.9655 | -53.5319 | 2024-10-12 00:56:20 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 129.5 |
| f2aa59b2-dbc2-36d0-9edc-5941306568d4 | -12.9658 | -53.511 | 2024-10-12 00:56:20 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 74.9 |
| adb7dc10-8a6a-3667-9d61-d5caa010bf75 | -13.2322 | -51.1192 | 2024-10-12 00:56:21 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 97c8a630-70f9-3cd6-a8f3-30cd91e95ddd | -13.2325 | -51.0978 | 2024-10-12 00:56:21 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 8fb9c308-3b3b-30b6-abb8-e6ac303e0214 | -15.0524 | -45.073 | 2024-10-12 00:56:30 | GOES-16 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 133.6 |
| 54c99c21-a873-3bdb-859d-e441052a7f10 | -15.0529 | -45.0495 | 2024-10-12 00:56:30 | GOES-16 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 69.4 |
| a8565967-09b4-3940-ac3d-0ececcab9419 | -16.9802 | -57.4609 | 2024-10-12 00:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 72.4 |
| 2127cfe7-6a0c-3166-b094-d091ce9886b0 | -16.9805 | -57.4404 | 2024-10-12 00:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 117.3 |
| f215d5e4-7230-3fd1-b742-66b2b9074246 | -16.9998 | -57.4586 | 2024-10-12 00:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 81.6 |
| 134859a8-803c-31ac-9df9-d67683c95932 | -17.0426 | -56.0333 | 2024-10-12 00:56:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 69.0 |
| 8f35c754-d755-37d6-ba41-064075982349 | -17.1564 | -57.4608 | 2024-10-12 00:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 69.5 |
| c9b9044e-d0ee-37ea-aac9-e6d5e4601dff | -17.1761 | -57.4585 | 2024-10-12 00:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 108.4 |
| 88f5b5f0-e386-3007-8b08-3aa003f5c860 | -17.627 | -56.3318 | 2024-10-12 00:56:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 147.1 |
| 904257c0-5801-354f-a86a-03f10d64863a | -17.6273 | -56.311 | 2024-10-12 00:56:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 79.4 |
| 122fcde8-7b9c-382f-b518-eaa242392ead | -17.6467 | -56.3292 | 2024-10-12 00:56:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 176.0 |
| 5f76ae06-ad95-3ae9-8b55-4c3e01467431 | -17.6471 | -56.3084 | 2024-10-12 00:56:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 92.7 |
| 312fe6ad-b1e9-38e0-b7f2-eb28989ecafa | -17.964 | -57.3843 | 2024-10-12 00:56:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 79.5 |
| ac43da42-532a-35b7-bb0c-3eaf584cb20a | -17.9643 | -57.3637 | 2024-10-12 00:56:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 78.0 |
| a6153193-912e-3d87-8f28-1e0eca35fda0 | -17.9837 | -57.3819 | 2024-10-12 00:56:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 83.7 |
| 2ac344b7-0296-36bf-86db-6714c984bd31 | -17.9841 | -57.3612 | 2024-10-12 00:56:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 83.1 |
| 2854d259-54b6-33ec-87e1-eb1f96eaffc2 | -18.196 | -56.5275 | 2024-10-12 00:56:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 78.8 |
| 6b2dcc80-2696-36d2-adba-e27e2b731afa | -18.1964 | -56.5066 | 2024-10-12 00:56:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 51.4 |
| 529ef9fb-7e32-399d-ba84-2955c0c8ab9d | -17.87 | -57.41 | 2024-10-12 01:03:43 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 9a6ca24f-f70a-3ffb-84fa-f718645e992e | -17.87 | -57.34 | 2024-10-12 01:03:43 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| addf03cd-c996-3222-b8f4-675e509969d2 | -17.84 | -57.31 | 2024-10-12 01:03:45 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| c38ea88f-801b-36ca-8058-198febd5cfe9 | -17.84 | -57.39 | 2024-10-12 01:03:45 | MSG-03 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| bbab9057-2c6e-3f54-9ec8-c0c0cd9c0c6a | -12.76 | -44.89 | 2024-10-12 01:04:12 | MSG-03 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5f83650f-4a50-36fe-9ab6-7ac524376b31 | -12.76 | -44.84 | 2024-10-12 01:04:12 | MSG-03 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 70b08bc9-2f23-3eac-b640-46aeb93f15b9 | -12.79 | -44.95 | 2024-10-12 01:04:12 | MSG-03 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 05ad29de-f963-3eb9-8730-ce68bfe531f9 | -12.79 | -44.9 | 2024-10-12 01:04:12 | MSG-03 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 96120b53-9be5-3eff-8672-6793ea27d1cd | -12.79 | -44.85 | 2024-10-12 01:04:12 | MSG-03 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f160f784-d9d6-3e88-b02c-54b62e86fc6b | -1.5877 | -53.3494 | 2024-10-12 01:05:15 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| f88b5ca7-d96d-3e36-b3fd-a750c9cad45c | -2.1911 | -54.4861 | 2024-10-12 01:05:19 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 43.7 |
| ca114187-a13b-32ae-9db9-b6f020ca5215 | -2.77 | -51.3829 | 2024-10-12 01:05:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 84.1 |
| d36c291c-2e73-3ce0-b8fe-f955334df571 | -2.7701 | -51.3622 | 2024-10-12 01:05:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 117.5 |
| 23f730db-adc8-32ee-a239-6cc5be4a733c | -2.7884 | -51.3825 | 2024-10-12 01:05:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 93.1 |
| ec14e812-840c-3ac5-b31b-8da5ceedec77 | -2.7885 | -51.3618 | 2024-10-12 01:05:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 136.6 |
| 8494ac86-1ff2-35da-a9e6-8dbfaba762d4 | -3.0311 | -50.5642 | 2024-10-12 01:05:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 618032e2-6b1e-32d3-b53f-2a3724854121 | -3.1426 | -50.3724 | 2024-10-12 01:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 103.2 |
| 3f5a72b9-c11e-376f-b560-09bc85563193 | -3.1427 | -50.3514 | 2024-10-12 01:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 85.0 |
| f5bdcd17-c099-307c-b0a0-5e7d54983f6f | -3.161 | -50.3718 | 2024-10-12 01:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 114.8 |
| 79bde4a9-cea9-3a11-9015-9f078e7525cf | -3.1611 | -50.3508 | 2024-10-12 01:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 132.0 |
| a3efe0ff-cd11-3d16-8b74-6dac342e5238 | -3.2136 | -46.7843 | 2024-10-12 01:05:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 106.0 |
| 62fbd565-ed67-3a15-91bc-cf6bb975232d | -3.2137 | -46.7623 | 2024-10-12 01:05:24 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 857c3096-a954-35fb-a07e-026a695cc500 | -3.6901 | -47.9234 | 2024-10-12 01:05:27 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| b55dfac0-8436-3c91-9cda-1c76e6f99ae4 | -3.7087 | -47.9227 | 2024-10-12 01:05:27 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 8ebab147-e177-3eb9-a17b-166003e0d096 | -3.9208 | -46.4459 | 2024-10-12 01:05:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 191629a7-0037-34fd-81eb-bf33d4667f7d | -3.9394 | -46.445 | 2024-10-12 01:05:29 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 103.5 |
| d8c96b43-f11f-3599-bc4d-f1b655d7728f | -3.9396 | -46.4229 | 2024-10-12 01:05:29 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 89.2 |
| b7191f40-9195-3d83-857c-adaa508ad10d | -4.2665 | -50.9594 | 2024-10-12 01:05:31 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 98.7 |
| 1741192a-24c0-36e9-8513-a88a5dc0f800 | -4.3782 | -50.8087 | 2024-10-12 01:05:31 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 95.4 |


[Clique aqui para ver as próximas entradas](README12.md)

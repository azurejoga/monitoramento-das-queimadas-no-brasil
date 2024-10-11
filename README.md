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
| 4dcca9c5-c8e8-33da-8b5b-db2841f0959b | -13.89 | -45.86 | 2024-10-11 00:04:05 | MSG-03 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4911878b-1818-3c37-890f-5a0c99d53361 | -13.92 | -45.87 | 2024-10-11 00:04:05 | MSG-03 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5438e66b-a3d2-32b9-b84b-256ccc869dbb | -13.92 | -45.82 | 2024-10-11 00:04:05 | MSG-03 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5ac2197b-c2b2-30e5-9699-f29e7092fa13 | -6.94 | -34.97 | 2024-10-11 00:04:44 | MSG-03 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9d96a4e2-c8af-32bb-a567-3f8841aab805 | -6.94 | -34.93 | 2024-10-11 00:04:44 | MSG-03 | LUCENA | PARAÍBA | Brasil | 2508604 | 25 | 33 | nan | nan | nan | Mata Atlântica | nan |
| fbacbcf2-fe38-3a06-8f88-d04b8db1413a | -6.97 | -34.94 | 2024-10-11 00:04:44 | MSG-03 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7a11add2-1f72-3b57-a9eb-ef560bc412c9 | -4.11 | -48.25 | 2024-10-11 00:05:03 | MSG-03 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 56d9d44f-a29c-31bf-89e0-d5165dd53e9f | -2.99 | -52.9 | 2024-10-11 00:05:11 | MSG-03 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0efe7ff0-48e8-35f5-b3a2-79f3bac51b3c | -2.78 | -52.53 | 2024-10-11 00:05:13 | MSG-03 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7eddac0e-539f-3b4b-a852-fa297516e58c | -2.78 | -52.47 | 2024-10-11 00:05:13 | MSG-03 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0b515b98-9387-3114-b10c-cee6e70289e2 | -2.5444 | -47.2231 | 2024-10-11 00:05:21 | GOES-16 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 1ac18430-7ab3-31da-8d4d-12fe90c1f10a | -2.6533 | -53.3506 | 2024-10-11 00:05:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 162.0 |
| 790ea20c-4aaf-36c4-9d46-462910755972 | -2.6716 | -53.3502 | 2024-10-11 00:05:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 112.9 |
| 1678cdd2-3699-3b6a-94d2-014c47a79875 | -2.7663 | -52.4937 | 2024-10-11 00:05:22 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 80.8 |
| db1308c3-0feb-331c-a809-3c9c0cbe3e4c | -2.7664 | -52.4733 | 2024-10-11 00:05:22 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 069de3f8-3a5f-3003-bade-9d80e5214731 | -2.7847 | -52.4933 | 2024-10-11 00:05:22 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 406.8 |
| 25e160d9-ade0-3749-9c23-4e6ff439b8e9 | -2.7848 | -52.4728 | 2024-10-11 00:05:22 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 392.7 |
| 37bf2f72-152a-36af-a4e4-2f0ad59a95bc | -2.8081 | -51.0084 | 2024-10-11 00:05:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 97031010-9947-3eae-971a-1b76ecc06644 | -2.9674 | -47.9931 | 2024-10-11 00:05:23 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 9439de20-aa8c-3348-80b6-58e4d1e1a584 | -2.9673 | -52.9169 | 2024-10-11 00:05:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 141.4 |
| b4e2466f-c203-3786-bae0-48aa513df672 | -2.9673 | -52.8966 | 2024-10-11 00:05:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 190.3 |
| db728cbf-882f-3d29-b40a-6de207594a07 | -2.9728 | -51.3568 | 2024-10-11 00:05:23 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 80eba7a7-8714-388b-89da-96d6eecf2b69 | -2.9859 | -47.9925 | 2024-10-11 00:05:23 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 6caa179d-a2d5-3a78-8d34-3a874cfc45f1 | -2.9857 | -52.9164 | 2024-10-11 00:05:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 172.3 |
| cf632a64-38f5-3076-9274-94ae07b2d7d6 | -2.9857 | -52.8961 | 2024-10-11 00:05:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 173.1 |
| 5a3bb2e7-8445-3534-adb3-e0a51e9a4c98 | -3.0343 | -61.6918 | 2024-10-11 00:05:24 | GOES-16 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 165b0815-7df8-3fd7-9b37-641fd4eea066 | -3.0343 | -61.673 | 2024-10-11 00:05:24 | GOES-16 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 106.4 |
| 03a761ea-0b84-34eb-8968-d5ecb2b5ce14 | -3.0525 | -61.6916 | 2024-10-11 00:05:24 | GOES-16 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 56.7 |
| e91a5966-024e-3eb8-bdd7-664d45a8f802 | -3.0525 | -61.6727 | 2024-10-11 00:05:24 | GOES-16 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 72.3 |
| c3c15c4c-ae3a-34c8-b083-fcd1cf092d32 | -3.1422 | -50.4562 | 2024-10-11 00:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 136319d9-3fd3-3901-a157-2ebf1256dcab | -3.1423 | -50.4352 | 2024-10-11 00:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 96.2 |
| b23b9751-7e29-3998-b052-3fb4c2939864 | -3.1607 | -50.4556 | 2024-10-11 00:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 105.4 |
| 80780b74-bd4c-3088-96ad-5064ba9e344e | -3.1608 | -50.4347 | 2024-10-11 00:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 185.3 |
| 4ccab6f8-05d4-383d-b71b-1aa1cf5cac2f | -3.3098 | -46.0724 | 2024-10-11 00:05:25 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 49512bbd-3267-30b9-afab-c2fa4fc6a200 | -3.3096 | -50.1781 | 2024-10-11 00:05:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 687c9301-5a7c-32de-8b77-9fa9b0da89ec | -3.614 | -44.7783 | 2024-10-11 00:05:27 | GOES-16 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 408ff26a-084a-3dba-8f87-d078f556f5f0 | -3.9103 | -48.3466 | 2024-10-11 00:05:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 4150b8f6-0f27-39d1-8bde-74c0799e7a7b | -4.0962 | -48.2523 | 2024-10-11 00:05:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 127.8 |
| 04d4d59d-4fff-3b5e-ac2f-e5e66400aec9 | -4.0963 | -48.2307 | 2024-10-11 00:05:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 62acb1c5-a502-33f6-ab29-33780d69b6f8 | -4.1148 | -48.2515 | 2024-10-11 00:05:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 129.4 |
| c3f55a5b-0447-3cff-a6c4-3b172b14cd8c | -4.1149 | -48.2299 | 2024-10-11 00:05:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 3fd166d2-82b3-30d4-9062-fbd321362928 | -5.1725 | -48.2848 | 2024-10-11 00:05:36 | GOES-16 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 165.5 |
| 4cf2801d-97a6-305d-98cb-4ee6f9699a13 | -5.1727 | -48.2632 | 2024-10-11 00:05:36 | GOES-16 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 60.4 |
| e136fab1-298f-36d4-bd97-1a7b77b8739e | -5.3264 | -60.143 | 2024-10-11 00:05:37 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 230f93da-0d3d-3dc4-bd25-ad08e4b9e26d | -5.3265 | -60.1239 | 2024-10-11 00:05:37 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 82.8 |
| c61bcd86-6260-3702-8093-fdb7f1ce17bd | -6.5404 | -60.0259 | 2024-10-11 00:05:44 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 33c04116-d450-39e5-ac5b-3cde9871c1e0 | -6.5588 | -60.0444 | 2024-10-11 00:05:44 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 66.9 |
| abd48554-ecf0-3597-a7a9-73378e0ae9fa | -6.5589 | -60.0252 | 2024-10-11 00:05:44 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 99.7 |
| a7c5581f-5e3e-310f-b2a1-8412d14efce6 | -6.9439 | -34.9766 | 2024-10-11 00:05:45 | GOES-16 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 62.4 |
| 7798e1f8-a4f1-3ccc-901a-632dee35eebd | -6.9442 | -34.949 | 2024-10-11 00:05:45 | GOES-16 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 104.6 |
| e78f324b-11f2-3bfa-a29c-e9e232836150 | -6.7469 | -59.3452 | 2024-10-11 00:05:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 41.3 |
| bf31bc33-4dde-3b85-ba99-1ee2972779b2 | -6.747 | -59.3259 | 2024-10-11 00:05:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 7155d866-76fe-3bfc-b667-cce61884a11d | -6.7654 | -59.3252 | 2024-10-11 00:05:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 76ee8c10-9224-3f79-bb36-3523998d6102 | -7.0786 | -59.4087 | 2024-10-11 00:05:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 8a8f740d-7eb9-3054-b9af-f20a6d2fc7c9 | -8.4417 | -55.4692 | 2024-10-11 00:05:54 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 125.6 |
| 8e89a5f2-9371-3502-8fd9-942a9d0c7f61 | -8.4419 | -55.4491 | 2024-10-11 00:05:54 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 38a156c4-4a57-336b-b0de-9b511c176a46 | -9.7374 | -46.9844 | 2024-10-11 00:06:01 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 92bf0791-94d4-395d-83dd-a477a196d2fa | -9.7377 | -46.9621 | 2024-10-11 00:06:01 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 192b124b-ff38-3501-8343-10dcce6160d0 | -10.441 | -46.7908 | 2024-10-11 00:06:05 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 38dfc078-85e8-3ba1-9978-39809d32708a | -10.46 | -46.7885 | 2024-10-11 00:06:05 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 161.0 |
| 23dac35a-804b-31a4-884c-1195c1e82a79 | -10.4604 | -46.766 | 2024-10-11 00:06:05 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 106.4 |
| a9147d1d-5616-3972-ad05-ba53c273f90f | -10.3632 | -55.8554 | 2024-10-11 00:06:05 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 2853899a-cead-33a2-b87e-5f5ec40b3ad9 | -10.4791 | -46.7862 | 2024-10-11 00:06:05 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 129.3 |
| 1e091d21-6c42-35ef-a220-551d0f1473b3 | -10.4794 | -46.7637 | 2024-10-11 00:06:05 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 81.9 |
| a54c4789-827d-3fe4-b848-6d6674f356c8 | -10.6171 | -47.704 | 2024-10-11 00:06:06 | GOES-16 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 362a5512-71bc-3d1f-8a7a-3843df474f2f | -10.6773 | -53.0372 | 2024-10-11 00:06:07 | GOES-16 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 95.4 |
| 7dd848e4-b661-388c-8219-7b3aa6c457a2 | -10.6776 | -53.0164 | 2024-10-11 00:06:07 | GOES-16 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 86.1 |
| dc65f739-dfa7-3978-a651-63ff7260725b | -10.6962 | -53.0354 | 2024-10-11 00:06:07 | GOES-16 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 178.3 |
| 1d5f02b7-d620-3247-acf6-657ecdc6e004 | -10.6965 | -53.0147 | 2024-10-11 00:06:07 | GOES-16 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 152.1 |
| e009f0c6-e697-3869-a250-2c8eaf749265 | -10.7151 | -53.0337 | 2024-10-11 00:06:07 | GOES-16 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 89.3 |
| 5ea7c1e7-fa39-3ef0-bb57-7df03233168d | -10.7154 | -53.013 | 2024-10-11 00:06:07 | GOES-16 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 77.0 |
| e8601231-d3a2-3f0c-ac92-8c0f07d5711d | -11.2407 | -53.2738 | 2024-10-11 00:06:10 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 8b476960-06f3-3879-a128-62487af7bf2c | -11.2597 | -53.272 | 2024-10-11 00:06:10 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 21cb3ca9-97f1-3281-87f0-105e1f470428 | -11.2859 | -51.3031 | 2024-10-11 00:06:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 66.4 |
| e79933cb-5942-3452-9ef9-61f1ff004695 | -11.3048 | -51.3011 | 2024-10-11 00:06:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 58.3 |
| aeb6ff99-29c2-3e33-874c-675bb62e800b | -11.2763 | -60.4844 | 2024-10-11 00:06:11 | GOES-16 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 6840a5a2-7a34-3cdc-87da-70d0ac03ed2a | -12.3171 | -45.3083 | 2024-10-11 00:06:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 77.2 |
| bc0d6626-4ebd-3e91-af79-5e8f90b84b99 | -12.3463 | -43.7638 | 2024-10-11 00:06:15 | GOES-16 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 459586be-b99e-31a6-8ae9-fae307769a1b | -12.3467 | -43.7401 | 2024-10-11 00:06:15 | GOES-16 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 7af4c76d-4667-3a26-87bf-b5a82362d760 | -12.3656 | -43.7606 | 2024-10-11 00:06:15 | GOES-16 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 71.1 |
| c065308b-17e5-3cd0-bd5e-31bdefcfa207 | -12.366 | -43.7369 | 2024-10-11 00:06:15 | GOES-16 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 45259917-be8f-37be-97af-de9dacdd331f | -12.1571 | -46.7451 | 2024-10-11 00:06:15 | GOES-16 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 8b0cacee-fc4d-30f2-92a8-d44119a1566a | -12.1763 | -46.7424 | 2024-10-11 00:06:15 | GOES-16 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 53593f6c-55ad-333d-a153-4ca6d48072ce | -12.1766 | -46.7197 | 2024-10-11 00:06:15 | GOES-16 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 6b108247-a3ee-3a0a-8f07-89a56087a527 | -12.1955 | -46.7396 | 2024-10-11 00:06:15 | GOES-16 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 61.8 |
| bbbe7809-47d7-365b-82dd-effab8d54a41 | -12.1958 | -46.717 | 2024-10-11 00:06:15 | GOES-16 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 272a206d-a9c4-3fcf-b245-5f2a6f1559b7 | -12.4566 | -53.1294 | 2024-10-11 00:06:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 94.1 |
| 86d1c701-d273-350b-b43f-cc7c924eafbf | -12.4569 | -53.1086 | 2024-10-11 00:06:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 60.3 |
| b4359074-76ad-3d34-b457-ce8abe989d6c | -12.4754 | -53.1482 | 2024-10-11 00:06:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 2d987646-ebed-38cc-a86b-98ee2cb86724 | -12.4757 | -53.1274 | 2024-10-11 00:06:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 95.2 |
| 5706ca87-37dc-3862-aeb1-3744da4857aa | -12.476 | -53.1065 | 2024-10-11 00:06:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 57.5 |
| dedef2d4-af9a-3b39-8a18-677cff0a6be5 | -12.7673 | -44.8904 | 2024-10-11 00:06:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 16d6591a-9ebe-3088-bc02-10b39f8080b7 | -12.7678 | -44.8671 | 2024-10-11 00:06:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 92b4537f-855e-3050-8d14-2c45c903826d | -12.7866 | -44.8873 | 2024-10-11 00:06:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 113.1 |
| 97d11a41-95ce-3fd7-8dc7-c4f9e08c749d | -12.7871 | -44.8639 | 2024-10-11 00:06:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 133.7 |
| 67418a0c-d18d-352f-8a9b-b2e48e5b8abd | -12.9855 | -53.4673 | 2024-10-11 00:06:20 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 81.0 |
| c3846271-8b24-33c8-b936-345c537186e3 | -13.5078 | -42.7246 | 2024-10-11 00:06:22 | GOES-16 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 99.5 |
| 3ea74c1f-e5a3-38bb-8201-deee14729461 | -13.5084 | -42.7003 | 2024-10-11 00:06:22 | GOES-16 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 88.2 |
| b7723abd-41fa-3f7f-9d17-13734f9cf0f4 | -13.9269 | -45.8323 | 2024-10-11 00:06:24 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 12aebb7a-020f-39c9-86cc-e06d7f4989a1 | -2.5444 | -47.2231 | 2024-10-11 00:15:21 | GOES-16 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |


[Clique aqui para ver as próximas entradas](README2.md)

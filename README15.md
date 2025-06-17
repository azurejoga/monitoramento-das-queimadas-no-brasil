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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 909664d3-5635-3cfc-883d-4077c3471095 | -11.91004 | -54.82254 | 2025-06-17 04:36:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cbb6a155-d3c4-3261-8a58-371917b8e562 | -11.57245 | -44.67576 | 2025-06-17 04:36:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1cc9ce50-c849-3e36-b93d-1e7990d1b9dc | -12.42919 | -50.02703 | 2025-06-17 04:36:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cda85c7e-c581-397a-ad3d-e87ae6a9dc42 | -12.34754 | -49.3081 | 2025-06-17 04:36:00 | NPP-375D | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 486c6291-b9eb-3dd9-8674-f72c586722c9 | -11.03405 | -44.65119 | 2025-06-17 04:36:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3e84a3a0-6e10-3220-b186-f31dde2d3ace | -10.28086 | -60.5333 | 2025-06-17 04:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| daf61d40-cd7f-35d1-9b3f-0ef66259410b | -10.93941 | -55.32749 | 2025-06-17 04:36:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 757449d5-0e5d-3fe0-a085-fe6db6439fa4 | -12.42934 | -54.87491 | 2025-06-17 04:36:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d18f325a-8b74-3896-9fbc-af1633d624c2 | -14.86089 | -45.12888 | 2025-06-17 04:36:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f77e625e-1fb1-3154-af49-fdfa1299a0cb | -14.83782 | -48.30273 | 2025-06-17 04:36:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0b2cbf78-79be-3392-a4bd-668cc07c5022 | -10.35759 | -57.22838 | 2025-06-17 04:36:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fec48238-3de4-359d-b204-e27247636e1b | -10.45332 | -47.95061 | 2025-06-17 04:36:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 85989b3e-c789-3076-9feb-e2309bb76242 | -10.96277 | -49.56802 | 2025-06-17 04:36:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3a506feb-b705-3490-9978-d05ae434ba76 | -11.08246 | -55.06029 | 2025-06-17 04:36:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 61f0223f-0306-3815-8e15-efaa459d8e07 | -9.51004 | -55.96376 | 2025-06-17 04:36:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4c1c1583-ea55-32ce-b611-5da55048d12a | -12.02264 | -57.09411 | 2025-06-17 04:36:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 54116a8a-0759-3ff2-9e2f-c24d132a185c | -13.29061 | -57.0716 | 2025-06-17 04:36:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3375f73e-ad08-37e5-8837-a0fe580aef2f | -13.28965 | -57.07676 | 2025-06-17 04:36:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 345126ff-7555-3014-89f4-16649a71fda5 | -11.02977 | -44.64788 | 2025-06-17 04:36:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c79fb4e0-c0e5-3079-9f4e-49b38e109e23 | -10.84451 | -53.78004 | 2025-06-17 04:36:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1cade2e2-db91-3eab-98fb-c122a24e884d | -11.08172 | -55.05786 | 2025-06-17 04:36:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0fff203f-1735-3810-90a1-ba054e7bfc68 | -10.93348 | -56.83156 | 2025-06-17 04:36:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| f4ddd112-6481-35ff-9e88-b783960e99ca | -14.0319 | -55.12058 | 2025-06-17 04:36:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 68cff474-5ef3-3a28-b409-56aa98918853 | -14.84756 | -52.28289 | 2025-06-17 04:36:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d2e518b0-3de8-3219-b729-5cda90b1c9cd | -12.82749 | -47.37493 | 2025-06-17 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9661f397-6a36-3c09-9990-6ce8eccec9aa | -10.24232 | -52.22177 | 2025-06-17 04:36:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 72a019dd-07ec-39f8-9cb4-4a61739f49af | -9.7012 | -49.48279 | 2025-06-17 04:36:00 | NPP-375D | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 74cf4347-b93e-3ed0-99b6-3ba8184a4a3f | -9.511 | -55.96577 | 2025-06-17 04:36:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| df776cfc-3f52-32bc-9fe2-2ebe2f006a94 | -10.29505 | -57.1438 | 2025-06-17 04:36:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 853a1d54-08ac-34c5-b41f-dc79f012b0c0 | -9.51474 | -55.96463 | 2025-06-17 04:36:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4b4cca00-1b50-35df-abae-835627cbe359 | -10.29059 | -60.53471 | 2025-06-17 04:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 04d5e94b-66f5-34c1-b3c5-e3934b00d03a | -12.20861 | -49.63388 | 2025-06-17 04:36:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cf124829-60fc-36ad-b0b7-6f6623e65237 | -10.72503 | -44.88478 | 2025-06-17 04:36:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 544c488b-0148-35d5-bafc-31c1443d251c | -14.23339 | -45.4752 | 2025-06-17 04:36:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 465093b1-07f4-34ef-838b-5a0233dc8897 | -12.0275 | -57.09497 | 2025-06-17 04:36:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 36b5aede-bfe4-3790-a2e5-1faf7c495bc5 | -10.93501 | -55.32673 | 2025-06-17 04:36:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8da2dc5b-79ed-35af-bca5-c4d32c3a76a2 | -11.02634 | -44.64999 | 2025-06-17 04:36:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 73df535c-8def-3555-b4ca-d2a044aa0744 | -10.29231 | -60.54086 | 2025-06-17 04:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2d3cc584-0b6e-3331-8652-6d483194aff9 | -10.28249 | -60.5432 | 2025-06-17 04:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e324e592-f1d8-37a0-a286-372ad7cd307f | -11.14621 | -53.93636 | 2025-06-17 04:36:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 2ed3721e-0f7d-3204-b875-ef10333ae677 | -10.36069 | -57.2317 | 2025-06-17 04:36:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 16b94f6e-db6d-3c11-b6ef-fe86cae23230 | -10.44998 | -47.95008 | 2025-06-17 04:36:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f7bb4308-2120-3d42-9422-81e244654505 | -13.28868 | -57.08197 | 2025-06-17 04:36:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7f2a370f-650e-3781-b7b5-a21a045198dc | -10.2761 | -47.6078 | 2025-06-17 04:36:00 | NPP-375D | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 760353d0-dd44-3186-8050-3b4f29d213e9 | -11.89379 | -47.46993 | 2025-06-17 04:36:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 64954e61-f52e-33aa-9b19-1f1e42ee2c8d | -13.39229 | -48.46015 | 2025-06-17 04:36:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| ace2d746-eb0a-3007-b611-49c9be259898 | -10.87747 | -54.313 | 2025-06-17 04:36:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0a0f8331-c2e9-3e10-a0ab-587969cc15cb | -14.55077 | -53.66679 | 2025-06-17 04:36:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7e04fd9b-a0d2-3c9b-81e7-2b1c01d2fcde | -14.85039 | -52.28749 | 2025-06-17 04:36:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 25e1d7cc-671e-35b1-92fe-99e4b2646ba9 | -12.20584 | -49.62979 | 2025-06-17 04:36:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bb4875a2-4947-3b2b-bc10-da88301a2446 | -11.9198 | -54.81628 | 2025-06-17 04:36:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 369c0de2-6031-3880-99ec-3a3bfa1ad2c7 | -10.52656 | -47.58714 | 2025-06-17 04:36:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 3a31ad7d-5fc2-35fe-b495-a7063ec54e85 | -11.88 | -54.67079 | 2025-06-17 04:36:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| abf524f2-224e-3d11-a869-6375c575040b | -14.84122 | -48.30325 | 2025-06-17 04:36:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 720180fb-0749-3099-8bf1-3896ff1184f7 | -10.95943 | -49.56748 | 2025-06-17 04:36:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 64863689-f6bf-35b7-a4d3-0dd5270c8ea1 | -10.52319 | -47.58661 | 2025-06-17 04:36:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3dc4b8fc-a35e-3f05-8eba-a7e8d25c1934 | -10.28777 | -60.5494 | 2025-06-17 04:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ecf2e0ad-e337-3d44-9191-af5c750bcd51 | -13.36245 | -47.85076 | 2025-06-17 04:36:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ddf7d477-cdaa-3501-8671-9f15395e2e78 | -14.03175 | -44.11665 | 2025-06-17 04:36:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 81cf4742-f82b-33c6-8b23-173336a8bc57 | -16.67999 | -43.88255 | 2025-06-17 04:36:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d831dabc-e5b2-3f8f-b790-c6dd418cb71d | -10.29037 | -60.55059 | 2025-06-17 04:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0c303abf-55b2-33e0-82a9-f62884c2471c | -11.07814 | -55.0529 | 2025-06-17 04:36:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aa523968-f33b-368d-859a-623f0b492018 | -14.02643 | -55.12727 | 2025-06-17 04:36:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b6c44643-84c5-3302-9a0b-554efa988fb1 | -13.38838 | -48.46323 | 2025-06-17 04:36:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7b146c80-8f2e-300d-9910-15f5eee3ce7c | -13.73745 | -53.93577 | 2025-06-17 04:36:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d2cf4c9f-2de6-39e6-a15b-9fc8f704221d | -13.72503 | -58.6844 | 2025-06-17 04:36:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| fc031081-cae2-31ed-a2f6-a298811fedf1 | -14.20966 | -57.41349 | 2025-06-17 04:36:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6127fd91-fd3b-30c0-b159-a508d027d3a5 | -10.36265 | -57.2292 | 2025-06-17 04:36:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 88f63838-d701-3b39-b5e0-4e02ba1dd1ed | -13.71981 | -58.68333 | 2025-06-17 04:36:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 34573512-fe29-31e8-bbfb-e36512d7c259 | -12.1656 | -56.54052 | 2025-06-17 04:36:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 13e1d909-4b3e-3482-93ce-010a8763a485 | -14.81709 | -48.44014 | 2025-06-17 04:36:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e906ee47-3110-3774-a6d6-d41751f1b2a8 | -13.4725 | -46.25383 | 2025-06-17 04:36:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| db6bb5a5-155a-357c-a74c-768e0bf4fbd6 | -10.17148 | -52.62156 | 2025-06-17 04:36:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1957f291-a5cd-301c-abcf-bbbe112a6112 | -9.4619 | -55.93427 | 2025-06-17 04:36:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fa41b737-7056-3a8e-bdcc-6d2855ae2b57 | -10.29614 | -57.13795 | 2025-06-17 04:36:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 63fb492e-9382-318b-a4b5-d4edab06c3a9 | -10.9256 | -56.84705 | 2025-06-17 04:36:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4f6853dc-8f49-3cf2-bcef-2d9b9dead6e0 | -11.081 | -55.062 | 2025-06-17 04:36:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7420af6d-e14a-3c8a-841b-770cc62aaa00 | -14.02778 | -55.11982 | 2025-06-17 04:36:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 448cfff8-654f-351d-8c58-1efeb104b39a | -11.80258 | -43.78302 | 2025-06-17 04:36:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 68561e8d-dc68-38ca-bc5a-520f90aa6d43 | -11.75769 | -46.70834 | 2025-06-17 04:36:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f05c4824-a154-3664-b0db-ec54e124081d | -20.07606 | -47.81612 | 2025-06-17 04:38:00 | NPP-375D | ARAMINA | SÃO PAULO | Brasil | 3503000 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e5f99ee1-790b-3263-a84a-0e7a9fdf28ac | -20.0118 | -45.76152 | 2025-06-17 04:38:00 | NPP-375D | IGUATAMA | MINAS GERAIS | Brasil | 3130309 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 386b47f3-c47c-3fc4-a7e6-4fbbf4fab109 | -20.70565 | -54.89339 | 2025-06-17 04:38:00 | NPP-375D | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3a5dfade-d966-31aa-b06e-d14cd1394239 | -19.0073 | -52.08581 | 2025-06-17 04:38:00 | NPP-375D | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5da736f5-7e06-38ba-843f-03a4c9ad55d8 | -20.8091 | -49.62524 | 2025-06-17 04:38:00 | NPP-375D | NEVES PAULISTA | SÃO PAULO | Brasil | 3532504 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 540fdc42-3e6d-3492-a61c-b3fbf103e63b | -20.23582 | -46.74217 | 2025-06-17 04:38:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 26d9838b-107a-3963-9323-f1b0ae0e09bf | -20.31093 | -45.58378 | 2025-06-17 04:38:00 | NPP-375D | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ce9fd545-9a4c-38b5-8e4e-5aed9dafcb9c | -23.40395 | -46.55648 | 2025-06-17 04:38:00 | NPP-375D | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 0022c86a-cfe1-3b4a-a740-c43b40d67447 | -17.44113 | -52.93344 | 2025-06-17 04:38:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 91c5157a-856c-3de1-bdbd-4008a254553b | -15.57006 | -55.64927 | 2025-06-17 04:38:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 94c174b5-119a-367d-bfad-ef9d1150c407 | -23.59334 | -47.44013 | 2025-06-17 04:38:00 | NPP-375D | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| ec0dd33b-d54a-3d0f-b86f-f613f39bd19f | -19.00792 | -52.08204 | 2025-06-17 04:38:00 | NPP-375D | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ca23792f-1e6e-3610-8913-71bebc6e1bd5 | -21.97322 | -42.80212 | 2025-06-17 04:38:00 | NPP-375D | SAPUCAIA | RIO DE JANEIRO | Brasil | 3305406 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| dc8cce2c-528b-30ab-a007-809e539b5505 | -20.8365 | -50.53609 | 2025-06-17 04:38:00 | NPP-375D | SANTO ANTÔNIO DO ARACANGUÁ | SÃO PAULO | Brasil | 3548054 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| cad63e02-9752-3404-b6f0-93db001ed87d | -16.09131 | -52.08504 | 2025-06-17 04:38:00 | NPP-375D | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 636d002c-9c51-39fa-aa9e-e97128bd647a | -16.59361 | -45.87642 | 2025-06-17 04:38:00 | NPP-375D | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 568969e5-dce6-3aa7-b42b-1407c61f92f6 | -22.77369 | -49.31635 | 2025-06-17 04:38:00 | NPP-375D | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8a4960a4-00e0-3d6b-af92-784a39cc1198 | -20.5784 | -44.5742 | 2025-06-17 04:38:00 | NPP-375D | PASSA TEMPO | MINAS GERAIS | Brasil | 3147709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 23b79157-5887-3836-a1df-db914cc7bcd8 | -20.76474 | -46.77173 | 2025-06-17 04:38:00 | NPP-375D | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| b11c95c3-76ad-3f36-82d2-32de19281e7f | -18.32315 | -49.88337 | 2025-06-17 04:38:00 | NPP-375D | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README16.md)

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

## Dados Diários - Página 218

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6a092ae1-ee17-36f5-b5ae-982ca3879771 | -9.12758 | -45.10456 | 2026-10-07 16:37:00 | NPP-375 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 38.0 |
| 3cd42ab6-a618-31e3-8c16-10a653513398 | -6.32549 | -43.34943 | 2026-10-07 16:37:00 | NPP-375 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 66.2 |
| c8aced1c-4422-3c6e-a8ad-f533144c64a2 | -9.83329 | -44.78753 | 2026-10-07 16:37:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 7e6e25ed-cb09-3368-b3c9-6e8415fcb134 | -6.24232 | -44.34907 | 2026-10-07 16:37:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 6a35f959-843e-3e39-8dec-c9912c1a294a | -7.45954 | -43.20726 | 2026-10-07 16:37:00 | NPP-375 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| f3e10dd3-f8d9-3c73-94c0-55add5b9f4aa | -4.03638 | -48.99545 | 2026-10-07 16:37:00 | NPP-375 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| d147f41b-15b5-3ee1-be8c-4ffea133dbff | -10.24699 | -53.93269 | 2026-10-07 16:37:00 | NPP-375 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ec98ba9d-9506-3593-bb80-36ca3f8c6b16 | -9.11397 | -45.10661 | 2026-10-07 16:37:00 | NPP-375 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 136.2 |
| f71067a0-ba41-3a17-96dc-f07efe7d9d17 | -11.15388 | -46.11907 | 2026-10-07 16:37:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| c193b5f3-8339-392f-81aa-1ec52ad3744c | -17.02316 | -45.90556 | 2026-10-07 16:37:00 | NPP-375 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 32.7 |
| 13e9d92e-3af9-33ff-a88f-f743b99133dd | -5.87264 | -51.16356 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 25691108-1372-3d85-91d7-b67de70786b8 | -7.58361 | -55.01383 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| ac8d61ed-308c-3f69-be0e-764e74ad1c04 | -6.58245 | -53.02655 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 320a6953-b145-3625-8a4c-7521127b05da | -6.60129 | -37.89526 | 2026-10-07 16:37:00 | NPP-375 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 14.4 |
| a1d3088a-b6d8-3dcb-9c42-f01aed61be42 | -6.6917 | -48.20901 | 2026-10-07 16:37:00 | NPP-375 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 8.9 |
| c7bd7738-15db-3763-a430-22dd5325a961 | -7.2039 | -55.11244 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 32.8 |
| 69808983-165c-3788-a8fa-b9529a63a06d | -11.08617 | -45.64347 | 2026-10-07 16:37:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 690e2ac1-1a4a-3e53-b1a0-de491b74d830 | -8.21408 | -46.34379 | 2026-10-07 16:37:00 | NPP-375 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 36.6 |
| 081561ad-eb87-3d1c-9dee-f08a11639b76 | -6.05224 | -53.49248 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 54dd42af-e4d8-3f84-b452-025f30f0d6e8 | -5.93145 | -53.5071 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 95580d9d-a02b-3c3e-ac3a-108bd8ea6986 | -3.95016 | -41.55181 | 2026-10-07 16:37:00 | NPP-375 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 51.9 |
| 988c7abf-91a2-3f44-854c-95a719f1cff5 | -6.15125 | -52.65874 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 71c218dd-96db-31e5-94a2-5b8e66ebe8f9 | -6.81549 | -52.86221 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bb810427-f365-3ffc-8531-8ccf24084074 | -10.23273 | -46.66668 | 2026-10-07 16:37:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| d4171c85-346c-3a5a-a524-1912a330650c | -5.96561 | -46.37734 | 2026-10-07 16:37:00 | NPP-375 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 9cbcad69-cd54-3950-9fa0-32f40a911106 | -6.23219 | -52.65815 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 5c4fcdb2-f871-35af-b410-fb36b24551e0 | -15.92372 | -47.37379 | 2026-10-07 16:37:00 | NPP-375 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 9.0 |
| c6992943-f208-371f-b928-6d75a36d9e87 | -7.79776 | -39.54803 | 2026-10-07 16:37:00 | NPP-375 | SERRITA | PERNAMBUCO | Brasil | 2614006 | 26 | 33 | nan | nan | nan | Caatinga | 58.2 |
| b35dbf01-b944-3af8-9309-840f2e4b441a | -11.06359 | -45.80632 | 2026-10-07 16:37:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 30.9 |
| d5ca8287-8f6d-3879-9017-944e9f82fd6d | -6.2005 | -40.80822 | 2026-10-07 16:37:00 | NPP-375 | PARAMBU | CEARÁ | Brasil | 2310308 | 23 | 33 | nan | nan | nan | Caatinga | 88.1 |
| e9a1c223-ff63-368a-a0e8-b34713bc168c | -7.80663 | -45.50161 | 2026-10-07 16:37:00 | NPP-375 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 07b457d2-1f19-3c6e-96da-c00b5dbbd0fb | -6.21331 | -52.78618 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 63f7fa74-2776-3846-8375-5c90af13e848 | -15.72132 | -40.6981 | 2026-10-07 16:37:00 | NPP-375 | MATA VERDE | MINAS GERAIS | Brasil | 3140555 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 470ec260-9b29-38ed-abf6-aeb4de1e8c3f | -6.60771 | -37.8805 | 2026-10-07 16:37:00 | NPP-375 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 32bcc9b9-c9ec-3f1d-8c8c-cef400ce7ff6 | -6.5776 | -53.03058 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| efe05408-fd0f-3656-834f-8acca2228ce8 | -7.30152 | -37.54228 | 2026-10-07 16:37:00 | NPP-375 | MÃE D'ÁGUA | PARAÍBA | Brasil | 2508703 | 25 | 33 | nan | nan | nan | Caatinga | 5.6 |
| c922d874-ee28-375a-9de9-39ec3d90457e | -10.88904 | -46.66556 | 2026-10-07 16:37:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 0da43e66-c882-3510-9b20-91d7d701c896 | -8.46768 | -51.50282 | 2026-10-07 16:37:00 | NPP-375 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 3564e036-af39-35a3-8889-39e7b473fde1 | -7.92905 | -54.74981 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| fc6ced1e-028e-356f-8ab4-d438266fbbb4 | -6.83005 | -50.35144 | 2026-10-07 16:37:00 | NPP-375 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 96d55d51-bb98-3a4c-8259-2a21b6bc4e1e | -7.12628 | -43.91434 | 2026-10-07 16:37:00 | NPP-375 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 81da2d71-3257-3f43-b3a2-c69a0565be63 | -8.96424 | -47.57567 | 2026-10-07 16:37:00 | NPP-375 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 1dee2d8f-5549-3b6a-b8d4-f6e05e1cfde0 | -8.3897 | -36.72857 | 2026-10-07 16:37:00 | NPP-375 | PESQUEIRA | PERNAMBUCO | Brasil | 2610905 | 26 | 33 | nan | nan | nan | Caatinga | 19.2 |
| 17196760-225e-3d30-995a-3b51c9dc6bff | -10.88131 | -46.67895 | 2026-10-07 16:37:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 500c4c32-045b-376b-aac7-b83659ec61ff | -10.3581 | -46.24976 | 2026-10-07 16:37:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 66766ce6-9ea2-3294-9cb7-a08fc060192a | -17.03456 | -45.91632 | 2026-10-07 16:37:00 | NPP-375 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 674d2251-bd91-306c-b8c3-5652126a4869 | -6.59492 | -41.5517 | 2026-10-07 16:37:00 | NPP-375 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 10.5 |
| e1a7cda9-4555-3b10-adb1-9dc65f3d0838 | -8.26123 | -54.67658 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 604632ab-32f0-34bc-ba5e-9265f6cfdecb | -6.93403 | -38.29856 | 2026-10-07 16:37:00 | NPP-375 | NAZAREZINHO | PARAÍBA | Brasil | 2510006 | 25 | 33 | nan | nan | nan | Caatinga | 7.7 |
| dab2af57-3fdf-30ab-bf01-7ab23995a71e | -5.96917 | -41.35503 | 2026-10-07 16:37:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 10.1 |
| d9ae8896-acd0-3e3b-98e8-7acaf6951179 | -7.17564 | -47.79665 | 2026-10-07 16:37:00 | NPP-375 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 43.2 |
| 9186a1ad-1d4f-31de-a221-b2b29fc47cf6 | -4.63017 | -48.85499 | 2026-10-07 16:37:00 | NPP-375 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 751c342c-cc3b-3e01-99ae-4a5f139a5027 | -8.55776 | -47.24355 | 2026-10-07 16:37:00 | NPP-375 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 27.1 |
| 082d6c5e-3a89-3ce4-88b5-3a5537e5df32 | -6.47798 | -52.81145 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 0a44b402-0859-3ab8-8323-de483af85f86 | -10.98792 | -45.41092 | 2026-10-07 16:37:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 24.8 |
| be073755-f672-3849-a980-d906a4cfa3ad | -7.71473 | -45.44413 | 2026-10-07 16:37:00 | NPP-375 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 8f21a8e0-c679-3217-be84-e3c23451632c | -7.2241 | -44.29322 | 2026-10-07 16:37:00 | NPP-375 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ef8bb0ba-d6c3-3293-b510-67fb744df7bd | -9.11737 | -45.10609 | 2026-10-07 16:37:00 | NPP-375 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 26.1 |
| b4da067b-4f1f-397a-aa2e-7a0d28545380 | -8.58584 | -45.67506 | 2026-10-07 16:37:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 977a2e6a-c046-38dc-a669-4a03e48358fa | -10.99713 | -45.47401 | 2026-10-07 16:37:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 460fd5c1-8c2d-38d1-9f0e-03dc6e6c5f02 | -7.76094 | -43.82 | 2026-10-07 16:37:00 | NPP-375 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 13c0d303-81e5-36fd-9695-fd69e03d8425 | -5.72355 | -41.74295 | 2026-10-07 16:37:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 10.6 |
| 038e15c9-f115-3474-b04b-3cdcad35bdf5 | -15.96936 | -40.70044 | 2026-10-07 16:37:00 | NPP-375 | BANDEIRA | MINAS GERAIS | Brasil | 3105202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.9 |
| a4934ec1-ece3-3654-8d0b-c67b0dded55c | -7.27757 | -45.57438 | 2026-10-07 16:37:00 | NPP-375 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 3424ca13-6e4a-3c4a-94bc-af2f3a556395 | -6.62597 | -37.88259 | 2026-10-07 16:37:00 | NPP-375 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 17.9 |
| 84dfb3b9-1ae2-3deb-b08f-8b548fffb29c | -7.11488 | -55.72636 | 2026-10-07 16:37:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 1912c9bc-d7a5-30d4-af8a-ff0f9d080f59 | -16.19208 | -44.45318 | 2026-10-07 16:37:00 | NPP-375 | BRASÍLIA DE MINAS | MINAS GERAIS | Brasil | 3108602 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 3b78d24e-3896-312f-85b5-01fef9ee31ce | -6.04366 | -42.59477 | 2026-10-07 16:37:00 | NPP-375 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 17.3 |
| 08a4badf-5a08-3917-be84-a3f4a3aca890 | -5.96532 | -40.94811 | 2026-10-07 16:37:00 | NPP-375 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 41.8 |
| 3d63a3a0-7c06-3513-9e0b-c7b023d75174 | -3.915 | -38.62104 | 2026-10-07 16:37:00 | NPP-375 | MARACANAÚ | CEARÁ | Brasil | 2307650 | 23 | 33 | nan | nan | nan | Caatinga | 3.4 |
| ffe7f75e-3852-31b3-8e3f-5ab502036a6a | -10.88224 | -46.67104 | 2026-10-07 16:37:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 21.2 |
| fd9bedd7-0ecf-3c13-898a-7cd8faafe0f6 | -6.04983 | -53.47567 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| ecb127bc-91d7-301d-b07d-193b81e97e60 | -11.38527 | -46.70038 | 2026-10-07 16:37:00 | NPP-375 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 037aba64-69c4-3959-a60c-b67cb3f30495 | -6.462 | -55.47446 | 2026-10-07 16:37:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 6d501cc8-fb51-349a-93f8-affe3c3cd9ae | -7.1055 | -45.24374 | 2026-10-07 16:37:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5944f54e-aab2-3224-a023-7c6a4213525f | -5.68267 | -53.49046 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| ba503cf7-5d9f-3d0f-93f7-243103690638 | -5.8448 | -53.57233 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 66eae580-a094-322f-8890-9d9f1944873e | -10.34367 | -46.25175 | 2026-10-07 16:37:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 31.1 |
| bcc18dea-b94d-3831-8a39-55073578d664 | -9.4057 | -36.68129 | 2026-10-07 16:37:00 | NPP-375 | PALMEIRA DOS ÍNDIOS | ALAGOAS | Brasil | 2706307 | 27 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 01c3e7a8-18a8-3379-85b5-cbe750e4f144 | -4.06068 | -42.22192 | 2026-10-07 16:37:00 | NPP-375 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 32.6 |
| 34e8ae8f-a7eb-3c19-a756-03e0462912d1 | -5.72985 | -45.15812 | 2026-10-07 16:37:00 | NPP-375 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 78.3 |
| baa89dd8-d4ca-3b1f-a968-d107a73dcaeb | -7.17574 | -47.79893 | 2026-10-07 16:37:00 | NPP-375 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 43.6 |
| 55ab2485-d822-324a-8935-402f12200e80 | -6.10628 | -55.68988 | 2026-10-07 16:37:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 44.7 |
| d9b81a06-70eb-3381-9031-0ffae62b67df | -7.00242 | -44.05781 | 2026-10-07 16:37:00 | NPP-375 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 29.6 |
| 769331c4-ac3d-3850-aaa5-bb70677af7a2 | -5.7724 | -38.56046 | 2026-10-07 16:37:00 | NPP-375 | JAGUARIBE | CEARÁ | Brasil | 2306900 | 23 | 33 | nan | nan | nan | Caatinga | 19.1 |
| 5ac67717-44f1-3e98-8138-30237480ffb3 | -4.79834 | -43.22704 | 2026-10-07 16:37:00 | NPP-375 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 5bb93a0a-87db-3e19-9678-36d60a8a171d | -7.46233 | -43.20324 | 2026-10-07 16:37:00 | NPP-375 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| bb1c2b53-8fc4-303e-9906-b0aef0c091de | -6.23074 | -53.14588 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 435911e1-68a2-3673-9676-b224a337f893 | -8.55169 | -40.28198 | 2026-10-07 16:37:00 | NPP-375 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 45.3 |
| 45131524-175b-339a-995e-35a456fa7f80 | -3.70697 | -40.83411 | 2026-10-07 16:37:00 | NPP-375 | FRECHEIRINHA | CEARÁ | Brasil | 2304509 | 23 | 33 | nan | nan | nan | Caatinga | 12.9 |
| a6801cf2-a621-3f25-8d05-0cba9208987b | -11.66402 | -51.53474 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c737d5ef-6ab3-3117-bc66-66339dd9b5ac | -6.46071 | -55.4648 | 2026-10-07 16:37:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 25.3 |
| a449254d-9f13-3531-93ae-94afea0193b6 | -11.10547 | -45.67737 | 2026-10-07 16:37:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| b7c2db79-b9ab-3a6c-802c-78bf35cad632 | -11.057 | -45.86105 | 2026-10-07 16:37:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 8d3d2e99-8173-3ee0-b0e6-df743d65f727 | -5.21726 | -37.3692 | 2026-10-07 16:37:00 | NPP-375 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 20.7 |
| d58d5592-c195-3db5-ba9a-0b7a9dd6f3fd | -11.04282 | -45.81329 | 2026-10-07 16:37:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 7013f0d5-b863-302c-8101-2e4b116d4c3c | -5.01152 | -38.81884 | 2026-10-07 16:37:00 | NPP-375 | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 4.2 |
| b34705e2-a98a-3692-9024-7261ed6aaa00 | -8.65751 | -54.56342 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| a1eebb4f-162d-34b5-8b5e-5f1d75e52a98 | -6.14708 | -53.47952 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 9388422d-5a3a-3842-8f78-7433db0ecc4c | -14.82782 | -40.83654 | 2026-10-07 16:37:00 | NPP-375 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |


[Clique aqui para ver as próximas entradas](README219.md)

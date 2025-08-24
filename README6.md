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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 72f18637-4520-3d27-99c4-725886507e0e | -13.4955 | -47.022202 | 2025-08-24 00:34:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 62afbe59-3115-3a28-8a34-e19fb3c756a2 | -20.961399 | -42.872299 | 2025-08-24 00:34:00 | METOP-C | SÃO GERALDO | MINAS GERAIS | Brasil | 3161502 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c674db27-0fa4-3610-89a1-ef0cff388e11 | -3.5891 | -47.529598 | 2025-08-24 00:34:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8a823eab-12a8-3083-991c-f024b33c2356 | -12.7181 | -48.125999 | 2025-08-24 00:34:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 03d3f324-ffda-3623-a018-cfd622ef12e8 | -8.1085 | -47.139301 | 2025-08-24 00:34:00 | METOP-C | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 00ad43e7-cf77-3fea-b6da-7a93f25ae6b9 | -15.9664 | -43.014702 | 2025-08-24 00:34:00 | METOP-C | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 38c81ca5-8fa5-313d-a33b-bd7108fe0c9f | -14.8208 | -55.957199 | 2025-08-24 00:34:00 | METOP-C | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 37815bbd-064f-3681-b438-ce63286a7b40 | -3.7813 | -47.558201 | 2025-08-24 00:34:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9b78c212-5327-3728-865c-b846209ed69d | -6.3583 | -45.574699 | 2025-08-24 00:34:00 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 214cbc8b-4226-343a-ab36-a864db0c4fe8 | -9.0245 | -47.640598 | 2025-08-24 00:34:00 | METOP-C | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d446946a-9267-3bc1-a52d-295ceceb841c | -5.4173 | -44.987999 | 2025-08-24 00:34:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f4718d8e-ae36-34b8-86d5-391fd70291f9 | -17.393 | -42.616501 | 2025-08-24 00:34:00 | METOP-C | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| b833fabe-bad9-3181-ad37-f0b6be589aa2 | -17.3832 | -42.618999 | 2025-08-24 00:34:00 | METOP-C | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| d7d11a9c-9822-3c54-9061-530117941266 | -18.7115 | -40.0177 | 2025-08-24 00:34:00 | METOP-C | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ed998483-5c2c-37c0-9c92-025e97b701da | -22.070999 | -53.743801 | 2025-08-24 00:34:00 | METOP-C | ANGÉLICA | MATO GROSSO DO SUL | Brasil | 5000856 | 50 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d63580b4-bc3d-39b6-88f2-6d6d435e86f8 | -4.7852 | -45.332199 | 2025-08-24 00:34:00 | METOP-C | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3811d43c-14da-3e11-b54e-1bd01f47fe7d | -13.0988 | -44.1021 | 2025-08-24 00:34:00 | METOP-C | CANÁPOLIS | BAHIA | Brasil | 2906105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 41b60b91-5c8f-3fb6-9c62-517c43e6c947 | -5.661 | -45.147999 | 2025-08-24 00:34:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e5529985-e50d-3774-910e-2f24c8bbf3aa | -23.356001 | -45.803398 | 2025-08-24 00:34:00 | METOP-C | SANTA BRANCA | SÃO PAULO | Brasil | 3546009 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 232c2dd8-aa7a-39ff-aeb9-f332504f49dc | -6.0316 | -43.993698 | 2025-08-24 00:34:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 93ab1911-da42-348d-821e-e85ca1066ef8 | -6.9143 | -52.8452 | 2025-08-24 00:34:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0385bd04-4207-30a0-b4fd-8218f93affa3 | -23.3318 | -47.8545 | 2025-08-24 00:34:00 | METOP-C | TATUÍ | SÃO PAULO | Brasil | 3554003 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| bff83ab4-2673-35ad-abc9-1dfd123ff6cf | -3.5958 | -47.513699 | 2025-08-24 00:34:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f4b63d0c-3f74-38be-8462-ae8e81d12a76 | -23.471001 | -46.813099 | 2025-08-24 00:34:00 | METOP-C | SANTANA DE PARNAÍBA | SÃO PAULO | Brasil | 3547304 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 123fbe99-3a13-3528-8600-19efa12bed27 | -13.4972 | -47.029701 | 2025-08-24 00:34:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 50f54f4d-fc1b-3c30-8a5e-1aa313fb53d0 | -23.625 | -46.028702 | 2025-08-24 00:34:00 | METOP-C | BIRITIBA MIRIM | SÃO PAULO | Brasil | 3506607 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8806cf62-f23c-3d62-a729-4b07215cd2ab | -5.5772 | -45.811298 | 2025-08-24 00:34:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1391dedd-06ec-3314-aab3-2ba48a781a33 | -2.911 | -48.306702 | 2025-08-24 00:34:00 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b7a6da23-1eb8-3830-8099-05c06b35cac3 | -9.5702 | -47.965401 | 2025-08-24 00:34:00 | METOP-C | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b6c05022-2b8d-3105-8dc7-04989eb051d6 | -7.1786 | -44.6614 | 2025-08-24 00:34:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4291e98e-37e2-3d7b-ac64-8bedd58c8b79 | -13.333 | -43.197601 | 2025-08-24 00:34:00 | METOP-C | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| ebce6941-c99b-3e37-be22-b9d650314a36 | -3.5876 | -47.522701 | 2025-08-24 00:34:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1a64c534-4bb3-350f-b51a-68f923d9603d | -11.2864 | -44.973202 | 2025-08-24 00:34:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b81a0402-e60c-39a9-931e-ed387cc1eda8 | -7.0751 | -44.615398 | 2025-08-24 00:34:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6da2bf48-f449-39ef-8ee5-119d99bed2cd | -8.7596 | -46.737701 | 2025-08-24 00:34:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7807f52f-96c0-3767-a054-62c1d1af79c4 | -6.3568 | -45.523102 | 2025-08-24 00:34:00 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 01500cd2-8cfc-3a02-994b-c7c4c1541947 | -8.7127 | -51.133701 | 2025-08-24 00:34:00 | METOP-C | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 24130b33-ce2c-3f23-9a56-24fd874a5a62 | -11.4214 | -47.594398 | 2025-08-24 00:34:00 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 527796c2-35e3-3a3f-ab19-44cef3924ae9 | -3.5157 | -47.209499 | 2025-08-24 00:34:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f2c8a4de-c615-3b0a-b6a8-6c64f7778ca7 | -11.5322 | -51.921001 | 2025-08-24 00:34:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 316b1313-7421-36b2-b9cd-fdf0ddc2984f | -6.1228 | -44.383598 | 2025-08-24 00:34:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a63a4c97-8291-3359-9680-2aa9aaaf1fb9 | -19.629 | -43.187 | 2025-08-24 00:34:00 | METOP-C | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2339e6d2-450c-32fe-b747-0705c406383f | -6.1917 | -45.434399 | 2025-08-24 00:34:00 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4914b3df-587c-3068-b4e2-f5ea87bbf995 | -10.4141 | -47.179501 | 2025-08-24 00:34:00 | METOP-C | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a5d6c758-bfbc-3508-93ba-27be71f86d3d | -17.6091 | -44.297901 | 2025-08-24 00:34:00 | METOP-C | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| fd9239ae-461c-39b3-9dc5-ea7705d8062b | -10.629 | -47.359299 | 2025-08-24 00:34:00 | METOP-C | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fe8a921a-c4aa-3003-8988-97c2e53db58d | -22.1413 | -43.649899 | 2025-08-24 00:34:00 | METOP-C | RIO DAS FLORES | RIO DE JANEIRO | Brasil | 3304508 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7988a4f3-092b-35f2-9be3-933c57c61277 | -14.804 | -47.955601 | 2025-08-24 00:34:00 | METOP-C | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 547129e8-e065-3f21-9616-67a28ad88d6f | -15.2368 | -48.213001 | 2025-08-24 00:34:00 | METOP-C | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 4ffe5a81-6dda-3e52-ac43-472cf90c4823 | -17.8291 | -44.547501 | 2025-08-24 00:34:00 | METOP-C | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 687d686e-c472-3edc-8026-fb2affe31459 | -7.018 | -44.636299 | 2025-08-24 00:34:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7a214012-75c5-3c30-acda-320d14a8ce3d | -10.4027 | -47.1745 | 2025-08-24 00:34:00 | METOP-C | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c112dcb2-6def-3925-b5e9-ce90998b1122 | -6.6043 | -48.0508 | 2025-08-24 00:34:00 | METOP-C | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 9f32a6f5-90c0-35c9-a52f-4684d9bbb19e | -17.048599 | -47.181599 | 2025-08-24 00:34:00 | METOP-C | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| f210af41-c035-31d3-96f5-670e141b3769 | -23.115101 | -47.295101 | 2025-08-24 00:34:00 | METOP-C | INDAIATUBA | SÃO PAULO | Brasil | 3520509 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 28a52cbf-f2e8-397a-b662-9b760e80f204 | -15.2386 | -48.221802 | 2025-08-24 00:34:00 | METOP-C | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 99143c09-9469-309c-9d2d-6e6da7affcbc | -20.344101 | -51.7001 | 2025-08-24 00:34:00 | METOP-C | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 1d711eb4-e8d8-3bca-9c0c-e046abe21b9b | -10.6105 | -44.324402 | 2025-08-24 00:34:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 67688d72-3fb0-39d1-bddd-8c4ebb74b92d | -7.0346 | -44.663502 | 2025-08-24 00:34:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6a861ec1-0233-3928-8d3c-3c57de696f9c | -20.3636 | -51.6964 | 2025-08-24 00:34:00 | METOP-C | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 4f0ad937-2e62-3510-8da6-40837689ebc5 | -22.069099 | -53.795601 | 2025-08-24 00:34:00 | METOP-C | ANGÉLICA | MATO GROSSO DO SUL | Brasil | 5000856 | 50 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 042059af-1d4d-30a4-86ba-4f55954a0c48 | -10.597 | -50.184502 | 2025-08-24 00:34:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3ee26a99-82b0-3914-ab2f-a6b763e50fb4 | -17.3965 | -42.6315 | 2025-08-24 00:34:00 | METOP-C | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| a488a522-d995-3a6a-9ffe-ecb7616e9d1e | -6.6125 | -48.0415 | 2025-08-24 00:34:00 | METOP-C | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 34d31534-a541-3a32-ad50-d6428a178b31 | -11.1075 | -44.778301 | 2025-08-24 00:34:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 82ebacf5-550d-3e44-9490-6e3905fb0312 | -4.5527 | -43.232498 | 2025-08-24 00:34:00 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 768cd6c6-6efe-3387-b2b0-1f42d5ac2654 | -20.3538 | -51.698299 | 2025-08-24 00:34:00 | METOP-C | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| b5bb4d22-7545-3b65-a5b8-7b1720c16683 | -5.4058 | -44.982899 | 2025-08-24 00:34:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 016ec2ec-9c7e-3673-b2d6-06be4aebf12a | -23.124901 | -47.292999 | 2025-08-24 00:34:00 | METOP-C | INDAIATUBA | SÃO PAULO | Brasil | 3520509 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d2532a69-363a-3ecf-ae1f-1b5483bacb5d | -12.7296 | -48.132 | 2025-08-24 00:34:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6f9f40a4-225b-3853-9fa1-17c2bc5cf4b2 | -8.7643 | -46.758499 | 2025-08-24 00:34:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ee9beab6-d4ba-36b4-930f-7efb01221c7a | -18.7544 | -45.1119 | 2025-08-24 00:34:00 | METOP-C | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| e19f3da3-1624-301b-84cb-14c371e8b1c6 | -2.9297 | -53.701199 | 2025-08-24 00:34:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| adfd3b95-2ff1-3926-8a51-17e342ea3a9f | -7.2636 | -43.6572 | 2025-08-24 00:34:00 | METOP-C | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 9da7caaa-f78d-3c0d-be85-3a2c58da7a08 | -12.7342 | -48.1054 | 2025-08-24 00:34:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1ef658fb-685c-367b-8694-05db947fe62c | -4.8156 | -43.5611 | 2025-08-24 00:34:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 56d9bac8-cb29-32b1-a8c3-a38071d172f6 | -21.2784 | -43.751301 | 2025-08-24 00:34:00 | METOP-C | BARBACENA | MINAS GERAIS | Brasil | 3105608 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3c6527b3-ba59-3581-854f-acc342aa86db | -8.8431 | -49.8908 | 2025-08-24 00:34:00 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bacf3b17-5f14-3180-ba30-9b245de2b295 | -5.587 | -45.808998 | 2025-08-24 00:34:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5604d878-9b0e-3c52-a247-4dc162be628d | -12.7359 | -48.113602 | 2025-08-24 00:34:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 94a77e70-d50d-3613-b200-cbd21721d177 | -14.165 | -43.666302 | 2025-08-24 00:34:00 | METOP-C | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 42cfc1a0-7ef1-3dc4-85ce-4a3caa58d75a | -11.5296 | -51.908001 | 2025-08-24 00:34:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5df7df65-076e-35b7-83d0-23fb73a1dcb3 | -9.0327 | -47.631199 | 2025-08-24 00:34:00 | METOP-C | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b8fa6ddc-4a91-3c9f-9aa7-22d23d2048b0 | -22.101999 | -53.815899 | 2025-08-24 00:34:00 | METOP-C | ANGÉLICA | MATO GROSSO DO SUL | Brasil | 5000856 | 50 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e2d07796-c48f-3fb3-bc04-96ec33bb5468 | -8.0622 | -49.652302 | 2025-08-24 00:34:00 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 84f2cc3f-55e8-32a1-bf3b-5e4d60c21b0c | -9.8314 | -47.751999 | 2025-08-24 00:34:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d3574e26-10ed-3bf7-9f2d-3e14ba50ce74 | -7.6033 | -45.245701 | 2025-08-24 00:34:00 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| ac197ebb-a211-3a04-920a-ca3f40c98648 | -22.0788 | -53.7939 | 2025-08-24 00:34:00 | METOP-C | ANGÉLICA | MATO GROSSO DO SUL | Brasil | 5000856 | 50 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b9f0620b-724b-3952-9873-0589ede6ef6a | -12.5471 | -45.621101 | 2025-08-24 00:34:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c262ba54-d3c9-3af6-91d4-5a47aeb5cbf2 | -18.7626 | -45.1022 | 2025-08-24 00:34:00 | METOP-C | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| c19ecad0-360b-3cd3-82ac-87b2adc84478 | -5.8474 | -52.080601 | 2025-08-24 00:34:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 33d19b8f-f5b6-319e-96ae-9c7cd9bd78d6 | -14.7924 | -47.949299 | 2025-08-24 00:34:00 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 3152a194-6021-34a9-9e64-915559f90fbc | -20.945999 | -46.833801 | 2025-08-24 00:34:00 | METOP-C | SÃO SEBASTIÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3164704 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| e74d5365-8fe2-3673-8bc9-3798046ea6fa | -8.536 | -48.866501 | 2025-08-24 00:34:00 | METOP-C | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| de8593f1-fed3-3c21-9475-9a994a8f3dab | -5.5267 | -36.8535 | 2025-08-24 00:34:00 | METOP-C | IPANGUAÇU | RIO GRANDE DO NORTE | Brasil | 2404705 | 24 | 33 | nan | nan | nan | Caatinga | nan |
| 34821873-b263-3c82-aae0-bfe163bd7f49 | -22.0884 | -53.792301 | 2025-08-24 00:34:00 | METOP-C | ANGÉLICA | MATO GROSSO DO SUL | Brasil | 5000856 | 50 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 438cfca3-5228-3982-aa1d-0ab9afff765b | -20.9695 | -42.862499 | 2025-08-24 00:34:00 | METOP-C | SÃO GERALDO | MINAS GERAIS | Brasil | 3161502 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 912c3d40-cee7-35c3-a143-e75718809289 | -6.8773 | -45.677399 | 2025-08-24 00:34:00 | METOP-C | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e6a30d68-7c9d-3afe-b7d3-2b4cd1daf24f | -13.0344 | -45.222099 | 2025-08-24 00:34:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 416eae0e-f2e9-3f17-92f2-114a8468ef11 | -13.0571 | -45.231602 | 2025-08-24 00:34:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README7.md)

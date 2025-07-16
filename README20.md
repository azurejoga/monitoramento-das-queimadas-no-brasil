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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| df302770-a939-323e-8ba3-e002caf4c81e | -22.25514 | -50.04115 | 2025-07-16 04:19:00 | NOAA-20 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 1710fc41-6547-3608-8258-13373fad29bc | -22.82901 | -42.06626 | 2025-07-16 04:19:00 | NOAA-20 | SÃO PEDRO DA ALDEIA | RIO DE JANEIRO | Brasil | 3305208 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 6e589844-9933-345c-828a-d80287100951 | -22.64144 | -47.38479 | 2025-07-16 04:19:00 | NOAA-20 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1b902bf2-9846-34f6-b05a-af49c3f5abcc | -28.76527 | -55.54418 | 2025-07-16 04:19:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 12.7 |
| d60fe183-6a00-399c-a442-8d0182be3b5c | -22.9054 | -49.69168 | 2025-07-16 04:19:00 | NOAA-20 | SANTA CRUZ DO RIO PARDO | SÃO PAULO | Brasil | 3546405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 597f962e-eae0-3acc-b9fe-0bd5eba2fdbb | -20.99063 | -49.76976 | 2025-07-16 04:19:00 | NOAA-20 | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 4efe1ebd-a568-382a-aa4d-bd1aaa99b323 | -28.76197 | -55.53845 | 2025-07-16 04:19:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 5.4 |
| 5519f3e2-8693-39bb-9470-ce73b42847b3 | -13.0146 | -45.0593 | 2025-07-16 04:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 82214db9-af93-32f7-b4f7-92249fae5fac | -9.4383 | -40.3668 | 2025-07-16 04:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 85.1 |
| 993d4a3f-ca03-3262-8452-629aaf79ba24 | -23.1204 | -50.0244 | 2025-07-16 04:20:00 | GOES-19 | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 151.9 |
| 79932e69-b00c-3ff1-8c03-a50ce5c0a15f | -13.0339 | -45.0561 | 2025-07-16 04:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 55.5 |
| b3a3ce53-b090-332c-a73b-54194170cf28 | -23.1414 | -50.0193 | 2025-07-16 04:20:00 | GOES-19 | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 107.1 |
| c1e996ac-3536-33d2-9e43-c14842a2a31a | -13.0146 | -45.0593 | 2025-07-16 04:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 73.2 |
| fcc83902-5c79-3483-b3fc-f2c4ad4a1ae1 | -13.0146 | -45.0593 | 2025-07-16 04:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 53d4a524-8cfc-38f0-bb0e-340e05eab51e | -13.0146 | -45.0593 | 2025-07-16 04:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 75.1 |
| f2e75b94-efde-359e-98c4-32c6586ae791 | -13.0146 | -45.0593 | 2025-07-16 05:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 65.3 |
| dc880286-00de-3a34-878e-a424c7c65b59 | 0.79005 | -51.96757 | 2025-07-16 05:01:00 | NOAA-21 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 48a4fe0c-1216-3698-9721-96dc1a1cb504 | -7.94837 | -49.65829 | 2025-07-16 05:04:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 40d8a4ff-1847-387d-8c04-d59e32295665 | -7.3152 | -45.76804 | 2025-07-16 05:04:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8cb89092-e5ac-3663-a5f4-f157dbf7c30d | -7.83887 | -44.19824 | 2025-07-16 05:04:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 6836b3c2-802a-3f67-ad4b-4cd6838c313a | -7.90233 | -55.42029 | 2025-07-16 05:04:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2a69f020-822c-3cf9-81d5-b9f1ca2b7098 | -7.18978 | -43.12034 | 2025-07-16 05:04:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| dcb0bb32-e876-3abe-a90f-b57d0967c256 | -5.46446 | -45.33875 | 2025-07-16 05:04:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ac1b057f-021c-321c-b8d1-08237b9cebd3 | -8.54378 | -47.85046 | 2025-07-16 05:04:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ddc88f14-0d43-3b76-9295-50289cdea9f8 | -8.65125 | -47.7474 | 2025-07-16 05:04:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7cadfd84-5815-3c7d-9137-f24b15432d40 | -8.9133 | -47.34147 | 2025-07-16 05:04:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5059c734-f71e-3e7e-8cc4-e2586ca189b1 | -6.62875 | -56.28218 | 2025-07-16 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 32a09a25-ede5-3cc8-a779-79bee23213f8 | -6.71359 | -44.33248 | 2025-07-16 05:04:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 07322557-02e2-37e3-a98e-4d102bb37b09 | -7.90566 | -55.42081 | 2025-07-16 05:04:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4bde6f20-8664-35b4-b911-b9b7d78ab9ed | -9.31228 | -44.84948 | 2025-07-16 05:04:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a73659de-6887-3196-bc1e-1872f0ca1170 | -8.24803 | -44.92462 | 2025-07-16 05:04:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9658af4e-8658-33dc-9a70-f271cebf5cce | -7.45847 | -44.70444 | 2025-07-16 05:04:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ec75775c-a3b7-3370-9e99-dee4b616dbeb | -8.68745 | -51.45507 | 2025-07-16 05:04:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f0441eb6-33b6-3c39-a197-466687c00d1f | -7.83775 | -44.19833 | 2025-07-16 05:04:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 5af73b9e-4680-3827-be15-142c01f76af3 | -6.62821 | -56.28564 | 2025-07-16 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f28b7508-9613-34d6-b3d6-8af78f02ddf2 | -6.13648 | -44.07671 | 2025-07-16 05:04:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0a040516-aede-3ee4-8c35-43e26fc0b9bf | -2.58742 | -51.92117 | 2025-07-16 05:04:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8db05abc-0d14-30cd-951e-a94cad350c50 | -4.11126 | -48.20888 | 2025-07-16 05:04:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4a7086cd-610d-3b99-b725-1b004f64f259 | -6.88341 | -59.32846 | 2025-07-16 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dbf93a4e-d1dd-329f-9595-b563ebd63192 | -7.31467 | -45.77211 | 2025-07-16 05:04:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dec132ac-a6e5-36f9-9afc-a0e3101d6d69 | -3.94901 | -49.01458 | 2025-07-16 05:04:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bf503c3d-7ee2-30fd-bec5-c40f8cdd1f73 | -4.03033 | -48.05777 | 2025-07-16 05:04:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| f78bf778-856f-3a4d-9610-3014ecc5bbde | -2.91674 | -48.2327 | 2025-07-16 05:04:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 290e9dd2-e9d2-33d0-b5c4-91a1022b653a | -8.68498 | -51.45481 | 2025-07-16 05:04:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5a82f1bf-d916-3fd7-b83f-4e86cdae859e | -7.94899 | -49.65394 | 2025-07-16 05:04:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ab195380-608f-34c9-8cc0-e18d6498420a | -9.31857 | -44.85036 | 2025-07-16 05:04:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7784d405-3a06-3f41-9f92-a7cc3a074033 | -8.75837 | -46.60093 | 2025-07-16 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4008d482-1dcf-3ff5-9eb4-b0e2128a722e | -8.54097 | -47.85406 | 2025-07-16 05:04:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 27501412-e08b-3c1a-9701-8c300df24b1a | -8.76395 | -46.60184 | 2025-07-16 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 31fb98ad-6bb2-39bc-8726-053dad3d6175 | -8.54336 | -47.8535 | 2025-07-16 05:04:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0b470ec6-b3b1-39b2-9b5c-6c99b8b94432 | -4.15662 | -50.22614 | 2025-07-16 05:04:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1b1fad15-81ba-32bf-bd04-c5ada583da8f | -3.84445 | -47.75309 | 2025-07-16 05:04:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e2675fc7-68a2-3b10-a23d-15f5d5d8dcc7 | -7.1974 | -43.11498 | 2025-07-16 05:04:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| bc391c44-7918-3d0d-8d0c-d16a1c7fb915 | -4.78079 | -45.34335 | 2025-07-16 05:04:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 0d7f6a4c-8af2-3536-bf64-549476dec777 | -8.75885 | -46.59726 | 2025-07-16 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5523e580-f507-3c9d-b610-c94e01d330f7 | -5.4641 | -45.33809 | 2025-07-16 05:04:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c5fd6bc5-d5c9-37f7-b04e-dd45f073f6b5 | -7.19658 | -43.12133 | 2025-07-16 05:04:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 97848eb1-67e7-3d0d-8193-27e8135ad25c | -6.91218 | -52.85843 | 2025-07-16 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5f411e51-62c0-32db-af01-7a2f781a99eb | -3.66384 | -50.9491 | 2025-07-16 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d42a06d9-77dd-3b2f-bd32-2fdf6beebc18 | -5.72163 | -44.83094 | 2025-07-16 05:04:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7b70e7bd-2d9d-3525-b504-543269332fb1 | -8.64872 | -47.7534 | 2025-07-16 05:04:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8419cd05-96cb-3242-9a30-8c8e34f5e5f2 | -6.83092 | -59.09464 | 2025-07-16 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 967439d8-b804-3a70-b1fc-871e091ebc82 | -8.65431 | -47.75105 | 2025-07-16 05:04:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3f23f647-89ec-38fc-91dd-e13390c0a0f0 | -8.5327 | -47.8551 | 2025-07-16 05:04:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6f07a513-3451-3443-8e92-650b23608b9d | -9.05631 | -49.30404 | 2025-07-16 05:04:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d425f07a-2ef2-32b6-b56a-88d3e124b42e | -4.30207 | -48.10291 | 2025-07-16 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 71a68d00-c1c7-3c2e-a695-df980eb98211 | -3.3834 | -47.49334 | 2025-07-16 05:04:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 79d8e824-3a71-3bf8-9647-14d6f516d90f | -2.91535 | -48.24213 | 2025-07-16 05:04:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 926c8ef3-70a0-398c-99fb-a8ff27c8681c | -6.92004 | -52.8553 | 2025-07-16 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e907caea-e905-3619-ad0c-2bcdcaaf58a6 | -6.63772 | -44.57611 | 2025-07-16 05:04:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6d1636cd-ff92-3497-8b17-2f65deeb5ec1 | -7.21304 | -45.33087 | 2025-07-16 05:04:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 46571348-af3f-3530-bdf6-22c32d363ec1 | -4.03356 | -48.06872 | 2025-07-16 05:04:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 60dea8a7-c1ed-3f89-a8d6-08fd6f6a13fb | -5.46349 | -45.34232 | 2025-07-16 05:04:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f8673d1d-849a-3d5f-8a8b-7d23b39a84cf | -8.65045 | -47.75361 | 2025-07-16 05:04:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f36b58ea-36e0-3d60-89c6-d149779588a2 | -8.5092 | -43.30705 | 2025-07-16 05:04:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 6c27972e-65bc-3893-8733-109f2c87ae85 | -8.53781 | -47.85592 | 2025-07-16 05:04:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c507a1b9-60ef-3c61-bff8-63c9d2d12a46 | -4.58576 | -47.26302 | 2025-07-16 05:04:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ba8033ab-2a64-384b-87dc-ee927cb0fc79 | -7.19058 | -43.11412 | 2025-07-16 05:04:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 70d26559-3f1a-377f-9486-d98bb229d842 | -7.31414 | -45.77108 | 2025-07-16 05:04:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 93681e24-44ce-320b-8a75-540481c33b36 | -7.84426 | -44.19864 | 2025-07-16 05:04:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 23f538f2-e08a-39cc-9c4d-88d302114fc4 | -3.52008 | -48.43747 | 2025-07-16 05:04:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 63d89c55-1364-366d-8a7e-632c9d549920 | -2.28509 | -48.58062 | 2025-07-16 05:04:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b7afe37c-3e76-3d57-a0ef-daa9dcc6551d | -9.30598 | -44.8486 | 2025-07-16 05:04:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| aca67a02-4e16-3925-a316-3a46d7be85f9 | -6.71425 | -44.32746 | 2025-07-16 05:04:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 17f694ee-7e76-3283-9dd2-c950c883c5de | -8.53545 | -47.8564 | 2025-07-16 05:04:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 345adcd8-6023-30ec-8d1d-ab96de7531a0 | -4.5912 | -47.26094 | 2025-07-16 05:04:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 54101484-ec69-3b60-8172-85bc9ba13a68 | -5.79114 | -45.08058 | 2025-07-16 05:04:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 8796c224-d568-318c-93d5-78dc18a98bdf | -4.96617 | -43.22986 | 2025-07-16 05:04:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| b55cf2fa-b83c-37c7-9718-1927cd14872b | -7.50857 | -46.69218 | 2025-07-16 05:04:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a96f838c-bfde-3431-993f-10e839e39f11 | -5.57583 | -46.52912 | 2025-07-16 05:04:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 36d80fec-ea82-37eb-ad20-5786ac2651c7 | -7.90179 | -55.4238 | 2025-07-16 05:04:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f5f041e3-5eca-37a2-8159-2629caa3427c | -8.68343 | -51.45451 | 2025-07-16 05:04:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 88a70e01-3e74-3868-84e1-d11a0c0a4af4 | -3.95262 | -49.44418 | 2025-07-16 05:04:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 19ae918c-a215-35ec-9522-0481a1ed13cc | -6.2672 | -57.40282 | 2025-07-16 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7f7616c0-6da9-38f8-8ea7-b9fa6e7994e8 | -3.38418 | -47.48806 | 2025-07-16 05:04:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ffee16bf-38fb-3be8-89a7-cad94a742bae | -6.90857 | -52.85785 | 2025-07-16 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 183d0899-5aab-383b-9481-e4fd09a3718b | -5.78463 | -45.08391 | 2025-07-16 05:04:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 22fc0c3e-b211-304b-a9af-64955dd6507d | -2.91993 | -48.24282 | 2025-07-16 05:04:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 73acd5f6-2758-3120-bd9e-96782849812f | -5.79648 | -45.08561 | 2025-07-16 05:04:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 88e6fa42-3cef-3c19-8a5e-d49bd478252f | -4.30322 | -48.1045 | 2025-07-16 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |


[Clique aqui para ver as próximas entradas](README21.md)

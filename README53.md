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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 882d8094-dba1-3aa8-ae8f-f4ac3e5d962e | -10.95345 | -50.79803 | 2025-09-03 04:46:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f6d84b97-2b9c-355e-abef-681d62d4dbdb | -11.60778 | -52.11324 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1d6ba4e4-8efc-38be-8ed5-3674c3054a8d | -10.9908 | -46.83031 | 2025-09-03 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 0e1b45b9-951d-3b6b-b3c8-95b64ef5171b | -6.40908 | -43.76184 | 2025-09-03 04:46:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9dabca16-871c-3f50-85a8-3b02ca8ff4f2 | -10.05349 | -48.09085 | 2025-09-03 04:46:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a0ab861b-ef48-3bd5-a8e9-b602c18f9033 | -5.86334 | -57.76411 | 2025-09-03 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| af9fbd76-1f12-398f-9fdf-84697216403c | -9.19652 | -45.19187 | 2025-09-03 04:46:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 22b8767a-5e81-33a3-ad77-141c533053e1 | -6.6796 | -58.86358 | 2025-09-03 04:46:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 623a33fa-4c1c-3dd0-8d9d-337c9b27f02f | -8.38368 | -48.31009 | 2025-09-03 04:46:00 | NOAA-21 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5559c2e8-cc6c-3f71-baa5-93e9c8a46439 | -8.89003 | -45.79756 | 2025-09-03 04:46:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| c5b368d7-01f7-384e-b9a8-b8ccb19eb8a1 | -7.12274 | -43.76284 | 2025-09-03 04:46:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 11809bc1-6285-3e8e-a346-f28ce2b9db56 | -6.94595 | -43.28139 | 2025-09-03 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| d3b875d4-86ce-3a8f-8ea9-1d88ad03123c | -7.69 | -50.27419 | 2025-09-03 04:46:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9378d613-73dd-30ad-8701-e30fcd25486f | -10.48878 | -50.34782 | 2025-09-03 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 62bac3db-e902-3703-9157-df50be17a9c4 | -7.58848 | -49.66203 | 2025-09-03 04:46:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 177ff65a-dc64-34e1-a3f9-d8e6b9bffa42 | -11.62488 | -52.13393 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0e8566d5-7f20-35b8-9099-8603ea176757 | -7.91386 | -46.47877 | 2025-09-03 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4b55541d-2672-37de-b092-08924bd56199 | -11.61388 | -52.13936 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 8cc5f3d5-5d0b-3d19-8633-1a025daf44d0 | -6.47783 | -45.41142 | 2025-09-03 04:46:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 0f5bc3ee-0c63-34ae-aac1-b75a81eb5cb7 | -9.71484 | -48.31274 | 2025-09-03 04:46:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 153e66a0-3937-32ef-a875-b02e9a799694 | -11.00877 | -46.82193 | 2025-09-03 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 72029c99-570d-3650-9a30-eb20ff16a877 | -7.96448 | -46.50764 | 2025-09-03 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 18eb31ee-4a31-3c29-a592-4f114f60efc6 | -9.73946 | -49.4113 | 2025-09-03 04:46:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 18658cc3-6f70-3061-9085-9d045fbf5918 | -6.87515 | -45.56551 | 2025-09-03 04:46:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4f8147bd-43ae-3ffe-8500-b950a3209438 | -5.6906 | -45.94403 | 2025-09-03 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d7842ca1-3c6d-31f0-9d54-f1f4408cd32b | -6.86132 | -52.81866 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 03cc7b02-8faf-3b7a-9f30-8db64fd71de5 | -11.61654 | -52.0787 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ee970ba0-1db2-3db8-b5f3-cf344d29fe8d | -10.99032 | -46.83377 | 2025-09-03 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 4f274093-32b4-3ac4-8e4c-0332ce2879b8 | -7.89835 | -46.44379 | 2025-09-03 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 032c8ed7-a382-36f8-be45-48261f6987f8 | -8.06981 | -45.36995 | 2025-09-03 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a559062c-e2bd-34a7-9f94-7556b2515505 | -9.33223 | -55.21701 | 2025-09-03 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d5075a18-eeb7-39ff-b9d7-22cf4c97c8c6 | -8.88551 | -45.8234 | 2025-09-03 04:46:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d6ab756d-4ee5-3560-bc99-dabe8b49d586 | -11.79873 | -51.49299 | 2025-09-03 04:46:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a897e042-3004-3903-867d-151459d40401 | -10.53625 | -50.43036 | 2025-09-03 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 69c77847-aa47-3962-89bd-d1fc61452a76 | -5.89853 | -57.7471 | 2025-09-03 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 22.4 |
| f300b73f-b531-36cf-bd03-7e22d40d4c21 | -11.59841 | -52.10815 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 69acbc0a-1fa5-344d-b3e1-062ddbecad3c | -6.79677 | -52.80116 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bdac62f0-fa4a-3490-b369-6a3308c2dbc2 | -7.70115 | -48.73701 | 2025-09-03 04:46:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 11.6 |
| c948de84-2e7b-3b64-a1cf-382f13309b3a | -6.16272 | -46.60258 | 2025-09-03 04:46:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a387079c-4759-3408-9dab-bcab8ccbe0ea | -7.11348 | -44.75644 | 2025-09-03 04:46:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| affe5795-f760-3cbd-a5b8-168a7e033559 | -6.27273 | -44.5034 | 2025-09-03 04:46:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 16f01bce-e254-338e-9aee-4972a89ea775 | -6.52929 | -56.20147 | 2025-09-03 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 59f3f898-d601-3f54-bfdc-4a3200864b8d | -10.94048 | -50.76993 | 2025-09-03 04:46:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c79e4928-177d-3123-9553-778e67f53b1e | -6.80457 | -52.81725 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 22147367-512f-344c-b6c3-6b011c1ffdb7 | -5.71259 | -43.10676 | 2025-09-03 04:46:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 824082b7-012a-3505-a9d5-69c2e0a03715 | -6.26127 | -57.89418 | 2025-09-03 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4f53e38f-2af4-37f7-a795-ce806021ea59 | -11.43931 | -46.9139 | 2025-09-03 04:46:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9cd00b1f-3037-3ed2-b981-4dfe4d05006c | -9.63551 | -47.04004 | 2025-09-03 04:46:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| af47aa0b-34e5-3d16-8430-6097bc714fc1 | -8.05626 | -52.35038 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c6b55424-e542-327e-97a3-a7131af237b6 | -6.67751 | -58.76213 | 2025-09-03 04:46:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 64c5a3cd-6101-3a81-ac3c-e8df5dbe09c6 | -6.44051 | -58.14032 | 2025-09-03 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c3c88c0b-a742-3b9b-9e65-9630d3c4d871 | -6.6421 | -44.09924 | 2025-09-03 04:46:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| df11a85a-6420-3e09-b6ad-22d1b7e0ea1e | -7.70958 | -50.25185 | 2025-09-03 04:46:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 29490aa5-b1ec-3ab3-9f9c-060e05ee8d5c | -6.79502 | -58.99428 | 2025-09-03 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 23c5bae1-7093-3932-a714-d4113a5109d9 | -6.85755 | -52.78852 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 862cb01d-599d-31dd-9190-cc11066e3fb4 | -7.92113 | -46.42896 | 2025-09-03 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ebc22bb5-562c-3a7e-a502-c9af8ee3f3cb | -8.08984 | -47.59672 | 2025-09-03 04:46:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| de3aa991-fb77-37c1-8503-1c3a296036ce | -7.23501 | -44.04806 | 2025-09-03 04:46:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8f2d0b73-a390-312a-ad45-828abb34821d | -9.79316 | -56.61328 | 2025-09-03 04:46:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1acc965f-6eb2-37b2-87b8-559544404b47 | -8.02328 | -44.10751 | 2025-09-03 04:46:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ddb25cd2-698e-33c3-940c-f4fd8c85901b | -11.65229 | -52.04487 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3a460d8a-3337-33d1-a40b-2577b7dd2f97 | -6.80342 | -52.82449 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a5ecf806-1944-339e-b9e5-7b862cbd161e | -11.59183 | -52.12865 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 29.9 |
| f101a36d-ce32-3ab0-8a45-361ce00d39f2 | -11.59895 | -52.10464 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 100ccaaf-ce48-3090-ba75-cab2f6949234 | -5.94036 | -46.47935 | 2025-09-03 04:46:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 47dea326-1601-3254-91f7-579510092228 | -10.48763 | -50.33245 | 2025-09-03 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0aed8cab-cfc4-346e-9aa3-ba2b118e37aa | -5.86258 | -57.76855 | 2025-09-03 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| fe8f0a29-b215-3067-95b8-9eafd631a697 | -5.75457 | -46.61768 | 2025-09-03 04:46:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6ee7dc96-5767-39b2-9922-06bb0c707589 | -7.71005 | -48.72604 | 2025-09-03 04:46:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a6d7a412-d080-3bd0-84cd-36a3f8822ea5 | -11.6028 | -52.10167 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| dbd2038d-acb3-3a83-a8fe-44b4edf8d7ed | -6.03102 | -46.00528 | 2025-09-03 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 92e54e25-3c73-32b2-ad58-83a3fb619409 | -6.85215 | -45.54368 | 2025-09-03 04:46:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 81a393be-b793-30b9-a126-d12e9af8fd2c | -10.13574 | -46.24331 | 2025-09-03 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7ca31b17-595c-3b8a-bf10-6b5853af4b66 | -7.49118 | -44.82445 | 2025-09-03 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6fd39895-1431-3690-afd6-f00a310543a0 | -11.05257 | -46.89113 | 2025-09-03 04:46:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ea74a156-cbb5-3f6b-a020-0e2f9948654a | -5.90304 | -57.74771 | 2025-09-03 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 22.4 |
| 6cafa32e-9c78-3bea-8255-0f1899147378 | -6.46631 | -45.40105 | 2025-09-03 04:46:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f1e2161b-36ea-319c-bebf-78a967c35f35 | -5.79885 | -43.23774 | 2025-09-03 04:46:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 84927392-5e5c-317b-910b-cc9cc295ae2c | -8.15216 | -54.92964 | 2025-09-03 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d9ba42a3-4933-3ebc-83bb-587d53d10942 | -10.95451 | -50.76839 | 2025-09-03 04:46:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 270ab41d-01cf-3516-81a0-18ec1c9effca | -8.45971 | -45.05262 | 2025-09-03 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ad9cc603-b415-3fe0-af45-1332a5f36098 | -9.64447 | -47.03418 | 2025-09-03 04:46:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 568cf030-fbc7-35bf-bde8-1fdb0cf46ffa | -5.90749 | -57.72118 | 2025-09-03 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 091b3de8-5985-3f23-8c25-38eb6154b6bb | -10.54531 | -50.43932 | 2025-09-03 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 7ab76231-dab9-3427-ba10-3039715b06b6 | -8.34314 | -52.53705 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c5cb2e88-a96d-381c-8b75-468f40bed07b | -6.27053 | -42.66155 | 2025-09-03 04:46:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e58ebe02-4604-323d-8bae-5136c69e48a9 | -6.09857 | -43.29568 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.4 |
| cbb8c1e3-b05a-328f-a046-01c1ddef1f19 | -6.99938 | -43.2604 | 2025-09-03 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.5 |
| b694c1df-b56f-3ee7-9c5e-352449c34cf1 | -6.73273 | -42.2692 | 2025-09-03 04:46:00 | NOAA-21 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| edfa137a-1756-35e9-a8e4-dfed382ab30b | -8.38006 | -48.30949 | 2025-09-03 04:46:00 | NOAA-21 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1a01884a-b1e4-3f42-93ce-97b278749006 | -6.79561 | -52.80841 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3846c0b3-1a4e-36f6-9456-32c3a83d20fe | -6.83666 | -52.81124 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a6a14500-222e-389a-aab7-e42eb990e478 | -5.89 | -43.00317 | 2025-09-03 04:46:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 2ec4c053-9c39-3faa-bb94-61b8ac23709c | -9.65449 | -48.0741 | 2025-09-03 04:46:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d7fc7aa3-9c46-307d-93ce-15d9de00cdd3 | -11.60386 | -52.07307 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 76e75951-b4fa-3b94-995a-c83efe305152 | -6.27439 | -44.50665 | 2025-09-03 04:46:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ea2b9604-c262-3ccd-8ec6-3b194b9849f1 | -8.14981 | -54.93947 | 2025-09-03 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| de70f92c-49ec-3e07-a653-814e487ea786 | -8.54294 | -51.30991 | 2025-09-03 04:46:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 92d83fa8-8bfd-3527-8613-9ba4ca777872 | -9.73176 | -49.0019 | 2025-09-03 04:46:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 68092122-d52d-36e7-8302-e4f6b60bc32a | -9.33151 | -55.22129 | 2025-09-03 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README54.md)

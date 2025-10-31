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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 938c0e9b-b5e9-3286-b104-ceafb1e4d291 | -12.29477 | -43.78363 | 2025-10-31 04:57:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c50e2c3a-2f86-3a17-92a7-47c0b21af88c | -11.7397 | -49.339 | 2025-10-31 04:57:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3454da2d-a313-3e79-a61c-1edc1deb45b5 | -11.31788 | -51.44775 | 2025-10-31 04:57:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 99443944-3a3b-3e09-84ec-9db3af803a42 | -8.08647 | -45.13647 | 2025-10-31 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 29f24a68-9763-3920-8a74-77ab35b8851f | -14.08384 | -44.15578 | 2025-10-31 04:57:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7594172a-ada9-391d-b1cb-6d37d84639b4 | -12.28356 | -48.06972 | 2025-10-31 04:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 68be85d8-0205-3a6f-8828-48e70a460009 | -12.04863 | -54.24646 | 2025-10-31 04:57:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 57217790-0091-3698-b3a0-2c66afe5fdca | -9.52154 | -47.26979 | 2025-10-31 04:57:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a332a6d8-9350-318b-ad32-b09196d9654c | -7.81093 | -46.38746 | 2025-10-31 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 2c2a274d-ed0f-3ef5-bb67-1d4b50468e3b | -12.11024 | -47.1184 | 2025-10-31 04:57:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 14a8652e-0e12-3eca-a935-7d1924c7c8e4 | -7.81923 | -46.39979 | 2025-10-31 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 01a9af37-2bcc-350c-af42-41c63d2553f5 | -8.06943 | -45.14088 | 2025-10-31 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b60005ab-c09f-3080-a01f-f5000f8e5f31 | -7.6167 | -46.47349 | 2025-10-31 04:57:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b09745ac-9bbe-3ffd-b23a-529ab7dd2892 | -7.64877 | -43.59439 | 2025-10-31 04:57:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| d37c076e-7f76-33e1-8e70-804d11960d24 | -13.56273 | -47.36931 | 2025-10-31 04:57:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6f155b01-aa3b-3806-a8d7-79998034c202 | -7.07402 | -44.92935 | 2025-10-31 04:57:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 075114d2-2e80-3285-aaf2-6c8d06191de7 | -8.9565 | -47.52379 | 2025-10-31 04:57:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fea077a4-f4e2-3b66-a20b-2e836e5f35d6 | -13.38765 | -47.34336 | 2025-10-31 04:57:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 67589d50-9d20-3484-9fb9-f0c544dcfbac | -10.53463 | -45.04383 | 2025-10-31 04:57:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2c473fe3-04fe-3f08-9a40-fe50f2e700c9 | -7.35324 | -44.99834 | 2025-10-31 04:57:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e259931f-2ed9-32c8-946e-d245596ca9c8 | -12.2861 | -48.05019 | 2025-10-31 04:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f87860e5-d584-30f0-9789-6e0294ecbf53 | -8.16444 | -45.50635 | 2025-10-31 04:57:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 8a8ec133-dcdd-3274-993d-1f17691eef4d | -12.09746 | -47.13378 | 2025-10-31 04:57:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 72085418-101d-3b00-a2b2-bf2790e7db78 | -10.92623 | -44.76319 | 2025-10-31 04:57:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c4e79911-27fa-35a2-9a56-a23f4f4830d9 | -7.64132 | -43.58888 | 2025-10-31 04:57:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 0871a73a-cbbd-3477-ac48-4963941ffc37 | -7.66716 | -43.59215 | 2025-10-31 04:57:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 899c1f75-1f2b-3079-982c-03c7b0c3c060 | -7.65464 | -43.5956 | 2025-10-31 04:57:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 2526747e-f475-3c90-b8de-f1d8d500909b | -10.54356 | -44.78907 | 2025-10-31 04:57:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f08026d2-6257-3e4a-9ba1-39feadf77260 | -8.9574 | -47.52275 | 2025-10-31 04:57:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8e156543-2b27-3814-9564-221797d59967 | -10.74834 | -47.83198 | 2025-10-31 04:57:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ee979428-050b-38f2-8f66-98f848812379 | -8.16918 | -45.51103 | 2025-10-31 04:57:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a0fbe3f2-2698-3857-bdd2-57cad7fc1cba | -12.06561 | -47.34212 | 2025-10-31 04:57:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| c10ab484-9315-3faf-9903-2a756fa9bc2c | -9.45508 | -56.64136 | 2025-10-31 04:57:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b80c0490-e503-39e4-ae6c-deb8693be629 | -5.13433 | -55.95652 | 2025-10-31 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 35d7cd84-07d7-3708-8cd1-7143a622b897 | -8.32841 | -47.9317 | 2025-10-31 04:57:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| eb3b0773-8648-3489-a2b7-a5e8646a8e5e | -11.29397 | -54.31427 | 2025-10-31 04:57:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1e3a9635-0e01-3d20-831a-b21d6f67f47b | -8.08431 | -45.13183 | 2025-10-31 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 532e9ed0-c78f-3d22-ac34-f0e4a61c0d57 | -12.27154 | -48.05222 | 2025-10-31 04:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c79cf116-1384-3c12-ae5e-a68e7b9a2d3d | -13.15467 | -48.44893 | 2025-10-31 04:57:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0caac6f6-bfa8-3dc6-8ede-a768974acd34 | -9.86069 | -44.86034 | 2025-10-31 04:57:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 4d7ed997-612b-35b4-bbaf-dcfea16d1500 | -7.07985 | -44.92678 | 2025-10-31 04:57:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 2c763914-7d86-3469-a2c8-01b3880cf737 | -7.12185 | -47.01453 | 2025-10-31 04:57:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ff0efcdd-0fb3-32d6-a6cf-966657564b54 | -7.08434 | -44.93411 | 2025-10-31 04:57:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ad0dcd53-96eb-38e4-b8cf-e61305891dda | -8.08968 | -45.13265 | 2025-10-31 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cb6b2a14-fdfc-3d73-bcb2-6d9173b042a5 | -7.79195 | -41.57922 | 2025-10-31 04:57:00 | NOAA-21 | CONCEIÇÃO DO CANINDÉ | PIAUÍ | Brasil | 2202802 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 6f0c8484-5899-39c0-bd91-16e8a45c3953 | -10.84595 | -44.92955 | 2025-10-31 04:57:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a755c39e-50c3-346a-a9c0-799dd899b0a2 | -8.08738 | -45.12978 | 2025-10-31 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 62c0c5b3-4327-37e5-8a23-32dd677c0c79 | -7.64936 | -43.59004 | 2025-10-31 04:57:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| d2d248e0-fb45-3a7a-9232-4db536ddf211 | -7.07939 | -44.93021 | 2025-10-31 04:57:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 756bb323-8be7-30d1-a938-c01132b2c375 | -13.70518 | -44.19941 | 2025-10-31 04:57:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| abd021a7-faf6-327c-8813-d24dddd78e4b | -12.03637 | -54.23717 | 2025-10-31 04:57:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 709b1676-7236-3750-9f25-1b336fd49c57 | -8.64553 | -54.54862 | 2025-10-31 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 30ec5283-3893-30ef-a530-2a71dd15634b | -10.64429 | -45.24369 | 2025-10-31 04:57:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c1da65a9-740a-3c39-be54-ef64f2fb5345 | -13.68343 | -47.17479 | 2025-10-31 04:57:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fdd318bc-3b80-3321-bcf7-9b045e1d5976 | -8.57959 | -48.65796 | 2025-10-31 04:57:00 | NOAA-21 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bc7f9b0c-5cda-3133-b440-b9a8ee811c3a | -7.86839 | -48.88357 | 2025-10-31 04:57:00 | NOAA-21 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9361f03f-1ec8-35ec-a8bf-47c6fbeb8b38 | -7.81018 | -46.39286 | 2025-10-31 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 9f651a06-b236-35e9-8ac7-f5e056572c8c | -10.5383 | -53.72448 | 2025-10-31 04:57:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6c592c42-565e-350d-8606-e4bccde7a63a | -12.07205 | -46.63602 | 2025-10-31 04:57:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3689cb79-2050-333a-a62e-16a7904e2e68 | -13.68375 | -47.17223 | 2025-10-31 04:57:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 85480a30-93ce-39fe-b31f-0d785d051ecf | -10.43036 | -44.31299 | 2025-10-31 04:57:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c1980edf-5470-3288-b6c6-18653899d1d2 | -13.15739 | -48.46465 | 2025-10-31 04:57:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 4d7e2b04-a194-344d-87f4-d9ec3a5636b7 | -7.6524 | -43.59656 | 2025-10-31 04:57:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 55b6beb1-7f78-3a51-8d6f-5e5b677fdb10 | -5.17924 | -56.11161 | 2025-10-31 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b70436ba-5669-34e2-95f4-73065a31912e | -8.08301 | -45.1419 | 2025-10-31 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 78e9710b-49f5-3c20-b17b-90c07e90a43f | -7.08527 | -44.92725 | 2025-10-31 04:57:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fdd75a65-2736-32f2-9a1b-6531450fedc7 | -12.10314 | -47.129 | 2025-10-31 04:57:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 241ca7bc-75b3-3560-a930-10a40a8a3639 | -8.26171 | -46.35624 | 2025-10-31 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 646629d6-72c9-3b6f-878c-b8c092568584 | -13.52015 | -47.34352 | 2025-10-31 04:57:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 11f932e9-ce71-3b75-9c50-cb4c1fd5983c | -8.31622 | -45.37026 | 2025-10-31 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c28b5100-bd61-3524-af94-d0b626f5cf14 | -9.24524 | -47.53905 | 2025-10-31 04:57:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3698bd0b-dc1a-36bc-a052-e94005c83b5a | -7.65522 | -43.59131 | 2025-10-31 04:57:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e8d1c0da-d3da-311e-8af5-08c4a2d1d93a | -8.08601 | -45.13981 | 2025-10-31 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3f862344-f09b-3818-b0a8-a0d55697e91f | -8.64499 | -54.55209 | 2025-10-31 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8c3612ba-a958-3159-9b59-5de848c5ae1f | -7.35455 | -44.98833 | 2025-10-31 04:57:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| ec07c74d-78e0-30f0-a055-c0e6a092d26b | -9.52307 | -47.26577 | 2025-10-31 04:57:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| fb266116-7579-3606-9e1f-999073928085 | -5.13372 | -55.96028 | 2025-10-31 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3b0b2d73-db14-3bd4-ae58-06fd0c64f2d2 | -7.34946 | -45.00282 | 2025-10-31 04:57:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f0b61ae6-564c-3d9b-b30e-ed38fdbd071f | -7.31989 | -44.93832 | 2025-10-31 04:57:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 27.9 |
| 16661c30-54bf-38db-973b-50c823fb0183 | -6.81128 | -44.45417 | 2025-10-31 04:57:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 74833ff4-7de4-360c-9198-de7b7a2d630c | -11.11839 | -54.63649 | 2025-10-31 04:57:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 56e8692b-c770-3c08-a9b6-4be5c2f93798 | -11.31047 | -51.44663 | 2025-10-31 04:57:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 021d3113-dfcc-3c22-b3d5-0b29535211ce | -7.65295 | -43.5923 | 2025-10-31 04:57:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 19c164c2-a840-336a-8528-fd8f85dd441c | -11.33319 | -51.18481 | 2025-10-31 04:57:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 64a2082f-9d3d-3def-9786-02b8531da6f4 | -11.01123 | -43.87373 | 2025-10-31 04:57:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0176c0a4-0f57-3bfa-8c28-6c8206f4df16 | -7.62027 | -43.62738 | 2025-10-31 04:57:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 89a2d6f8-fbe8-3ad3-baba-83304d22c5dc | -7.78914 | -41.57464 | 2025-10-31 04:57:00 | NOAA-21 | CONCEIÇÃO DO CANINDÉ | PIAUÍ | Brasil | 2202802 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 6f443097-7d4e-32a8-a3a5-5bfd9b45588b | -7.0848 | -44.93069 | 2025-10-31 04:57:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4150ea93-e930-3daf-8812-32437d5f8b3b | -12.10885 | -47.12397 | 2025-10-31 04:57:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 75fe9e0e-bca5-32ab-8b9a-105aae5e2dcb | -10.53045 | -53.70853 | 2025-10-31 04:57:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a4facc0b-331f-3d92-ba60-27ce4d7ef8e7 | -12.8418 | -43.45772 | 2025-10-31 04:57:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 25a3d0d9-01a7-3a6b-a49a-e7a006e7480e | -10.88396 | -44.32477 | 2025-10-31 04:57:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 90740db4-04a6-33f1-b866-9f78d7ddbb79 | -7.6471 | -43.59092 | 2025-10-31 04:57:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 040311f4-0a22-3dc0-8652-525ad1712452 | -9.95906 | -54.74475 | 2025-10-31 04:57:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e6385d2c-061b-3a77-ab09-72e58a282ca4 | -13.65753 | -47.04657 | 2025-10-31 04:57:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3e16b2a9-cbb8-36a3-a141-5a100f17b865 | -10.50553 | -42.41061 | 2025-10-31 04:57:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 13.7 |
| 5db7ed79-5dac-3572-9f57-3da988de0254 | -10.97818 | -51.04463 | 2025-10-31 04:57:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3b7baca6-0dd8-3c5f-8280-ac76e78dbc0d | -11.64157 | -44.04183 | 2025-10-31 04:57:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3da0f0b6-b28e-3b31-ab28-a8bb5326280d | -10.53435 | -53.70545 | 2025-10-31 04:57:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d5cea89a-86b4-3837-902e-b4d9695bd7c3 | -12.07242 | -46.6329 | 2025-10-31 04:57:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README37.md)

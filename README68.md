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

## Dados Diários - Página 68

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5b4a530c-484d-34eb-b00b-53e21f5cf3d9 | -3.272 | -51.62552 | 2025-10-27 05:23:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6be88c3b-7f0b-3503-99d7-991c211e7d2f | -7.06583 | -46.7602 | 2025-10-27 05:23:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4750814e-b8f8-3cfa-890b-73a4062a511a | -3.04593 | -53.01889 | 2025-10-27 05:23:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 2bbb2a79-5e1f-31e8-b23c-fbc088d9cccc | -4.15963 | -51.08152 | 2025-10-27 05:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6d209b90-f04a-3c20-92e1-80719c354f91 | -3.13338 | -53.00248 | 2025-10-27 05:23:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f92596e0-cc62-3da0-a70f-c9fa90d6c39b | -3.77677 | -51.81188 | 2025-10-27 05:23:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e6cdf045-82bd-32c2-91b9-3a79ec8ed3db | -9.13731 | -51.30699 | 2025-10-27 05:23:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| c2e92933-ee73-3ab7-bf3e-e863c277fe60 | -14.82757 | -52.42587 | 2025-10-27 05:23:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ef55aa7c-debc-3ca6-99ae-a185bfb0f502 | -3.34058 | -52.84023 | 2025-10-27 05:23:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 12a701bd-3294-3716-8797-adc9af45c1d1 | -2.94376 | -51.76102 | 2025-10-27 05:23:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 33f361ff-4131-3b03-a11f-d42f677fb456 | -2.77122 | -54.57254 | 2025-10-27 05:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bc52fa9f-2759-3640-b5ac-ef3ac9818de9 | -3.86113 | -49.80705 | 2025-10-27 05:23:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 75faa021-5307-33c7-b065-de51bf77279c | -14.82708 | -52.43004 | 2025-10-27 05:23:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1b19b9c9-9ca1-390b-aea5-3734da7ce952 | -3.79952 | -49.29765 | 2025-10-27 05:23:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 779578a6-f02a-3f19-ac5d-c755215023c9 | -9.59789 | -50.79009 | 2025-10-27 05:23:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ba8575d1-5ea7-31b3-b00a-eee09f2ccaa0 | -9.14245 | -51.3081 | 2025-10-27 05:23:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1d17e3b5-b1dc-3acc-b450-20e8448faea3 | -8.53246 | -47.20036 | 2025-10-27 05:23:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2786e176-cea9-3610-b8f0-6cdb28409244 | -8.07048 | -46.95186 | 2025-10-27 05:23:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 91bca707-e07f-32be-9574-d75bd16fca87 | -4.87282 | -50.85856 | 2025-10-27 05:23:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cbc243ba-4f5a-38a8-bc0a-8f046adac542 | -3.73052 | -49.69006 | 2025-10-27 05:23:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c16154ec-6c9b-36d8-bd02-fcf47fa89cbf | -5.70986 | -49.31143 | 2025-10-27 05:23:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 80da78f0-4274-320c-a2ec-a5653da677b0 | -7.22148 | -46.87689 | 2025-10-27 05:23:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a562bf71-0da3-3158-ada8-e2f2ff0a12c7 | -3.98912 | -51.03683 | 2025-10-27 05:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 44426bec-404e-3f9d-b41d-3da4bd181067 | -3.0982 | -49.46238 | 2025-10-27 05:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9c9fffce-f809-3e6a-8ed3-097e3ff44882 | -9.14285 | -51.30778 | 2025-10-27 05:23:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 975c6123-9367-33f0-9a8a-daad988248ba | -3.11383 | -51.21615 | 2025-10-27 05:23:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e0619ad4-8c2c-333a-8305-bc070c9c4aa3 | -3.47122 | -49.96216 | 2025-10-27 05:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2bac9cdc-4c52-3613-b5b4-ea8e16e2e5f3 | -5.71526 | -49.31675 | 2025-10-27 05:23:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3c66bc38-9a9d-331a-9152-ee13fcfc20ff | -4.26858 | -50.51938 | 2025-10-27 05:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6989f645-e978-344c-af73-dc78dfe89a80 | -2.44862 | -57.9526 | 2025-10-27 05:23:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2aedbf69-8f1c-3051-bdaa-4989563b7d17 | -3.75457 | -51.75666 | 2025-10-27 05:23:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e9e80f0a-d98a-35c9-8439-fe5bd0452dd4 | -3.2843 | -52.96185 | 2025-10-27 05:23:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0ca0e716-75d6-3776-90af-08018ad3fd59 | -9.13782 | -51.30328 | 2025-10-27 05:23:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 126b6988-4de8-3bb0-aa79-3fcb14b24122 | -7.24314 | -46.96393 | 2025-10-27 05:23:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a86699fa-c79d-3a6e-b472-24bcb2d3de10 | -3.05114 | -53.01498 | 2025-10-27 05:23:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4b5785b5-aa6e-3d58-a848-abc2a791a0b2 | -7.94563 | -47.24858 | 2025-10-27 05:23:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 908f1dd0-adff-351b-82ba-aed0653d22eb | -5.71651 | -49.30772 | 2025-10-27 05:23:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7c0bcea7-a320-3ddf-b4da-59d1d24fc326 | -3.47011 | -49.96978 | 2025-10-27 05:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a6d4d102-718b-3893-9b08-5a5666563f3a | -4.31974 | -48.08911 | 2025-10-27 05:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6bf970ff-7a18-3fda-ab8a-c5ef79f0dcbe | -3.14384 | -50.45381 | 2025-10-27 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6b7b16b7-18a6-3645-be70-17f035d4038a | -13.31763 | -54.36202 | 2025-10-27 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 1876c309-0a75-365f-8544-92e088257057 | -4.26364 | -50.51508 | 2025-10-27 05:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 860beb57-ccb1-38ea-9240-874839f48990 | -13.32381 | -54.38914 | 2025-10-27 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 38536a5b-4756-3ca3-8b9c-1819c8d877cb | -3.24159 | -48.77955 | 2025-10-27 05:23:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| af9ad4cc-6e61-3999-84d4-9c4f80094418 | -13.29447 | -54.39086 | 2025-10-27 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 273ecef1-25e7-366f-b1fc-1903942e24f2 | -3.09369 | -49.4603 | 2025-10-27 05:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e6cd23bc-5bc7-332c-8080-68527ed4fa0b | -5.26773 | -50.977 | 2025-10-27 05:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 672292bf-85b5-3b98-9468-d2c96c015762 | -3.24206 | -50.64647 | 2025-10-27 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 41b171cb-23e8-3f3f-ab1d-1e7e8c083212 | -13.30403 | -54.392 | 2025-10-27 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 22501690-6204-3734-8909-98d0eb36868c | -9.13185 | -51.30273 | 2025-10-27 05:23:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 6ba3619b-27ed-3354-a43e-829c2a9f1277 | -9.13228 | -51.30246 | 2025-10-27 05:23:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 992c7b83-9551-3ec9-a914-1046b25748d3 | -3.11473 | -51.21016 | 2025-10-27 05:23:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 108fc017-ca8f-38ad-8c2f-9f5d396c536a | -3.24303 | -50.64882 | 2025-10-27 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 48d67e99-4bd8-383b-a464-4f24aa42176c | -10.19262 | -48.07397 | 2025-10-27 05:23:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 535c0dab-1e08-3510-a18c-6a30c03e27db | -3.57753 | -49.02349 | 2025-10-27 05:23:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8967fae1-9bd8-3b13-9b3b-1b8f11d5b6f7 | -13.26304 | -54.3709 | 2025-10-27 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 956bf490-0526-3663-9e11-571adfd3ef8a | -4.10019 | -51.04849 | 2025-10-27 05:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f1404eed-21f1-383d-9e5d-c0d9ce67086a | -2.48299 | -58.04268 | 2025-10-27 05:23:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 40bb0c1b-0074-366e-8d6a-8dac7be72c74 | -13.30259 | -54.36554 | 2025-10-27 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 9531eb30-43bc-3176-b6b7-ca777bbdce79 | -10.68264 | -47.84523 | 2025-10-27 05:23:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 99362bbd-59c3-3da5-b98f-a8525f474fea | -14.37061 | -51.52941 | 2025-10-27 05:23:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5b3270ed-31c6-3807-8780-37c0359a380c | -9.13691 | -51.30729 | 2025-10-27 05:23:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| e4796a7d-b10e-34e1-aea5-d10ad4ca4b3e | -3.04523 | -53.02349 | 2025-10-27 05:23:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 36c44768-04e0-371e-b043-72e7330f60e0 | -7.24602 | -46.96505 | 2025-10-27 05:23:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 9649d6f9-e57c-3a41-9268-2ae548b8d857 | -2.86838 | -54.20929 | 2025-10-27 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| af557bd0-d7d7-362e-a9ad-7c59bd9d8ea1 | -14.84376 | -52.43188 | 2025-10-27 05:23:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7fdee289-e35d-3248-a8fa-b2f753c538b6 | -3.3257 | -52.62766 | 2025-10-27 05:23:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6a699d5c-2d55-3145-8573-ae6ab982a1d8 | -3.24202 | -50.65538 | 2025-10-27 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 38fbb652-f9b9-3e5b-9a11-bb14ad1a4ed1 | -13.25762 | -54.37543 | 2025-10-27 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 11.0 |
| b63fa55b-e3b2-396e-ae80-3752cf45b85b | -13.29792 | -54.40172 | 2025-10-27 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4e3a3283-0be3-3d7a-91f2-8efeab7af7b6 | -8.88227 | -47.99859 | 2025-10-27 05:23:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8b534662-6c50-3d40-9974-15cb857cebe4 | -13.29858 | -54.39658 | 2025-10-27 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4725b3df-76c6-39b3-9a60-db332772ebc7 | -13.30872 | -54.35571 | 2025-10-27 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 607f6d47-1717-311d-97d9-5cb787f5bf7e | -3.23722 | -50.65127 | 2025-10-27 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| fdae2532-f611-3c09-93d3-835c36e1d7a9 | -4.62681 | -50.41972 | 2025-10-27 05:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a033d2df-dc78-3c11-a19c-4e238a6a418f | -5.26724 | -50.98039 | 2025-10-27 05:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6ccbd699-811c-38da-9a41-49597ce61ea4 | -8.21955 | -46.94968 | 2025-10-27 05:23:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a77b561d-9d72-36b2-9b0e-c52136f189ca | -3.14604 | -50.45602 | 2025-10-27 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a224ebf2-043c-317b-92df-b5b040416be0 | -13.26702 | -47.97282 | 2025-10-27 05:23:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 24a8fb6e-e94b-3057-a75e-54af5b26e923 | -13.32107 | -54.37296 | 2025-10-27 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| ade72bcb-c0eb-35fd-be7b-def99f8a0460 | -13.29381 | -54.396 | 2025-10-27 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 46bcb69e-78e3-37e4-9692-93dccda25d18 | -3.10001 | -49.45723 | 2025-10-27 05:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d924293b-c32c-35af-b08f-93097dd97202 | -4.25921 | -50.50726 | 2025-10-27 05:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 87fa4cb3-0ce8-360b-a94d-7de1bbc8cdcc | -2.77525 | -54.57322 | 2025-10-27 05:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 714c060d-e60d-310f-ac48-b910d54de8c7 | -11.9801 | -58.06155 | 2025-10-27 05:23:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b20f73de-0c34-3e3e-86be-5f87588c3856 | -4.15606 | -51.14296 | 2025-10-27 05:23:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 357a35a5-0688-3c9d-81f2-f126e858aec3 | -9.04199 | -47.62099 | 2025-10-27 05:23:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c23201b6-6b83-3e04-a470-b6c4cb6fccd0 | -10.19343 | -48.06742 | 2025-10-27 05:23:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| b240d0f1-e76a-36a9-8116-0f8aec6cbd9a | -3.07931 | -51.2724 | 2025-10-27 05:23:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f0746d0d-eed4-38cd-8f21-6088ad26a032 | -2.0679 | -56.8735 | 2025-10-27 05:23:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0e80bba9-abc7-3b02-ba58-871e75e85a66 | -2.13052 | -56.84665 | 2025-10-27 05:23:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3ae4bb84-d7f0-3cb4-a21f-57355d9b62e7 | -3.11983 | -51.21097 | 2025-10-27 05:23:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5d5dc472-77de-370d-90e4-13dbca5dc4f4 | -3.57417 | -49.02499 | 2025-10-27 05:23:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b0751f6a-dfb5-3307-be0d-51f551c4cd61 | -14.37013 | -51.53367 | 2025-10-27 05:23:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e57558b3-82cd-36ba-a2cb-0c46bb27c4a2 | -3.14654 | -50.45259 | 2025-10-27 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6e360094-1334-3cb7-9f33-5c95dd06e24b | -2.90273 | -53.13166 | 2025-10-27 05:23:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0b85b730-8222-352e-bfd4-70f085c9ab6f | -3.17798 | -52.49556 | 2025-10-27 05:23:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 698c5222-9186-3bb6-b445-d34fd146a5f1 | -3.52182 | -52.20605 | 2025-10-27 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cfb04699-1b64-3a1d-93d0-bb17f27c3f85 | -2.97601 | -51.03429 | 2025-10-27 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7c49d12b-6eca-3f0d-ad6b-9c86c7dcd3e1 | -3.69375 | -60.55912 | 2025-10-27 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README69.md)

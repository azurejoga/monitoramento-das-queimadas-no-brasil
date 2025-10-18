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
| d2b817a0-1180-38a0-b56a-88a206296e75 | -3.1431 | -50.2464 | 2025-10-18 00:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| b4a650c6-23e9-38f4-a159-fb8964a1a85b | -4.4428 | -43.4724 | 2025-10-18 00:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 694b19e8-24c2-3db4-92c5-97995c5e8402 | -10.9755 | -45.4553 | 2025-10-18 00:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 4d8cac8d-31b8-3f03-9c4c-40ca08cc929c | -10.9567 | -45.4349 | 2025-10-18 00:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 125.0 |
| 3d8aeb72-8eda-3181-9424-4998a002d308 | -10.9756 | -44.3011 | 2025-10-18 00:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 2abd7008-3cec-393a-ab1b-26898808cf41 | -4.4632 | -43.2386 | 2025-10-18 00:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 255.0 |
| fcf5a990-8047-35c3-aa77-b90254ebe7e6 | -4.4446 | -43.2164 | 2025-10-18 00:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 246.5 |
| 6b230d96-f598-3bb0-9c4c-7bdc521fe708 | -4.4241 | -43.4735 | 2025-10-18 00:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 5cebd2e8-7ec1-31ff-9b48-cb0a9b442de8 | -11.204 | -47.8318 | 2025-10-18 00:40:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 40.6 |
| 3066ea4b-d8e1-3182-a865-655c777f9182 | -18.3938 | -55.4559 | 2025-10-18 00:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 81.2 |
| 5034bd44-7371-35dd-97ae-43d82db0b44e | -10.5335 | -43.3552 | 2025-10-18 00:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 8500af34-12d3-3b34-a289-2b64f1c493e8 | -17.4587 | -40.0547 | 2025-10-18 00:40:00 | GOES-19 | MEDEIROS NETO | BAHIA | Brasil | 2921104 | 29 | 33 | nan | nan | nan | Mata Atlântica | 75.6 |
| 85422341-9506-3278-b136-bfcccba88218 | -17.4385 | -40.0602 | 2025-10-18 00:40:00 | GOES-19 | MEDEIROS NETO | BAHIA | Brasil | 2921104 | 29 | 33 | nan | nan | nan | Mata Atlântica | 116.5 |
| 4920dd03-3abf-35c7-a78b-a3712525d803 | -10.4937 | -43.4552 | 2025-10-18 00:40:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 219.0 |
| 1f01e0d6-eb6c-3f4b-8df5-24dfbac591bb | -5.0214 | -46.032 | 2025-10-18 00:40:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 137.0 |
| 049585dd-3262-389c-962b-fea762c30d7a | -11.5917 | -44.0707 | 2025-10-18 00:40:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 106.8 |
| 086a9a9a-210f-345c-92fe-ef43e9a04a91 | -4.4445 | -43.2397 | 2025-10-18 00:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 345.4 |
| cf89b022-9f09-3631-a669-32cd016c5c85 | -8.4079 | -46.2314 | 2025-10-18 00:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 68.5 |
| a38a1a18-b273-3772-8e5a-c5e4addfb9f2 | -13.4663 | -43.7617 | 2025-10-18 00:40:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 7a40c5aa-db30-3e59-970f-98678f64c411 | -5.0029 | -46.0108 | 2025-10-18 00:40:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 115.1 |
| d5623c6d-bc31-3cd6-9da7-ebc4c132d457 | -5.0215 | -46.0097 | 2025-10-18 00:40:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 157.7 |
| 7390f003-9c60-3b37-b661-0d30e23c39cb | -14.2766 | -51.8807 | 2025-10-18 00:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 23b8df8a-efcd-3ffd-a53a-3e1b66db730e | -18.3735 | -55.4798 | 2025-10-18 00:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 100.7 |
| 3cbda23b-adbe-3e5d-aec5-4f0a5a06c83c | -10.9564 | -45.4579 | 2025-10-18 00:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 179.9 |
| 058a26d8-6329-3efd-ac7d-d7e0317aab8b | -8.389 | -46.2333 | 2025-10-18 00:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 120.1 |
| 99a5e54d-9000-30c4-99b1-78265b5c96cf | -4.4633 | -43.2152 | 2025-10-18 00:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 180.3 |
| 21ced8e2-bb5d-39b5-be0e-57c868fa4b0c | -13.2102 | -43.9726 | 2025-10-18 00:40:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 53.0 |
| b686383a-98ae-3aff-b641-950e3167b1dc | -8.3704 | -46.2127 | 2025-10-18 00:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 58.5 |
| f1ecfcbe-1280-3427-968d-ad94b5bb40fe | -5.0027 | -46.0331 | 2025-10-18 00:40:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 99.8 |
| 07defdce-0dee-39c5-8212-890c3ac71df6 | -11.6109 | -44.0678 | 2025-10-18 00:40:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 140.9 |
| 9dcf91bd-545b-39ab-a34f-78a24010599e | -14.277 | -51.8593 | 2025-10-18 00:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 86.3 |
| c4adbca4-0cd0-3002-8377-8fb7586ba7f1 | -18.3934 | -55.477 | 2025-10-18 00:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 116.9 |
| d6e1e5c5-cb31-35fd-8fd2-64ac90581451 | -10.9752 | -44.3244 | 2025-10-18 00:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 67.0 |
| f61f5689-0865-3a9a-a009-e2e9d10c654f | -3.1616 | -50.2458 | 2025-10-18 00:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 35.3 |
| 041e01ff-bdf1-3796-afae-363e8c681d46 | -8.389 | -46.2333 | 2025-10-18 00:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 91.2 |
| f0c432d8-1a24-32e4-b86a-5f32fbbb2c59 | -10.5335 | -43.3552 | 2025-10-18 00:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 68.0 |
| fb0a0966-f65d-3c0d-bed0-afee7f633dba | -11.5917 | -44.0707 | 2025-10-18 00:50:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 7b02fbcc-0584-3ed8-aad5-bb2237acd2da | -14.277 | -51.8593 | 2025-10-18 00:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 76ef015c-24fa-386e-9e9c-3f2485d3fcc8 | -3.1432 | -50.2254 | 2025-10-18 00:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 34.9 |
| 5a1509c7-23a4-31c3-960d-e1271c492867 | -18.3934 | -55.477 | 2025-10-18 00:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 120.0 |
| 0ed8c13e-3702-398f-b11d-87de94b26332 | -10.9944 | -44.3217 | 2025-10-18 00:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 88.5 |
| d174149c-fafd-38d7-99ff-dafa21f32151 | -5.0027 | -46.0331 | 2025-10-18 00:50:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 128.5 |
| 7c499b45-eb22-3a41-a352-20a9d9032af5 | -5.0214 | -46.032 | 2025-10-18 00:50:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 91.5 |
| 97c7c26b-ca29-3b06-bf87-f364c5562ecb | -14.3225 | -53.7718 | 2025-10-18 00:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 81.2 |
| db5dcd83-0be5-30af-ace3-99ceb1768dcf | -4.4445 | -43.2397 | 2025-10-18 00:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 253.9 |
| d1d5f3d8-7118-353e-8b18-956168d7c060 | -17.4579 | -40.0808 | 2025-10-18 00:50:00 | GOES-19 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 50.9 |
| 93ca085f-e91f-31e2-9e35-7be459efdd42 | -18.3938 | -55.4559 | 2025-10-18 00:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 77.5 |
| 1d352491-c0c1-379a-b038-20a885820825 | -3.1431 | -50.2464 | 2025-10-18 00:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 86.7 |
| f2771643-2e13-3e61-af80-c06a50e5d7d3 | -5.0215 | -46.0097 | 2025-10-18 00:50:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 89.2 |
| b9be1318-4871-3087-b4ec-f70d773dd241 | -10.9564 | -45.4579 | 2025-10-18 00:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 3d5339f1-996c-308d-b610-4fbc8b210382 | -4.4446 | -43.2164 | 2025-10-18 00:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 138.1 |
| 3c3d3a05-d31a-327f-b9bc-083659c7d0f0 | -17.4385 | -40.0602 | 2025-10-18 00:50:00 | GOES-19 | MEDEIROS NETO | BAHIA | Brasil | 2921104 | 29 | 33 | nan | nan | nan | Mata Atlântica | 216.0 |
| f00241ab-dad6-3124-a041-1476c38ca6fa | -2.9127 | -52.735 | 2025-10-18 00:50:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 84.1 |
| b3ae1960-77db-3f3e-8e02-4caced11b4e0 | -7.3447 | -43.8503 | 2025-10-18 00:50:00 | GOES-19 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 204728fd-3e2c-367c-ac6c-344ce3950671 | -2.9257 | -49.1747 | 2025-10-18 00:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 3e8d1df1-07eb-32f7-aec6-0d2bb300c518 | -17.2554 | -56.2135 | 2025-10-18 00:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 57.2 |
| 7573e034-c32c-3d38-b8d9-568730544cc9 | -3.8572 | -41.5719 | 2025-10-18 00:50:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 87.3 |
| 62cd713d-99f0-3a96-9ca4-fce85c422917 | -13.4663 | -43.7617 | 2025-10-18 00:50:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 58.5 |
| ba027658-4640-3141-a395-611c4df63107 | -4.4632 | -43.2386 | 2025-10-18 00:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 337.5 |
| 6fae00f1-6238-3e1f-93f7-2e71599ff599 | -12.7566 | -48.6221 | 2025-10-18 00:50:00 | GOES-19 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 48.8 |
| 1bbc4575-3add-3261-8e3f-a786ea236160 | -14.3415 | -53.7904 | 2025-10-18 00:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 105.9 |
| d147ccdb-3676-3dab-998a-de544e751078 | -5.0029 | -46.0108 | 2025-10-18 00:50:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 129.1 |
| 517f4d70-caee-30ad-8cb1-5cb73f6e0232 | -4.4633 | -43.2152 | 2025-10-18 00:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 174.8 |
| 265fee26-cd11-3a8f-b38b-84dc89247cd6 | -11.6109 | -44.0678 | 2025-10-18 00:50:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 204.1 |
| 8aab309e-790f-3206-8693-c5c6ff5aa9ee | -13.2296 | -43.9692 | 2025-10-18 00:50:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 734d632d-99ab-3601-820c-f72124189f08 | -2.9128 | -52.7146 | 2025-10-18 00:50:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 76.7 |
| ccd2702d-6726-3069-9079-c21464bb7735 | -17.4377 | -40.0863 | 2025-10-18 00:50:00 | GOES-19 | MEDEIROS NETO | BAHIA | Brasil | 2921104 | 29 | 33 | nan | nan | nan | Mata Atlântica | 167.4 |
| 1972df0a-d8b2-35b0-9544-5664ec9ee252 | -11.204 | -47.8318 | 2025-10-18 00:50:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 35.9 |
| 3aef676d-53ab-3362-8389-cfbeaea451e9 | -14.3418 | -53.7695 | 2025-10-18 00:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 739c7122-9c1a-3939-a662-d26930542ef2 | -17.4587 | -40.0547 | 2025-10-18 00:50:00 | GOES-19 | MEDEIROS NETO | BAHIA | Brasil | 2921104 | 29 | 33 | nan | nan | nan | Mata Atlântica | 64.6 |
| f762129c-8f27-388a-a10b-74820a96468f | -11.6104 | -44.0913 | 2025-10-18 00:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 115.0 |
| d6610702-ee32-3391-9288-6a5b5f459ed6 | -14.3222 | -53.7927 | 2025-10-18 00:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 9ac237e8-6a36-3481-96a3-60bb03a278f3 | -18.37915 | -55.44725 | 2025-10-18 00:50:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.0 |
| 5b5ea061-7504-3fe3-a1e0-929590bb8a81 | -18.3926 | -55.47605 | 2025-10-18 00:50:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 94.0 |
| b6e91245-7caa-3007-891a-1db0fb589afd | -19.8646 | -48.32254 | 2025-10-18 00:50:00 | TERRA_M-M | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 7e8e3b3c-559a-34b4-9c8e-28db70c29f8a | -18.38066 | -55.45938 | 2025-10-18 00:50:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.5 |
| b2260568-cf45-34e4-bed7-b2b9dc5a8c6c | -18.37823 | -55.44094 | 2025-10-18 00:50:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 22.0 |
| fc65a70b-a97c-3048-8308-c934cfad1073 | -19.1065 | -57.5497 | 2025-10-18 00:50:00 | TERRA_M-M | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 26.5 |
| 406b894f-cfb5-3141-bd62-b5a8f84d1a14 | -20.51341 | -57.46974 | 2025-10-18 00:50:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.4 |
| 3bb6185b-16e2-33b4-805b-6feb492e4475 | -15.7996 | -43.56064 | 2025-10-18 00:50:00 | TERRA_M-M | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 30.3 |
| 52a17c9b-080a-3ed6-a6b7-c15790ee0df7 | -18.38254 | -55.47741 | 2025-10-18 00:50:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 43.8 |
| 4f62a9a6-d226-34b5-b263-762105b01881 | -17.96077 | -46.73957 | 2025-10-18 00:50:00 | TERRA_M-M | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 0d3b842f-f313-337e-9fa7-6c601350d4bd | -19.28491 | -46.51636 | 2025-10-18 00:50:00 | TERRA_M-M | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 4e594854-489a-3ef0-ada4-9b8ff87356cd | -18.39116 | -55.46387 | 2025-10-18 00:50:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 32.8 |
| a264f09d-eeb2-39fd-a489-fb051f3d2156 | -17.8493 | -42.62519 | 2025-10-18 00:50:00 | TERRA_M-M | ARICANDUVA | MINAS GERAIS | Brasil | 3104452 | 31 | 33 | nan | nan | nan | Mata Atlântica | 60.5 |
| df08127c-e69b-3fe2-a474-a0bd43296b03 | -17.85568 | -42.63007 | 2025-10-18 00:50:00 | TERRA_M-M | ARICANDUVA | MINAS GERAIS | Brasil | 3104452 | 31 | 33 | nan | nan | nan | Mata Atlântica | 41.2 |
| b9fe51fc-6c4f-3560-80c0-2bd4566aa97c | -17.37339 | -46.68008 | 2025-10-18 00:50:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 267d7162-d990-306c-bcda-96736f8de46b | -17.95738 | -46.73454 | 2025-10-18 00:50:00 | TERRA_M-M | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 12.4 |
| f92a3a65-f797-3e68-ac72-d0984e75414d | -15.80342 | -43.56659 | 2025-10-18 00:50:00 | TERRA_M-M | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 40.7 |
| 54094afd-cbe5-3992-8a26-627ebc56a79a | -18.38217 | -55.47152 | 2025-10-18 00:50:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 65.0 |
| dd984a81-d61f-3448-8145-a896da9250c5 | -18.37764 | -55.43513 | 2025-10-18 00:50:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 20.2 |
| bbdfc8cf-5ccd-3174-b13c-781c4ca3952a | -18.38369 | -55.4837 | 2025-10-18 00:50:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.7 |
| 18c9b959-fd66-3f29-9c26-12fc4c1c3bbb | -19.86646 | -48.33444 | 2025-10-18 00:50:00 | TERRA_M-M | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 6e0fab52-092e-3c47-acb7-abf9810bc233 | -18.3811 | -55.46523 | 2025-10-18 00:50:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 25.7 |
| bc1023b0-145b-3c93-b066-479cc8b28437 | -17.96017 | -46.7508 | 2025-10-18 00:50:00 | TERRA_M-M | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 0c7d23d4-ea32-3ed7-98d5-94e3780d8290 | -9.87927 | -49.12463 | 2025-10-18 00:52:00 | TERRA_M-M | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 45088920-6108-35b4-aeda-5310676996e0 | -13.46357 | -43.78706 | 2025-10-18 00:52:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 39.3 |
| 5af10bfb-8a3c-3416-a68b-f4fcd5589d25 | -9.21933 | -46.85497 | 2025-10-18 00:52:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 249c6f62-76c8-3802-ac28-63d1591a33a6 | -8.10551 | -45.42842 | 2025-10-18 00:52:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 30.3 |
| e9699d73-54e7-397f-b7e9-b2cd012afead | -11.47551 | -44.02483 | 2025-10-18 00:52:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 26.7 |


[Clique aqui para ver as próximas entradas](README4.md)

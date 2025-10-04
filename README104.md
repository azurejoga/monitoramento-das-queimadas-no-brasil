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

## Dados Diários - Página 104

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 06d99410-bd95-33db-a528-d94897d48eed | -7.47376 | -43.0445 | 2025-10-04 05:04:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| c7ecc5db-5a4f-3d93-a3fb-b8df9a8732cb | -9.33778 | -54.51366 | 2025-10-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d8c12e1a-1cd1-3533-a9b8-a8cbc3886c94 | -10.7758 | -45.33207 | 2025-10-04 05:04:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ca363074-b58c-3ae1-8965-140b67e7cd47 | -8.61775 | -54.96356 | 2025-10-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6433adcf-02b1-3667-9a7b-6d6b00d5caf4 | -3.84395 | -41.58309 | 2025-10-04 05:04:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| f80c34c2-3d24-3ec3-a2bd-ba112f280358 | -7.73921 | -42.60521 | 2025-10-04 05:04:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 65eb2bc5-515a-374d-81c4-678212babdaa | -5.79173 | -45.77342 | 2025-10-04 05:04:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 61f91411-402b-34bf-bc77-eccebd06aebb | -7.64406 | -46.76901 | 2025-10-04 05:04:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 862786a6-757b-3599-8e84-a46ee5ca97a7 | -6.3513 | -43.4534 | 2025-10-04 05:04:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 65898a88-3b34-3fae-8061-f0b4c8ac943a | -6.17743 | -43.91719 | 2025-10-04 05:04:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 08048566-7a04-3259-861f-916896b53a20 | -9.91272 | -43.73702 | 2025-10-04 05:04:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 2a3fa20e-93a4-390f-973b-cde47c01ef0f | -6.87912 | -47.23144 | 2025-10-04 05:04:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b5c0f5e8-8d1c-3415-abda-8ce1ae7801d5 | -4.95768 | -45.07533 | 2025-10-04 05:04:00 | NOAA-21 | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| c446252a-8105-3d21-989a-3edc4cb74821 | -2.97324 | -53.09191 | 2025-10-04 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d482be47-7ff6-3a9e-a83d-008004c826a9 | -9.97682 | -50.24065 | 2025-10-04 05:04:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c3e45252-d620-3796-a39e-38c8b69150d2 | -5.20265 | -45.06274 | 2025-10-04 05:04:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| f25b6d95-f121-3026-b289-07032490f01c | -8.50767 | -54.59742 | 2025-10-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d7f99f5c-54d8-3910-8704-962c0be507f3 | -6.65775 | -42.81752 | 2025-10-04 05:04:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 74b980e8-cef5-3a82-baaa-6e5671f73c94 | -9.35952 | -45.78469 | 2025-10-04 05:04:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 065040f4-b627-3a2d-a2de-c8604572ffab | -6.28073 | -44.03859 | 2025-10-04 05:04:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| a8387ea6-a063-3b69-b6ef-2303ec219782 | -6.17338 | -43.92887 | 2025-10-04 05:04:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| aa3d72a4-b1ad-3c92-868f-bb62b35a80a0 | -2.69874 | -52.82567 | 2025-10-04 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f5b33489-6ecf-38e0-8375-3030024b7a94 | -10.53788 | -44.52367 | 2025-10-04 05:04:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 57fb47b1-50aa-30b8-ae8c-6111ab58d0aa | -10.3416 | -48.17157 | 2025-10-04 05:04:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7a8a6b20-d303-3b79-a86b-cc80b4378362 | -9.32075 | -54.53413 | 2025-10-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2ee21053-6e9d-30d1-b3e4-d2798380a5a1 | -8.87133 | -47.81988 | 2025-10-04 05:04:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3b573ac7-9ec4-3503-8d85-d8acf08c2123 | -6.37697 | -43.89957 | 2025-10-04 05:04:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 36c43b33-f5c5-3c66-803a-de2bf12ef742 | -8.11258 | -55.09038 | 2025-10-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 27ed1f34-1e3c-3a94-b3ea-ab7b0bc32def | -4.43672 | -43.23888 | 2025-10-04 05:04:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| d455126c-4f85-3f04-8575-838969f3510d | -6.24863 | -45.35038 | 2025-10-04 05:04:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 54f71ea9-3e9c-3f1d-8f28-4d93b4495517 | -9.32633 | -45.7618 | 2025-10-04 05:04:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 053a4da3-94b0-3f20-bf85-6e9a6e187399 | -9.36001 | -45.78076 | 2025-10-04 05:04:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 41ca3399-b24c-342b-8bd1-ead17dab1a1f | -7.05043 | -42.77003 | 2025-10-04 05:04:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| ccedd73a-ed06-3b01-af55-c063a2060e7d | -8.19888 | -46.99011 | 2025-10-04 05:04:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5bf5c15a-fda2-329a-a950-17e082c20e7d | -6.34395 | -43.45831 | 2025-10-04 05:04:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9e663959-d1af-3d58-924d-b8d13a4e6ba3 | -9.88317 | -47.81724 | 2025-10-04 05:04:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4fda3df3-8d92-3910-b331-4cc9326755ce | -2.90238 | -50.7314 | 2025-10-04 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 788af06e-f318-3be0-9ca0-c11b6224e933 | -6.35073 | -43.452 | 2025-10-04 05:04:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 961c6c95-3fab-3786-9545-ed31c2493d41 | -8.62345 | -54.99384 | 2025-10-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 14ba78b2-721f-3908-ab9e-87d0cfe4e76e | -8.91429 | -50.77906 | 2025-10-04 05:04:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c1cc94a1-bfcf-31b3-9af2-bd89b1c7078d | -3.84763 | -41.57629 | 2025-10-04 05:04:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 14.3 |
| 3e01e50f-e1b8-365f-95a3-894d514eb406 | -8.52193 | -50.03653 | 2025-10-04 05:04:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fb75dfd6-320a-37ac-8f4a-3f139e6e3a6b | -8.6268 | -54.99435 | 2025-10-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 63906d02-fc7a-3339-be80-281307455945 | -8.99414 | -47.48869 | 2025-10-04 05:04:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 594d04ab-6c2a-3596-a5b8-cf9cdb76740c | -8.62337 | -54.97176 | 2025-10-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 68e17db1-fa9c-3ca9-afbb-b5d44684c4b0 | -6.28303 | -44.04445 | 2025-10-04 05:04:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6eee823f-e30d-364d-abcf-00125f59ff00 | -3.88091 | -52.19153 | 2025-10-04 05:04:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 532eaf3f-0599-3f46-bea0-e0e8dfe369f5 | -7.86163 | -48.19421 | 2025-10-04 05:04:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| edac45bf-8deb-3d3c-9ea7-5e20bb45ef58 | -3.66222 | -50.27225 | 2025-10-04 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3402cb70-d021-33d0-865a-2d53aab7f150 | -8.62563 | -54.97948 | 2025-10-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5c9f4a1e-825e-3959-875b-cbca6d949d40 | -6.24678 | -44.2482 | 2025-10-04 05:04:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 40eba7b7-cb28-3bcc-ae65-64f8ae64222d | -8.61104 | -54.96253 | 2025-10-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 109628ee-7b25-3214-ace1-ada8f5132be0 | -6.17479 | -43.91863 | 2025-10-04 05:04:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 19209ab6-2c3f-3176-83f9-cd767297fd4b | -5.07994 | -44.09349 | 2025-10-04 05:04:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 64d53cf2-d798-3a40-9714-bde2a9895cdd | -6.27738 | -44.03868 | 2025-10-04 05:04:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 37e7b600-b96b-3b4f-805a-183cab58d3b0 | -9.6644 | -48.20433 | 2025-10-04 05:04:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d36259c6-8ba6-3222-a7b3-9dc462f41f0a | -8.46751 | -47.42046 | 2025-10-04 05:04:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7e75a5f5-88fc-3979-af5c-0ab10b7c051f | -6.38329 | -46.50986 | 2025-10-04 05:04:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fab60e9d-4754-3a80-9325-23f8ed1303fb | -3.86383 | -51.81531 | 2025-10-04 05:04:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d0c9a6a7-234a-3cd5-9a77-397483e5a1f1 | -9.7533 | -43.61695 | 2025-10-04 05:04:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 50368fdb-1af8-3793-8af4-082646b3116a | -9.91202 | -43.7428 | 2025-10-04 05:04:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| c9992c52-3485-3505-9aaa-cd77672b1292 | -9.94045 | -50.2443 | 2025-10-04 05:04:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b42de195-00ab-3db7-b60c-7ecb7d013533 | -8.7124 | -47.9861 | 2025-10-04 05:04:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ba111bec-8378-3e4e-81d1-30b48a3bc9c7 | -9.92331 | -50.20446 | 2025-10-04 05:04:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7128a777-01a8-3fe6-870a-c7cc2a4cbdaf | -9.94044 | -50.24244 | 2025-10-04 05:04:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 448b850f-8b5e-323c-b5cd-7de6202187a5 | -9.10457 | -44.39806 | 2025-10-04 05:04:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f5a6e054-f8f3-36e0-9865-c6ea3fdb441c | -6.66825 | -42.83199 | 2025-10-04 05:04:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| fd209cd1-11ff-3a60-bb9c-3bc74cbeb84e | -4.51863 | -50.47981 | 2025-10-04 05:04:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 093eff49-a7e3-3ffd-ab9d-ccb945666b63 | -7.04891 | -42.78732 | 2025-10-04 05:04:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| c7a1daeb-6315-341c-84a7-737afd029cd3 | -9.99088 | -48.2811 | 2025-10-04 05:04:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a89182a0-b6da-3b0d-9e7e-14d7b1ea4b72 | -8.7132 | -47.98022 | 2025-10-04 05:04:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ef4267c9-dd02-30b0-9124-78ac7d7b2d45 | -9.08453 | -48.02774 | 2025-10-04 05:04:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 499ca0c7-ec56-3ae5-bd19-505cb3abd687 | -3.89082 | -52.15097 | 2025-10-04 05:04:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e07515f4-d753-398a-99a9-da41eb2f7190 | -8.05725 | -44.79825 | 2025-10-04 05:04:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7b7a1f13-bfff-373b-b4cb-05cf50e16759 | -7.7016 | -42.57524 | 2025-10-04 05:04:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 46dd28bc-e9e1-331f-b213-8fb5b685f3cd | -9.32871 | -54.52762 | 2025-10-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f3e2fd49-1767-33a9-8315-1c7da3038f9e | -8.53233 | -47.21333 | 2025-10-04 05:04:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9b435f80-105a-35d8-8563-ad4b8ce8e880 | -7.79497 | -42.55899 | 2025-10-04 05:04:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| a7016544-5084-32f9-b841-559b6e3685ed | -8.62618 | -54.97588 | 2025-10-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 86c763b2-91f0-3126-8023-8cc7dbe261c3 | -5.98191 | -43.48787 | 2025-10-04 05:04:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 85674e8d-4072-3194-a1c3-44e744292858 | -4.4424 | -43.24541 | 2025-10-04 05:04:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 38.6 |
| 3dff1c32-eba9-3902-82a1-7225abc0c1fc | -9.92963 | -50.89917 | 2025-10-04 05:04:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 995b1667-4abe-3cff-862d-9591bdb4c259 | -9.33786 | -45.77869 | 2025-10-04 05:04:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1fff1aa5-87b2-371a-8f42-b9e2ba0320d8 | -7.75866 | -42.521 | 2025-10-04 05:04:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 8dfe6fe6-aace-3f69-b528-b7cc15e011e2 | -9.9386 | -50.89644 | 2025-10-04 05:04:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 82e735de-e9d0-3fea-9ab2-9ec0fd06badc | -4.95302 | -45.06604 | 2025-10-04 05:04:00 | NOAA-21 | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| bc5d0626-a9ea-3b5c-bd46-54afffb8f9f9 | -8.95888 | -48.68546 | 2025-10-04 05:04:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 1bc3ca5b-5f11-326a-b5e1-40ecf599b060 | -3.30921 | -48.71007 | 2025-10-04 05:04:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 699d3aea-d76c-3224-9a43-bf9888411026 | -9.76834 | -48.57861 | 2025-10-04 05:04:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0ba0e91e-8e0d-3383-b2a2-32d58460d784 | -8.22936 | -46.80518 | 2025-10-04 05:04:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7ebcf527-428f-3fcf-9578-504c277a96c6 | -9.94167 | -50.23376 | 2025-10-04 05:04:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 09b1d19b-2e46-33f7-a3cd-3a2029515f7a | -6.34343 | -43.45679 | 2025-10-04 05:04:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 00628d39-5c1a-3cd6-96a6-12037d1f86b0 | -4.58828 | -47.03706 | 2025-10-04 05:04:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 073dd481-8f18-348b-b596-1f1c8c6f13d8 | -8.19841 | -46.99363 | 2025-10-04 05:04:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 94adc13c-ad77-35fc-8687-3452f5f1c36f | -9.31845 | -54.52606 | 2025-10-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2edf3d6a-b844-3789-89dd-d17ce955c29f | -6.24795 | -44.23936 | 2025-10-04 05:04:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 58cf229d-fe54-3feb-8b68-f604dbeba4d2 | -5.19675 | -45.06234 | 2025-10-04 05:04:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 6ea4b83c-7be3-3e9c-955e-aef2ecad8300 | -7.72939 | -46.29602 | 2025-10-04 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 5879b3e1-9539-3e6f-b0a8-2d491112e319 | -4.31365 | -48.08848 | 2025-10-04 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6e8088a1-1a22-3682-a570-cf93bf0da1da | -8.60995 | -54.96971 | 2025-10-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README105.md)

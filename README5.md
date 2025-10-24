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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cc6197e5-3d11-3cb8-9920-2bd46f7ee9f2 | -6.0242 | -48.90386 | 2025-10-24 03:47:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 211b54be-f1d7-3808-9f17-56dc8ceb79b4 | -8.31176 | -39.13111 | 2025-10-24 03:47:00 | NOAA-21 | CABROBÓ | PERNAMBUCO | Brasil | 2603009 | 26 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 7a74fe7b-b027-3c08-a8e4-fdc8b4c50e70 | -7.82295 | -45.37685 | 2025-10-24 03:47:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5afc5451-3099-3f4b-9647-e70bee991624 | -7.55548 | -47.36988 | 2025-10-24 03:47:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 0ef81544-f8a3-3bcc-8dbc-3e0b407930fa | -8.34476 | -46.18332 | 2025-10-24 03:47:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 63a2047a-bc22-3c8e-a8ba-6fc23c72149a | -6.01059 | -45.87486 | 2025-10-24 03:47:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 56741deb-ef8f-331d-ae8a-4d6d877d0b83 | -8.10803 | -47.0489 | 2025-10-24 03:47:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b772384d-99ae-384c-ac80-11e9a2215c6d | -6.77938 | -45.47043 | 2025-10-24 03:47:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a52ee711-328e-3282-aee9-cb7393557043 | -6.02301 | -48.90996 | 2025-10-24 03:47:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b9c9ea4e-8240-333d-8f43-c4c4d203fed5 | -8.82773 | -45.41852 | 2025-10-24 03:47:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6c7c4ec5-64cd-313a-9d4b-ae373c0b98c4 | -6.79293 | -46.46604 | 2025-10-24 03:47:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 20ab3b98-c041-31f9-abac-92e18a1ccde5 | -7.63047 | -42.18797 | 2025-10-24 03:47:00 | NOAA-21 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| d46bf1df-47a7-3b64-8de3-4622675280c7 | -6.30067 | -41.88917 | 2025-10-24 03:47:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 092921b3-1f10-348e-b0ce-99c1aa37b562 | -6.02399 | -48.90449 | 2025-10-24 03:47:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0e4c1c3d-2598-37a1-af1f-a5e3cd1d69d2 | -8.34233 | -46.19688 | 2025-10-24 03:47:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ce9ea759-f32e-3c10-b34f-1aa85fea290c | -8.32793 | -46.24685 | 2025-10-24 03:47:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 15d41aca-be62-386f-b494-dbcbed142f2d | -7.6327 | -42.1996 | 2025-10-24 03:47:00 | NOAA-21 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0ac1fb34-b1cd-335c-8924-404d04b73bd6 | -8.6939 | -47.1147 | 2025-10-24 03:47:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 63b46c4b-1f17-3609-8c97-3a183ce8a2fc | -6.99433 | -38.05384 | 2025-10-24 03:47:00 | NOAA-21 | COREMAS | PARAÍBA | Brasil | 2504801 | 25 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 946aa1af-bb75-35ad-b383-5b45707a1130 | -7.6887 | -42.23912 | 2025-10-24 03:47:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 8e83afb3-f7a2-3986-9488-3aab6d6612aa | -6.8418 | -41.55376 | 2025-10-24 03:47:00 | NOAA-21 | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| cccb3e1e-6d84-3c79-b232-32da717ad9d0 | -6.89339 | -38.27621 | 2025-10-24 03:47:00 | NOAA-21 | SOUSA | PARAÍBA | Brasil | 2516201 | 25 | 33 | nan | nan | nan | Caatinga | 1.5 |
| fe94bf1f-67f3-3d1b-a119-6bd299d44888 | -2.87397 | -45.25812 | 2025-10-24 03:47:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 9.7 |
| d68e767c-7f3f-3cd4-ab82-356a2a9d5f2b | -6.80511 | -42.39449 | 2025-10-24 03:47:00 | NOAA-21 | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| b5a58ebe-c3a2-3f31-a046-f0cf85ddf3ad | -7.54972 | -47.36891 | 2025-10-24 03:47:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| d29f6d58-a486-3240-9843-3c40e08bc5cb | -8.69461 | -47.11091 | 2025-10-24 03:47:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e1f7b4b7-28d5-3588-9794-64e45958dcff | -7.06167 | -35.73555 | 2025-10-24 03:47:00 | NOAA-21 | ALAGOA NOVA | PARAÍBA | Brasil | 2500403 | 25 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 5bf6dfd8-e620-3299-80c1-e3c844f838ad | -7.27128 | -50.00557 | 2025-10-24 03:47:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 103fc352-7a42-362a-80c5-b1b7e482d6c3 | -6.28457 | -47.01402 | 2025-10-24 03:47:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 99f86e98-3960-3cd1-a4fb-d5e9bc6d8cab | -4.91669 | -47.32887 | 2025-10-24 03:47:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 875048fc-e57c-33a4-8e4d-92c77fb1c2b4 | -7.6376 | -42.17032 | 2025-10-24 03:47:00 | NOAA-21 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 92ad9001-8f4b-31b9-94ad-1728694288b3 | -8.03812 | -39.87149 | 2025-10-24 03:47:00 | NOAA-21 | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 1.8 |
| bfcea05e-91a3-35c7-8cb4-ba1fbdfafdf2 | -8.11368 | -47.04953 | 2025-10-24 03:47:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f5ea85a4-1bd2-3a2d-8dc2-0f50ebf33af5 | -6.27677 | -47.01769 | 2025-10-24 03:47:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1f872a4a-af8b-33d4-879f-c3774ae0d2a8 | -7.62683 | -42.20974 | 2025-10-24 03:47:00 | NOAA-21 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 1a66db40-9108-31b6-b4bc-fb40b675a9e9 | -8.34164 | -46.20077 | 2025-10-24 03:47:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5afbaa88-eb83-3c70-9eeb-e6fe41542b6c | -6.84661 | -41.54926 | 2025-10-24 03:47:00 | NOAA-21 | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| b1615f1c-c2fc-3ee2-8360-0265e4fb4350 | -7.62923 | -41.85294 | 2025-10-24 03:47:00 | NOAA-21 | CAMPINAS DO PIAUÍ | PIAUÍ | Brasil | 2202109 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 68c7a99e-1346-3cb7-a781-4cb285feae54 | -6.22671 | -41.37656 | 2025-10-24 03:47:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| aea9e7b9-26e4-3357-9873-4fc70bd40a38 | -5.4071 | -46.41005 | 2025-10-24 03:47:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 410faf2c-7c89-39b6-9d8c-286afc1fa2f0 | -7.63725 | -42.29822 | 2025-10-24 03:47:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 5288cdef-96bd-33b2-92cf-0601267a718d | -7.14337 | -45.04708 | 2025-10-24 03:47:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ef4998ee-0967-32b3-a0c4-d23e5c03c6e8 | -7.55694 | -47.36195 | 2025-10-24 03:47:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 29d3fbb3-ff1c-3db1-8042-a8bd696303b9 | -7.62744 | -42.2061 | 2025-10-24 03:47:00 | NOAA-21 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| cc8d7f8f-4e2d-3520-aede-ad1bcac41346 | -8.12002 | -47.04646 | 2025-10-24 03:47:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 210aded4-b6de-3862-95b3-f0070e45ef00 | -6.18386 | -41.53657 | 2025-10-24 03:47:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a219aad2-a7f2-3383-ab1c-4140b3c05026 | -5.48114 | -46.47124 | 2025-10-24 03:47:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ecd85972-9024-3fb8-a978-319c7114cb9a | -6.88597 | -43.61311 | 2025-10-24 03:47:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 08ef7fd7-9bcc-3d4e-b8a9-1e0fc923f41f | -9.3431 | -40.21738 | 2025-10-24 03:47:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 50f764fb-305c-3495-b967-7fbbb9c11d78 | -6.09018 | -46.23515 | 2025-10-24 03:47:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| dfcedead-34c2-369e-a204-7e25c953d809 | -7.684 | -42.24209 | 2025-10-24 03:47:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| fd19cc7d-3fba-3bc6-a4fb-dace379550dd | -7.73438 | -47.01307 | 2025-10-24 03:47:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 89039c8e-a442-39cf-952e-6517ad7aaf2f | -7.00718 | -45.20771 | 2025-10-24 03:47:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 87b37e49-26d8-3616-beff-59ee00e69268 | -8.61231 | -44.81635 | 2025-10-24 03:47:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 87af2320-51c1-3654-8b01-a13e09fa289b | -2.26248 | -47.85137 | 2025-10-24 03:47:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 526680c0-6fab-3956-8c99-2df8a6adc92a | -8.11593 | -47.04602 | 2025-10-24 03:47:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 86b7f043-365d-3e9e-b06a-25643fa70ad9 | -6.43503 | -45.67041 | 2025-10-24 03:47:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 491fc23d-aac3-3432-8a93-637a986aa35a | -7.83248 | -45.38152 | 2025-10-24 03:47:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bd599294-aba9-3f8e-9214-f2acf068f2bd | -7.5376 | -38.54971 | 2025-10-24 03:47:00 | NOAA-21 | CONCEIÇÃO | PARAÍBA | Brasil | 2504405 | 25 | 33 | nan | nan | nan | Caatinga | 2.6 |
| a700f616-69e2-3679-adae-0c92a5c6c4c8 | -7.69276 | -42.23988 | 2025-10-24 03:47:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| aa176b13-eb19-3eca-aaca-3f35773749fc | -8.51016 | -44.20545 | 2025-10-24 03:47:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2e5dcd09-664b-3ebc-9a5e-3a70c97029a7 | -8.17792 | -47.76625 | 2025-10-24 03:47:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2becc9f2-be24-32b0-9504-d954d3636937 | -8.20535 | -46.98876 | 2025-10-24 03:47:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 9260f6a1-ef01-3081-be26-4af3af2fb8a2 | -5.82062 | -46.21643 | 2025-10-24 03:47:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 41a51c78-b1a0-308b-89b9-6880824c77e5 | -8.66809 | -44.77932 | 2025-10-24 03:47:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3f3c254f-9e2b-30b4-ae95-80fd50585203 | -1.1064 | -48.87951 | 2025-10-24 03:47:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f16df653-476e-3aef-b32f-853f908fc6a1 | -6.09023 | -46.23151 | 2025-10-24 03:47:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 73114db7-7b75-3c29-b621-7fd835a21605 | -6.84576 | -41.55434 | 2025-10-24 03:47:00 | NOAA-21 | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 94747039-25f8-305e-af96-48490bc0b5ab | -6.27747 | -47.01372 | 2025-10-24 03:47:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b3d08ee9-056c-3894-a3d6-f93625c46c9c | -6.23065 | -41.37719 | 2025-10-24 03:47:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b3584873-c2c7-3cc5-a5eb-0d7c9912e3bd | -6.11918 | -41.74989 | 2025-10-24 03:47:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 851f6d36-d593-3bb1-a114-ed1e0a8e9bd5 | -6.77681 | -45.47252 | 2025-10-24 03:47:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c167bffd-f8aa-3366-8020-93c4ac42a7e3 | -4.8208 | -48.67065 | 2025-10-24 03:47:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| eb3aa7c3-c168-3430-bb64-741182998b34 | -8.64554 | -44.7957 | 2025-10-24 03:47:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 79060e7d-b7ff-3c56-bbb4-41b1b2c3de96 | -4.87745 | -47.54641 | 2025-10-24 03:47:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d83e2827-812c-3c43-ab34-f0a9ab3f505d | -6.01116 | -45.87157 | 2025-10-24 03:47:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 83abecd1-4b5b-3dea-90e3-91a983a1a775 | -6.31436 | -41.85782 | 2025-10-24 03:47:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| a0abc11d-5658-3dc7-9c63-1eb109704949 | -2.2689 | -47.85252 | 2025-10-24 03:47:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| fffd5cf7-258b-325f-a22d-bca61a07789f | -6.89456 | -38.26894 | 2025-10-24 03:47:00 | NOAA-21 | SOUSA | PARAÍBA | Brasil | 2516201 | 25 | 33 | nan | nan | nan | Caatinga | 2.5 |
| e0b3099b-f704-3636-a65e-5f06831ea7f8 | -5.47551 | -46.47033 | 2025-10-24 03:47:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b15e71b7-3b78-30ec-9aca-10b6a2db85f6 | -6.43561 | -45.66719 | 2025-10-24 03:47:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5f2025e1-937e-3c60-8180-5c2f424b4685 | -7.00668 | -45.2106 | 2025-10-24 03:47:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e814f1e6-b34d-3560-a422-60090b9bcd6c | -7.63676 | -42.20034 | 2025-10-24 03:47:00 | NOAA-21 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a1256e80-f44b-30f1-8441-711db452f127 | -4.81978 | -48.6763 | 2025-10-24 03:47:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 18.2 |
| e21d62e7-fdad-3faf-9710-4ff71b7fa594 | -6.08743 | -40.57224 | 2025-10-24 03:47:00 | NOAA-21 | PARAMBU | CEARÁ | Brasil | 2310308 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 28bb101e-6198-3fff-833b-c78f45be24f5 | -6.28322 | -47.0147 | 2025-10-24 03:47:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bd8ba373-2ea3-3b09-8138-b69079872dca | -6.77883 | -45.47346 | 2025-10-24 03:47:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c94c06cc-c95c-3db6-be61-3f00af5935dd | -7.4655 | -44.609 | 2025-10-24 03:47:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6067fdcd-38aa-3494-8d9c-f34b513719ec | -6.1321 | -41.72253 | 2025-10-24 03:47:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| b4f8d1e1-5d61-3abb-973e-a24da0394b3b | -8.61804 | -44.8119 | 2025-10-24 03:47:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f5c556e5-1c4b-348d-a902-835b1c296897 | -7.83712 | -45.59336 | 2025-10-24 03:47:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 449bd150-a8fa-3979-b6a6-dcb57958880b | -7.6315 | -42.20681 | 2025-10-24 03:47:00 | NOAA-21 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 94961364-001d-3f18-931d-ed82aa73941a | -6.92575 | -44.0148 | 2025-10-24 03:47:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 17852835-51d4-3c0a-875e-aee7f80be219 | -6.44418 | -43.82008 | 2025-10-24 03:47:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| b638d1d9-0ed2-3653-a110-6245a8c01dba | -6.73201 | -44.14848 | 2025-10-24 03:47:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7fbe4a1c-1bd1-3665-97bc-61e5e222c3b7 | -6.61637 | -43.66804 | 2025-10-24 03:47:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fac9280f-3548-3fef-8376-bebc78eee9e7 | -8.65205 | -44.78672 | 2025-10-24 03:47:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c7a1978a-642e-3b7c-9e0a-14947a09f6bc | -7.78642 | -45.40721 | 2025-10-24 03:47:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 618536cc-3513-3d59-8daf-67f41c1fa2fb | -6.31002 | -41.88334 | 2025-10-24 03:47:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| df17dec7-c554-30f0-9a46-07dfc4beca5f | -6.30128 | -41.88559 | 2025-10-24 03:47:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |


[Clique aqui para ver as próximas entradas](README6.md)

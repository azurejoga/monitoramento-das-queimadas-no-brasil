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
| ed06909e-45a3-33b4-b986-c4032a191621 | -18.06875 | -57.5369 | 2025-10-11 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 0dec0099-b8ac-3267-8f78-75a4c77981c0 | -17.90259 | -57.66976 | 2025-10-11 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 0a5e04a2-3f4e-3213-aacb-cc75058843eb | -17.29099 | -50.97035 | 2025-10-11 01:09:00 | TERRA_M-M | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 48.6 |
| 87ba083f-8656-3ac7-af94-7425ff47aa5f | -17.82841 | -57.66801 | 2025-10-11 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.2 |
| aeece694-b09a-343e-b11b-1c61ed58c99c | -15.17827 | -56.75213 | 2025-10-11 01:09:00 | TERRA_M-M | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 5ceaee05-1690-3b0b-914e-ed11481ffbd9 | -17.89001 | -57.50943 | 2025-10-11 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 3095d2c8-21e7-36a1-ab0e-3647275a2446 | -15.86766 | -56.74426 | 2025-10-11 01:09:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 62d49142-b87d-37d5-9360-87e7277c6b47 | -15.21166 | -56.85989 | 2025-10-11 01:09:00 | TERRA_M-M | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 78492cf1-ef6c-39f9-9401-a4ac5eadc093 | -17.96024 | -57.617 | 2025-10-11 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 8b1e9e01-d37b-36d6-b62e-a04516be5f02 | -15.17695 | -56.74292 | 2025-10-11 01:09:00 | TERRA_M-M | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| b61d8613-c2ed-354f-bf75-ba35e93d5ca5 | -17.8221 | -57.62129 | 2025-10-11 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 47722580-3874-3fb8-9d64-2a1162ddcbb9 | -16.29716 | -47.15709 | 2025-10-11 01:09:00 | TERRA_M-M | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 27.2 |
| de0aa55a-b64b-358d-9fce-d5f1fc47e324 | -18.04462 | -57.5597 | 2025-10-11 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.7 |
| 5c745784-77b5-3eef-a2bb-1e897c40815c | -15.69793 | -46.62642 | 2025-10-11 01:09:00 | TERRA_M-M | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 49.0 |
| a48baa00-b40b-33c2-8d54-9136e6fbbf21 | -17.84493 | -57.65597 | 2025-10-11 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.3 |
| c47ab477-7d16-3a6e-9998-d90fcf0f31df | -15.22266 | -56.74547 | 2025-10-11 01:09:00 | TERRA_M-M | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| cccdb4fc-88d5-3df2-825b-90143184fdb6 | -17.89368 | -57.67107 | 2025-10-11 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.4 |
| 901c3824-3d75-3bde-a5fa-d761c7498ca5 | -17.2873 | -50.97689 | 2025-10-11 01:09:00 | TERRA_M-M | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 5e5dd7f2-64da-381f-9c12-7eaa630cba38 | -17.29937 | -50.97441 | 2025-10-11 01:09:00 | TERRA_M-M | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 59.3 |
| b22b58ad-dba5-3419-842d-9f879cbbb1f5 | -15.16007 | -56.82702 | 2025-10-11 01:09:00 | TERRA_M-M | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 00d4b627-f72c-334a-8483-234021c190de | -17.82335 | -57.63054 | 2025-10-11 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.9 |
| 7834b974-b7cc-3aad-b9b0-251ac2a87530 | -15.699 | -46.61899 | 2025-10-11 01:09:00 | TERRA_M-M | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 33.7 |
| 5d146302-0036-3ce2-a27d-9f6b7f42146a | -15.03019 | -49.4471 | 2025-10-11 01:09:00 | TERRA_M-M | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 35.7 |
| 299711d2-7866-353a-b3be-a7977e51f73e | -17.8437 | -57.57993 | 2025-10-11 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.6 |
| 28224b85-be6a-35ad-bcd0-17099cb226c2 | -13.2057 | -42.345 | 2025-10-11 01:10:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 423.5 |
| c110b5ad-d5e8-3229-99b9-30a7faca4a6d | -13.2252 | -42.3414 | 2025-10-11 01:10:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 547.7 |
| 03293a28-8e57-3021-a926-04b6ec786e18 | -13.2257 | -42.317 | 2025-10-11 01:10:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 157.0 |
| 8e6ccfe9-cc08-34bd-ac04-1796440c10cf | -7.8645 | -44.4692 | 2025-10-11 01:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 316.8 |
| e04bb388-bdf5-3e1b-8287-236d6c6a5864 | -17.2722 | -46.8932 | 2025-10-11 01:10:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 0a32157b-d2e2-33ea-a023-942932663d8b | -5.871 | -42.8357 | 2025-10-11 01:10:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 58.7 |
| d3c7eeb2-310e-3c96-82d4-65fa307aebbe | -11.7589 | -43.3136 | 2025-10-11 01:10:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 4733bd0c-b230-3c9d-83ba-be7ae302adb9 | -7.8457 | -44.4711 | 2025-10-11 01:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 226.1 |
| 9c035e3c-8088-3217-bb4b-7d1f91c967e1 | -13.2246 | -42.3657 | 2025-10-11 01:10:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 108.0 |
| c3f7088b-b4b8-39d0-8f73-97af3eca69ef | -17.2969 | -50.9765 | 2025-10-11 01:10:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 72.9 |
| a8f76705-e854-3bf1-9037-d1fbc2a5e2f2 | -7.8642 | -44.4922 | 2025-10-11 01:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 248.9 |
| e5f7ad87-f6f1-3fb3-92ca-316db7ef41d0 | -4.4241 | -43.4735 | 2025-10-11 01:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 61.1 |
| c85d521f-bc6c-3916-bc76-178e6ee8de03 | -12.6957 | -51.1641 | 2025-10-11 01:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 124.2 |
| 74f78b3e-b16b-3cb6-83af-b97b80c33940 | -13.2052 | -42.3693 | 2025-10-11 01:10:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 95.0 |
| 786ecc58-b83c-37a5-8a57-8417915e7f37 | -12.6766 | -51.1665 | 2025-10-11 01:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 155.8 |
| 57bee16a-c5a5-3dff-a058-0e0608a56453 | -5.8522 | -42.8372 | 2025-10-11 01:10:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 26.8 |
| e2e9d8b7-fb63-38e9-9859-af645c25b492 | -12.6762 | -51.1878 | 2025-10-11 01:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 2c381c63-cb84-35d6-bcb6-4805c3a39c3f | -5.852 | -42.8608 | 2025-10-11 01:10:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 34.9 |
| 4acd3849-7e21-3122-958f-b2131992b055 | -7.8454 | -44.4941 | 2025-10-11 01:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 181.6 |
| 7ebde8e5-44f2-36da-bb88-0c076652dc03 | -7.4616 | -46.8542 | 2025-10-11 01:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 1fc15b1f-5b55-32a6-a64a-b7132aa6730f | -8.1996 | -43.3189 | 2025-10-11 01:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 96.8 |
| 86a655c7-0798-343f-8ea5-41360f058c71 | -13.2062 | -42.3206 | 2025-10-11 01:10:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 168.9 |
| 3d17265a-bfbc-3985-8ec0-874464f5d959 | -5.8708 | -42.8593 | 2025-10-11 01:10:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 74.4 |
| 88c0eadf-f5f3-3ebd-8d94-ede7b7c42c7c | -13.00874 | -61.4313 | 2025-10-11 01:11:00 | TERRA_M-M | CORUMBIARA | RONDÔNIA | Brasil | 1100072 | 11 | 33 | nan | nan | nan | Amazônia | 8.7 |
| bd73207d-6e2d-3a22-b570-f20ec64426b0 | -13.2582 | -48.02131 | 2025-10-11 01:11:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 46.0 |
| a23dee87-a2de-38da-a195-4b06218ad4eb | -14.08124 | -51.56881 | 2025-10-11 01:11:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 11.4 |
| f83dcf53-6b20-34b7-92f9-41bcabd9e7a2 | -14.95469 | -59.43826 | 2025-10-11 01:11:00 | TERRA_M-M | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 979aa0a5-3dde-3933-b6c6-7615558c00ff | -12.69691 | -51.16924 | 2025-10-11 01:11:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 34.7 |
| 4d0b9311-f52d-30e9-b240-9b2624687da1 | -13.01873 | -61.43579 | 2025-10-11 01:11:00 | TERRA_M-M | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 25.0 |
| 55510c45-a777-3621-a536-2bfa5d5202d1 | -11.31325 | -51.46642 | 2025-10-11 01:11:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 15.3 |
| d42e348b-cff8-32e1-9dfb-ea0519c06baf | -12.68385 | -51.17157 | 2025-10-11 01:11:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 201.4 |
| d0edeecf-cfc3-3fd0-a431-47a05d2e7603 | -10.06091 | -67.54953 | 2025-10-11 01:11:00 | TERRA_M-M | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 24.0 |
| 9b89b00b-2b98-3300-8ee4-988d9f12a954 | -12.68737 | -51.19279 | 2025-10-11 01:11:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 431ec602-0ed7-30aa-badd-781f53854e0b | -14.95337 | -59.42828 | 2025-10-11 01:11:00 | TERRA_M-M | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| cd20b18a-1887-3789-bf5f-deb22a384e43 | -12.09422 | -64.23969 | 2025-10-11 01:11:00 | TERRA_M-M | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 15.7 |
| c560c585-73c1-3f5d-aa5a-3990c8130741 | -15.01751 | -56.08424 | 2025-10-11 01:11:00 | TERRA_M-M | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 44508691-7da3-3721-a6e0-a16b5398a372 | -9.45554 | -56.65568 | 2025-10-11 01:11:00 | TERRA_M-M | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 8482b684-413d-336a-8ce1-7ef88dfe4e61 | -9.24898 | -56.30482 | 2025-10-11 01:11:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| b5feba68-dd03-3d39-8682-053861f139c4 | -12.68031 | -51.1503 | 2025-10-11 01:11:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 39.8 |
| bfadf1d1-dd4e-3bae-bbb1-a16775a90457 | -15.01612 | -56.07461 | 2025-10-11 01:11:00 | TERRA_M-M | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 922dd74d-c456-3e61-8771-d266caacef8b | -12.60271 | -62.01011 | 2025-10-11 01:11:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 8.6 |
| e42a39d5-c66b-3c9d-9368-032f1228fecb | -14.94414 | -59.42953 | 2025-10-11 01:11:00 | TERRA_M-M | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 9c51a135-9973-3680-95b8-c5e7f56eadbf | -13.01887 | -61.42994 | 2025-10-11 01:11:00 | TERRA_M-M | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 52db8951-3850-3146-a513-62031b8a2f63 | -12.49655 | -55.74326 | 2025-10-11 01:11:00 | TERRA_M-M | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 10.4 |
| bb4d87c6-0e73-318b-9a33-00cb6e8dd50a | 1.92991 | -55.68976 | 2025-10-11 01:15:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| da20c013-b947-30f1-a7e1-3f304e019c72 | 1.9276 | -55.7063 | 2025-10-11 01:15:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 65a32e0f-7dca-3063-a700-70cecb088736 | 1.9158 | -55.70471 | 2025-10-11 01:15:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| a517724b-6f99-3669-8783-645db20a8d99 | -5.871 | -42.8357 | 2025-10-11 01:20:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 44.4 |
| c1fe75b9-953d-35bf-b92c-71cd1355f244 | -7.4616 | -46.8542 | 2025-10-11 01:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 911c8e2e-36ce-3e65-9029-1cb7e807acf9 | -12.6766 | -51.1665 | 2025-10-11 01:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 124.7 |
| 5508ce03-0d9c-3f65-8297-adda26435d4d | -12.6954 | -51.1855 | 2025-10-11 01:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 70.9 |
| a87e106b-0357-3083-b21d-4a00cb48b691 | -5.8708 | -42.8593 | 2025-10-11 01:20:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 27.4 |
| c63e003e-bea9-3b52-b4c0-a9f8b6c293c5 | -13.2252 | -42.3414 | 2025-10-11 01:20:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 701.9 |
| 6a07f35d-0ab7-3442-bab5-1389772cc51d | -13.2257 | -42.317 | 2025-10-11 01:20:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 207.7 |
| cc5895be-35a7-34f9-8947-9fbf40bb692c | -13.2246 | -42.3657 | 2025-10-11 01:20:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 75.0 |
| 4edea81b-ad02-336c-a2e2-658dbf666b89 | -13.2057 | -42.345 | 2025-10-11 01:20:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 461.7 |
| db6e1289-a1f7-3826-8acc-f7628b802a3d | -8.1996 | -43.3189 | 2025-10-11 01:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 101.7 |
| 1a8d676b-3e2a-3ce9-89e5-d93fc355225f | -7.8457 | -44.4711 | 2025-10-11 01:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 138.3 |
| ac10c1ca-a53f-3c24-8840-1936a74dcb16 | -7.8454 | -44.4941 | 2025-10-11 01:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 120.2 |
| 1500e6d6-7498-3e4c-afcd-1d9c7c363769 | -7.8645 | -44.4692 | 2025-10-11 01:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 163.3 |
| cf26c9c7-60b8-3eb1-b8d5-77c25076d8a8 | -4.4241 | -43.4735 | 2025-10-11 01:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 879a8dc2-14b6-3e03-b14d-4357e000ee9b | -7.8642 | -44.4922 | 2025-10-11 01:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 125.7 |
| 22340fdb-f913-3968-8bb1-54257822340f | -13.2062 | -42.3206 | 2025-10-11 01:20:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 142.3 |
| 5d7bdf8b-86a3-3aeb-953a-92e96921a717 | -12.6957 | -51.1641 | 2025-10-11 01:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 130.6 |
| 5128cd65-e8d5-3edc-a973-edac325b0c87 | -17.2722 | -46.8932 | 2025-10-11 01:20:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 4f9eb854-5de5-390e-b99f-9162c9ba2d65 | -12.6957 | -51.1641 | 2025-10-11 01:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 4390d22f-e6c3-3d69-a1bb-21ae6114e84e | -8.1996 | -43.3189 | 2025-10-11 01:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 98.7 |
| 2a2d18b6-4f97-354f-a918-5aa5181b4955 | -4.4241 | -43.4735 | 2025-10-11 01:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 57.2 |
| e6f5a577-d595-36aa-81ce-daa490f74148 | -13.2062 | -42.3206 | 2025-10-11 01:30:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 141.1 |
| 3067ba72-516d-3db0-8e65-93c94bf2d86d | -7.8645 | -44.4692 | 2025-10-11 01:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 101.1 |
| cfce74ed-79c0-3347-a060-d1e4cad6616e | -8.5024 | -46.1995 | 2025-10-11 01:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 104.3 |
| ed6dbb70-4b35-3a0f-bc1d-53fbc796636d | -7.4616 | -46.8542 | 2025-10-11 01:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 1fe4dc80-0be7-3ab3-891e-8b9ca23b51cc | -13.2257 | -42.317 | 2025-10-11 01:30:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 175.8 |
| 72e36275-bab8-3e3e-a8d5-d68a22fb0864 | -13.2252 | -42.3414 | 2025-10-11 01:30:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 511.1 |
| 7cf074c1-0ad5-3e50-a63d-020535abd397 | -8.5027 | -46.177 | 2025-10-11 01:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 48.6 |
| 970971e3-cf27-3de4-992b-ca5196499505 | -5.325 | -43.0884 | 2025-10-11 01:30:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 49.9 |


[Clique aqui para ver as próximas entradas](README4.md)

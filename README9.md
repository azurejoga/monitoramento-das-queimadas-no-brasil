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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 67089707-0330-35fb-9499-a6768dcfb2d9 | -15.63809 | -41.25206 | 2025-07-18 03:38:00 | NOAA-20 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| c023f7ac-1870-38a0-bfd4-2f7ddaeef796 | -13.54395 | -43.70895 | 2025-07-18 03:38:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d4bd5dd8-e9b3-3e8a-9a8c-32cd26c2a54a | -11.85343 | -46.7525 | 2025-07-18 03:38:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e2c68d36-6e05-3013-9d30-b60104f80459 | -11.45619 | -48.16471 | 2025-07-18 03:38:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cd5e08d8-5385-3af6-b1f2-386c7b4a9970 | -12.57031 | -44.75162 | 2025-07-18 03:38:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b30020be-93b2-3134-850e-82d53f6e147a | -20.03811 | -41.66388 | 2025-07-18 03:38:00 | NOAA-20 | CHALÉ | MINAS GERAIS | Brasil | 3116001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.5 |
| 05caa377-4993-31fd-9c27-8a81c6a0ca9b | -14.72179 | -45.07469 | 2025-07-18 03:38:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5cbe620a-d052-3d2f-bb6b-13e177069ace | -16.42933 | -42.63551 | 2025-07-18 03:38:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aeebd0ad-5e79-3651-b235-55b2d4406423 | -12.48542 | -46.92149 | 2025-07-18 03:38:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7d4baa73-369f-3021-8a48-728cf9bf33f8 | -11.56806 | -47.08972 | 2025-07-18 03:38:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 67e2e7fb-d4e0-39a7-8572-5a6abc3749b7 | -15.63843 | -41.25284 | 2025-07-18 03:38:00 | NOAA-20 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 58123276-b284-33dc-ae7a-2d9a72695f34 | -14.2045 | -45.34262 | 2025-07-18 03:38:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aa6330a7-40e3-3841-8eb1-407b1830f4d0 | -18.91612 | -40.60924 | 2025-07-18 03:38:00 | NOAA-20 | NOVA VENÉCIA | ESPÍRITO SANTO | Brasil | 3203908 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 8d7bcda5-b174-3de2-924c-80bab1d31ac4 | -11.57178 | -47.09291 | 2025-07-18 03:38:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 23187cdd-9a55-3734-be5b-283a35b74ec6 | -14.70427 | -46.19366 | 2025-07-18 03:38:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7cee8b26-cb86-39cb-a650-516a4c4c682e | -11.85447 | -46.75464 | 2025-07-18 03:38:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e45ca73a-5f96-3533-bd48-190a7913f115 | -11.56279 | -47.08328 | 2025-07-18 03:38:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 1338701e-30d7-3486-bf07-0cdc06a03c3f | -12.47693 | -44.50085 | 2025-07-18 03:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 84603153-fd1e-3bdb-b0f1-600d80b8fc8e | -14.73759 | -45.07831 | 2025-07-18 03:38:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 52dc86ce-49c4-3940-af28-7bca2f77c672 | -15.18485 | -43.53465 | 2025-07-18 03:38:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f1360fbe-0427-3b50-b40f-cb150abbdfc1 | -14.73232 | -45.07713 | 2025-07-18 03:38:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f5adc9b2-84e0-3600-9156-c8781af64a06 | -12.66515 | -47.0955 | 2025-07-18 03:38:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 684d474b-271d-313d-8c8d-c98d00a973b1 | -14.74696 | -46.30392 | 2025-07-18 03:38:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| be253ca7-7583-3155-a306-d3d13b8fd586 | -12.47461 | -46.91841 | 2025-07-18 03:38:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3d5c10ae-97e5-3f73-8958-c40b7da4444f | -14.72487 | -45.11422 | 2025-07-18 03:38:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cb80f6c4-c997-313c-899e-237992bb0186 | -15.64074 | -41.26044 | 2025-07-18 03:38:00 | NOAA-20 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 6a709070-cb4c-314f-a1cd-9d2ed0a89d32 | -11.73696 | -48.19366 | 2025-07-18 03:38:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 785c4550-6f71-34ee-b508-1ddc81a3c350 | -14.71569 | -45.10495 | 2025-07-18 03:38:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 619b97a0-9937-3135-a9a3-b1118ed8b1a6 | -11.57439 | -47.09105 | 2025-07-18 03:38:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 09ab5222-ba78-31ce-8324-fc377cf2a9db | -20.20446 | -41.31871 | 2025-07-18 03:38:00 | NOAA-20 | BREJETUBA | ESPÍRITO SANTO | Brasil | 3201159 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| aec121f0-0894-3458-b745-0fc7ea714061 | -16.1486 | -40.28112 | 2025-07-18 03:38:00 | NOAA-20 | JACINTO | MINAS GERAIS | Brasil | 3134707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 96f00713-a2b3-3d48-9808-b18c56c177a2 | -11.7357 | -48.19971 | 2025-07-18 03:38:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 29.9 |
| b9c5d339-3616-3251-bc73-89e59dd68087 | -12.66174 | -47.0915 | 2025-07-18 03:38:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 9bc665ca-4fb1-3a05-901c-5f4163f14aab | -15.63776 | -41.2566 | 2025-07-18 03:38:00 | NOAA-20 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| d9232824-dfeb-3b0b-91d1-4b3ae44f002b | -12.48078 | -46.91972 | 2025-07-18 03:38:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| faa5d64c-80e4-3c41-8129-f9309e609ccc | -11.85348 | -46.75962 | 2025-07-18 03:38:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 29944e47-0b59-3d0f-8518-241bd2dc3f56 | -11.56493 | -47.07296 | 2025-07-18 03:38:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 55319556-2244-3dce-b40f-33bcb6630b76 | -20.04218 | -41.66714 | 2025-07-18 03:38:00 | NOAA-20 | CHALÉ | MINAS GERAIS | Brasil | 3116001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 58551bd1-e418-3652-b13e-2f25608e63e3 | -12.66072 | -47.09658 | 2025-07-18 03:38:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 50918ac6-0b17-3160-85a3-334ece3a7ccf | -11.56016 | -47.0851 | 2025-07-18 03:38:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| d79f4360-6d4c-39a8-9a7a-950cd651d96e | -12.47926 | -46.92018 | 2025-07-18 03:38:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0217a0f0-02fa-3c0c-9505-427f78d41e45 | -11.56445 | -47.09661 | 2025-07-18 03:38:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| bfca26b6-cd0b-362d-9b46-28e66d7f53db | -11.45899 | -48.15905 | 2025-07-18 03:38:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fea2bd89-9ca8-35f2-9c6d-336f3b88811a | -11.73819 | -48.18774 | 2025-07-18 03:38:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 23.1 |
| f01a88f0-2bd4-3ee9-a340-b2ba82c46d03 | -14.71249 | -46.18257 | 2025-07-18 03:38:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8440eb54-bd7a-307a-ae16-a75f57a4a160 | -14.70596 | -46.18553 | 2025-07-18 03:38:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eac81f0f-0ad2-33ff-8c9d-7afcee1d27e8 | -15.15735 | -46.18573 | 2025-07-18 03:38:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fed08d9e-c6af-352e-89bd-c58e72d46eb3 | -12.71119 | -46.81265 | 2025-07-18 03:38:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ac1089e1-56bf-3757-99cf-a68a6a4118c6 | -16.71292 | -43.86616 | 2025-07-18 03:38:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 22281455-4c25-34f9-81cb-b74bb896bb18 | -14.20521 | -45.33902 | 2025-07-18 03:38:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 60042a32-7cc7-3fe9-815f-900b4755c158 | -16.06765 | -43.64532 | 2025-07-18 03:38:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 895d25e1-fbc3-3fe1-be62-2adb67b9d5bb | -13.30277 | -44.18209 | 2025-07-18 03:38:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0adec3b3-b13d-3dfb-89d0-399a70eb4a68 | -15.6374 | -41.25581 | 2025-07-18 03:38:00 | NOAA-20 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 3ba67ab0-bd6e-35b9-9b76-14d6709d0465 | -11.99533 | -45.30803 | 2025-07-18 03:38:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c0f41666-c1f6-3fc4-bd35-2fb0affd94e5 | -14.20614 | -45.33872 | 2025-07-18 03:38:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1ff45b8e-6bb3-3615-914a-61d0bcb6f5f0 | -16.70569 | -49.35621 | 2025-07-18 03:38:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0d160a80-61de-36da-a684-5abc217d4d0e | -11.85238 | -46.75757 | 2025-07-18 03:38:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7f3636ed-1e9b-31c2-ade7-4155865c6ce5 | -12.57099 | -44.7481 | 2025-07-18 03:38:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| efb6fb4c-6fae-3cca-9dac-c1445c776e83 | -12.47628 | -44.50423 | 2025-07-18 03:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5d2d5ee2-de8a-3eed-b7b7-f4c0e3168f9f | -14.7068 | -46.1815 | 2025-07-18 03:38:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e2f66b01-14cb-31fa-adcf-d3519958f401 | -12.99788 | -44.86665 | 2025-07-18 03:38:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a7701d84-e269-3a78-8c96-b0335c7532ec | -18.56437 | -46.49376 | 2025-07-18 03:38:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cb993793-1bd4-319a-9fe5-5bb426b2b079 | -11.56067 | -47.0935 | 2025-07-18 03:38:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| c26d35f6-c13d-3b10-bd7c-c8a6679a2799 | -12.70595 | -46.80816 | 2025-07-18 03:38:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c131aed1-e95e-3950-88f3-476f7f4f3342 | -12.99571 | -44.85863 | 2025-07-18 03:38:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1ac2e1df-e431-3f2c-8a39-5fc22160e790 | -18.40671 | -44.18919 | 2025-07-18 03:38:00 | NOAA-20 | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2ffa90b0-8cf8-39eb-b22e-33c101356b83 | -13.54352 | -43.70693 | 2025-07-18 03:38:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| eba86902-ba1a-301c-b81f-9d72d71b0040 | -19.45288 | -45.30679 | 2025-07-18 03:38:00 | NOAA-20 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 499ac4a8-848e-3275-b69e-6f3604d4a188 | -14.71166 | -46.18658 | 2025-07-18 03:38:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 944448b8-2354-36f8-906a-6b5496f54c23 | -14.72246 | -45.07137 | 2025-07-18 03:38:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a0d72ec4-75c4-3630-a5ef-9f3c282acd37 | -13.00106 | -44.85985 | 2025-07-18 03:38:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d6d8fe13-b8aa-33e9-92ba-de75930b5f34 | -16.06668 | -43.65048 | 2025-07-18 03:38:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b6192aec-c66f-3188-b2cb-66a880c62baa | -14.19999 | -45.34114 | 2025-07-18 03:38:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5295784d-9705-3ea1-8870-5173646a7104 | -20.04196 | -41.6648 | 2025-07-18 03:38:00 | NOAA-20 | CHALÉ | MINAS GERAIS | Brasil | 3116001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.5 |
| c4808fa5-331c-3859-9abe-ecd918fa1227 | -12.48694 | -46.92106 | 2025-07-18 03:38:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1e2dc7d1-fb3d-37ce-9882-3b325d20fd3b | -14.72554 | -45.11091 | 2025-07-18 03:38:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 32682fd7-d7f2-3b30-8bb5-f94ded101707 | -19.34396 | -40.86903 | 2025-07-18 03:38:00 | NOAA-20 | BAIXO GUANDU | ESPÍRITO SANTO | Brasil | 3200805 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| b34256a2-eb77-3b61-9bc0-b1e369d52ac9 | -11.4577 | -48.16517 | 2025-07-18 03:38:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c6509c61-1fef-3d2f-8206-c9843af2e0bc | -14.20591 | -45.33546 | 2025-07-18 03:38:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 70d9b335-0662-303e-be3f-2dae06047a50 | -12.9997 | -44.86668 | 2025-07-18 03:38:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 51c48591-9d18-30dd-9de2-13b52d7cc7db | -14.71332 | -46.17857 | 2025-07-18 03:38:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4ad7a80c-72bb-30b2-9b40-8558e2bcbe25 | -13.00038 | -44.86327 | 2025-07-18 03:38:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 94f092e5-a41c-3d18-a1b3-036a46c41a3b | -12.99854 | -44.86326 | 2025-07-18 03:38:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ed919ca6-5b1e-3d58-8d21-812ddbf61461 | -12.06899 | -47.98155 | 2025-07-18 03:38:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 93e33e28-b5bb-3bfe-83d3-5367af1f86eb | -11.56751 | -47.08131 | 2025-07-18 03:38:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| cb011506-8020-3d60-ae13-f7077e174ee0 | -15.41122 | -41.99704 | 2025-07-18 03:38:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 9d7bd1ff-3c6e-32dc-ab38-3afe5b9bdbf2 | -14.72094 | -45.1063 | 2025-07-18 03:38:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d3badf95-a7ab-3186-b4e4-0cda26466fdd | -14.71895 | -45.11617 | 2025-07-18 03:38:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3552cc4b-391d-3c95-8054-6bb9dc350b2c | -11.56854 | -47.07618 | 2025-07-18 03:38:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 5e81d27d-7fbd-3d40-9bee-0f3521756efa | -14.71786 | -45.0669 | 2025-07-18 03:38:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3e569c90-8fbd-3603-ac88-092a095232fd | -11.56119 | -47.07992 | 2025-07-18 03:38:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 08fe3ec6-35c6-30fd-8135-da5a76d4a00b | -5.6569 | -43.6929 | 2025-07-18 03:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 543b30c4-907f-3b69-b13d-c3e31c3ec529 | -3.3958 | -47.4785 | 2025-07-18 03:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 108.0 |
| ed7a0b8f-cd86-35a8-8c6a-e12b3723de19 | -8.0886 | -43.1431 | 2025-07-18 03:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 78.1 |
| 5187ef2a-b7b8-350a-8063-8d19fb352cd6 | -11.7317 | -48.1849 | 2025-07-18 03:40:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 518b46d8-6f0f-3786-8410-64f011af7880 | -5.6567 | -43.7161 | 2025-07-18 03:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 211.0 |
| 99e75f22-4935-372b-a506-462818050a2c | -5.6379 | -43.7175 | 2025-07-18 03:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 4c8597ba-6289-3a65-bc2d-32af59da885d | -11.7508 | -48.1825 | 2025-07-18 03:40:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 52.0 |
| 4693068f-0f3a-3fe6-9ef5-24fe38352a65 | -3.3957 | -47.5003 | 2025-07-18 03:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 1b27946e-ecf2-3eda-8702-72e93d257a36 | -25.42011 | -49.10059 | 2025-07-18 03:40:00 | NOAA-20 | PIRAQUARA | PARANÁ | Brasil | 4119509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |


[Clique aqui para ver as próximas entradas](README10.md)

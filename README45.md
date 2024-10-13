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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0c466250-976f-3484-8c5d-a052045e1919 | -10.1792 | -42.46548 | 2024-10-13 03:49:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 76b97384-034f-31ea-86af-3ee6bd6811fd | -14.7079 | -42.30482 | 2024-10-13 03:49:00 | NOAA-20 | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 32365dac-d2b9-3709-a7a3-f39210c14b53 | -16.34802 | -43.69559 | 2024-10-13 03:49:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 74c4db92-bdf9-3948-bda0-ccd923d94773 | -16.34694 | -43.69828 | 2024-10-13 03:49:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5c57d491-6224-3fd5-8b28-76c6bb174a46 | -17.09492 | -43.80687 | 2024-10-13 03:49:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cc9ad764-2e68-39b1-aa21-d8a06955c050 | -17.09416 | -43.80573 | 2024-10-13 03:49:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c388ee5c-9982-3f92-9d3b-555871c699e6 | -16.91595 | -43.6801 | 2024-10-13 03:49:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e1873892-e874-37d1-99e3-2add5e14a10b | -16.6804 | -43.88667 | 2024-10-13 03:49:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9019797f-b164-30ce-a41a-1f06fc1c3f3b | -7.93514 | -43.18089 | 2024-10-13 03:49:00 | NOAA-20 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 8dc9a959-9169-3052-bf80-96163e367c2e | -9.26637 | -43.53804 | 2024-10-13 03:49:00 | NOAA-20 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| c90d48ef-8fa2-3e68-a6fc-e3aca7c69c2e | -8.13628 | -43.01655 | 2024-10-13 03:49:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 52b0a840-fc74-3c91-ad8e-1394b8a0504a | -8.13558 | -43.02058 | 2024-10-13 03:49:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 246a3c00-225e-3a33-b0dd-04e568898cf9 | -8.13275 | -43.0117 | 2024-10-13 03:49:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 1cacd419-4051-39af-a8eb-760f50317495 | -8.13204 | -43.01574 | 2024-10-13 03:49:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0c33b22e-90ed-3cd8-a2c3-3768c260babb | -8.13133 | -43.01986 | 2024-10-13 03:49:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| feacb08f-b62f-32d0-81d6-d0a54a9dc53d | -8.12919 | -43.00697 | 2024-10-13 03:49:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ab9a6709-667c-33ca-94cb-b164521f815f | -8.12493 | -43.00631 | 2024-10-13 03:49:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b8e0ee97-c7da-3bb5-a1ee-6f16b2748fa6 | -8.12353 | -43.01437 | 2024-10-13 03:49:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f1721c13-15d9-337b-a70c-4cc143a8ad96 | -8.12067 | -43.00565 | 2024-10-13 03:49:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 16af473e-e4ac-38c7-bbb1-e5d8ddd08b08 | -8.11997 | -43.0097 | 2024-10-13 03:49:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| bfb6028e-6a0f-3e61-8bef-226e9c2dc5fd | -9.44337 | -44.14867 | 2024-10-13 03:49:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 44f3e05e-deae-3eb1-a532-69efb70c0c85 | -10.05908 | -44.17823 | 2024-10-13 03:49:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b36168a9-becf-32de-87c5-5f401ab516b7 | -9.44417 | -44.1442 | 2024-10-13 03:49:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 6a3aa08a-939e-3555-8882-29b01b21a6d0 | -10.06354 | -44.17899 | 2024-10-13 03:49:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8e94dbd1-df7b-3d0c-acd0-be2e92606279 | -14.2291 | -44.6119 | 2024-10-13 03:49:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| facea15e-21ff-3eeb-9538-2b118c5d7de0 | -14.18843 | -44.31419 | 2024-10-13 03:49:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a10eeb48-1a35-333c-8e95-e0387a547a64 | -17.96402 | -44.93235 | 2024-10-13 03:49:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5142bdea-c944-3625-a3f8-8481085d7744 | -20.945 | -46.00263 | 2024-10-13 03:49:00 | NOAA-20 | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1bf43f22-f78e-3883-a151-1727779f15a0 | -20.94422 | -46.0066 | 2024-10-13 03:49:00 | NOAA-20 | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| aa1ea68c-c4b5-3713-8154-6b81cb68b1f0 | -20.95331 | -46.00409 | 2024-10-13 03:49:00 | NOAA-20 | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3ae10b23-5dde-3727-8aa6-91c02fb4819c | -20.94915 | -46.00339 | 2024-10-13 03:49:00 | NOAA-20 | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b11d6f05-3dd6-399a-a03e-a9f078b67de7 | -20.94838 | -46.00734 | 2024-10-13 03:49:00 | NOAA-20 | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0cab097d-34e6-33a3-9a46-03217730433b | -20.94727 | -46.00365 | 2024-10-13 03:49:00 | NOAA-20 | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 39c63775-0706-3726-bca4-77bed86a3d48 | -20.94652 | -46.00762 | 2024-10-13 03:49:00 | NOAA-20 | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 34796f55-2d54-3f95-8155-143a775f550c | -7.89968 | -44.62109 | 2024-10-13 03:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 32df8f2e-2c26-3c5b-b432-0c52296cdc78 | -7.89581 | -44.61513 | 2024-10-13 03:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 66b6a2b9-6991-33da-af08-9825c395bd27 | -7.89493 | -44.62021 | 2024-10-13 03:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a7df1468-a8da-3bac-a292-fa67647df43c | -7.96883 | -44.51113 | 2024-10-13 03:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e742f344-2d03-309a-8764-2a6eb94b6fc2 | -7.96795 | -44.51606 | 2024-10-13 03:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| abaa5825-bdda-30ca-aaa2-63f3c2bc8dfc | -7.89403 | -44.62534 | 2024-10-13 03:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f5907fad-3abb-3668-b7b1-9c97a9aa8517 | -7.89017 | -44.61937 | 2024-10-13 03:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9e73f4d1-271a-3ae1-a323-44b67c8ecef2 | -8.05554 | -44.82649 | 2024-10-13 03:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9236bc8b-0f73-30a2-a8c0-e797ac275c85 | -8.07159 | -44.81986 | 2024-10-13 03:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 877abb2b-8820-327d-84d3-d0b4ef46b64b | -8.06681 | -44.81886 | 2024-10-13 03:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0f27ad45-2352-36a9-b51b-77bd9a2870cd | -8.06287 | -44.81308 | 2024-10-13 03:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 87d7c6c9-8a89-3ca7-949e-2b0ee58603f5 | -8.69268 | -45.26681 | 2024-10-13 03:49:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9d9b313c-4f0c-361e-8ddf-d609a7b8cf5c | -8.0612 | -44.82256 | 2024-10-13 03:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9792d1b5-9422-3820-8061-aa5d29a12cdc | -9.82346 | -45.04864 | 2024-10-13 03:49:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eea32ae6-668f-3ef3-8962-3617754afa9a | -9.55881 | -44.47943 | 2024-10-13 03:49:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 20d4029d-ae37-3b97-843a-1288b080ab11 | -9.43863 | -45.5129 | 2024-10-13 03:49:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 3b244da0-c6fe-39c1-8545-67af94a12585 | -9.57539 | -44.38474 | 2024-10-13 03:49:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0534b982-1d6a-3849-87e1-9b7b2499840b | -9.57456 | -44.38951 | 2024-10-13 03:49:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 10.0 |
| c1ced33a-0be3-3f9b-b710-b3bc6707d27b | -9.44349 | -45.51415 | 2024-10-13 03:49:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 269abc10-bc46-3aa1-a731-fa72055cd779 | -9.44458 | -45.50813 | 2024-10-13 03:49:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 254a0031-d8cc-31fa-875f-f3f69eb5b753 | -9.43972 | -45.50692 | 2024-10-13 03:49:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b02d698e-5124-311a-8c26-2061a9327cee | -9.43483 | -45.50584 | 2024-10-13 03:49:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7b2cd671-93a2-3b97-a5b5-50fdd93f9810 | -9.56501 | -44.47101 | 2024-10-13 03:49:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b9b9c52f-ab41-391d-a475-6f1405f279f5 | -9.5642 | -44.4756 | 2024-10-13 03:49:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| bbdc01aa-cef9-33ab-a46e-6c84f241a315 | -7.53794 | -46.86874 | 2024-10-13 03:49:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d25581f5-6619-3256-8ce3-76406defa9d9 | -7.53728 | -46.87248 | 2024-10-13 03:49:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e215c6c5-7e2f-3a1f-8ffb-5ec2befdcdf5 | -7.53669 | -46.86883 | 2024-10-13 03:49:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e5b9377a-b803-37ce-82d1-d5b0006a49d5 | -7.53601 | -46.87255 | 2024-10-13 03:49:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ec3098bf-4c68-3d9b-9163-da7a23314d2c | -7.51894 | -46.59254 | 2024-10-13 03:49:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 08608f43-c2d3-358e-a0ee-31a9b23c1224 | -7.4109 | -45.69383 | 2024-10-13 03:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f14a7cd6-7053-370e-bc17-b4ea4ae5b960 | -7.41003 | -45.68997 | 2024-10-13 03:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f32083a9-4eba-310b-823c-28948fc5fd9b | -7.41144 | -45.69085 | 2024-10-13 03:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f29a819e-0ebd-31ee-a59c-d04cb2e37689 | -7.40951 | -45.69297 | 2024-10-13 03:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d85f8ed7-59cc-344c-b5db-5e707c4c3dca | -9.28152 | -46.58063 | 2024-10-13 03:49:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 20392ee9-2204-3c94-ac78-cd636c0dc445 | -9.22469 | -46.68074 | 2024-10-13 03:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 5612c3d6-abc8-3e36-bb99-756f84ac96c9 | -9.22405 | -46.68418 | 2024-10-13 03:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 431d6ac4-6b73-37bc-8076-caa6a52ebb8b | -9.22342 | -46.68761 | 2024-10-13 03:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| dee245ea-ab45-3470-a564-a91f2b81fec9 | -8.70245 | -46.61374 | 2024-10-13 03:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 16a01604-970c-3122-8c51-4dd7ef5a9c8f | -8.69766 | -46.60966 | 2024-10-13 03:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 97b90ef7-6d09-386a-8715-1692ceeb4598 | -8.69705 | -46.61295 | 2024-10-13 03:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b1ce2fcd-98b6-3a15-8a6d-fb15f484b560 | -8.69646 | -46.61621 | 2024-10-13 03:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 0695deaf-c67e-3c4b-97f3-9908ce2cbe35 | -8.69106 | -46.61543 | 2024-10-13 03:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a491350b-cb21-3c8b-a609-3f12ea9ac8ed | -8.52697 | -45.56477 | 2024-10-13 03:49:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9241f714-9e17-351d-8ccb-013baa957bce | -8.52721 | -45.56713 | 2024-10-13 03:49:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 22026399-2e69-36a2-8be7-e13e052655f5 | -19.09315 | -48.30827 | 2024-10-13 03:49:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7e169702-2dd1-3c98-8eac-a86968e85144 | -7.67607 | -47.31323 | 2024-10-13 03:49:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| ef6203d2-003b-3031-9659-e49f7af2ce49 | -7.67533 | -47.31723 | 2024-10-13 03:49:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 8618542f-55ea-32f1-af1c-9253899714c4 | -7.67459 | -47.32123 | 2024-10-13 03:49:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| c1e77f92-164f-32e6-9b24-f02b0667846b | -7.67447 | -47.31311 | 2024-10-13 03:49:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 17.4 |
| dfc4cf3b-2b4c-30f2-b33e-4af07050c734 | -7.67376 | -47.31711 | 2024-10-13 03:49:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 6cee4612-65b4-336c-8b2f-b47dcc749354 | -7.67305 | -47.3211 | 2024-10-13 03:49:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 20.1 |
| ce124ba6-6188-3ba6-ae79-b19f787110c7 | -7.67234 | -47.32513 | 2024-10-13 03:49:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 716ab633-627c-3b86-9cc4-606410ff3674 | -7.67035 | -47.31227 | 2024-10-13 03:49:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| a13f0ae0-3b70-3a12-aec2-751029b320d5 | -7.66961 | -47.31623 | 2024-10-13 03:49:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 15.5 |
| ef73c3f9-e240-3547-b8e6-f2300922bbb4 | -7.66887 | -47.32019 | 2024-10-13 03:49:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 15.5 |
| ec7244be-0f85-30b7-92eb-156b6874f957 | -7.66813 | -47.3242 | 2024-10-13 03:49:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| de3e75e3-5c82-3650-82e0-06ae1447ff49 | -7.66805 | -47.31609 | 2024-10-13 03:49:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 3473210f-0a57-3a62-84e2-74c1d66167ba | -7.66734 | -47.32007 | 2024-10-13 03:49:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 2f461947-bd19-3df4-b531-cc9d31fc6a6a | -7.66662 | -47.32409 | 2024-10-13 03:49:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| eca0ff66-7b6e-3005-9df2-894e056edd73 | -7.66315 | -47.31921 | 2024-10-13 03:49:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 6ef30159-472b-329d-94d7-1d79d1f1f335 | -7.66241 | -47.3232 | 2024-10-13 03:49:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 5ff8b372-0a38-33cc-a593-2b17c6a208c9 | -7.66162 | -47.31905 | 2024-10-13 03:49:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| f902e7bf-f299-32ef-971f-bac6351f9d0e | -7.6609 | -47.32305 | 2024-10-13 03:49:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 5692d7b5-6708-39a3-9fff-1750bffc2f4d | -7.60379 | -47.74347 | 2024-10-13 03:49:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 66ea14d8-786b-3600-a6eb-ac33e2b6a732 | -7.60302 | -47.74776 | 2024-10-13 03:49:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| edcfd67f-74fe-342e-b12d-da61aeea5bef | -7.60237 | -47.74243 | 2024-10-13 03:49:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README46.md)

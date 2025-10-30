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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9c5142cf-6632-3e3e-a3c1-b6c1c4191996 | -11.1373 | -51.0859 | 2025-10-30 03:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 12b3a6f0-40e5-3411-8c9a-fd08ddf19448 | -12.4947 | -50.5898 | 2025-10-30 03:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 86.5 |
| ec45d2ad-29bf-3ffb-a31a-654fce6905f2 | -3.7867 | -43.9011 | 2025-10-30 03:00:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 56.6 |
| ab74bfcc-8067-3006-a35c-481d288de093 | -8.3311 | -47.9438 | 2025-10-30 03:00:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 0333d9d4-f61b-3eaa-9003-1104c4c837af | -7.804 | -46.4234 | 2025-10-30 03:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 74.0 |
| c6fb9210-950d-3834-a119-2d5309a55509 | -15.0249 | -46.3082 | 2025-10-30 03:00:00 | GOES-19 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 64.5 |
| a2760a8d-e116-3284-8b65-c3631c340347 | -12.4947 | -50.5898 | 2025-10-30 03:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 81.6 |
| e1314009-0354-3fa7-b22f-d4f38b1be952 | -4.2544 | -43.7149 | 2025-10-30 03:10:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 6105d0a8-8121-3a5a-9ef3-a6cff0c70e18 | -8.3313 | -47.9219 | 2025-10-30 03:10:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 112.4 |
| 0fc318fe-9ffb-3874-8009-784e285afb4c | -12.495 | -50.5684 | 2025-10-30 03:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 115.9 |
| 86fa829e-8236-36a2-bd36-c2e740ee4110 | -3.8054 | -43.9002 | 2025-10-30 03:10:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 41.6 |
| 6adc48d9-3dfa-337b-ab2a-04a0756db90d | -3.7867 | -43.9011 | 2025-10-30 03:10:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 53.9 |
| 4557651d-7d82-3b27-bdc1-695ed0bf65ef | -12.5141 | -50.566 | 2025-10-30 03:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 87.7 |
| d7551159-6dce-3a42-9042-c486693a6924 | -8.3311 | -47.9438 | 2025-10-30 03:20:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 62.4 |
| bb900323-2771-3740-8b91-ed47c31504dd | -15.0249 | -46.3082 | 2025-10-30 03:20:00 | GOES-19 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 3d453e08-bc3a-3d62-b254-5ba2304fb049 | -3.7867 | -43.9011 | 2025-10-30 03:20:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 46.9 |
| 964be5ac-6acd-36ff-b4aa-f0e202e4103e | -3.8054 | -43.9002 | 2025-10-30 03:20:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 42.3 |
| 0c7648e6-b2e4-3e7d-8772-1542f8fe1ea0 | -4.2544 | -43.7149 | 2025-10-30 03:20:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 9d256ecc-aec0-30dd-bc82-a881c7fcc950 | -12.5141 | -50.566 | 2025-10-30 03:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 0aabd4dc-9c9e-3900-bcce-ebaccdd38bed | -12.3088 | -50.2688 | 2025-10-30 03:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 5b933ff2-ba57-3c54-b6f5-f924ea05fc34 | -12.4755 | -50.5922 | 2025-10-30 03:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 87.7 |
| b0a014e4-1f06-3114-8c6b-88f66450bbac | -12.4947 | -50.5898 | 2025-10-30 03:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 91ddaa49-7d4d-3875-838c-85fed40dc56f | -8.3313 | -47.9219 | 2025-10-30 03:20:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 109.2 |
| 8c653e50-eda3-3a68-a3bb-ab5b468626a3 | -12.495 | -50.5684 | 2025-10-30 03:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 134.3 |
| 4c194c39-c5b6-3a0a-87bd-1dd15a83b8b5 | -12.3088 | -50.2688 | 2025-10-30 03:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 91.8 |
| e4791c4a-3d18-398f-828b-25b225cabd99 | -4.2544 | -43.7149 | 2025-10-30 03:30:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 135.8 |
| cc303c37-fd28-32a7-8305-abfc9648e024 | -4.2832 | -59.6554 | 2025-10-30 03:30:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 91127bf8-022f-3b67-b253-09ec925fe88c | -12.4947 | -50.5898 | 2025-10-30 03:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 639b3d69-f2e3-3010-be6a-8a73627e58dd | -12.495 | -50.5684 | 2025-10-30 03:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 141.9 |
| dea57db9-9e35-3c2c-a996-2fef1852c993 | -4.2731 | -43.7139 | 2025-10-30 03:30:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 53.9 |
| 55b03136-ebe3-3d75-ad73-907479923471 | -12.5141 | -50.566 | 2025-10-30 03:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 101.8 |
| 819199ee-b0e4-3be4-9a3d-7a067a162466 | -8.3313 | -47.9219 | 2025-10-30 03:30:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 112.0 |
| 9d24bfb6-46ef-368a-a031-8580926c3caa | -5.4372 | -45.3323 | 2025-10-30 03:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 7a9d4c4f-0d64-391c-9ee7-1f37373ed120 | -12.4759 | -50.5707 | 2025-10-30 03:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 113.5 |
| 88db3678-4f24-36c2-8d8f-8e615d641609 | -8.3311 | -47.9438 | 2025-10-30 03:30:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 2b350968-464a-363a-8183-4359a4e6ed3c | -12.4755 | -50.5922 | 2025-10-30 03:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 102.8 |
| c89cd321-a4aa-35f7-a8b0-518225c98b3a | -4.2649 | -59.6558 | 2025-10-30 03:30:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 58.1 |
| cb1b3dcd-144d-3e88-a7b7-0a2bcbe81e5e | -4.2545 | -43.6918 | 2025-10-30 03:30:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 49.1 |
| a0cdb76e-ab5d-32b9-b791-01c30b611a22 | -5.04055 | -43.61402 | 2025-10-30 03:34:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 29f7c657-15bf-3503-bbb4-f1a11ec11ea4 | -5.51924 | -41.24387 | 2025-10-30 03:34:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 49da2739-69f7-3d18-a879-24f1fa8c36a0 | -4.98475 | -45.51889 | 2025-10-30 03:34:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 59f9d563-1eb4-318b-bcfc-7ed6fbc8e84c | -3.80242 | -43.90005 | 2025-10-30 03:34:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 8bc7c9f5-c2a6-384b-82e2-3a766164d0af | -3.79044 | -43.89772 | 2025-10-30 03:34:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| db5d8925-76d6-35a0-a67e-ef3ba4a3a522 | -4.63872 | -42.52671 | 2025-10-30 03:34:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 00675a4a-304a-3c52-a4d1-5da4afd1bb72 | -5.02513 | -44.81007 | 2025-10-30 03:34:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 77449ce6-c6c3-3bbd-8d60-aa99034b1993 | -5.57793 | -42.17369 | 2025-10-30 03:34:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| dfcde7e7-3dd6-3489-ae6e-9281f32e4d07 | -5.06503 | -40.47427 | 2025-10-30 03:34:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 12.6 |
| 24af6d9f-b3a9-3558-99b1-12bd18bae19b | -5.59585 | -42.7772 | 2025-10-30 03:34:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 0e24e4b2-52bc-395e-9765-98ec9f917158 | -4.84066 | -45.35238 | 2025-10-30 03:34:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 13057b1f-1d38-3c81-ae51-99e3d9f41ccf | -5.88681 | -35.25664 | 2025-10-30 03:34:00 | NOAA-21 | PARNAMIRIM | RIO GRANDE DO NORTE | Brasil | 2403251 | 24 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 715f5087-4355-3b8e-9c97-87f09048f3f9 | -5.65813 | -41.83737 | 2025-10-30 03:34:00 | NOAA-21 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 1537393f-1433-3bba-91f0-a8fa76fe48f6 | -3.96447 | -40.61292 | 2025-10-30 03:34:00 | NOAA-21 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| cbf71c0f-0b55-3110-bd7e-a0f2cf91200f | -5.79505 | -40.82136 | 2025-10-30 03:34:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 019c3ec6-03e4-36c7-9919-e3395040135a | -5.53723 | -41.70792 | 2025-10-30 03:34:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| b4c233a5-436e-3245-8537-efa0774aed1a | -5.57257 | -42.17049 | 2025-10-30 03:34:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 70f1fcba-6419-3ef1-bc2d-1e5d007e7b1f | -5.52224 | -41.24276 | 2025-10-30 03:34:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 60b12d0e-49e4-3dbc-a8ca-9fa66bc8fac1 | -4.84422 | -45.85376 | 2025-10-30 03:34:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f1e2de31-a6a2-3c1d-92cd-67598872fcf0 | -4.25789 | -43.71604 | 2025-10-30 03:34:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 24.4 |
| 15a60ec8-efe5-3502-a7b6-1afc837c492d | -5.64451 | -41.08976 | 2025-10-30 03:34:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 4551bc15-fe53-3ae8-b607-4ada4c29d73f | -5.80923 | -40.82409 | 2025-10-30 03:34:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 782a6f1c-f41e-3b92-9b1b-5a9d14eb0d02 | -5.03474 | -43.61311 | 2025-10-30 03:34:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 5ed0eff1-882e-3d9f-9a9a-d76071f454a3 | -5.79422 | -40.82615 | 2025-10-30 03:34:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 024a156b-f8a8-3789-b6a3-0dcb4a73d1c3 | -4.46626 | -43.44375 | 2025-10-30 03:34:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3a7aa149-5376-3eae-b0d8-d960d8a95dfb | -4.46879 | -45.75375 | 2025-10-30 03:34:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 516c8e41-a1c9-3396-a357-6ebd07d9c378 | -4.48503 | -43.43835 | 2025-10-30 03:34:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7892b017-8835-3933-8ac5-138418c9d2cb | -3.93381 | -44.19712 | 2025-10-30 03:34:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 23d5b092-7072-3491-94c6-8f1deff1e66a | -4.25863 | -43.71179 | 2025-10-30 03:34:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 592b53bb-3816-308c-81b8-8c92191676b1 | -5.8058 | -40.8438 | 2025-10-30 03:34:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| febf08a0-3524-3c2b-b2d9-622bf55a2b51 | -5.57848 | -42.1706 | 2025-10-30 03:34:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 41898ae2-df0b-3df6-84dc-0ad0da3b9547 | -3.78965 | -43.90229 | 2025-10-30 03:34:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 7b800e35-baf8-305f-800f-c39df41a79f5 | -5.79463 | -40.818 | 2025-10-30 03:34:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 0b1695a1-7b98-3b1e-b61a-8b1ee0d9ce0c | -4.4908 | -43.43937 | 2025-10-30 03:34:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 33b8f63f-aee9-362f-a3f2-f6a7ffc8f9e5 | -3.95965 | -40.6121 | 2025-10-30 03:34:00 | NOAA-21 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ab215658-517d-3155-8dbf-d0205dc0af49 | -5.46082 | -40.87142 | 2025-10-30 03:34:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 219c3ca7-098a-3906-b7f3-1c8e1267580d | -5.49191 | -42.0781 | 2025-10-30 03:34:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 098c9594-a269-3aaf-8176-2634e874aa96 | -3.13288 | -40.05216 | 2025-10-30 03:34:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 42971816-9266-3543-8303-a1d443a3d170 | -5.30142 | -44.31833 | 2025-10-30 03:34:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d8c1cd31-4e02-3388-91fa-1174420635b5 | -5.56871 | -37.96521 | 2025-10-30 03:34:00 | NOAA-21 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| e6c8ae5e-52ae-3b99-84a2-7e5f6f8aeffa | -5.49742 | -35.34106 | 2025-10-30 03:34:00 | NOAA-21 | CEARÁ-MIRIM | RIO GRANDE DO NORTE | Brasil | 2402600 | 24 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 73ca1786-f778-3146-8fe3-961c50fc5fe2 | -4.47207 | -43.44756 | 2025-10-30 03:34:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 6b29cfb1-cd91-3928-a0f4-79fd8b3bf7d5 | -4.47134 | -43.44886 | 2025-10-30 03:34:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| d8bfd060-bd61-3f82-b0d3-ce2add425c18 | -5.78986 | -40.81731 | 2025-10-30 03:34:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| b6801731-59e9-34f0-8893-35c05dcd7157 | -5.30213 | -35.97609 | 2025-10-30 03:34:00 | NOAA-21 | PARAZINHO | RIO GRANDE DO NORTE | Brasil | 2408805 | 24 | 33 | nan | nan | nan | Caatinga | 2.5 |
| e89ea18c-e20a-3d5c-8d08-66ed1482577b | -4.83058 | -42.7365 | 2025-10-30 03:34:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f3b19768-ed59-3081-adf8-21db261baa78 | -5.80097 | -40.80922 | 2025-10-30 03:34:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 98a314d6-c09b-3242-8d82-f5f987c750ea | -4.99123 | -45.52027 | 2025-10-30 03:34:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d4e2460a-309b-3195-95ac-f88d3cbf9334 | -4.15154 | -43.88641 | 2025-10-30 03:34:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 71ea638f-765d-3a11-90f8-61d832df66af | -5.22768 | -46.13644 | 2025-10-30 03:34:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 50bc5d01-cbff-33db-84be-a50c1d55100a | -4.84732 | -45.42778 | 2025-10-30 03:34:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 173c9878-4369-31ee-8005-a91a706394c6 | -5.02423 | -44.81509 | 2025-10-30 03:34:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 37f2c785-a8bb-3318-8707-21f45c46da42 | -5.57779 | -42.17144 | 2025-10-30 03:34:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| f31d08dc-af1c-3463-96ec-0dd4b51f13dc | -5.51732 | -41.24202 | 2025-10-30 03:34:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| f554eb2d-3a2a-3898-b127-b2f6b7e5f416 | -2.76472 | -45.39252 | 2025-10-30 03:34:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 54f4eea9-ea71-3e87-834a-0e531ecdabe1 | -5.43527 | -45.09742 | 2025-10-30 03:34:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 836bfd76-ceae-39a6-b66b-c78061802d31 | -5.91823 | -41.91844 | 2025-10-30 03:34:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 55b2795c-e2c6-354a-83b6-2ba08eab2046 | -5.2986 | -35.97553 | 2025-10-30 03:34:00 | NOAA-21 | PARAZINHO | RIO GRANDE DO NORTE | Brasil | 2408805 | 24 | 33 | nan | nan | nan | Caatinga | 2.5 |
| ea034b54-0022-3050-9f07-f6983b9f545e | -5.81029 | -40.84124 | 2025-10-30 03:34:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| a23b2697-c887-3e55-aa12-85984095d7f9 | -5.79204 | -40.81068 | 2025-10-30 03:34:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 24e8f13f-6cb6-3f67-992a-783dcf293803 | -3.79564 | -43.90345 | 2025-10-30 03:34:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4f73ae53-703e-3b6d-ad4b-6cefbf5d5c56 | -2.77045 | -45.39943 | 2025-10-30 03:34:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 9.0 |


[Clique aqui para ver as próximas entradas](README12.md)

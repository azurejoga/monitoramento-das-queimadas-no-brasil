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

## Dados Diários - Página 73

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2827f0c2-535c-34a1-a5c1-46bf6c49ab49 | -5.7386 | -44.94907 | 2025-10-27 12:36:00 | TERRA_M-T | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 22.3 |
| ddb8ab15-1497-346d-951f-05b0621f62da | -7.10465 | -50.17605 | 2025-10-27 12:36:00 | TERRA_M-T | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 71631c3d-7821-31fe-8477-fa715f87e399 | -4.86641 | -43.26352 | 2025-10-27 12:36:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 59.9 |
| f0b6ed45-763d-356b-a2fa-32543dabe502 | -5.41029 | -44.41412 | 2025-10-27 12:36:00 | TERRA_M-T | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 29.6 |
| 7d0bb6fe-2518-38a0-9764-91fe45de823b | -4.45055 | -43.4085 | 2025-10-27 12:36:00 | TERRA_M-T | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 48.5 |
| 7a825241-4cf4-3472-9307-1fad495ffd00 | -7.76107 | -45.38807 | 2025-10-27 12:36:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 29.0 |
| bad202d7-29a2-3687-8fcf-21df084e7d13 | -8.10459 | -46.95563 | 2025-10-27 12:36:00 | TERRA_M-T | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 44.9 |
| 64f45d25-7bba-3029-8e91-006f2cdb7191 | -4.44725 | -45.45121 | 2025-10-27 12:36:00 | TERRA_M-T | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 75.9 |
| ed056e73-3ba5-3b79-aaf1-9cb15a7d6d9b | -6.18084 | -42.6008 | 2025-10-27 12:36:00 | TERRA_M-T | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 109.8 |
| 0939bb00-ccf5-3fed-a6a2-9bff272b480b | -7.43574 | -47.20943 | 2025-10-27 12:36:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 722d936a-1d85-37ce-b2cf-de5c5dd3b5f8 | -8.05523 | -46.94909 | 2025-10-27 12:36:00 | TERRA_M-T | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 3af0a7b3-6b69-3fbf-972f-9021009771ea | -3.47739 | -45.26118 | 2025-10-27 12:36:00 | TERRA_M-T | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 19.3 |
| a91a1560-b92b-3f5b-9295-5840e4689610 | -9.05769 | -45.11631 | 2025-10-27 12:36:00 | TERRA_M-T | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 25.5 |
| c80b4608-0add-3702-8dec-ec1f100fabaa | -7.073 | -46.75727 | 2025-10-27 12:36:00 | TERRA_M-T | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 63.5 |
| f973630d-adb7-3fb7-aebc-d0444d066400 | -8.01454 | -46.7494 | 2025-10-27 12:36:00 | TERRA_M-T | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 31.7 |
| 27f943ee-4cad-3060-b5cc-90f513438963 | -4.38492 | -43.30611 | 2025-10-27 12:36:00 | TERRA_M-T | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 67.9 |
| d9eaa8ec-249a-31d3-b4ce-b499dba70645 | -7.83617 | -48.27504 | 2025-10-27 12:36:00 | TERRA_M-T | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 16.6 |
| af49dc55-9c25-324e-8f6a-7ae01ff6164a | -6.07565 | -44.68047 | 2025-10-27 12:36:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 942a0716-498c-3c4c-9073-3568d4dd5e1a | -7.86348 | -46.40209 | 2025-10-27 12:36:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 29.9 |
| fd3ce30e-84ed-3dad-a1a2-da9c9c96d333 | -4.38581 | -43.33089 | 2025-10-27 12:36:00 | TERRA_M-T | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 140.7 |
| 0907a4ef-a20c-35c6-ac90-835dac6a9baf | -8.03514 | -45.19604 | 2025-10-27 12:36:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 48.0 |
| 145d2838-df78-347e-8682-dc73e3ece4d5 | -8.03819 | -45.17035 | 2025-10-27 12:36:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 187.8 |
| e50e0e6a-4595-3c24-9c18-506154178204 | -7.44987 | -47.19406 | 2025-10-27 12:36:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 57.0 |
| b164ad47-c22b-3ef7-9c55-bbb590f84f3f | -7.00879 | -46.96687 | 2025-10-27 12:36:00 | TERRA_M-T | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 1d90b6fd-b4c0-3846-a09c-6ec96a7bfff3 | -7.07621 | -44.95799 | 2025-10-27 12:36:00 | TERRA_M-T | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 27.2 |
| 37eb5d8e-fbba-3150-884c-67105fb49e56 | -8.096 | -47.05308 | 2025-10-27 12:36:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 65.7 |
| abc97e67-d01c-3387-b8d9-e03cdf7aa315 | -7.21119 | -46.71369 | 2025-10-27 12:36:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 146ee205-3a85-3896-91d0-d4ad78962d12 | -7.8277 | -46.47841 | 2025-10-27 12:36:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 115.7 |
| c063fce0-c2e6-35d9-8d6f-0da3d58552a6 | -4.86452 | -43.23652 | 2025-10-27 12:36:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 52.9 |
| b28c9bde-2ad4-3422-b2e1-ffff3563ca12 | -3.19738 | -43.46344 | 2025-10-27 12:36:00 | TERRA_M-T | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 38.6 |
| 500b3f0b-0d61-3d13-825c-710e97352e83 | -7.5886 | -45.69231 | 2025-10-27 12:36:00 | TERRA_M-T | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 43.3 |
| c89dca1c-1fd3-3f1a-8433-99a82205e7df | -7.25463 | -44.95988 | 2025-10-27 12:36:00 | TERRA_M-T | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 69.1 |
| b17e3147-12c1-350d-8026-07508695a695 | -7.68774 | -46.34661 | 2025-10-27 12:36:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 57.4 |
| ab603fe0-d5bc-34c0-a0eb-4ae7c5e283f9 | -3.6114 | -43.54679 | 2025-10-27 12:36:00 | TERRA_M-T | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 44.4 |
| 5ce9f2d5-2a4a-304a-b735-5aeb620a759b | -3.58679 | -43.60851 | 2025-10-27 12:36:00 | TERRA_M-T | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 75.2 |
| f6dbcb02-e4cf-355e-975f-fae8a8737674 | -3.58846 | -43.60227 | 2025-10-27 12:36:00 | TERRA_M-T | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 66.2 |
| e5f35778-d7bf-3b6f-b219-ae658f3bf855 | -7.86612 | -46.48286 | 2025-10-27 12:36:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 46.1 |
| f2531763-0522-3310-aba3-2711018eea26 | -0.35997 | -52.06347 | 2025-10-27 12:36:00 | TERRA_M-T | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 38.9 |
| be708cd0-4430-3fe8-a588-4bd799ccb3ad | -7.00204 | -46.97739 | 2025-10-27 12:36:00 | TERRA_M-T | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 601b8010-6b55-3b9d-9e91-cf7defc8ba09 | -8.10958 | -46.94415 | 2025-10-27 12:36:00 | TERRA_M-T | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 54.3 |
| bafc2933-5016-335c-8382-8c7b9d77b6fe | -8.52957 | -47.20524 | 2025-10-27 12:36:00 | TERRA_M-T | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 25.5 |
| 36868671-3a24-34ed-a0c1-dea9ad6f0426 | -3.34947 | -42.87251 | 2025-10-27 12:36:00 | TERRA_M-T | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 37.3 |
| 2fb8b61c-d1a8-3b19-ae56-a32c4ec6dcb5 | -7.95311 | -43.75879 | 2025-10-27 12:36:00 | TERRA_M-T | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Caatinga | 64.9 |
| 33f77649-4d2b-3866-a471-5856adccee4c | -6.87998 | -45.14421 | 2025-10-27 12:36:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 1bb7610b-8df6-39d8-927d-1ae469dce7e2 | -6.50495 | -46.58496 | 2025-10-27 12:36:00 | TERRA_M-T | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| f91be112-f0c0-37f1-b566-99e8676c5c85 | -7.91933 | -45.68254 | 2025-10-27 12:36:00 | TERRA_M-T | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 36.5 |
| 961f62ac-c4fc-3661-8a60-c4a9c1109f6d | -7.83744 | -48.28106 | 2025-10-27 12:36:00 | TERRA_M-T | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 14.2 |
| c485f1db-dbde-3327-9017-1521d22a97e0 | -7.8792 | -47.2733 | 2025-10-27 12:36:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 921027de-4f26-37bc-bfb9-c17304db3ce2 | -7.06066 | -46.75568 | 2025-10-27 12:36:00 | TERRA_M-T | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 0138da19-a7cb-3802-a1c9-68c79fa89dce | -7.07654 | -44.92622 | 2025-10-27 12:36:00 | TERRA_M-T | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 887df6a3-1b24-3f39-9260-6baafd9bd34e | -7.43941 | -44.58895 | 2025-10-27 12:36:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 50.5 |
| 5d013547-05dd-369b-bc02-d673d2bcda8c | -7.442 | -47.20452 | 2025-10-27 12:36:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 30.3 |
| c52e5370-74f9-32c0-aa5c-d4c4b5598d53 | -7.83013 | -46.45919 | 2025-10-27 12:36:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 2afb340c-1ecb-35fd-a9d6-6b402505a4c8 | -6.43858 | -43.13055 | 2025-10-27 12:36:00 | TERRA_M-T | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 5ba6ec3e-086f-39d5-9761-8d92af3bac90 | -3.33572 | -42.89714 | 2025-10-27 12:36:00 | TERRA_M-T | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 43.0 |
| 210c7186-73b6-3060-b650-6d7ee0e68f09 | -8.04888 | -45.16597 | 2025-10-27 12:36:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 112.4 |
| 52e83466-1233-3fbe-9a72-178f0821831a | -6.61474 | -44.62721 | 2025-10-27 12:36:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 34.8 |
| 8bfa1f66-574a-3907-8023-ccc74899beef | -7.07923 | -44.93325 | 2025-10-27 12:36:00 | TERRA_M-T | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 76.9 |
| aa3f14dd-a607-370c-80ed-9da08242448b | -7.68341 | -46.89537 | 2025-10-27 12:36:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 548d5c1e-08e2-37a0-8759-6d84d7bd8c64 | -7.7751 | -45.38933 | 2025-10-27 12:36:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 26.3 |
| 8b70db6f-f871-3de3-9e16-5a239df1b0a8 | -6.86766 | -45.17317 | 2025-10-27 12:36:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 25.1 |
| 2c9b32b9-2e5d-328c-a0b4-edabb4c885dd | -8.96578 | -47.18092 | 2025-10-27 12:36:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 32.3 |
| c3de430d-eb02-3377-85ff-bc5713f93d30 | -6.88827 | -43.55693 | 2025-10-27 12:36:00 | TERRA_M-T | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 197.5 |
| 0b2b4d22-8ae9-3365-86e2-a5a2556dfa99 | -8.02705 | -46.75119 | 2025-10-27 12:36:00 | TERRA_M-T | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 4476669f-1de7-3dc3-b2fa-1cd85a319dc3 | -8.04559 | -45.1918 | 2025-10-27 12:36:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 0ff57a81-a999-3c9e-95b7-a0c3537dd8b3 | -7.3566 | -45.13754 | 2025-10-27 12:36:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 28.5 |
| c76980ec-1ad7-3923-a93a-be43941f3cd7 | -8.94108 | -44.95942 | 2025-10-27 12:36:00 | TERRA_M-T | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 27.7 |
| 1bde707f-8148-3b09-b81a-ae17553e5181 | -7.8198 | -46.43773 | 2025-10-27 12:36:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 49.7 |
| 95ace23c-648a-3b1b-b4a4-1e5b30a27191 | -6.88161 | -45.17543 | 2025-10-27 12:36:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 3cdf6364-d850-3f5d-abe5-d1b139b75a98 | -7.95323 | -47.21991 | 2025-10-27 12:36:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 45ef99ed-a066-3109-a1a6-72659ff6794c | -6.89324 | -43.59729 | 2025-10-27 12:36:00 | TERRA_M-T | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 281.4 |
| ccce903e-7533-3504-b31d-40c0935f4f6a | -8.45218 | -48.22047 | 2025-10-27 12:36:00 | TERRA_M-T | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 30.6 |
| 09a50fac-5ac2-3d8e-a9c9-430bbe7bd351 | -7.87238 | -47.27888 | 2025-10-27 12:36:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 394d37f9-1c3c-3e8a-b969-89e40219b252 | -6.88458 | -45.15155 | 2025-10-27 12:36:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 108.8 |
| db131244-6c0a-3c17-80ac-2d5dadc97e4d | -6.89719 | -43.56461 | 2025-10-27 12:36:00 | TERRA_M-T | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 236.4 |
| f4e8378c-86ae-347c-8fa6-76b845915d0f | -9.30331 | -45.21971 | 2025-10-27 12:38:00 | TERRA_M-T | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 39.3 |
| fdbc1a55-1f41-3ab4-9319-15c2b970ed2a | -9.55962 | -46.92885 | 2025-10-27 12:38:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 22.9 |
| d423c017-3a87-379c-9177-0a0a7f074872 | -13.25978 | -54.37249 | 2025-10-27 12:38:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 29.9 |
| 2f80a726-08df-3968-be44-25890b15a60c | -14.07353 | -50.15786 | 2025-10-27 12:38:00 | TERRA_M-T | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 845ad04a-b5f1-3580-a15b-86bd6549760c | -14.65205 | -48.42247 | 2025-10-27 12:38:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 277.9 |
| e8764184-3da2-3f31-8f2e-4b233c258219 | -9.33955 | -48.18134 | 2025-10-27 12:38:00 | TERRA_M-T | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 575cd655-cc3e-330a-a721-3a38cd69aa08 | -11.41613 | -46.05799 | 2025-10-27 12:38:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 161.4 |
| 70490ff4-4f8e-35c5-8081-ee2b24341a8a | -10.31319 | -48.63386 | 2025-10-27 12:38:00 | TERRA_M-T | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 16.4 |
| a5d7efa4-9dde-3c3d-80ea-bb6b7524efb1 | -11.41852 | -46.08886 | 2025-10-27 12:38:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 304.0 |
| 2fe3198b-da9c-31ab-82ed-99d198313c15 | -8.6227 | -51.57559 | 2025-10-27 12:38:00 | TERRA_M-T | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 23.6 |
| 72a56e49-2a4f-3908-b87f-297cc3620749 | -13.25095 | -54.37119 | 2025-10-27 12:38:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 32d4e397-1906-3074-8646-8bb60485fdba | -10.31129 | -48.64868 | 2025-10-27 12:38:00 | TERRA_M-T | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 82936bd7-8755-34ab-80be-0dfa0b6a1d1a | -9.25414 | -45.84426 | 2025-10-27 12:38:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 199.3 |
| ccaeb112-f403-3a84-a227-ad880194aece | -10.25364 | -47.24542 | 2025-10-27 12:38:00 | TERRA_M-T | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 23.0 |
| c568314b-78a3-3f0e-91fd-9d0f5419710c | -9.55714 | -46.9483 | 2025-10-27 12:38:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 25.7 |
| ccf4c28f-b287-31f1-9641-786a0f81f8a2 | -11.08747 | -45.76422 | 2025-10-27 12:38:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 40.8 |
| d92dc411-7535-3fc6-9fe9-a9f998f56396 | -9.30549 | -45.22595 | 2025-10-27 12:38:00 | TERRA_M-T | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 37.2 |
| 360a03bb-1aef-3f0b-8de7-117a08858712 | -10.34776 | -47.10194 | 2025-10-27 12:38:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 24.1 |
| f1941ee2-cb74-386b-aa56-8035cb660c81 | -9.26351 | -45.82792 | 2025-10-27 12:38:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 20.4 |
| b9ec8881-390d-3014-8087-d549811d32fe | -13.04992 | -45.86561 | 2025-10-27 12:38:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 48.5 |
| 8fb87fc5-a166-3e9c-8d0d-12730a3efdf2 | -9.47779 | -46.85368 | 2025-10-27 12:38:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 51.2 |
| ed1b96e6-c0d1-3b02-aa76-7aa426f304e9 | -8.62139 | -51.58499 | 2025-10-27 12:38:00 | TERRA_M-T | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 38dd27c2-9517-3716-bcac-56f1f031223d | -9.57748 | -46.89867 | 2025-10-27 12:38:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 8b02fd48-79d6-378d-9bab-ea163ae02db8 | -14.07521 | -50.1446 | 2025-10-27 12:38:00 | TERRA_M-T | UIRAPURU | GOIÁS | Brasil | 5221577 | 52 | 33 | nan | nan | nan | Cerrado | 12.9 |
| f9e3f0af-d1bc-3ec4-9a33-05021cff8fbb | -13.32544 | -54.36992 | 2025-10-27 12:38:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 22.2 |


[Clique aqui para ver as próximas entradas](README74.md)

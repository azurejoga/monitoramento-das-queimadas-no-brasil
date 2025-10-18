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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7229968d-5ad9-3451-bf9a-67a2e6103e67 | -13.73727 | -44.22763 | 2025-10-18 04:02:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 00c7287a-0e76-3f71-9341-421c9f042bfd | -8.55098 | -50.0769 | 2025-10-18 04:02:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bae95a2e-9b54-3b2e-aae8-2b27185db6ba | -8.11622 | -40.34923 | 2025-10-18 04:02:00 | NOAA-21 | SANTA CRUZ | PERNAMBUCO | Brasil | 2612455 | 26 | 33 | nan | nan | nan | Caatinga | 1.9 |
| becdae5d-05ec-38d7-a0d3-b8ffd5ce8d76 | -12.29874 | -47.10822 | 2025-10-18 04:02:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| acaffd02-b6e3-3a66-b6dd-91ff943a081a | -8.81042 | -49.6817 | 2025-10-18 04:02:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 838214dc-3f9c-3de2-a23f-5d71c77f69ba | -8.61062 | -40.19449 | 2025-10-18 04:02:00 | NOAA-21 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 5c09b42a-f0ca-3883-a25e-24e60743dded | -10.48863 | -43.44126 | 2025-10-18 04:02:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 26.3 |
| 8ed65dce-a7fa-307b-8c02-ac2c0aa0d619 | -10.55981 | -43.8206 | 2025-10-18 04:02:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a4173535-d226-39fd-b7db-5b7663be0067 | -10.51912 | -43.40907 | 2025-10-18 04:02:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8f49ae8d-1dde-33f9-8ae4-97de05217179 | -10.48915 | -43.41655 | 2025-10-18 04:02:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 29a5b022-867b-307e-b820-08ae403b6ea1 | -6.40777 | -47.21109 | 2025-10-18 04:02:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3d33c8df-9fc7-3b54-8c4a-a7d6e749229c | -6.93759 | -43.69386 | 2025-10-18 04:02:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d0363dd6-c799-3cda-8146-2db7406c3013 | -11.5975 | -44.06828 | 2025-10-18 04:02:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 11c81e42-65b6-327e-9dfb-53183ff52ffc | -9.50526 | -47.264 | 2025-10-18 04:02:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| f2778451-f1c1-3d99-b86b-07eb7855fd03 | -10.47993 | -47.73656 | 2025-10-18 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 00d6681f-de95-3b8a-a3f6-c85bf4f03daa | -11.35237 | -44.27352 | 2025-10-18 04:02:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e390add0-b0ca-368d-adfa-abf6a444ef8b | -6.88854 | -45.43017 | 2025-10-18 04:02:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ee8a3093-5409-38b9-a0c4-920b2308fad3 | -8.17792 | -47.04133 | 2025-10-18 04:02:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1fd4c592-89d1-3976-9b70-c78454d95446 | -8.82103 | -49.68368 | 2025-10-18 04:02:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ee02d7d6-696c-3eb5-9838-b0d52d8a268b | -13.72623 | -48.37406 | 2025-10-18 04:02:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2c25831e-b172-3dec-9e7a-7e5b2800a5d6 | -13.02995 | -46.94971 | 2025-10-18 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| dfaa420b-02dc-33a7-8322-7a3ea6d6a8b6 | -7.45493 | -42.69284 | 2025-10-18 04:02:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 87aec07d-29a8-34a0-9a41-88a01a6abb91 | -7.66506 | -44.6333 | 2025-10-18 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3e694d2d-23f1-31d0-a80c-b4ce52cb79ce | -6.86665 | -44.70419 | 2025-10-18 04:02:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| db612bd1-1f1d-3b5a-a4b9-b1e315f7753a | -11.0026 | -47.9048 | 2025-10-18 04:02:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b85d27e2-450b-3108-ab47-b6fc7c9e8aa3 | -6.89295 | -45.45404 | 2025-10-18 04:02:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7de4a128-a08e-3b1b-95fd-28673d753e0a | -10.48769 | -43.40377 | 2025-10-18 04:02:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 63d1d831-cd17-37e9-baf4-e95f40247e40 | -10.50547 | -43.44812 | 2025-10-18 04:02:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 1427b9a3-2d08-3288-87dc-49a65f1bfb03 | -10.24335 | -44.07035 | 2025-10-18 04:02:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b8f6d9bf-c29c-3b7c-b0ac-69ba16b2abb0 | -14.09656 | -43.63611 | 2025-10-18 04:02:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 1b043185-d43f-3692-91b1-3d06823c5490 | -9.91658 | -47.65678 | 2025-10-18 04:02:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 4d715ab9-85b1-3d0a-8f89-8f82b71f3b32 | -7.16657 | -42.36985 | 2025-10-18 04:02:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| df57a6f8-b657-3086-90a9-8089ba8d73e7 | -8.64622 | -47.0846 | 2025-10-18 04:02:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e61a85ef-6533-3b19-99c8-9e8decfd930d | -8.44247 | -44.17277 | 2025-10-18 04:02:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 3072f6a6-9242-3002-9bc2-53fbcdb890d7 | -10.57888 | -47.39511 | 2025-10-18 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| a3287f64-9652-33ca-bb84-c22fbd0a447d | -11.48922 | -44.19599 | 2025-10-18 04:02:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e2cb29da-d6d5-3068-b890-bf9b90288282 | -13.42001 | -43.7508 | 2025-10-18 04:02:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a666561e-89db-3905-941a-73e67c5563a2 | -8.31579 | -43.42057 | 2025-10-18 04:02:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 2d6881a0-9d4d-3466-9a0c-383c0fdf291e | -13.52932 | -41.33384 | 2025-10-18 04:02:00 | NOAA-21 | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6b90ed43-3c16-3fc1-9696-c2f19b9418fa | -10.81751 | -43.9289 | 2025-10-18 04:02:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bc7e25cf-0cdd-3f38-b69b-993d28f35970 | -11.00446 | -47.89474 | 2025-10-18 04:02:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d03a74ae-23c4-3f61-8062-066a4d59ef6a | -10.6361 | -42.29923 | 2025-10-18 04:02:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 5.6 |
| aa1292c7-85bc-3a51-a6e2-acf9cdf6e77d | -8.43926 | -48.70098 | 2025-10-18 04:02:00 | NOAA-21 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1d2d29d1-16f4-3564-9ff9-8069e20d00e6 | -8.36922 | -46.20636 | 2025-10-18 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3ec3ffbb-e858-3d6d-a659-a63003ee0aa9 | -12.58649 | -43.36727 | 2025-10-18 04:02:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 52c0150e-365d-3a19-9217-11f896cec256 | -10.49629 | -43.43844 | 2025-10-18 04:02:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 34.8 |
| dd5a6851-c253-3bba-afde-b1a1f23b5fb6 | -10.07499 | -47.64051 | 2025-10-18 04:02:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ec939939-2fab-3ca5-88a0-9045b8469936 | -8.26105 | -43.3367 | 2025-10-18 04:02:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b5e82e4a-6eaa-362e-8f51-d285aba89803 | -10.80623 | -44.01706 | 2025-10-18 04:02:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 62cf484c-ca2d-3748-8e8c-1d347294331e | -13.41307 | -47.9771 | 2025-10-18 04:02:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0f66c13b-5c83-3e39-bc45-980fc36c63d4 | -10.25826 | -44.03298 | 2025-10-18 04:02:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 30c4a80b-cc1a-3e44-b77d-8e68462b717f | -10.82179 | -43.93086 | 2025-10-18 04:02:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f01c0bcd-87b0-3c35-8037-aad845e79ed8 | -10.42765 | -47.73448 | 2025-10-18 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 31135fd7-4c88-3f7b-9092-631d3d42a6f8 | -7.96968 | -38.28163 | 2025-10-18 04:02:00 | NOAA-21 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 0ca2c07b-15f0-3c45-87b3-da34117278e0 | -7.66039 | -44.63739 | 2025-10-18 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f13626c1-9d44-35dd-bf67-cdedbd11e9da | -10.70215 | -44.56625 | 2025-10-18 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ab5df3a6-4f00-340c-abb8-4906057d660a | -10.57611 | -44.50996 | 2025-10-18 04:02:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ed86f1cf-2f44-3d65-816a-75d2ad358cbd | -11.81066 | -44.58786 | 2025-10-18 04:02:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 74f82d60-e6d1-3ad3-be04-e672eb902200 | -10.49545 | -43.42187 | 2025-10-18 04:02:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 118f2fa9-464c-332c-909b-4bc3745007c2 | -13.84332 | -42.38287 | 2025-10-18 04:02:00 | NOAA-21 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 89be6e01-6de3-36d6-a97b-f95dc98ae761 | -9.75178 | -43.95839 | 2025-10-18 04:02:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| ebe5147e-019d-3ac6-86dd-f413976ad3f5 | -9.90943 | -48.14457 | 2025-10-18 04:02:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a4f0a4d2-5b4c-3459-b4ba-ef8600ec0879 | -6.97899 | -44.87339 | 2025-10-18 04:02:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6f688b87-b71b-3dfa-9012-75d159305d6d | -9.28428 | -43.73848 | 2025-10-18 04:02:00 | NOAA-21 | GUARIBAS | PIAUÍ | Brasil | 2204550 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 1ae2f67f-3975-3bf0-a3f6-76294193f87e | -7.34549 | -43.86313 | 2025-10-18 04:02:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 877d96c5-aa98-329e-bb66-c4dac2718dcc | -6.79128 | -46.47436 | 2025-10-18 04:02:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6474f1e4-fd7c-30b7-9bfd-cffaea1a5da9 | -13.47613 | -48.12645 | 2025-10-18 04:02:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 81668dc1-895a-353b-b6ae-75d12b57a908 | -12.71005 | -45.84775 | 2025-10-18 04:02:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 409d4639-ed14-36bf-987c-b9d2062de228 | -10.71553 | -44.54852 | 2025-10-18 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9f48414e-85f5-3a2a-bf66-cd9ba3f435d9 | -9.55188 | -47.76923 | 2025-10-18 04:02:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bbfa6289-4da3-3b7f-858f-583a1e7a20bf | -8.27946 | -41.45237 | 2025-10-18 04:02:00 | NOAA-21 | SÃO FRANCISCO DE ASSIS DO PIAUÍ | PIAUÍ | Brasil | 2209658 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| ed3025aa-34a7-3dad-a0be-ef04f91ca934 | -7.16594 | -42.37369 | 2025-10-18 04:02:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| ff8c5f6d-2ab5-3dbe-994c-28926f9eb511 | -10.49761 | -43.43048 | 2025-10-18 04:02:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 0bd6402f-515c-3de1-96f1-590550bd7953 | -10.48796 | -43.44524 | 2025-10-18 04:02:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2e6872fa-ec4d-3b7d-ad3c-65307e314e0f | -7.84483 | -40.25991 | 2025-10-18 04:02:00 | NOAA-21 | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 195df0c7-adb3-3502-af47-3aa351ec9524 | -13.22948 | -43.98365 | 2025-10-18 04:02:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c5a60e37-e8bd-340b-89d0-9bcf6c4b1f06 | -11.14933 | -47.72366 | 2025-10-18 04:02:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 917043f5-3b44-31be-bc61-a3889dce90cc | -7.49129 | -47.02882 | 2025-10-18 04:02:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f5336ded-f53e-38e4-ab46-ccc909b79fc2 | -10.80911 | -44.02182 | 2025-10-18 04:02:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 211468e1-c405-3a9a-8efb-a164b886c615 | -9.88684 | -49.11867 | 2025-10-18 04:02:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d5e1a23b-77ac-3bdf-952d-de561ced8829 | -8.94892 | -49.01856 | 2025-10-18 04:02:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e627e519-7189-3307-b90f-3d4a1a72df2d | -9.41887 | -47.01081 | 2025-10-18 04:02:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 54e07b84-8342-391f-9eef-afe0f67c06fa | -10.24112 | -44.06136 | 2025-10-18 04:02:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5d637bca-c397-3534-9eb7-a579d7e51185 | -11.38488 | -44.30087 | 2025-10-18 04:02:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2e71bf9d-1d65-3103-8952-5984efc3a635 | -8.54574 | -50.07814 | 2025-10-18 04:02:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 943076df-da0b-338d-ad01-cde1322d5ded | -7.39505 | -44.74859 | 2025-10-18 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6ef8a3d5-f063-33fc-9a03-1b460390ffca | -8.22627 | -47.84172 | 2025-10-18 04:02:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cdd751fa-0f27-3860-a4fe-49088733faf8 | -7.75941 | -42.51109 | 2025-10-18 04:02:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 8f9dc224-b0cf-3254-b0d8-527c4e4b03d7 | -8.85336 | -41.02979 | 2025-10-18 04:02:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6a9814bd-4cb0-37f6-99c8-88dd96c7aade | -12.53159 | -43.76309 | 2025-10-18 04:02:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 62b941aa-104e-3ce1-8894-1b0e7da7dd04 | -8.78533 | -41.52335 | 2025-10-18 04:02:00 | NOAA-21 | LAGOA DO BARRO DO PIAUÍ | PIAUÍ | Brasil | 2205565 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 7c39236c-f48b-349b-9efb-b360c39c16ce | -11.151 | -47.7257 | 2025-10-18 04:02:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 82a1420e-5b47-3c82-9dd2-16e5ab24793d | -10.23385 | -44.06037 | 2025-10-18 04:02:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 2aea1f75-4a5b-39c6-879e-9704510e9dd2 | -14.09859 | -41.08115 | 2025-10-18 04:02:00 | NOAA-21 | TANHAÇU | BAHIA | Brasil | 2931004 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b747954b-fc57-303f-94a7-ca7939cf46b8 | -10.85253 | -43.96059 | 2025-10-18 04:02:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 4a2639a7-f1b1-3e51-bb4c-f6e21db97676 | -12.4685 | -45.46833 | 2025-10-18 04:02:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 823731d7-8edb-3e4b-8373-3392fa46db3c | -10.62486 | -42.30485 | 2025-10-18 04:02:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| e5cdea6a-bd2d-3e3b-9f13-2ac68f2708af | -10.24978 | -44.05384 | 2025-10-18 04:02:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 86db22c5-ab0c-3961-88f0-e79f33f5a2d6 | -11.49918 | -44.18049 | 2025-10-18 04:02:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 23238618-6b79-336c-ae48-52a8ebb0517d | -11.00128 | -47.87908 | 2025-10-18 04:02:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README23.md)

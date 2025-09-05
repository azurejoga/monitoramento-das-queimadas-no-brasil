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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5275d1b7-3715-33ae-ad21-25b43971a438 | -16.4538 | -45.26522 | 2025-09-05 03:19:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2ede68be-8d4c-3c4f-92af-92e48e58f012 | -21.7966 | -46.8077 | 2025-09-05 03:19:00 | NOAA-20 | VARGEM GRANDE DO SUL | SÃO PAULO | Brasil | 3556404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.4 |
| ab51b879-ba51-3c18-9c71-f0dceeffb701 | -16.45537 | -45.25852 | 2025-09-05 03:19:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c8f64ee9-081a-393d-8743-c32e0ce6cf9d | -16.37358 | -43.03843 | 2025-09-05 03:19:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8d61faf0-e38a-3e0c-8c8a-3f3dd349041c | -21.50427 | -41.26094 | 2025-09-05 03:19:00 | NOAA-20 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 6e5e8b8d-ea69-3aa6-8213-d6ec7b92fd50 | -16.45519 | -45.26364 | 2025-09-05 03:19:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 842e482c-07a7-3c0e-81af-ebca62326887 | -16.49389 | -43.73045 | 2025-09-05 03:19:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7d200b74-020b-3890-ba3d-c4d5687e2dd8 | -16.45671 | -45.25693 | 2025-09-05 03:19:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4ed6c77b-155d-3639-ad22-a1715f900626 | -21.49021 | -46.20114 | 2025-09-05 03:19:00 | NOAA-20 | DIVISA NOVA | MINAS GERAIS | Brasil | 3122405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 9480eece-90e0-34dc-8d49-392a2aeadaa0 | -18.95098 | -44.68879 | 2025-09-05 03:19:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9481a504-06cb-3d0f-89dd-dca76e8d6484 | -18.95238 | -44.68624 | 2025-09-05 03:19:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 68b59708-7417-3952-a7d3-b9cca2038510 | -16.45441 | -45.23503 | 2025-09-05 03:19:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0d72c167-d135-3119-a7b9-fc52b91157b9 | -16.45693 | -45.25184 | 2025-09-05 03:19:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4a5ce4f9-df56-3a28-bed9-863d18b044b7 | -21.49174 | -46.19492 | 2025-09-05 03:19:00 | NOAA-20 | DIVISA NOVA | MINAS GERAIS | Brasil | 3122405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a0d03e3f-c6af-30a8-9b35-1018cfa2f997 | -16.49263 | -43.73611 | 2025-09-05 03:19:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 990dcc8f-e587-3fc7-a553-da7ab0b7d399 | -18.95228 | -44.68311 | 2025-09-05 03:19:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3bfb5a33-b9ec-36c6-90bb-995b5ec64e3a | -18.5617 | -43.61592 | 2025-09-05 03:19:00 | NOAA-20 | DATAS | MINAS GERAIS | Brasil | 3121001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 93c0bae0-f580-372b-bcbc-988a3f6fe06f | -18.6172 | -44.26201 | 2025-09-05 03:19:00 | NOAA-20 | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 2072c017-42c8-3e04-8085-98349df07f20 | -19.79065 | -43.55715 | 2025-09-05 03:19:00 | NOAA-20 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e6887456-87cb-3eff-8481-120345a4c252 | -18.56206 | -43.61264 | 2025-09-05 03:19:00 | NOAA-20 | DATAS | MINAS GERAIS | Brasil | 3121001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 7cd31433-4b88-3395-858b-e6d49178c476 | -9.0762 | -47.0113 | 2025-09-05 03:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 45c77091-3e28-3f00-b105-c945a1e1e91c | -20.2476 | -51.3021 | 2025-09-05 03:20:00 | GOES-19 | APARECIDA DO TABOADO | MATO GROSSO DO SUL | Brasil | 5001003 | 50 | 33 | nan | nan | nan | Mata Atlântica | 112.8 |
| 272e16e1-4ab1-3452-86d9-fe91b413d34e | -5.6079 | -45.0265 | 2025-09-05 03:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 40.1 |
| 774cef91-ae93-396f-b87e-69197ad2bad5 | -15.6141 | -52.891 | 2025-09-05 03:20:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 6a41b9e6-01f5-3d6c-ac62-8853644a9018 | -22.51514 | -47.09733 | 2025-09-05 03:21:00 | NOAA-20 | ARTUR NOGUEIRA | SÃO PAULO | Brasil | 3503802 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 20beb69e-e225-358b-be24-1c7d6e1ed3bd | -22.50619 | -47.69541 | 2025-09-05 03:21:00 | NOAA-20 | CHARQUEADA | SÃO PAULO | Brasil | 3511706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| 53a1998c-579a-3e3f-b210-8ade99513e76 | -22.51697 | -47.0902 | 2025-09-05 03:21:00 | NOAA-20 | ARTUR NOGUEIRA | SÃO PAULO | Brasil | 3503802 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c401f9bd-8c8e-36e7-8234-f5bd0e3e7376 | -22.26087 | -47.64184 | 2025-09-05 03:21:00 | NOAA-20 | CORUMBATAÍ | SÃO PAULO | Brasil | 3512704 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c5de3999-c4f8-3f02-809c-b6dec91b336d | -22.87136 | -45.93018 | 2025-09-05 03:21:00 | NOAA-20 | SÃO JOSÉ DOS CAMPOS | SÃO PAULO | Brasil | 3549904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 3b7083ac-a757-3542-9c53-8f5037300b7a | -22.28248 | -47.63152 | 2025-09-05 03:21:00 | NOAA-20 | CORUMBATAÍ | SÃO PAULO | Brasil | 3512704 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| eb2e2e3a-45fd-3678-967c-65d04c58eec4 | -22.2754 | -47.62999 | 2025-09-05 03:21:00 | NOAA-20 | CORUMBATAÍ | SÃO PAULO | Brasil | 3512704 | 35 | 33 | nan | nan | nan | Cerrado | 6.8 |
| d19eddfe-36d9-3541-987d-70682d4cd155 | -22.2578 | -47.64006 | 2025-09-05 03:21:00 | NOAA-20 | CORUMBATAÍ | SÃO PAULO | Brasil | 3512704 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e12505a8-4624-332b-9b10-a3139bc9630e | -22.26615 | -47.65044 | 2025-09-05 03:21:00 | NOAA-20 | CORUMBATAÍ | SÃO PAULO | Brasil | 3512704 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 16fd05dd-9555-3e8c-9177-ac2e43dba3fc | -22.51313 | -47.69746 | 2025-09-05 03:21:00 | NOAA-20 | CHARQUEADA | SÃO PAULO | Brasil | 3511706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| a49823ef-ce99-3503-a3ff-836ec41fc64d | -22.263 | -47.64881 | 2025-09-05 03:21:00 | NOAA-20 | CORUMBATAÍ | SÃO PAULO | Brasil | 3512704 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9f2db67a-3f33-3cf4-ad73-5498285bc01d | -22.27839 | -47.63172 | 2025-09-05 03:21:00 | NOAA-20 | CORUMBATAÍ | SÃO PAULO | Brasil | 3512704 | 35 | 33 | nan | nan | nan | Cerrado | 7.9 |
| a18767b4-57f2-3500-86c4-6039c462a152 | -22.87759 | -45.93221 | 2025-09-05 03:21:00 | NOAA-20 | SÃO JOSÉ DOS CAMPOS | SÃO PAULO | Brasil | 3549904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| e87eaef8-f569-3ef1-92d1-275bd940e9df | -12.9853 | -54.8301 | 2025-09-05 03:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 178ac817-a441-32ed-85b7-007b61c0ce92 | -12.9665 | -54.8116 | 2025-09-05 03:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 22948c27-f58b-343a-bd79-d72143e6ca4f | -13.0044 | -54.8282 | 2025-09-05 03:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 69.2 |
| cc84c83e-0e6b-3de4-8011-224385ed0fb1 | -12.9668 | -54.791 | 2025-09-05 03:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 145.3 |
| 09ef68b9-59de-3e80-98e5-223ccaeb893a | -12.9856 | -54.8096 | 2025-09-05 03:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 119.0 |
| 19eff3a8-b0ba-3ff7-a134-58e5bd508395 | -12.9859 | -54.7891 | 2025-09-05 03:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 2798179f-5eb4-36ce-9202-e8a7124488c8 | -20.2476 | -51.3021 | 2025-09-05 03:30:00 | GOES-19 | APARECIDA DO TABOADO | MATO GROSSO DO SUL | Brasil | 5001003 | 50 | 33 | nan | nan | nan | Mata Atlântica | 115.1 |
| 93a2a44a-269a-3ba2-9870-b813a0083728 | -15.6137 | -52.9122 | 2025-09-05 03:40:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 43.6 |
| 031b9e09-70d9-3dff-bc6e-1f99d8fe9b38 | -15.6141 | -52.891 | 2025-09-05 03:40:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 43.1 |
| b8715810-af39-39d9-9945-0aac9a2fa0de | -12.9853 | -54.8301 | 2025-09-05 03:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 0615933d-3ad2-3454-8b6a-07f1675fd41d | -12.9859 | -54.7891 | 2025-09-05 03:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 65.0 |
| e39d30d4-07c3-30dc-851f-c3c07292c80f | -5.908 | -57.7311 | 2025-09-05 03:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 32.0 |
| 93d71804-5882-374d-8084-f6da658b8e32 | -12.9665 | -54.8116 | 2025-09-05 03:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 175fe0d9-10fc-3605-8d74-7fe4c126e6d7 | -13.0044 | -54.8282 | 2025-09-05 03:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 58.7 |
| e8236ec8-5f23-3952-856a-13920ffb2d02 | -12.9856 | -54.8096 | 2025-09-05 03:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 107.2 |
| 885dd571-38d8-38d6-9762-0f4ccd8514a9 | -12.9668 | -54.791 | 2025-09-05 03:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 133.1 |
| e7a2ae55-45bf-315e-9de0-da05fd2ce9c7 | -13.0044 | -54.8282 | 2025-09-05 04:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 58.6 |
| ba9ea621-b8cd-3b63-97d3-91087be79578 | -12.9665 | -54.8116 | 2025-09-05 04:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 691fd5d1-195b-38ca-8eb5-4ec68eb626b1 | -15.6141 | -52.891 | 2025-09-05 04:00:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 92bb129c-0134-3a6f-8c29-31d45ebfa38c | -12.9856 | -54.8096 | 2025-09-05 04:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 94.8 |
| fdfb2612-57db-32e6-9992-02108ceb712c | -12.9668 | -54.791 | 2025-09-05 04:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 138.7 |
| d5761371-8b58-369e-af88-9f7973aac9a8 | -12.9853 | -54.8301 | 2025-09-05 04:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 65.9 |
| b955e4ff-607d-3682-83e8-fdd4b877aa80 | -15.6137 | -52.9122 | 2025-09-05 04:00:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 533747e4-69ec-34d3-9475-f09813133e23 | -4.56735 | -40.3506 | 2025-09-05 04:34:00 | NPP-375D | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 90b763b2-1a73-3b64-a0d0-fc14e558873c | -6.27839 | -53.44131 | 2025-09-05 04:34:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2c2efc15-71d0-3223-a898-8687787fa889 | -5.45077 | -42.81364 | 2025-09-05 04:34:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 62d2632d-a7e8-3d04-83fe-ac76362167d0 | -6.25031 | -43.30496 | 2025-09-05 04:34:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2d1a7bae-902b-30cb-a9d7-834ca1755646 | -6.49816 | -43.73628 | 2025-09-05 04:34:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6659cc73-84be-3ccb-9858-9d965d974b38 | -5.03352 | -49.75839 | 2025-09-05 04:34:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 25167b05-56af-36b9-9d17-ec3dfd151854 | -5.3814 | -43.24736 | 2025-09-05 04:34:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 81d24234-23b3-3797-b6d2-adc21b6218b9 | -7.62063 | -42.64497 | 2025-09-05 04:34:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 49e97fc0-5613-38c5-92ac-739f1ee0971b | -3.9931 | -47.37143 | 2025-09-05 04:34:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7a9b1f7f-76d5-3ab9-8012-b61eaf60c7cd | -5.6296 | -45.73052 | 2025-09-05 04:34:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 49fd0a4e-5077-3b08-ac6b-c9bb36d69971 | -6.16202 | -44.31136 | 2025-09-05 04:34:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2dae8f31-2a8b-3938-8b1e-5bb7b69e6900 | -7.01652 | -43.23145 | 2025-09-05 04:34:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 736dac13-c3c6-3587-9313-1355965925b1 | -7.59087 | -44.67532 | 2025-09-05 04:34:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 51feabb2-9095-352d-93d4-a49cb2bf1418 | -5.75178 | -45.54936 | 2025-09-05 04:34:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e160bc71-cd51-3868-96ed-c41306faa8a6 | -5.97769 | -43.82084 | 2025-09-05 04:34:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6c07733a-7b84-3001-942e-cf74d25b22b6 | -6.88572 | -45.55614 | 2025-09-05 04:34:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6bf92bff-a3b0-35e2-815f-01de36e23cc9 | -7.88943 | -45.24023 | 2025-09-05 04:34:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a391325f-efe6-31fd-8613-0dda4204f2b2 | -4.23894 | -48.55706 | 2025-09-05 04:34:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f30438f3-7ff3-3177-8724-eb1a9d5d2f2f | -6.22964 | -42.62229 | 2025-09-05 04:34:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 8aa915cc-2092-3278-8e8e-5711fe3cd99c | -4.85918 | -42.54138 | 2025-09-05 04:34:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ac56f7cb-a8bd-3f64-af87-18293dbe08ea | -5.87594 | -46.03498 | 2025-09-05 04:34:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e1ac88da-8ba4-3f94-b7e1-1ddacefd0b1d | -5.2118 | -43.69355 | 2025-09-05 04:34:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| cd56bfa5-f66c-37eb-87c6-6476190a6dd1 | -6.15443 | -43.17116 | 2025-09-05 04:34:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 44d2af74-43f9-3449-bb72-48f9b3deda6b | -7.61374 | -43.84438 | 2025-09-05 04:34:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e769a6ec-a1f9-34e9-9c9f-0c56e9d217cb | -6.15339 | -43.17208 | 2025-09-05 04:34:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6aa49c2f-4c47-3510-ac3e-9270d12d858f | -3.60944 | -52.64108 | 2025-09-05 04:34:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f732f430-4e82-3472-8257-d0ff819bde19 | -6.89528 | -45.19154 | 2025-09-05 04:34:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3083e35a-78d6-3990-ac85-16c3342af265 | -6.23563 | -42.63777 | 2025-09-05 04:34:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 36ec7eea-e05d-3144-8967-74649585f733 | -6.35311 | -47.09789 | 2025-09-05 04:34:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 42b84d5d-025e-3552-aa16-158969db59d7 | -5.57518 | -45.64968 | 2025-09-05 04:34:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a6abcca9-71b9-35f5-86df-93fe05242ae1 | -6.95945 | -43.9558 | 2025-09-05 04:34:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 49e8e595-3904-3759-91b9-b4084d40d175 | -5.57926 | -45.1276 | 2025-09-05 04:34:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 271f2965-dcd4-3b3e-8ebb-0db4cc032ddf | -2.4061 | -48.39999 | 2025-09-05 04:34:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6ac02f0d-08fb-38cc-b1cc-4238b9e081dd | -6.31044 | -44.84952 | 2025-09-05 04:34:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a50e0657-f5a9-3b4f-a690-db902140dea5 | -7.90722 | -44.92937 | 2025-09-05 04:34:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 798fb015-d727-3187-bec6-bdd0cef3fe3f | -6.04555 | -45.99697 | 2025-09-05 04:34:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0f14215a-1100-3022-a87d-a99a805a4f03 | -7.89648 | -45.23197 | 2025-09-05 04:34:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8df72723-14b7-3d73-91ff-d93357627702 | -6.1223 | -42.95408 | 2025-09-05 04:34:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| fb69b73b-51c9-36ea-a3f8-1f258854d48e | -6.12579 | -44.11092 | 2025-09-05 04:34:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8362068f-d291-3fcf-9b15-af700d8f4aa3 | -6.54245 | -43.90891 | 2025-09-05 04:34:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README15.md)

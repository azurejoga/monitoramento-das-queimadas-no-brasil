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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8e067349-e64c-383b-b96e-fc29f4af333d | -3.01862 | -45.39898 | 2024-11-17 03:44:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 312bc7a5-60b1-3b68-9eec-e61da3b07590 | -6.49713 | -47.50104 | 2024-11-17 03:44:00 | NOAA-21 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ad2e1508-66d3-326c-a237-60083419b7b3 | -8.44593 | -44.18457 | 2024-11-17 03:44:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 3dd2ae95-e2ab-39c4-916c-5f064bb9675b | -2.67156 | -46.21988 | 2024-11-17 03:44:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5af486e1-4910-321b-87f4-3f2f254f61f2 | -3.62242 | -43.15572 | 2024-11-17 03:44:00 | NOAA-21 | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2a91d3a0-98b5-3283-a1f2-924c2a679092 | -7.6605 | -38.83683 | 2024-11-17 03:44:00 | NOAA-21 | BREJO SANTO | CEARÁ | Brasil | 2302503 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 9eaaf48e-0a94-3743-868f-3b589b59d290 | -3.41636 | -46.13755 | 2024-11-17 03:44:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c6b42c0b-1d9f-3183-9f84-da26303c33b7 | -3.24211 | -43.42997 | 2024-11-17 03:44:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bc73dc61-b43a-3cbf-880c-4187a572921c | -8.44541 | -44.1875 | 2024-11-17 03:44:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 34630c66-571d-3720-b60d-505206190061 | -2.65545 | -46.21547 | 2024-11-17 03:44:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e9ef55ad-aefe-3e86-9b34-72466cd60750 | -7.0489 | -40.41756 | 2024-11-17 03:44:00 | NOAA-21 | CAMPOS SALES | CEARÁ | Brasil | 2302701 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 6ba6a39f-33a2-3b57-8e23-12bb03e779b5 | -8.28062 | -45.96677 | 2024-11-17 03:44:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| dd7c254e-8d25-386d-b109-90f47af501f8 | -5.40637 | -46.34737 | 2024-11-17 03:44:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5c7e0e52-2a92-3ece-8d17-c74f05edd7ee | -6.49074 | -47.49993 | 2024-11-17 03:44:00 | NOAA-21 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 6348451c-a0ef-3551-a894-259024cda4e8 | -3.78322 | -43.90818 | 2024-11-17 03:44:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 33edd407-6671-32bb-92eb-14c3cd1abad4 | -2.09227 | -48.27232 | 2024-11-17 03:44:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 77c02bd2-7c80-3cbf-a877-5f86821bfed0 | -5.4611 | -42.15096 | 2024-11-17 03:44:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 1d5a10eb-e31a-3287-912c-484ecc801a17 | -3.03873 | -45.75832 | 2024-11-17 03:44:00 | NOAA-21 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b25d2c4a-ed0c-3798-a8f4-7c7aa46e29fe | -8.28654 | -35.66718 | 2024-11-17 03:44:00 | NOAA-21 | SAIRÉ | PERNAMBUCO | Brasil | 2612000 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 7cfcd32c-f22b-3acb-b352-b68595b40f49 | -8.45278 | -44.20419 | 2024-11-17 03:44:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9ad58859-6669-3fc4-8f1d-319b36f700bf | -6.90685 | -35.61514 | 2024-11-17 03:44:00 | NOAA-21 | PILÕES | PARAÍBA | Brasil | 2511608 | 25 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c98bc650-eccd-3404-be78-6ca75e00293e | -4.81201 | -44.48149 | 2024-11-17 03:44:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| aec265e1-32cd-370d-b86f-781c88e65418 | -8.45329 | -44.2013 | 2024-11-17 03:44:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8b008bfd-7c5e-3579-a777-923feba68790 | -7.3036 | -39.62074 | 2024-11-17 03:44:00 | NOAA-21 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c632cec6-5132-31fa-8531-3847d0b90d14 | -4.53525 | -43.29436 | 2024-11-17 03:44:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f07dc448-2a74-3faf-b0e0-79b4d5d7e484 | -2.60744 | -46.25501 | 2024-11-17 03:44:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d901dbac-d5ec-3b3a-836b-3da714d1fdff | -5.59208 | -45.21252 | 2024-11-17 03:44:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b9d20d9b-0498-3a7f-9603-236bd1e48443 | -3.00753 | -45.42842 | 2024-11-17 03:44:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 9.3 |
| e4481e95-5a1d-314e-b96f-a9545e3dc079 | -4.65329 | -45.00186 | 2024-11-17 03:44:00 | NOAA-21 | LAGO DOS RODRIGUES | MARANHÃO | Brasil | 2105948 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 37cde8db-d0b3-355b-ac76-a4796e6a6bac | -7.5199 | -40.58351 | 2024-11-17 03:44:00 | NOAA-21 | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2ae2ee5b-10e8-3e04-a2d5-31a726fca7f9 | -2.65987 | -46.21281 | 2024-11-17 03:44:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ccf2fd8f-3ddf-329d-9714-7ed7152ab0ac | -2.62761 | -46.03427 | 2024-11-17 03:44:00 | NOAA-21 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a6d3f528-5a77-389e-abfe-92a545e527f9 | -8.51223 | -35.04146 | 2024-11-17 03:44:00 | NOAA-21 | IPOJUCA | PERNAMBUCO | Brasil | 2607208 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 5d09d0df-ffd8-319e-98b5-f7b8e8720a99 | -5.13697 | -41.43084 | 2024-11-17 03:44:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b0fcb480-afd5-32ee-805b-d596bc317b53 | -3.4175 | -46.13509 | 2024-11-17 03:44:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d8d0c2d4-72da-314f-87f4-2a0f65d74797 | -4.55461 | -48.00937 | 2024-11-17 03:44:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 4d07f1a3-a470-37a7-b95d-c15c30b28156 | -8.10306 | -35.20369 | 2024-11-17 03:44:00 | NOAA-21 | MORENO | PERNAMBUCO | Brasil | 2609402 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| b0ca9cfe-4dc2-3181-8ad9-1e5ace4af356 | -8.44231 | -44.20497 | 2024-11-17 03:44:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 0daf945e-f72b-3f36-8f24-9a0fd671d244 | -7.47208 | -40.34042 | 2024-11-17 03:44:00 | NOAA-21 | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 52235851-a5c6-3d96-b1f1-790676f5134e | -5.21128 | -43.7929 | 2024-11-17 03:44:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| cf44f95a-5a36-3d6b-9730-e0325eb87c7f | -6.40222 | -44.73993 | 2024-11-17 03:44:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f9ec8513-b03c-3bf6-84d6-6b64c8489500 | -6.38484 | -45.68882 | 2024-11-17 03:44:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 12484d59-c655-39f2-9a8a-f51efb2f4f1e | -4.9339 | -40.84324 | 2024-11-17 03:44:00 | NOAA-21 | IPAPORANGA | CEARÁ | Brasil | 2305654 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| fbf045f1-eec8-3352-beb5-27b73df547fd | -3.49504 | -43.78771 | 2024-11-17 03:44:00 | NOAA-21 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 838a7e5b-485d-321c-b179-74b8a19fed4c | -3.2183 | -42.08949 | 2024-11-17 03:44:00 | NOAA-21 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| be6ce429-a790-3454-998c-d6ad7d079029 | -7.65872 | -38.83771 | 2024-11-17 03:44:00 | NOAA-21 | BREJO SANTO | CEARÁ | Brasil | 2302503 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 7f11d146-9eea-3a6c-8611-e03590a1f9f9 | -3.17463 | -46.60006 | 2024-11-17 03:44:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 05db0d25-d557-309c-bf70-492162a2979e | -6.49578 | -47.49932 | 2024-11-17 03:44:00 | NOAA-21 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| aa444a63-bcc1-336b-b98a-bbd4de68332f | -5.69575 | -46.5642 | 2024-11-17 03:44:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 20d78111-0f19-32c4-b854-4fd5e2014b72 | -4.74101 | -48.12271 | 2024-11-17 03:44:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9cb67614-8080-3413-a3aa-fb23ab46fdb1 | -4.54226 | -45.2548 | 2024-11-17 03:44:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 6a74c8f5-1ffc-3039-ad17-3f57c062f2bd | -4.36807 | -43.0073 | 2024-11-17 03:44:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8a841011-0665-3904-90ce-682a38a0e5a4 | -2.6029 | -47.55166 | 2024-11-17 03:44:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 3a2d0346-ac14-3fc5-96d7-c8579a23534c | -4.14187 | -42.12867 | 2024-11-17 03:44:00 | NOAA-21 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 6a7e0f50-c23e-38da-a4eb-cf59b07dea2d | -2.62223 | -46.0283 | 2024-11-17 03:44:00 | NOAA-21 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 6883c6c8-89b8-365e-8172-872fe5c65aca | -8.29038 | -35.66424 | 2024-11-17 03:44:00 | NOAA-21 | SAIRÉ | PERNAMBUCO | Brasil | 2612000 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 07ac9d32-ce11-3ebf-bc66-16bf5bf33407 | -4.29791 | -48.0964 | 2024-11-17 03:44:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 72eba376-3a81-359d-86c8-73d2b775e4ca | -3.50034 | -43.78854 | 2024-11-17 03:44:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| c5975a84-bbd6-35a8-b5d0-e2993182d69f | -8.44334 | -44.19915 | 2024-11-17 03:44:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 15.0 |
| e1be165a-dffd-384a-a717-d6ea9568b727 | -5.46491 | -42.15643 | 2024-11-17 03:44:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 8892b7d0-8911-3d7c-9cf7-20c7377b6aee | -5.34089 | -40.90186 | 2024-11-17 03:44:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 491e400d-5ed5-314d-ad9f-96f3a73691c6 | -3.93399 | -46.17222 | 2024-11-17 03:44:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6ad3e465-4fa9-3707-85d5-223403a40f16 | -4.29605 | -42.18533 | 2024-11-17 03:44:00 | NOAA-21 | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| b519d85c-8a4d-3494-8b8d-5be0b0b095da | -10.72882 | -40.52509 | 2024-11-17 03:44:00 | NOAA-21 | MIRANGABA | BAHIA | Brasil | 2921401 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b210e18c-679a-3005-ac35-24d8420aa60d | -2.65276 | -46.21669 | 2024-11-17 03:44:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 79f19e8b-6d33-3960-87b6-8175a8507517 | -5.34111 | -44.99834 | 2024-11-17 03:44:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 64d729c7-f099-3773-96e8-0d34e89e4a69 | -6.38728 | -45.68424 | 2024-11-17 03:44:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 19c203ae-2ca4-3873-b6da-bf5b31198b9b | -8.28708 | -35.66371 | 2024-11-17 03:44:00 | NOAA-21 | SAIRÉ | PERNAMBUCO | Brasil | 2612000 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 16a925d3-2f02-33ab-9fe9-5d054c8a84e6 | -2.86598 | -46.7262 | 2024-11-17 03:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 11119571-6c76-3e87-896f-0d93aa8c81c8 | -3.21414 | -42.09235 | 2024-11-17 03:44:00 | NOAA-21 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2b7fb859-c6f4-35ef-b3b6-85f600a371cb | -8.44489 | -44.19042 | 2024-11-17 03:44:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 059c504c-ca14-37e0-ba79-e8084db8166e | -5.58878 | -45.21057 | 2024-11-17 03:44:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 291c9c67-51e5-31f6-8522-c527807afdf5 | -4.03825 | -45.47188 | 2024-11-17 03:44:00 | NOAA-21 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ea11594d-91ff-3ee0-be3c-a616d024ea1e | -2.66613 | -46.21388 | 2024-11-17 03:44:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 54a3f8ec-7c98-3007-93e9-7c7aded01f5c | -8.44884 | -44.19729 | 2024-11-17 03:44:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d94ecf73-3395-34ca-951f-757e85781021 | -4.99767 | -44.33533 | 2024-11-17 03:44:00 | NOAA-21 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 3e5888f7-69a8-3ebe-9f6f-7d6a3c00ef8b | -2.59393 | -47.56293 | 2024-11-17 03:44:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 39518e4d-baa2-3fd7-a731-29416d15b213 | -2.08858 | -48.27134 | 2024-11-17 03:44:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| c3329995-efe9-393e-afdd-a4662ac3e991 | -4.47339 | -48.11131 | 2024-11-17 03:44:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| fcae3a64-3e22-34b3-8961-77a1617288f9 | -2.67406 | -46.20509 | 2024-11-17 03:44:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8e57077f-a367-3fbe-9daf-626411dc05d1 | -4.23502 | -41.93311 | 2024-11-17 03:44:00 | NOAA-21 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| bbd5b76b-00ed-3105-868a-b8e494ed97c4 | -2.60076 | -47.56392 | 2024-11-17 03:44:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 10341fd0-f93d-3029-8309-948c3d673425 | -4.37247 | -40.588 | 2024-11-17 03:44:00 | NOAA-21 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 21513eb3-4e4f-376f-ab7b-832b0769316e | -4.45442 | -44.55028 | 2024-11-17 03:44:00 | NOAA-21 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| df5d0306-f163-3dd4-bee2-4da0814ed829 | -8.44283 | -44.20205 | 2024-11-17 03:44:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 716ff8ba-0565-39ad-8ed3-e5e5ae167b51 | -5.1216 | -45.15343 | 2024-11-17 03:44:00 | NOAA-21 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 73d670a4-adbb-3104-bd4b-d8048daa8d73 | -6.97848 | -38.48402 | 2024-11-17 03:44:00 | NOAA-21 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 14d031e0-fce4-3530-a7f5-46c22d00316e | -2.62841 | -46.02946 | 2024-11-17 03:44:00 | NOAA-21 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 133168e8-2117-3d39-b186-6f843cbd54f2 | -8.4368 | -44.20694 | 2024-11-17 03:44:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 5285b931-41e5-37a8-a48a-53905c5fea6b | -3.78046 | -46.03822 | 2024-11-17 03:44:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cc42933e-46fa-3c09-8b58-8a8b1c2b402a | -4.55717 | -48.00491 | 2024-11-17 03:44:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 41.1 |
| e34a4db0-5e08-342d-84bb-1f0ed16d908b | -10.69774 | -38.27947 | 2024-11-17 03:44:00 | NOAA-21 | HELIÓPOLIS | BAHIA | Brasil | 2911857 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 0ea74336-0186-3a1a-ad41-c082cea981bc | -7.45072 | -35.06923 | 2024-11-17 03:44:00 | NOAA-21 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b7b72f79-55a9-300f-aa42-bce833c0d120 | -4.11667 | -40.85033 | 2024-11-17 03:44:00 | NOAA-21 | SÃO BENEDITO | CEARÁ | Brasil | 2312304 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 00f87574-7dd5-3da2-a64f-2b32889482c2 | -4.18711 | -46.82026 | 2024-11-17 03:44:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e85a6e28-880b-34b6-92eb-73b7fa5080f7 | -5.33786 | -40.89393 | 2024-11-17 03:44:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 10fd4948-4df9-38f6-9f38-0e307083d572 | -4.29679 | -48.10273 | 2024-11-17 03:44:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 8adb6a83-eb64-3740-8157-264764b2d738 | -4.48024 | -48.1124 | 2024-11-17 03:44:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| db55b194-9779-3092-83f9-2107cb6e7f8d | -4.93385 | -40.84382 | 2024-11-17 03:44:00 | NOAA-21 | IPAPORANGA | CEARÁ | Brasil | 2305654 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 59eac9c8-1d10-333b-9125-71a487596642 | -2.59288 | -47.56897 | 2024-11-17 03:44:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |


[Clique aqui para ver as próximas entradas](README24.md)

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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4998e565-9b5d-37c4-bb65-16143ee113f2 | -7.75115 | -44.94489 | 2025-09-26 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e7666ad4-6279-3a90-ac24-a4689ae54c2b | -10.40748 | -46.16695 | 2025-09-26 04:14:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c40e099e-3256-336e-a3f6-4c025afced16 | -6.05768 | -43.58175 | 2025-09-26 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9ee0a4e2-4152-39a4-8fb7-362cf4aaf14a | -10.19217 | -44.86139 | 2025-09-26 04:14:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8c7b4dc8-1142-3667-bc25-6026ff92d905 | -5.53787 | -42.81487 | 2025-09-26 04:14:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| d4736451-ea46-3153-b8a1-87e0a07a0742 | -7.44314 | -41.90889 | 2025-09-26 04:14:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 96f8d7c3-e598-3eab-94b9-7ba188ae147c | -4.16847 | -44.27113 | 2025-09-26 04:14:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e74a1ebe-5da5-3f97-8581-ffb6d0e18e35 | -7.25517 | -43.01869 | 2025-09-26 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5dec2db3-f208-348c-9778-e5042c3f51eb | -4.12794 | -42.36766 | 2025-09-26 04:14:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 1060ac2a-3753-3e4e-9464-d7024e301ce6 | -8.85 | -46.60629 | 2025-09-26 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ad1d4cc8-d097-34a8-bd3d-74e07c4db1a9 | -8.84934 | -46.61036 | 2025-09-26 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b395854f-22a8-3a1f-932f-6d1334a19e3d | -6.25764 | -42.47923 | 2025-09-26 04:14:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| b7e532bc-e03f-3820-945b-30b9e3ad7293 | -8.84131 | -46.26228 | 2025-09-26 04:14:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1c44f7f3-527f-35ac-9ca4-0f6652de0a07 | -3.63035 | -43.86776 | 2025-09-26 04:14:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b89f45c1-36e5-3f42-8a1a-bbe9ed0feeae | -8.18716 | -46.37386 | 2025-09-26 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ae13647c-f9d4-38a7-a909-5a53d650a689 | -8.78074 | -43.03176 | 2025-09-26 04:14:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 62b2154b-8a23-35a8-9329-992d651fd5de | -6.80152 | -41.75616 | 2025-09-26 04:14:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 62f58731-7f5c-3170-92ef-ae2dce6b6441 | -6.25656 | -42.48616 | 2025-09-26 04:14:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 81fe6e9e-4ecd-3af5-9ed9-ae0e39f7c336 | -7.49188 | -43.89964 | 2025-09-26 04:14:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d566044d-ee2c-30f3-935e-d9e80651fafc | -5.29381 | -48.12416 | 2025-09-26 04:14:00 | NOAA-21 | BURITI DO TOCANTINS | TOCANTINS | Brasil | 1703800 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a4cf3fe1-31e6-36af-8151-24e76ff468dc | -9.75783 | -45.969 | 2025-09-26 04:14:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 99e1fad0-6f7e-38d5-b179-6f18d5c02e28 | -10.93745 | -44.30072 | 2025-09-26 04:14:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cbc93451-b896-3b14-b27e-53e12ea8cd59 | -8.13662 | -44.12743 | 2025-09-26 04:14:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cb8fd641-46e1-371b-bc28-e4b1a32dc8dc | -8.66824 | -43.99539 | 2025-09-26 04:14:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d17212da-2a54-3ac5-a4d1-0bf9252b1369 | -6.90916 | -44.80302 | 2025-09-26 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0968f642-ef2b-3347-9168-e79a4ae0bbae | -5.72932 | -42.63726 | 2025-09-26 04:14:00 | NOAA-21 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| d74a5dd8-5381-3a83-8e13-e07a02b6eefa | -7.28918 | -42.9785 | 2025-09-26 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 75fe32e7-f5e4-38ad-a091-6689ac847cc3 | -2.92162 | -48.31429 | 2025-09-26 04:14:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7f92c0ab-96ab-3c71-b0f4-5fa85fe2a04e | -5.82936 | -43.90874 | 2025-09-26 04:14:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| a6b66887-29bd-31b4-b0a8-26a279928ac8 | -5.31687 | -43.14308 | 2025-09-26 04:14:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fd6dd02d-ccdc-3892-a134-1198e7c32904 | -5.64837 | -43.93357 | 2025-09-26 04:14:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| aaf039ca-00f6-3060-ac3d-914712a53add | -5.46127 | -43.06705 | 2025-09-26 04:14:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 896db9f4-9679-3c1d-b5f1-a95e5abaf609 | -7.80225 | -46.01844 | 2025-09-26 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 0c811811-9a08-30a7-95e8-20cf789ca13c | -8.71773 | -50.05271 | 2025-09-26 04:14:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| abeb5273-795b-3b0a-bcff-b15b8edebba3 | -8.85787 | -46.20499 | 2025-09-26 04:14:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 60cf8fdf-27c9-3543-8521-2de7b0265797 | -7.63894 | -47.68847 | 2025-09-26 04:14:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ad4a054a-0429-3d51-99ab-f3a9ffd2630b | -5.60065 | -45.37734 | 2025-09-26 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| df3eff88-8cef-31e1-800b-1dbf889b85b1 | -5.74225 | -44.95558 | 2025-09-26 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 487da5b2-464b-3e28-a682-bb6cc9875e9e | -6.71326 | -42.74224 | 2025-09-26 04:14:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 6ca8ed96-de91-306e-a9ac-959e05441757 | -5.20166 | -43.72349 | 2025-09-26 04:14:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6fed3dea-85e8-39ef-bf5a-39f1061410d9 | -5.74778 | -44.9869 | 2025-09-26 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7d2c61c8-3456-3db7-a56a-f9d9919f7e66 | -5.4039 | -42.27799 | 2025-09-26 04:14:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b368a6c8-aa69-3708-970e-6d64c3958db4 | -7.6676 | -46.0006 | 2025-09-26 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 30f7652a-639d-30f6-87a5-13e49cf359b4 | -9.70272 | -48.25018 | 2025-09-26 04:14:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1139f2f8-8273-3ac0-aa0a-68f6c16d1583 | -4.74982 | -43.60876 | 2025-09-26 04:14:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 990a8b95-badc-304a-9245-7ab13d4dcfc8 | -6.89258 | -44.75594 | 2025-09-26 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 7d0209fc-4b1e-3caa-aa7b-b85ba4b25bda | -5.4684 | -43.06464 | 2025-09-26 04:14:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 76f25608-5724-304a-958a-72f77801fe08 | -6.63536 | -43.82664 | 2025-09-26 04:14:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 94fd8644-8f52-378e-9071-60ea42aac8fd | -7.11476 | -43.74299 | 2025-09-26 04:14:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5c32b22e-9f15-32b8-b1d0-61554671a1f5 | -8.77634 | -43.03825 | 2025-09-26 04:14:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 5a8ca611-63b4-331b-b902-a1db7e8b2212 | -6.26211 | -42.49416 | 2025-09-26 04:14:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0e0b099e-2b95-3099-8f1b-e18cc123a684 | -6.26649 | -42.48777 | 2025-09-26 04:14:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9b867f5e-f1f6-33f8-a049-191ecd5fa7db | -11.4825 | -39.00052 | 2025-09-26 04:14:00 | NOAA-21 | TEOFILÂNDIA | BAHIA | Brasil | 2931509 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 5783762c-375e-3cf5-beb8-d0bccae7cde2 | -3.86763 | -40.34374 | 2025-09-26 04:14:00 | NOAA-21 | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 608adf5d-0e45-3029-8b7d-5e57803f3762 | -9.48866 | -40.35469 | 2025-09-26 04:14:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 11.4 |
| e82125e0-b86a-3c92-8840-f4d0367d4182 | -8.79007 | -43.06172 | 2025-09-26 04:14:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 915ad465-302f-3fd9-bea8-a4f023089e79 | -5.80421 | -43.82989 | 2025-09-26 04:14:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 594317ff-9103-3099-8204-db10cdc7f4da | -5.62845 | -43.93039 | 2025-09-26 04:14:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 40cce9c2-7fc9-30ef-b5c0-f3155bbf25e1 | -3.86841 | -43.78209 | 2025-09-26 04:14:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b7220b67-1809-3792-a294-1c9eb55549a7 | -5.22315 | -44.4884 | 2025-09-26 04:14:00 | NOAA-21 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4dcb69a7-e5fa-3405-999e-6006ab412ae3 | -6.31897 | -41.88379 | 2025-09-26 04:14:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 1385914f-3120-3f9a-b6d8-72fc88ed55f1 | -8.77086 | -43.05168 | 2025-09-26 04:14:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a2c0c1ed-09f7-34c7-ba80-1dd45f8cbeee | -5.74108 | -44.96295 | 2025-09-26 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 60.1 |
| be9ac597-f02c-33f0-a9f8-209a6ccb01ae | -6.93893 | -44.63842 | 2025-09-26 04:14:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9188d1de-0fff-3f2f-b859-7d837eff59e7 | -8.14121 | -44.46481 | 2025-09-26 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 92643983-d4dd-3a4e-9142-bf9b4a7d3779 | -4.79859 | -43.03971 | 2025-09-26 04:14:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| a8c31c37-8372-329c-826b-79bfb913e5c0 | -10.10404 | -45.30624 | 2025-09-26 04:14:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dc95e926-837e-3781-897d-c9e0ba740cc6 | -10.40906 | -46.17885 | 2025-09-26 04:14:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b2ec3bbb-7781-3a8b-958c-8fbc9160c8d1 | -10.12354 | -45.31311 | 2025-09-26 04:14:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 28eeb56e-9596-3e64-8c39-be40b92aaf36 | -3.84442 | -50.96935 | 2025-09-26 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 54a7a138-a0b0-3113-8269-6875a5b7be50 | -5.98891 | -42.75945 | 2025-09-26 04:14:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d3ccf182-71d8-396f-870d-dc8d9142c6f6 | -6.98758 | -42.59625 | 2025-09-26 04:14:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| cffe50fc-506a-3e46-a355-120dffcec128 | -9.76535 | -49.31621 | 2025-09-26 04:14:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f96d2ee2-71b3-3638-8ff4-5a1cf96e2654 | -7.77433 | -43.92357 | 2025-09-26 04:14:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3c408f85-f875-3310-aeef-ff51437735f1 | -7.30994 | -45.76207 | 2025-09-26 04:14:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8ea56949-b9ea-33ff-b9b1-34e473526604 | -4.81236 | -43.53727 | 2025-09-26 04:14:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 75611e48-32ea-3219-8230-827b20650e71 | -7.81533 | -46.89742 | 2025-09-26 04:14:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d2aebb8d-9f03-3b24-b50a-b57fdd3ee58d | -9.85406 | -49.16761 | 2025-09-26 04:14:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7c1d474a-f041-3f90-accf-18fcb22ef349 | -6.48953 | -43.28287 | 2025-09-26 04:14:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 17e6250b-f12c-3844-9280-f3aaeae2d920 | -10.94951 | -44.26688 | 2025-09-26 04:14:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c767541d-6377-39f8-8949-3047158fe6c9 | -9.1174 | -48.89359 | 2025-09-26 04:14:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7205c24a-1600-3597-affd-6f7ab51987cd | -6.7171 | -42.73928 | 2025-09-26 04:14:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| fab006b6-b89b-3e6a-86e7-fe2cbaf5eb8e | -5.25041 | -43.06579 | 2025-09-26 04:14:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2d1f4a72-a4b5-3634-8a59-61160cf17b79 | -8.8537 | -46.25221 | 2025-09-26 04:14:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 12f159c5-af9c-3aa7-8928-5fe2093978ba | -10.93415 | -44.30019 | 2025-09-26 04:14:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7dcba514-f7ad-3b31-b434-9879f145647d | -7.45771 | -41.90379 | 2025-09-26 04:14:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| d26919de-fc52-3e94-ac52-31591741a93b | -6.99053 | -44.84607 | 2025-09-26 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 369dc9e5-9d45-36ca-ac6e-fd4d804d170c | -6.26542 | -42.49468 | 2025-09-26 04:14:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 519567f0-4f08-372c-84d2-26cda095a79f | -9.69245 | -48.94048 | 2025-09-26 04:14:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 6a7b9b15-dc1f-38bc-8f67-a74c474b01cb | -6.61259 | -42.92784 | 2025-09-26 04:14:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| fe292282-0289-3dfb-9034-0dbd2bd3c9a0 | -5.16622 | -42.71401 | 2025-09-26 04:14:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c6fd26f5-4b25-308b-b2eb-788547a87d9b | -8.2816 | -44.94925 | 2025-09-26 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 72a99465-d188-35ea-ba49-552c38bba5f8 | -5.72612 | -44.9911 | 2025-09-26 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3f829820-8527-3f07-b364-a941e6b704b7 | -6.25987 | -42.4867 | 2025-09-26 04:14:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 3ab82e31-c944-32f2-adcc-7987a1ebaa87 | -9.88231 | -47.7463 | 2025-09-26 04:14:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 26339ab0-8371-3911-9bcd-8ba3287f7611 | -6.91504 | -44.74482 | 2025-09-26 04:14:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 377788ac-ec4a-36d6-807d-e47c75fd7f3b | -7.63519 | -45.99211 | 2025-09-26 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e6ec6c56-64d5-360a-b5fb-fe7511ff1a24 | -3.33469 | -50.25264 | 2025-09-26 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 14a342b5-ec05-3105-a966-fd8b1107f474 | -7.05591 | -46.42699 | 2025-09-26 04:14:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5d4ae216-9d2d-317c-a53d-9fe6b48bf748 | -5.7039 | -43.64619 | 2025-09-26 04:14:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README11.md)

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
| 9210ea51-eaf4-33ee-9edf-a259f2468d16 | -4.14203 | -39.99433 | 2025-09-27 03:53:00 | NOAA-21 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 80bd75b3-107b-3a6f-9244-e3c4b5d47a9c | -6.24819 | -42.48115 | 2025-09-27 03:53:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 11b58063-105d-36a5-8e20-d1c24572cbbd | -3.87289 | -40.44138 | 2025-09-27 03:53:00 | NOAA-21 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| bc4f06ed-d8a2-39a9-83ec-1b001a30ca7d | -6.40677 | -43.31187 | 2025-09-27 03:53:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| facac882-4d1d-3503-8394-6ee559edf803 | -5.4799 | -43.07195 | 2025-09-27 03:53:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 61.8 |
| a19e4d6f-b36c-3a1a-9b29-559dc1af0d2c | -2.55165 | -48.40899 | 2025-09-27 03:53:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a65ba45e-193f-38d5-bd00-7180cf4a3e25 | -5.48616 | -43.08353 | 2025-09-27 03:53:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 68c9e657-7b85-3922-b8c1-1c1f0d33cc2d | -3.4459 | -44.12047 | 2025-09-27 03:53:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 153ebc06-b86d-35bf-9351-f3329042c061 | -3.92747 | -40.75397 | 2025-09-27 03:53:00 | NOAA-21 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 6ae43060-fbeb-3340-b848-9370e88a0b77 | -4.70625 | -40.62494 | 2025-09-27 03:53:00 | NOAA-21 | NOVA RUSSAS | CEARÁ | Brasil | 2309300 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2ed348ca-5790-3357-844e-34c98ae03313 | -3.66789 | -39.00357 | 2025-09-27 03:53:00 | NOAA-21 | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 395d1cbe-68bf-381d-9c47-157c4169bbf2 | -4.57671 | -44.08265 | 2025-09-27 03:53:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7a220067-c89f-30a3-8054-1295048276da | -5.47084 | -43.07748 | 2025-09-27 03:53:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 18.5 |
| e7aa3f0f-d013-3806-b3b0-f2da11ac8640 | -2.55241 | -48.40457 | 2025-09-27 03:53:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 13a4ef9e-367e-3f66-9274-53252a1a7fd4 | -4.76841 | -43.28363 | 2025-09-27 03:53:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d38d3443-9849-316f-b537-31785400deca | -6.81532 | -38.58053 | 2025-09-27 03:53:00 | NOAA-21 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 338ea3e7-eb79-3e51-b50e-b7903591421b | -6.33356 | -43.35796 | 2025-09-27 03:53:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aac52221-d206-3c17-b15d-e0c00e79c917 | -5.67501 | -44.84899 | 2025-09-27 03:53:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| bdde9ff4-f9c7-3656-a864-bf825ecc131b | -3.72896 | -39.65295 | 2025-09-27 03:53:00 | NOAA-21 | ITAPAJÉ | CEARÁ | Brasil | 2306306 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d586a8f5-514b-3aa9-8ae3-5b61944e9228 | -4.45852 | -38.3516 | 2025-09-27 03:53:00 | NOAA-21 | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| d8ecac8d-3e45-3485-9b65-664fa82a425d | -3.82717 | -40.99504 | 2025-09-27 03:53:00 | NOAA-21 | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a9b5b646-c5a8-3d47-b47d-80475f75db5f | -5.47207 | -36.66633 | 2025-09-27 03:53:00 | NOAA-21 | AFONSO BEZERRA | RIO GRANDE DO NORTE | Brasil | 2400307 | 24 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 0a1bca8c-63e4-38e1-8103-0d897a5d61df | -3.82642 | -40.34299 | 2025-09-27 03:53:00 | NOAA-21 | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 17e1232d-8422-3038-9c57-ad9e400f0fed | -5.47251 | -43.06728 | 2025-09-27 03:53:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 01d17765-efeb-3a26-be57-c871d17c6f61 | -6.25274 | -42.47702 | 2025-09-27 03:53:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2f5154a7-989c-318b-bd01-1056cb60b945 | -5.82574 | -41.29357 | 2025-09-27 03:53:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| d52b93da-151d-3976-93da-8a6f672ea41e | -5.5222 | -43.87749 | 2025-09-27 03:53:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1df99a5e-78c5-3a2d-bc37-9e9b873eac53 | -5.47481 | -43.07811 | 2025-09-27 03:53:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 23.5 |
| c478d607-f1e6-35d1-8a07-fd07994ca125 | -2.45172 | -49.02685 | 2025-09-27 03:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8c28667b-b9ef-34af-b65d-5b8016f69969 | -5.48387 | -43.07259 | 2025-09-27 03:53:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 9efd15a0-4691-31ed-87b1-2419d5589b92 | -6.42949 | -43.07714 | 2025-09-27 03:53:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| a34fb634-20f5-35d1-9144-9cda5781a483 | -4.00235 | -46.96593 | 2025-09-27 03:53:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b430ecad-5809-33c9-9bbb-7b8e0fcd4d87 | -5.79435 | -42.82621 | 2025-09-27 03:53:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 080b39e1-be21-3ab0-8150-1986ace440bd | -5.46743 | -43.07342 | 2025-09-27 03:53:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 19.8 |
| b8544e6e-ead5-3abe-aed6-5d425fd6a542 | -2.96075 | -48.59945 | 2025-09-27 03:53:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 63a69860-9a80-3889-879c-bdc82e4ccc5e | -6.27181 | -44.07223 | 2025-09-27 03:53:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 74bf94da-826f-3977-bffb-6a8aefa875b6 | -4.44121 | -40.97105 | 2025-09-27 03:53:00 | NOAA-21 | CROATÁ | CEARÁ | Brasil | 2304236 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 24f0593a-4d09-3fc1-bb2b-9f9e2e96d597 | -5.51317 | -43.88008 | 2025-09-27 03:53:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 0c7cdbd8-d470-32dc-bc16-7581e2c3ae07 | -6.27115 | -44.07618 | 2025-09-27 03:53:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 4fd49a30-eea3-33f7-a987-54e858b4d8ff | -5.76968 | -42.79976 | 2025-09-27 03:53:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 1b073fe5-44f9-3a05-a7a5-0efcc904e376 | -6.33697 | -43.36205 | 2025-09-27 03:53:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 046af741-ca50-31a1-9d89-6dd49048028f | -6.26406 | -43.91502 | 2025-09-27 03:53:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9bf1ff52-4570-33d0-ab75-92079f35efe6 | -6.33637 | -43.36555 | 2025-09-27 03:53:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b2a85124-92bc-31ce-a6e0-0a72d513d334 | -3.80496 | -41.57236 | 2025-09-27 03:53:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 9.2 |
| c0ec1265-c6fa-37f5-92df-b12ba684686a | -5.80049 | -42.8373 | 2025-09-27 03:53:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b440d59c-c42c-3935-a5fb-f8caae2f6038 | -5.79906 | -42.82187 | 2025-09-27 03:53:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| a2e3a5de-b9e6-3dd3-923a-a21bdb15cee3 | -7.15395 | -35.79722 | 2025-09-27 03:53:00 | NOAA-21 | LAGOA SECA | PARAÍBA | Brasil | 2508307 | 25 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 41870c58-d959-3418-a6ab-c0adb6335e5d | -5.48045 | -43.06858 | 2025-09-27 03:53:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 36.8 |
| 251e0791-a7cc-3075-9f91-63cf7887aadd | -4.26489 | -48.5554 | 2025-09-27 03:53:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5c4fa479-1840-3b99-b41a-708ae57213f6 | -5.07738 | -44.86059 | 2025-09-27 03:53:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 8713cb60-4027-3c09-9e3c-a8880c2ed85f | -5.08713 | -44.85761 | 2025-09-27 03:53:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a1949216-eb1e-30ba-b724-a80264e44908 | -5.51511 | -43.86857 | 2025-09-27 03:53:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| c37dbf2e-aa53-31c2-b236-8b6b26196126 | -4.00762 | -46.96699 | 2025-09-27 03:53:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 61d335e0-dba6-3fc2-84bc-9ff5e90a58ca | -4.70564 | -40.6288 | 2025-09-27 03:53:00 | NOAA-21 | NOVA RUSSAS | CEARÁ | Brasil | 2309300 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f1e060c5-157b-3d62-979d-f4c9dca38016 | -5.07658 | -44.86542 | 2025-09-27 03:53:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 7ce66566-d298-367e-abd5-0cac1b61af46 | -3.45029 | -44.1212 | 2025-09-27 03:53:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e5960021-f276-3355-b68c-6cead014614c | -5.72553 | -42.3026 | 2025-09-27 03:53:00 | NOAA-21 | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| b3a05351-aa76-3f6c-93af-ebd4e2f9e77f | -0.91209 | -47.5472 | 2025-09-27 03:53:00 | NOAA-21 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ed663cbc-c6ae-3f2c-9e9e-1a170d4943fc | -4.77614 | -41.05047 | 2025-09-27 03:53:00 | NOAA-21 | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| a80cc32f-ca35-37bf-b4bc-eb7687e89591 | -3.83053 | -40.33966 | 2025-09-27 03:53:00 | NOAA-21 | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1fe9377b-dd27-36cc-8c1f-ad656421c0d8 | -5.12005 | -42.685 | 2025-09-27 03:53:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| fc68ebd5-e1a9-3a78-872b-c6760f0b5840 | -3.9992 | -43.23375 | 2025-09-27 03:53:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9222539a-ada4-3c17-9e2e-27bfe8203c44 | -6.24635 | -44.0956 | 2025-09-27 03:53:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3b51aee8-96ec-39e9-a909-4e1b9edcbb3e | -5.49465 | -43.08146 | 2025-09-27 03:53:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 32.7 |
| d2f799d6-f091-3f64-b888-b8f8b5512f1f | -5.49125 | -43.07732 | 2025-09-27 03:53:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 3c02d93b-0b80-3650-8637-1dc52c2c6bc0 | -4.48217 | -47.67086 | 2025-09-27 03:53:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4150e773-ab7b-3ff6-b854-1c665203f5fa | -5.02337 | -37.04247 | 2025-09-27 03:53:00 | NOAA-21 | AREIA BRANCA | RIO GRANDE DO NORTE | Brasil | 2401107 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7ea128f3-4739-3fda-974b-e1122afadc60 | -4.05801 | -41.77837 | 2025-09-27 03:53:00 | NOAA-21 | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c1e6bc8c-3a27-3062-84fa-ea25cf071a98 | -5.49974 | -43.07523 | 2025-09-27 03:53:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 19.4 |
| a74a47c2-765e-3dd6-9bce-8639590ee06f | -6.19564 | -44.24082 | 2025-09-27 03:53:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 30861595-e60d-38a4-899d-ba5b904296b9 | -5.51672 | -43.88453 | 2025-09-27 03:53:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f8f4fad4-5318-318d-98ee-0c9e75e7217e | -3.59125 | -43.09707 | 2025-09-27 03:53:00 | NOAA-21 | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4dce268e-0ff8-3dcc-b3ab-bcdb1b3d1b27 | -4.57991 | -44.078 | 2025-09-27 03:53:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7adea4cf-5ae1-3038-93e2-44e807fef7d5 | -5.49521 | -43.07802 | 2025-09-27 03:53:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 20.2 |
| dcf1bd1f-8b68-36f8-bfa3-5d77f7b49295 | -3.82169 | -40.3502 | 2025-09-27 03:53:00 | NOAA-21 | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 4cb4afd7-039b-303f-902d-2fc11b4eb3fc | -4.97182 | -43.19219 | 2025-09-27 03:53:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c8d29299-cdf9-3118-bc26-45827092a66b | -3.82231 | -40.34631 | 2025-09-27 03:53:00 | NOAA-21 | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3b4b80ba-843a-3b10-9a26-62b573e0bc57 | -3.99647 | -46.96844 | 2025-09-27 03:53:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 85d171f1-b58d-3409-9483-c708d3a003a8 | -5.51028 | -43.87176 | 2025-09-27 03:53:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| b5a0a0a4-3f87-3722-8966-372bf6d05884 | -6.27058 | -42.48736 | 2025-09-27 03:53:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| f1fef434-519d-361b-8a49-1cbbf05a567b | -4.57869 | -44.07045 | 2025-09-27 03:53:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a238669b-baed-345c-9216-ee1597dc94ff | -5.48155 | -43.06184 | 2025-09-27 03:53:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7cc78e7b-aa69-322d-858d-07288013d981 | -5.92923 | -43.51928 | 2025-09-27 03:53:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c364d1f4-dd90-3e67-94dd-0567fa13c2e0 | -4.53668 | -48.64528 | 2025-09-27 03:53:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3ad1b416-d442-3f62-8ff6-580169f2d004 | -4.78573 | -45.34235 | 2025-09-27 03:53:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 0c6b50b5-f73f-3821-ab0e-6cdacf4af29b | -6.31371 | -43.39055 | 2025-09-27 03:53:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 91cf3cce-dda7-35c7-8544-342f40396832 | -5.37487 | -42.28501 | 2025-09-27 03:53:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d8c20e59-e99e-3e1e-9733-2a4d13a30216 | -5.70045 | -43.07759 | 2025-09-27 03:53:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e1ffee78-8874-37c7-85b0-58534fca7877 | -3.43045 | -39.04585 | 2025-09-27 03:53:00 | NOAA-21 | PARACURU | CEARÁ | Brasil | 2310209 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ad930336-8fb0-312d-a84c-56df9d33d1b2 | -6.13502 | -43.46477 | 2025-09-27 03:53:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2471391e-e4af-3196-ba83-04bfef8d5d5d | -5.46402 | -43.06937 | 2025-09-27 03:53:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 43f8108c-94e3-3e51-a714-6a1adc0c1005 | -5.47648 | -43.06793 | 2025-09-27 03:53:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 36.8 |
| b7eea8ee-80b1-3383-8169-601baa094d8c | -4.40143 | -44.08416 | 2025-09-27 03:53:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1a0c8c67-d499-3d79-815c-5b98ad7d2abf | -5.27952 | -45.03348 | 2025-09-27 03:53:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 251efa25-2258-3b5e-8161-7d756c4d39f1 | -5.76653 | -42.80156 | 2025-09-27 03:53:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 7f94ab77-7d0f-3f39-b7dd-e1d6bf386969 | -4.05744 | -38.43297 | 2025-09-27 03:53:00 | NOAA-21 | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2b7ee8dd-50a4-38b5-b712-178b43611168 | -6.31771 | -43.39122 | 2025-09-27 03:53:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5445c726-4c9b-34aa-bc9b-4ab49cdfa6c2 | -3.82784 | -40.9909 | 2025-09-27 03:53:00 | NOAA-21 | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4d6e7c48-e865-3c29-b9e6-7d7f517dbf1b | -5.4691 | -43.06325 | 2025-09-27 03:53:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 49eced97-132e-36ab-abbd-dd85d1dc0710 | -6.33542 | -43.35808 | 2025-09-27 03:53:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |


[Clique aqui para ver as próximas entradas](README15.md)

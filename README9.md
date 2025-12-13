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
| 9ab37bdd-df49-3b67-9868-450b625aaef1 | -2.59557 | -46.87251 | 2025-12-13 04:50:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6bab54fd-a8bc-3013-ac94-1563a88b26d0 | -0.69979 | -49.23393 | 2025-12-13 04:50:00 | NOAA-21 | SANTA CRUZ DO ARARI | PARÁ | Brasil | 1506401 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c7ee9f10-d685-379d-867f-0c3cd4b3cf0a | -2.10226 | -53.47865 | 2025-12-13 04:50:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fd43efc1-ba9e-379a-8bc9-c270c527d0f8 | -0.79412 | -48.63155 | 2025-12-13 04:50:00 | NOAA-21 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 237d9dbc-8b61-3846-9939-fa16bd5c779c | -2.41829 | -51.92251 | 2025-12-13 04:50:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fa3ce242-b1a4-3e40-a710-0d2a02fd124a | -3.2023 | -41.85811 | 2025-12-13 04:50:00 | NOAA-21 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 30.5 |
| d99dc118-63f8-3d1f-a019-c17917cf208a | -3.24345 | -47.25402 | 2025-12-13 04:50:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 81c4dcff-ffe0-362b-9028-c11395749954 | -3.19717 | -41.85337 | 2025-12-13 04:50:00 | NOAA-21 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 68115199-ee78-3f13-86fd-a632b6a7bd1f | -1.0322 | -53.7405 | 2025-12-13 04:50:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c0d8e8eb-d491-346a-a7eb-912d5939b214 | -2.66261 | -51.64462 | 2025-12-13 04:50:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5f9baaa2-7d71-33b6-9bc3-a92430e4b8ad | -3.44112 | -41.64675 | 2025-12-13 04:50:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 8301b490-dc84-38b4-8ef7-a756c3acd39a | -1.90931 | -45.47263 | 2025-12-13 04:50:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| f66bbed3-0adf-3438-97ab-398a61aa9b42 | -3.24026 | -47.24837 | 2025-12-13 04:50:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 17943eb6-2374-3fcb-b180-b8a3f401000d | -3.43476 | -41.64985 | 2025-12-13 04:50:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 5db279b6-7672-3a1a-ab55-7799c6f0c62f | -2.49875 | -51.79783 | 2025-12-13 04:50:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ef95cc84-f7b2-3f00-a7c6-18f525709187 | -3.20344 | -41.8503 | 2025-12-13 04:50:00 | NOAA-21 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 30.2 |
| a2f6b86f-2aec-345b-bd82-6d062ffaebf5 | -2.15166 | -53.76613 | 2025-12-13 04:50:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1332b569-06c3-3fc7-802f-a5b9ef3e1c9e | -3.23951 | -47.2534 | 2025-12-13 04:50:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| abe52712-6e29-3883-ab67-e587123f80ba | -2.58971 | -52.04484 | 2025-12-13 04:50:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f0c2a1d9-dabc-31af-8484-3eb05c602fad | -3.19661 | -41.85722 | 2025-12-13 04:50:00 | NOAA-21 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 46.5 |
| a66060c3-575b-3798-a2a9-3158aa61daee | -3.19775 | -41.84941 | 2025-12-13 04:50:00 | NOAA-21 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 5cac7867-1b04-3265-b25a-7219884c4f6c | -1.55183 | -53.14401 | 2025-12-13 04:50:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a00307bd-ff78-351e-9bba-9155f57067aa | -2.44479 | -46.90936 | 2025-12-13 04:50:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 31a9cf76-08f7-3e89-8728-7682b389d940 | -2.36345 | -51.94553 | 2025-12-13 04:50:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 056ecb88-ce02-3530-ac24-6cf2883b3613 | -2.36014 | -51.94501 | 2025-12-13 04:50:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d6c95613-c31b-358f-a484-567829c84573 | -3.02035 | -47.08902 | 2025-12-13 04:50:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9e106678-f2bf-3b01-8e7e-9d8c68456f25 | -2.48436 | -47.76922 | 2025-12-13 04:50:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7a257a52-f6d2-32ce-83da-8564f5ea323c | -3.52326 | -47.21199 | 2025-12-13 04:50:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 99cd7b9a-b65e-3b2d-9a11-1ba618b9afca | -2.43856 | -47.16178 | 2025-12-13 04:50:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 561a9747-9f17-3dc7-8166-5a1356b492ae | -3.47685 | -44.20881 | 2025-12-13 04:50:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| fc65c154-cf69-3884-ac0c-c3722b64300d | -2.70588 | -51.88691 | 2025-12-13 04:50:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3924f57d-d3a3-3a69-b68d-805eabdf9ebd | -2.70257 | -51.8864 | 2025-12-13 04:50:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e3a74dd5-bc72-3556-982a-dc3430629706 | -1.63407 | -55.58775 | 2025-12-13 04:50:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6c52f37c-c286-309b-9034-e331201d6489 | -2.4999 | -51.81208 | 2025-12-13 04:50:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8abc51d7-47e8-3f64-9fd8-9ecff925c78a | -2.50205 | -51.79834 | 2025-12-13 04:50:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a2271f6d-0bc6-3bc6-bdeb-45c560921fa1 | -3.44838 | -44.73286 | 2025-12-13 04:50:00 | NOAA-21 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 8509ddd1-9901-332a-bcff-c6e0c687806c | -1.84701 | -54.52431 | 2025-12-13 04:50:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b1f5b62f-dd3d-3440-bf00-407839865b2c | -2.48685 | -47.777 | 2025-12-13 04:50:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 2575aa88-fc2e-3afb-a15e-5c98f14a9ab8 | -1.63322 | -52.11279 | 2025-12-13 04:50:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| eda3c619-392b-3b56-ac3a-31491969a205 | -1.89385 | -45.42726 | 2025-12-13 04:50:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e4967dce-8405-3d5f-b407-8d6bfde0bb0c | -1.66445 | -54.57543 | 2025-12-13 04:50:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e2aedec7-2134-3503-906e-b669dc0c32f8 | -1.41817 | -52.56999 | 2025-12-13 04:50:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fc1db9a2-c4db-3a3c-9828-e27183ea55fc | -1.34955 | -55.39979 | 2025-12-13 04:50:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4d5ef4f0-eaa5-3cb6-a34c-870989b50d7f | -2.48746 | -47.77437 | 2025-12-13 04:50:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 14d709ac-705e-364b-9564-a224061c147f | -0.6992 | -49.23769 | 2025-12-13 04:50:00 | NOAA-21 | SANTA CRUZ DO ARARI | PARÁ | Brasil | 1506401 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2c61b265-723a-3a45-8db2-0068dbc5d86f | -1.18418 | -52.09136 | 2025-12-13 04:50:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c973cee3-6191-3358-8416-64627d633397 | -1.35027 | -55.39527 | 2025-12-13 04:50:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cebeb445-46ea-32ac-af94-b690153bf61a | -1.11529 | -53.15082 | 2025-12-13 04:50:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 553bcc77-a7c5-33f2-a260-50f3beb22505 | -2.48677 | -47.77898 | 2025-12-13 04:50:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9445eb1c-3500-328d-8297-5bf9b63417e2 | -2.09954 | -53.42957 | 2025-12-13 04:50:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1e28fc9f-e09b-3a72-a71a-202124c8a521 | -2.42874 | -51.92061 | 2025-12-13 04:50:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 59811f3a-4dd2-3a3b-a4e7-b55e55a64592 | -1.16945 | -53.7854 | 2025-12-13 04:50:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 540a0a23-2a6d-3d5f-b6ee-f6f48e2c173e | -2.67144 | -46.89808 | 2025-12-13 04:50:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2fcd801e-3a04-330b-ab36-7370d4ff9787 | -2.49821 | -51.80127 | 2025-12-13 04:50:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ebf937b8-fd0e-3c19-8bdd-8b5784a3f691 | -2.49767 | -51.8047 | 2025-12-13 04:50:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 128ba827-8ab8-378b-a9db-50ce37529539 | -1.82588 | -45.7133 | 2025-12-13 04:50:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fe82e00d-1656-3ba9-9cbb-fb0a61bda5a8 | -3.1915 | -41.85241 | 2025-12-13 04:50:00 | NOAA-21 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 95a5beef-8304-31d8-a1af-dfa35e8a4b14 | -1.42928 | -53.47282 | 2025-12-13 04:50:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c341ed71-bb31-3668-b9e1-7fd743fb4bbd | -1.281 | -53.16496 | 2025-12-13 04:50:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8405f2ae-4a0d-37e7-8c40-530c3b280eb0 | -2.01299 | -46.37897 | 2025-12-13 04:50:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e768bcf1-e261-333b-a9b0-887923d5e771 | -1.90496 | -45.47195 | 2025-12-13 04:50:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 190987f9-495c-3467-88e0-e57b393f0bd6 | -2.86817 | -45.44635 | 2025-12-13 04:50:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8ee08ed4-fdb7-3cc6-be43-c134c398c563 | -2.18201 | -46.09703 | 2025-12-13 04:50:00 | NOAA-21 | MARACAÇUMÉ | MARANHÃO | Brasil | 2106326 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 13ca437a-1522-3266-9c73-979a8eccfeb8 | -2.11066 | -51.431 | 2025-12-13 04:50:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a0eebacc-8a55-33c2-b149-793841fc9443 | -2.3611 | -53.70704 | 2025-12-13 04:50:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 393fd98b-6ea3-3981-925d-61f09191d209 | -0.79766 | -48.6321 | 2025-12-13 04:50:00 | NOAA-21 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0f0ae0d8-bc6f-3218-8414-333acc563abd | -2.8726 | -45.44704 | 2025-12-13 04:50:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e4526919-fdc4-3263-9472-3570aa8b0ee7 | -1.42811 | -53.4802 | 2025-12-13 04:50:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 72b284e8-cf8a-35dc-9391-5194fbe6eb23 | -3.47763 | -44.20344 | 2025-12-13 04:50:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c18e0b8c-bfb9-3ed2-a4b0-8daef59d9ae2 | -1.57938 | -54.12738 | 2025-12-13 04:50:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 36cd0c7f-4556-3027-b662-fcc2bc1ceaa2 | -2.65877 | -51.64754 | 2025-12-13 04:50:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6a8a815d-b2e1-3e79-8001-cd90797318ef | -2.48368 | -47.77381 | 2025-12-13 04:50:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 31a1fcc2-e1de-3537-a16d-bfd7d191174f | -2.50098 | -51.80521 | 2025-12-13 04:50:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 51180d5a-96f6-3777-b759-d614da8d2a3c | -3.20286 | -41.85426 | 2025-12-13 04:50:00 | NOAA-21 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 30.2 |
| bbdb4b49-9ee6-30d2-b1be-c99a137d4028 | -1.7249 | -47.15562 | 2025-12-13 04:50:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 45c13da4-0025-358d-86ea-09067fb7a6c5 | -1.89822 | -45.42794 | 2025-12-13 04:50:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8c6fe5ad-5c96-303d-b232-90c022eba238 | -1.90559 | -45.46775 | 2025-12-13 04:50:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f2940eaa-ca11-31a6-ae9d-882799a6b4b9 | -2.43204 | -51.92112 | 2025-12-13 04:50:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ce50bbc7-205a-3160-888f-248ea13eeaa8 | -1.49353 | -53.13129 | 2025-12-13 04:50:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ec6dd84f-0904-39e0-a065-807d493b435e | -2.78518 | -45.78188 | 2025-12-13 04:50:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4b11a073-47b0-3d0a-8834-f098ecbe89b4 | -1.88245 | -54.68749 | 2025-12-13 04:50:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 93b08d3c-3f20-30ff-9212-b16e25574977 | -2.42105 | -51.92646 | 2025-12-13 04:50:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f7ae4945-7f2b-31c6-be2f-52cc3b844887 | -1.99017 | -52.07008 | 2025-12-13 04:50:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e7cd7896-4975-351d-ac60-9e5223bc4478 | -2.50151 | -51.80178 | 2025-12-13 04:50:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6306c150-eedc-3166-9741-f05b751f545b | -1.11145 | -53.68722 | 2025-12-13 04:50:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bad2f359-fdf8-3452-9941-44cae1eb983e | -2.41837 | -45.05747 | 2025-12-13 04:50:00 | NOAA-21 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 23f17061-d8b3-305a-966b-62cd8c780b31 | -3.37635 | -45.48527 | 2025-12-13 04:50:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a9042c92-3129-33ab-a11d-8db95ccd435f | -2.42382 | -51.9304 | 2025-12-13 04:50:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bb4d9e09-b929-3d7a-85f2-bd2d154e226d | -1.49015 | -53.13077 | 2025-12-13 04:50:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 451d9e51-28be-3fd9-9c4f-e11c3ecfc48c | -3.20858 | -41.85489 | 2025-12-13 04:50:00 | NOAA-21 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 30.2 |
| 1ec1acfc-46f0-3433-8fcf-3d91760260aa | -2.4165 | -44.03747 | 2025-12-13 04:50:00 | NOAA-21 | RAPOSA | MARANHÃO | Brasil | 2109452 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d611d661-bb19-3d14-adf2-7eca13167dad | -3.51927 | -47.21146 | 2025-12-13 04:50:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4737a445-1d7c-39cd-bd5a-a8d361e1c3ad | -2.01243 | -46.38263 | 2025-12-13 04:50:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b49f6ff1-995b-36a6-b35b-0e984be15a1f | -2.4315 | -51.92456 | 2025-12-13 04:50:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f84dbf23-f594-3332-b8ae-5499a177eeea | -2.78454 | -45.786 | 2025-12-13 04:50:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5dcd285f-ef10-328e-9916-b6a52f4458ef | -1.71221 | -47.02556 | 2025-12-13 04:50:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6defaa33-e81f-3a04-9287-2f7aad0f24ad | -2.48815 | -47.76978 | 2025-12-13 04:50:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| d3d2c2d4-a95c-383f-b9b0-cbb44358f63f | -1.11432 | -53.69155 | 2025-12-13 04:50:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ef295c7d-44b6-3e8f-8678-42bbf8f9cbe5 | -1.03282 | -53.73664 | 2025-12-13 04:50:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3e4649b0-17ac-3d04-ae4c-82b31def7f58 | -2.67197 | -46.89456 | 2025-12-13 04:50:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |


[Clique aqui para ver as próximas entradas](README10.md)

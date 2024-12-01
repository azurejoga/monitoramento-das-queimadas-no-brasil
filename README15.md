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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6cc1c566-04d6-3ddb-9200-5176b16d25c1 | -2.6578 | -51.8811 | 2024-12-01 01:00:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 7ced4aa2-a1a9-3129-99ce-3b77342589ed | -4.5563 | -43.2795 | 2024-12-01 01:00:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 97.4 |
| d238ba3b-3739-3679-814b-2c6e9dadd5a4 | -6.9158 | -43.5185 | 2024-12-01 01:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 105.9 |
| c2151e2e-32da-3741-90ef-b9f7b6fc5d07 | -3.1456 | -54.5259 | 2024-12-01 01:00:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 74.1 |
| f8978962-3cf8-3bc7-ba3f-286e14d7cebc | -3.69 | -51.8101 | 2024-12-01 01:00:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 86.0 |
| 3dd52ff2-2983-3b1f-8421-dd2bb2a2bf4b | -3.2774 | -53.6383 | 2024-12-01 01:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 112.2 |
| 80cd4c86-8dff-3888-9d86-dc24bf2ed58f | -4.5562 | -43.3028 | 2024-12-01 01:00:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 258.7 |
| 11045b9e-eec4-3669-866c-4ef53875a5a0 | -3.2057 | -53.1341 | 2024-12-01 01:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 4e665e8b-155e-3d95-8210-b8035d1bccde | -6.9153 | -43.5652 | 2024-12-01 01:00:00 | GOES-16 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 0db83b8f-b68f-38d5-8a80-a10e799d3150 | -2.8197 | -53.0425 | 2024-12-01 01:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 7398f607-4f6e-330f-b4e4-c6eb05db518e | -3.5158 | -53.8333 | 2024-12-01 01:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 104.4 |
| c5d37e36-e32a-3f88-bfe2-7655630d6760 | -4.556 | -43.3261 | 2024-12-01 01:00:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 76.4 |
| bf3b0a69-ef08-3a73-923e-91f1329b2be4 | -3.1273 | -54.5264 | 2024-12-01 01:00:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 84.9 |
| 4f9c452d-ee86-3ca5-8253-2f18f17a3e55 | -3.2058 | -53.1138 | 2024-12-01 01:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 1e5eddd3-442a-33bd-87ce-1f67081add37 | -3.4755 | -50.2566 | 2024-12-01 01:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 95.3 |
| 834bd84f-5f02-3d16-b979-cbf0d0fdacd5 | -6.9341 | -43.5634 | 2024-12-01 01:00:00 | GOES-16 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 91.5 |
| d91eadc9-eebc-3f5b-8512-330c02e80844 | -4.5392 | -45.7243 | 2024-12-01 01:00:00 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 64aa6259-5a46-3d95-8633-b3efa85ae167 | -6.9344 | -43.5401 | 2024-12-01 01:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 321.0 |
| 0049b75e-1889-3b24-a6e5-79def433f818 | -3.2591 | -53.6186 | 2024-12-01 01:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 99.4 |
| 019a6fe1-f1d8-34ef-84e0-86ca696ab77e | -4.5394 | -45.7019 | 2024-12-01 01:00:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 139.4 |
| e2a9b736-8efa-35b5-9ee0-7686d68f69c6 | -4.5395 | -45.6794 | 2024-12-01 01:00:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 61.7 |
| ca0b18b8-3eef-370f-9b07-786a98895070 | -6.9346 | -43.5168 | 2024-12-01 01:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 78.6 |
| a9e6c04d-e465-3491-ad05-cbd1ba2917cf | -2.6579 | -51.8606 | 2024-12-01 01:00:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| c58d6376-b939-34d3-b329-bd925bce8ae2 | -2.8196 | -53.0629 | 2024-12-01 01:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| b36c4261-5757-3ae2-8159-7844fd4d45a0 | -3.259 | -53.6388 | 2024-12-01 01:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 143.8 |
| 27fc1ed5-b346-3b71-adde-a9e2379b77d2 | -6.93 | -43.56 | 2024-12-01 01:00:00 | MSG-03 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 0f476447-3232-3051-b766-5e9932e0fa94 | -4.55 | -45.7 | 2024-12-01 01:00:00 | MSG-03 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5c8977a7-8a48-390b-8705-89b3cf02ecb8 | -4.56 | -43.28 | 2024-12-01 01:00:00 | MSG-03 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ebd2841b-94a4-3d69-b2d6-cb20863206ae | -6.92 | -43.52 | 2024-12-01 01:00:00 | MSG-03 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d1e28f57-8889-3842-b2d3-e6290bafda1d | -3.4974 | -53.8339 | 2024-12-01 01:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 147.9 |
| 7712e14a-8405-3394-bc2f-4a36a5073075 | -4.5394 | -45.7019 | 2024-12-01 01:10:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 151.7 |
| 104a1931-bb05-3fc8-bd8d-2af17b583573 | -3.1273 | -54.5264 | 2024-12-01 01:10:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 86.7 |
| e6a56060-8af2-397e-9c96-0d161f688a23 | -1.7139 | -46.1422 | 2024-12-01 01:10:00 | GOES-16 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 88.5 |
| b9e43d49-d2ca-35ad-919e-e51a0726eee6 | -3.5158 | -53.8333 | 2024-12-01 01:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 59704c09-9726-3fd4-b934-7b5a8d5631c6 | -2.8491 | -49.8763 | 2024-12-01 01:10:00 | GOES-16 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| c1cc1811-56d4-39d4-ab60-b18b8c496ce6 | -3.0081 | -51.7897 | 2024-12-01 01:10:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 0ff97788-9aee-3fda-a600-158bd46369a1 | -4.5562 | -43.3028 | 2024-12-01 01:10:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 271.2 |
| df1aa12f-fd75-30ec-9171-0304f0f62644 | -10.6674 | -44.4835 | 2024-12-01 01:10:00 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 129f2449-aa42-3bd6-97a2-c37fcf3ba05a | -6.9156 | -43.5418 | 2024-12-01 01:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 218.5 |
| 170f9e2b-5580-38cc-bdd2-6a49f7d08abf | -4.8899 | -41.3143 | 2024-12-01 01:10:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 76.3 |
| e5a67d0d-1a61-3936-b63b-626400ae2f54 | -4.5578 | -45.7232 | 2024-12-01 01:10:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 141.4 |
| fd4dcbee-37e0-318f-93da-dcdd2aee4602 | -2.8197 | -53.0425 | 2024-12-01 01:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| b5a4d3bf-42a8-33fe-935b-d98df8108b35 | -2.6578 | -51.8811 | 2024-12-01 01:10:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 96.3 |
| 5d3232b9-9380-3fac-b125-ecda281f592f | -2.6579 | -51.8606 | 2024-12-01 01:10:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 0b6eca68-c3a6-390f-8f3f-3dd4f50e32ad | -3.0169 | -45.1426 | 2024-12-01 01:10:00 | GOES-16 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 6ebbc2dd-a78f-3298-b3b0-f550c83cae91 | -3.2591 | -53.6186 | 2024-12-01 01:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 101.4 |
| 0a3a486f-68b6-3b7c-8ce0-0d2535e953d3 | -4.5563 | -43.2795 | 2024-12-01 01:10:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 69dc5a81-5ed6-31e0-ad3a-11bf4a81426d | -4.558 | -45.7008 | 2024-12-01 01:10:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 69a5c95e-246a-35d0-8e60-f2a4ffe67c65 | -1.7139 | -46.1644 | 2024-12-01 01:10:00 | GOES-16 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 59.9 |
| de365055-bc07-39d8-8efe-16c83f1a692c | -3.2774 | -53.6383 | 2024-12-01 01:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 91.3 |
| 8a283c3f-1c80-352c-aa7a-60b85e6604d7 | -6.9346 | -43.5168 | 2024-12-01 01:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 0f4015b7-3510-3a6f-8f2a-39956bedfeb8 | -4.5765 | -45.7222 | 2024-12-01 01:10:00 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 49888d97-0a61-3e5f-9e3c-414e7aecf5a9 | -3.3134 | -53.8592 | 2024-12-01 01:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 665b307a-421e-3bc6-985f-845c695a0a6a | -3.4754 | -50.2776 | 2024-12-01 01:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 113.2 |
| 3ae359bd-6fad-3224-bb10-df0850a03da2 | -2.7503 | -51.7553 | 2024-12-01 01:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 91.4 |
| 41c876ad-0fd3-3c77-bf5c-fb1586f784fb | -2.8013 | -53.043 | 2024-12-01 01:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 32a859cf-27cb-375d-88b9-69d5fa5487c8 | -1.6954 | -46.1426 | 2024-12-01 01:10:00 | GOES-16 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 97.8 |
| 7882fa27-f91a-3fe9-aa74-104faa00451f | -6.9344 | -43.5401 | 2024-12-01 01:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 301.4 |
| 47eb597f-6517-39e2-9a8c-40c9cdcea0f9 | -4.556 | -43.3261 | 2024-12-01 01:10:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 8428abe9-0276-37bf-8edf-070bedaaa8fb | -2.103 | -46.2443 | 2024-12-01 01:10:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 17b220cd-0e46-37cd-91f3-fae1f273ec26 | -1.6953 | -46.1648 | 2024-12-01 01:10:00 | GOES-16 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 05d6a960-a440-351e-847c-f5ff20475514 | -3.259 | -53.6388 | 2024-12-01 01:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 156.5 |
| 13ecfeec-b2f5-3733-9281-0f0e3cbb6e63 | -4.5392 | -45.7243 | 2024-12-01 01:10:00 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 86.6 |
| bb9a15b4-fc0e-33b5-a517-3967db2daf46 | -3.4755 | -50.2566 | 2024-12-01 01:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 788b7ed2-421e-397e-b17f-87f843426b13 | -3.69 | -51.8101 | 2024-12-01 01:10:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| e3a680c2-3814-32fc-8224-b8165e4dfdce | -6.9153 | -43.5652 | 2024-12-01 01:10:00 | GOES-16 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 78.1 |
| b192af7f-269d-30d0-b482-d6969c4dbc1c | -2.1215 | -46.2439 | 2024-12-01 01:10:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 8056653e-9b31-3923-8916-a747c6d6b072 | -3.1456 | -54.5259 | 2024-12-01 01:10:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 6f976d91-ed07-3730-b1ed-f03b05a7c57c | -6.9341 | -43.5634 | 2024-12-01 01:10:00 | GOES-16 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 110.2 |
| e3623aa1-62d1-3143-9d46-8963ba81f484 | -19.084 | -57.698799 | 2024-12-01 01:16:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| b3fba8a9-0edd-3d4f-921a-63bed10299db | -19.085699 | -57.706299 | 2024-12-01 01:16:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| d1d98542-7e1f-35c3-a079-a62510029b8a | -3.6797 | -51.7841 | 2024-12-01 01:18:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8210a5b3-02a3-308d-898d-72e0c086317f | 1.172 | -55.969002 | 2024-12-01 01:18:00 | METOP-B | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3de25761-9765-3bea-881f-91e46f8f8419 | -3.0059 | -51.778099 | 2024-12-01 01:18:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 23af2b09-7128-3dab-9378-2c552f5e60b9 | -3.2411 | -53.615398 | 2024-12-01 01:18:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1d364e5d-c76c-3b67-b677-4c6e9e7d4e21 | -3.0605 | -53.802799 | 2024-12-01 01:18:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fc5abb48-7db5-36c5-8935-a8ad50ba6e67 | -2.7458 | -51.754601 | 2024-12-01 01:18:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| be7b2d5b-1540-322d-bf2f-0293abf5d021 | -3.8085 | -52.231899 | 2024-12-01 01:18:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ecd2b9d2-ea43-3312-9108-739de4c69dbd | -3.52 | -62.7425 | 2024-12-01 01:18:00 | METOP-B | CODAJÁS | AMAZONAS | Brasil | 1301308 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c2d453b7-988b-376f-bc04-68907dc19183 | -2.7296 | -51.729599 | 2024-12-01 01:18:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a99a3671-fb77-3de8-a2cf-9ae8e9a5d02d | -3.2555 | -53.6329 | 2024-12-01 01:18:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 48655b75-bef8-35a7-8be4-11c60dd51901 | -3.1235 | -54.501499 | 2024-12-01 01:18:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 798c4c4c-04b1-3150-b771-c5a4a3f0f272 | -3.246 | -53.593201 | 2024-12-01 01:18:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 950a14df-c29f-3896-91b8-fc46e3b21b14 | -3.2604 | -53.610802 | 2024-12-01 01:18:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 88083a94-6ba7-3928-a41a-18320db44607 | -3.3334 | -53.359001 | 2024-12-01 01:18:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b1f26051-f9ca-3d75-be97-38d3d9c11166 | -3.2651 | -53.6306 | 2024-12-01 01:18:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 970ce5e8-4e38-3f9c-9ced-c63e0c7fedb9 | -3.1135 | -53.810699 | 2024-12-01 01:18:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 67c82279-ba35-30ad-bc8d-cd6a47b86802 | -2.7361 | -51.756901 | 2024-12-01 01:18:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c681d7cb-1d13-3540-9c3b-70546fe53567 | -3.5215 | -62.749298 | 2024-12-01 01:18:00 | METOP-B | CODAJÁS | AMAZONAS | Brasil | 1301308 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a19e985a-e2b5-30d3-964d-57a003f4ed5d | -0.1865 | -60.668201 | 2024-12-01 01:18:00 | METOP-B | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 3d08784a-4f57-3cf7-90bb-114b2de289b6 | 2.7368 | -60.3862 | 2024-12-01 01:18:00 | METOP-B | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| eb1bdc32-851d-3a5f-9e68-a0111d6de946 | -3.2004 | -53.101299 | 2024-12-01 01:18:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0d67b53d-322b-3e1e-9bcc-161747ef2872 | -3.1219 | -54.5382 | 2024-12-01 01:18:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 731a1d05-abe0-3430-a243-c150bd097825 | -3.5102 | -62.744701 | 2024-12-01 01:18:00 | METOP-B | CODAJÁS | AMAZONAS | Brasil | 1301308 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e2dba34a-d795-3aa1-8baa-ea7cdb6d3ff0 | -3.3106 | -53.8652 | 2024-12-01 01:18:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3481d0df-1283-3cd2-9377-d6f2e2825c2c | -1.0654 | -62.642399 | 2024-12-01 01:18:00 | METOP-B | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bc25537d-9102-3b50-9798-459f913e1bcb | -3.2055 | -53.122799 | 2024-12-01 01:18:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f624c88b-7d74-3f76-a4f3-da8872a7a8ea | -3.4851 | -53.824001 | 2024-12-01 01:18:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3350e32e-7786-3b39-a38e-a634ef5270bb | -3.2458 | -53.635201 | 2024-12-01 01:18:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cd892358-f261-3323-8f68-cb8d9655b88d | -3.4948 | -53.821701 | 2024-12-01 01:18:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README16.md)

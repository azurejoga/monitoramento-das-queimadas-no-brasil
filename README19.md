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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d4c200a8-af84-3f9d-8408-15dee999c769 | -1.22346 | -53.68502 | 2024-11-24 00:49:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| e67c5624-9b6a-3abd-960b-2035c75ef568 | -2.45776 | -49.08403 | 2024-11-24 00:49:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 33.6 |
| 456fca72-14e2-3a7a-96e1-4510ecb68ae9 | -2.64218 | -46.24171 | 2024-11-24 00:49:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a740542c-fddd-381c-b1b3-5a8935d382c2 | -3.30458 | -50.03594 | 2024-11-24 00:49:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 373aa7b1-d320-3b59-a581-7a068e85f9f5 | -2.21601 | -49.86595 | 2024-11-24 00:49:00 | TERRA_M-M | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 67e4be8e-d7e1-361a-b93f-de053ec9af22 | -2.4163 | -48.98248 | 2024-11-24 00:49:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 86832f45-bb47-359b-94fd-29cf97a181c5 | -3.47118 | -51.99166 | 2024-11-24 00:49:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 19.8 |
| fa9ac385-9eef-339e-82de-385fe0cdf7c2 | -3.93869 | -48.141 | 2024-11-24 00:49:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| eba05ccb-6890-362e-a448-ab1224ee0c22 | -3.85967 | -50.06215 | 2024-11-24 00:49:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 1dd95764-f271-3e0f-8594-48cd60e656b9 | -3.80786 | -51.34011 | 2024-11-24 00:49:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 89ed42b2-d872-3a56-8a28-997544b7d5ac | 0.4068 | -50.86325 | 2024-11-24 00:49:00 | TERRA_M-M | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 413cd056-848e-3552-bdae-f18ec12dac6d | -3.25769 | -53.27443 | 2024-11-24 00:49:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| f6f46f7d-2e7f-3ef8-9c87-368aa8c72288 | -4.31579 | -43.20323 | 2024-11-24 00:49:00 | TERRA_M-M | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 9b7755bd-aa50-32d4-aeeb-1662042cc090 | -4.24777 | -48.71174 | 2024-11-24 00:49:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 3d0fbe60-12a0-3535-9364-84c77d3a2b6e | -4.23741 | -48.70367 | 2024-11-24 00:49:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 136.9 |
| b275dfb7-6ca6-33c0-9ff3-f9d03a49d2e9 | -3.24571 | -50.66487 | 2024-11-24 00:49:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 23.3 |
| bab69d1e-8cbc-312b-8833-59b462611eaa | -2.8627 | -51.81749 | 2024-11-24 00:49:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 126.9 |
| cc430398-31e6-3b14-80b9-3ca992698fd9 | -2.25314 | -49.00224 | 2024-11-24 00:49:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 9bdba067-ed46-359d-9fa6-0fe413b758c7 | -4.08538 | -46.1545 | 2024-11-24 00:49:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 22db14f4-9b68-31be-9962-59f3d2fe5962 | -4.56434 | -48.53542 | 2024-11-24 00:49:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| d1429a5c-d036-382c-803a-90601e616042 | -3.86259 | -47.06259 | 2024-11-24 00:49:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 635d35e6-0457-380b-b33e-513b4c503b37 | -3.26762 | -53.82453 | 2024-11-24 00:49:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 33.6 |
| dd7fbb8d-4fae-33a7-8daa-7836371fdeac | -1.47182 | -46.04646 | 2024-11-24 00:49:00 | TERRA_M-M | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 41.8 |
| 742c2338-47a0-35cd-9746-d45c5d4c0ce5 | -2.50298 | -46.10494 | 2024-11-24 00:49:00 | TERRA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 222a6093-d5e3-3092-8e82-01dec09cc72e | -2.56708 | -46.55883 | 2024-11-24 00:49:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 32f5e2cc-1eb1-3011-9b5f-8cc86be7dd72 | -4.23888 | -48.64676 | 2024-11-24 00:49:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| ecb33c16-517e-39ba-856b-7ed7308cec3b | -4.69712 | -45.85431 | 2024-11-24 00:49:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 248408c7-a514-30e6-916c-7c49cf3ee1e6 | -3.39197 | -50.31635 | 2024-11-24 00:49:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 18.2 |
| c1388022-afae-39ba-b4cc-8a2474207216 | -3.50399 | -50.46228 | 2024-11-24 00:49:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 26c106cc-3747-3211-bd84-46625c615dac | -3.21707 | -53.93232 | 2024-11-24 00:49:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 83afb6dd-58a2-33ab-9124-970e5ef2797e | -4.89297 | -48.91275 | 2024-11-24 00:49:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ec7f00b9-4b2b-3f9e-9019-f500dcb726d4 | -0.28505 | -51.49439 | 2024-11-24 00:49:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 39bd08e0-229c-373a-b816-aa35fbbc3520 | -2.69286 | -46.27556 | 2024-11-24 00:49:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 27.8 |
| 7ec2ab49-e8af-37fc-9ca4-9c6d50c321a5 | -3.04598 | -45.52262 | 2024-11-24 00:49:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ec9ad8c7-0789-3ec3-bcb4-efc4111ac544 | -2.44996 | -49.09459 | 2024-11-24 00:49:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 2e4afc98-a6dd-3bb5-8062-299ebc7698ff | -3.70503 | -47.1242 | 2024-11-24 00:49:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 3076ab29-3c42-3fa9-9059-bfe0b40286df | -1.45346 | -53.39917 | 2024-11-24 00:49:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 22.9 |
| f5521771-7a16-3756-addb-2850e15c622e | -1.23041 | -51.74431 | 2024-11-24 00:49:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 5a885796-561a-3e75-88fc-5e3fec990704 | -0.33208 | -51.54114 | 2024-11-24 00:49:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 33.1 |
| 373d0961-3a5f-3dbc-978f-04749e7c83a2 | -1.83316 | -46.64644 | 2024-11-24 00:49:00 | TERRA_M-M | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 5f821a44-fd94-31e2-9ecb-04dafe1791a1 | -4.0851 | -50.37376 | 2024-11-24 00:49:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| c20451c4-7904-3e49-a601-7f57dc880a3c | -3.02744 | -45.12366 | 2024-11-24 00:49:00 | TERRA_M-M | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 24.6 |
| 16762c5d-49f3-33c1-b023-815709352ded | -4.63769 | -46.87029 | 2024-11-24 00:49:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 57a583cf-5013-3c71-bff3-47327c97a157 | -1.57087 | -52.01348 | 2024-11-24 00:49:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 16df18e0-6e1b-3403-b55a-f77bc1934ccf | -3.66506 | -51.72131 | 2024-11-24 00:49:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| e57a7d11-e034-375f-a085-e87503a053c5 | -3.1934 | -46.55684 | 2024-11-24 00:49:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 5bb34606-7259-301a-a4f4-003d4c63805e | -2.60984 | -48.2494 | 2024-11-24 00:49:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 98664c82-0b83-3ca1-9b22-716e0688eadc | -4.62058 | -46.61891 | 2024-11-24 00:49:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 43ef6698-0285-3ba7-987e-21684e034ec5 | -2.80333 | -46.79885 | 2024-11-24 00:49:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| dc79fa60-3b4e-3ed7-8997-016948fff728 | -4.26482 | -49.83164 | 2024-11-24 00:49:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1db09c15-76ca-34e5-ac5b-f420967ae3bb | -4.36604 | -48.56619 | 2024-11-24 00:49:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| b1e4819c-24fe-366a-bee5-862fc6b772d3 | -1.11705 | -53.39491 | 2024-11-24 00:49:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 35.1 |
| 410234ce-5e26-35d2-9cf3-33c46d31dfb7 | -2.48009 | -48.84601 | 2024-11-24 00:49:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| c6db6205-3d9c-3575-8158-d4ed0eae7512 | -4.62213 | -46.04105 | 2024-11-24 00:49:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 7.4 |
| d5e8f4f1-24ca-3d38-92b8-93d35ee62fcd | -3.24513 | -54.22424 | 2024-11-24 00:49:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 37.6 |
| 559f45d9-3cfa-3822-a32d-a5784cf9656d | -1.14421 | -47.71108 | 2024-11-24 00:49:00 | TERRA_M-M | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ef205751-cebf-3929-978a-3145662ed198 | -4.10862 | -49.50521 | 2024-11-24 00:49:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 3ae690e0-c9a5-3083-9ce3-c517b060e269 | -3.6448 | -52.2504 | 2024-11-24 00:49:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 22696d6c-78ab-3176-8df2-da1e31ece29b | -3.84801 | -50.43589 | 2024-11-24 00:49:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 5b459a87-8359-37f7-bd51-73a978c6d423 | -4.23744 | -44.63786 | 2024-11-24 00:49:00 | TERRA_M-M | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 2c6cce78-60b3-347f-8937-c8559bfb3dcd | -4.63027 | -49.67215 | 2024-11-24 00:49:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| f59b82f9-4e4a-3e19-95b7-0ea5b8959668 | -3.95172 | -45.99114 | 2024-11-24 00:49:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 42.7 |
| 72d059b3-d05e-3933-a782-ef4e482297db | -2.41627 | -49.11466 | 2024-11-24 00:49:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 42ef301d-e8c3-3ed2-a3e1-c1f625cc09cb | -1.81446 | -46.64607 | 2024-11-24 00:49:00 | TERRA_M-M | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 7d969874-a1e3-321a-be15-ba38ae74c55c | -1.95826 | -49.53641 | 2024-11-24 00:49:00 | TERRA_M-M | LIMOEIRO DO AJURU | PARÁ | Brasil | 1504000 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| ca14cf7f-7236-38ee-ae83-cbb5a375926b | -2.276 | -47.97787 | 2024-11-24 00:49:00 | TERRA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 18727a11-904a-30b3-90dd-85b9270b1ba7 | -1.5288 | -51.62752 | 2024-11-24 00:49:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 19.7 |
| 07565529-7dbd-3f59-a281-a116e10f3396 | -4.69861 | -47.17714 | 2024-11-24 00:49:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 8483c927-745b-3d35-99ca-dc14171a2a4e | -3.66689 | -51.73483 | 2024-11-24 00:49:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| e67f7673-e58c-3749-a679-9ddc5f32f970 | -2.62916 | -46.21507 | 2024-11-24 00:49:00 | TERRA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 200505ac-e1be-3e92-9124-c68a4e6a5086 | -2.5251 | -45.40972 | 2024-11-24 00:49:00 | TERRA_M-M | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 40.2 |
| ba0394e5-a90d-34d3-9950-5cbbbe72e01f | -4.22777 | -44.63926 | 2024-11-24 00:49:00 | TERRA_M-M | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| d7c33ca2-5717-364b-985d-32ecbee5eeaa | -2.5994 | -46.2668 | 2024-11-24 00:49:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 10.9 |
| d786c65e-7122-3402-a168-2d6f8ae45b5d | -0.19548 | -51.65691 | 2024-11-24 00:49:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 7bf12510-0b47-3e0d-9133-a3ce36113416 | -2.74825 | -49.1201 | 2024-11-24 00:49:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 198.2 |
| 98b85634-81c4-32f5-bfa8-ac3554dcddb5 | -3.54812 | -52.04691 | 2024-11-24 00:49:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 00c1c9f5-be4e-3cf3-80f4-64e911706cb0 | -1.4612 | -46.03812 | 2024-11-24 00:49:00 | TERRA_M-M | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 20.2 |
| 435490d9-3b10-3eee-ae06-d996f685cd87 | -4.36731 | -48.57537 | 2024-11-24 00:49:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| b2beb796-7fff-388e-9114-d8cf00a3ee6b | -2.66553 | -46.1431 | 2024-11-24 00:49:00 | TERRA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 10.6 |
| dc435707-3380-3198-bfeb-2d7eccd94b13 | -3.67985 | -50.11577 | 2024-11-24 00:49:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b2c2139f-c837-3c17-acab-b999b5484685 | -2.70969 | -46.2637 | 2024-11-24 00:49:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 22.2 |
| ea97d4d7-cb88-314a-aba2-6f8123e48169 | -4.18477 | -45.622 | 2024-11-24 00:49:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 11.2 |
| b6653a95-09de-3c7e-9161-126008c1d464 | -0.8907 | -52.7685 | 2024-11-24 00:50:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 128.7 |
| 4f881245-89ff-3b82-9ea9-ca029647b5a0 | -4.2419 | -48.7193 | 2024-11-24 00:50:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 42720a2d-620c-3312-9c8f-a953b6f48f7d | -2.7411 | -49.1162 | 2024-11-24 00:50:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 108.9 |
| cf99478c-eee5-3ebe-86a3-a7486da49568 | -3.2569 | -54.2226 | 2024-11-24 00:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| efd559f9-d361-372a-b582-e7ec1997655f | -3.2386 | -54.223 | 2024-11-24 00:50:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 544cf7e5-0ae6-3c67-af62-b370d241bb61 | -3.1068 | -45.7903 | 2024-11-24 00:50:00 | GOES-16 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 07a0ada0-043b-3169-8718-f4a673704ec8 | -3.6181 | -47.5134 | 2024-11-24 00:50:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| d6461e1c-b37b-3bf5-9689-bbcf16bb5630 | -3.849 | -46.0048 | 2024-11-24 00:50:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 150.1 |
| 6a067a78-b6a6-3f7f-a482-820170d15d13 | -3.8303 | -46.028 | 2024-11-24 00:50:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 55.5 |
| fa681123-52ca-3a77-8789-4d08d7e0756d | -4.2605 | -48.697 | 2024-11-24 00:50:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 40.1 |
| 0426fce2-b721-3c6f-80bf-8ff307558698 | -3.2604 | -53.2746 | 2024-11-24 00:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 237d587a-e573-3e67-a741-1ab337c1118d | -1.5129 | -54.1959 | 2024-11-24 00:50:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 9e3071f9-fe68-3a3c-a402-29f84f26c7c8 | -5.9557 | -48.0425 | 2024-11-24 00:50:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 97.8 |
| f5993b5b-c4a7-3a3f-9087-4c40c051fbe4 | -3.8489 | -46.0271 | 2024-11-24 00:50:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 86.5 |
| 753190c6-28eb-3def-88dc-07c7434bed07 | -2.7596 | -49.1157 | 2024-11-24 00:50:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 85.1 |
| b59f1bf5-2163-37b7-b560-3d75fdfba7be | -2.9044 | -45.3494 | 2024-11-24 00:50:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 5a99f7aa-2c40-3cce-902b-33cb15dc37b1 | -2.9043 | -45.3719 | 2024-11-24 00:50:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 2b0a31e6-fc5c-36fb-b024-42d57b850c38 | -5.0078 | -42.9466 | 2024-11-24 00:50:00 | GOES-16 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 79.5 |


[Clique aqui para ver as próximas entradas](README20.md)

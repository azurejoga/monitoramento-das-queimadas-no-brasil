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

## Dados Diários - Página 77

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8fc5f260-2680-3376-81fc-e12d9b5ffa76 | -7.5104 | -61.3832 | 2026-08-26 09:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 36.0 |
| 522f9347-69fa-3121-9a2d-002ff9a30425 | -7.5289 | -61.3825 | 2026-08-26 09:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 25.8 |
| b03b7479-b90a-32e2-a2af-2a4be444efb6 | -6.641 | -58.4987 | 2026-08-26 09:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 937a307b-5080-303d-b6f5-e2f3ed16a446 | -11.4302 | -44.5382 | 2026-08-26 10:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 133.8 |
| 485635b8-f0a9-36ac-a66e-afdf1d12841b | -11.4302 | -44.5382 | 2026-08-26 10:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 146.4 |
| 222beee5-f921-3aca-a550-cda25c7112a5 | -11.411 | -44.541 | 2026-08-26 10:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 106.4 |
| 7b930f10-e742-30e3-8374-3da9827f9e3a | -11.411 | -44.541 | 2026-08-26 10:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 91.2 |
| c79cd7d5-9f69-3abf-8a67-d868b35966a8 | -11.4302 | -44.5382 | 2026-08-26 10:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 176.6 |
| 1d17e575-7173-3613-b9ff-7ff707357827 | -11.4298 | -44.5615 | 2026-08-26 10:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 87398478-ea3c-3af1-88e4-dddb61ea402a | -11.4302 | -44.5382 | 2026-08-26 10:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 232.5 |
| 32ab39a2-3b4e-30e0-b47c-e49a5fbf9b61 | -11.4302 | -44.5382 | 2026-08-26 11:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 280.5 |
| 037e2184-6fd2-3540-be33-6322ffd90c86 | -11.411 | -44.541 | 2026-08-26 11:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 120.8 |
| 7550daf9-60bd-36f5-a2e2-b774c63cd05e | -11.4298 | -44.5615 | 2026-08-26 11:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 96.5 |
| ab28c4b9-2791-3c3e-8ee2-6854ffb1f515 | -11.4302 | -44.5382 | 2026-08-26 11:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 374.3 |
| 49b928e0-c918-372c-be60-75896509dcd5 | -13.1906 | -51.3166 | 2026-08-26 11:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 109.9 |
| 8b0f6e22-2083-34fd-9ffe-b2205fbed7ef | -11.4306 | -44.5148 | 2026-08-26 11:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 114.4 |
| 676cfc0d-8e68-379d-9cb2-ec4bbc40232d | -11.4306 | -44.5148 | 2026-08-26 11:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 63e823e0-0d4b-3434-a60b-723cc8391a7f | -11.4302 | -44.5382 | 2026-08-26 11:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 369.7 |
| 01d332ec-b0f3-3483-a16b-f720dedd4b62 | -13.2095 | -51.3356 | 2026-08-26 11:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 118.4 |
| c50eabe5-b401-3583-b515-0de9669e80ef | -11.411 | -44.541 | 2026-08-26 11:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 119.2 |
| 7242de85-f46e-3d57-9b12-7021da1c1eaf | -11.4494 | -44.5353 | 2026-08-26 11:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 80.3 |
| bb4f0645-d192-3e62-afed-36d82f1a9c20 | -11.4298 | -44.5615 | 2026-08-26 11:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 96.6 |
| bff3b27e-8b60-3d17-b41a-742296e511bf | -13.1906 | -51.3166 | 2026-08-26 11:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 141.0 |
| 5d5180ea-d4a9-37ad-bd19-c2076dff0798 | -13.1903 | -51.338 | 2026-08-26 11:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 81a4b368-1df0-305c-9b92-e5ee0ec12177 | -11.4302 | -44.5382 | 2026-08-26 11:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 390.7 |
| 986e1251-8e6a-3dac-a814-9800e0b02daa | -13.2095 | -51.3356 | 2026-08-26 11:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 180.1 |
| 020336c6-2677-3b42-9bd1-2815b8a641ec | -11.4298 | -44.5615 | 2026-08-26 11:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 3a3a4310-1383-391e-a785-bccdb2c3de2f | -11.4306 | -44.5148 | 2026-08-26 11:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 6c6599d7-c517-3373-b57b-980811fa2873 | -4.8002 | -43.1709 | 2026-08-26 11:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 6aa9b2f9-eaae-363a-bb6f-f41dc21967cb | -11.411 | -44.541 | 2026-08-26 11:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 148.8 |
| fefac2db-50e5-38b6-bf80-824d4f4d1d2b | -13.2095 | -51.3356 | 2026-08-26 11:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 223.2 |
| 7171e2da-bbe2-31b9-829b-6d078a07b277 | -10.7596 | -54.0384 | 2026-08-26 11:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 71.9 |
| ca26a053-9b47-3f7d-8a4f-cb9afc3b11a1 | -11.411 | -44.541 | 2026-08-26 11:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 137dbe66-4e98-370e-b3c6-6de859533f54 | -8.1482 | -47.5218 | 2026-08-26 11:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 116.2 |
| ee0411c6-64d0-3b91-a642-aaa96a8119e0 | -11.4298 | -44.5615 | 2026-08-26 11:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 82.3 |
| f807071a-2add-3ed2-ad63-6f0c61c0c5aa | -11.4302 | -44.5382 | 2026-08-26 11:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 413.0 |
| 564904ac-9070-3b48-a2da-d5069dd46b94 | -13.1906 | -51.3166 | 2026-08-26 11:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 4e527437-5049-3aca-a761-f54b749bd585 | -13.3034 | -51.4517 | 2026-08-26 11:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 110.9 |
| 9530e879-e346-338f-ac12-9c9d3e1df8ef | -12.6452 | -48.4168 | 2026-08-26 11:40:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 23102e02-be2c-3086-98b5-88f90621f082 | -11.4306 | -44.5148 | 2026-08-26 11:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 136.7 |
| 09e3e2f2-606e-36f6-baf6-0da58b45f6b5 | -11.4298 | -44.5615 | 2026-08-26 11:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 1982e99c-f0ff-39e6-a396-9a55dbcb863f | -10.7596 | -54.0384 | 2026-08-26 11:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 71.2 |
| fe72c840-5593-3930-a255-c6b534e4f14c | -11.411 | -44.541 | 2026-08-26 11:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 167.4 |
| a60c5f51-995d-3423-9a06-1f464f8d7ae7 | -8.1482 | -47.5218 | 2026-08-26 11:50:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 90.2 |
| f57bd81a-df3d-3397-a607-ef6a334b90d9 | -13.3034 | -51.4517 | 2026-08-26 11:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 131.6 |
| b8235e36-555b-344a-99d8-443baefc55eb | -12.6452 | -48.4168 | 2026-08-26 11:50:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 0a9eafd7-01aa-36ee-af75-4b729bdd566e | -12.6836 | -48.4116 | 2026-08-26 11:50:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 72.8 |
| cef13171-3252-3004-aaf5-6d831536efe5 | -11.4494 | -44.5353 | 2026-08-26 11:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 62ff68e9-ea53-3cc1-920c-b44e2739cac1 | -11.4302 | -44.5382 | 2026-08-26 11:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 317.6 |
| cface25c-ec82-35e8-8c57-037204d1b449 | -11.2923 | -47.0644 | 2026-08-26 12:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 19dd88f2-1700-3546-abaf-42d03510c651 | -12.6644 | -48.4142 | 2026-08-26 12:00:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 64a16a69-cd60-3b32-8c56-e1786c031905 | -8.1482 | -47.5218 | 2026-08-26 12:00:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 139.7 |
| 8c785e7d-bb0a-38a8-96ae-0e69854416c9 | -12.6452 | -48.4168 | 2026-08-26 12:00:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 111.8 |
| a3112415-011d-30ff-95a7-f10e1432d9af | -8.1484 | -47.4998 | 2026-08-26 12:00:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 88.4 |
| d71a778a-c0e8-3c1d-bada-a8ce3094210f | -11.4302 | -44.5382 | 2026-08-26 12:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 287.2 |
| 558f2f9d-c928-3f96-9ed1-c71058afb9b2 | -13.3034 | -51.4517 | 2026-08-26 12:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 3e51a869-c43e-3ae8-8e34-5618a978c489 | -11.411 | -44.541 | 2026-08-26 12:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 154.4 |
| 9b3c5923-d739-3755-a036-2d1290cff029 | -11.4298 | -44.5615 | 2026-08-26 12:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 89.3 |
| ebe0d9d0-ebbe-320c-8aeb-873536f1ac2a | -11.4306 | -44.5148 | 2026-08-26 12:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 4c49c750-bf8d-3b50-b869-545f8b406aa0 | 2.39923 | -50.97871 | 2026-08-26 12:08:00 | TERRA_M-T | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 09c2aae5-6c81-3aad-b398-66c2ba7c9c5c | -12.6452 | -48.4168 | 2026-08-26 12:10:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 23d88d4d-9c79-3733-882a-5cf001450b64 | -11.4298 | -44.5615 | 2026-08-26 12:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 652018ee-47b5-3355-964a-65cf11bd8160 | -13.3034 | -51.4517 | 2026-08-26 12:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 17703589-3f2a-3cdd-8d66-39e857fa4248 | -11.4302 | -44.5382 | 2026-08-26 12:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 375.5 |
| aef299ca-db92-3014-8ba8-5aef9fd9fcba | -13.2664 | -51.3711 | 2026-08-26 12:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 37eaf4bf-3252-349a-9fa2-c5837b5f232f | -8.1482 | -47.5218 | 2026-08-26 12:10:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 112.0 |
| 0e6dc155-f0f1-3d8c-8980-300104136f87 | -11.4306 | -44.5148 | 2026-08-26 12:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 104.3 |
| a388a2ef-0dde-346e-ac15-c87d5ed3f258 | -13.2668 | -51.3497 | 2026-08-26 12:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 621d3c1b-53be-396a-af40-472c6aad78cc | -8.1484 | -47.4998 | 2026-08-26 12:10:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 9e579db1-5a74-3da5-8631-8012adb7940e | -11.411 | -44.541 | 2026-08-26 12:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 70.1 |
| c3ef7b22-0828-3f72-91fe-98f828b480bb | -10.7596 | -54.0384 | 2026-08-26 12:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 81.3 |
| b9a5aecb-ec70-3490-93c7-34546110c875 | -5.95471 | -53.58592 | 2026-08-26 12:12:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 3e333c15-e022-3648-93eb-d2455827936e | -7.0269 | -59.23693 | 2026-08-26 12:12:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 9ce2408b-13f7-3fe2-aaab-eccc929d0cb9 | -8.18217 | -54.95852 | 2026-08-26 12:12:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| eafee071-a8b7-324e-bbc2-88d310975e5d | -9.5815 | -49.27456 | 2026-08-26 12:12:00 | TERRA_M-T | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 31.8 |
| 4683c9da-4619-332d-963a-ce3d11cdcba5 | -6.26201 | -55.41549 | 2026-08-26 12:12:00 | TERRA_M-T | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| d3da3ff3-85ed-33ff-9f14-9e0cebf553b0 | -8.22148 | -55.00791 | 2026-08-26 12:12:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 191c3b52-899f-35ea-9040-af5b98d0d8ed | -9.60918 | -55.10591 | 2026-08-26 12:12:00 | TERRA_M-T | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 28.9 |
| 64b22acf-179e-33c7-8bda-a859392b3df3 | -8.26251 | -46.35162 | 2026-08-26 12:12:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 4136c794-c052-37a3-ab07-062397434c1f | -8.09846 | -47.57595 | 2026-08-26 12:12:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 15.2 |
| c50141da-a639-3490-8bed-2af529f5cf2f | -9.72264 | -49.33528 | 2026-08-26 12:12:00 | TERRA_M-T | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 29.3 |
| 8e558be7-2a3e-385d-acee-7e4bf2f33043 | -5.94416 | -57.72994 | 2026-08-26 12:12:00 | TERRA_M-T | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 4340ea78-ba72-35b1-8fae-9b0dfa194ee1 | -6.99697 | -59.31462 | 2026-08-26 12:12:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 15.4 |
| dd3a7944-8174-3e1a-a67a-81f6b699aaf3 | -6.23483 | -55.47181 | 2026-08-26 12:12:00 | TERRA_M-T | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 1623e519-95dc-308f-aae3-e1a5aa5a9a60 | -8.1572 | -47.52992 | 2026-08-26 12:12:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 93.0 |
| b6504d3d-a07e-31b7-b809-b7cccb2cde1b | -9.71208 | -49.32788 | 2026-08-26 12:12:00 | TERRA_M-T | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 36.2 |
| 2bd3c594-0cb8-3bf3-a478-7d160a201d35 | -6.26883 | -53.38767 | 2026-08-26 12:12:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 31.3 |
| a5b20b53-bfec-346a-950b-55ca0098fd6a | -8.95593 | -50.77411 | 2026-08-26 12:12:00 | TERRA_M-T | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| f573cbcb-af8b-36af-a17a-4bc6cb755f58 | -8.08313 | -47.49508 | 2026-08-26 12:12:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 6af263e5-5473-3977-b49d-9012fd84de74 | -8.38423 | -46.44923 | 2026-08-26 12:12:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 970d331d-2814-3de4-8b2c-131e1c563118 | -8.79903 | -49.39362 | 2026-08-26 12:12:00 | TERRA_M-T | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 16e273de-3345-3fc2-a8ca-de30d232de2d | -6.17038 | -53.49376 | 2026-08-26 12:12:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| b527b923-7ba2-3279-8cbe-51b8a2a3ccea | -4.79686 | -43.17388 | 2026-08-26 12:12:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 56.3 |
| 9e790925-70a6-3204-911a-73e06fab4671 | -9.08099 | -50.5994 | 2026-08-26 12:12:00 | TERRA_M-T | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 6fd6c0a6-79f2-3bd4-a9fb-13782b339c17 | -4.80181 | -43.13548 | 2026-08-26 12:12:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 37.8 |
| 2e9f48d7-fe90-32b2-b767-633ad6bd7120 | -8.101 | -47.55647 | 2026-08-26 12:12:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 26.0 |
| fad37814-68c1-3a15-ad17-4a29fe0683ca | -7.07749 | -59.22702 | 2026-08-26 12:12:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 20a48639-156b-3437-8871-21fb935e0e35 | -10.02599 | -46.42837 | 2026-08-26 12:12:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 22.6 |
| d0ebd53d-e72f-3a9d-94be-7d81e53d800a | -8.57026 | -55.27221 | 2026-08-26 12:12:00 | TERRA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 6585288c-a144-3f6b-a6ba-8f26aa902467 | -6.67171 | -43.41926 | 2026-08-26 12:12:00 | TERRA_M-T | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 58.4 |


[Clique aqui para ver as próximas entradas](README78.md)

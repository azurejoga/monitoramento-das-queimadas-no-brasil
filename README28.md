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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 071109d6-5c82-3167-8b23-2ac861e3b7b2 | -6.7295 | -59.153 | 2025-08-01 07:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 4bb891c2-b3b3-377f-a222-a3577449154f | -6.8395 | -59.2643 | 2025-08-01 07:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 124.9 |
| 02bfc8b1-6b6e-30ea-aab3-857e34de7491 | -6.7478 | -59.1716 | 2025-08-01 07:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 100.7 |
| 0cd40e64-464b-358b-9cee-20b198fc6b07 | -8.051 | -43.1237 | 2025-08-01 07:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 69.6 |
| d9d505e5-d74b-3881-a0ac-f86a9713041a | -8.0513 | -43.1001 | 2025-08-01 07:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 55.7 |
| 4f0cfed4-de55-328d-a247-f4d627c0c9ff | -6.7293 | -59.1916 | 2025-08-01 07:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 3acaaf90-38db-3ddb-8ad8-bca0ba9b63a1 | -6.8026 | -59.2658 | 2025-08-01 07:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 2a13df31-be90-33bf-992d-61a19e64549a | -6.821 | -59.2844 | 2025-08-01 07:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 1f881dfe-3a6d-391b-b6ae-d538f2488873 | -6.7294 | -59.1723 | 2025-08-01 08:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 140.5 |
| c79a1287-6613-3a9a-929c-5b22b989a52a | -6.821 | -59.2844 | 2025-08-01 08:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 89075c40-3714-339a-9c90-7e0defc74cb1 | -10.0815 | -46.7441 | 2025-08-01 08:00:00 | GOES-19 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 94.6 |
| b482f3d3-8343-3107-9727-a89444229429 | -6.8395 | -59.2643 | 2025-08-01 08:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 108.9 |
| cf2cb5a6-1da2-3fe4-a4a6-61827754e346 | -8.051 | -43.1237 | 2025-08-01 08:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 66.3 |
| 60d91064-e9af-3d28-a16e-d3b67bd7501e | -8.0321 | -43.1257 | 2025-08-01 08:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 63.4 |
| 0ab5ef32-8c1a-3d7f-88ba-9be4becfc691 | -6.7293 | -59.1916 | 2025-08-01 08:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 79defb1e-80ae-3707-ba8f-f3c90456c1b2 | -6.8211 | -59.2651 | 2025-08-01 08:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 223.3 |
| a9081798-10bc-31ee-b6ba-f286d7394fcc | -6.8212 | -59.2458 | 2025-08-01 08:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 86265f35-0aee-39fb-b523-7b28e181065d | -8.0513 | -43.1001 | 2025-08-01 08:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 63.1 |
| 31074a7c-6df7-3573-964e-c7cf46abb6c2 | -6.748 | -59.1523 | 2025-08-01 08:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 843ca902-3233-3022-9cc4-ec12b32501d1 | -6.7478 | -59.1716 | 2025-08-01 08:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 102.6 |
| 8c7d26cd-1488-3e44-8cf7-32189e97a20f | -6.7478 | -59.1716 | 2025-08-01 08:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 89.9 |
| de5a3a85-b4a8-3e50-a57b-edff5f95d2ea | -6.8395 | -59.2643 | 2025-08-01 08:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 101.6 |
| bf02507e-84db-3092-a012-956210e38703 | -6.8026 | -59.2658 | 2025-08-01 08:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.3 |
| ff4d3555-2ffd-3aaa-a8c5-da1d75a9c400 | -6.8211 | -59.2651 | 2025-08-01 08:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 216.3 |
| 9c7775ee-e971-3de8-8b34-a7edb6b1a790 | -8.051 | -43.1237 | 2025-08-01 08:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 71.0 |
| 9febc5fa-224b-3a0c-b3a8-b9a4eff61db4 | -8.0321 | -43.1257 | 2025-08-01 08:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 80.9 |
| 397f796c-cf05-3d4b-9e2e-4eb1f49ba702 | -6.821 | -59.2844 | 2025-08-01 08:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 80.2 |
| 8bcbce92-9541-3ca0-8872-0e1ba31b192d | -6.7293 | -59.1916 | 2025-08-01 08:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 60b63ed2-b7d2-30be-9643-6f498b4781a0 | -6.8212 | -59.2458 | 2025-08-01 08:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 646896cb-7162-3e11-b9a4-29fc482d8754 | -6.7294 | -59.1723 | 2025-08-01 08:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 164.5 |
| b9f41f8b-d3e6-37d5-840e-e54fb89e97fc | -8.0513 | -43.1001 | 2025-08-01 08:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 68.1 |
| 2341abe4-6138-32e6-9fcb-43295d65b508 | -6.7293 | -59.1916 | 2025-08-01 08:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 2b56c9b0-3e45-36ee-9245-89df5b39f464 | -6.7294 | -59.1723 | 2025-08-01 08:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 162.0 |
| 794228e8-8a4c-3880-a6ce-8bfbe0aa6c07 | -8.0513 | -43.1001 | 2025-08-01 08:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 74.7 |
| 15f1bba9-6240-3ae9-befa-5b036923ef3f | -6.8211 | -59.2651 | 2025-08-01 08:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 241.7 |
| d3fd2711-0a9e-390b-b9ff-a683ebbdb0c1 | -6.7478 | -59.1716 | 2025-08-01 08:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 83.4 |
| 50707f6b-53e4-3683-9e46-92ad5dbd90e3 | -8.051 | -43.1237 | 2025-08-01 08:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 82.9 |
| 80402577-58e6-34e0-b991-d00b09edb431 | -6.8212 | -59.2458 | 2025-08-01 08:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 3c466fa7-3d61-31d8-8d42-e67af2561280 | -6.821 | -59.2844 | 2025-08-01 08:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 66e3ff6e-7f82-3d72-be8f-c45bb38d41d1 | -6.8395 | -59.2643 | 2025-08-01 08:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 86.3 |
| 425d4a13-52a1-3b33-93fe-c3f841453456 | -6.8211 | -59.2651 | 2025-08-01 08:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 201.6 |
| 5efa9d35-ac09-37e9-bd7a-58278e676a7e | -6.8026 | -59.2658 | 2025-08-01 08:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 1ad8e4f7-e8a1-3a53-86a8-19877321d872 | -6.7478 | -59.1716 | 2025-08-01 08:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 104.7 |
| fc9d0ffd-9094-39e7-9366-4523e21e222f | -6.7294 | -59.1723 | 2025-08-01 08:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 135.6 |
| e6a52bf5-eced-35dc-9038-83550b444eae | -6.7295 | -59.153 | 2025-08-01 08:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 2d8595df-9314-37fa-8564-ca38515f9a94 | -6.8395 | -59.2643 | 2025-08-01 08:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 125.2 |
| f3254964-6f2c-3e49-b90a-e5b98dd62ea8 | -6.821 | -59.2844 | 2025-08-01 08:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 2dab97f6-5e7e-3a88-94e7-d880fae744f4 | -6.8212 | -59.2458 | 2025-08-01 08:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 36e9fa97-c048-3185-b1dd-b0366bed3cb9 | -6.7293 | -59.1916 | 2025-08-01 08:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.6 |
| c20748e2-9e4f-31cd-916a-c7b3dafdc307 | -6.8395 | -59.2643 | 2025-08-01 08:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 82.5 |
| 65e45cc4-810f-325b-aa27-74afd9896e22 | -6.7294 | -59.1723 | 2025-08-01 08:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 145.1 |
| 91c63d14-bd05-3a52-b45a-08f70268b48e | -6.821 | -59.2844 | 2025-08-01 08:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.1 |
| faa19053-0ad4-3df1-a5bc-e65611ef87f6 | -6.7478 | -59.1716 | 2025-08-01 08:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 65edeb4c-9514-3aab-8c9c-26a50d89c93b | -6.8211 | -59.2651 | 2025-08-01 08:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 215.9 |
| af7cc608-5f5f-38b5-881e-c8fd2bb99daf | -6.7295 | -59.153 | 2025-08-01 08:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.3 |
| d32c4b9b-0a04-3323-ab69-dbb37f46f89f | -6.7294 | -59.1723 | 2025-08-01 08:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 147.0 |
| 2018e81e-1c59-36ab-bf24-a18ee039708f | -6.7293 | -59.1916 | 2025-08-01 08:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 71e207d2-531e-34bc-a492-c08b68ed27ea | -6.821 | -59.2844 | 2025-08-01 08:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 23eea0e2-8b65-337c-be67-fbd5bb626ddd | -6.7478 | -59.1716 | 2025-08-01 08:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.7 |
| d9838f9d-bc23-34cc-bdf1-d10282093fab | -6.8395 | -59.2643 | 2025-08-01 08:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 89.2 |
| 783b09f7-f5cb-3d97-ba7d-21db3ff78335 | -6.8211 | -59.2651 | 2025-08-01 08:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 236.3 |
| 0dd814ac-531c-3c48-af52-4705918d6726 | -6.7294 | -59.1723 | 2025-08-01 09:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 106.8 |
| a27b6ce4-3704-3d4d-9804-604ab5f8085e | -6.7295 | -59.153 | 2025-08-01 09:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 7d986f18-9f3e-37bb-9510-dd79d29ce1a3 | -6.7478 | -59.1716 | 2025-08-01 09:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 1d2259d5-3ce3-30f3-9ebe-ad609b9d8973 | -6.8395 | -59.2643 | 2025-08-01 09:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 90.8 |
| 3b8245d9-bb12-3a98-b355-588601b2553a | -6.8211 | -59.2651 | 2025-08-01 09:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 240.8 |
| 5b268cdb-ca31-36c1-b8b2-52f118a4ed37 | -6.8212 | -59.2458 | 2025-08-01 09:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 311caa65-0e25-3f94-9450-6504f9803203 | -6.7294 | -59.1723 | 2025-08-01 09:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 39.2 |
| 04a41c9e-5f8b-3a30-9d58-58c5ca1cc6e3 | -6.8212 | -59.2458 | 2025-08-01 09:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.2 |
| e148ad8a-d753-36a7-b86a-475b907e6f33 | -6.8211 | -59.2651 | 2025-08-01 09:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 219.1 |
| 587f50c3-4de5-3393-b7d2-717fcce2377c | -6.8395 | -59.2643 | 2025-08-01 09:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 87.1 |
| dfb7f2bc-8eeb-3331-b2eb-6467ced30464 | -6.7294 | -59.1723 | 2025-08-01 09:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 88.0 |
| 9f2ab070-cac2-3be6-b655-b9fc01c674b5 | -6.8395 | -59.2643 | 2025-08-01 09:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 86.2 |
| 4ac9a81d-93f0-3f0e-8f65-9d6f2ed4675d | -6.821 | -59.2844 | 2025-08-01 09:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.0 |
| fac9ecff-a086-357a-8fa4-ef11b4a2eff1 | -6.7478 | -59.1716 | 2025-08-01 09:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 2f478d37-943a-3af1-a00a-f325e50c7171 | -6.8211 | -59.2651 | 2025-08-01 09:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 216.7 |
| 722bd8f6-b70e-350a-9b09-6088db7a36dc | -6.8212 | -59.2458 | 2025-08-01 09:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.8 |
| f72b38e2-ab90-3f0c-9fc7-18157ec3cad2 | -6.7478 | -59.1716 | 2025-08-01 09:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.7 |
| c6f9ef2c-bc4f-377c-b6d1-9d11d3a96b72 | -6.7293 | -59.1916 | 2025-08-01 09:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.1 |
| c30ef91b-f74f-3dca-bd5e-615acd0719bc | -6.8395 | -59.2643 | 2025-08-01 09:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 6b0402d9-80f9-3197-8d4f-cce0ab8816e0 | -6.8211 | -59.2651 | 2025-08-01 09:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 188.3 |
| 8ad3c942-b2fe-37a9-8ea8-018d5c9f7891 | -6.821 | -59.2844 | 2025-08-01 09:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 8cee9706-ffb8-3658-a596-cefd52cfcaa5 | -6.7294 | -59.1723 | 2025-08-01 09:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 125.5 |
| 5bc5f86e-3c0f-3e70-b2fb-a625ed21c168 | -6.8211 | -59.2651 | 2025-08-01 10:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 167.7 |
| ffeeb093-99b9-3c1b-9423-06a4a9f6313d | -6.7294 | -59.1723 | 2025-08-01 10:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 114.9 |
| 667e1e5d-cd8a-3684-9f4a-99d7724f6afd | -6.8395 | -59.2643 | 2025-08-01 10:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 104.8 |
| 81e09c26-8a3a-37fe-a1d2-2152cae032a5 | -6.8395 | -59.2643 | 2025-08-01 10:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 96.7 |
| 71c2100f-b30c-34e9-ae98-73d00ce7b48d | -6.8211 | -59.2651 | 2025-08-01 10:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 147.1 |
| 253ef9a4-edbb-310a-aff5-f5a499c27c52 | -6.7478 | -59.1716 | 2025-08-01 10:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 91.3 |
| 098fb4a6-805a-3f94-9047-a1c0383c13f9 | -6.7294 | -59.1723 | 2025-08-01 10:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 109.7 |
| 5cffe4e3-1f9b-329b-a87e-7c5b017022d9 | -6.7294 | -59.1723 | 2025-08-01 10:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 121.3 |
| d78dc11b-4a7a-38c8-9e97-cafa2f91cc33 | -6.8211 | -59.2651 | 2025-08-01 10:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 144.2 |
| 771f85b7-dc76-3e0f-8245-950c71f9b7f6 | -6.7294 | -59.1723 | 2025-08-01 10:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 118.7 |
| cecb888e-a713-3bff-9645-678b6ec6b7bf | -6.8211 | -59.2651 | 2025-08-01 10:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 149.2 |
| 78cdcba6-0562-3034-99d3-36f265320e07 | -6.8395 | -59.2643 | 2025-08-01 10:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 92.0 |
| 6f99c0e9-53f2-3fa5-867f-3181b7a9b050 | -6.7294 | -59.1723 | 2025-08-01 10:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 110.2 |
| d510b418-ee49-3b54-b58f-549a97b789a9 | -6.8211 | -59.2651 | 2025-08-01 10:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 137.2 |
| 4de422f4-6af2-3c5b-b2ef-992853d97691 | -6.8211 | -59.2651 | 2025-08-01 11:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 147.1 |
| bcca1784-2c84-32dd-b5e5-9d8529567986 | -8.051 | -43.1237 | 2025-08-01 11:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 125.6 |
| cc501c44-22a4-3b12-8bc6-5214a4b51cf9 | -6.7294 | -59.1723 | 2025-08-01 11:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 102.5 |


[Clique aqui para ver as próximas entradas](README29.md)

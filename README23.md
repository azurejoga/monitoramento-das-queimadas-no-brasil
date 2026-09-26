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
| ab451a81-e053-39d9-99c0-d3f2f1374cc1 | -1.11925 | -57.06239 | 2026-09-26 05:10:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 44013ce7-53a0-3367-a80e-de5f3bd2ce2a | -5.06505 | -56.06066 | 2026-09-26 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8eb23452-cbce-34f7-b1c5-0bb14f20141b | -1.1508 | -54.09428 | 2026-09-26 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 567b596d-c84b-3c64-861b-5f0817c33821 | -2.88667 | -54.08789 | 2026-09-26 05:10:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c078ddae-1f7f-392a-aa20-292be060a5d4 | -3.20229 | -53.41051 | 2026-09-26 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 67d80b82-a474-34e2-b97c-7501361c7ded | -3.99385 | -52.0486 | 2026-09-26 05:10:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6dbc7940-3077-331f-b786-b1ea85a71670 | -4.41162 | -47.79845 | 2026-09-26 05:10:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b12772ec-b574-39b8-8478-c57aea2057ab | -2.15175 | -53.7088 | 2026-09-26 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8ca1030f-aebb-30cf-99c6-46327884dee4 | -2.57388 | -54.74338 | 2026-09-26 05:10:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 19bbe807-723c-3b4d-842b-4c48e10b2409 | 1.63033 | -55.91025 | 2026-09-26 05:10:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 450d834d-f174-31c8-b460-362cb762f6c7 | 1.57918 | -56.0584 | 2026-09-26 05:10:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1cf11b19-e569-3490-9c69-513e949abf97 | -3.7633 | -51.80434 | 2026-09-26 05:10:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 25dbfe7f-a0e8-34ac-97f0-19b2c9cb3903 | -3.30165 | -54.68797 | 2026-09-26 05:10:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 56cbd40c-5196-3bc3-9888-6e74b51554ec | -2.8397 | -51.38437 | 2026-09-26 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 448024fc-47ef-33b8-93be-81bd94d6773b | -2.8671 | -49.62951 | 2026-09-26 05:10:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3a70216a-cab4-3be3-aef8-c8b2f10cef9c | -3.22807 | -54.3213 | 2026-09-26 05:10:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bd2e4716-7ee6-3aae-879e-88c63ff2a453 | -5.16901 | -56.00387 | 2026-09-26 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 57718076-187a-352c-8361-2ed163acb282 | -3.80603 | -49.18389 | 2026-09-26 05:10:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 00d9da22-fb83-3302-847a-63903cb696c9 | -1.41366 | -54.62211 | 2026-09-26 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 40c8e4a4-6e3c-3b4a-a6a7-4ecaec9268b8 | -4.44874 | -55.03088 | 2026-09-26 05:10:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| decd5576-65d0-3c0a-839b-22e2a7f297e6 | -5.0645 | -56.0642 | 2026-09-26 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8835e0f0-e8b3-3095-9a80-05094291bfb5 | -5.77943 | -45.10252 | 2026-09-26 05:10:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6c1167bf-15f4-3fcf-824b-4d25485ecc6f | -1.69006 | -55.56181 | 2026-09-26 05:10:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 87bb2cdc-9f90-3fb3-807e-5478ce574b46 | -2.57332 | -54.74707 | 2026-09-26 05:10:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e4bd27c9-3023-3a3a-92a6-aea0bf7bace2 | -3.01102 | -54.20173 | 2026-09-26 05:10:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8ebe220b-45d5-3554-96f4-2bf405a5507a | -2.41223 | -56.42738 | 2026-09-26 05:10:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3701e4ac-3b72-341e-b592-f3e3f3406d7a | -2.90424 | -54.09421 | 2026-09-26 05:10:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 84dada77-3e46-3796-8c5a-9a47564d6496 | -4.87072 | -48.91238 | 2026-09-26 05:10:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 70023183-150a-30ae-a1fe-76fcb7b6d4cc | -1.68619 | -55.56477 | 2026-09-26 05:10:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9d065c84-69de-339f-ab5f-93f02793695d | -3.49188 | -54.68138 | 2026-09-26 05:10:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| dcb6a692-2e03-30dd-8d18-1bd0b39df7c3 | -5.77799 | -45.1131 | 2026-09-26 05:10:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e963be08-f5b1-3a8f-93a3-0a8dede64372 | -2.40947 | -56.42344 | 2026-09-26 05:10:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 498f980f-d27c-39ce-a120-b6faac8f29a2 | -2.91627 | -54.18045 | 2026-09-26 05:10:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1c2d1212-7ec3-38a4-8035-27a3153f2f50 | -2.91568 | -54.18434 | 2026-09-26 05:10:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| be1d29f5-fa7e-300d-941a-1cebe24ef08b | -1.19672 | -49.12717 | 2026-09-26 05:10:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 408d8779-0f4c-3ea0-8c23-079f3cb0f118 | -1.33581 | -55.47784 | 2026-09-26 05:10:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 59c645c3-8b64-378d-8827-73c88fcfe8be | -3.22493 | -48.81351 | 2026-09-26 05:10:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0dacc92b-b6cb-3509-80bc-28303ff1eac6 | -1.14618 | -54.10136 | 2026-09-26 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 75a594ef-7cc7-3684-b67f-d42281d74e8b | -1.33968 | -55.47486 | 2026-09-26 05:10:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bdfebeda-518a-346a-8908-75c78283bd7a | -5.16846 | -56.00739 | 2026-09-26 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 65b1394f-a5df-3dcd-bc3d-b30a4cae7c25 | -3.50539 | -50.74184 | 2026-09-26 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9f3f7721-b6c8-3d6d-804d-8c667317ddef | -3.80305 | -51.02466 | 2026-09-26 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e211d56d-faa5-33b5-b46e-712b83fed11a | -3.23156 | -54.32185 | 2026-09-26 05:10:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6e0a0f31-4bf4-3c3c-8c88-dc79503d29b7 | -2.27781 | -54.5923 | 2026-09-26 05:10:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 81582971-bd6b-3554-9426-f77345b1791f | -1.14792 | -54.08996 | 2026-09-26 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 396628a3-27f4-34a2-9867-fbde03f4fa5b | -1.14602 | -54.0866 | 2026-09-26 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 6363c03e-be65-30df-b332-1b2807dedd0f | -1.15022 | -54.09809 | 2026-09-26 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 20400fab-061d-3e3a-a392-5fb46be37912 | -2.99231 | -50.47296 | 2026-09-26 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d0cf4016-8096-3518-af82-6b37b2714c74 | -3.72657 | -49.05991 | 2026-09-26 05:10:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1318b09b-89b9-3775-8232-ce04243c42de | -2.83954 | -51.35782 | 2026-09-26 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| be3fb482-96b7-310f-a35b-e943efac9ad6 | -4.4598 | -47.9206 | 2026-09-26 05:10:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| fd780829-f3c3-31b3-85b4-fd3e3d620ae6 | 1.5852 | -55.81559 | 2026-09-26 05:10:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b457ef69-f28d-36a5-9188-0b4f94deacd4 | -4.29863 | -50.89509 | 2026-09-26 05:10:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9f845346-89b3-32e5-a3a9-886ac878c16b | -3.22408 | -48.81912 | 2026-09-26 05:10:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7f8411b2-2229-3c28-bc62-f6cad25abfb8 | -1.21858 | -54.56649 | 2026-09-26 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c05ba980-2b2f-3f36-b3bb-492b8373d0c4 | -2.91866 | -54.16483 | 2026-09-26 05:10:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7d17eaf6-bcbe-316e-b7a4-13b810e447ba | -2.37599 | -50.409 | 2026-09-26 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f9aea08a-4cbe-38a4-bac0-17d89a07cff4 | -1.14446 | -54.08943 | 2026-09-26 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| fa913f8a-42f7-3df3-9a7a-2298c352136a | -3.19962 | -53.40311 | 2026-09-26 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7f5f7869-89ff-3261-b3ed-3f553deb8e5c | -1.14543 | -54.0904 | 2026-09-26 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| acfba7dc-4522-3e03-8c01-a058ace97c2d | -3.49854 | -53.45665 | 2026-09-26 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 240b1085-9ebe-37aa-876e-071dd1e9c78d | -2.71347 | -57.52852 | 2026-09-26 05:10:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 3c930996-3837-37d4-9018-12fd9dc46ac1 | -1.54683 | -54.26134 | 2026-09-26 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fd2b9f06-53bc-31c5-af8c-3acfabe3b260 | -3.20659 | -53.40675 | 2026-09-26 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a3c0e3c6-d18c-32a0-ac9c-5a039a75fbb8 | -1.83729 | -54.71912 | 2026-09-26 05:10:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 20.8 |
| bb0e83c3-0998-3334-912b-9bb79cb6cb65 | -3.76275 | -51.80794 | 2026-09-26 05:10:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fb0d9acf-e423-33b9-82f9-5f53e28db9dc | -5.1662 | -55.99986 | 2026-09-26 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 018af5fa-1628-3807-8567-b5e6191d2f5d | -3.20626 | -53.40855 | 2026-09-26 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eabb3600-46fc-37e5-85ec-199686d66a30 | -3.80249 | -51.02853 | 2026-09-26 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b21b37f1-b6b9-3c96-9a45-b6c53208a999 | -3.87506 | -52.281 | 2026-09-26 05:10:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 49c89cdb-72bb-3f73-a588-b88c68098a38 | -5.74404 | -45.06823 | 2026-09-26 05:10:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 08e37e43-5812-307c-bfa5-029f6ac71cbf | -4.87662 | -55.84981 | 2026-09-26 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| de2bb066-7dcf-35bd-ab95-498d22494608 | -3.71794 | -54.64841 | 2026-09-26 05:10:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3d07c103-1dcd-3576-932f-53370a7879bc | -2.15468 | -53.71337 | 2026-09-26 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 19a51313-f14d-3b91-a565-333f64308c78 | -3.26841 | -50.14176 | 2026-09-26 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 18a366fb-36c3-3d2f-9843-60da0f64d7d5 | -3.9825 | -48.43178 | 2026-09-26 05:10:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6e164e3e-a87a-3675-913e-21326c88da7a | 0.17863 | -51.10799 | 2026-09-26 05:10:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2f76d4d6-7888-31f2-af56-466b2eea7195 | -2.54925 | -54.65263 | 2026-09-26 05:10:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 27234264-c08f-3b29-8acc-2dba4b8b667f | -5.77514 | -45.08508 | 2026-09-26 05:10:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c4a56627-f623-39c4-8a1c-5f5e6c20d6ec | -3.96282 | -56.12762 | 2026-09-26 05:10:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0ac879ea-049f-33d2-be18-3a69d8cbb833 | -4.97979 | -56.19226 | 2026-09-26 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b0ff054c-19ea-364f-87a4-2e31673f1b6c | -2.95887 | -54.0905 | 2026-09-26 05:10:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6107449a-b8d0-38cb-ace6-d5b9e5a96292 | -3.26445 | -54.27114 | 2026-09-26 05:10:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 38e2e6d6-3680-3b3a-9d38-2b406d544212 | -4.13017 | -54.25018 | 2026-09-26 05:10:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c53d0b16-72a6-39c8-a7e8-90cce5ab0f8b | -4.98033 | -56.18875 | 2026-09-26 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3afecfc8-0ca6-3633-bdb4-e3dc25d2b6d7 | -3.26772 | -50.14627 | 2026-09-26 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 119a2d15-f69a-3c76-bb3a-6ea915cee5b7 | -1.34355 | -55.47189 | 2026-09-26 05:10:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 76946920-036a-304f-80e1-5463886ec5ea | -4.46788 | -54.90646 | 2026-09-26 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b69f4566-a522-3643-aab9-b53a2871ea54 | -2.72784 | -57.52362 | 2026-09-26 05:10:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 79bc7d9d-7758-37cd-b93c-960c9703ac11 | -4.4593 | -47.92396 | 2026-09-26 05:10:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| a1860cd2-5726-3ec1-b06c-1b78127261e0 | 1.58907 | -56.05688 | 2026-09-26 05:10:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d6420413-d96c-3252-b6ce-005d5d6d5cc0 | -5.16511 | -56.0069 | 2026-09-26 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1c1eaa50-091d-37bf-911e-c1f178dc9d74 | -1.21518 | -54.56596 | 2026-09-26 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dddf459d-8492-3ed4-b041-3d7a60f2817d | -3.27499 | -50.13999 | 2026-09-26 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d53d7da9-cb7c-3112-af47-cd372cee289d | -1.69338 | -55.56235 | 2026-09-26 05:10:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 60ad7c73-e8ac-3216-9e52-28b461a28b09 | -3.22398 | -54.32464 | 2026-09-26 05:10:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8fc2b3e2-11c7-3d5e-a6bc-93d37e9e6a97 | -1.68673 | -55.56129 | 2026-09-26 05:10:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f5bff951-7bc9-3a75-b416-88b035c73936 | -3.20925 | -53.41342 | 2026-09-26 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0ebd11bb-e1a5-3079-bc0e-86dae7cf48d7 | -2.46555 | -57.93812 | 2026-09-26 05:10:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0c552a52-16b1-38fc-83de-67846eee1060 | -3.87111 | -52.28043 | 2026-09-26 05:10:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README24.md)

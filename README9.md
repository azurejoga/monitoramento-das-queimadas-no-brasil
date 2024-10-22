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
| 974978d5-67dd-30d1-b2c8-4d8088118e8c | -2.7589 | -49.3072 | 2024-10-22 01:15:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 102.7 |
| a5e4aea7-508e-32f9-8849-9ab28c1bb050 | -2.7773 | -49.3279 | 2024-10-22 01:15:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| a332232a-0b58-3ab5-aeeb-1dd8a9efca27 | -2.7773 | -49.3067 | 2024-10-22 01:15:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 78.3 |
| c7d958bb-ee71-380f-8cf4-e83cd0f44a03 | -2.8482 | -45.4637 | 2024-10-22 01:15:22 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 93.9 |
| 24997944-168d-3990-95e1-73a22511bf16 | -2.8668 | -45.4631 | 2024-10-22 01:15:22 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 87.0 |
| 0779c3d3-d811-3bc4-be39-35d3155de909 | -3.0765 | -53.239 | 2024-10-22 01:15:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| b2152f35-1f6e-3c61-92de-3c769d60cb14 | -3.0838 | -51.25 | 2024-10-22 01:15:24 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 83f19855-0224-3ff8-be15-5ac0af72fc8c | -3.0917 | -54.1867 | 2024-10-22 01:15:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| c5927ef4-b060-3bf3-bee9-1fcea4d402c7 | -3.0917 | -54.1666 | 2024-10-22 01:15:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 130.7 |
| 614f223c-5e11-3f14-869f-247a632a0d8d | -3.0918 | -54.1465 | 2024-10-22 01:15:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 0c8fb3fb-fe50-3f06-9b60-7130eb4fe9c4 | -3.11 | -54.1862 | 2024-10-22 01:15:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| a24566c7-a903-36e2-a310-8ee37299602a | -3.1101 | -54.1661 | 2024-10-22 01:15:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 104.1 |
| 1109c26e-3a18-3226-b9b9-2f06e78d8581 | -3.1102 | -54.146 | 2024-10-22 01:15:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 1284517f-550a-3bad-990a-36948f3c2625 | -3.9975 | -46.0425 | 2024-10-22 01:15:29 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 60.5 |
| d7ade4e4-7075-3132-95eb-2fbc46ef4dc6 | -3.9977 | -46.0202 | 2024-10-22 01:15:29 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 126.2 |
| 96472e53-4eca-34a3-9005-482684ab5d2b | -4.0161 | -46.0416 | 2024-10-22 01:15:29 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 84.2 |
| de4498ce-829e-36bc-84b5-50d84e808084 | -4.0163 | -46.0193 | 2024-10-22 01:15:29 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 230.9 |
| 0d30c8b2-9aa3-32ad-b82b-485368cf486e | -4.0164 | -45.997 | 2024-10-22 01:15:29 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 08cbc6d4-faaa-39ec-867e-236e83e87860 | -4.5572 | -45.8128 | 2024-10-22 01:15:32 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 58.9 |
| af372dd4-2205-3e0f-80c7-ae2f65f7e67a | -4.5574 | -45.7905 | 2024-10-22 01:15:32 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 50.4 |
| c09ae0e4-edde-314e-8bf5-4117aa92aaa3 | -5.2305 | -43.1886 | 2024-10-22 01:15:36 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 59.9 |
| bd04c76d-e8b7-3ba9-9e51-4a51c4b07d5a | -5.5716 | -44.8927 | 2024-10-22 01:15:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 55.2 |
| e9d2264a-0554-3ea8-9af2-72e5029fc68c | -5.5718 | -44.87 | 2024-10-22 01:15:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 85.9 |
| e25d8a43-87e0-3f6e-8d5d-ad6b46debb47 | -5.5903 | -44.8914 | 2024-10-22 01:15:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 98b795a6-c894-37f0-a1c0-b54730a95a51 | -5.5905 | -44.8687 | 2024-10-22 01:15:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 140.0 |
| f6a7b0a5-1eaf-37cb-ab13-e72bdc8b1776 | -6.2334 | -44.1565 | 2024-10-22 01:15:41 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 51.5 |
| c1a28c52-ca49-3a67-a6c9-fc13823b63f3 | -6.2336 | -44.1335 | 2024-10-22 01:15:41 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 937aab43-3fee-3bd6-92c0-a4ec0823ffe8 | -6.2524 | -44.132 | 2024-10-22 01:15:41 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 57.6 |
| f03e9f47-7d75-3a3a-9f2c-2f7f968d100b | -7.8245 | -61.3709 | 2024-10-22 01:15:51 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 8a6a2d2a-1a34-3d5d-b88a-805167a05fbf | -17.0213 | -57.3333 | 2024-10-22 01:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 100.9 |
| 7403d285-347f-3111-8ff0-bd1c127cedd9 | -1.1834 | -53.6569 | 2024-10-22 01:25:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 7d79f8c8-75bd-3cb1-aa3a-0f8402ae053b | -2.4824 | -49.1233 | 2024-10-22 01:25:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 118.9 |
| 76ca0833-3b48-3303-831b-0afe604642da | -2.4824 | -49.102 | 2024-10-22 01:25:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 112.7 |
| 868cec67-80c5-362f-923c-8db1d7d82dcf | -2.7404 | -49.3077 | 2024-10-22 01:25:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| c4d69111-7f7f-36bf-b7d1-c7a570c3567f | -2.7588 | -49.3285 | 2024-10-22 01:25:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 95.1 |
| b44f04be-8868-3308-89b5-786d46b655b0 | -2.7589 | -49.3072 | 2024-10-22 01:25:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 124.4 |
| a5d74fd0-da64-3801-aaf9-3105bccdfc1f | -2.7773 | -49.3279 | 2024-10-22 01:25:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 4e15895c-c734-326d-b588-af4eccbf4434 | -2.7773 | -49.3067 | 2024-10-22 01:25:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 001bf6eb-4f9f-3053-80e6-57fdc5c55b57 | -2.8482 | -45.4637 | 2024-10-22 01:25:22 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 100.5 |
| df97f865-cf6d-3808-954e-1dd01f6930dc | -2.8668 | -45.4631 | 2024-10-22 01:25:22 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 134.6 |
| fc4d5e28-0599-3c0d-8430-36813171ffac | -3.0581 | -53.2395 | 2024-10-22 01:25:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 3de90b66-ed70-38ef-9255-06c470be2d41 | -3.0838 | -51.25 | 2024-10-22 01:25:24 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| e331c410-7983-39d3-adb1-fac561346d8f | -3.0917 | -54.1867 | 2024-10-22 01:25:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 7f9d517e-9c90-387e-84cd-813a82a2302d | -3.0917 | -54.1666 | 2024-10-22 01:25:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 97.0 |
| 8f604c42-94f2-3a84-abb1-1412b9639efa | -3.0918 | -54.1465 | 2024-10-22 01:25:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 6fa4a39c-50cd-3649-bc31-23d4187edbd1 | -3.1101 | -54.1661 | 2024-10-22 01:25:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 80.6 |
| 1419dcbc-e0a1-3a03-bd8b-6d5022c17eff | -3.9977 | -46.0202 | 2024-10-22 01:25:29 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 521afcc7-4629-3bba-acb6-2fbc1c63e549 | -4.0161 | -46.0416 | 2024-10-22 01:25:29 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 49.4 |
| c2314190-8d85-3cf8-b870-7835275c984e | -4.0163 | -46.0193 | 2024-10-22 01:25:29 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 95.0 |
| 3c233eb1-04dc-33b3-a8cb-6cbefcec72b1 | -4.5572 | -45.8128 | 2024-10-22 01:25:32 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 083ac7c2-d04b-39ab-89b2-bddc620865c8 | -5.2305 | -43.1886 | 2024-10-22 01:25:36 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 64.1 |
| f1564a8b-54b6-3340-a5c0-703570795bd5 | -5.5718 | -44.87 | 2024-10-22 01:25:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 35c84f5d-c3ef-33db-948e-0f8bf369f26c | -5.5903 | -44.8914 | 2024-10-22 01:25:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 80.8 |
| e1867008-9959-33d1-a100-46702706ee1b | -5.5905 | -44.8687 | 2024-10-22 01:25:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 140.2 |
| 0c734ae3-d986-373a-9e51-f16f709a28c9 | -7.8245 | -61.3709 | 2024-10-22 01:25:51 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 1cf7b42c-0cc0-34a3-a5dd-fcb26ddd4040 | -1.1834 | -53.6569 | 2024-10-22 01:35:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| ae7f3c9c-a753-3fee-acf9-62ec981733eb | -2.4639 | -49.1237 | 2024-10-22 01:35:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| da6a917a-62a0-3e4c-9f6f-0d2279820516 | -2.4824 | -49.1233 | 2024-10-22 01:35:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 100.2 |
| 9f7dd3b5-2332-3fd9-bb73-a2832ceb8499 | -2.4824 | -49.102 | 2024-10-22 01:35:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 32da02a4-798d-3a53-9689-e6859a4b57df | -2.5009 | -49.1228 | 2024-10-22 01:35:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 77d15317-6ada-36db-a56e-b0f19b4dc511 | -2.7589 | -49.3072 | 2024-10-22 01:35:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 09ca712e-b12a-3d05-a024-df80afd6df4f | -2.8482 | -45.4637 | 2024-10-22 01:35:22 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 117.9 |
| c17202db-f632-3ebb-9abb-e008f35cf91b | -2.8668 | -45.4631 | 2024-10-22 01:35:22 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 116.1 |
| b426db27-be63-308c-abe6-ed557e1d073a | -3.0765 | -53.239 | 2024-10-22 01:35:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 483470bf-2180-3228-a612-115a95e3eaa4 | -3.0837 | -51.2708 | 2024-10-22 01:35:24 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 2e2fbb67-9f25-3d36-a01f-b463efe978f7 | -3.0838 | -51.25 | 2024-10-22 01:35:24 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 0069e692-4db7-30f2-8683-eccc63b612ef | -3.0917 | -54.1666 | 2024-10-22 01:35:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 85.7 |
| 2c44b812-0cbc-3fc8-81c0-65b23012e3a9 | -3.0918 | -54.1465 | 2024-10-22 01:35:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| cf2c448b-d347-3582-90f9-d7abab7fe3b1 | -3.1101 | -54.1661 | 2024-10-22 01:35:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 97.7 |
| 498b279e-aadb-3f21-af6c-5bb4391a4ea7 | -3.1102 | -54.146 | 2024-10-22 01:35:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 4ebcff2e-27e1-3ba9-9e2e-4147a8bb394a | -3.3384 | -44.0828 | 2024-10-22 01:35:25 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 92d78c53-9a5c-3e7e-8ec0-62ab05622324 | -3.9977 | -46.0202 | 2024-10-22 01:35:29 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 58.5 |
| b5bd2fc1-42fc-373e-8278-cb81cd25400d | -4.0163 | -46.0193 | 2024-10-22 01:35:29 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 52.8 |
| d0096a82-730e-35ad-a45a-8791d664d081 | -4.5572 | -45.8128 | 2024-10-22 01:35:32 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 1bcae8d4-4fb6-3d31-9faa-6ecc2d4772b9 | -4.5574 | -45.7905 | 2024-10-22 01:35:32 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 7ac60278-0426-3d45-afb6-eb12392bf4c0 | -4.5759 | -45.8118 | 2024-10-22 01:35:32 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 312ede30-ba84-3e4d-956a-f5e11e73ae4d | -5.5716 | -44.8927 | 2024-10-22 01:35:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 51.5 |
| 0630233d-d7a6-3d68-b157-c513c77c4672 | -5.5718 | -44.87 | 2024-10-22 01:35:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 4286a514-7122-3417-990c-65094cbd4b1d | -5.5903 | -44.8914 | 2024-10-22 01:35:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 6b1556b5-f968-3971-9119-49d394353561 | -5.5905 | -44.8687 | 2024-10-22 01:35:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 23a0c4c1-d672-3e13-af67-145525e13398 | -19.64988 | -56.9935 | 2024-10-22 01:41:00 | TERRA_M-M | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 139e2c43-90bb-3c63-8cd0-8534bc0e2a58 | -17.26182 | -57.31294 | 2024-10-22 01:41:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.9 |
| 97da92d1-821b-3ba6-8004-e4326ef9109d | -17.26047 | -57.30353 | 2024-10-22 01:41:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 42.4 |
| c1deb66b-ca7c-35ca-8fb4-98950b6559c8 | -17.25912 | -57.29412 | 2024-10-22 01:41:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.1 |
| d7af5675-4bf8-3e16-a749-a66d66290bd6 | -17.25778 | -57.28471 | 2024-10-22 01:41:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 19d3bb27-3c25-3fe2-8742-a2b3f616d1a3 | -17.22962 | -57.27959 | 2024-10-22 01:41:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.0 |
| 9e0d3640-6b4b-31c3-9fe6-b04f0c47a954 | -17.22745 | -57.32805 | 2024-10-22 01:41:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.5 |
| f8798add-9f39-3485-838a-32a32c933b3d | -17.01784 | -57.4696 | 2024-10-22 01:41:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.6 |
| 80b0a37c-a77d-3c14-bad7-03c2ffc65af6 | -17.01545 | -57.52354 | 2024-10-22 01:41:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 14.9 |
| 5e104de9-943c-3ee2-8ceb-0ea3261e2c35 | -17.01412 | -57.51421 | 2024-10-22 01:41:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.4 |
| 0b0a1722-6a1a-3033-8c65-dab4d83301cc | -17.00655 | -57.52495 | 2024-10-22 01:41:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 33.2 |
| 62389c3b-4155-34c0-8568-107262b8ed31 | -16.21721 | -56.59508 | 2024-10-22 01:41:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 20.7 |
| 8fa6b939-ba4a-3dad-a443-c4652bb00a6f | -16.21574 | -56.58509 | 2024-10-22 01:41:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 19.3 |
| 3e840dc8-3e0e-386c-a33c-8294ba95bd07 | -16.09315 | -60.12796 | 2024-10-22 01:41:00 | TERRA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 37.2 |
| c96bb759-9e9e-36da-a8fa-3b399d87c201 | -16.09188 | -60.11812 | 2024-10-22 01:41:00 | TERRA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 8520e018-64ed-3c69-867f-474393c45af5 | -16.08488 | -60.12498 | 2024-10-22 01:41:00 | TERRA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 33.5 |
| 81325717-c4e2-3c96-845e-aeb1a4d61011 | -16.08357 | -60.11515 | 2024-10-22 01:41:00 | TERRA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 69e747c0-4752-314d-bffd-5adbb7c11b37 | -15.9497 | -56.65676 | 2024-10-22 01:41:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 20538107-fafd-3dd1-afbc-72bee89bc8f0 | -15.94824 | -56.64681 | 2024-10-22 01:41:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| bc58fb8a-c99d-3481-a2a0-7384af9e6db3 | -15.83618 | -56.64082 | 2024-10-22 01:41:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |


[Clique aqui para ver as próximas entradas](README10.md)

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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ab762aaf-2907-3591-b3d7-f25693a85656 | -14.3031 | -59.32 | 2024-10-22 00:26:27 | GOES-16 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 222.0 |
| 4f678689-776c-35aa-b235-d68a9bf921df | -14.3218 | -59.3581 | 2024-10-22 00:26:27 | GOES-16 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 7b5819ff-3bab-3cb4-8b71-7ee3ae8ad3cc | -14.322 | -59.3382 | 2024-10-22 00:26:27 | GOES-16 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 303.7 |
| 90590150-977e-382d-b11b-ad36ce1c065c | -14.3223 | -59.3184 | 2024-10-22 00:26:27 | GOES-16 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 167.3 |
| 3f573d4c-a460-3cd4-a25d-f303ec438e63 | -17.0213 | -57.3333 | 2024-10-22 00:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 112.9 |
| b216560f-8c64-347a-be02-f738c1f5913c | -17.257 | -57.3055 | 2024-10-22 00:26:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 70.8 |
| 03c41b53-5f85-3b04-be99-82df509928c7 | -1.165 | -53.6773 | 2024-10-22 00:35:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 0e1bc1c9-5409-343c-8455-1a190c35cd3e | -1.165 | -53.6571 | 2024-10-22 00:35:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 79.8 |
| b3ba3a84-0543-347c-8276-08e277f50593 | -1.1834 | -53.6569 | 2024-10-22 00:35:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| f7dcca45-e454-34dc-9773-d253cef9b63a | -2.7867 | -58.1492 | 2024-10-22 00:35:22 | GOES-16 | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 57e8a61e-51ca-3902-b74a-8962df943ff7 | -2.8482 | -45.4637 | 2024-10-22 00:35:22 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 135.6 |
| 62aa6e4e-9180-35b6-8b5b-23975ccca2b3 | -2.9574 | -50.5245 | 2024-10-22 00:35:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 04afba33-bd78-3674-8d6e-d1a3348beacf | -3.0654 | -51.2506 | 2024-10-22 00:35:24 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| ace26d8e-bd7f-3a11-9269-2cd412db3cf8 | -3.0765 | -53.239 | 2024-10-22 00:35:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 4b318f4e-14be-301f-872b-bd917c4db21b | -3.0837 | -51.2708 | 2024-10-22 00:35:24 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 76.8 |
| b92a6fe9-768d-3638-9d32-0be5a7eed534 | -3.0838 | -51.25 | 2024-10-22 00:35:24 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 85.2 |
| edcb9585-97da-393c-a1c0-9697ed620c00 | -3.0917 | -54.1867 | 2024-10-22 00:35:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| fcb3c1c5-ce73-3789-be4f-abc062302312 | -3.0917 | -54.1666 | 2024-10-22 00:35:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 139.2 |
| 629427c8-ef74-3643-8d4b-049c47376258 | -3.0918 | -54.1465 | 2024-10-22 00:35:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 81.9 |
| edacab6e-161a-3c60-beb1-8524ce980c25 | -3.11 | -54.1862 | 2024-10-22 00:35:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 64d8065f-9a00-378b-ba31-0045bc052d8a | -3.1101 | -54.1661 | 2024-10-22 00:35:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 105.6 |
| 1eac24f1-d2ac-3fc9-b97b-050ecf69d9a7 | -3.1102 | -54.146 | 2024-10-22 00:35:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| ab6e7ad7-0cdc-39b0-a2a3-96357519acf8 | -3.9977 | -46.0202 | 2024-10-22 00:35:29 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 785b9b6c-cb84-3283-a59b-a8ff9c6083c5 | -4.0161 | -46.0416 | 2024-10-22 00:35:29 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 9a25c0c1-d886-3324-9e05-2f1002d83def | -4.0163 | -46.0193 | 2024-10-22 00:35:29 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 95.1 |
| 06fd4ddd-7867-3eab-baa6-6aaf2f4c254e | -4.4655 | -42.9112 | 2024-10-22 00:35:31 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 5c6a212e-33b0-3aaa-897e-753ff62627ca | -4.9513 | -45.4309 | 2024-10-22 00:35:34 | GOES-16 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 12efcb20-8f8f-32d5-ae07-32a44e49b764 | -5.1514 | -46.0911 | 2024-10-22 00:35:35 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 8a89b087-80ba-3dbf-9bfa-9e5f80ae3c1c | -5.2305 | -43.1886 | 2024-10-22 00:35:36 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 73.6 |
| aae30b95-c77b-3cbd-b6a8-ae135ddb3cfc | -5.5905 | -44.8687 | 2024-10-22 00:35:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 65.4 |
| fbda3c51-4c45-359a-a9a8-d3ea7db9cfb2 | -5.9036 | -45.4127 | 2024-10-22 00:35:39 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 646740ff-3163-376c-8d68-3e6f50c86bb8 | -6.2334 | -44.1565 | 2024-10-22 00:35:41 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 3d244956-8fce-357b-bdc7-1246b126a98d | -6.2336 | -44.1335 | 2024-10-22 00:35:41 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 6dbd3d37-dde4-373b-89c4-b6dbcef83228 | -6.2524 | -44.132 | 2024-10-22 00:35:41 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 726f8732-59ae-3565-bd30-0034e221388b | -12.5336 | -63.3003 | 2024-10-22 00:36:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 6b3e8e7a-9c04-3d5d-8f5f-dfc1638b1772 | -14.3029 | -59.3399 | 2024-10-22 00:36:27 | GOES-16 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 197.5 |
| 98e22064-0d10-31bf-8b9d-b38acd312267 | -14.3031 | -59.32 | 2024-10-22 00:36:27 | GOES-16 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 221.7 |
| ebc47f79-8dcb-3c86-b9eb-0c48ef20d079 | -14.322 | -59.3382 | 2024-10-22 00:36:27 | GOES-16 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 175.4 |
| cb132c9f-f974-33eb-80ce-52b2f790bf9a | -14.3223 | -59.3184 | 2024-10-22 00:36:27 | GOES-16 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 126.1 |
| 8b7d72b2-8274-3808-beb3-eae59c7535d8 | -17.0213 | -57.3333 | 2024-10-22 00:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 93.6 |
| 698a7112-0b60-3523-8ca2-616e43cbeb8d | -17.257 | -57.3055 | 2024-10-22 00:36:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 72.1 |
| 968245d9-46cd-3ab3-9ecb-f65bcf0d9dcd | -1.165 | -53.6571 | 2024-10-22 00:45:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 8e4112e4-b33d-3019-a37b-033801cf4803 | -1.1834 | -53.6569 | 2024-10-22 00:45:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 6e65d29c-23a0-3d0c-bdba-fa9c8c887ca3 | -1.9849 | -48.6865 | 2024-10-22 00:45:17 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 9eb276e9-c870-3365-ab01-13f8023b18f0 | -2.4824 | -49.1233 | 2024-10-22 00:45:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 33a2f83f-90a3-3c74-af8b-ff1925fc4c2f | -2.4824 | -49.102 | 2024-10-22 00:45:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 0c49e63f-2976-3769-8ca0-cd1e6cde9f21 | -2.7867 | -58.1492 | 2024-10-22 00:45:22 | GOES-16 | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 5c39e25f-3baf-360a-ba47-c3cca55f1903 | -2.8069 | -51.3613 | 2024-10-22 00:45:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 5678ed35-2fbb-3689-a1d9-0e4fffa6d524 | -2.8482 | -45.4637 | 2024-10-22 00:45:22 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 116.4 |
| 26eb41e6-0534-35ee-8dfa-19172242f7c0 | -2.9574 | -50.5245 | 2024-10-22 00:45:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 28578f46-aef9-36ab-9e8d-648a3658e18f | -3.0654 | -51.2506 | 2024-10-22 00:45:24 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 3e861cf7-d318-3c4d-87d6-1aa46d4832d6 | -3.0837 | -51.2708 | 2024-10-22 00:45:24 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 0d30d7cd-26bb-3cac-8dfa-128f4b062ced | -3.0838 | -51.25 | 2024-10-22 00:45:24 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 1d827f73-19a3-3da6-b2c3-a8030171f519 | -3.0917 | -54.1867 | 2024-10-22 00:45:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| fb99c3e5-c4fd-3848-9a33-00df7ffb7310 | -3.0917 | -54.1666 | 2024-10-22 00:45:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 134.9 |
| c317db88-f4e3-3269-9c57-a82bc25bb306 | -3.0918 | -54.1465 | 2024-10-22 00:45:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 28ccabf5-84cb-37ed-910e-1200d693a121 | -3.1101 | -54.1661 | 2024-10-22 00:45:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 91.1 |
| 5fe03345-a35c-3a22-a772-7560f5ab6e90 | -3.1102 | -54.146 | 2024-10-22 00:45:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| e86429ae-a591-38ad-a4d6-fccc696b48af | -3.9977 | -46.0202 | 2024-10-22 00:45:29 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 80.0 |
| b1dab0f2-45bf-31d7-9b67-a4f5850da0d8 | -4.0161 | -46.0416 | 2024-10-22 00:45:29 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 4dc31b9d-fe9d-3352-9d52-095246c0c04c | -4.0163 | -46.0193 | 2024-10-22 00:45:29 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 125.9 |
| dc6d1c08-c23c-3e4a-969c-b307f1998024 | -5.2305 | -43.1886 | 2024-10-22 00:45:36 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 60.2 |
| daaf2ad6-0dc7-3532-a5fe-5a7adffdb40d | -5.5718 | -44.87 | 2024-10-22 00:45:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 9983c477-4363-3d76-9cef-f576698775a0 | -5.5903 | -44.8914 | 2024-10-22 00:45:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 53.9 |
| 1d391c09-3ff2-33a2-ac1a-966a4d383f4d | -5.5905 | -44.8687 | 2024-10-22 00:45:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 95764bbd-56b6-3270-a841-a2a36985882e | -5.9036 | -45.4127 | 2024-10-22 00:45:39 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 63.2 |
| b29483fd-77d6-3bd2-9b56-99228006f18a | -6.2334 | -44.1565 | 2024-10-22 00:45:41 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 3b4ede25-e9df-3892-a3c4-b9ffd13926b2 | -6.2336 | -44.1335 | 2024-10-22 00:45:41 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 9aa0c4b7-205f-3782-b091-568784ae635d | -6.2522 | -44.155 | 2024-10-22 00:45:41 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 47.8 |
| 35cd5287-cc5e-3b05-8749-45e5c95cec5b | -6.2524 | -44.132 | 2024-10-22 00:45:41 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 75bdb36f-6391-3865-b44f-511278c9a479 | -7.8245 | -61.3709 | 2024-10-22 00:45:51 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 20e4fef6-283c-35e4-a26d-f1cf13a8708a | -12.4778 | -63.1885 | 2024-10-22 00:46:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 7d999c53-e35e-3aa9-9dfc-1f977f06e16a | -12.5167 | -63.0521 | 2024-10-22 00:46:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 62.9 |
| b0751c0c-6140-3624-a7e6-3ce9b12dcb9c | -12.5336 | -63.3003 | 2024-10-22 00:46:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 869fc753-7b73-3012-a4b2-3e4ef8e32058 | -14.3218 | -59.3581 | 2024-10-22 00:46:27 | GOES-16 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 70.0 |
| f6b7283b-678c-3f86-a5f4-c46e57dbc230 | -14.322 | -59.3382 | 2024-10-22 00:46:27 | GOES-16 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 1f3da035-1372-325d-89f0-22acdd48fcca | -17.0213 | -57.3333 | 2024-10-22 00:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 100.6 |
| 2b5ca8f0-831a-375c-8f4a-74226faea325 | -1.165 | -53.6571 | 2024-10-22 00:55:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 82979689-4265-318a-a19d-0100ff2e9198 | -1.1834 | -53.6569 | 2024-10-22 00:55:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 17750006-094d-3e2e-a155-fafc121ee099 | -2.7588 | -49.3285 | 2024-10-22 00:55:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 158.2 |
| 77b36966-7e9f-33cc-8c4b-8ea28a234851 | -2.7589 | -49.3072 | 2024-10-22 00:55:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 201.3 |
| c594be07-0b8e-3995-9197-f09c28b72bbe | -2.7589 | -49.286 | 2024-10-22 00:55:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 4064c44b-e1f4-3164-91d1-a1e1592337cf | -2.7773 | -49.3279 | 2024-10-22 00:55:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| c16a08f0-18ac-3512-8378-35661130e530 | -2.7773 | -49.3067 | 2024-10-22 00:55:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 101.0 |
| 0526813c-dcec-3f6d-8066-a48fa25a0162 | -2.7774 | -49.2854 | 2024-10-22 00:55:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| dec6b163-897b-3cfd-aa73-ec60c0ee2ec5 | -2.8482 | -45.4637 | 2024-10-22 00:55:22 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 98.0 |
| d1207b81-1e20-3107-b506-405cb4e5cdcb | -2.8668 | -45.4631 | 2024-10-22 00:55:22 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 103.1 |
| 51721769-96fc-375d-a472-3f9c2e5a9f28 | -2.9574 | -50.5245 | 2024-10-22 00:55:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 71.2 |
| a557226d-cb3e-3bb4-b268-e0c68713e24f | -3.0581 | -53.2395 | 2024-10-22 00:55:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 1d5e0cdb-2f6c-375e-a90d-9f5e51c0d896 | -3.0765 | -53.2593 | 2024-10-22 00:55:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 042e0093-53c6-3e18-b687-a4b53f41c476 | -3.0765 | -53.239 | 2024-10-22 00:55:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 664d0bcb-2d90-338d-87f7-4440429e407d | -3.0837 | -51.2708 | 2024-10-22 00:55:24 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| b6ece323-8b0b-394e-a720-8e97c8e67304 | -3.0838 | -51.25 | 2024-10-22 00:55:24 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 84.5 |
| 2f761b26-4bf9-3818-9771-2fd186f1f6ea | -3.0917 | -54.1867 | 2024-10-22 00:55:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 5b99143a-52ee-32ca-b0a6-ef3fc7d77b89 | -3.0917 | -54.1666 | 2024-10-22 00:55:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 111.6 |
| 7f74f0d4-14a9-35fa-a2d1-d7476b536427 | -3.0918 | -54.1465 | 2024-10-22 00:55:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 624d0507-feae-316e-b9cf-5a958bb9376e | -3.11 | -54.1862 | 2024-10-22 00:55:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 38a63dfc-cccc-3ff0-9eff-06dfbbe2e3c7 | -3.1101 | -54.1661 | 2024-10-22 00:55:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 119.8 |
| e50d38d3-6449-3b67-9b5c-132301eabfd1 | -3.1102 | -54.146 | 2024-10-22 00:55:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| c096e1a7-1b76-3ba1-8a89-692b2908d4bd | -3.9975 | -46.0425 | 2024-10-22 00:55:29 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 72.0 |


[Clique aqui para ver as próximas entradas](README7.md)

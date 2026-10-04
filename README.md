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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c30f0258-358b-38cb-9fb3-4bf60743cc20 | -14.5877 | -52.8789 | 2026-10-04 00:00:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 1d16ba74-99bc-34dd-bc6f-171724a62468 | -2.798 | -54.0933 | 2026-10-04 00:00:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| c056f858-0ff0-323a-9f21-8c92ef018c8b | -3.8848 | -49.6933 | 2026-10-04 00:00:00 | GOES-19 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 28436617-8717-37f4-b406-a65e93d87285 | -4.2887 | -50.2675 | 2026-10-04 00:00:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 133.4 |
| 9ae9767f-da43-34ce-aa49-e6f7a8d9cc94 | -3.1116 | -53.7436 | 2026-10-04 00:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 328.5 |
| 94254ab7-a6f8-347b-abf0-46be9d5e3912 | -3.4762 | -50.0883 | 2026-10-04 00:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 163.3 |
| 19be8256-de01-306c-b2d2-0924ae3c5404 | -4.2745 | -46.3624 | 2026-10-04 00:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 186.6 |
| 2e352f50-95f7-32fc-b0f0-69c1c42f8817 | -3.0548 | -54.2277 | 2026-10-04 00:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 76119b41-5ffc-3581-ba4b-9a199b70bff2 | -3.0364 | -54.2282 | 2026-10-04 00:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 99.9 |
| c19967cc-0789-3447-8bdb-c3efc1303516 | -4.2558 | -46.3855 | 2026-10-04 00:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 101.7 |
| 046f6118-db88-39ae-9101-cd7ba4c24441 | -3.8756 | -55.8184 | 2026-10-04 00:00:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 90.0 |
| 6be85a7e-f138-3e4c-9a84-cad3c72d9f4a | -3.072 | -49.5525 | 2026-10-04 00:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 86.9 |
| df1b4f83-eb05-3abf-9f1e-b9083fbbc2f4 | -4.4845 | -45.5478 | 2026-10-04 00:00:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 117.7 |
| c73ff7d4-0a93-38ff-a049-66f8e724ce74 | -2.9817 | -54.089 | 2026-10-04 00:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 6efc16b1-4303-3aab-8672-f9a920f31618 | -9.9175 | -65.0313 | 2026-10-04 00:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 57.4 |
| bc62b7b7-2213-3241-ae44-0b5538af7364 | -1.0911 | -54.1001 | 2026-10-04 00:00:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| f743748a-0c08-394c-9c84-5c214f2c5660 | -3.1839 | -54.0839 | 2026-10-04 00:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 9a78196f-27ac-3883-b3d9-2c202f8ef549 | -9.1332 | -65.9559 | 2026-10-04 00:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 52365ecf-8bbc-3a7b-adce-13b207aac8b9 | -3.13 | -53.7229 | 2026-10-04 00:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 174.5 |
| 19699607-c044-35ad-9876-89a8c55c89f1 | -3.055 | -54.1675 | 2026-10-04 00:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 4e6101de-da75-378b-9707-47f0bdc9b63e | -4.4847 | -45.5253 | 2026-10-04 00:00:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 90.7 |
| 29c93a63-0388-3e56-a2bf-09d0121d1124 | -3.1299 | -53.7431 | 2026-10-04 00:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 142.3 |
| 6f0c0db0-7617-3e8b-b243-07119785e04e | -8.593 | -66.8081 | 2026-10-04 00:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 70.4 |
| a72d4d6e-04e2-3061-a0a7-f59bc9cbc2e1 | -1.0911 | -54.1202 | 2026-10-04 00:00:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| d1d1be4e-3c38-3397-a13e-75814d37041b | -3.4577 | -50.089 | 2026-10-04 00:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 74.1 |
| fe4a99c3-3e2a-3664-8c96-2f9ec107e797 | -3.1116 | -53.7234 | 2026-10-04 00:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 294.8 |
| 0540bb9e-2d46-3669-8d26-c50b7b618d62 | -3.5128 | -54.6162 | 2026-10-04 00:00:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| cd28ecb0-8592-3b21-8538-2aa91c763752 | -4.2559 | -46.3633 | 2026-10-04 00:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 195.5 |
| b8c29c05-b71b-39fc-8dc3-4bbe714d8f0a | -3.0721 | -49.5313 | 2026-10-04 00:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 105.1 |
| 98c5ee94-7660-3562-bb99-8d28b5348197 | -3.4761 | -50.1094 | 2026-10-04 00:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 88.8 |
| c79ee719-fd37-33dc-9398-06d7575a25b3 | -4.2744 | -46.3846 | 2026-10-04 00:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 94.5 |
| c635d8e7-6ccd-39d7-8c99-dd6f4f5356f8 | -9.0857 | -61.1629 | 2026-10-04 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 805b1abd-f01b-3563-a871-b58b6adcf530 | -2.8163 | -54.133 | 2026-10-04 00:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 109.9 |
| 008b0867-3e60-3303-ab5b-49a1a4b12a12 | -2.2113 | -53.7029 | 2026-10-04 00:00:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 171a6002-3c17-3053-b436-ce7df4d22c8c | -2.8163 | -54.1129 | 2026-10-04 00:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 143.0 |
| 4c824022-282e-3013-95e1-1a82d8a6140c | -15.9255 | -56.3336 | 2026-10-04 00:00:00 | GOES-19 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 33.1 |
| 13c5423d-3ada-3679-a04d-07e6a455509c | -14.5683 | -52.8814 | 2026-10-04 00:00:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 38f57ad3-b56c-3a8a-b87c-5471a46a0537 | -3.1115 | -53.7637 | 2026-10-04 00:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 90.3 |
| db900a2b-06b2-3626-9d8c-565a75d45cc0 | -8.3526 | -62.8302 | 2026-10-04 00:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 68d63ddd-2387-3997-8536-de93c79cc037 | -3.0365 | -54.2081 | 2026-10-04 00:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 90128782-a5db-3e64-a6b3-dd68a13877a1 | -9.899 | -65.0132 | 2026-10-04 00:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 62.0 |
| ce7cedad-f481-3187-b237-79074d8034bc | -2.7979 | -54.1134 | 2026-10-04 00:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 94.9 |
| fdd763c0-6576-3edb-a470-87d0b9913232 | -3.8757 | -55.7986 | 2026-10-04 00:00:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 32750017-c4ce-3ef4-bb0e-30a6b1b84724 | -2.8164 | -54.0929 | 2026-10-04 00:00:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 5e861e69-6701-3885-b48c-1c77995af62b | -2.2297 | -53.7026 | 2026-10-04 00:00:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 03758c37-6479-31ae-ba4a-bdbfb7c6c21c | -1.4873 | -49.4725 | 2026-10-04 00:09:00 | METOP-B | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 10436473-ac37-3c66-adc8-a3957b1734ad | -2.9216 | -54.1497 | 2026-10-04 00:09:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 789f595f-35d8-3398-96a1-310d55d1e007 | -6.5634 | -44.146599 | 2026-10-04 00:09:00 | METOP-B | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 267ba886-c2ce-39c0-b043-18a5a11c43c1 | -1.0916 | -54.1077 | 2026-10-04 00:09:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7d2e250b-426f-34b8-9423-d1580c37ff09 | -4.1463 | -49.696098 | 2026-10-04 00:09:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 08d53fbf-60f7-344f-af7e-55b2ff53d9f6 | -15.2337 | -40.518101 | 2026-10-04 00:09:00 | METOP-B | ITAMBÉ | BAHIA | Brasil | 2915809 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 49c0ea63-ef2a-3440-9462-b35f2d8593d0 | -2.812 | -54.119099 | 2026-10-04 00:09:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 865fd307-19d9-3b11-9cb6-cf884775afb2 | -3.0035 | -53.871399 | 2026-10-04 00:09:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a3213d09-8cbf-3c7b-8e16-bf49ef07055e | -6.0009 | -53.5354 | 2026-10-04 00:09:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c262b711-4776-3067-b1de-546d541aafbe | -2.9688 | -53.2556 | 2026-10-04 00:09:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bd044bf8-ec2b-3a5c-845a-88b3e22b3fb3 | -2.212 | -53.6898 | 2026-10-04 00:09:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 268bc25e-6759-3f7f-9bf5-d6468a582d08 | -7.7548 | -49.196201 | 2026-10-04 00:09:00 | METOP-B | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 488e019d-b6d8-38c7-9767-b56b6c235c17 | -4.1094 | -53.621101 | 2026-10-04 00:09:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 35a23d89-ecba-3fba-b680-afcf3dc3395d | -3.7034 | -50.6549 | 2026-10-04 00:09:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c96e1952-aa46-3acd-abfa-4c7dff0e3809 | -7.2813 | -49.245098 | 2026-10-04 00:09:00 | METOP-B | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 951d6d57-c348-33f1-9736-6f1ebaedf91a | -3.1922 | -54.072399 | 2026-10-04 00:09:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e44ad85a-50cd-3fc6-96cf-53b443d120c8 | 1.763 | -55.635201 | 2026-10-04 00:09:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e70ace70-b832-3c8d-8f5a-8a12e3f3edb1 | -3.4599 | -50.0793 | 2026-10-04 00:09:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5568ac84-62ca-3ee7-bd68-37fcbf3fe587 | -6.0679 | -53.465801 | 2026-10-04 00:09:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0747e86b-2070-376b-ab80-7cb316e78316 | -0.4949 | -49.096001 | 2026-10-04 00:09:00 | METOP-B | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d7ebbd48-94ca-388b-8ca2-f7274afc545b | -2.2482 | -51.926102 | 2026-10-04 00:09:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 319af96b-6b52-3b8a-afa5-5d80c137533b | -2.8883 | -54.138699 | 2026-10-04 00:09:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0979e9eb-fcef-3c9c-8a7c-a421f7317d42 | -3.1701 | -50.530201 | 2026-10-04 00:09:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eef13e49-ac87-3e21-bc30-c5a22acf88fa | -1.4775 | -49.474701 | 2026-10-04 00:09:00 | METOP-B | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 66292541-5f29-3564-a86c-6f773bb8f001 | -4.135 | -54.154301 | 2026-10-04 00:09:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a0a18d7c-a5ad-38a2-9c04-1f5e7bb56a1c | -4.2844 | -50.260799 | 2026-10-04 00:09:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fecf6aba-edc7-30ee-bf4c-21d265b5a37e | -3.0645 | -49.517601 | 2026-10-04 00:09:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d8afbdb5-ff69-3f95-919d-65c70647c27f | -2.9472 | -54.1259 | 2026-10-04 00:09:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 168866de-5283-350e-8170-7a26a8236b98 | -2.7675 | -57.657101 | 2026-10-04 00:09:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0d5c0ce1-c275-35cc-98c8-3bb2802ea2c5 | -5.5681 | -49.737701 | 2026-10-04 00:09:00 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 63adac7e-ad90-32e9-affc-eb37b4463ef8 | -3.7049 | -50.661701 | 2026-10-04 00:09:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 24153b27-db8d-3b9f-8342-944947e90ad3 | -2.7847 | -54.088902 | 2026-10-04 00:09:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0f6e8866-80ae-3fcf-bcef-12b44a987cbc | -3.3155 | -54.1646 | 2026-10-04 00:09:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c2e0dace-d6ab-3deb-9b4e-250aad2aa023 | -6.0069 | -53.515701 | 2026-10-04 00:09:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 67291bbf-07da-3ddb-a3f4-faeedef082b5 | -3.1361 | -53.728199 | 2026-10-04 00:09:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a6d93d88-75c9-39a0-a69a-cf322a112569 | -4.4438 | -49.917198 | 2026-10-04 00:09:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e10c24f1-8428-3b23-9506-f1c1e30149f6 | -3.1706 | -54.068001 | 2026-10-04 00:09:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 93373d73-ff76-31a7-a2b7-80e4bb287679 | -2.8231 | -50.500099 | 2026-10-04 00:09:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7b7ba61b-c1c1-3182-9457-159254588f1d | -1.4759 | -49.467602 | 2026-10-04 00:09:00 | METOP-B | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b76ccfae-eb02-3e46-8fb8-834b3433e4f8 | -2.4465 | -50.247601 | 2026-10-04 00:09:00 | METOP-B | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d95e0a41-565f-3778-ae44-df8c933d823a | -6.0561 | -53.459202 | 2026-10-04 00:09:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a0966e3e-ea0d-30bb-9d46-386c9ca7b1a4 | -2.5721 | -51.854599 | 2026-10-04 00:09:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b5655465-c4d8-3ef5-b049-0ba2cdbcfe71 | -4.2071 | -53.4594 | 2026-10-04 00:09:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8694754c-8bf1-3a48-b1e9-fbab1ed9ac18 | -3.1225 | -53.713699 | 2026-10-04 00:09:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 91f398c0-3676-387f-a1d6-c4cd47bfe548 | -5.999 | -53.5266 | 2026-10-04 00:09:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f294c4d2-2a3b-3062-ab39-25ba5834fec8 | 2.1033 | -50.732201 | 2026-10-04 00:09:00 | METOP-B | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| bf2fbb43-f118-3e9b-8bae-7b7a72bd7bb5 | -5.2902 | -49.1936 | 2026-10-04 00:09:00 | METOP-B | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1f451c2a-6ed1-3d62-abcc-c050fc98f9e3 | -5.7378 | -45.144699 | 2026-10-04 00:09:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 729d4b19-b1b9-3301-adcc-bc2c8924f529 | 1.7686 | -55.6558 | 2026-10-04 00:09:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b7f2fda6-a7a3-33a5-bf05-a3297c31e626 | -4.4628 | -50.9617 | 2026-10-04 00:09:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5e4f5743-6c29-38ae-959b-159ba5004633 | -4.5281 | -49.697201 | 2026-10-04 00:09:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8e988c79-5a18-3a51-ae6c-14b6a32b7ca8 | -2.9295 | -54.138901 | 2026-10-04 00:09:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e39983a9-b1a7-367b-959b-6e1d715c6a43 | -2.0577 | -56.8577 | 2026-10-04 00:09:00 | METOP-B | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 962bc830-d389-3be6-a978-abe21306b29e | -1.1593 | -49.253601 | 2026-10-04 00:09:00 | METOP-B | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c5d6f424-4d3b-336b-b5cb-5c755cda685f | -2.0479 | -56.859901 | 2026-10-04 00:09:00 | METOP-B | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README2.md)

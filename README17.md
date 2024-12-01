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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| da5ff31d-32fd-3ffa-8f77-077498febeb9 | -6.9156 | -43.5418 | 2024-12-01 01:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 188.1 |
| e59f2853-d2b6-3ce4-8414-6913b3b68d0c | -3.1273 | -54.5264 | 2024-12-01 01:30:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 112.3 |
| c24e366a-cd1e-3840-b522-fc4111e18447 | -1.7139 | -46.1422 | 2024-12-01 01:30:00 | GOES-16 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 210.0 |
| 842bbe57-ec76-3bc7-b4e5-7bc0d6c06510 | -3.5158 | -53.8333 | 2024-12-01 01:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 127d9f88-b4b1-3575-b1fc-252004867f8f | -3.259 | -53.6388 | 2024-12-01 01:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 145.1 |
| b21c8f1f-9285-3af8-8711-d96d29316ca5 | -3.2774 | -53.6383 | 2024-12-01 01:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 83.0 |
| dc5eeb23-f4df-3a96-9cdb-0d617bba4741 | -3.4569 | -50.2782 | 2024-12-01 01:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 74a4ed6e-ef7c-32e5-b952-2ee43851c833 | -3.4755 | -50.2566 | 2024-12-01 01:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 38ffef50-a674-330a-b5e6-435c7e048e22 | -2.8196 | -53.0629 | 2024-12-01 01:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 40e913e2-5b53-3955-bf23-896a20f6c29b | -6.9341 | -43.5634 | 2024-12-01 01:40:00 | GOES-16 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 22bb4fcc-92a2-3322-b082-1a54c01d20c4 | -3.69 | -51.8101 | 2024-12-01 01:40:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 102f1f01-acfa-3eb7-a254-e02a4241a3a4 | -1.7139 | -46.1644 | 2024-12-01 01:40:00 | GOES-16 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 8e626c39-020a-3c86-bfcb-930d89b0a502 | -3.2725 | -50.2003 | 2024-12-01 01:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 168cd481-0034-35b4-8028-23b6ee9c7eb4 | -3.5158 | -53.8333 | 2024-12-01 01:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 88.5 |
| aeb41f5e-92dc-352d-8c05-930bbad9f474 | -1.6954 | -46.1426 | 2024-12-01 01:40:00 | GOES-16 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 120.2 |
| c899dbd0-d2bc-386e-86b1-3a81983d599e | -3.0081 | -51.7897 | 2024-12-01 01:40:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 85.0 |
| 79a4ec3f-9d3b-3dba-afa7-fac93efa6afd | -3.2591 | -53.6186 | 2024-12-01 01:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 94.1 |
| 7cb27267-bd24-36b7-b4c5-ec6567c9e0b4 | -4.558 | -45.7008 | 2024-12-01 01:40:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 128d7472-914f-3ce5-ab6e-ff991cc46c4b | -3.4569 | -50.2782 | 2024-12-01 01:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| eca8cdf8-4077-3fe9-bf76-72b77706e559 | -3.2057 | -53.1341 | 2024-12-01 01:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| baf318ff-14e8-3953-9b37-2d1123859dab | -2.5319 | -45.6086 | 2024-12-01 01:40:00 | GOES-16 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 87.7 |
| f181eb9d-939d-39e1-8039-356632c8c2a4 | -1.7139 | -46.1422 | 2024-12-01 01:40:00 | GOES-16 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 106.0 |
| e157ecd0-9700-31f4-9077-093ba3d33209 | -1.6953 | -46.1648 | 2024-12-01 01:40:00 | GOES-16 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 74692bb7-0c34-30eb-8f35-93fa64849a60 | -6.9344 | -43.5401 | 2024-12-01 01:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 210.2 |
| ea51f8b1-6e8c-3a84-b9ad-236382a5f82a | -2.8197 | -53.0425 | 2024-12-01 01:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 74.3 |
| b81b4014-6977-3019-9862-01bcc53b0a2e | -3.4974 | -53.8339 | 2024-12-01 01:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 99.0 |
| 14048699-2c55-3cdb-9f80-29d02f657b63 | -2.5504 | -45.6304 | 2024-12-01 01:40:00 | GOES-16 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 195.2 |
| bcf7ab59-06b5-3931-8918-f65d2c8776cb | -3.4754 | -50.2776 | 2024-12-01 01:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 58c56960-45c0-3c64-ba56-015771f5a8ef | -3.259 | -53.6388 | 2024-12-01 01:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 126.0 |
| ce0f96f8-3949-3e4b-ae32-a69fcd5d115a | -4.5578 | -45.7232 | 2024-12-01 01:40:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 156.2 |
| 005ba4d1-1353-3923-8da5-78d2105f453a | -4.5375 | -43.304 | 2024-12-01 01:40:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 60.5 |
| bae4b3c2-1c38-3adb-ae80-e1ebf308423d | -2.5504 | -45.608 | 2024-12-01 01:40:00 | GOES-16 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 314.6 |
| 6cb86d6f-7aac-3e95-950a-d66895fb7396 | -4.5562 | -43.3028 | 2024-12-01 01:40:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 177.2 |
| 7e6e25bf-555b-34bd-91b0-999c5c2092ac | -4.5394 | -45.7019 | 2024-12-01 01:40:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 108.2 |
| a37fa8d1-15f4-3e53-9be7-0fb0e45ae7c0 | -2.6579 | -51.8606 | 2024-12-01 01:40:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 0419c5d8-4fda-3e86-a803-dd3d876b32c1 | -6.9156 | -43.5418 | 2024-12-01 01:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 167.7 |
| 805a44cb-3bbd-31f4-88e1-c81093a2c240 | -3.1456 | -54.5259 | 2024-12-01 01:40:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 6f940cab-a2b2-36d7-ae3b-b04f3360aaa2 | -4.5563 | -43.2795 | 2024-12-01 01:40:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 2a1d6979-bf20-373f-9bc8-570e3f926c4d | -3.1273 | -54.5264 | 2024-12-01 01:40:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 84.2 |
| d851f0a8-5a1c-3104-bc7a-4133322df9d3 | -2.6578 | -51.8811 | 2024-12-01 01:40:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 410e3186-ae97-321d-97d5-8f896a4bba6a | -2.5318 | -45.631 | 2024-12-01 01:40:00 | GOES-16 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 0cdd8762-ca7a-3aee-8288-f3c93ac7d907 | -3.2774 | -53.6383 | 2024-12-01 01:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 96.7 |
| facebe79-e58f-3f4d-b152-7b3039649735 | -1.7139 | -46.1422 | 2024-12-01 01:50:00 | GOES-16 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 107.5 |
| d052bb7f-642f-3dae-b27a-b6b582e61b78 | -4.558 | -45.7008 | 2024-12-01 01:50:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 73.1 |
| ce05ce3a-dcb6-350d-a980-3d01d99aad05 | -3.3134 | -53.8592 | 2024-12-01 01:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 66ae5321-0e26-38ee-a0ef-dcffb3d53a16 | -3.1273 | -54.5264 | 2024-12-01 01:50:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 102.3 |
| cef6fd88-883a-3766-8531-85e7ef987da8 | -6.9156 | -43.5418 | 2024-12-01 01:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 168.4 |
| 9e65a540-7901-30b4-8dde-fbbbf9e2feec | -3.4755 | -50.2566 | 2024-12-01 01:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 10de5e9f-657e-32d7-aef6-f52645641279 | -4.5375 | -43.304 | 2024-12-01 01:50:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 656f80a4-4da2-33e4-840b-7b01e375a551 | -3.4974 | -53.8339 | 2024-12-01 01:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 122.4 |
| e80b9644-edd9-3f09-be67-47f343df01ad | -2.6578 | -51.8811 | 2024-12-01 01:50:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 0912ade9-363d-34fa-b9f5-b7e93d410436 | -2.8012 | -53.0633 | 2024-12-01 01:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 3a190ec1-35d0-31b9-a82f-c054f7e402df | -2.7503 | -51.7553 | 2024-12-01 01:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 61559c8d-0bdd-3792-a5ef-62b4ce12f88a | -3.4754 | -50.2776 | 2024-12-01 01:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 261a9d23-e705-3d8c-82fb-0291b882b202 | -4.5562 | -43.3028 | 2024-12-01 01:50:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 201.0 |
| dd2bb70c-bdc4-3d2b-b04a-bce48ed3aa70 | -2.8013 | -53.043 | 2024-12-01 01:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| ec5f0e1a-5e2d-3406-86ec-b880636db203 | -2.5504 | -45.608 | 2024-12-01 01:50:00 | GOES-16 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 164.9 |
| 5532b03b-d174-3f85-81f1-6dc21cd8c0ee | -2.6579 | -51.8606 | 2024-12-01 01:50:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 7cbbca9d-dcd6-3d8d-890e-7efb8bca75a7 | -4.5578 | -45.7232 | 2024-12-01 01:50:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 115.3 |
| 379a7b29-a5a0-341d-b598-04185e7d0493 | -1.6954 | -46.1426 | 2024-12-01 01:50:00 | GOES-16 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 6c58d3bc-a8a2-3323-aea8-a9b93b778107 | -2.9778 | -45.5713 | 2024-12-01 01:50:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 62.4 |
| dcb7a996-7ef2-3dcc-ace2-317dc646499e | -4.556 | -43.3261 | 2024-12-01 01:50:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 64.1 |
| d65fe5aa-457f-33e3-baf0-6adcd97e9b12 | -3.2591 | -53.6186 | 2024-12-01 01:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 91.9 |
| 78b8b2b0-7571-359a-9bcc-2e8e3108d7a2 | -1.7139 | -46.1644 | 2024-12-01 01:50:00 | GOES-16 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 75.6 |
| fc555e32-d4d3-36f0-ae48-9bd1fb499cfa | -3.0081 | -51.7897 | 2024-12-01 01:50:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| ace8166c-c1af-3f35-a7c5-6cdf68e6df53 | -4.5394 | -45.7019 | 2024-12-01 01:50:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 88.8 |
| cd5a6e65-ae1a-33dd-9473-b52448ed2060 | -3.0265 | -51.7892 | 2024-12-01 01:50:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 71ad5f16-1c5f-3499-907e-9efea80ff89c | -3.259 | -53.6388 | 2024-12-01 01:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 145.5 |
| 3bff6254-04c8-341c-b428-88f6b8121f6b | -2.9043 | -45.3719 | 2024-12-01 01:50:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 76.3 |
| c332a5fd-de42-3490-8a0c-6572789b9488 | -3.2774 | -53.6383 | 2024-12-01 01:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 1852467e-c4cf-3b48-9d27-4bcda098e4c3 | -3.1456 | -54.5259 | 2024-12-01 01:50:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 133dc303-7b58-3d3b-8bb1-d9ba2ab0edd4 | -2.8197 | -53.0425 | 2024-12-01 01:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| ba6b619b-ba04-3d1a-9189-06134abb5693 | -2.5504 | -45.6304 | 2024-12-01 01:50:00 | GOES-16 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 87.4 |
| 21c310f2-aa3e-3322-801f-23e6d5e9cc70 | -6.9344 | -43.5401 | 2024-12-01 01:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 151.6 |
| 0af4d864-68c0-3046-b211-1d5efd9b8259 | -3.5158 | -53.8333 | 2024-12-01 01:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| c6fe7a33-a528-3ac7-a0b7-26f00a0dff2a | -10.6674 | -44.4835 | 2024-12-01 02:00:00 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 08a18888-0e50-3808-ba0e-c892b4854507 | -3.1272 | -54.5464 | 2024-12-01 02:00:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 03b3ad1d-ee32-35c2-ba9b-adbb6cf505ec | -3.4754 | -50.2776 | 2024-12-01 02:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 1701b217-8a21-369f-aa2a-7a6fe2363b5c | -2.5504 | -45.608 | 2024-12-01 02:00:00 | GOES-16 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 90.5 |
| 10edb6a8-8922-3ca9-9389-c258bf6c03e7 | -1.7139 | -46.1644 | 2024-12-01 02:00:00 | GOES-16 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 61.6 |
| c3968b17-93d5-3b1a-8c62-207858108de3 | 1.1622 | -55.9869 | 2024-12-01 02:00:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 50.4 |
| d218d6df-fa4c-3352-ad5b-87ea8b438aca | -3.259 | -53.6388 | 2024-12-01 02:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 137.5 |
| 5c0cc381-8066-3cc1-b359-a9ef66814981 | -6.9344 | -43.5401 | 2024-12-01 02:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 139.6 |
| 17d4cef9-d646-3561-884e-585ad5fcbb72 | -1.7139 | -46.1422 | 2024-12-01 02:00:00 | GOES-16 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 83.6 |
| df13fda8-86dc-3d24-82b6-0e6e017099b4 | 1.1622 | -55.9672 | 2024-12-01 02:00:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| d7bce1fd-6d0f-3342-8f32-dfb8c4368e6c | -4.5394 | -45.7019 | 2024-12-01 02:00:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 82.5 |
| 822720e1-54cc-3708-98c8-84868eb8e8e7 | -9.7592 | -36.1822 | 2024-12-01 02:00:00 | GOES-16 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 79.5 |
| 0aaf99e4-fdde-39cb-bbe8-8d358fc35f56 | -2.3311 | -44.6219 | 2024-12-01 02:00:00 | GOES-16 | ALCÂNTARA | MARANHÃO | Brasil | 2100204 | 21 | 33 | nan | nan | nan | Amazônia | 86.7 |
| 8bcd6cb6-f42a-3cda-a019-52a4abbc08e7 | -4.558 | -45.7008 | 2024-12-01 02:00:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 260bf13b-cff8-3a00-a312-1401162b47ac | -4.5375 | -43.304 | 2024-12-01 02:00:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 88.4 |
| d5b12bf4-e581-3cee-b4d7-e62276855a1b | -3.4974 | -53.8339 | 2024-12-01 02:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 103.6 |
| c348afe4-78ef-3afc-b09e-9781f692fc5e | -2.8013 | -53.043 | 2024-12-01 02:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 5a3ceb71-36c4-3e4b-a067-b6c44700e4d0 | -2.7503 | -51.7553 | 2024-12-01 02:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 80.3 |
| 0dda8368-819e-3100-9822-f56db5c079dc | -2.8197 | -53.0425 | 2024-12-01 02:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| c68e890d-7435-3f41-b157-b0b759ce8b05 | -2.9043 | -45.3719 | 2024-12-01 02:00:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 1730bd93-33ae-3d7d-9e83-1531a5a32fa1 | -6.9156 | -43.5418 | 2024-12-01 02:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 150.8 |
| ffcd78a6-10b9-3eb4-98ea-d7e6ce5f4a1d | -1.6954 | -46.1426 | 2024-12-01 02:00:00 | GOES-16 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 0e955df0-09c0-38b2-85db-8b0120a86060 | -3.1273 | -54.5264 | 2024-12-01 02:00:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 115.8 |
| fac184b8-90a5-3c4f-8415-87487c8a8190 | -2.6578 | -51.8811 | 2024-12-01 02:00:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| d425b1e5-1c19-33b3-8a92-a94ed88bbbf9 | -3.5158 | -53.8333 | 2024-12-01 02:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 78.2 |


[Clique aqui para ver as próximas entradas](README18.md)

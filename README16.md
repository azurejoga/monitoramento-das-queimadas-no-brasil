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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 89e68602-62cb-3b3c-867d-11b32a6001e3 | -8.5758 | -62.6323 | 2025-08-25 02:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 1ddf1375-6224-3d99-b682-717e947283cf | -9.06 | -65.7344 | 2025-08-25 02:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 42.7 |
| a4c4a249-61a3-3a06-bb3a-439498fbece5 | -8.9689 | -65.4198 | 2025-08-25 02:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 625e344b-55e9-337d-b363-836d9edd7b0b | -11.4782 | -55.4819 | 2025-08-25 02:20:00 | GOES-19 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 82.5 |
| 824917da-a847-3e50-b650-be3632222f4e | -11.4595 | -55.4633 | 2025-08-25 02:20:00 | GOES-19 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 185.3 |
| ed91c58c-1718-33d2-bf18-6c30515693ed | -11.4784 | -55.4617 | 2025-08-25 02:20:00 | GOES-19 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 100.3 |
| 1e4a3601-35e7-39ad-8c6b-19aaaa90b2f7 | -9.0061 | -65.3813 | 2025-08-25 02:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 62e2a96f-a1e6-3651-928f-dc6c1c98e592 | -9.0601 | -65.7157 | 2025-08-25 02:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 33.5 |
| 7b61de68-8dbe-3160-9423-e346b364c0c3 | -9.006 | -65.4 | 2025-08-25 02:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 77.7 |
| d7df1f34-386a-37a6-9973-9d05dfe3bba9 | -6.8202 | -59.4194 | 2025-08-25 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 29.8 |
| 1aa48854-1d31-39e2-b57c-67c3e48367d0 | -8.9875 | -65.4006 | 2025-08-25 02:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 102.1 |
| 263ca7e1-0bbc-3224-9acf-eacaa04cb8e1 | -9.0416 | -65.7163 | 2025-08-25 02:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 29.6 |
| f0696ad9-1dbe-3749-b974-3f78d92fe569 | -10.6162 | -55.0487 | 2025-08-25 02:20:00 | GOES-19 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 0fc0820b-7700-3de1-8f95-0cfa3d6697a6 | -8.8734 | -62.4495 | 2025-08-25 02:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 130.0 |
| 106b8770-801c-34ac-b3df-87c0780805da | -8.8733 | -62.4685 | 2025-08-25 02:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 135.8 |
| b05187dc-29fe-3946-a1ef-1ae13b3b1c47 | -8.5136 | -63.8799 | 2025-08-25 02:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 78dff2c4-b97c-345f-8bd2-da50a45649d9 | -6.8201 | -59.4386 | 2025-08-25 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 33.2 |
| bdfca045-d4ed-31a3-a8d0-01d023bf08d3 | -9.1722 | -59.4629 | 2025-08-25 02:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 1a8bc7ab-f172-31ea-bb2c-f9de7caf6c76 | -11.4593 | -55.4836 | 2025-08-25 02:20:00 | GOES-19 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 139.1 |
| 8da5ac28-c282-3f5a-820e-c4ef911f2550 | -9.0415 | -65.7349 | 2025-08-25 02:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 39.9 |
| 655b5ebd-dee3-316f-8825-4680982ce331 | -3.4254 | -49.0517 | 2025-08-25 02:20:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 73d286dc-bbb3-3dfb-9833-54283f6b82a5 | -8.8919 | -62.4487 | 2025-08-25 02:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 105.5 |
| 417576bf-5ff6-3976-8d30-4a37360c2436 | -5.0994 | -43.1977 | 2025-08-25 02:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 25.2 |
| 4c67c7fc-9789-3004-ab0b-57472b983afb | -8.969 | -65.4012 | 2025-08-25 02:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 6209aa67-b256-3b83-b5ed-b64fcca80e5f | -9.0972 | -65.7145 | 2025-08-25 02:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 32.4 |
| cca34e40-b360-31ef-b15a-8206aa3d8dad | -9.0971 | -65.7332 | 2025-08-25 02:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 33.4 |
| 0f72359c-716b-3501-92ec-f800b566bd72 | -8.9874 | -65.4192 | 2025-08-25 02:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 141.3 |
| e3d41e4a-7f42-354d-b0e8-ce1d57945f1a | -7.6326 | -62.7243 | 2025-08-25 02:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 40b71153-e74a-3b7f-8532-f358adeb6ff5 | -8.8918 | -62.4677 | 2025-08-25 02:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 89.7 |
| 8f680fdf-8c34-3df7-a3d6-85e0afb97f40 | -8.9689 | -65.4198 | 2025-08-25 02:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 6263d4c6-3106-30e5-9251-398e827ac4a9 | -9.0416 | -65.7163 | 2025-08-25 02:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 30.8 |
| 5ef1ec90-246f-3306-956e-3b4b2b1ee1e7 | -11.4406 | -55.465 | 2025-08-25 02:30:00 | GOES-19 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 2d04734d-ec93-3dbd-ba91-ea8eac6822b0 | -9.006 | -65.4 | 2025-08-25 02:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 4d7225f0-0ff9-3b4a-9697-04d211d7f8c0 | -8.969 | -65.4012 | 2025-08-25 02:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 4a89094d-7eb9-30d2-a9d3-4504f8b94a4f | -8.8919 | -62.4487 | 2025-08-25 02:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 115.6 |
| 8b4a3b5d-17ec-3e82-8a5a-be5932b8b169 | -10.6162 | -55.0487 | 2025-08-25 02:30:00 | GOES-19 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 80675d0b-52c3-389a-bf10-e9736c49f9cc | -11.4595 | -55.4633 | 2025-08-25 02:30:00 | GOES-19 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 520.2 |
| 3544c3c8-3909-34b0-8906-4c5f55048ea9 | -11.4782 | -55.4819 | 2025-08-25 02:30:00 | GOES-19 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 120.3 |
| 7d78cbc2-6962-3cd5-86e8-2e92d3fe1d26 | -9.0061 | -65.3813 | 2025-08-25 02:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 9515a91e-98c4-386e-b457-dacab8134dc5 | -8.5136 | -63.8799 | 2025-08-25 02:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 53.3 |
| a3c97597-e7f2-38c3-b40a-e699b7700f7c | -13.5188 | -46.9032 | 2025-08-25 02:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 59.0 |
| bf8b428c-5de0-33a6-91f0-781b3610516e | -9.0971 | -65.7332 | 2025-08-25 02:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 30.2 |
| 05bb8394-5523-3742-bd58-9ae7b07fcc4c | -9.6553 | -59.6302 | 2025-08-25 02:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 56.7 |
| a5207f2e-7210-3c32-98a9-11562e4d74db | -7.6326 | -62.7243 | 2025-08-25 02:30:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 72.8 |
| a245ed1f-6e18-3b9c-b560-2609f8c7bf5a | -8.9874 | -65.4192 | 2025-08-25 02:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 156.7 |
| 80fedc54-a7f3-3291-bef8-4cbc452f5aeb | -9.0415 | -65.7349 | 2025-08-25 02:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 32.1 |
| 416d81ed-d235-3496-94e7-7ab13a0db366 | -3.4254 | -49.0517 | 2025-08-25 02:30:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| eef4a8ec-c307-3629-89e3-afcdb93ca290 | -11.4593 | -55.4836 | 2025-08-25 02:30:00 | GOES-19 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 342.9 |
| 9d39d344-e56f-32de-8c8d-78aecf81ccae | -9.1722 | -59.4629 | 2025-08-25 02:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.2 |
| ee532beb-690c-358d-b162-dee61ce41319 | -8.8918 | -62.4677 | 2025-08-25 02:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 87.8 |
| 310c9897-cd71-385c-b412-1961ff89766a | -3.4439 | -49.051 | 2025-08-25 02:30:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 41dc7fec-6579-3588-9cec-94c05f60520e | -9.8101 | -64.2642 | 2025-08-25 02:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 28.5 |
| 9eb7754b-6aeb-306e-9fcc-dcf1f4561cb6 | -6.8932 | -45.6512 | 2025-08-25 02:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 68.5 |
| aa20f956-58b2-3c90-91e8-e950d9932208 | -8.8733 | -62.4685 | 2025-08-25 02:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 130.3 |
| 5900e9a0-a1f6-3923-b14d-dd4b1b3b0492 | -9.0972 | -65.7145 | 2025-08-25 02:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 33.9 |
| 4c6c3f62-227c-3917-b976-d8f52eb31810 | -6.8745 | -45.6528 | 2025-08-25 02:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 105.7 |
| 4e6826d8-acd5-34f1-8171-5ca7164af44a | -9.0601 | -65.7157 | 2025-08-25 02:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 33.2 |
| b1b4d4ac-a504-3346-bf4d-89fe0d99b585 | -8.9875 | -65.4006 | 2025-08-25 02:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 102.3 |
| 541baf11-eaea-318c-8c74-974db4763646 | -11.4784 | -55.4617 | 2025-08-25 02:30:00 | GOES-19 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 155.2 |
| 6a1109e3-98c1-3f03-b186-22798d6ea485 | -8.8734 | -62.4495 | 2025-08-25 02:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 145.6 |
| eae49972-63f5-33af-9fe7-8b8d15a0086c | -11.4404 | -55.4852 | 2025-08-25 02:30:00 | GOES-19 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 766e18d7-3e96-39d1-8fc6-94620c84bbbd | -9.06 | -65.7344 | 2025-08-25 02:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 34.0 |
| 1ae2f552-b0d4-33bd-af6e-a3ede0af936d | -8.969 | -65.4012 | 2025-08-25 02:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 4ef2c7b5-2e3d-3243-95ea-857406ceef52 | -7.9077 | -63.073 | 2025-08-25 02:40:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 60.7 |
| e199e51d-d74d-3caa-abc0-5924dcfbca27 | -9.0061 | -65.3813 | 2025-08-25 02:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 70.9 |
| e5ca1889-a328-3dcd-af2a-95d4652f88ab | -7.9262 | -63.0724 | 2025-08-25 02:40:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 940d0b88-1514-3e84-8431-32461b8b618d | -7.9263 | -63.0535 | 2025-08-25 02:40:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 87.7 |
| 5d563a33-18d1-3898-af21-746c343f691e | -8.8918 | -62.4677 | 2025-08-25 02:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 84.4 |
| e9b351ab-9283-3548-a0f7-fee96444c19b | -9.0971 | -65.7332 | 2025-08-25 02:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 32.4 |
| f053df72-a554-33a1-8978-96c781343fd9 | -8.8919 | -62.4487 | 2025-08-25 02:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 98.4 |
| b49cdc27-1d59-30b1-9ae3-578036e7d5d6 | -8.8733 | -62.4685 | 2025-08-25 02:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 160.0 |
| d0fbe151-25f6-3bff-aba1-4aa1edad31c4 | -9.0415 | -65.7349 | 2025-08-25 02:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 34.6 |
| 5109699d-4023-30de-8960-28967761a7ae | -9.1722 | -59.4629 | 2025-08-25 02:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 1ba20349-d452-32b1-b636-7d9ea6980180 | -8.9874 | -65.4192 | 2025-08-25 02:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 150.7 |
| 354cd04b-620f-32ec-b535-e213da2b1781 | -8.8734 | -62.4495 | 2025-08-25 02:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 132.3 |
| e051fd56-a55b-3236-800f-0da91a40a2df | -9.8101 | -64.2642 | 2025-08-25 02:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 23.2 |
| 96acd8ff-8f4c-3e96-9993-e2e0a10f6c1b | -7.6326 | -62.7243 | 2025-08-25 02:40:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 65.3 |
| efca6e18-e5b5-34bd-8718-c9acd4248329 | -11.4595 | -55.4633 | 2025-08-25 02:40:00 | GOES-19 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 173.8 |
| 69decd75-d0be-3aa6-9ecf-72c3568193a3 | -8.9875 | -65.4006 | 2025-08-25 02:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 100.7 |
| cedc7c6d-0bd4-39dd-a028-3b1eb584363d | -9.06 | -65.7344 | 2025-08-25 02:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 38.9 |
| a8dc650f-883a-3692-91f9-881b30a53160 | -9.0972 | -65.7145 | 2025-08-25 02:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 28.9 |
| f2d31fcc-d4c0-358d-b4a1-ee704f8967cb | -9.0601 | -65.7157 | 2025-08-25 02:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 29.0 |
| bed45a7e-e3c4-3141-a823-bc624a58be26 | -6.8413 | -58.9552 | 2025-08-25 02:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 35.1 |
| 6152f43d-29e9-3127-89a3-f97ce3f1a4f6 | -11.4593 | -55.4836 | 2025-08-25 02:40:00 | GOES-19 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 125.2 |
| e40ceb22-65ce-3e36-9aa9-002c6de2b5a1 | -9.0416 | -65.7163 | 2025-08-25 02:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 25.7 |
| e0349eb7-bd6f-3794-b4c4-09faaf8a981d | -8.9689 | -65.4198 | 2025-08-25 02:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 44a3fd00-43e0-31fa-91bb-4ddd7db684f2 | -9.006 | -65.4 | 2025-08-25 02:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 93adfdfe-6028-3949-85f8-1a99a81eb3ec | -5.0994 | -43.1977 | 2025-08-25 02:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 505a5b4a-33ea-3073-9caf-fed9379eca8e | -6.8414 | -58.9359 | 2025-08-25 02:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 39.0 |
| 21808e86-b58f-3c8f-be71-fa93cece620d | -6.8229 | -58.956 | 2025-08-25 02:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.1 |
| dafb2dad-5061-3f7d-ac88-e19da1b5f2f3 | -9.06 | -65.7344 | 2025-08-25 02:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 34.2 |
| 9ecfeaec-8091-38b6-9a5b-7bea96a7c537 | -9.0971 | -65.7332 | 2025-08-25 02:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 25.7 |
| 43e20fd1-b68c-37cf-a3a3-bae88d6abce5 | -8.9874 | -65.4192 | 2025-08-25 02:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 148.4 |
| c53c3f1f-9be1-3e99-a2cd-c16550125c46 | -8.8734 | -62.4495 | 2025-08-25 02:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 149.2 |
| 4ad5c424-6ea5-384d-81cd-b5752fd550bf | -8.8918 | -62.4677 | 2025-08-25 02:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 515c6711-98c4-3716-b174-0e97775c7cba | -9.0416 | -65.7163 | 2025-08-25 02:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 30.5 |
| 7cc51b2b-26bc-35d1-98cc-77e34b0a3088 | -8.8733 | -62.4685 | 2025-08-25 02:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 133.0 |
| 1d59a12f-4a77-3549-a442-c0122b711861 | -9.1722 | -59.4629 | 2025-08-25 02:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.9 |
| e3f01c2a-26ac-36f9-ba0d-0631770097f0 | -6.8742 | -45.6753 | 2025-08-25 02:50:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 43.5 |
| a5194e7a-b024-3d3d-915f-86fdc08f9d72 | -8.2313 | -61.3922 | 2025-08-25 02:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 151.0 |


[Clique aqui para ver as próximas entradas](README17.md)

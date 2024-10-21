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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a1aa6d91-2f37-3a87-8988-81a0b44e03ce | -2.5513 | -49.18148 | 2024-10-21 01:05:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 19064890-7b87-36d9-80d4-0cb29abac039 | -2.48789 | -49.11588 | 2024-10-21 01:05:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| cbc8907d-aeb3-3c4d-a0cf-91e3abb19519 | -2.48648 | -49.1059 | 2024-10-21 01:05:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 5a3206b3-99c8-3c0c-96e6-7406d7edaebc | -2.47851 | -49.11721 | 2024-10-21 01:05:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 48.7 |
| d0808daa-8adf-37fd-b296-5d4455e97bfd | -2.4771 | -49.10723 | 2024-10-21 01:05:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 78.2 |
| aac29dd5-89f1-3f8b-8227-aaf17b21f077 | -2.47567 | -49.09722 | 2024-10-21 01:05:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 42.5 |
| e9308532-1074-39d0-aa79-3f28fa75ba8d | -2.46629 | -49.09857 | 2024-10-21 01:05:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| b6e2cb90-70d5-3bb5-b775-97acd243ea97 | -2.43147 | -50.28289 | 2024-10-21 01:05:00 | TERRA_M-M | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 3506bab5-c6d8-3510-835b-39d3d4529109 | -2.42878 | -50.33524 | 2024-10-21 01:05:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 5a65b766-6b4e-3609-a0dd-7e2084e7a9da | -2.42251 | -50.29008 | 2024-10-21 01:05:00 | TERRA_M-M | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 495c6fb1-89f8-3c02-bd68-fcd5dba02df8 | -2.42125 | -50.28104 | 2024-10-21 01:05:00 | TERRA_M-M | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 3bf78ed1-af3d-3f97-a161-8ff6ed78fb32 | -2.41203 | -50.41105 | 2024-10-21 01:05:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 30ac5610-21bf-3fe6-bf83-ffa0972a3a60 | -2.39969 | -48.9386 | 2024-10-21 01:05:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| e98adbd7-c1f4-30d8-9c35-86afc45602cd | -2.36508 | -52.52324 | 2024-10-21 01:05:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| c85d56e5-09cb-3375-a13a-a7f6cf8b517e | -2.3638 | -52.51414 | 2024-10-21 01:05:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9e7ccd2c-7dde-3616-8683-e83eb7cda4b5 | -2.31918 | -48.88319 | 2024-10-21 01:05:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| debd732c-c687-3190-b342-a701de386390 | -2.30563 | -46.63253 | 2024-10-21 01:05:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 8b1eb1db-18d4-3c73-acdc-7f7d45b0b94e | -2.30148 | -48.5902 | 2024-10-21 01:05:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9e79b0e4-b4a3-3c10-870d-664b4950d32c | -2.29244 | -49.10497 | 2024-10-21 01:05:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ea9cc78c-cf0e-3dea-9945-823cc316e0e7 | -2.29102 | -49.09491 | 2024-10-21 01:05:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 2aca41c1-ed0c-3a04-97b7-fc39932497ce | -2.28521 | -51.14612 | 2024-10-21 01:05:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c43dc36b-1900-3a94-9dea-1f4c63cbbb9d | -2.27614 | -53.75495 | 2024-10-21 01:05:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 21.0 |
| db5a9593-43cd-37aa-ad70-072f683cc254 | -2.27195 | -53.7242 | 2024-10-21 01:05:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 8413ae4d-dc3a-3a39-8a8b-a451af4b083d | -2.26841 | -47.08625 | 2024-10-21 01:05:00 | TERRA_M-M | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 41.6 |
| 62d70cd8-9755-3298-abae-14e080e28a03 | -2.26664 | -53.75627 | 2024-10-21 01:05:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 86829be8-d532-3739-ac18-f2d3e28eec1a | -2.26648 | -47.07294 | 2024-10-21 01:05:00 | TERRA_M-M | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 7d975e53-f844-341c-8c49-d040f64791d5 | -2.25744 | -48.58098 | 2024-10-21 01:05:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 91d86e97-eb66-34bd-8dcd-5ffafd37cf0f | -2.25558 | -51.93395 | 2024-10-21 01:05:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| b798056a-a871-35c9-b1c7-117606929833 | -2.24671 | -51.93519 | 2024-10-21 01:05:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 116c233b-6b4b-3e9a-8c9f-39d45f7ed718 | -2.24548 | -51.92633 | 2024-10-21 01:05:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| efe409af-f427-3426-b574-e61010abc2dc | -2.23418 | -50.45759 | 2024-10-21 01:05:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 1eda507f-b9bf-3b42-aadc-94ebedb129ba | -2.23292 | -50.4486 | 2024-10-21 01:05:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b84317d8-1cd5-331b-a808-bc4b6566cd88 | -2.22526 | -50.45886 | 2024-10-21 01:05:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 0b8e4f2d-6d0d-3454-8498-0642836b3d99 | -2.224 | -50.44986 | 2024-10-21 01:05:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 6afdf933-f966-3c8e-a278-c72891d39881 | -2.21634 | -50.46011 | 2024-10-21 01:05:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 3c47fed8-b229-3843-b9bb-02bf753f7c7f | -2.20742 | -50.46138 | 2024-10-21 01:05:00 | TERRA_M-M | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| f3f301e8-dfe5-36a8-8dc8-74f8644c7051 | -2.16992 | -50.52789 | 2024-10-21 01:05:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 80fae0c1-39cd-3f60-b563-39aba3221bc3 | -2.16688 | -50.70112 | 2024-10-21 01:05:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b8a9dc10-4a92-3dd5-9018-f446f31ecfda | -2.05789 | -46.90481 | 2024-10-21 01:05:00 | TERRA_M-M | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 3de97b1f-8171-3548-9655-3e8a0f5581be | -2.05585 | -46.8908 | 2024-10-21 01:05:00 | TERRA_M-M | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 852869f7-de57-32b8-84fc-49990bd74c0a | -1.98762 | -52.12597 | 2024-10-21 01:05:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3372af8d-06ca-315c-bdbb-2c76cb8d6594 | -1.93876 | -52.11144 | 2024-10-21 01:05:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 29.6 |
| 2efb786c-59e8-3782-947b-3687563c304d | -1.93752 | -52.10255 | 2024-10-21 01:05:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 77399ae5-8c28-3747-892a-ac7a4a6ac7aa | -1.92988 | -52.11268 | 2024-10-21 01:05:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 28.3 |
| fc755647-12bc-321e-9611-de6f13e28ec9 | -1.92864 | -52.10379 | 2024-10-21 01:05:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 36.4 |
| 9a368615-038a-3faa-88a7-caf1fcd09513 | -1.67413 | -50.47266 | 2024-10-21 01:05:00 | TERRA_M-M | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c7863712-b98f-3b38-b29c-dc2e6d7c0c46 | -1.67286 | -50.46363 | 2024-10-21 01:05:00 | TERRA_M-M | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 97fce636-1b2e-3bb0-8fa8-18b450d16878 | -1.63577 | -52.64626 | 2024-10-21 01:05:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| bda0132d-e7c3-3f33-830c-845cb03102b9 | -1.47222 | -47.45904 | 2024-10-21 01:05:00 | TERRA_M-M | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| f5a42182-033f-3331-9474-f310bbcad9ed | -1.12671 | -49.19545 | 2024-10-21 01:05:00 | TERRA_M-M | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| e897a2d0-df82-3868-b5fa-92b53f351272 | -1.1834 | -53.6368 | 2024-10-21 01:05:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 36.6 |
| 17a7947c-fafc-3302-8024-00f1105f4cba | -1.2018 | -53.6366 | 2024-10-21 01:05:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 3ef1bd93-3324-3f1c-92c0-fc284f433332 | -1.9395 | -52.1016 | 2024-10-21 01:05:17 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| fa6ee535-7116-3b08-9e0c-2699897d0709 | -2.2199 | -50.4594 | 2024-10-21 01:05:19 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| f8bda664-881b-3861-8c34-13b9b37e0651 | -2.2671 | -47.0775 | 2024-10-21 01:05:19 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 1a3cbdd0-bdac-30e6-8603-b4aa833fd464 | -2.2856 | -47.077 | 2024-10-21 01:05:19 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 28.7 |
| 920b419c-1546-39bc-ac09-d3cd0a297e9d | -2.464 | -49.1024 | 2024-10-21 01:05:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 42.3 |
| 7339c0ba-f189-3ca2-b570-7eeae34a4166 | -2.4824 | -49.1233 | 2024-10-21 01:05:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 3377d73a-b166-35fb-95ff-a99778061fd1 | -2.4824 | -49.102 | 2024-10-21 01:05:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 91.5 |
| 24b42385-bea7-3e03-8dca-79c82d17ff65 | -2.8069 | -51.3613 | 2024-10-21 01:05:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 06314f24-d5dd-33a3-be48-f2c1a3453894 | -2.8482 | -45.4637 | 2024-10-21 01:05:22 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 50.9 |
| bf88fb3e-3d51-357a-b0af-c367307783e1 | -2.8372 | -53.3261 | 2024-10-21 01:05:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 71df0dd8-765e-33a1-ba89-22e662e4c9b5 | -2.8668 | -45.4631 | 2024-10-21 01:05:22 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 6b0acf2e-01bb-39ce-8a74-889d85d363af | -2.8556 | -53.3256 | 2024-10-21 01:05:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 52.1 |
| d0253a82-5c55-30f8-93c2-184f82b70863 | -2.8864 | -45.215 | 2024-10-21 01:05:22 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 46.5 |
| eae8cfe2-8712-37f5-804b-6529f087ff35 | -2.8865 | -45.1924 | 2024-10-21 01:05:22 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 44.8 |
| d2bfa8f1-906b-3698-a13b-594040f737d5 | -2.905 | -45.2143 | 2024-10-21 01:05:22 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 136.1 |
| efcee774-73e3-3cf2-85d9-35db2b466962 | -2.9051 | -45.1918 | 2024-10-21 01:05:22 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 98.2 |
| 281cf818-8e90-3bdd-8a75-9e8d2f32025b | -2.9674 | -47.9931 | 2024-10-21 01:05:23 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 841ce82d-19c6-3fcb-a378-90d661241654 | -3.0036 | -53.0583 | 2024-10-21 01:05:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 79d45a11-1009-3aa1-8437-f7cc274c158c | -3.0037 | -53.038 | 2024-10-21 01:05:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 6dc75c00-298e-3bd1-a736-3d5903c3e040 | -3.0176 | -54.3489 | 2024-10-21 01:05:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 40.8 |
| 8851aba2-805d-36c0-b262-f02934daa7b5 | -3.0581 | -53.2395 | 2024-10-21 01:05:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 836924b7-d7ca-3972-8b9b-4637cab9cb45 | -3.1138 | -53.1163 | 2024-10-21 01:05:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 628f8db1-5f05-386c-b79c-e8d65529c0bc | -3.1962 | -50.8099 | 2024-10-21 01:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 21785980-a223-3d5a-a357-8d8e4d208d5f | -3.2146 | -50.8093 | 2024-10-21 01:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 119.5 |
| be5a6e3c-a783-3c89-b663-c16dddb9085a | -3.2147 | -50.7884 | 2024-10-21 01:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 112.7 |
| 10f1fcbf-7b33-3bb0-afdc-570b0128f7ed | -3.7752 | -53.4012 | 2024-10-21 01:05:28 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| b6c58df1-926e-3977-a9f8-b1eee4dabc8c | -4.8474 | -44.3472 | 2024-10-21 01:05:33 | GOES-16 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 6f21f5c0-485a-3dc3-8202-a3dae163bbb2 | -4.8476 | -44.3243 | 2024-10-21 01:05:33 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 4429cb2a-24de-3550-9e8e-bd0a28ea00b8 | -4.8661 | -44.3461 | 2024-10-21 01:05:33 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 8e402f5f-d475-37cd-a45e-5196c091d9dd | -4.8662 | -44.3232 | 2024-10-21 01:05:33 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 48.9 |
| 999ec75e-091f-3dd5-b55d-ad88c0678e37 | -4.8924 | -45.8386 | 2024-10-21 01:05:34 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 3973541c-a416-303c-899f-a9ad7c03c24a | -5.509 | -50.5872 | 2024-10-21 01:05:37 | GOES-16 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 48cd1ae9-c351-38bf-b2c5-71cd4c6b81d8 | -5.6707 | -46.4363 | 2024-10-21 01:05:38 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 63.7 |
| b605eed1-e3e9-336d-9892-dee0d45eb3cb | -5.6894 | -46.435 | 2024-10-21 01:05:38 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 132.8 |
| 31867e3f-79a7-3c7f-bc39-efa0130c40c3 | -5.6896 | -46.4128 | 2024-10-21 01:05:38 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 40f61526-ae97-3e9d-b2f5-6143c7fae04c | -5.7081 | -46.4338 | 2024-10-21 01:05:38 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 69.9 |
| af970969-c767-324e-8626-bae51e55f1a8 | -5.7083 | -46.4115 | 2024-10-21 01:05:38 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 55.2 |
| d815438d-30c3-39a1-a0f5-3ec729f3a32c | -9.7704 | -64.7174 | 2024-10-21 01:06:02 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 43.0 |
| d938ca06-4bc0-3e4f-9b2d-1c2e640b3a43 | -10.1978 | -64.8328 | 2024-10-21 01:06:05 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 35.4 |
| 0c11b7ff-588f-3610-a2ea-bf1c20cd6d91 | -12.4778 | -63.1885 | 2024-10-21 01:06:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 45.9 |
| e954e068-fa8b-32b7-9756-d4b076c209f2 | -12.5147 | -63.3014 | 2024-10-21 01:06:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 9cf42e84-69ad-3017-a197-23a2d866eccd | -12.5357 | -63.0319 | 2024-10-21 01:06:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 55a1d860-1805-3fea-8b67-cdd4be5dedf4 | -17.7848 | -57.4885 | 2024-10-21 01:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 95.7 |
| ee58f1a1-33d1-3487-bab6-37d5c19f6444 | -18.263 | -56.1021 | 2024-10-21 01:06:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 97.2 |
| 28718cc9-bdf3-37da-880a-6355b2f33d3b | -18.2828 | -56.0994 | 2024-10-21 01:06:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 181.8 |
| 2c5600c1-1161-31fd-9df5-ab67b1fe9c71 | -18.2832 | -56.0785 | 2024-10-21 01:06:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 85.1 |
| 859e8334-0fd0-3634-ab02-052fc2419e43 | -1.20438 | -53.64841 | 2024-10-21 01:07:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 63823569-4a81-321c-8e0e-fc0a5a24cf39 | -1.20304 | -53.63879 | 2024-10-21 01:07:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 29.8 |


[Clique aqui para ver as próximas entradas](README14.md)

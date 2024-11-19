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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1ba9881b-fe1a-3ad0-838e-aaa0d4f08e1e | -1.1328 | -51.6859 | 2024-11-19 04:46:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1233b6d0-3fd8-38a4-97c8-3d12fc13f22d | -3.48178 | -48.2492 | 2024-11-19 04:46:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7d58c666-1504-3089-962c-3dc43e5ff247 | -2.20706 | -50.71695 | 2024-11-19 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 983a6c35-9737-32fc-b122-9ef3627f9308 | -3.05603 | -54.40383 | 2024-11-19 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1335b807-2541-34a1-b88d-c48c41fc98c7 | -3.05257 | -51.33512 | 2024-11-19 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a145f987-a798-36bf-847a-49a0112459a8 | -4.11168 | -45.6343 | 2024-11-19 04:46:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4616be06-560b-3c06-b451-235b73161e1e | -3.47075 | -48.25154 | 2024-11-19 04:46:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9cd1bc7d-5f20-3729-a4da-ed12c2bd1a14 | -2.15817 | -50.48422 | 2024-11-19 04:46:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3c57c0cb-79bb-35a3-a1f3-4fac91ac2749 | -3.32682 | -52.99335 | 2024-11-19 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0d8ae77e-96b3-3318-a093-9468cfe0263f | -4.22595 | -46.52853 | 2024-11-19 04:46:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b6b9253f-4df8-3e98-aacb-038dfb4c0aed | -1.40836 | -52.43326 | 2024-11-19 04:46:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 50132db8-1871-3a76-8846-f26bd722acbe | -1.55101 | -53.0998 | 2024-11-19 04:46:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ca9e939e-60a8-3f76-b3ba-139e36d2cce1 | -4.09582 | -44.85315 | 2024-11-19 04:46:00 | NOAA-21 | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1a14f480-a987-38b0-b725-5b4f930d96fc | -2.78755 | -51.72229 | 2024-11-19 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 0e40516a-51e1-3876-ba35-f28e83da5554 | -1.42223 | -52.43539 | 2024-11-19 04:46:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 4eccbff4-b9e0-3427-b969-dc248009ba19 | -6.0548 | -44.04736 | 2024-11-19 04:46:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 18.0 |
| d58793b6-7f85-3961-a125-ec5bcb7f90b7 | -3.79341 | -51.07897 | 2024-11-19 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 1f5566c6-3152-3946-8702-a2486af4b5e7 | -3.31088 | -53.36434 | 2024-11-19 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7aab6034-25b0-340e-bfab-beda0502669b | -3.39119 | -53.2701 | 2024-11-19 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5e3fe8a7-08bd-30d1-a57f-5711b5a90abb | -3.21129 | -51.1046 | 2024-11-19 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 24cbf3ed-91a7-3ecb-8292-a81a02c050f2 | -1.58804 | -53.80041 | 2024-11-19 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 4a218ddd-8a22-3d0a-85f0-cb552453f48f | -3.31319 | -54.17612 | 2024-11-19 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 574c7673-5478-3b87-8287-dc6887d0847f | -2.58288 | -51.72658 | 2024-11-19 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5c2fa431-5f99-3fb6-90c3-233c35230539 | -1.07803 | -52.39112 | 2024-11-19 04:46:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e127ab58-d5a9-32c1-93e4-79a0c6e3a765 | -1.61936 | -53.28948 | 2024-11-19 04:46:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 7ba53aa9-489d-3e2b-924c-276cfcfd9b05 | -4.99196 | -44.33115 | 2024-11-19 04:46:00 | NOAA-21 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 73fb8dbb-c38b-38c1-bb3a-b87268ece931 | -3.04475 | -54.40215 | 2024-11-19 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a968b8fa-f96c-31fa-a07b-ed393ba03718 | -3.04474 | -49.46598 | 2024-11-19 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 12d964cc-bf1a-390f-9bb7-e28e010526d0 | -3.71425 | -51.84172 | 2024-11-19 04:46:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 66964596-5a40-3d54-9464-4cb0b68b6956 | -3.2012 | -54.31853 | 2024-11-19 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cea2b7a9-5f08-3e74-a1ad-24a140c2c7a2 | -1.21178 | -52.48174 | 2024-11-19 04:46:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7b0eb123-f272-3ddd-b76f-7557de5a6e03 | -2.95882 | -51.45642 | 2024-11-19 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 06b2999a-0d84-3832-b2bd-b20c2bdfcb9c | -0.09428 | -51.38984 | 2024-11-19 04:46:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bd777ddf-2801-3083-b287-3d2a12894ada | -1.70932 | -46.23709 | 2024-11-19 04:46:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| cd6a2e64-30e6-3cd9-8958-528a62dd8ab4 | -3.09221 | -51.03957 | 2024-11-19 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b99d9d5e-fb2e-3685-a271-cb3a656da2fc | -3.97951 | -49.95044 | 2024-11-19 04:46:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c42746b2-62e3-31b7-9f86-946fbb2ab06e | -2.68697 | -46.23261 | 2024-11-19 04:46:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1b2d5c15-0fd7-3051-9221-35fcf6a555be | -3.05644 | -51.33215 | 2024-11-19 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 64f6617e-2fab-3398-ae8d-b23d0e984d19 | -0.64419 | -51.70736 | 2024-11-19 04:46:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 30591003-2513-375e-9b54-3ffefb0c7ec4 | -4.82358 | -47.31731 | 2024-11-19 04:46:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b0b23637-8951-33f1-b9da-4be8eec4e340 | -1.54605 | -51.1143 | 2024-11-19 04:46:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fb5de9cd-e7fa-3180-a894-3bf157774d44 | -1.64797 | -52.64563 | 2024-11-19 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 10437ea7-2e84-3a7b-b6c5-0c3725611fec | -5.55043 | -47.04971 | 2024-11-19 04:46:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0e47ee1a-212f-30e1-bf8f-aacd08237f6c | -4.5786 | -48.01989 | 2024-11-19 04:46:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| fef38b52-7b34-3f72-addc-51b48b060874 | -5.9761 | -45.35762 | 2024-11-19 04:46:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| b5503e4b-1d3b-36e6-a86d-05cfc63a75e2 | -5.54975 | -47.05435 | 2024-11-19 04:46:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2d188f4f-4347-30e1-8aec-a71937815273 | -5.71865 | -44.8126 | 2024-11-19 04:46:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 85f07dcf-9b4e-3ee6-94bc-40a8aed05ce5 | -2.43142 | -50.4147 | 2024-11-19 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8651dfc9-5e71-3c22-a33d-9f4cc4a3eedd | -3.82014 | -52.16467 | 2024-11-19 04:46:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b1659ddc-7e09-32f2-bebb-2978afe0287e | -1.09251 | -51.73494 | 2024-11-19 04:46:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 00b00b21-4f69-3069-b6cd-848e4d531189 | -6.65028 | -47.25603 | 2024-11-19 04:46:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fe6cb66d-de5a-38b1-8e85-82830b9c0e77 | -3.55574 | -51.53214 | 2024-11-19 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 560f3482-9337-324c-93ad-f3719ffd3a30 | -2.95386 | -53.72144 | 2024-11-19 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d45a2baf-f3e1-382b-8890-471e8ceb6913 | -2.78169 | -48.5786 | 2024-11-19 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ac3c7b30-b6f2-3e40-81c9-88eb2bccf1a0 | -1.63957 | -52.676 | 2024-11-19 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 40f53aad-d7b4-3e02-850a-768f01a31f91 | -1.99704 | -45.3518 | 2024-11-19 04:46:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 8.9 |
| cecc988b-8ed6-3629-b4a8-953488591152 | -4.38598 | -47.76123 | 2024-11-19 04:46:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| cc42983d-58c2-3f8f-abda-5a56ded48793 | -1.6771 | -52.55174 | 2024-11-19 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6fff51c3-ba7c-37f0-95b7-d884800f5087 | 0.22157 | -51.11007 | 2024-11-19 04:46:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2c7ef78d-730c-3bfd-8e48-58aa73405267 | -2.2481 | -50.51917 | 2024-11-19 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aa3bcd7f-c4fc-3871-afd8-a2b53abb2fc3 | -4.10008 | -44.8538 | 2024-11-19 04:46:00 | NOAA-21 | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| be5fe4f2-4bbd-30c9-b3b2-676532fdc3db | -2.68981 | -51.805 | 2024-11-19 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 265aaf32-bb0d-3b57-98c3-f4d1b4b95fee | -1.24178 | -51.7507 | 2024-11-19 04:46:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| efaa7100-ca26-35ea-9bfe-e41f81a6e29e | -0.39334 | -51.54226 | 2024-11-19 04:46:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 06e6f95d-e68e-3c34-8662-47f076c4a17b | -3.34053 | -45.36182 | 2024-11-19 04:46:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 8ec99ba4-edd4-30f1-9c6c-1818843ada52 | -2.6118 | -54.53922 | 2024-11-19 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 23da949e-a2bc-39e9-91b7-602dea9a34e0 | -3.36113 | -50.82089 | 2024-11-19 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| db3b90ad-08ca-333a-b6a4-f6b6b96a6b24 | -2.20242 | -50.28732 | 2024-11-19 04:46:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 55729883-9827-3e44-9d05-e23ed4c9a0ec | -2.92895 | -49.11931 | 2024-11-19 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d64e2287-7ed5-3fe1-9179-2bdade26e0d1 | -7.48525 | -45.89396 | 2024-11-19 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2cf4b776-f3c6-3786-8aea-ed3ce2d32780 | -4.3871 | -47.77808 | 2024-11-19 04:46:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 4378afb8-6921-3807-85ba-2b33925a30ba | -3.50833 | -50.22427 | 2024-11-19 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 0e2dfba3-248c-3764-9f48-d9704b7bc972 | -3.41625 | -42.38498 | 2024-11-19 04:46:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 2.2 |
| f333b090-5a22-3c0e-996e-6431d1914c66 | -1.24745 | -52.04769 | 2024-11-19 04:46:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a7369360-c348-32e8-8c2a-56581eb7f2a5 | -1.73063 | -52.6974 | 2024-11-19 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 5d8f5206-0bdc-34de-b862-97d665f62a2a | -1.38049 | -51.56178 | 2024-11-19 04:46:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0e6efccf-4b39-304c-9bf8-48b625e775fb | -0.11678 | -51.42276 | 2024-11-19 04:46:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7525091f-8c10-3b49-893d-9fc1f5b270b1 | -0.35418 | -51.40728 | 2024-11-19 04:46:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0ad51a8a-91eb-343b-bf84-3a36eb930080 | -1.26965 | -52.13042 | 2024-11-19 04:46:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 712d6fc9-28a3-381d-a3fb-0cf30d88f66c | -3.03752 | -49.46848 | 2024-11-19 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 798ff5f2-5c6e-35b0-b870-dfed5946ddb3 | -0.97611 | -51.71721 | 2024-11-19 04:46:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 262645f5-6f7f-3b54-bd0d-a3de39439edd | -1.20726 | -51.76409 | 2024-11-19 04:46:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 021c8db8-f059-3fb5-afe0-120f581422eb | -3.54963 | -51.52764 | 2024-11-19 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9d4c31c4-a734-353d-8d55-887cd8612950 | -3.98105 | -49.9186 | 2024-11-19 04:46:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 83812b80-109b-3f7a-b842-3db2df08a53f | -3.97773 | -49.91809 | 2024-11-19 04:46:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| c78182de-19c8-3b15-ba95-ae2631937c1e | -3.05156 | -54.40776 | 2024-11-19 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2366c7ef-47e2-3cd8-87c4-482a7a85600e | -2.15261 | -50.91337 | 2024-11-19 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bfca6049-4ebd-318f-9c37-ee3809c5beb9 | -1.20274 | -51.77082 | 2024-11-19 04:46:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6cd2239e-ebff-38a9-9040-caffacbb52b0 | -1.20501 | -51.7786 | 2024-11-19 04:46:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 00d9ed5b-c347-331c-a07e-dd510166af5b | -0.92079 | -52.54039 | 2024-11-19 04:46:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0a1ab9da-3b78-36bd-b6e7-2ea89c2b1c18 | 0.37802 | -50.8654 | 2024-11-19 04:46:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 07c53123-732f-3d2e-a3a4-826e39e3ca80 | -1.97549 | -52.15108 | 2024-11-19 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 93a8c691-2cd2-3f32-aadb-bd8937db8916 | -2.22445 | -50.51904 | 2024-11-19 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| edaf330c-cd8d-3c21-8ab6-22131d8be947 | -3.77004 | -51.01186 | 2024-11-19 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 8f4139bc-19f4-358a-b0b4-1f72478db4e9 | -1.16157 | -46.75242 | 2024-11-19 04:46:00 | NOAA-21 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9ea56e6c-16c6-3a00-931a-6c7c5f716a4a | -4.36032 | -45.28356 | 2024-11-19 04:46:00 | NOAA-21 | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d41499b5-26fc-3de0-8b6e-ef4da250e7d8 | -7.99634 | -44.38351 | 2024-11-19 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ae58650c-d6e7-3fe0-a87b-b80379a985ab | -2.71793 | -46.08177 | 2024-11-19 04:46:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5e11e119-96a3-3c34-be32-63a40eb4df80 | -3.79571 | -50.2586 | 2024-11-19 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c66b0c32-0821-3466-b40e-0966c87ee849 | -1.99564 | -45.34847 | 2024-11-19 04:46:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 7.4 |


[Clique aqui para ver as próximas entradas](README35.md)

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
| ddb6d523-4438-38af-9dc2-f0769b9ee4ef | -6.0912 | -57.9187 | 2026-08-19 00:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 120.2 |
| cb011046-38d7-39e1-8620-b6b0c9bb0b7d | -9.4256 | -60.4353 | 2026-08-19 00:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 108.0 |
| 9c56734d-9f08-31aa-9e6e-4a0cd3e102c9 | -19.7442 | -57.9425 | 2026-08-19 00:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 210.6 |
| 1ef220fa-985a-3740-9a52-69e0ce39b861 | -5.9994 | -57.8639 | 2026-08-19 00:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 170.9 |
| 58313e5f-37f2-3073-bda1-5531bdc75bda | -6.0913 | -57.8992 | 2026-08-19 00:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 50.0 |
| d8efebf3-5961-3691-88c4-2e42980410d5 | -6.6938 | -58.942 | 2026-08-19 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 158.1 |
| 62caa574-3ac1-374f-9a88-e1ab336c166a | -6.0178 | -57.8631 | 2026-08-19 00:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 40a8a100-0537-30f7-b662-5944ba15c20e | -19.7438 | -57.9633 | 2026-08-19 00:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 128.0 |
| 0578b9e5-3826-3c60-88fb-d197834110c3 | -6.8593 | -59.0318 | 2026-08-19 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 89.0 |
| a9fafcf6-12dd-379f-a16e-1e42c64abf64 | -5.9198 | -43.6264 | 2026-08-19 00:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 226.0 |
| 734f0a85-e6c8-35df-aba2-ab600fd1e03d | -6.0912 | -57.9187 | 2026-08-19 00:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 118.2 |
| ee317892-356b-3e71-bd57-574775982b2a | -6.3496 | -54.9068 | 2026-08-19 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 5d52501c-85cd-3f16-ba90-9aca42e72b6f | -6.8778 | -59.031 | 2026-08-19 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 93bc9112-cfe2-3da5-9fbc-9322de287e0b | -5.92 | -43.6032 | 2026-08-19 00:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 79.2 |
| b347972e-f6f7-3ad5-9309-3926ab68efa4 | -5.9995 | -57.8444 | 2026-08-19 00:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 90.1 |
| e12b4521-da5e-3dc6-88c9-6fe2abb50b5e | -7.5487 | -55.5829 | 2026-08-19 00:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 6ab09c6a-cac3-3fa4-87f6-934aa27a27c6 | -9.4061 | -60.5518 | 2026-08-19 00:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 876c9739-7066-3e31-b672-393bb2f655a9 | -7.5488 | -55.5629 | 2026-08-19 00:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 8492ee7d-d9f0-31b3-b687-a1f9af39f207 | -19.7446 | -57.9217 | 2026-08-19 00:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 76.4 |
| e8110c95-6643-3663-aaf4-4156264a595b | -5.4317 | -48.4212 | 2026-08-19 00:30:00 | GOES-19 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 73.4 |
| dbf78e64-aff6-3dc9-a96a-2143cfa92a70 | -5.9011 | -43.6279 | 2026-08-19 00:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 39b712a1-56bb-3882-97eb-ee58acb37798 | -9.406 | -60.5711 | 2026-08-19 00:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 95.8 |
| 7a7de3a3-113b-38ad-bd41-900947b693c8 | -6.0728 | -57.9194 | 2026-08-19 00:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 5a30e28a-6ce1-37f2-b328-510b83046f07 | -19.7442 | -57.9425 | 2026-08-19 00:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 376.5 |
| 8c978e65-c28a-3002-a8c8-4fc8b715e823 | -6.7486 | -59.0364 | 2026-08-19 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.4 |
| aebe458e-ab80-307c-b253-7077c649e7dc | -5.9994 | -57.8639 | 2026-08-19 00:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 169.4 |
| 5b274b74-8806-3923-861f-9243a3094865 | -7.0576 | -59.8523 | 2026-08-19 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.3 |
| d524c6df-2a88-3c07-9777-cc3632107fb2 | -6.7123 | -58.9412 | 2026-08-19 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 399f5c57-ae25-3a25-bd95-0b9e4b445aae | -19.7639 | -57.9607 | 2026-08-19 00:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 84.5 |
| b87436bb-d851-3e7d-8bcf-e651ebd8d91f | -7.0577 | -59.8331 | 2026-08-19 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 05e1b3e5-7f6d-35ee-a379-a0c418b8d98f | -9.0158 | -60.5138 | 2026-08-19 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 32.0 |
| 6213f05c-c11c-3b56-b995-cea8e375cc79 | -6.8777 | -59.0504 | 2026-08-19 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 7d358442-d708-314d-b4a5-9c8493ab49e3 | -14.4554 | -45.6251 | 2026-08-19 00:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 53.1 |
| a2a8a99a-c1b0-399e-99ea-b1fd42d04d04 | -9.3875 | -60.5528 | 2026-08-19 00:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 124.5 |
| 13f08987-2afb-3ce6-9f15-fe79875c69b3 | -9.4257 | -60.416 | 2026-08-19 00:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 90.4 |
| 02706706-c525-38cc-95e4-e35f69992e75 | -9.4256 | -60.4353 | 2026-08-19 00:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 103.1 |
| 4576ddd4-5993-3d75-8d14-d627dc1fa8a9 | -19.7643 | -57.9399 | 2026-08-19 00:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 99.3 |
| aa8100c6-4236-3e57-9f25-5fa49cd58b62 | -19.7241 | -57.9452 | 2026-08-19 00:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 96.6 |
| 06f7cb4c-9777-3e0d-8105-188f185d1806 | -9.4058 | -60.5904 | 2026-08-19 00:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 4ce3bdb8-86aa-3421-8ddb-9551febf67eb | -9.4254 | -60.4545 | 2026-08-19 00:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 59.1 |
| afa79900-afc2-38ae-84bb-0b682eb21921 | -9.3873 | -60.5721 | 2026-08-19 00:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 107.3 |
| b724bbd2-e81c-3289-8cdb-482492c1570b | -7.5301 | -55.5839 | 2026-08-19 00:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 2b6ddf2a-4a8f-357f-8b2c-3f428db35dd5 | -7.5301 | -55.5839 | 2026-08-19 00:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 54df3d1e-5ddd-3986-b76f-5be0de646fab | -5.9995 | -57.8444 | 2026-08-19 00:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 793f1acf-41d5-3876-9863-75fb14787343 | -6.6938 | -58.942 | 2026-08-19 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 135.5 |
| acb05fa4-1ed6-358e-a656-e7f27b835f0d | -5.9994 | -57.8639 | 2026-08-19 00:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 146.7 |
| 558a99e6-96c3-30fa-bed1-01ffbec5bcb2 | -5.92 | -43.6032 | 2026-08-19 00:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 64.7 |
| ca838fd3-e60b-3b49-97b1-b1e7a3a6b3f8 | -19.7639 | -57.9607 | 2026-08-19 00:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 97.8 |
| 018d34aa-9ebd-3b40-b66f-f0e84681607f | -9.4058 | -60.5904 | 2026-08-19 00:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 53.6 |
| ce1db07a-0103-39ea-a192-0cbee016aa99 | -19.7442 | -57.9425 | 2026-08-19 00:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 224.4 |
| a4082eb1-6fc4-389c-89d4-2f132f08e9e4 | -6.0913 | -57.8992 | 2026-08-19 00:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 613a72b1-0b3d-3e46-aa7b-cdc4d309b205 | -5.9011 | -43.6279 | 2026-08-19 00:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 113.3 |
| a9c1d0a8-ebbc-30f3-be25-a4170f075113 | -6.0912 | -57.9187 | 2026-08-19 00:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 137.9 |
| e92e0a8a-4dff-318a-98e8-2b05ee87df46 | -7.5487 | -55.5829 | 2026-08-19 00:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 195344b5-09a1-3322-bcd4-04b88040cbdb | -19.7241 | -57.9452 | 2026-08-19 00:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 90.2 |
| c4592684-39da-37a0-af5b-15230c05b0b1 | -6.7123 | -58.9412 | 2026-08-19 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 89.6 |
| 8f53a04d-f0c5-39dc-8db9-542dd59dac65 | -7.5488 | -55.5629 | 2026-08-19 00:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 88ea51bf-a6e0-3e80-b67f-ff5b350fe9da | -9.4061 | -60.5518 | 2026-08-19 00:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 86cab440-9bd0-373a-8c58-0bf5dcf95e62 | -9.4254 | -60.4545 | 2026-08-19 00:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 8cb98e4b-fe94-3160-a330-4620a427135b | -6.0179 | -57.8437 | 2026-08-19 00:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 24d30ba3-ff81-3cb0-adfb-b35b83ce8491 | -7.0577 | -59.8331 | 2026-08-19 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.0 |
| a6229f50-4c50-337c-b823-ca24aa50a814 | -9.4257 | -60.416 | 2026-08-19 00:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 88.9 |
| 117e452d-d04c-36d5-9ed7-e033a2a97d4b | -6.8777 | -59.0504 | 2026-08-19 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 71792a02-8034-3bec-8649-3fdcbdf6b44b | -6.8593 | -59.0318 | 2026-08-19 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 86.6 |
| 29f5832f-75fa-3a8a-87e4-79045f1a4137 | -19.7438 | -57.9633 | 2026-08-19 00:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 92.8 |
| 44e21546-02ec-35c0-99db-22e0431fd026 | -9.406 | -60.5711 | 2026-08-19 00:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 102.8 |
| 59945457-3032-3f25-b171-646f8aed0b5a | -6.8778 | -59.031 | 2026-08-19 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 73b2c057-5e84-3e20-a729-7284eeeb71f3 | -9.0158 | -60.5138 | 2026-08-19 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 39.9 |
| f2fbd572-fe6b-3f15-b4ba-416c9f3bdbfc | -5.9198 | -43.6264 | 2026-08-19 00:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 200.2 |
| 44b0bfd1-39ac-3635-a416-1b92afa26152 | -3.5053 | -44.236 | 2026-08-19 00:40:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 20f8ff5a-a6db-39e8-acd4-359eeebf7319 | -6.0178 | -57.8631 | 2026-08-19 00:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 29a2b018-e9e2-32e9-9375-5c9c137e5471 | -6.3496 | -54.9068 | 2026-08-19 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 58d8f84b-70bb-33c4-acba-02a07b461cc6 | -7.0576 | -59.8523 | 2026-08-19 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 1a9744d3-dda0-3240-a4ea-b9a6712ad7d1 | -9.3875 | -60.5528 | 2026-08-19 00:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 112.8 |
| c37bd3d4-359d-3933-9eef-1099c1218b09 | -9.3873 | -60.5721 | 2026-08-19 00:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 90.7 |
| 40594182-79fa-37bd-bc3b-d1fb365c7b7b | -19.7643 | -57.9399 | 2026-08-19 00:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 113.0 |
| 327ab5a0-f18e-3fab-85f8-aca0f8646ecb | -5.4317 | -48.4212 | 2026-08-19 00:40:00 | GOES-19 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 77.4 |
| f16e9748-a925-380f-bd09-cf299366095b | -9.4256 | -60.4353 | 2026-08-19 00:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 117.6 |
| d0260195-1359-3f46-b563-5e869617cf1f | -14.1432 | -52.9558 | 2026-08-19 00:50:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 39.7 |
| 135bdc81-03a7-3d7a-b8f4-606a33cd63a4 | -5.9011 | -43.6279 | 2026-08-19 00:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 653891aa-031e-329f-8909-16aa8587e6f3 | -19.7442 | -57.9425 | 2026-08-19 00:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 518.0 |
| 7bb5d3ea-7418-331e-91d0-368f026ec2a5 | -6.7123 | -58.9412 | 2026-08-19 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 86964434-ada4-39ff-9b95-8f0ea2ef48de | -6.3496 | -54.9068 | 2026-08-19 00:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 58.2 |
| e5fa68ae-34ce-3f33-b27f-4d3ebf190c8c | -5.9995 | -57.8444 | 2026-08-19 00:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 0caf8297-5879-3d8d-9865-c2912f7d9f66 | -6.0912 | -57.9187 | 2026-08-19 00:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 143.1 |
| 36afe898-30d6-3fc7-a5b3-da216941a2f7 | -9.4061 | -60.5518 | 2026-08-19 00:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 86.3 |
| 35ec9d9f-6697-3464-9047-5a358965b02b | -9.4256 | -60.4353 | 2026-08-19 00:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 93.0 |
| 33fb0544-1191-33e7-8a35-77e2eb6aaf2a | -6.8778 | -59.031 | 2026-08-19 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 48f23dd2-d46a-3ff8-a716-0dfa233587b9 | -19.7446 | -57.9217 | 2026-08-19 00:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 95.9 |
| 632d8341-1164-3225-9b11-03a33c77d75a | -6.8593 | -59.0318 | 2026-08-19 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 76.4 |
| c50a8a4c-83ae-3b6b-8960-c42774183b74 | -7.5488 | -55.5629 | 2026-08-19 00:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| f30eb523-a53b-3aa7-84f5-0ec9a7013d03 | -19.7639 | -57.9607 | 2026-08-19 00:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 153.6 |
| b348518d-4de5-3990-a940-38e12e6aec56 | -9.4254 | -60.4545 | 2026-08-19 00:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 58.7 |
| fa4a4d27-67be-39bf-9d42-20d4a9cd6812 | -5.9994 | -57.8639 | 2026-08-19 00:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 173.3 |
| 1b9d3394-5911-3c5e-9ef6-994c9fb4c24b | -5.4319 | -48.3996 | 2026-08-19 00:50:00 | GOES-19 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 6946686a-9172-3db3-bba0-c244ec246591 | -9.0158 | -60.5138 | 2026-08-19 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 94c23611-6eb9-3193-9a95-61990bdcb6cb | -7.5487 | -55.5829 | 2026-08-19 00:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 140705dd-7fa6-315b-ad2c-612d8c239af9 | -19.7241 | -57.9452 | 2026-08-19 00:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 130.3 |
| bc263948-d555-37f7-9e89-e324d58085f0 | -7.0577 | -59.8331 | 2026-08-19 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 7025040b-517e-3129-9f3b-98e832fafb4c | -19.7438 | -57.9633 | 2026-08-19 00:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 159.2 |


[Clique aqui para ver as próximas entradas](README7.md)

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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 644c8fa9-dcc8-3f16-8f4d-e630f822aa4c | -3.4968 | -54.62031 | 2026-10-06 05:23:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5a75c61a-4bb2-35e6-b039-3d4eb6e393fe | -3.87369 | -55.81664 | 2026-10-06 05:23:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| c920d86c-7511-3ca4-a524-b418824c39e8 | -6.75893 | -55.47237 | 2026-10-06 05:23:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b4a1a229-e24b-315e-ad84-5cef7e17d392 | -3.3375 | -59.4899 | 2026-10-06 05:23:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a208fa69-d13d-37b7-b5d8-5b7d10d1270c | -3.06615 | -54.17279 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d28f70d8-d620-3bfb-80e4-eb4fde3f381c | -3.8951 | -49.71432 | 2026-10-06 05:23:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 19b0d5a4-c95d-32fb-b3cb-c293b2beef1f | -3.10503 | -53.74956 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 527529e7-1d7d-3e9a-830f-93479b4a01b8 | 0.31553 | -60.43777 | 2026-10-06 05:23:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| edd77bb9-7ab8-3954-b05a-287229b4ab78 | -3.11084 | -53.71142 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 49ebbccb-b95b-3014-bfe4-40405233a805 | -3.87902 | -55.80757 | 2026-10-06 05:23:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8ce40cab-7963-3d1a-bd88-7fd838c4f807 | -2.92373 | -54.11369 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 27a2b196-5fee-3f04-bdd9-2615ff2eaa85 | -3.33261 | -59.47489 | 2026-10-06 05:23:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9905fc89-b4cd-3b2e-8f7e-72fd666b0ce4 | -2.98194 | -54.12869 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 6b70c7e7-62b4-3194-a6f1-12851e733e9f | 2.01382 | -61.091 | 2026-10-06 05:23:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| aeee14ff-fb76-3961-aaf2-3fe436acc41b | -3.4924 | -53.44156 | 2026-10-06 05:23:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2a01be16-aa12-3bf8-bf55-4ab8761df55c | -3.37868 | -58.19065 | 2026-10-06 05:23:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 292beff8-a444-3a2c-8d79-30d2d7369ed3 | -3.27619 | -54.18584 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2bcd8068-89e7-3518-878f-0912bbc021b9 | -8.97439 | -65.43645 | 2026-10-06 05:23:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 769b5f7d-f362-3ed7-86be-3d766d706944 | 2.4635 | -50.83419 | 2026-10-06 05:23:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 12.6 |
| dc01269f-ffd6-33bf-bc58-8efcfd7fc0bd | -3.84141 | -50.31908 | 2026-10-06 05:23:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a7b7851f-7b80-338b-991d-808344406497 | 3.0631 | -60.58964 | 2026-10-06 05:23:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 5.9 |
| dbc8e9cf-8816-3ea3-901a-d966eb2b6e4c | -3.13341 | -53.71052 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b2bb941a-8943-31da-8ada-44b58ee88c31 | -3.05767 | -54.17146 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ad8a35cf-2584-33ba-b4fe-b76550792694 | -2.78035 | -57.6776 | 2026-10-06 05:23:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5458a0fb-ca86-3f8c-babd-5861f42ccf43 | -2.07276 | -56.85641 | 2026-10-06 05:23:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 45478faa-1cb6-3421-8942-421e6c134220 | -3.06205 | -54.17365 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 78a1a0d4-f3f9-3f94-a543-6e74dfd3b069 | -6.48704 | -62.85786 | 2026-10-06 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 39c4c4a6-7ca4-34be-9b3f-d64ff86ba3af | -2.95899 | -54.1108 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 789d26ea-dcf3-39af-b7bc-b6571f6973ef | -3.11313 | -53.75513 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 145418e3-eb06-3f36-9b14-3022406c9d0e | -4.2829 | -50.271 | 2026-10-06 05:23:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0ceb5d3e-5bdb-34b1-b9c6-82190b84f1b5 | -3.05657 | -54.20917 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| eea32886-9ea6-3929-ad01-8ccf5a58a792 | -3.73459 | -48.87213 | 2026-10-06 05:23:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 4a7661fa-ada9-30e2-8c7d-6d6ba1d9c4c6 | -3.00675 | -53.87122 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f5962876-9d6d-3eaa-a964-ad5713fd4c6f | -3.10712 | -53.70644 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 716843b9-76b6-3017-afcd-b2baf65f0387 | -3.72101 | -48.87969 | 2026-10-06 05:23:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 59a34f93-e2d9-35e6-9a60-0ab5de4d01f9 | -3.68664 | -55.94675 | 2026-10-06 05:23:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 9b728e42-2441-3657-982a-314503721d93 | -3.10876 | -53.75446 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bc135d8f-e5c3-3de3-8e57-b127b13df2cd | 3.06254 | -60.58594 | 2026-10-06 05:23:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6297842c-b5f2-3a6a-aa83-48b2b932939d | -2.99031 | -54.10161 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5b4f6c89-464c-312d-8e28-c64345950218 | -2.9456 | -54.1413 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b8f6ad68-b5df-388a-9860-979378f39b7d | -3.09577 | -53.72214 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 3f4b432e-c8ee-38fa-9e83-79cf04254bba | -4.11218 | -49.39598 | 2026-10-06 05:23:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f93e664f-a606-3ba4-8412-919e0a67a6fc | -2.94754 | -54.15595 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ed356b03-e963-3bf9-b425-4513367ed6ae | -8.34659 | -62.82676 | 2026-10-06 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| beaf5064-3d7c-386a-bdd6-d9f086dece50 | -3.58194 | -54.31399 | 2026-10-06 05:23:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3da19b8f-844c-3a39-b074-799b22356247 | -1.09011 | -54.11645 | 2026-10-06 05:23:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f27b3c61-1087-3ca2-96a8-dc880d398786 | -3.05414 | -54.2249 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f962b75c-64b9-30f3-b686-2c924e61c437 | -2.78326 | -57.65862 | 2026-10-06 05:23:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 68239d7c-4521-330d-b3c5-aa5f931e9f6a | -3.68213 | -55.95086 | 2026-10-06 05:23:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 8e4469e4-9bd5-3af2-a0d6-110f83862730 | -3.11652 | -53.70358 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d0b952ed-fe0b-3a69-bc6a-0b647dddbceb | 1.72831 | -55.62054 | 2026-10-06 05:23:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a339b39c-9a9d-3c10-ab77-fcb64c1991e5 | -3.8412 | -50.30936 | 2026-10-06 05:23:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| df5bfc79-b24b-3eb7-84c6-7513cd81a77f | -3.05941 | -54.15956 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 66de8669-5f10-3565-bdca-4c167ac6ad12 | -2.7821 | -57.66621 | 2026-10-06 05:23:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f1ddf221-0433-35e1-9ad5-a6352f5e7535 | -3.10195 | -53.74043 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| cc590ced-8af5-3356-8eb1-40ec2356dc24 | -3.50338 | -54.63282 | 2026-10-06 05:23:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 60f7c76e-4092-3848-9dc9-346f7d52f926 | -3.08008 | -54.16665 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 68fb0854-4753-34e9-a87f-c061829638db | -3.19296 | -54.10541 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ca88f531-1bc5-3dac-bb72-8477ff20aca9 | -7.68202 | -62.54906 | 2026-10-06 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 52b69df8-5240-3c81-9a2e-8cdc5d7c6f39 | -3.99772 | -56.27509 | 2026-10-06 05:23:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d0979cd1-2baf-3d1e-8b2a-bcc0e376fdde | -2.48192 | -56.09675 | 2026-10-06 05:23:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7db68cae-56f6-3df8-b6bc-9cc6629d6ae6 | -2.94438 | -54.14923 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8fa64703-9b7e-3b63-b7b8-55d8c266d96a | -2.06858 | -56.85989 | 2026-10-06 05:23:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 08b0dba1-1161-3613-876f-33078e8e796e | -2.96262 | -54.14183 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5ca57772-2c5b-3962-a51f-a0a48643b79f | -8.99649 | -65.39705 | 2026-10-06 05:23:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cfecbbb6-3afa-3c35-a1c5-ee6dfe517fbc | -2.44043 | -58.01575 | 2026-10-06 05:23:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 40bdab87-c06e-3287-bd5b-40f563960871 | -7.90842 | -61.52841 | 2026-10-06 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9082f8a4-9128-3061-a65d-3f031569aacb | -3.37982 | -58.20588 | 2026-10-06 05:23:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| f3a652a3-73e8-3627-beea-ba68e38e8d9a | -3.1632 | -50.43849 | 2026-10-06 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d930e981-3b7b-347c-8b74-1f853cf9e3b9 | -4.00148 | -56.27565 | 2026-10-06 05:23:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0ca82955-9436-39d8-b965-9705d675e10e | -2.94986 | -54.14003 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c9c5a568-7765-3aaf-9a85-1ad2c846981a | -3.58304 | -54.30706 | 2026-10-06 05:23:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 16428bf6-7d13-31ff-964b-1dd0891c8167 | -3.11855 | -53.75387 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 02bdd873-e219-3923-9d8c-773ddd4c6fa5 | -6.69204 | -55.20979 | 2026-10-06 05:23:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 64647598-0215-37a4-b4cf-954920eea0be | -3.83624 | -57.16874 | 2026-10-06 05:23:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4978e032-81f6-37a4-b5cf-d648cef10816 | -3.67208 | -55.93969 | 2026-10-06 05:23:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f637b7c6-6ba0-3f96-95de-b105e70e3de9 | -2.94379 | -54.06779 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8ccdc904-67ef-3255-aa44-f5d5a0849dbd | 3.12629 | -60.56871 | 2026-10-06 05:23:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ee8504c8-5062-321e-a830-640f633f3fdb | -3.06366 | -54.16019 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7828ca42-f44a-30ba-b6ad-591658b0e1c1 | -2.78381 | -57.67812 | 2026-10-06 05:23:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 27c569be-d51e-37c1-ae9a-08408fd17861 | -2.99102 | -54.12616 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 16d67f5a-ec5f-3846-a2e5-7db7775502ea | -7.44667 | -63.55492 | 2026-10-06 05:23:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9e56a667-7060-3675-babd-82dd94ce4915 | -8.59412 | -66.81742 | 2026-10-06 05:23:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5ea9c2cb-5824-3bcc-96b2-281ef53a8add | -3.66981 | -54.54059 | 2026-10-06 05:23:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2894ab46-e5a8-3a0d-8a2d-d3d0b8c8f23e | -3.0685 | -54.15682 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a4a51d62-b045-3efc-9d94-dae3e865e610 | -1.32606 | -56.40662 | 2026-10-06 05:23:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1173c29a-aa3b-33de-96f9-670df82719b8 | -3.61257 | -54.59934 | 2026-10-06 05:23:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a2559731-4e6b-32a4-a961-1b9f62ea1e37 | -2.99586 | -54.12286 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4324a7c2-227a-3930-ac51-02247c5fd953 | -2.95104 | -54.16235 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 053067ca-c8e1-3077-b648-3de20b00242c | -3.72005 | -48.88448 | 2026-10-06 05:23:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d2a7bf4d-1207-3657-933a-4c186de10def | 3.06367 | -60.59334 | 2026-10-06 05:23:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 289bb1c9-031b-3466-b161-c7160e63fc13 | -1.42527 | -55.34887 | 2026-10-06 05:23:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 18026eac-81ac-39a4-b901-7546751f0291 | -2.95662 | -54.15318 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 61a8110d-2053-3703-8000-48396d1c209d | -3.06908 | -54.15286 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 273b0f0c-c059-302b-9cf5-4968d893bd40 | -3.16923 | -50.43793 | 2026-10-06 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2e8c0faa-3940-3c46-82c1-b479e58886f2 | -3.50808 | -54.62976 | 2026-10-06 05:23:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 3b151e25-c996-3cd9-8b37-0c2e6710c75d | -3.06733 | -54.16479 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 48d8602f-f5c7-37bf-81af-230c6f1d68d3 | -3.13349 | -53.71275 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f5b4097e-72e1-389e-a4a0-fcebfa6aaa63 | -2.55465 | -53.97476 | 2026-10-06 05:23:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 022446af-0f53-3a1f-8495-80187ec9f193 | -2.78439 | -57.67433 | 2026-10-06 05:23:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |


[Clique aqui para ver as próximas entradas](README60.md)

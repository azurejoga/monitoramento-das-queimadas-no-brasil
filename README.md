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
| 1f24ef93-5b0d-3bbd-ba7c-c845e851a473 | -17.6069 | -57.5304 | 2024-11-12 00:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 115.3 |
| 6623c29a-2fd0-320c-bb90-6d9bfa85f490 | -2.7588 | -49.3285 | 2024-11-12 00:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 177.0 |
| 96123bb2-bda5-3294-b3aa-14e1fcad6f8f | 2.7438 | -60.96 | 2024-11-12 00:00:00 | GOES-16 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 67.5 |
| bbde7f64-6ad3-3c70-9f2b-353e0fcd5a83 | -3.7529 | -50.1836 | 2024-11-12 00:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 88ebad74-e306-3c17-a013-745da1258411 | 1.048 | -60.5986 | 2024-11-12 00:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 124.9 |
| 0a8ec824-29df-3f30-bc40-b0508467ee2f | -2.9912 | -51.3563 | 2024-11-12 00:00:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| b3d52e64-16e3-3205-9801-d0e37b748db2 | -3.8146 | -48.9515 | 2024-11-12 00:00:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 637f5cd0-2b5c-3b11-ae26-af7d342e0b05 | -2.7587 | -49.3497 | 2024-11-12 00:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 178.7 |
| 021177fe-876d-3155-8b6a-dbebf791e0c7 | -17.6266 | -57.5281 | 2024-11-12 00:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 84.0 |
| 2f1b4b55-966b-326f-b4e5-d5b095920c53 | -20.898 | -48.9959 | 2024-11-12 00:00:00 | GOES-16 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 143.8 |
| 1deff95c-7ca2-38dd-a08a-16523310596d | -2.9797 | -49.5342 | 2024-11-12 00:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 776250c7-4907-3e5a-b20a-775f5fe8d67f | -17.6066 | -57.551 | 2024-11-12 00:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 98.1 |
| f86ad2f9-7880-3175-a639-06e502e8846a | -17.5875 | -57.5122 | 2024-11-12 00:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 105.8 |
| 6bc80a0a-674c-346f-90b0-bde37021a8a8 | 2.762 | -60.9598 | 2024-11-12 00:00:00 | GOES-16 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 1f8de738-5347-37a7-8a30-a4e9cf11ca68 | -2.7402 | -49.3502 | 2024-11-12 00:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 81.1 |
| ff98d9ff-c2c9-3611-80f6-31aa08655137 | -2.7773 | -49.3279 | 2024-11-12 00:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 86.2 |
| 2e41a232-e0df-33cf-8fb6-2378758e3acd | 1.0481 | -60.5796 | 2024-11-12 00:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 0dc8a718-8889-31b5-9e32-9f026e1a2961 | -2.9982 | -49.5336 | 2024-11-12 00:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 3cfeb1d6-e3ef-371a-a5d8-a2550784ad0c | -3.8144 | -48.9729 | 2024-11-12 00:00:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| d1e39f0f-7400-31d5-8753-e907abbe4ac2 | 1.0663 | -60.5985 | 2024-11-12 00:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 84.7 |
| aab93bea-def7-3205-b6c3-29403691a302 | -17.6283 | -57.4252 | 2024-11-12 00:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 100.4 |
| 8f471ebc-c47d-38b3-85a4-91dffa72a3ce | -17.6073 | -57.5099 | 2024-11-12 00:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 82.0 |
| 717ca95a-ad3a-387b-83ac-4f5afb7d6ceb | -2.9729 | -51.3361 | 2024-11-12 00:00:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 5392d2a5-46b8-3b5b-bbed-ad916239da0c | -17.6477 | -57.4434 | 2024-11-12 00:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 96.6 |
| 08ba6c0d-a9d3-32b7-92e7-197b9281e99b | -2.9913 | -51.3356 | 2024-11-12 00:00:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 90.8 |
| 79e9cbb8-0026-3be2-aab4-98fcc7a74336 | -17.648 | -57.4229 | 2024-11-12 00:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 123.8 |
| 3287c7ab-552f-39d5-bdab-3ceaf19e0fd1 | -2.7772 | -49.3492 | 2024-11-12 00:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| d477d83a-dec7-360b-9ec8-3b66d233add3 | -17.5872 | -57.5328 | 2024-11-12 00:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 108.3 |
| 3ec79cbc-47e4-3c59-9ad7-2998cf0c8120 | -2.7403 | -49.329 | 2024-11-12 00:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 5df070cb-48ac-3979-b087-65f39d4f4c8b | -20.8774 | -49.0006 | 2024-11-12 00:00:00 | GOES-16 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 95.6 |
| 75c18b0f-0e38-3228-b120-6d93db495a8a | -2.76 | -49.32 | 2024-11-12 00:00:00 | MSG-03 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ac78ec6d-4450-3610-9bda-58591b8678bd | -2.9912 | -51.3563 | 2024-11-12 00:10:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 74e68d73-6357-3666-97a5-2b6a3e0ac010 | 2.762 | -60.9598 | 2024-11-12 00:10:00 | GOES-16 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 83.7 |
| dcc588ae-9231-36c4-9302-4dab3a542ae4 | -17.5875 | -57.5122 | 2024-11-12 00:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 111.2 |
| 7f675d19-c911-339f-8118-6a61528043e4 | -2.7773 | -49.3279 | 2024-11-12 00:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 96.4 |
| 59374b97-b47c-3741-9745-829a773b6fea | -3.1097 | -54.2865 | 2024-11-12 00:10:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 6778dd10-b228-3306-b53d-be67f5557192 | -2.7403 | -49.329 | 2024-11-12 00:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| b27e4964-528f-3ea3-9fff-096a702343a4 | -17.6066 | -57.551 | 2024-11-12 00:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 100.5 |
| b56051d1-9642-372e-8587-1258ab52f90b | -17.6477 | -57.4434 | 2024-11-12 00:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 85.1 |
| b3c44ded-e6fa-39a0-95c5-c56dff6f646a | 1.048 | -60.5986 | 2024-11-12 00:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 89.5 |
| 271bcecf-fa5d-36f1-9092-e14cfa233b55 | 1.0481 | -60.5796 | 2024-11-12 00:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 55.9 |
| fbdb28b8-9b05-30f5-8813-8c351930ed89 | -2.7588 | -49.3285 | 2024-11-12 00:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 181.9 |
| 182f411b-48a4-3095-94a5-2ea8109f33a0 | -17.6283 | -57.4252 | 2024-11-12 00:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 103.1 |
| d7bcdc4e-e65b-38f6-9c9f-0f3e7b5b04a8 | 1.0663 | -60.5985 | 2024-11-12 00:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 91.3 |
| 5bcf2881-5570-3ae9-bed4-a074d8d3ada7 | -17.648 | -57.4229 | 2024-11-12 00:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 109.7 |
| 4ac30ab2-98f6-3b0b-9d88-0613dfc710c1 | -2.7871 | -51.7544 | 2024-11-12 00:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 46f0e4d7-6d85-398e-925d-c52d4d75434a | -17.5872 | -57.5328 | 2024-11-12 00:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 102.2 |
| 45d47366-c8ed-3488-ba4e-4ec665f233d9 | -2.9797 | -49.5342 | 2024-11-12 00:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 8b615250-9e36-3199-8b7f-b3d0f344d62d | -3.1096 | -54.3066 | 2024-11-12 00:10:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 79c0d606-f8b4-3ec7-8e45-8a8e096c444c | -17.6069 | -57.5304 | 2024-11-12 00:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 123.0 |
| 45697581-97e7-3f96-862f-2e361437f6b8 | -6.9747 | -40.0297 | 2024-11-12 00:10:00 | GOES-16 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 75.2 |
| 6600e74a-c2e1-32c7-a899-29726a0c994f | -2.7772 | -49.3492 | 2024-11-12 00:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 102.7 |
| cde16c2b-4c24-3134-9da7-a7783343cd85 | 1.0663 | -60.5795 | 2024-11-12 00:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 55.7 |
| e7bf9c7c-fc07-3b45-baf4-15d343b116ea | -2.9913 | -51.3356 | 2024-11-12 00:10:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 87.8 |
| db726906-ba02-3fda-b5ed-782fa7ea9f33 | -2.7587 | -49.3497 | 2024-11-12 00:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 211.4 |
| 89342f4e-b3ec-3dc7-a46f-e723bd542450 | -2.7402 | -49.3502 | 2024-11-12 00:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 01d4367d-f1f0-3bb6-9221-17e13f05f5a7 | -2.9982 | -49.5336 | 2024-11-12 00:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 6e68087b-efb0-302d-af63-023e36e958c2 | -17.313 | -57.4834 | 2024-11-12 00:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 55.7 |
| bae0bc52-47ae-3c8b-8d9c-c0126565df8b | -3.1097 | -54.2865 | 2024-11-12 00:20:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| d1805380-4e69-3989-8617-ecf9a1f6c47c | -2.9982 | -49.5336 | 2024-11-12 00:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 8fc36f10-0e60-375c-b538-87bc034a4b1a | -17.2936 | -57.4652 | 2024-11-12 00:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 81.6 |
| 402985b9-9700-3aa5-a107-c4a678101fea | 1.0663 | -60.5795 | 2024-11-12 00:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 43341935-9fa2-309c-be74-b9ac76a7eb69 | -17.5875 | -57.5122 | 2024-11-12 00:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 99.3 |
| 5c5750e6-3014-342b-892c-c848c5fe9aaf | -2.7403 | -49.329 | 2024-11-12 00:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 12212c38-3f85-30d7-9d79-91dcf4ab7af5 | -17.6477 | -57.4434 | 2024-11-12 00:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 83.0 |
| fda0608f-8811-38dd-a883-212628490d0d | -2.7588 | -49.3285 | 2024-11-12 00:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 173.9 |
| efb4ca67-6aef-39bd-9a50-a3f51fb2e489 | -17.274 | -57.4675 | 2024-11-12 00:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 66.1 |
| cebabbb2-b8c9-3423-8ca7-aec190291788 | -2.9913 | -51.3356 | 2024-11-12 00:20:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 99eb59d2-1610-3127-82ab-735e9aefed2a | -17.6266 | -57.5281 | 2024-11-12 00:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 82.1 |
| 09dc9719-174e-3608-af6f-501a0a3ca169 | 1.0481 | -60.5796 | 2024-11-12 00:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 46.1 |
| b90632b9-85bd-3d01-98f9-d945fef8f41e | -2.7772 | -49.3492 | 2024-11-12 00:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 93cc1de3-a178-3ce9-99af-e39f8ed5eb5a | -2.7922 | -50.2986 | 2024-11-12 00:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 86.2 |
| a7464858-5fab-39d3-83db-fa043ce049c5 | -17.6283 | -57.4252 | 2024-11-12 00:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 102.0 |
| a12cfc39-0dfc-3f4d-913a-48be62ab32ee | -17.2933 | -57.4857 | 2024-11-12 00:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 106.5 |
| 0a2c4f77-ad09-3ac3-bd2f-e635716c40ad | 1.0663 | -60.5985 | 2024-11-12 00:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 91.2 |
| 253942db-b92b-3d74-a053-ebde41532716 | -17.2737 | -57.488 | 2024-11-12 00:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 97.7 |
| f3b3fb46-575d-3c98-859b-ba40bf895556 | -17.3126 | -57.5039 | 2024-11-12 00:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 55.0 |
| 310a1cee-482e-337b-ae06-cb8d0f9babab | -2.7737 | -50.2992 | 2024-11-12 00:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 105.3 |
| 48ddd35e-4bef-3c89-bda4-0a3b4e19892f | -17.648 | -57.4229 | 2024-11-12 00:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 101.9 |
| 14de45d4-47ce-3479-8124-281f72a4892e | -2.7871 | -51.7544 | 2024-11-12 00:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 3eb6bf6b-993b-3102-8a81-5641468c3631 | -2.7402 | -49.3502 | 2024-11-12 00:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| a39d7bff-b62c-3b9a-9539-10d9e3c95c31 | -2.7587 | -49.3497 | 2024-11-12 00:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 179.1 |
| 39488a9a-d55b-3671-b5b9-de1eda721736 | -3.1096 | -54.3066 | 2024-11-12 00:20:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| a95c082b-357c-3df1-ad3b-8068dfff7d28 | -2.9912 | -51.3563 | 2024-11-12 00:20:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 94fa7c73-3c83-3b6c-9728-e52837ec63ba | -17.5872 | -57.5328 | 2024-11-12 00:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 98.0 |
| 7d08033d-5075-30d4-a622-6226305138b0 | 1.048 | -60.5986 | 2024-11-12 00:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 78.9 |
| d5b05c14-dcfe-3bec-9664-93a61a6f8b5d | -2.7773 | -49.3279 | 2024-11-12 00:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 685acc8f-507d-39de-b3e6-87953e209240 | -17.6069 | -57.5304 | 2024-11-12 00:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 117.6 |
| cbaf5245-2d60-31a5-97a1-416e8d314b2b | -17.6066 | -57.551 | 2024-11-12 00:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 101.2 |
| 54109930-1257-364b-8f50-379e035759ce | -2.9797 | -49.5342 | 2024-11-12 00:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| cb242c1b-d393-3420-8171-0ae63b149a4f | -17.6066 | -57.551 | 2024-11-12 00:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 91.1 |
| c0fea993-ea73-302d-a03d-5fba97f0e3a2 | -3.1096 | -54.3066 | 2024-11-12 00:30:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 011d3ea1-f428-35c2-be3e-7df51be42a6c | -2.9912 | -51.3563 | 2024-11-12 00:30:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 78.2 |
| b9ce6ff1-c665-3310-a09a-492d98785013 | -17.313 | -57.4834 | 2024-11-12 00:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 54.2 |
| be22d306-cfb6-399e-8271-fe60f0348a72 | -17.6266 | -57.5281 | 2024-11-12 00:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 82.3 |
| 38c18568-907d-3886-958d-4bce4b67bcb7 | -2.7772 | -49.3492 | 2024-11-12 00:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 81d5433c-a4ca-3dd3-bd88-1220b58c3d5f | -17.5875 | -57.5122 | 2024-11-12 00:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 90.0 |
| fc76d165-d726-3926-810f-780b4eaa2af2 | -2.7773 | -49.3279 | 2024-11-12 00:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 4848d59a-07c1-3f6d-9ce0-cfdb3d76bab6 | -17.2936 | -57.4652 | 2024-11-12 00:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 69.3 |
| ae4e32fb-6cf1-342c-b5a4-58194d136a39 | -17.648 | -57.4229 | 2024-11-12 00:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 105.3 |


[Clique aqui para ver as próximas entradas](README2.md)

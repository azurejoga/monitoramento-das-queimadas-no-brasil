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
| d62c5377-3975-38d8-bf0c-14ac6b87bb48 | -9.3392 | -64.710503 | 2026-10-06 01:08:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 18c652d4-f11e-3605-a168-f6fb48397be4 | -2.8747 | -54.1726 | 2026-10-06 01:08:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f6f074a1-beaf-37e4-a33f-f3b88a99d2a3 | -8.6158 | -66.941101 | 2026-10-06 01:08:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2fb82699-cdbb-396d-8dd8-429b2b0327cf | -9.676 | -66.812103 | 2026-10-06 01:08:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4181c27d-37a5-3726-ae52-edb673f6259c | -8.3077 | -64.013901 | 2026-10-06 01:08:00 | METOP-B | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 799b7320-fdb3-3272-8e11-464d137be636 | -9.4887 | -63.949699 | 2026-10-06 01:08:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 00062e6d-2e35-371e-a16e-f4ef3f80e769 | -9.4725 | -64.337898 | 2026-10-06 01:08:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4baa271c-43cb-3bf4-a3f8-f420cf023d64 | -3.7 | -58.931801 | 2026-10-06 01:08:00 | METOP-B | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 99a338b4-f3a2-3f21-84de-95a2c1b1e1cb | -7.53 | -70.378601 | 2026-10-06 01:08:00 | METOP-B | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 55817c7f-d6b7-36a3-8388-2ea5c78b63a7 | -9.9721 | -65.012199 | 2026-10-06 01:08:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 6d313399-6a54-32d7-be1a-3ef2191a50a3 | -9.4903 | -63.9566 | 2026-10-06 01:08:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 67cc5559-0e35-3d33-ad8d-03425f6f653a | -9.5433 | -65.682098 | 2026-10-06 01:08:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 61e8bdba-da45-334b-ab20-595ed4c9d70e | -2.942 | -54.156399 | 2026-10-06 01:08:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 589423f7-d715-3afc-ac87-c8d8348e092d | -9.3369 | -68.872704 | 2026-10-06 01:08:00 | METOP-B | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 5f8a4fae-5102-3e9d-b136-34eb21ac22f1 | -8.7815 | -62.873901 | 2026-10-06 01:08:00 | METOP-B | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 98f5eb79-2157-347a-86bd-d47a67c1ec4c | -9.73 | -65.081001 | 2026-10-06 01:08:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 151b90fc-623c-31a5-a196-ae18032948d9 | -9.1186 | -67.701797 | 2026-10-06 01:08:00 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bc814ec3-51dc-3e1f-bcb4-7606f9f7edc7 | -3.6845 | -55.9697 | 2026-10-06 01:08:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1f73c22d-f6b1-3647-8e7e-cc52112daa7a | -9.7234 | -65.097397 | 2026-10-06 01:08:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 3ad7d78a-d805-3ae2-9ce6-487417c777ca | -3.6699 | -55.951599 | 2026-10-06 01:08:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ad0b712a-5ed1-31f7-a022-16426e7ac01c | -8.9764 | -65.442703 | 2026-10-06 01:08:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c19e25eb-92e3-395d-96ea-c163f2c5f861 | -9.1213 | -65.867599 | 2026-10-06 01:08:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a45568b9-fd66-38c4-ad26-4a91dbbfbd7e | -9.1432 | -65.4058 | 2026-10-06 01:08:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f9144635-e31b-32da-801b-3f9099c20cef | -9.1327 | -65.872704 | 2026-10-06 01:08:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3707a686-9077-3896-ba2c-5c205e33bbc0 | -3.0517 | -54.188999 | 2026-10-06 01:08:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9d777ea6-6421-3a49-b612-a2996b60da77 | -3.0554 | -54.246601 | 2026-10-06 01:08:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 06cd24b1-5b89-311f-9beb-bacf6d1dcf17 | -8.9324 | -66.838799 | 2026-10-06 01:08:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f864c3e0-1b81-3edb-b767-1f80c9f9d99c | -3.3623 | -58.194801 | 2026-10-06 01:08:00 | METOP-B | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| da75cdc4-35a0-379f-a2fe-cdb1a222b9af | -8.9979 | -65.400398 | 2026-10-06 01:08:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| dc493d10-429d-380c-8755-7365ac3d94a1 | -14.9109 | -59.381001 | 2026-10-06 01:08:00 | METOP-B | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 45cbb56b-0138-3e80-ba57-8f4358b3ec90 | -9.1613 | -68.237297 | 2026-10-06 01:08:00 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ff082163-cf4c-375a-acc6-cab74eeb5d27 | -9.4596 | -64.326302 | 2026-10-06 01:08:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| cd02d8c5-0dfe-37a6-96fa-9526fe17518a | -9.6778 | -66.820297 | 2026-10-06 01:08:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9316610c-cf90-38bb-94e9-2779f5388800 | -3.0746 | -54.242001 | 2026-10-06 01:08:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6c6db3a2-46da-3a96-8799-661b022992a5 | -9.1066 | -67.741402 | 2026-10-06 01:08:00 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 50c7e6c6-4b48-35d1-97a3-7e6ef9437bdf | -8.347 | -62.9137 | 2026-10-06 01:08:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f7cc639d-d52a-3d03-bbbb-a36abac29652 | -2.9901 | -54.144798 | 2026-10-06 01:08:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f96d4b30-1e19-3142-8c34-de7bf260a974 | -8.9748 | -65.4356 | 2026-10-06 01:08:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 69f472c2-bcc7-39f9-bcb7-6447da33aed9 | -3.0621 | -54.274101 | 2026-10-06 01:08:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3c326914-a987-31b4-bbbe-c4bc36681d2c | -8.6458 | -66.842903 | 2026-10-06 01:08:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1731e688-e58b-3a33-9921-69fac18fd45a | -3.0545 | -54.158798 | 2026-10-06 01:08:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 632e4136-ce3c-30a0-aec8-47c24ac4ff69 | -8.3487 | -62.830898 | 2026-10-06 01:08:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 6e3b7e27-9776-3ca8-9fdd-f51b92a49a1b | -3.3754 | -58.206902 | 2026-10-06 01:08:00 | METOP-B | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 16a5fec9-be1d-360f-88e1-4e124e020eaa | -2.8486 | -54.149101 | 2026-10-06 01:08:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a38f5cbc-3c44-391f-8c8f-8e9454be3e45 | -8.5409 | -66.974197 | 2026-10-06 01:08:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 79c84734-b897-3a1f-8901-b57592d84712 | -9.7398 | -65.078796 | 2026-10-06 01:08:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 63fd305e-a94a-3bb7-9f09-aeda47009a94 | -8.9226 | -66.841003 | 2026-10-06 01:08:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 688d6ea3-f10a-352d-a8b7-576e8c01b753 | -10.5911 | -67.8834 | 2026-10-06 01:08:00 | METOP-B | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 4e4d4dc2-f993-3560-bd1e-a751b68ee382 | -14.9129 | -59.3895 | 2026-10-06 01:08:00 | METOP-B | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5c52c25b-81c7-3585-81ff-9a2deb1ae5c0 | -3.0889 | -53.754299 | 2026-10-06 01:08:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ecfa3c62-badd-3ae9-abc0-1cfc0473a781 | -2.8583 | -54.146801 | 2026-10-06 01:08:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e75d87ea-ae26-395e-a17c-96a43054c0ee | -9.4612 | -64.333199 | 2026-10-06 01:08:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1921dc64-a066-384d-b3f9-57ce03592ee4 | -9.1392 | -65.902298 | 2026-10-06 01:08:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8596d153-3667-353b-abcc-6c924adf45b6 | -3.0641 | -54.156502 | 2026-10-06 01:08:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c540baba-132b-3d3b-938c-4ce5c90e88ff | -2.758 | -54.110802 | 2026-10-06 01:08:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b9894999-2f8a-3ee1-aba9-9d3e019a7770 | -2.9805 | -54.147099 | 2026-10-06 01:08:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3bf771fe-b4c6-3a3d-91f3-6705ee17db06 | -3.6651 | -55.9743 | 2026-10-06 01:08:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fc7c0c7f-8e87-376c-ba6e-9cd0f1320bf7 | -3.0738 | -54.154202 | 2026-10-06 01:08:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| be9dbb27-fbe8-3e60-ba11-b242a082fd91 | -3.0021 | -53.899899 | 2026-10-06 01:08:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 408bc928-6d72-3035-b633-82e75ead40e3 | -2.9064 | -54.135201 | 2026-10-06 01:08:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8534ae7e-3bc6-30ec-9e8a-b30fe0e2d705 | -8.85 | -66.790199 | 2026-10-06 01:08:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d8fded37-2dbf-3828-82fd-aabbd2d2b06e | 3.5757 | -61.324501 | 2026-10-06 01:08:00 | METOP-B | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 9c089384-87b7-3131-ab7f-61dc2248588b | -8.939 | -67.343597 | 2026-10-06 01:08:00 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3364e23a-9c92-3e19-90c4-1c441936fc82 | -9.2293 | -67.883904 | 2026-10-06 01:08:00 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| affbe54d-1b8d-3ecd-9784-11e1439aa998 | -3.0902 | -54.179798 | 2026-10-06 01:08:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3447ab97-5c2a-3a75-893e-277e784ec76f | -9.1311 | -65.865402 | 2026-10-06 01:08:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1114f178-7914-3d1c-8d11-266b12278627 | -10.2774 | -60.5485 | 2026-10-06 01:08:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c4f2ff35-ce56-30ad-b383-d6e39c93e761 | -9.7218 | -65.090302 | 2026-10-06 01:08:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 91074845-9e57-36d6-86a5-42dbb1169a0c | -9.1295 | -65.858002 | 2026-10-06 01:08:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5d8a9c91-8cad-37d1-a6ea-79a2f799da31 | -9.9737 | -65.019302 | 2026-10-06 01:08:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a8cdced2-cbdd-3137-aadb-57bceab21253 | -9.5468 | -64.810799 | 2026-10-06 01:08:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1a222b02-7ddd-3fe5-bc6c-b06a563cfc22 | -9.0764 | -65.383102 | 2026-10-06 01:08:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2834c9e1-52f1-3dbd-bfdf-5ad781405886 | -3.6748 | -55.972 | 2026-10-06 01:08:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2bcba38e-282a-3aa0-b993-ae9a8964361e | -9.4395 | -67.095299 | 2026-10-06 01:08:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 98bd22ae-b22a-37d0-9a50-6cc5ae14e249 | -9.1167 | -67.693001 | 2026-10-06 01:08:00 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a5c0ac65-2854-3ad3-930a-6b17713af44d | -9.2313 | -67.892998 | 2026-10-06 01:08:00 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 61d7efe1-0fbe-377a-9cb8-3d5f26ee4d5b | -9.4892 | -64.0438 | 2026-10-06 01:08:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 98176b9d-99f4-3ab3-8927-eb6a841c9810 | -9.8266 | -65.052002 | 2026-10-06 01:08:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ebb0e37c-fddc-3c86-a6bc-8a5999da7566 | -3.3657 | -58.209202 | 2026-10-06 01:08:00 | METOP-B | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f7430eb3-6f86-33de-90b1-17f0b80e10a3 | -9.9442 | -62.273602 | 2026-10-06 01:08:00 | METOP-B | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 826c0a75-e0de-373d-922f-f94f030d1ea9 | -9.1117 | -64.382698 | 2026-10-06 01:08:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 3612575c-768a-30f0-aab5-d0ce85f9eed9 | -3.372 | -58.192501 | 2026-10-06 01:08:00 | METOP-B | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b028e40c-638d-360f-8612-51510265307a | -14.5447 | -59.757401 | 2026-10-06 01:08:00 | METOP-B | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2d6dff38-7bc2-3461-b68e-36ca06705170 | -3.3788 | -58.221401 | 2026-10-06 01:08:00 | METOP-B | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9978d8be-f879-34c8-93fd-e28574a400fc | -9.105 | -67.686302 | 2026-10-06 01:08:00 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7c1583d6-9b85-3df2-a1d4-296a8946665c | -14.9344 | -59.3932 | 2026-10-06 01:08:00 | METOP-B | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5fd58090-aa1e-3ea8-8a02-4a23af574474 | -3.0717 | -54.271801 | 2026-10-06 01:08:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 67e4f3fd-3deb-39ce-a688-3db338be47e4 | -9.4941 | -67.779999 | 2026-10-06 01:08:00 | METOP-B | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| d66797e8-0772-3314-88f7-9b7a8746ce39 | -2.8651 | -54.1749 | 2026-10-06 01:08:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cc0b158d-a95d-31ce-a305-ec046b36dc6d | -2.8554 | -54.1772 | 2026-10-06 01:08:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6901b657-3767-3bd3-9820-c4a790fa29af | -9.1205 | -67.710602 | 2026-10-06 01:08:00 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3fe48f12-07ea-3e5a-946f-c4c38c3e3c2b | -9.4733 | -67.061897 | 2026-10-06 01:08:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7929f6d7-165b-353b-ba4f-87fc619eca0d | -3.0613 | -54.186699 | 2026-10-06 01:08:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 47aab56a-56e8-383a-8663-a39d08cab3f4 | -3.6796 | -55.9492 | 2026-10-06 01:08:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c696b2aa-a1d2-3671-a1f0-8b3a022a492e | -8.6295 | -69.492302 | 2026-10-06 01:08:00 | METOP-B | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 54617a54-d758-3aca-9230-75fa5fb90383 | -9.1049 | -68.308899 | 2026-10-06 01:08:00 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| acab0dcb-9ee0-3da0-b748-d41eb64720da | -2.7813 | -57.687901 | 2026-10-06 01:08:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| af98c15e-e189-300f-ad8e-d62ab0acb7ca | -3.0721 | -53.726799 | 2026-10-06 01:08:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a8360d20-9b43-3bc3-8b85-c62b5e2ce7dd | -8.9209 | -66.833 | 2026-10-06 01:08:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6f9d0ed4-894f-3c4a-8b1a-2515d2e45a5f | -3.3691 | -58.223598 | 2026-10-06 01:08:00 | METOP-B | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README10.md)

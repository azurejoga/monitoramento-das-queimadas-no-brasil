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
| f2245100-c1eb-37ea-880a-2bf29976b194 | 1.9237 | -60.3639 | 2026-02-24 00:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 64.1 |
| fb2d2f23-7f4d-337f-86f5-3c1e994ff1f4 | 1.8321 | -60.6114 | 2026-02-24 00:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 4c4cdcf8-f443-3c3f-bf20-87b0a121dd29 | 2.2333 | -60.7018 | 2026-02-24 00:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 53.5 |
| f345cd20-2bd0-3f9e-b58d-b09281fa04c4 | 2.7087 | -60.2588 | 2026-02-24 00:00:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 144f7432-9753-341f-b857-808937852df4 | 1.9419 | -60.3637 | 2026-02-24 00:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 153.5 |
| d885b0c6-2336-324d-9f8b-1665588dff10 | 2.7088 | -60.2398 | 2026-02-24 00:00:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 92.1 |
| 2639e9eb-d535-3c39-98f2-f31d642109a3 | 1.9419 | -60.3447 | 2026-02-24 00:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 39126cc8-a285-3717-8216-a632ceafcdce | -9.46823 | -35.5946 | 2026-02-24 00:05:00 | TERRA_M-M | PARIPUEIRA | ALAGOAS | Brasil | 2706448 | 27 | 33 | nan | nan | nan | Mata Atlântica | 40.0 |
| 8abf3e4d-6f0f-3a9e-88ac-0b404c6f953e | -9.47477 | -35.58818 | 2026-02-24 00:05:00 | TERRA_M-M | MACEIÓ | ALAGOAS | Brasil | 2704302 | 27 | 33 | nan | nan | nan | Mata Atlântica | 35.5 |
| 767f53b5-522f-3259-ac80-e54286752a25 | -4.73916 | -46.65635 | 2026-02-24 00:07:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 14.0 |
| c0de4cf9-ac6b-3df6-b3e1-22bf083e5e26 | 1.8321 | -60.6114 | 2026-02-24 00:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 39.8 |
| a584cee9-c3ed-3c4b-bf2b-0e9a1471461e | 1.9419 | -60.3447 | 2026-02-24 00:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 879849b4-5f1f-3070-8eaa-316121375640 | 2.7088 | -60.2398 | 2026-02-24 00:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 70.4 |
| b5b3865d-0786-372e-88aa-f008f63beaba | 1.9602 | -60.3635 | 2026-02-24 00:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 949e091d-6417-39b8-a285-af0c9c1a1ca6 | 2.7087 | -60.2588 | 2026-02-24 00:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 8eec6db2-7c34-3fbc-8727-44067571d698 | 2.2333 | -60.7018 | 2026-02-24 00:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 44.0 |
| b7358019-0704-38c2-8b8e-f6181df145cf | 1.9237 | -60.3639 | 2026-02-24 00:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 271988a8-4c98-3668-9d0e-55492308ffca | 1.9419 | -60.3637 | 2026-02-24 00:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 136.9 |
| 76cd18f9-2e39-3233-9414-3f901c83d638 | 2.2333 | -60.7018 | 2026-02-24 00:20:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 42.6 |
| db1720b1-0351-31b4-b4e7-76ee1785c6b9 | 2.7088 | -60.2398 | 2026-02-24 00:20:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 688d3bc5-f485-363f-8a3d-e96b69ab2a13 | 2.7087 | -60.2588 | 2026-02-24 00:20:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 13d43043-a81a-30ae-803a-0e80f4bd30ea | 1.9419 | -60.3637 | 2026-02-24 00:20:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 124.3 |
| f8959c01-b8c6-31a8-9beb-b3535d525c32 | 1.8321 | -60.6114 | 2026-02-24 00:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 44.2 |
| aa3fa2ec-4606-30b7-9675-e8038bef1c48 | 1.9419 | -60.3447 | 2026-02-24 00:20:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 42.6 |
| 2f3ba1e5-52c0-3244-8312-edf4d1a1c535 | 1.9237 | -60.3639 | 2026-02-24 00:20:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 4bfeecb9-97c0-39fb-836f-8d4514ec27d9 | 1.9419 | -60.3827 | 2026-02-24 00:20:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 41.9 |
| 3d6bd463-19e1-35bf-a041-8b7c037ceb13 | 1.9419 | -60.3827 | 2026-02-24 00:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 39.9 |
| 19a559d4-b079-3401-b9f6-a74fd1877a35 | 1.9419 | -60.3637 | 2026-02-24 00:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 136.7 |
| a1e1a03f-0f2e-31eb-bc4a-ba962dda409b | 2.7088 | -60.2398 | 2026-02-24 00:30:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 2d43efed-ca76-300e-b3aa-518945c6d6b0 | 2.2333 | -60.7018 | 2026-02-24 00:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 747fc276-93eb-3b36-9c71-a43dffeeb39a | 1.8321 | -60.6114 | 2026-02-24 00:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 42.9 |
| 6f6c08e8-cdcb-3dea-a1fb-67ba9e27192f | 1.9237 | -60.3639 | 2026-02-24 00:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 59.7 |
| d9f6a1d6-8636-3a4b-9376-8e702888f496 | 1.9419 | -60.3447 | 2026-02-24 00:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 43.7 |
| a609accc-a50d-3378-ae43-d55d989113ee | 1.9236 | -60.3829 | 2026-02-24 00:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 38.9 |
| b598bb37-1955-3e3c-bb81-e0970f58cf95 | 1.9602 | -60.3635 | 2026-02-24 00:40:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 37.7 |
| 6848a8d7-e584-39fb-8190-dd7240e823eb | 2.7088 | -60.2398 | 2026-02-24 00:40:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 9fcc6bb4-24c9-330e-87bc-ba39c5604ca3 | 1.9236 | -60.3829 | 2026-02-24 00:40:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 43.7 |
| e1a36092-2aca-3d6a-a991-f6a2b7c5218c | 1.9419 | -60.3447 | 2026-02-24 00:40:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 31e982c7-133d-3bfd-ad23-d6056123ac7c | 1.9419 | -60.3637 | 2026-02-24 00:40:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 119.3 |
| ef0487c5-1b47-3d39-85d9-77066aff95d2 | 1.9237 | -60.3639 | 2026-02-24 00:40:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 67.9 |
| f659e1d8-03ef-3cc1-b09f-93462a819ec5 | 2.7088 | -60.2398 | 2026-02-24 00:50:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 6b9ffddb-fc67-3906-85e1-b11676588157 | 1.9237 | -60.3639 | 2026-02-24 00:50:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 80860b6a-40e7-3d36-ad31-bc5f9bd3eaeb | 1.9602 | -60.3635 | 2026-02-24 00:50:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 40.6 |
| 44a84aac-9cf6-3b11-a8dd-38fbaaf50321 | 1.9419 | -60.3447 | 2026-02-24 00:50:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 40.3 |
| 20b1d902-dc0a-3f82-b104-2f8537aad584 | 1.9419 | -60.3827 | 2026-02-24 00:50:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 40.1 |
| 3a9b8b90-dcc5-32e9-ad69-87aef5fe0467 | 1.9236 | -60.3829 | 2026-02-24 00:50:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 54.9 |
| c7eb9912-dd5f-37e3-8393-b100c3299af6 | 1.9419 | -60.3637 | 2026-02-24 00:50:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 108.7 |
| f77c075e-549f-3789-8d1e-637806ee1406 | 2.7088 | -60.2398 | 2026-02-24 01:00:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 47.9 |
| d492431e-a277-3bba-8099-84cc94be32f1 | 1.9419 | -60.3637 | 2026-02-24 01:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 109.5 |
| 3a870682-4ef0-373f-acd9-dc9aa2417a1a | 1.9237 | -60.3639 | 2026-02-24 01:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 7696df2d-13c7-351d-a117-c9540095d43e | 1.9236 | -60.3829 | 2026-02-24 01:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 38.6 |
| 007eb19b-4f5c-34ca-bce5-219d520fa52f | 1.9419 | -60.3447 | 2026-02-24 01:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 41.0 |
| 0fb19dc9-a571-3a08-9d26-d777262567db | 2.2333 | -60.7018 | 2026-02-24 01:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 31.8 |
| c2780f7c-1b8b-3b45-8f7c-a82fe7ae003b | 1.9419 | -60.3637 | 2026-02-24 01:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 110.4 |
| 510e6079-c2e2-3869-ac51-c44e7498026f | 1.9237 | -60.3639 | 2026-02-24 01:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 53.9 |
| d8ed2497-20c0-3af6-9a16-e6a2cdec6208 | 2.7088 | -60.2398 | 2026-02-24 01:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 44.8 |
| b7eefa18-9802-3734-8fee-63de1eec1cea | 1.9419 | -60.3637 | 2026-02-24 01:20:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 95.6 |
| 02133a01-6f6b-353a-83c4-077e254d180e | 2.7088 | -60.2398 | 2026-02-24 01:20:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 41.7 |
| f68688d0-5416-361a-a26e-fbb2a7543d70 | 1.9237 | -60.3639 | 2026-02-24 01:20:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 5164e0b6-0860-33c4-8745-59d4d9737314 | 2.7088 | -60.2398 | 2026-02-24 01:30:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 38.5 |
| 70cc5f41-fe8c-3b36-be60-a5b83da3d567 | 1.9419 | -60.3637 | 2026-02-24 01:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 89.8 |
| 79d19214-759b-34f8-bf83-2eb54a287936 | 1.9237 | -60.3639 | 2026-02-24 01:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 4be49e0f-2460-3456-b06a-d32bcb222271 | 1.9237 | -60.3639 | 2026-02-24 01:40:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 7e4bdcd4-69e7-33d5-ba96-6d0678c09869 | 1.9419 | -60.3637 | 2026-02-24 01:40:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 91.0 |
| 56e9cea1-2f9c-3193-af9b-fe8d3909de35 | 1.9237 | -60.3639 | 2026-02-24 01:50:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 753a213b-f594-36c5-9d20-1a8b963cc262 | 1.9419 | -60.3447 | 2026-02-24 01:50:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 38.8 |
| af3864b8-4435-3dc6-968e-374f60150ab3 | 1.9419 | -60.3637 | 2026-02-24 01:50:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 7ab75a20-04a8-3509-80d3-760fdab00421 | 1.9419 | -60.3637 | 2026-02-24 02:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 92f97b13-dcb6-35c7-8efd-2151e80408a9 | 1.9237 | -60.3639 | 2026-02-24 02:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 6170551f-cec3-37af-a5cc-909f950a89f4 | 1.9419 | -60.3637 | 2026-02-24 02:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 99.2 |
| cfaa67f9-408b-32cd-ae88-93a89f5e0ff6 | 3.1661 | -59.9848 | 2026-02-24 02:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 39.4 |
| 51eb778b-b02c-3f33-be40-3205332d8600 | 3.1478 | -59.9851 | 2026-02-24 02:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 140162d2-c364-3090-a91c-4feca71c5a1b | 1.9237 | -60.3639 | 2026-02-24 02:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 42.8 |
| da4b44d5-55dc-39d0-a7b8-fbfa1a69e6da | 1.9419 | -60.3637 | 2026-02-24 02:20:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 93.8 |
| 30262d44-6e31-3bf9-b77a-c3378be30b6a | 1.9237 | -60.3639 | 2026-02-24 02:20:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 45.0 |
| 8655aa32-2f4a-3b7c-aaf6-861e28cab58d | 1.9237 | -60.3639 | 2026-02-24 02:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 42.8 |
| 7961a83f-0065-3f3b-aa39-d4d90306e912 | 1.9419 | -60.3637 | 2026-02-24 02:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 88.9 |
| 2a9b7f91-d099-37a2-bfff-54fdafa78cd4 | 1.9419 | -60.3637 | 2026-02-24 02:40:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 469345f5-8425-324c-81b7-56a786ac5449 | 1.9419 | -60.3637 | 2026-02-24 02:50:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 528ed5d3-6749-3569-840f-d3e4e184b1fc | 1.9237 | -60.3639 | 2026-02-24 02:50:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 40.9 |
| 40ad444f-1e04-371c-a384-0ab5527e8371 | -10.24832 | -36.30695 | 2026-02-24 02:53:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| d977eb78-7e6a-31aa-89d4-3df06961907d | -7.87675 | -35.22821 | 2026-02-24 02:53:00 | NOAA-20 | CARPINA | PERNAMBUCO | Brasil | 2604007 | 26 | 33 | nan | nan | nan | Mata Atlântica | 11.2 |
| 109f0d96-0cd9-39c6-852c-e8539839ae15 | -10.24522 | -36.30978 | 2026-02-24 02:53:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| e78a6262-6bd8-3b16-9aad-ef61a660b2ca | -10.24946 | -36.3012 | 2026-02-24 02:53:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 8183e5e4-34e0-3d2b-bad3-1f229bf99055 | -10.25296 | -36.30553 | 2026-02-24 02:53:00 | NOAA-20 | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 98d5b0ed-1717-3fe3-9e8a-0077c9c4a5e8 | -7.87655 | -35.22708 | 2026-02-24 02:53:00 | NOAA-20 | CARPINA | PERNAMBUCO | Brasil | 2604007 | 26 | 33 | nan | nan | nan | Mata Atlântica | 11.2 |
| d729de12-7770-3a71-acc5-5f87b3f57d7f | -10.24639 | -36.30409 | 2026-02-24 02:53:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 4fd09894-a484-331b-9ce7-1272d7016238 | 1.9419 | -60.3637 | 2026-02-24 03:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 914ed975-a957-3de4-88cf-d9a7c3f84e11 | 1.9419 | -60.3637 | 2026-02-24 03:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 72.4 |
| f256ab6a-adf7-312e-aaaf-efe5a7d820dd | 1.9237 | -60.3639 | 2026-02-24 03:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 39.8 |
| dc2a55fe-1ff2-3212-b428-e0bdd3793efe | 1.9419 | -60.3637 | 2026-02-24 03:20:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 9268d2d4-10b1-3f0b-8fcb-b6a1f58b3e66 | 1.9419 | -60.3637 | 2026-02-24 03:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 2759ea7d-e5e8-368b-a3de-43bad898a0d1 | 1.9419 | -60.3637 | 2026-02-24 03:40:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 68.5 |
| e498ef6f-7f2b-3feb-a971-675386d60f9f | -6.23787 | -37.47216 | 2026-02-24 03:44:00 | NOAA-21 | SÃO JOSÉ DO BREJO DO CRUZ | PARAÍBA | Brasil | 2514651 | 25 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4261da2d-0919-3c75-a707-1709aaa2cc40 | -10.85174 | -37.53928 | 2026-02-24 03:44:00 | NOAA-21 | LAGARTO | SERGIPE | Brasil | 2803500 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| a638ac74-8810-3737-9407-66066218e923 | -9.71372 | -36.94715 | 2026-02-24 03:44:00 | NOAA-21 | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d71aded0-d6ac-3373-a38d-5ca88957f5fd | -9.62969 | -36.94084 | 2026-02-24 03:44:00 | NOAA-21 | GIRAU DO PONCIANO | ALAGOAS | Brasil | 2702900 | 27 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4d58fc2e-493e-3bb6-854b-ee6c30aa4ad4 | -9.63245 | -36.94491 | 2026-02-24 03:44:00 | NOAA-21 | GIRAU DO PONCIANO | ALAGOAS | Brasil | 2702900 | 27 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 16e2c8dd-813c-3286-a07b-f8f779e5971f | -8.69934 | -40.67929 | 2026-02-24 03:44:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 71f8ddce-517b-36f7-a287-49798a29bb01 | -9.81201 | -38.10361 | 2026-02-24 03:44:00 | NOAA-21 | SANTA BRÍGIDA | BAHIA | Brasil | 2927606 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |


[Clique aqui para ver as próximas entradas](README2.md)

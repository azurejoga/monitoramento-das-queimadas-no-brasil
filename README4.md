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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cafd1fbb-8481-33a9-9cab-913ed1747382 | 2.689 | -60.9797 | 2024-11-13 00:10:00 | GOES-16 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 0d695203-cacb-367c-bfec-0e1aae47fd3b | -2.2479 | -53.7627 | 2024-11-13 00:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 183.2 |
| c32e0ead-e874-325e-a134-26e1cf464985 | -1.6627 | -52.5357 | 2024-11-13 00:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 39.2 |
| b5c52d9c-629e-335f-9a51-b00c62d76751 | -21.2181 | -47.1261 | 2024-11-13 00:10:00 | GOES-16 | CÁSSIA DOS COQUEIROS | SÃO PAULO | Brasil | 3510906 | 35 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 7f31c861-4992-36de-9a22-5fa2030c7374 | -2.9925 | -51.0242 | 2024-11-13 00:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 79.7 |
| a4253fbd-6df0-3fd8-9fdc-a5962c633d49 | -3.0504 | -50.3332 | 2024-11-13 00:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 88.5 |
| 3ff2123a-3d7d-343f-9528-92ff2812014d | -3.5743 | -53.0218 | 2024-11-13 00:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 88.8 |
| 8db6f70d-80fa-3b9d-ba82-4a6f37b52b33 | -2.7374 | -45.2877 | 2024-11-13 00:10:00 | GOES-16 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 8b59f7a0-9985-358f-82e2-50158751883b | -2.2295 | -53.7631 | 2024-11-13 00:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 846b9e0d-421b-3428-8bf7-32d2e997f057 | -3.5098 | -50.8415 | 2024-11-13 00:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 33.7 |
| 19fa06ff-e580-3802-a17b-3eee6aa850e4 | -5.3587 | -43.529 | 2024-11-13 00:10:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 36a761fd-8886-37e2-bb84-3aff8032d887 | -2.9924 | -51.045 | 2024-11-13 00:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| f788c515-ce9a-3829-a9aa-746d6b791602 | -4.4265 | -48.8395 | 2024-11-13 00:10:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| eb7466bd-c0a1-337a-96d5-5e295a64cdb9 | -3.9447 | -45.780602 | 2024-11-13 00:12:00 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c71e6a85-8420-3b86-bb7c-a7ac965f23f2 | -2.6453 | -51.712601 | 2024-11-13 00:12:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4c99f862-136e-38a0-9713-5486c73c0ef3 | -16.136499 | -43.571999 | 2024-11-13 00:12:00 | METOP-C | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| b0c7b390-2e5a-39b8-8a81-cc7c179cc555 | -16.1343 | -43.5611 | 2024-11-13 00:12:00 | METOP-C | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| af50d39e-5396-3013-b7ab-a98282b83e8b | -2.007 | -48.018299 | 2024-11-13 00:12:00 | METOP-C | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0bb471a2-0332-39dc-9346-9c648adc658d | -1.5929 | -47.0075 | 2024-11-13 00:12:00 | METOP-C | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| de68ee07-0664-3856-b253-a49b579f9681 | -2.2405 | -53.739899 | 2024-11-13 00:12:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8826dc0b-d44a-3b50-b0fa-37ea6c72a6ba | -2.2383 | -53.774899 | 2024-11-13 00:12:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6905624b-4f94-3ad0-adbb-0f4d9202c25c | -2.1947 | -53.715401 | 2024-11-13 00:12:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 63524f09-2067-35c1-915e-7bc648353659 | -2.01 | -48.0313 | 2024-11-13 00:12:00 | METOP-C | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7db2cf1d-dffe-3a8d-bc64-141241c90fbb | -2.2309 | -53.742001 | 2024-11-13 00:12:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1f317498-dccd-3d54-b40e-e03cb147a4c2 | -1.6453 | -52.5401 | 2024-11-13 00:12:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7e8ea616-d9ab-3044-8c2b-69a917048c31 | -1.5905 | -46.996601 | 2024-11-13 00:12:00 | METOP-C | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6557f1ba-326c-3b69-aeba-aa8b2479410d | -1.8504 | -47.824699 | 2024-11-13 00:12:00 | METOP-C | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dcaf0a6b-ce42-3369-9ffd-073c549e1b50 | -2.2213 | -53.744099 | 2024-11-13 00:12:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b3256ebd-cd9d-3ba0-8dc1-5e4500b04dd1 | -2.6549 | -51.710499 | 2024-11-13 00:12:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1b7c8319-1e99-35c4-bc53-58b615f28c2b | -2.2021 | -53.748199 | 2024-11-13 00:12:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4c96f84e-7d15-3331-86bc-92e6becb989a | -3.9425 | -45.770699 | 2024-11-13 00:12:00 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a6f20d5d-75e1-3b77-9782-b9a9fd8589ed | -1.574 | -47.330502 | 2024-11-13 00:12:00 | METOP-C | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 392197f8-e7d8-3315-87b8-bfe52399501a | -1.5766 | -47.341999 | 2024-11-13 00:12:00 | METOP-C | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d76b3f94-216d-3ab2-a41b-64d6d184db9f | -2.2139 | -53.7113 | 2024-11-13 00:12:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1511bc58-88c1-3be1-b207-a3c323bc7a1e | -1.606 | -46.251801 | 2024-11-13 00:12:00 | METOP-C | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9c8fe34d-1406-3e3d-b1c9-403f12124a83 | -5.0511 | -40.030399 | 2024-11-13 00:12:00 | METOP-C | MONSENHOR TABOSA | CEARÁ | Brasil | 2308609 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 479ca3e0-03a0-36cb-8e0a-a8693320fdb8 | -5.6137 | -44.884899 | 2024-11-13 00:12:00 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a50c6f60-8298-31f8-9b74-780e64aebf6f | -1.3831 | -47.123402 | 2024-11-13 00:12:00 | METOP-C | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a7eb62f9-12f1-3ed6-9293-8478eecd0a8f | -2.2235 | -53.709202 | 2024-11-13 00:12:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 628b1e15-54cb-3501-8505-15faf2eddb9d | -1.6393 | -52.513599 | 2024-11-13 00:12:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 85c0a0d1-0e61-3de2-8ceb-e1e131ff5d07 | -3.31 | -40.041901 | 2024-11-13 00:12:00 | METOP-C | MORRINHOS | CEARÁ | Brasil | 2308906 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 6943046e-2a9b-34e2-a1a5-9ae2ae751b8f | -2.2331 | -53.7071 | 2024-11-13 00:12:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 006cd601-07ea-36c4-8d33-71d1425e1b86 | -4.3636 | -48.078201 | 2024-11-13 00:12:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4304efeb-c060-355e-b3e0-875d530f0a22 | -5.3587 | -43.529 | 2024-11-13 00:20:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 85.5 |
| ec9fff58-8a60-39dc-8846-e88d492c24aa | -3.9483 | -48.1724 | 2024-11-13 00:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| c7ae0d51-f57b-30d5-b85a-eeb502e48f2d | -3.1321 | -59.0098 | 2024-11-13 00:20:00 | GOES-16 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 84ce972f-eec4-3d75-91e8-8ca671e4a291 | -2.7374 | -45.2877 | 2024-11-13 00:20:00 | GOES-16 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 38.9 |
| f4292d2c-5af4-3fdd-be14-51ed19dfa58b | -2.9925 | -51.0242 | 2024-11-13 00:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| c3a3c72d-8fa7-3621-9bde-90ea8c914a77 | -3.1096 | -54.3066 | 2024-11-13 00:20:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 2668e06a-9b27-3523-9217-0dd419db3474 | -3.4913 | -50.8421 | 2024-11-13 00:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 186830d6-6406-31b6-b068-a91dc28da563 | 1.0663 | -60.5985 | 2024-11-13 00:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 136.3 |
| 8088d3b7-4b8c-3b0d-8120-4731fa4a34a8 | -21.2181 | -47.1261 | 2024-11-13 00:20:00 | GOES-16 | CÁSSIA DOS COQUEIROS | SÃO PAULO | Brasil | 3510906 | 35 | 33 | nan | nan | nan | Cerrado | 97.1 |
| c270f473-79a9-38fd-b132-1adbf6e0c895 | -3.5743 | -53.0218 | 2024-11-13 00:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 102.9 |
| 2bc6a568-b4b9-336d-a673-7eebf54e60dd | -3.0504 | -50.3332 | 2024-11-13 00:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 94.3 |
| f900b34e-1c17-39e6-8d43-e063cc1b5f1d | -3.5098 | -50.8415 | 2024-11-13 00:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 237a72fb-1a27-3244-8c18-5394909cd238 | -3.6791 | -50.1653 | 2024-11-13 00:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 47.2 |
| a821750b-7e2c-32f7-a332-df2c7601a3fb | -3.1501 | -53.2574 | 2024-11-13 00:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 31.3 |
| 8c25277c-913e-329f-9829-1020dbd203b6 | -3.5928 | -53.0009 | 2024-11-13 00:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 47.9 |
| b851947d-c760-3807-a3ac-812babce7328 | -1.6444 | -52.536 | 2024-11-13 00:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 36.8 |
| 9bb5b258-b65b-31e4-bbef-627d0cb493af | 1.048 | -60.5986 | 2024-11-13 00:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 141.8 |
| 04204b82-d1cb-327b-98ee-383d1af01832 | -3.0913 | -54.307 | 2024-11-13 00:20:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 1fba0932-545e-327a-9dc1-79ed452e2061 | -2.2663 | -53.7422 | 2024-11-13 00:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 91b973c6-e814-30cc-8ddd-408ce3aff87c | -3.1501 | -53.2371 | 2024-11-13 00:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 6d7c00ba-ec46-3688-a4ae-b3143bb37ea9 | -3.0505 | -50.3122 | 2024-11-13 00:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 41.0 |
| 1f60dc3f-ce1e-3c19-aeb1-61a1c2b119f5 | -2.2112 | -53.7432 | 2024-11-13 00:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| b642877a-2e13-3352-9e85-2800a3055985 | -2.9924 | -51.045 | 2024-11-13 00:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 3cebf758-bf9d-30cb-b9cc-16b66200a74a | -3.0689 | -50.3326 | 2024-11-13 00:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 82.9 |
| 7ff9d627-0616-3605-84ed-a5dcf2de8a98 | -21.0044 | -47.4141 | 2024-11-13 00:20:00 | GOES-16 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 72.7 |
| d238fc65-5821-3648-8b0f-77c5d7be05f6 | -1.6627 | -52.5357 | 2024-11-13 00:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 33.8 |
| 3b259946-d76a-3de5-a9a0-7acb2296d0c8 | -2.2295 | -53.7631 | 2024-11-13 00:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 83.9 |
| 375beb84-ac4a-318d-8249-47e1d04eb5bb | -2.248 | -53.7426 | 2024-11-13 00:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 241.4 |
| b3892d67-8ebd-3711-a6b3-f559a681d1c5 | -2.7189 | -45.2883 | 2024-11-13 00:20:00 | GOES-16 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 39.2 |
| 1c8568a5-78d2-3091-8410-877a86a2c9c6 | -2.2296 | -53.7429 | 2024-11-13 00:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 144.5 |
| ccef7c22-8f62-3e9a-97cc-51dd0564d517 | -3.2495 | -43.2547 | 2024-11-13 00:20:00 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 20a1e12e-3974-353a-a8a6-9c604baa2b94 | -10.7425 | -49.5244 | 2024-11-13 00:20:00 | GOES-16 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 63.8 |
| df763a0e-7f75-3619-8cd6-757a2dce44db | -2.2479 | -53.7627 | 2024-11-13 00:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 137.7 |
| cb69a868-c625-3132-953b-debebe05435b | -3.5743 | -53.0015 | 2024-11-13 00:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 149.1 |
| 20fac803-8913-31a9-8d39-8a74ea0d9f36 | -4.4265 | -48.8395 | 2024-11-13 00:20:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| b7035c98-1333-3388-9181-7c30c73e556f | -2.7033 | -49.3513 | 2024-11-13 00:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 44.2 |
| b070b90a-a080-3887-b6d3-8384721333b8 | -3.4914 | -50.8213 | 2024-11-13 00:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 873da7eb-2258-3b3e-97bf-6fa812179ac7 | 1.0663 | -60.6174 | 2024-11-13 00:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 66bac353-271d-3951-ace2-54d3618ef2a3 | -3.1096 | -54.3066 | 2024-11-13 00:30:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 075999db-6aa8-3923-a2a8-faa5cac9451b | -1.6444 | -52.536 | 2024-11-13 00:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 28.0 |
| 463540bf-33ac-3600-a974-7a38d88a16c0 | -2.9925 | -51.0242 | 2024-11-13 00:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 08da6039-5c57-346c-a776-41dfdbe73f1c | -2.7374 | -45.2877 | 2024-11-13 00:30:00 | GOES-16 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 39.5 |
| 3acaa412-7428-399c-ac52-23f15a8e24d1 | -3.1501 | -53.2371 | 2024-11-13 00:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 47.2 |
| f39a6206-dd49-3f3d-9d44-e9a53393d8b8 | -5.3587 | -43.529 | 2024-11-13 00:30:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 141e9d92-e88b-3b61-9f86-b97b033fda6a | -7.1434 | -40.1602 | 2024-11-13 00:30:00 | GOES-16 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 70.4 |
| e2430126-caec-3fad-bf75-d62b70664ceb | -2.2296 | -53.7429 | 2024-11-13 00:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 164.4 |
| d92f1ad0-107c-332a-8dd5-fd301b2b340b | -2.7189 | -45.2883 | 2024-11-13 00:30:00 | GOES-16 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 37.7 |
| b11743bb-3c3e-3394-9944-5954dff63f10 | -4.3638 | -44.1006 | 2024-11-13 00:30:00 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 65.3 |
| d0b64962-cd31-3d1d-9e30-cf8f763dc3ae | -3.5558 | -53.0224 | 2024-11-13 00:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| fb4eb642-08ad-37e9-9c4c-4d8b6359d722 | -2.2295 | -53.7631 | 2024-11-13 00:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 92.5 |
| bdae62c5-15e3-33bd-908f-dc8847e5ea53 | 1.048 | -60.5986 | 2024-11-13 00:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 110.6 |
| e4ab720f-1919-3493-8aba-e37b3368b035 | -3.4913 | -50.8421 | 2024-11-13 00:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 88bdf6b5-8ede-300f-b380-97f855e6549e | -3.5743 | -53.0218 | 2024-11-13 00:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 104.0 |
| c1dae815-44d1-3cb0-949c-0a71ca37d39a | -2.2663 | -53.7422 | 2024-11-13 00:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 3e449bda-ae29-32eb-90ac-2eff6cdd9737 | -3.9483 | -48.1724 | 2024-11-13 00:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 6742121f-3627-35a7-a236-5b27e4d96da2 | -2.9924 | -51.045 | 2024-11-13 00:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 502f1b12-343b-3823-ab05-1abfcc410752 | -3.5743 | -53.0015 | 2024-11-13 00:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 136.1 |


[Clique aqui para ver as próximas entradas](README5.md)

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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b20941e8-3598-3532-9a9c-81f0b8e56860 | -9.85435 | -65.23553 | 2025-07-27 05:50:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7eb3d87f-4668-30c1-876d-c51e2563ab76 | -10.28233 | -64.4572 | 2025-07-27 05:50:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cdd04d01-e3f9-3113-a295-d67afe229afb | -10.04757 | -64.98167 | 2025-07-27 05:50:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d8c3ce68-da91-3378-9526-5c58fd19516f | -10.03325 | -66.9214 | 2025-07-27 05:50:00 | NOAA-20 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 0.3 |
| ded1f164-04b8-311b-8044-cfad62a360c7 | -11.30018 | -55.12534 | 2025-07-27 05:50:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 153855f5-877e-384c-b5bb-61ccd6e5cdf7 | -10.04696 | -64.98572 | 2025-07-27 05:50:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7e005132-d855-3af8-b533-e06383289a48 | -13.45463 | -60.97895 | 2025-07-27 05:50:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b2530160-f49a-32a2-91de-869d926178f6 | -11.93725 | -63.84692 | 2025-07-27 05:50:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7a791bf9-f237-35f2-8926-2a0c8cd4f81a | -9.3457 | -68.37848 | 2025-07-27 05:50:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 909bde9e-6e5b-3b6f-a338-74749ca9461c | -10.02189 | -67.69296 | 2025-07-27 05:50:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9cd87c0b-b2b6-338b-80c1-6f20ca7e45ec | -11.30087 | -55.11924 | 2025-07-27 05:50:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| eb31c03a-5292-32d3-aab2-573d58f41a14 | -6.6575 | -58.8468 | 2025-07-27 06:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 53.9 |
| a4da842b-f050-3744-b0dc-e4f77480fcc5 | -12.0391 | -45.8316 | 2025-07-27 06:00:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 82.8 |
| c7973ca5-7ced-3b17-9f56-2e36d370e649 | -6.639 | -58.8475 | 2025-07-27 06:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 43.2 |
| 17f4592c-a9a2-3f65-aee3-7ab5c2931d5a | -12.0391 | -45.8316 | 2025-07-27 06:10:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 43.6 |
| 366e2a2f-c576-345a-b22c-ddda63b3d065 | -6.639 | -58.8475 | 2025-07-27 06:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 2f46df8e-5b94-399e-9af1-79b2fc017986 | -6.6575 | -58.8468 | 2025-07-27 06:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 63.3 |
| ef2179ad-5ee7-31cb-beed-c0247f4a2d91 | -6.6389 | -58.8669 | 2025-07-27 06:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.4 |
| af2dc366-76c4-3a0f-9167-832b223ab21f | -6.1549 | -42.6001 | 2025-07-27 06:40:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 50.0 |
| 15aca028-1a48-33fd-8577-145688d00260 | -17.9828 | -53.1615 | 2025-07-27 06:40:00 | GOES-19 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 3f944ba3-fa9c-3ec6-b4b1-b83d08032c1b | -6.1547 | -42.6237 | 2025-07-27 06:40:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 49.2 |
| a55d8e39-a10a-3150-9f93-8c077d1703f4 | -6.639 | -58.8475 | 2025-07-27 06:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 75.6 |
| d293ec65-ef10-3d62-adc1-8b165188209f | -6.6575 | -58.8468 | 2025-07-27 06:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 9d7818c6-23d3-35ad-87e1-e2555579887b | -6.6575 | -58.8468 | 2025-07-27 06:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 57.2 |
| c462c84a-7d93-3011-bbea-093cbe4a2ed7 | -6.639 | -58.8475 | 2025-07-27 06:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 60.7 |
| c998de5d-7e83-3f03-bc32-d7db3f16d99a | -6.1547 | -42.6237 | 2025-07-27 06:50:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 53.1 |
| 12bcfde2-0868-3fc4-80a6-87b178bfb95f | -17.9828 | -53.1615 | 2025-07-27 06:50:00 | GOES-19 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 52.9 |
| d8456140-7213-309f-afd6-ee864d445440 | -6.1549 | -42.6001 | 2025-07-27 06:50:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 67.1 |
| f6029ed8-2ca4-3779-b80e-d29abcfee83f | -7.5649 | -61.39765 | 2025-07-27 06:52:00 | AQUA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 8.8 |
| b95faf58-00dc-390b-b553-38990e0470ab | -7.60094 | -61.21667 | 2025-07-27 06:52:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 23.3 |
| fced61c5-de58-3b78-b4f0-f0b96a8def60 | -6.63671 | -58.85474 | 2025-07-27 06:52:00 | AQUA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 35.1 |
| 9365459f-7d35-3b56-88b6-c63474b2b294 | -7.55464 | -61.40541 | 2025-07-27 06:52:00 | AQUA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 64f02fff-e8a4-3907-acab-bb4de70d20bf | -6.62666 | -58.85336 | 2025-07-27 06:52:00 | AQUA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 42.1 |
| 6b4e3636-5a3f-3961-8203-6e8524cd4ea4 | -6.64846 | -58.84448 | 2025-07-27 06:52:00 | AQUA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 23.6 |
| 55f0b933-68f8-39f5-a2fc-d4f31591ffd9 | -6.63839 | -58.84315 | 2025-07-27 06:52:00 | AQUA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 9a2f77f8-f745-3b22-8193-48519d25b1c9 | -7.60231 | -61.2075 | 2025-07-27 06:52:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 80ea83ea-ab41-31bc-9d7b-dd68dd026755 | -10.03657 | -59.10453 | 2025-07-27 06:54:00 | AQUA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 2a868eab-9416-324b-98c8-73948249cd44 | -10.04324 | -64.98597 | 2025-07-27 06:54:00 | AQUA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 21e187df-1c58-3899-b7c3-ea920b30cac8 | -9.02694 | -59.75856 | 2025-07-27 06:54:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 12cc0c0f-7464-3e2a-87d3-ed08afe7258b | -6.1547 | -42.6237 | 2025-07-27 07:00:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 62.4 |
| 2b0aca36-dce1-3e2a-b73d-4074e449922d | -6.639 | -58.8475 | 2025-07-27 07:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 77.1 |
| f2088695-3f58-3365-aeef-0b1051c8b190 | -6.6575 | -58.8468 | 2025-07-27 07:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 8c851683-3723-3c6d-af18-0fee77a93913 | -6.1549 | -42.6001 | 2025-07-27 07:00:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 93.9 |
| 60d20a7b-1dcf-3e30-a1b7-1989a8a34782 | -6.1547 | -42.6237 | 2025-07-27 07:10:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 71.7 |
| 35a79c51-8f46-31be-9a6a-6022a0b7a5f9 | -6.1549 | -42.6001 | 2025-07-27 07:10:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 116.7 |
| 7d2dd74d-7d54-3ccb-bf96-8e06de50595f | -6.1549 | -42.6001 | 2025-07-27 07:20:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 101.1 |
| 40f5d1a4-7535-3367-8b71-419f63518f00 | -6.1547 | -42.6237 | 2025-07-27 07:20:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 61.0 |
| fab2b03c-803f-3c10-a172-92e69adb2b5a | -6.1547 | -42.6237 | 2025-07-27 07:30:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 54.8 |
| 33deed14-0eaf-3be5-911d-43a50afa49f9 | -6.1549 | -42.6001 | 2025-07-27 07:30:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 90.3 |
| 686e5b12-d3d6-30bb-a2fd-5a27dda9a9c3 | -6.1547 | -42.6237 | 2025-07-27 07:40:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 43.8 |
| 420be53f-0b64-3d53-9fa4-7edfe32c0d09 | -6.1549 | -42.6001 | 2025-07-27 07:40:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 67.8 |
| b64293b0-3322-3308-a3a2-de6c988ee6b6 | -6.1549 | -42.6001 | 2025-07-27 07:50:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 72.0 |
| 16f3b2df-7bef-3310-a275-de680ed073e8 | -6.1547 | -42.6237 | 2025-07-27 07:50:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 52.8 |
| 5d79b89a-adcd-38db-bf19-9ac222b2275d | -6.1549 | -42.6001 | 2025-07-27 08:00:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 71.9 |
| 0c24523f-3a76-31ff-9888-8a7239b6d709 | -6.1547 | -42.6237 | 2025-07-27 08:00:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 45.4 |
| 0ecb5eb1-d37a-37b7-8244-a044de262c95 | -6.1549 | -42.6001 | 2025-07-27 08:10:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 68.4 |
| 06a4ac5e-b287-3760-9212-b4e17a47924e | -6.1547 | -42.6237 | 2025-07-27 08:10:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 41.2 |
| 3c0a1f7b-ff91-375a-bbf6-f2f2445c7cad | -12.6696 | -47.0318 | 2025-07-27 08:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 6210e0ea-98d7-3d84-b18d-beeac2809b94 | -6.1549 | -42.6001 | 2025-07-27 08:20:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 54.7 |
| 9103325d-54a6-3978-a7e1-0fb640d96f75 | -12.67 | -47.0092 | 2025-07-27 08:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 6cc5a58b-bcf3-3e65-b665-dba19a7bbfd9 | -12.6892 | -47.0064 | 2025-07-27 08:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 0fcd2050-0a48-3b53-83bb-f0f36cf491ee | -12.67 | -47.0092 | 2025-07-27 08:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 71446300-1a5a-33b7-a823-a1caa912c312 | -14.9714 | -46.9811 | 2025-07-27 08:40:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 244.4 |
| 34afa43e-1184-3be6-a5a3-ed2a52a3a5ae | -14.9719 | -46.9583 | 2025-07-27 08:40:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 184.0 |
| 4cfc6766-562e-3639-a03d-4c03f67c12c5 | -14.9714 | -46.9811 | 2025-07-27 08:50:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 5217e927-4011-3f63-809e-aa89336eb307 | -14.9719 | -46.9583 | 2025-07-27 08:50:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 357b42ca-e305-3c57-a542-227d0266a4aa | -4.9454 | -43.7425 | 2025-07-27 12:10:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 81.3 |
| fd129142-074f-37a6-8dda-27b1ae984bea | -4.9641 | -43.7413 | 2025-07-27 12:20:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 85.8 |
| cbd6ba98-177d-3803-a91d-738dbd29848e | -4.9643 | -43.7182 | 2025-07-27 12:30:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 32230c03-e4a2-342a-8012-05981eebf7cc | -4.9641 | -43.7413 | 2025-07-27 12:30:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 139.2 |
| 6f417644-e5cd-3842-a91d-e36b36b50652 | -12.0007 | -45.8372 | 2025-07-27 12:40:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 5b7b168f-6b96-32a1-8853-f6c44c948f04 | -4.9454 | -43.7425 | 2025-07-27 12:40:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 96bc7f41-1741-35d4-9c89-dfa22022082c | -4.9641 | -43.7413 | 2025-07-27 12:40:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 176.6 |
| 13881c2b-de3c-3abf-8391-6719d74cf403 | -4.9643 | -43.7182 | 2025-07-27 12:40:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 152.7 |
| 453add98-0d52-3bc5-8228-c57cd080604b | -4.948 | -43.74287 | 2025-07-27 12:49:00 | TERRA_M-T | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 285.0 |
| 1143ebea-0c2a-317a-af6a-240b5cf0cf48 | -4.96489 | -43.74504 | 2025-07-27 12:49:00 | TERRA_M-T | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 39.5 |
| d58d07a6-c299-302d-a4f0-b04099291992 | -5.25245 | -48.59354 | 2025-07-27 12:49:00 | TERRA_M-T | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 34144ef3-4cf9-30fa-91c2-00660a682198 | -3.41411 | -42.99868 | 2025-07-27 12:49:00 | TERRA_M-T | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 47.2 |
| 033b91e9-cd6a-346e-a894-420031c9c68a | -7.0943 | -51.57823 | 2025-07-27 12:49:00 | TERRA_M-T | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| b9b74c5c-ecdd-3031-95a5-f458938be43b | -5.95693 | -45.05937 | 2025-07-27 12:49:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 113.7 |
| 485839ef-fc6d-394d-a438-ee6725f0b93c | -4.95306 | -43.70459 | 2025-07-27 12:49:00 | TERRA_M-T | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 167.7 |
| 4450169c-6ec5-3147-95fe-e9a21b8d4381 | -4.95191 | -43.75011 | 2025-07-27 12:49:00 | TERRA_M-T | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 250.8 |
| f879eeb5-f2cb-32a3-aa7c-0daf1e56a758 | -6.8946 | -52.86549 | 2025-07-27 12:49:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 901826e7-36c1-31ae-b1c4-2a47dc4f366b | -7.05336 | -48.42683 | 2025-07-27 12:49:00 | TERRA_M-T | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Cerrado | 18.6 |
| e4e3ffc5-79d8-3345-96d9-26ac76ca80ff | -6.01254 | -44.06375 | 2025-07-27 12:49:00 | TERRA_M-T | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 0ff4d81f-1e90-3498-84df-12b632d03491 | -4.95672 | -43.71183 | 2025-07-27 12:49:00 | TERRA_M-T | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 290.2 |
| 2afead6b-73c8-35cf-ad56-bf0e3b66ab7e | -5.95257 | -45.06411 | 2025-07-27 12:49:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 113.2 |
| 59c13655-0e3d-3a17-b227-0993fc76a170 | -4.60545 | -43.31847 | 2025-07-27 12:49:00 | TERRA_M-T | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 57.6 |
| adfa3719-7666-388f-93f4-910dcec39abf | -6.01715 | -44.0713 | 2025-07-27 12:49:00 | TERRA_M-T | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 38.9 |
| 3c51df4a-658c-3d46-9a0c-0f4e4c8fa301 | -4.9454 | -43.7425 | 2025-07-27 12:50:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 128.1 |
| a792d9c5-4278-3a04-be1b-2e2eca51a5e9 | -4.9643 | -43.7182 | 2025-07-27 12:50:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 177.8 |
| 021b017a-0fb6-3a8f-b340-ec5bc1588a20 | -4.9641 | -43.7413 | 2025-07-27 12:50:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 196.2 |
| f9a176da-98e6-3008-82b1-d4b52acd57c3 | -7.75142 | -51.1261 | 2025-07-27 12:51:00 | TERRA_M-T | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| e77ca479-758e-3b37-8347-af5d696cae87 | -8.01745 | -48.1774 | 2025-07-27 12:51:00 | TERRA_M-T | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 52.2 |
| 089f713b-3bd7-30a5-a4cf-1d2a91a205f5 | -11.30476 | -55.12087 | 2025-07-27 12:51:00 | TERRA_M-T | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 0a87e782-aa5b-30c4-8bad-a35a1fce7aed | -13.51012 | -45.51509 | 2025-07-27 12:51:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 112.7 |
| 0762d8c6-d9c6-354d-a83b-ae6031865d2e | -12.66155 | -47.0041 | 2025-07-27 12:51:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 4a510685-c876-3ceb-b7e9-3796ab479519 | -10.04278 | -59.10074 | 2025-07-27 12:51:00 | TERRA_M-T | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 17.4 |
| 8b646fc2-3b86-3d15-90c7-75fa78a1174b | -8.29571 | -46.36086 | 2025-07-27 12:51:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 28.0 |
| 0618bb2b-172c-3867-bcb8-ee9db2a637ae | -7.75293 | -51.11487 | 2025-07-27 12:51:00 | TERRA_M-T | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |


[Clique aqui para ver as próximas entradas](README28.md)

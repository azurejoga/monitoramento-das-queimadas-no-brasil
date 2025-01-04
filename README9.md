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
| 1125a7be-ad2f-3efc-9a3f-4cec7582fc84 | -5.0079 | -56.17546 | 2025-01-04 05:25:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9e3f9afb-c36b-367d-99bf-5f9aea105c3f | -11.80624 | -49.32706 | 2025-01-04 05:25:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a51f0bbf-1e19-3f58-8dad-56fa1f9892cd | -2.95426 | -60.01382 | 2025-01-04 05:25:00 | NOAA-21 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 28b73615-6d5d-314c-9564-4139a6c3fed6 | 1.3401 | -60.2932 | 2025-01-04 05:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 48.2 |
| a70a109d-ff20-38ea-90ac-0f21cb4c2afa | 1.34 | -60.3122 | 2025-01-04 05:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 3eb140d5-2ec6-3ecb-b86b-e80ecb18b29c | -10.6128 | -44.3284 | 2025-01-04 05:30:00 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 84.8 |
| d3e69245-2339-3432-8bd5-f5b9865cee19 | 1.34 | -60.3122 | 2025-01-04 05:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 8f43ed22-5ac1-39f6-bc3f-885f049fe9eb | -10.6319 | -44.3257 | 2025-01-04 05:40:00 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 8cd50dee-a9dc-3405-a80c-6dbe84539cff | 1.3401 | -60.2932 | 2025-01-04 05:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 85f0497f-d8f5-3f11-884b-fd083380c2bf | -10.6124 | -44.3517 | 2025-01-04 05:40:00 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 1dc218ec-1b9d-3c03-9795-0f67789f4240 | -10.6128 | -44.3284 | 2025-01-04 05:40:00 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 101.7 |
| 033fbace-dbd5-3ee5-9d7c-557777363d6e | 1.53953 | -60.38188 | 2025-01-04 05:46:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 21df0304-f14b-38ff-8c93-a060497b3bd9 | 1.34531 | -60.30894 | 2025-01-04 05:46:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 86a9153e-e951-3ec3-952d-e16233117737 | 1.34124 | -60.30919 | 2025-01-04 05:46:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 7.2 |
| fd4f9324-80c5-3a2f-90eb-9e0e0327c667 | 1.3372 | -60.30983 | 2025-01-04 05:46:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 664c2887-feab-3791-be2d-9cade831ccda | 1.34069 | -60.30567 | 2025-01-04 05:46:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 7.6 |
| fb2e71a2-5efa-3f9e-a900-701b70d55dd6 | 1.34012 | -60.30255 | 2025-01-04 05:46:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 26be3fac-42d3-34e3-8b4d-62dcec6d3ee8 | 1.618 | -60.32738 | 2025-01-04 05:46:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3f0cbdf6-784f-3377-9d9d-2dc45295b7ef | 1.34416 | -60.30192 | 2025-01-04 05:46:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 7dc2d9ae-ffc1-344c-8935-69b3c3b1d661 | 1.34474 | -60.30543 | 2025-01-04 05:46:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 5287e95d-d2d1-30c6-a0e4-9157b645d7ad | 1.33665 | -60.30631 | 2025-01-04 05:46:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 1ee8ead3-b38f-3601-891d-a3bb168a59a1 | 1.61856 | -60.33086 | 2025-01-04 05:46:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 671185a0-3df0-307b-ab27-18390060847f | 1.54355 | -60.38125 | 2025-01-04 05:46:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d2e17fb3-8aa7-3991-8ebe-e38b96f8104a | 1.3407 | -60.30606 | 2025-01-04 05:46:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 92e2defa-b02f-3f8d-8a38-d2d4d05a07ad | 1.32248 | -60.70708 | 2025-01-04 05:46:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d513323e-3f66-38bf-bcc8-124d5d6475b1 | 0.58985 | -60.46682 | 2025-01-04 05:46:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7e9bad9c-2756-3011-82fe-2517c7af6855 | 1.3361 | -60.30278 | 2025-01-04 05:46:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 08042ac6-83fc-38b3-a9bc-167af912d9ca | 1.33665 | -60.3067 | 2025-01-04 05:46:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 06a55a35-6012-3dc0-8065-270efdf2e62d | 4.0013 | -60.10036 | 2025-01-04 05:46:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 628e1bb1-3a0a-3d7f-883b-48fdd33a67ae | 1.34014 | -60.30214 | 2025-01-04 05:46:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 7.6 |
| c58d0945-a27f-33a8-838b-1ebb78448e92 | 1.33723 | -60.31021 | 2025-01-04 05:46:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 6.2 |
| b9344a16-cce3-3d60-b07a-6f6812522d39 | 1.33608 | -60.30318 | 2025-01-04 05:46:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 8.1 |
| ca4d0f64-2c90-3a13-9335-48abad491b0a | 1.34127 | -60.30959 | 2025-01-04 05:46:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 6.2 |
| b9034b21-4e45-377a-938f-35f2b8af16dc | 0.5939 | -60.4662 | 2025-01-04 05:46:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 85143f6f-4cc7-3923-a180-7d97fe93d4a3 | -10.6128 | -44.3284 | 2025-01-04 05:50:00 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 108.5 |
| 11e69974-ca17-3e26-b223-4720cd446de3 | 1.3401 | -60.2932 | 2025-01-04 05:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 48.5 |
| d76b4270-514d-338e-b035-8500e3d474ce | 1.34 | -60.3122 | 2025-01-04 05:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 58.1 |
| da1013ba-e5fe-3c09-ba67-97d1f25eb785 | -10.6124 | -44.3517 | 2025-01-04 05:50:00 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 71.1 |
| f8ba9344-e943-39af-bfbf-fc742f3be340 | 1.34298 | -60.3103 | 2025-01-04 06:09:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 37856295-161d-3863-8e6e-1d4147fb29a4 | 1.33612 | -60.30661 | 2025-01-04 06:09:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 032c4eed-a92b-382b-84cb-0016802938d3 | 1.33536 | -60.30196 | 2025-01-04 06:09:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f6eef78e-aa70-36ad-b388-fc3b2e157c90 | 1.33688 | -60.31124 | 2025-01-04 06:09:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 6.6 |
| ea362061-85fa-3c69-9a17-5ab278c910ee | 1.34146 | -60.30102 | 2025-01-04 06:09:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 28de4a6e-a57f-3de1-a977-4aaf7eeac9a9 | 0.59516 | -60.46552 | 2025-01-04 06:09:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e55fbea1-c9be-3f15-a564-c682d7edab02 | 1.34908 | -60.30931 | 2025-01-04 06:09:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 96c377af-f652-3a64-84c5-d603a45a66fa | 1.34222 | -60.30565 | 2025-01-04 06:09:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 8bbec8f6-4ede-3a6b-b113-5a120cc3d21c | -10.6128 | -44.3284 | 2025-01-04 06:10:00 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 810bdbc6-c26c-3e96-a359-150b44aca3be | 1.34 | -60.3122 | 2025-01-04 06:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 45.4 |
| eeec77cf-c797-32ea-bfd4-5ea7f62bf15c | 1.34 | -60.3122 | 2025-01-04 06:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 5277cbc0-1a64-3851-972f-65568243a1b5 | 1.34 | -60.3122 | 2025-01-04 06:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 91702add-305f-35dc-9dbf-3df567aa133c | 1.34591 | -60.30425 | 2025-01-04 06:33:00 | AQUA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 34.0 |
| cad75ccf-aefa-3b61-8a30-ac46aedace91 | 1.34454 | -60.29513 | 2025-01-04 06:33:00 | AQUA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 43da2239-1281-351f-ba17-e99513b0d6fe | 1.33556 | -60.29643 | 2025-01-04 06:33:00 | AQUA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 14.6 |
| d5947846-259b-31a4-be80-ca3f047ed1f1 | 1.33694 | -60.30555 | 2025-01-04 06:33:00 | AQUA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 24.7 |
| 4b102eeb-5303-3b4e-a15f-6b3b8768531f | 1.34 | -60.3122 | 2025-01-04 06:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 47.0 |
| cce11836-8443-367d-ae83-7e8e5afb3d61 | 1.34 | -60.3122 | 2025-01-04 07:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 46.1 |
| ca9b37f6-d9af-3543-aa68-f04768739539 | -6.5631 | -51.1126 | 2025-01-04 07:00:00 | GOES-16 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 50.4 |
| f2609c37-a7ee-37ae-9a08-9a2a4e02644f | 1.34 | -60.3122 | 2025-01-04 07:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 46.4 |
| d2282c12-de44-32ea-8e15-a7bfd66eef56 | 1.3401 | -60.2932 | 2025-01-04 07:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 90cfb83d-2f0f-309a-abca-a156011f54e4 | 1.34 | -60.3122 | 2025-01-04 07:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 313c1a9f-6595-33c7-b87e-4893072f06e8 | 1.34 | -60.3122 | 2025-01-04 07:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 5c04fbfa-2bab-3464-a73f-210fcef3329f | 1.3401 | -60.2932 | 2025-01-04 07:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 45.2 |
| cd9304ca-04e9-3f40-87c4-fa9e2f71236b | 1.34 | -60.3122 | 2025-01-04 08:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 47.2 |
| bc20189d-50ce-3389-ad1a-aba89e2a57ca | 1.34 | -60.3122 | 2025-01-04 08:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 5d809bd4-7aa1-3d77-a2e7-c25ee20559c4 | 1.3401 | -60.2932 | 2025-01-04 08:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 50.1 |
| b348b9e6-e627-38ba-9449-88043fc31457 | 1.34 | -60.3122 | 2025-01-04 08:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 52.7 |
| a56083cf-a08a-364c-aab0-149ad2fe7bb5 | -6.67167 | -38.58847 | 2025-01-04 12:33:00 | TERRA_M-T | TRIUNFO | PARAÍBA | Brasil | 2516805 | 25 | 33 | nan | nan | nan | Caatinga | 26.5 |
| 8c3ba368-6ba6-3d06-b5b7-080c37b818ff | -3.47215 | -43.32299 | 2025-01-04 12:33:00 | TERRA_M-T | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| e8365297-e529-3f6a-a7fe-521621e9ed6a | -7.6308 | -37.7537 | 2025-01-04 12:33:00 | TERRA_M-T | TAVARES | PARAÍBA | Brasil | 2516607 | 25 | 33 | nan | nan | nan | Caatinga | 40.3 |
| 526d2625-82ed-3c24-a6f2-0b7cfee20bf0 | -6.12519 | -42.54397 | 2025-01-04 12:33:00 | TERRA_M-T | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 11.0 |
| c9336ba3-8441-3477-ad6a-68de06cb7df8 | -4.47247 | -42.51893 | 2025-01-04 12:33:00 | TERRA_M-T | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 7048bcf7-aa69-3860-bfc9-0890e22dbb53 | -7.66014 | -37.85824 | 2025-01-04 12:33:00 | TERRA_M-T | QUIXABA | PERNAMBUCO | Brasil | 2611533 | 26 | 33 | nan | nan | nan | Caatinga | 34.7 |
| 501981f8-763c-3cc1-82da-c8d455640f63 | -7.62788 | -37.75863 | 2025-01-04 12:33:00 | TERRA_M-T | JURU | PARAÍBA | Brasil | 2508000 | 25 | 33 | nan | nan | nan | Caatinga | 30.4 |
| 25a31d60-9a13-361b-b469-68424248a740 | -5.05485 | -44.45491 | 2025-01-04 12:33:00 | TERRA_M-T | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a3cf5708-d74d-38ec-bbea-ab3b04928090 | -3.03692 | -42.03641 | 2025-01-04 12:33:00 | TERRA_M-T | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| cc076c9c-af4c-3d0a-a9ea-42d55edc8568 | -7.63155 | -37.72855 | 2025-01-04 12:33:00 | TERRA_M-T | CARNAÍBA | PERNAMBUCO | Brasil | 2603900 | 26 | 33 | nan | nan | nan | Caatinga | 60.6 |
| 8286ead7-9c6b-308f-8fef-1a150876f40c | -2.41629 | -44.77927 | 2025-01-04 12:33:00 | TERRA_M-T | BEQUIMÃO | MARANHÃO | Brasil | 2101905 | 21 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 14f3dfcd-359a-3d5c-84b2-6f2809d05c83 | -3.18182 | -41.80732 | 2025-01-04 12:33:00 | TERRA_M-T | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 78929e48-a128-3968-afad-cbade56f19a9 | -7.65903 | -37.88154 | 2025-01-04 12:33:00 | TERRA_M-T | TAVARES | PARAÍBA | Brasil | 2516607 | 25 | 33 | nan | nan | nan | Caatinga | 37.7 |
| dade58d0-73a2-38e3-88bb-8ba5cb25f156 | -7.63474 | -37.72338 | 2025-01-04 12:33:00 | TERRA_M-T | CARNAÍBA | PERNAMBUCO | Brasil | 2603900 | 26 | 33 | nan | nan | nan | Caatinga | 43.9 |
| 73778dbe-1c42-3ce4-9734-27ec61ee7423 | -6.12686 | -42.53193 | 2025-01-04 12:33:00 | TERRA_M-T | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 12.9 |
| 1d648a22-b118-34c6-ae65-6c6d8e81ede7 | -2.41501 | -44.78811 | 2025-01-04 12:33:00 | TERRA_M-T | BEQUIMÃO | MARANHÃO | Brasil | 2101905 | 21 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 58dbbfda-eccf-34ce-b505-c4808f5470be | -3.97299 | -43.30968 | 2025-01-04 12:33:00 | TERRA_M-T | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 24.0 |
| 1175ae71-948c-3581-a1fb-31bf7d68c4bc | -6.3066 | -38.02138 | 2025-01-04 12:33:00 | TERRA_M-T | PILÕES | RIO GRANDE DO NORTE | Brasil | 2410009 | 24 | 33 | nan | nan | nan | Caatinga | 42.6 |
| a46def12-3b0a-3ed8-bc86-f2e5702ae968 | -6.30592 | -38.01584 | 2025-01-04 12:33:00 | TERRA_M-T | PILÕES | RIO GRANDE DO NORTE | Brasil | 2410009 | 24 | 33 | nan | nan | nan | Caatinga | 38.7 |
| 123479b9-42fa-3c17-9f51-3ab25b6e0d1e | -3.03529 | -42.04804 | 2025-01-04 12:33:00 | TERRA_M-T | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 958d24d0-db79-3f80-9b0c-5753e0449c5e | -1.70319 | -45.05753 | 2025-01-04 12:33:00 | TERRA_M-T | SERRANO DO MARANHÃO | MARANHÃO | Brasil | 2111789 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| cb0d545f-d7cb-3d5f-adfc-8a70e1b75c09 | -11.61131 | -40.12973 | 2025-01-04 12:36:00 | TERRA_M-T | VÁRZEA DA ROÇA | BAHIA | Brasil | 2933059 | 29 | 33 | nan | nan | nan | Caatinga | 22.0 |
| dec9bccb-d9cf-36b0-b83f-566fdf49f983 | -9.51011 | -44.74738 | 2025-01-04 12:36:00 | TERRA_M-T | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 12.1 |
| e6f42557-4a39-3f5b-b8d0-915dedb123c6 | -10.54177 | -44.6794 | 2025-01-04 12:36:00 | TERRA_M-T | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 8592c94b-43d2-3337-b082-144189a142b5 | -10.61154 | -44.34341 | 2025-01-04 12:36:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 26.7 |
| d39fb319-cc69-38f6-a7af-b79f11cb714c | -8.86137 | -48.83828 | 2025-01-04 12:36:00 | TERRA_M-T | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 649f2c20-ef1c-3b3c-87d3-31f3a5f0ddaf | -10.61296 | -44.33273 | 2025-01-04 12:36:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 23.3 |
| f416a078-6d46-31fc-97b1-19b9d760300a | -11.80908 | -48.07315 | 2025-01-04 12:38:00 | TERRA_M-T | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 0c5d6c94-77a2-38db-936e-2a950dcc5300 | -11.8064 | -48.09146 | 2025-01-04 12:38:00 | TERRA_M-T | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 9dfdf46c-3478-3a29-8f8d-2f0d9b6e17be | -11.80774 | -48.08229 | 2025-01-04 12:38:00 | TERRA_M-T | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 73.4 |
| da7f8606-2b36-3d69-8fc2-69a7711d6127 | -12.61748 | -46.6286 | 2025-01-04 12:38:00 | TERRA_M-T | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 55a390f0-62fa-32d9-bbd0-8c8d5c95aca6 | -12.47913 | -42.28951 | 2025-01-04 12:38:00 | TERRA_M-T | IBITIARA | BAHIA | Brasil | 2913002 | 29 | 33 | nan | nan | nan | Caatinga | 29.3 |
| fd3be8ab-226f-3174-858e-022c2ef09598 | -12.48115 | -42.2734 | 2025-01-04 12:38:00 | TERRA_M-T | IBITIARA | BAHIA | Brasil | 2913002 | 29 | 33 | nan | nan | nan | Caatinga | 16.1 |
| 12560804-c541-3283-a4f9-477f354b653f | -12.35856 | -38.45833 | 2025-01-04 12:38:00 | TERRA_M-T | CATU | BAHIA | Brasil | 2907509 | 29 | 33 | nan | nan | nan | Mata Atlântica | 37.7 |


[Clique aqui para ver as próximas entradas](README10.md)

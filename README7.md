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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1c20f24a-52ec-369d-804a-5950d7588bfb | -3.5592 | -48.1666 | 2026-09-08 01:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 150.3 |
| ae2341c5-5ac2-3742-8fe9-0cdecdc42360 | -9.4769 | -40.3365 | 2026-09-08 01:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 142.3 |
| e06dbe15-4d0d-371e-bff8-e3362ac7c74c | -9.7508 | -43.485 | 2026-09-08 01:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 114.6 |
| fd8d79ea-5a58-3244-a56c-6738d8c3d23b | -9.7134 | -43.4428 | 2026-09-08 01:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 113.0 |
| 38a74a68-e9fd-3fc1-875d-d64854bd085a | -9.4765 | -40.3613 | 2026-09-08 01:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 114.1 |
| 4658c042-c723-391c-a7a8-10efab8c1095 | -3.5591 | -48.1882 | 2026-09-08 01:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 203.9 |
| 49099fe9-d88d-343e-b8ef-94e480240363 | -8.5323 | -63.8416 | 2026-09-08 01:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 43.3 |
| 70b180a6-07cc-3eaa-8065-072a01fa01ad | -9.7317 | -43.4874 | 2026-09-08 01:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 97.1 |
| f28168f1-76d1-384a-aa26-b3cd182a0ef2 | -9.7131 | -43.4664 | 2026-09-08 01:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 101.0 |
| c89fc378-87cb-3c5c-a293-659fe5d6fc87 | -13.2289 | -61.7161 | 2026-09-08 01:40:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 656019e8-0eb1-397c-b2f7-7c097bf5e2f9 | -8.5138 | -63.8423 | 2026-09-08 01:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 44.2 |
| d6d25696-128e-3a71-89a8-5a0bff8783d2 | -3.5407 | -48.1673 | 2026-09-08 01:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 170.6 |
| 5344d612-4ed5-3289-96b0-e912199962c4 | -13.2479 | -61.7148 | 2026-09-08 01:40:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 36.7 |
| 9ac34ae0-9161-3d40-99af-9afe23033fb1 | -3.5406 | -48.1889 | 2026-09-08 01:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 225.6 |
| bf934411-1b4c-3cd6-8372-880c69030470 | -9.7314 | -43.511 | 2026-09-08 01:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 100.6 |
| f7a26f16-7205-322a-bdc4-966ee535609a | -9.7504 | -43.5085 | 2026-09-08 01:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 111.3 |
| 0e1e9d2f-645c-37cc-b4e7-0fd12d85f83a | -13.2289 | -61.7161 | 2026-09-08 01:50:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 46.3 |
| fd1cbda4-3256-3c26-96b6-39fa8c66d294 | -9.7504 | -43.5085 | 2026-09-08 01:50:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 114.7 |
| 37e71f28-948c-32b3-9658-5254bd48906f | -9.7131 | -43.4664 | 2026-09-08 01:50:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 112.7 |
| 8fb60b77-bd4f-38f7-be46-a93007953796 | -9.7134 | -43.4428 | 2026-09-08 01:50:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 111.8 |
| ded14b8e-7adf-331f-9769-40a2dcde471e | -5.2898 | -60.125 | 2026-09-08 01:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 42.0 |
| 847fcba4-556c-3bf7-b39d-74151da7f363 | -9.4769 | -40.3365 | 2026-09-08 01:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 90.3 |
| 12522554-05bf-3032-a761-fb032ab79151 | -3.5591 | -48.1882 | 2026-09-08 01:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 149.8 |
| a91dfabe-208c-3716-9738-25c60665b9d3 | -6.6357 | -59.4459 | 2026-09-08 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.2 |
| cba5ee46-0d82-3740-a0e6-ad45519d1ebc | -9.4765 | -40.3613 | 2026-09-08 01:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 84.7 |
| 4a530ad3-cb14-361b-9734-e071b50ab104 | -9.7508 | -43.485 | 2026-09-08 01:50:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 109.6 |
| 4697dfdc-b08d-3225-9e09-567013fadfa0 | -3.5407 | -48.1673 | 2026-09-08 01:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 187.3 |
| b13a011e-4153-337d-b51a-7102cdb56759 | -3.5406 | -48.1889 | 2026-09-08 01:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 260.4 |
| ae4b52b2-3dfc-3964-909e-03ff149068b6 | -9.7317 | -43.4874 | 2026-09-08 01:50:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 14316c03-0a81-3dd2-ae20-5497cdbaa4a3 | -9.7138 | -43.4192 | 2026-09-08 01:50:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 65.7 |
| 347ab99a-75d4-30cb-b87c-b79d45afdfe8 | -3.5592 | -48.1666 | 2026-09-08 01:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 115.1 |
| 164aab26-eda2-3021-99b9-be871a09be96 | -9.7504 | -43.5085 | 2026-09-08 02:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 1739a383-c951-3cb2-9f0e-33af5ba5bb50 | -3.5407 | -48.1673 | 2026-09-08 02:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 155.0 |
| b28992d5-f767-3b8c-a6f7-8a10433a79be | -9.7138 | -43.4192 | 2026-09-08 02:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 86.5 |
| 681a5c45-2310-3bd9-9c0b-7ad6accd7f47 | -5.2898 | -60.125 | 2026-09-08 02:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 42.9 |
| 65325bb9-9bff-3515-b249-994f8eb019f3 | -9.7317 | -43.4874 | 2026-09-08 02:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 106.6 |
| 1cc858cf-b7f2-3051-8ac7-5ed2652e1057 | -3.5591 | -48.1882 | 2026-09-08 02:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 226.9 |
| de549a29-af88-33a0-992b-ce1547972e00 | -9.7134 | -43.4428 | 2026-09-08 02:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 110.3 |
| 45f177a2-a2b8-3e06-abab-de2d807e7926 | -9.7508 | -43.485 | 2026-09-08 02:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 41c07577-c110-3d10-a338-6b11df5c2169 | -9.7314 | -43.511 | 2026-09-08 02:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 106.8 |
| c2d9cc24-9ced-3561-a350-209069448391 | -13.2289 | -61.7161 | 2026-09-08 02:00:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 58d11b20-ff16-3aaf-b5c8-81e4254d87ba | -3.5592 | -48.1666 | 2026-09-08 02:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 115.0 |
| 3b44e1d4-ec5e-35fc-a82b-89f5edc67ff0 | -3.5406 | -48.1889 | 2026-09-08 02:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 312.0 |
| b262f5e3-011d-34fe-b4e7-06a69314cf58 | -6.6357 | -59.4459 | 2026-09-08 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 4a2dbd48-36ba-36b7-9caa-ea4596025afa | -9.7131 | -43.4664 | 2026-09-08 02:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 96.6 |
| 922ab3ce-8786-32c3-89b8-a99469faae4b | -3.5407 | -48.1673 | 2026-09-08 02:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 160.8 |
| d4b89e6a-c794-3b27-898d-2ea59b912b83 | -3.5406 | -48.1889 | 2026-09-08 02:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 312.6 |
| b62a04a8-ed14-3182-a9d1-bb59b2ae4c25 | -3.5592 | -48.1666 | 2026-09-08 02:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 85.3 |
| 84367113-7560-36ac-aaa5-fb83b0862e6d | -9.7504 | -43.5085 | 2026-09-08 02:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 68f2c2ec-bdcd-36c6-b80d-da97336d0d89 | -3.5591 | -48.1882 | 2026-09-08 02:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 157.1 |
| 19e3e879-d074-31a0-ab38-85113a442516 | -9.7508 | -43.485 | 2026-09-08 02:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 91.9 |
| ac9747ed-e387-3a03-b853-f4ab15254f3b | -9.7138 | -43.4192 | 2026-09-08 02:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 101.3 |
| 4fbce6ce-76fe-3beb-b373-1afd9e21ee17 | -5.2898 | -60.125 | 2026-09-08 02:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 43.0 |
| 69aacabc-d305-329f-9f83-86d29c35c734 | -9.7134 | -43.4428 | 2026-09-08 02:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 116.0 |
| 380dd86f-102d-33cf-8444-aec9e56f7fe5 | -9.7321 | -43.4639 | 2026-09-08 02:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 96fabeba-d0cc-3c93-b446-e4d96d98fe4e | -9.7131 | -43.4664 | 2026-09-08 02:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 101.3 |
| 1a0f88f0-cd42-3d59-a2f9-be4189da021a | -3.53 | -48.2 | 2026-09-08 02:15:00 | MSG-03 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0c72a61b-2f34-3b6d-b465-650654f62517 | -3.53 | -48.15 | 2026-09-08 02:15:00 | MSG-03 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0558b68d-f13a-381f-bc74-f694ad40aa91 | -5.2898 | -60.125 | 2026-09-08 02:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 42.6 |
| 544736e5-39fd-3be3-a259-d746919c09d2 | -3.5592 | -48.1666 | 2026-09-08 02:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 121.7 |
| af109c9b-51ba-3cef-bdfd-1de2602df9ed | -9.7131 | -43.4664 | 2026-09-08 02:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 3e66382f-5e3b-3c15-abb1-3f649c3d661c | -3.5591 | -48.1882 | 2026-09-08 02:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 186.2 |
| 2daf30f4-30aa-396c-99e1-8f97c5ba3669 | -9.7504 | -43.5085 | 2026-09-08 02:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 7bcfc094-33e2-3631-8dc6-ca624ece0c16 | -9.7134 | -43.4428 | 2026-09-08 02:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 114.3 |
| 1ea2fa54-3137-36b3-9584-11e22be66eab | -3.5407 | -48.1673 | 2026-09-08 02:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 128.2 |
| ec806743-0456-3166-8f2f-5bd132333f99 | -3.5406 | -48.1889 | 2026-09-08 02:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 196.7 |
| b4a57230-1f47-3bbb-a55e-62d2867ad498 | -9.7138 | -43.4192 | 2026-09-08 02:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 108.5 |
| 5841c26b-621d-3542-b419-3bb2fe357314 | -3.5592 | -48.1666 | 2026-09-08 02:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 04cc9a85-b1d1-32e6-aaf8-257ab6a69cd6 | -9.7134 | -43.4428 | 2026-09-08 02:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 114.9 |
| 916fa1ac-9569-33d9-aae1-32abf3c43649 | -3.5591 | -48.1882 | 2026-09-08 02:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 98.0 |
| f78a85a8-87b7-3abf-a0d1-9fa2ef1bb4ba | -11.3525 | -45.7237 | 2026-09-08 02:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 51.2 |
| 1168e53d-18de-355a-96b9-f547c1b70a99 | -3.5407 | -48.1673 | 2026-09-08 02:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 186.2 |
| d2045119-0be5-31de-86c4-a16d1808387e | -9.7131 | -43.4664 | 2026-09-08 02:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 9a870c68-a53f-3679-9285-bf7cd2a718d2 | -3.5406 | -48.1889 | 2026-09-08 02:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 251.9 |
| dc56473d-b3ea-35fe-b018-d2d6430f96d3 | -6.6357 | -59.4459 | 2026-09-08 02:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 44.4 |
| ee556135-1033-31a2-92fa-0fb739e89755 | -9.7138 | -43.4192 | 2026-09-08 02:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 102.7 |
| 8b53bc20-624d-32af-a648-40d543e83fdb | -3.5406 | -48.1889 | 2026-09-08 02:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 193.9 |
| 54d7c6f7-86c9-32a7-a9de-d93515290b05 | -3.5592 | -48.1666 | 2026-09-08 02:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 108.2 |
| 9d372ce6-3104-3843-b725-a316086ece15 | -3.5407 | -48.1673 | 2026-09-08 02:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 118.9 |
| 6897c2ec-90fd-3350-89e1-81d026372d2f | -3.5591 | -48.1882 | 2026-09-08 02:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 174.8 |
| 6ad59031-aae5-30b6-b2d7-eca4d94a9a77 | -3.5406 | -48.1889 | 2026-09-08 02:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 179.8 |
| e277185d-be73-3304-ab60-668dba53e934 | -3.5407 | -48.1673 | 2026-09-08 02:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 111.3 |
| ea964d6f-370f-388e-aba8-ef9b51dd530e | -13.3009 | -45.2209 | 2026-09-08 02:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 241fc35d-81c9-3f1d-b2bc-8422e00cb738 | -3.5592 | -48.1666 | 2026-09-08 02:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 91.9 |
| 6dc05482-cccb-31c3-8a33-89269094d16d | -3.5591 | -48.1882 | 2026-09-08 02:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 143.1 |
| 69be433a-bbdb-3120-84df-4b8bd44ae96f | -13.3203 | -45.2177 | 2026-09-08 03:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 1e68162b-c80a-3ff0-9b5c-924426e0d041 | -3.5591 | -48.1882 | 2026-09-08 03:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 101.6 |
| ece44771-3b49-35e2-902a-fd04db6e4122 | -3.5592 | -48.1666 | 2026-09-08 03:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 58ec84bd-4801-3f3c-93f4-0097b79292cd | -3.5407 | -48.1673 | 2026-09-08 03:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 139.0 |
| 61826b37-c593-3380-9828-810a47f3fcdf | -13.3004 | -45.2442 | 2026-09-08 03:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 75.5 |
| a7b092ff-5ea6-38c9-9f06-71872d63f906 | -13.3009 | -45.2209 | 2026-09-08 03:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 153.1 |
| cb6a9cc3-fbef-3d71-8d1c-b6d170d96595 | -3.5406 | -48.1889 | 2026-09-08 03:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 213.4 |
| a3370022-dd3e-3989-9ff6-399afedc5249 | -6.60951 | -35.08849 | 2026-09-08 03:04:00 | NPP-375D | MATARACA | PARAÍBA | Brasil | 2509305 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 18e6d1db-c063-345f-8f60-1a637db53283 | -6.6105 | -35.08308 | 2026-09-08 03:04:00 | NPP-375D | MATARACA | PARAÍBA | Brasil | 2509305 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 8c411c20-69e1-374e-a472-828c30e1a39a | -6.60691 | -35.08762 | 2026-09-08 03:04:00 | NPP-375D | MATARACA | PARAÍBA | Brasil | 2509305 | 25 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 35ce0c81-733b-3192-8dab-41041d0cf29a | -6.60793 | -35.08224 | 2026-09-08 03:04:00 | NPP-375D | MATARACA | PARAÍBA | Brasil | 2509305 | 25 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| cffee53e-01d3-306e-9be1-554f849dab9c | -9.7138 | -43.4192 | 2026-09-08 03:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 65.6 |
| a14e7799-f1ec-3536-93ce-a11734843f81 | -9.7134 | -43.4428 | 2026-09-08 03:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 220c06f3-b812-3f3c-8871-5e335a9e312a | -3.5591 | -48.1882 | 2026-09-08 03:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 144.3 |
| d40ba583-801c-35d3-a900-6703059235df | -3.5406 | -48.1889 | 2026-09-08 03:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 141.2 |


[Clique aqui para ver as próximas entradas](README8.md)

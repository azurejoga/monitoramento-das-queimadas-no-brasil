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
| 712953db-3e4a-3e5b-af28-0c533166bbe4 | -11.1382 | -53.9223 | 2025-06-17 00:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 96.4 |
| fea7d7ff-0d92-364b-9235-8fb778d7d56c | -11.1571 | -53.9206 | 2025-06-17 00:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 53.1 |
| ec0768e1-3556-3d8d-a8bd-a15414342679 | -11.1379 | -53.9429 | 2025-06-17 00:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 127.5 |
| 13e2e21b-537b-3232-aeca-d96df7ea3e2b | -10.3014 | -60.5421 | 2025-06-17 00:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 31.9 |
| 49e23045-b4e6-37f4-b07b-81b3446dd22d | -10.9355 | -56.8322 | 2025-06-17 00:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 80.7 |
| afb8c8a6-1a53-3054-af04-277712bd9b9f | -10.9353 | -56.8522 | 2025-06-17 00:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 47.3 |
| b1544fc1-9abb-3058-a62d-4134508b5c32 | -10.9167 | -56.8336 | 2025-06-17 00:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 60bd78bb-60a7-375e-a3ce-14fb65bac8cc | -11.1568 | -53.9411 | 2025-06-17 01:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 52.4 |
| d610ff00-0c1f-35cd-b6ac-66e983d0bb07 | -11.1379 | -53.9429 | 2025-06-17 01:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 114.9 |
| 16504380-fd52-3551-a28d-70973da74ccb | -11.1382 | -53.9223 | 2025-06-17 01:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 96.3 |
| f2adb900-b752-31b2-852f-9c6c6ac1f647 | -11.1571 | -53.9206 | 2025-06-17 01:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 0348d5b9-4253-3f02-bd90-c62b1f76708b | -10.2827 | -60.5432 | 2025-06-17 01:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 38.3 |
| 187b9402-a51c-3bdf-992c-bdf12234f5b1 | -10.3014 | -60.5421 | 2025-06-17 01:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 34.3 |
| 1a704f2b-3849-30fc-b17b-9d32ca7cc47c | -10.9355 | -56.8322 | 2025-06-17 01:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 29c26112-6b4c-314a-9918-c2241aa285e5 | -10.9167 | -56.8336 | 2025-06-17 01:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 4c6a8dcd-621b-382e-b215-185246e7dd82 | -11.1571 | -53.9206 | 2025-06-17 01:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 43.4 |
| 5c7b562d-3d24-38d7-8f34-9acb57092402 | -10.2827 | -60.5432 | 2025-06-17 01:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 164fcf06-bb24-3331-8371-a7aa10796f72 | -11.1568 | -53.9411 | 2025-06-17 01:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 65.6 |
| e67c6d6c-de2d-3463-8265-5161cceb3b82 | -11.1379 | -53.9429 | 2025-06-17 01:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 99.3 |
| 99c98968-2dd8-3691-b815-ec3a5b649009 | -10.3014 | -60.5421 | 2025-06-17 01:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 31.4 |
| 75cfe1f9-9e21-3010-af63-1e0bf52f7213 | -11.1382 | -53.9223 | 2025-06-17 01:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 6e8c2315-c4df-3098-9a57-2651a5582d73 | -10.9355 | -56.8322 | 2025-06-17 01:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 77ee41ce-d596-304a-b4c9-1ce3b2068ce6 | -11.1568 | -53.9411 | 2025-06-17 01:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 5790a035-2fc3-36a3-9912-4aeabacda170 | -11.1379 | -53.9429 | 2025-06-17 01:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 104.7 |
| eb389de8-b4ad-3660-989d-054279b5d7a3 | -19.2901 | -48.4521 | 2025-06-17 01:20:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 54.7 |
| 61130664-5f7f-329c-b229-3e3c8ed8311a | -10.2827 | -60.5432 | 2025-06-17 01:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 51.9 |
| d0317006-dc84-30b3-849b-10f01f97b4b1 | -11.1382 | -53.9223 | 2025-06-17 01:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 4f46f121-a854-3d86-8eaf-42068c882f99 | -10.9355 | -56.8322 | 2025-06-17 01:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 64.8 |
| d95d649d-8dc6-342f-8064-028a1e0236a5 | -10.9167 | -56.8336 | 2025-06-17 01:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 42.3 |
| 30ce5e53-3dc1-340f-9b2f-5c53a92b4790 | -10.2947 | -60.5387 | 2025-06-17 01:29:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 90b4eecc-d47c-3c97-9135-d434b41f1884 | -11.1205 | -53.929699 | 2025-06-17 01:29:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 08d92ac4-2c64-31c6-88eb-5c3c0fbbed78 | -11.13 | -53.926998 | 2025-06-17 01:29:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2dcb8b50-996a-37b9-9ab7-e7f942e9deee | -10.919 | -56.837601 | 2025-06-17 01:29:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 80710861-4618-3b69-bf54-0a6c1aa19d5c | -10.9139 | -56.817501 | 2025-06-17 01:29:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 062ce2e1-a7d6-366f-bf16-20f84daa9d36 | -11.1385 | -53.958199 | 2025-06-17 01:29:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7e36b1c8-b552-34c2-9dc2-7aa46f7060d7 | -10.2822 | -60.529499 | 2025-06-17 01:29:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6ea4c674-6803-317a-a907-337d7e1f8c28 | -11.1216 | -53.895599 | 2025-06-17 01:29:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3909ff25-0750-36c2-a7bf-1b484ff964a5 | -10.2919 | -60.527 | 2025-06-17 01:29:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 291e8925-fd7a-37d1-99a1-ba485b231a5a | -9.456 | -57.849499 | 2025-06-17 01:29:00 | METOP-B | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7068434a-c8c2-367b-b97d-64383575b9d8 | -10.9286 | -56.835098 | 2025-06-17 01:29:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4868fb72-ae71-3c67-a154-cfbda8f36dab | -11.1396 | -53.924301 | 2025-06-17 01:29:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3f579f1c-727b-3828-a286-f1c59670e3f2 | -10.285 | -60.5411 | 2025-06-17 01:29:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c4cd9f96-be23-316f-b879-abc1f3efbe5f | -10.9235 | -56.814999 | 2025-06-17 01:29:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1f087e10-e1a1-3a56-8275-eb4fa4a76a8d | -11.1379 | -53.9429 | 2025-06-17 01:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 0812ec87-baa9-3543-8ca2-cda47895b83e | -11.1382 | -53.9223 | 2025-06-17 01:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 64.9 |
| ed33fba8-090a-3526-a2d2-d3ea579d1959 | -10.9355 | -56.8322 | 2025-06-17 01:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 91d8dd2a-f5f8-3fbb-a006-4676e9f73c03 | -19.2901 | -48.4521 | 2025-06-17 01:30:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 0b689184-fc97-36ac-a6f4-21c555bde445 | -10.2827 | -60.5432 | 2025-06-17 01:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 92b7952d-7886-3b77-b3a2-8c6dce293985 | -8.0703 | -43.0981 | 2025-06-17 01:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 53.3 |
| 0db5f467-5fb3-3ca4-b0cf-808c2c94f2e9 | -10.9355 | -56.8322 | 2025-06-17 01:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 504cb8a9-6e8c-32b2-bcb6-fb81cb7c0c91 | -11.1382 | -53.9223 | 2025-06-17 01:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 14046e84-7371-3461-be42-541f78c8588c | -11.1379 | -53.9429 | 2025-06-17 01:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 90.4 |
| a34070d5-59ed-34ed-b5db-eb1511a23a61 | -19.2901 | -48.4521 | 2025-06-17 01:40:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 0d36342f-7d72-3c8a-a0d9-279b434bb3be | -19.3103 | -48.4478 | 2025-06-17 01:40:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 52.1 |
| 2bf4dc53-1e46-3995-9133-368e7faea24f | -11.1379 | -53.9429 | 2025-06-17 01:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 78e4d8c5-d147-365c-9cf3-75dddad6d8f2 | -10.9355 | -56.8322 | 2025-06-17 01:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 70.4 |
| ea5021b2-b257-3178-9020-b2deff2b8ecb | -19.3103 | -48.4478 | 2025-06-17 01:50:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 2f2970f1-e4e3-30bb-a021-1e81ee02cd2d | -19.3097 | -48.4708 | 2025-06-17 01:50:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 44.6 |
| b5e1f87d-3abb-39f4-a89b-d136674e83a3 | -19.2895 | -48.4751 | 2025-06-17 01:50:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 60.8 |
| a77816d8-141c-323c-8fae-79065c9b4312 | -19.2901 | -48.4521 | 2025-06-17 01:50:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 120.3 |
| c1b31e71-62a7-3a17-a24e-51aeeed98b20 | -11.1382 | -53.9223 | 2025-06-17 01:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 47.4 |
| c44be608-1c79-38ec-8260-e2479475aa86 | -11.1568 | -53.9411 | 2025-06-17 01:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 45ee285c-683f-359a-a312-08d4dbed61c0 | -10.28385 | -60.53219 | 2025-06-17 01:58:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 30.3 |
| db5aa4d5-8c35-351b-bb20-9cbd78d147af | -10.29757 | -60.52969 | 2025-06-17 01:58:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 23.2 |
| 6269febd-a9b6-37ea-a92f-c7309a10f0f6 | -10.28783 | -60.55613 | 2025-06-17 01:58:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 24.1 |
| bd4201aa-33da-37ba-822a-a7b222231131 | -7.2594 | -43.0881 | 2025-06-17 02:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 67.4 |
| 38aa2f0a-2a8c-3345-9975-d1a7560e3da0 | -11.1382 | -53.9223 | 2025-06-17 02:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 46.9 |
| c9fcf4fc-bc48-38a5-b66e-bf151a5447aa | -11.1379 | -53.9429 | 2025-06-17 02:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 0ece5a2d-5f19-300d-b53b-a06fe8cfb8a6 | -7.2405 | -43.0899 | 2025-06-17 02:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 128.9 |
| e677818f-11ab-337a-bada-e0d93f59bd95 | -10.9355 | -56.8322 | 2025-06-17 02:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 0f33601f-bf03-379f-9004-459822eb10c1 | -19.2901 | -48.4521 | 2025-06-17 02:00:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 53.3 |
| 8ae86c04-363f-368e-9c89-cc7837bc7bab | -11.1379 | -53.9429 | 2025-06-17 02:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 0d21ec04-4f4d-3b32-baf0-89695d0cd379 | -10.9355 | -56.8322 | 2025-06-17 02:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 78cc98ef-0508-3025-8691-3771cda10990 | -19.3103 | -48.4478 | 2025-06-17 02:10:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 63.7 |
| a0c31448-10fc-30bf-8dab-118e6774eb08 | -19.2901 | -48.4521 | 2025-06-17 02:10:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 99.1 |
| a9fa4bd2-dd0b-3b06-9301-05baf5248c04 | -11.1382 | -53.9223 | 2025-06-17 02:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 46.2 |
| c600aacf-fe10-3b93-903a-9337416a9605 | -8.07 | -43.1216 | 2025-06-17 02:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 55.5 |
| 2de14921-f77f-3ba5-9b61-383cfd230110 | -8.0703 | -43.0981 | 2025-06-17 02:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 56.4 |
| 098e1af6-9ba5-37b4-898b-71c596228350 | -7.2405 | -43.0899 | 2025-06-17 02:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 64.2 |
| 87a7a31c-1d3d-3a28-8933-dd7163782ba4 | -7.2405 | -43.0899 | 2025-06-17 02:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 101.5 |
| 3168e397-4829-38ec-a626-c84f9ad496a8 | -19.3103 | -48.4478 | 2025-06-17 02:20:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 41.6 |
| 264c2e11-950e-3f7f-9c93-e7b7d2c0cd0f | -11.1379 | -53.9429 | 2025-06-17 02:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 02bfbb16-06c6-3d07-9ae5-5099912bfbe2 | -8.07 | -43.1216 | 2025-06-17 02:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 56.9 |
| 8b947004-5de0-3fe2-89dc-89ccff63b7bc | -19.2901 | -48.4521 | 2025-06-17 02:20:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 87.9 |
| f6b12a24-de2e-3bfd-9d77-e653715bc9ba | -10.9355 | -56.8322 | 2025-06-17 02:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 58.1 |
| d5844c99-5365-334a-8972-45c0f7ff7a29 | -8.0703 | -43.0981 | 2025-06-17 02:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 67.1 |
| 0a34c879-e1e2-322f-8525-280fcc2da9c5 | -11.1382 | -53.9223 | 2025-06-17 02:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 5ee6502e-7870-3358-8f71-eb3ec1d4bfae | -8.07 | -43.1216 | 2025-06-17 02:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 73.4 |
| ce4e7f9c-3979-357f-8d2a-d9ce2abfb4e4 | -10.9355 | -56.8322 | 2025-06-17 02:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 52.1 |
| e537cc06-241d-320f-afb3-6b2c3885508a | -11.1379 | -53.9429 | 2025-06-17 02:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 68.7 |
| c6e98cba-0422-3f8d-9704-48eeb5808049 | -8.0703 | -43.0981 | 2025-06-17 02:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 65.0 |
| 5f9bf111-9652-31e8-8230-6c2eb1cc9d0c | -10.9355 | -56.8322 | 2025-06-17 02:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 42d21c43-5041-3bf4-a0ae-2ec21d0a9258 | -11.1379 | -53.9429 | 2025-06-17 02:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 9aed3472-65c8-3c67-ab78-56625edd4236 | -11.1379 | -53.9429 | 2025-06-17 02:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 45.5 |
| e6317000-a77e-3a1d-b1df-4dea25e7dbeb | -17.64821 | -39.18507 | 2025-06-17 02:56:00 | NPP-375D | ALCOBAÇA | BAHIA | Brasil | 2900801 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 4ba1bd95-4fd2-3613-a06d-c14264c0b0d5 | -17.64138 | -39.18325 | 2025-06-17 02:56:00 | NPP-375D | ALCOBAÇA | BAHIA | Brasil | 2900801 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 4f16179a-aa62-36a3-a8d6-fa05effad2c2 | -11.1379 | -53.9429 | 2025-06-17 03:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 4ddcb377-4722-3fcf-a007-51d1020c3379 | -7.2405 | -43.0899 | 2025-06-17 03:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 66.1 |
| da13d9fe-0a79-334d-a2a0-258b7a2149a3 | -10.9355 | -56.8322 | 2025-06-17 03:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 49.8 |
| db556223-8ad3-3f9c-bbe6-4d11e6ec805e | -4.88816 | -37.52648 | 2025-06-17 03:13:00 | NOAA-20 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |


[Clique aqui para ver as próximas entradas](README5.md)

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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f5391adc-c654-35ba-b88e-aa02819607ce | -4.1942 | -50.649 | 2025-11-10 01:20:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 76.1 |
| d80fc6e7-f790-32b4-a13b-f33c29b194b9 | -3.6975 | -50.1857 | 2025-11-10 01:30:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| fd363b60-c0d4-36df-a78e-99c7b2dd74e0 | -4.727 | -42.9652 | 2025-11-10 01:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 162.5 |
| 7a7d16f8-e374-3494-961c-62459c926e3f | -4.7268 | -42.9886 | 2025-11-10 01:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 61.1 |
| e168c92a-8f4c-3e2f-bf5e-d04f5fcf3153 | -8.0142 | -41.6024 | 2025-11-10 01:30:00 | GOES-19 | CONCEIÇÃO DO CANINDÉ | PIAUÍ | Brasil | 2202802 | 22 | 33 | nan | nan | nan | Caatinga | 65.9 |
| 8d62f3f7-e3f7-3c65-b6ff-1385c5812ebb | -4.7083 | -42.9664 | 2025-11-10 01:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 391964b6-6851-36be-b31c-761cb2505fc7 | -4.2129 | -50.6064 | 2025-11-10 01:30:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 7f913ae6-95fe-359d-ba8a-428a858db16e | -4.7081 | -42.9898 | 2025-11-10 01:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 34.7 |
| d9a602c6-86e7-363e-a449-c8714ce2a4dc | -4.2128 | -50.6273 | 2025-11-10 01:30:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 269.2 |
| a0037cd2-b092-342b-b996-046a6c188604 | -4.1943 | -50.6281 | 2025-11-10 01:30:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 124.9 |
| d4e955a0-ec7f-339d-9c20-7f937205bcdc | -4.2127 | -50.6483 | 2025-11-10 01:30:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 92.3 |
| e7abac48-a7f7-365b-8d1d-dfbd25956ac6 | -4.1943 | -50.6281 | 2025-11-10 01:40:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 144.4 |
| a86ced88-0e56-3735-ad30-ea4eb4573007 | -4.2128 | -50.6273 | 2025-11-10 01:40:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 248.6 |
| acb64054-b0b6-3dbb-931c-2b349efad47f | -8.0142 | -41.6024 | 2025-11-10 01:40:00 | GOES-19 | CONCEIÇÃO DO CANINDÉ | PIAUÍ | Brasil | 2202802 | 22 | 33 | nan | nan | nan | Caatinga | 72.3 |
| 74bd5651-800f-367b-9508-6dca7389d86d | -4.1942 | -50.649 | 2025-11-10 01:40:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 76.6 |
| def8890e-05cb-3085-825c-859d1d9972d5 | -3.6975 | -50.1857 | 2025-11-10 01:40:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 4944b306-3881-3f40-aefe-71ee3e08722a | -4.2127 | -50.6483 | 2025-11-10 01:40:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 122.4 |
| 777828ba-47bc-3831-97a1-526ae1500860 | -4.2127 | -50.6483 | 2025-11-10 01:50:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 8608227e-8840-3d45-b188-d8bddbbb8166 | -4.1943 | -50.6281 | 2025-11-10 01:50:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 110.5 |
| d21753cb-a4a0-3a8c-bed0-8a969e3891dd | -4.2128 | -50.6273 | 2025-11-10 01:50:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 154.3 |
| b5984e6b-172b-35d0-9d25-6c722cf71ef2 | -3.6975 | -50.1857 | 2025-11-10 01:50:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| e8f4f9ca-9ee7-347a-a8bd-10cb54da9f63 | -8.0142 | -41.6024 | 2025-11-10 01:50:00 | GOES-19 | CONCEIÇÃO DO CANINDÉ | PIAUÍ | Brasil | 2202802 | 22 | 33 | nan | nan | nan | Caatinga | 74.4 |
| e02ec70c-0836-3f41-a3d8-7a6d735aa116 | -4.1943 | -50.6281 | 2025-11-10 02:00:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 129.3 |
| b7516ef6-f8f1-38b8-8a7d-018972940257 | -4.2127 | -50.6483 | 2025-11-10 02:00:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 79950ac1-b94c-3485-82a0-64ff89be36e9 | -4.2128 | -50.6273 | 2025-11-10 02:00:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 167.2 |
| e2aa080e-0134-3847-af88-48d62e2a01ae | -4.1942 | -50.649 | 2025-11-10 02:00:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| d7a49e7a-63a5-33e1-8fa7-3d8d047360a0 | -19.632401 | -58.0695 | 2025-11-10 02:00:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| e18b7714-bc23-3530-8d5b-9d762613c519 | -14.707 | -46.5935 | 2025-11-10 02:10:00 | GOES-19 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 80.7 |
| edf9a1b6-9850-32c0-929f-786626da7639 | -4.2128 | -50.6273 | 2025-11-10 02:10:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 125.1 |
| 81ccb23c-32dd-3260-b72f-bc975685fc09 | -4.1943 | -50.6281 | 2025-11-10 02:10:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 25a53423-ca09-3102-bcf7-7aef69790992 | -4.2127 | -50.6483 | 2025-11-10 02:10:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 6fea80e4-c6db-392b-878a-03ac56b1cc81 | -4.1942 | -50.649 | 2025-11-10 02:20:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| a8cc3bbe-06c2-36a8-be25-de1c35a30651 | -14.688 | -46.5739 | 2025-11-10 02:20:00 | GOES-19 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 9ce44f44-fad2-3e8d-9ce0-d518c17c34b1 | -14.707 | -46.5935 | 2025-11-10 02:20:00 | GOES-19 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 108.9 |
| 6ffa7881-0436-3038-adbc-71b712adfa3b | -4.2127 | -50.6483 | 2025-11-10 02:20:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 03dbd944-8695-374d-8834-baffc8dc0b53 | -4.1943 | -50.6281 | 2025-11-10 02:20:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 117.1 |
| b6b513ba-af99-3e3a-ba7d-a86f4efe866f | -4.2128 | -50.6273 | 2025-11-10 02:20:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 108.2 |
| c2c8ca7e-c63a-3eaa-a8b6-898232044ca9 | -14.7075 | -46.5705 | 2025-11-10 02:20:00 | GOES-19 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 79.8 |
| c2ea1877-cc20-39e0-bdb0-86438d5f4e95 | -14.707 | -46.5935 | 2025-11-10 02:30:00 | GOES-19 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 115.5 |
| 32d12785-4ed6-35a7-a306-3e90eaa99a01 | -4.1943 | -50.6281 | 2025-11-10 02:30:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 85.1 |
| 1b5a2afa-d5c1-3dac-8004-d09ec93fe9e4 | -14.7075 | -46.5705 | 2025-11-10 02:30:00 | GOES-19 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 82.8 |
| d9f5c0a4-fce5-3e1b-8156-542973a6e12c | -4.2128 | -50.6273 | 2025-11-10 02:30:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 108.8 |
| fbcda7e8-886c-38d2-aacd-24874a0042bd | -4.2127 | -50.6483 | 2025-11-10 02:30:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 9ae31414-c104-3f50-812c-be82bbdf312e | -14.688 | -46.5739 | 2025-11-10 02:40:00 | GOES-19 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 015811cc-3cdc-3fbe-a7d2-477e91051e56 | -14.6875 | -46.5969 | 2025-11-10 02:40:00 | GOES-19 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 77.8 |
| ab9bd34a-405d-353a-aab3-55d1beea1c2d | -14.707 | -46.5935 | 2025-11-10 02:40:00 | GOES-19 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 103.5 |
| 8b43dcd8-2356-320b-b532-5c0e7868c98b | -4.2128 | -50.6273 | 2025-11-10 02:40:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 94.5 |
| d0ef2b37-9b4f-32b7-8099-0c75068cbc08 | -4.1943 | -50.6281 | 2025-11-10 02:40:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 107.2 |
| c97d718f-1426-3ba7-93ed-bef64e6b53c1 | -4.1942 | -50.649 | 2025-11-10 02:40:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 4e7aefca-8768-32b4-b6c3-cb2332a4ce3a | -2.9341 | -57.7786 | 2025-11-10 02:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 3c35ddec-f773-35ed-82ce-757268ab3c87 | -4.2127 | -50.6483 | 2025-11-10 02:40:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| e0d9b0df-b188-3884-bef1-e29d19aa3674 | -14.7075 | -46.5705 | 2025-11-10 02:40:00 | GOES-19 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 435025dd-e989-3ee6-9b25-d52a80f28929 | -14.688 | -46.5739 | 2025-11-10 02:50:00 | GOES-19 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 558ac51d-5062-3479-b5c3-a0449e60f5e7 | -4.2127 | -50.6483 | 2025-11-10 02:50:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 74b763f1-7811-365e-ad9e-6ec437bbc540 | -4.1943 | -50.6281 | 2025-11-10 02:50:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 8050d76b-766e-330f-8324-4e8093bd64bc | -14.6875 | -46.5969 | 2025-11-10 02:50:00 | GOES-19 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 8aa46dcf-f5fb-3557-a6de-9d71d709fc80 | -14.707 | -46.5935 | 2025-11-10 02:50:00 | GOES-19 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 138.3 |
| b2962244-d972-3471-b647-abff2f4c856d | -4.2128 | -50.6273 | 2025-11-10 02:50:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 129.5 |
| 41535340-9bb6-3be0-bd33-44e77b86e0c0 | -14.7075 | -46.5705 | 2025-11-10 02:50:00 | GOES-19 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 5f9e1fcf-c46b-31ed-b9c3-36a0b1e4a0a1 | -14.688 | -46.5739 | 2025-11-10 03:00:00 | GOES-19 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 53cc2fbb-0b46-3376-abba-c0a83d9ac0dd | -14.6875 | -46.5969 | 2025-11-10 03:00:00 | GOES-19 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 5bd586a5-3267-3bf5-84e3-2b137742616b | -14.707 | -46.5935 | 2025-11-10 03:00:00 | GOES-19 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 116.4 |
| 4ccef52d-66d9-3229-9f79-71267da042fd | -4.2127 | -50.6483 | 2025-11-10 03:00:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 4130717b-995a-38f8-b8a9-5499817111bc | -4.2128 | -50.6273 | 2025-11-10 03:00:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 106.0 |
| c1fb5447-95b7-3cac-a5f6-84aca7e06c3e | -4.1943 | -50.6281 | 2025-11-10 03:00:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |
| f4cbc175-f6c8-3994-b486-ba1542d92d8f | -4.2128 | -50.6273 | 2025-11-10 03:10:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 0bc7dcfb-363c-3e42-81db-f3fafb420478 | -4.1943 | -50.6281 | 2025-11-10 03:10:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 82.6 |
| ae7203da-b724-33fc-b60a-780b6fa50f72 | -4.1942 | -50.649 | 2025-11-10 03:10:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| adf9fad7-d62e-35c7-bfd5-a4b32e236c2d | -14.707 | -46.5935 | 2025-11-10 03:10:00 | GOES-19 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 7b5eb29c-87ec-3edd-b139-25763a1e12d8 | -4.1943 | -50.6281 | 2025-11-10 03:20:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 71.2 |
| a3b50df6-4ed2-334a-b408-11e275930703 | -4.2128 | -50.6273 | 2025-11-10 03:20:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 74.1 |
| f463b01a-5d28-3e7e-abdd-4b61e918237c | -14.707 | -46.5935 | 2025-11-10 03:20:00 | GOES-19 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 8ff61738-fb4c-3edd-95c4-fc56a54f1550 | -7.63995 | -35.15158 | 2025-11-10 03:27:00 | NOAA-21 | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| c64106a9-8353-35a6-a3b9-83e502de2c1c | -5.84156 | -38.35452 | 2025-11-10 03:27:00 | NOAA-21 | IRACEMA | CEARÁ | Brasil | 2306009 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 7349a2f1-394d-3328-b893-2d494c0097ac | -5.75973 | -40.79181 | 2025-11-10 03:27:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 3795efcd-a754-32ab-9392-db0a1963ffd9 | -5.76087 | -40.79126 | 2025-11-10 03:27:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a4f2ea20-e27f-38bf-9d1e-b5fde826438d | -5.92672 | -43.93011 | 2025-11-10 03:27:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f42a5330-475a-304f-925a-74cc6f5f7ba3 | -5.1277 | -44.72466 | 2025-11-10 03:27:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f34fafb5-0f96-33ee-860b-eb0446a12594 | -5.12664 | -44.73053 | 2025-11-10 03:27:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 5ef74321-6d18-3578-914f-6c83d4247be5 | -5.92579 | -43.93529 | 2025-11-10 03:27:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1dede218-3bd4-3fe7-b5a5-85729287172c | -7.64285 | -35.15624 | 2025-11-10 03:27:00 | NOAA-21 | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 3a5768f0-0ad4-3551-ace5-dcc6e6e6fc5a | -6.857 | -40.15745 | 2025-11-10 03:27:00 | NOAA-21 | CAMPOS SALES | CEARÁ | Brasil | 2302701 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 832ac2aa-cbfa-3437-942d-1843cdafaf7f | -4.07213 | -44.13484 | 2025-11-10 03:27:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f27a833f-16e5-3c6a-8dfa-47fc0b52ebe6 | -6.85798 | -40.15607 | 2025-11-10 03:27:00 | NOAA-21 | CAMPOS SALES | CEARÁ | Brasil | 2302701 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| e5dbbb26-4dca-3c79-ad28-c8c5c88517ed | -3.77283 | -43.97439 | 2025-11-10 03:27:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9d11926b-ec74-34b7-b22a-e994d0ab1f09 | -5.79626 | -35.38707 | 2025-11-10 03:27:00 | NOAA-21 | SÃO GONÇALO DO AMARANTE | RIO GRANDE DO NORTE | Brasil | 2412005 | 24 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 04c600f8-f800-31e3-8810-c701c020d415 | -6.85748 | -40.1589 | 2025-11-10 03:27:00 | NOAA-21 | CAMPOS SALES | CEARÁ | Brasil | 2302701 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 10c5347f-7983-3066-8fb2-45ad1bab94f9 | -3.76514 | -43.97908 | 2025-11-10 03:27:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| bc5c1fcc-033f-367c-91ee-9862d3e65560 | -6.11248 | -38.1657 | 2025-11-10 03:27:00 | NOAA-21 | PAU DOS FERROS | RIO GRANDE DO NORTE | Brasil | 2409407 | 24 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 2d65d5b6-c3a8-32cc-9729-dad206283193 | -2.92046 | -40.00426 | 2025-11-10 03:27:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 5.1 |
| f1b2b3d8-96d3-3634-9e11-2b171cf94440 | -6.57369 | -42.90984 | 2025-11-10 03:27:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| db8cc931-46d4-3b81-89ed-ff045a833e0d | -5.6335 | -43.92259 | 2025-11-10 03:27:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9d6d8336-0224-3299-84d2-f8bcb503718a | -5.76571 | -40.7948 | 2025-11-10 03:27:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 11cb04de-ae41-3fa8-91e8-371c38172757 | -5.7651 | -40.79229 | 2025-11-10 03:27:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b8d65b41-8c46-3318-bc05-c96d7bba2f68 | -6.86246 | -40.1597 | 2025-11-10 03:27:00 | NOAA-21 | CAMPOS SALES | CEARÁ | Brasil | 2302701 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0dd16402-36ac-3ca3-ad88-3da2b425415e | -7.34771 | -35.21254 | 2025-11-10 03:27:00 | NOAA-21 | JURIPIRANGA | PARAÍBA | Brasil | 2507903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 8b9cd563-6901-329c-b8a4-4aacb2f06041 | -3.34289 | -39.99504 | 2025-11-10 03:27:00 | NOAA-21 | MORRINHOS | CEARÁ | Brasil | 2308906 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2ab88858-a139-31d8-8378-36294ee97af1 | -5.83783 | -38.34932 | 2025-11-10 03:27:00 | NOAA-21 | IRACEMA | CEARÁ | Brasil | 2306009 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 770e28ff-2453-3659-871f-6b7fb9d8a0a7 | -4.01745 | -40.90043 | 2025-11-10 03:27:00 | NOAA-21 | SÃO BENEDITO | CEARÁ | Brasil | 2312304 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2b45f0af-8655-3665-ae34-c49d3c943984 | -2.91991 | -40.00751 | 2025-11-10 03:27:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 8.9 |


[Clique aqui para ver as próximas entradas](README4.md)

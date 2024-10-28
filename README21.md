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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| da25d557-ac39-35eb-83ce-8afbecbe286e | -2.8514 | -49.262 | 2024-10-28 02:25:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 0778e651-ecb6-3706-b6a3-a5d24b8e7a5a | -2.8556 | -53.3256 | 2024-10-28 02:25:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 74.4 |
| eaa1acac-5ba6-30c2-b34f-75cc5f7083c2 | -2.8699 | -49.2615 | 2024-10-28 02:25:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 9e20930c-879d-3fac-8748-382e579966f7 | -2.87 | -49.2402 | 2024-10-28 02:25:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 6071aaed-1953-3fce-a5b0-3796149d8d88 | -3.0317 | -50.4176 | 2024-10-28 02:25:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 102.7 |
| 318565a0-867e-3f41-90ad-7663afea80cf | -3.0317 | -50.3967 | 2024-10-28 02:25:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| b40c9237-34b5-3c73-b52e-7aefeda23c58 | -3.0538 | -49.4895 | 2024-10-28 02:25:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 95a95242-0828-31a4-9cb3-28826b17bd89 | -4.0681 | -50.024 | 2024-10-28 02:25:28 | GOES-16 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 25.4 |
| 02d11922-01eb-332d-aa98-3cf6929b1600 | -4.2797 | -45.5362 | 2024-10-28 02:25:29 | GOES-16 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 71.4 |
| f1584347-1796-36cd-98e9-b20eca7e7492 | -4.428 | -45.6406 | 2024-10-28 02:25:30 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 105.7 |
| d8fcc8a5-a217-3b69-bf1e-b3278f3ba6c6 | -4.7766 | -46.4022 | 2024-10-28 02:25:32 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 67.0 |
| f2d8925e-e786-39da-9fc9-0d8a17e82fcb | -6.0744 | -47.2263 | 2024-10-28 02:25:40 | GOES-16 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 104.5 |
| f200f017-deed-3ec7-b31c-0a99c9bbb118 | -6.0746 | -47.2043 | 2024-10-28 02:25:40 | GOES-16 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 101.7 |
| 83095119-86ea-36ec-9231-a629db6b4cb4 | -6.0931 | -47.225 | 2024-10-28 02:25:40 | GOES-16 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 85.1 |
| a7146652-c825-3810-8389-29767169595b | -6.0933 | -47.203 | 2024-10-28 02:25:40 | GOES-16 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 40b77596-1760-3c33-bc22-cbf6e6cf5462 | -1.1836 | -53.4956 | 2024-10-28 02:35:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| ed9d4685-8031-3c1a-a70d-7c6070c0c3b7 | -1.1836 | -53.5158 | 2024-10-28 02:35:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 41.4 |
| 36c0da09-70f7-38c1-b421-aabfdb0786f1 | -1.9763 | -52.0804 | 2024-10-28 02:35:16 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 32.7 |
| fd148d60-3f0a-3f19-9c2c-f383a8dbc35d | -2.0499 | -52.0791 | 2024-10-28 02:35:17 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 35.3 |
| 39a56773-6607-32e6-b5c8-9d34bee92d58 | -2.2846 | -53.762 | 2024-10-28 02:35:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 45.9 |
| c6bc4db0-2f26-36ca-a62b-fcc07748d8bf | -2.2846 | -53.7822 | 2024-10-28 02:35:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 141.9 |
| 97332a00-4bf6-3954-a2b0-1be7abe83c47 | -2.2845 | -53.8023 | 2024-10-28 02:35:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| bf69026d-7e00-3d18-8c45-2f68f3ee2eee | -2.2662 | -53.7825 | 2024-10-28 02:35:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 115.4 |
| 3099b9f6-c434-383d-8c9b-e0b5756bdf9c | -2.2662 | -53.8027 | 2024-10-28 02:35:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 151ce0af-c5ca-347b-ab99-1ef1d8ee3d77 | -2.4104 | -48.5479 | 2024-10-28 02:35:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 479cd952-782e-327a-b92d-ed3f06daf6ec | -2.8515 | -49.2408 | 2024-10-28 02:35:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 2055f61f-3c0a-3e01-a00f-88584d60f3cd | -2.833 | -49.2413 | 2024-10-28 02:35:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| ab49d025-a4f6-3f3f-8415-53890adbc111 | -2.7034 | -49.3088 | 2024-10-28 02:35:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 027134e5-3304-3280-b416-0e7c5afced3b | -2.87 | -49.2402 | 2024-10-28 02:35:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| e4229773-1123-3957-b965-75398c51e66e | -2.8699 | -49.2615 | 2024-10-28 02:35:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 880ad5dd-052a-3c39-b3a6-16ba356d30a2 | -2.8556 | -53.3256 | 2024-10-28 02:35:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 14e3c5df-0a5b-339b-a24d-21d03b309bca | -3.0538 | -49.4895 | 2024-10-28 02:35:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 81.3 |
| e63b1578-ef34-32f0-839d-a319aab27ba5 | -3.0317 | -50.3967 | 2024-10-28 02:35:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 5727af7c-a953-3276-8c90-0003ec87f268 | -3.0317 | -50.4176 | 2024-10-28 02:35:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 110.9 |
| c10ee33c-5fd2-38a8-bcf7-8fa6329c5cad | -3.0501 | -50.4171 | 2024-10-28 02:35:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| c3318aae-2def-3b64-8f72-c5a03d759767 | -3.4014 | -46.3131 | 2024-10-28 02:35:25 | GOES-16 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 1e7c347f-c20c-3dd6-b8f1-e654bdec2162 | -4.0681 | -50.024 | 2024-10-28 02:35:28 | GOES-16 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 33.9 |
| 5e6a1bd2-5d29-3dfd-895a-4203f8ce8152 | -3.9949 | -46.4867 | 2024-10-28 02:35:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 733ff73e-aae2-30b7-91fa-e38325053556 | -4.2797 | -45.5362 | 2024-10-28 02:35:29 | GOES-16 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 719f5134-fd31-35f1-b17f-cbe274e4f3be | -4.1201 | -47.3169 | 2024-10-28 02:35:29 | GOES-16 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 36b68f3e-1b40-3230-b4ed-45e890663759 | -4.4094 | -45.6416 | 2024-10-28 02:35:30 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 75bcd2cd-60f5-36c6-8473-06f1819ec17f | -4.428 | -45.6406 | 2024-10-28 02:35:30 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 57.8 |
| b1883136-4c12-34f6-b61d-47d6d5f099b8 | -1.1836 | -53.5158 | 2024-10-28 02:45:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 44.8 |
| f659900d-d32d-3cb8-a559-da596953d3ec | -1.1836 | -53.4956 | 2024-10-28 02:45:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 42.2 |
| 6297bc9a-931f-3d4a-adbd-69445a5687d7 | -2.0499 | -52.0791 | 2024-10-28 02:45:17 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 35.7 |
| 963bbda6-77db-3e10-97a1-d4d11cab55ff | -2.2662 | -53.8027 | 2024-10-28 02:45:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| ca9428f1-0705-314a-9861-4eb0c166a172 | -2.2846 | -53.7822 | 2024-10-28 02:45:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 111.6 |
| 76b916db-344b-3d61-879c-4d865f3b2448 | -2.2845 | -53.8023 | 2024-10-28 02:45:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 273da5b7-87a4-3759-b914-01c5399ad317 | -2.2662 | -53.7825 | 2024-10-28 02:45:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 93.4 |
| c637b85d-5b51-3c9a-abb7-b032ff62b2e4 | -2.4104 | -48.5479 | 2024-10-28 02:45:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 76.4 |
| a84fcf14-c8d2-3a82-aacd-5d480d98118c | -2.833 | -49.2413 | 2024-10-28 02:45:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| bed23cdd-bdcc-3e78-934f-b9fc1f14612c | -2.8515 | -49.2408 | 2024-10-28 02:45:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 01b97b02-a516-396d-96c8-d5fd01339768 | -2.8555 | -53.3459 | 2024-10-28 02:45:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 34.9 |
| 80955fbe-21fc-387f-8b9e-1fa99f01438c | -2.8556 | -53.3256 | 2024-10-28 02:45:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 37.4 |
| 3674c48c-7f17-3a65-844b-603c0d4e3178 | -2.8699 | -49.2615 | 2024-10-28 02:45:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 2892a39f-97c7-3eab-8b64-e4a36ccb1fea | -2.9761 | -50.4821 | 2024-10-28 02:45:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| e1769c6a-a32c-33a5-9664-41b392e90667 | -3.0317 | -50.4176 | 2024-10-28 02:45:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 115.6 |
| 0f5a41c9-5019-3b15-bfe3-e75a0dd7b90d | -3.0538 | -49.4895 | 2024-10-28 02:45:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 885211c7-38b5-3e86-a4b5-a3c6c1bf895e | -3.0501 | -50.4171 | 2024-10-28 02:45:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 8ae9f68f-33d2-3014-845b-4cc96f717a4e | -3.0317 | -50.3967 | 2024-10-28 02:45:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 9e260dfc-4235-3ca2-85bf-52f6bc204211 | -4.4094 | -45.6416 | 2024-10-28 02:45:30 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 3dc7235e-63f6-3fe4-a5d7-2c322c507f23 | -4.428 | -45.6406 | 2024-10-28 02:45:30 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 13b5debb-0a41-3042-b3d5-f713d0f3829c | -4.758 | -46.4033 | 2024-10-28 02:45:32 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 55.0 |
| a5631a5a-361b-3efd-a935-e568f3bd7409 | -4.7766 | -46.4022 | 2024-10-28 02:45:32 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 64.5 |
| e81edffc-5a19-37fe-9113-c925e6d88f10 | -1.1836 | -53.4956 | 2024-10-28 02:55:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 43.2 |
| 4427c0cd-c230-3bca-bb1d-020ad330b0e9 | -1.1836 | -53.5158 | 2024-10-28 02:55:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 40.5 |
| d46d7e5a-e284-3237-956c-f832f055b022 | -1.9763 | -52.0804 | 2024-10-28 02:55:16 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 35.8 |
| 373ed9a1-839e-318f-9563-6d951cca51bd | -2.0499 | -52.0791 | 2024-10-28 02:55:17 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 3a6faf96-6795-39fd-b696-d599cb8b2bf1 | -2.2846 | -53.7822 | 2024-10-28 02:55:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 122.5 |
| eb943f0e-7577-3981-9f2a-e3508bc91513 | -2.2845 | -53.8023 | 2024-10-28 02:55:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 539628cf-3992-3b3d-89c3-8a39bbf89fd6 | -2.2662 | -53.7825 | 2024-10-28 02:55:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 104.5 |
| a0660606-8e01-38c9-a942-6fef28511306 | -2.2662 | -53.8027 | 2024-10-28 02:55:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 0c811431-c696-345e-b3ab-3a97f19cd212 | -2.4104 | -48.5479 | 2024-10-28 02:55:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 4e570953-31ae-396e-a3ed-8595f82028c4 | -2.5311 | -51.1816 | 2024-10-28 02:55:20 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 26.8 |
| 2c8219bc-e2e5-3765-981a-0dd7891f7113 | -2.8515 | -49.2408 | 2024-10-28 02:55:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 461ef3f6-3096-34f5-abf8-5c7c3028118c | -2.833 | -49.2413 | 2024-10-28 02:55:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| e0f1c132-0717-336c-8c45-3eebe250ab09 | -3.0317 | -50.3967 | 2024-10-28 02:55:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 35d5a589-7465-34b1-8ac1-5b19728772f1 | -3.0317 | -50.4176 | 2024-10-28 02:55:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 124.4 |
| df650ccc-b562-397d-932f-14b012a2b65f | -2.9945 | -50.4816 | 2024-10-28 02:55:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 46313e4a-2d96-3342-9862-938cc1786692 | -2.9761 | -50.4821 | 2024-10-28 02:55:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 116.4 |
| 63dfc6b1-da4f-3916-9f89-bbbb58dd8193 | -3.0538 | -49.4895 | 2024-10-28 02:55:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 9235463d-b194-3470-82b0-9848e16f6e8c | -3.0501 | -50.4171 | 2024-10-28 02:55:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 8cb0f936-d1a4-3d0b-a4cd-3559e7702df3 | -4.2797 | -45.5362 | 2024-10-28 02:55:29 | GOES-16 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 74b6a045-057a-3a72-9939-5637df432f01 | -4.1201 | -47.3169 | 2024-10-28 02:55:29 | GOES-16 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 70267fb3-4a11-30cd-934d-a71d9f544191 | -4.428 | -45.6406 | 2024-10-28 02:55:30 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 55.6 |
| db377cca-8ba6-3abb-9a84-d3ea3678c58b | -4.4094 | -45.6416 | 2024-10-28 02:55:30 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 61.0 |
| e87dda70-36ba-3295-af3e-43aeac5fff97 | -4.7766 | -46.4022 | 2024-10-28 02:55:32 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 72.6 |
| e26d56e3-0e1e-3d5c-b85e-98ee9a1f1e30 | -4.758 | -46.4033 | 2024-10-28 02:55:32 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 0d92e5fe-16c3-3cf3-b399-32c8a1b7089c | -1.1836 | -53.4956 | 2024-10-28 03:05:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 41.2 |
| bc3fa58d-293d-3968-9a2e-6058ad66a374 | -1.1836 | -53.5158 | 2024-10-28 03:05:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 39.4 |
| 883086e6-47fd-3806-9378-7bdfc6248dd6 | -1.9763 | -52.0804 | 2024-10-28 03:05:16 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| cc8470b3-6411-319a-b322-ab044754e723 | -2.2662 | -53.8027 | 2024-10-28 03:05:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 2ef696af-dffa-36b0-bfad-0682ec5dc732 | -2.2662 | -53.7825 | 2024-10-28 03:05:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 146.9 |
| 3a0ea64f-1879-3b6f-b503-77f2e500c993 | -2.2846 | -53.7822 | 2024-10-28 03:05:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 90.4 |
| 958a535e-3d86-327e-ac11-ba4978b6d44e | -2.4104 | -48.5479 | 2024-10-28 03:05:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| f0d0e5f3-acb4-3db8-b3fb-79a6995c4021 | -2.833 | -49.2413 | 2024-10-28 03:05:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| b361cf61-3a90-368c-941d-6519d1f66dd2 | -2.9761 | -50.4821 | 2024-10-28 03:05:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 96.2 |
| 4e7fd182-6504-3ada-939d-e9ebc8cb449b | -2.9945 | -50.4816 | 2024-10-28 03:05:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 9b135c93-13ff-3d8b-90e7-c6652144ff42 | -3.0132 | -50.4182 | 2024-10-28 03:05:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 33.3 |
| e3778eac-710a-344d-ac3c-3e6bc73efcb7 | -3.0316 | -50.4386 | 2024-10-28 03:05:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 35.4 |


[Clique aqui para ver as próximas entradas](README22.md)

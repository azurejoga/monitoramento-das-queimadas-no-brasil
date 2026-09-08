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
| 354c47ec-be1f-33f5-b55f-ebca40d62f4e | -8.72344 | -62.44283 | 2026-09-08 12:29:00 | TERRA_M-T | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 10.3 |
| f8fc1a19-851b-3d42-be43-098fa7428b97 | -13.27654 | -61.77406 | 2026-09-08 12:29:00 | TERRA_M-T | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 858e03a6-1c44-32a7-a90b-bf012754d680 | -10.8147 | -60.79777 | 2026-09-08 12:29:00 | TERRA_M-T | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| db50784b-7ec2-370c-aff7-27970802d3e8 | -13.28603 | -61.77554 | 2026-09-08 12:29:00 | TERRA_M-T | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 8.1 |
| d5829f92-538c-3d12-9ec3-7cec40115059 | -7.0752 | -56.46645 | 2026-09-08 12:29:00 | TERRA_M-T | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 34.0 |
| 74338d66-1ab3-3ad1-a414-2576b35f0d23 | -13.20598 | -61.82174 | 2026-09-08 12:29:00 | TERRA_M-T | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 1a7f7292-68da-3501-b7a7-bb5cfd333df0 | -6.22706 | -55.62112 | 2026-09-08 12:29:00 | TERRA_M-T | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| c3929390-436b-3d4e-a154-fdc609e5ac03 | -13.26311 | -61.70164 | 2026-09-08 12:29:00 | TERRA_M-T | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 0fdcbcee-9171-3a5e-a51c-d77fe999944d | -10.83327 | -60.80055 | 2026-09-08 12:29:00 | TERRA_M-T | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 33.7 |
| 5629c67a-c270-3858-ad0d-2c013ec5f23a | -7.11535 | -56.51033 | 2026-09-08 12:29:00 | TERRA_M-T | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 7a216224-69d6-3dd0-8dc1-5e41674efa7a | -6.87829 | -55.61429 | 2026-09-08 12:29:00 | TERRA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| b23cd778-b79d-3e2b-bb2b-202a2d1a612c | -13.2155 | -61.82323 | 2026-09-08 12:29:00 | TERRA_M-T | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 570182b7-1bf8-3293-be75-92e77018be86 | -13.2237 | -61.70618 | 2026-09-08 12:29:00 | TERRA_M-T | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 13.3 |
| e18f3d14-2644-3e13-acd7-805c523bb9a1 | -10.8318 | -60.8105 | 2026-09-08 12:29:00 | TERRA_M-T | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 29.7 |
| 0b1c000e-63c6-3b91-bdb5-0274e3072996 | -7.06611 | -56.46519 | 2026-09-08 12:29:00 | TERRA_M-T | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 24.3 |
| c7db57e6-9949-3437-8d10-7a01acdbc00c | -13.27491 | -61.78456 | 2026-09-08 12:29:00 | TERRA_M-T | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 10.8 |
| ca248e0e-2fa3-3d6c-81c3-59479c56f4d4 | -8.55826 | -63.88546 | 2026-09-08 12:29:00 | TERRA_M-T | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 11.7 |
| d07550b4-fb5f-3d68-a3b5-a6321ab2a170 | -10.81323 | -60.8077 | 2026-09-08 12:29:00 | TERRA_M-T | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 3ebde2ac-0048-3bf7-9d92-3be00dadaa76 | -7.07651 | -56.45705 | 2026-09-08 12:29:00 | TERRA_M-T | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 26c91015-4a3b-3323-9990-a33445a67572 | -9.7695 | -43.506 | 2026-09-08 12:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 107.0 |
| 8cc29169-5e17-3769-983a-50d93fdf7a1c | -10.7017 | -45.9016 | 2026-09-08 12:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 133.4 |
| 073be1eb-e8b5-383b-8eda-327ad563ee63 | -9.7702 | -43.4589 | 2026-09-08 12:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 232.2 |
| f517808a-cf5c-3f8c-a6f9-088834e4178c | -9.7698 | -43.4825 | 2026-09-08 12:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 200.6 |
| 48914df4-b285-3452-acab-e87fa57cd693 | -9.7705 | -43.4354 | 2026-09-08 12:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 145.2 |
| de0c48e5-315c-3f1c-89ae-e16f20daafaf | -8.691 | -44.727 | 2026-09-08 12:30:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 81.0 |
| f4359c6f-f669-32a5-99d6-4405f944a84b | -7.6968 | -44.3247 | 2026-09-08 12:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 80.7 |
| bc4581cf-5b89-3236-b363-dc8fc15f11f2 | -9.7508 | -43.485 | 2026-09-08 12:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 36b405c4-79c4-37dd-af56-efd609bc39a4 | -10.7013 | -45.9244 | 2026-09-08 12:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 197.8 |
| 643bf929-523b-3424-a24b-dbde142a7a11 | -9.7511 | -43.4614 | 2026-09-08 12:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 109.3 |
| b22f24a9-9daa-317e-968e-9d8ab746c153 | -9.7138 | -43.4192 | 2026-09-08 12:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 87.4 |
| 7c1849fe-5bc0-3329-b6d3-e833dc61183c | -10.7208 | -45.8992 | 2026-09-08 12:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 220.2 |
| b315b6d6-2629-328f-8644-448e12705e99 | -2.7582 | -49.4771 | 2026-09-08 12:30:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 90.2 |
| 799f7f53-a902-310c-aa06-f30b855f583f | -11.3716 | -45.721 | 2026-09-08 12:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 110.6 |
| 7f2a9d68-dd56-3431-85ae-0048558cd5fa | -3.5406 | -48.1889 | 2026-09-08 12:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 8009531f-1288-3c8d-bca6-95cce7ddae4f | -9.7131 | -43.4664 | 2026-09-08 12:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 137.5 |
| 6a0e3e37-0595-3563-aaa5-bba487284644 | -9.7141 | -43.3956 | 2026-09-08 12:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 88.3 |
| 97730dd0-253e-38ca-9d4c-7c23f4f0e9cd | -9.7511 | -43.4614 | 2026-09-08 12:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 131.3 |
| 080f747f-2885-32a5-83c6-c91c0cfeb062 | -10.7208 | -45.8992 | 2026-09-08 12:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 149.9 |
| 5071c85a-7a3b-3c2b-9d11-c572af983b18 | -11.3713 | -45.7439 | 2026-09-08 12:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 109.1 |
| 74ca6410-12bc-3bbb-a272-5e12245a1491 | -9.7702 | -43.4589 | 2026-09-08 12:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 199.5 |
| 776e5e0c-a37c-33a4-8fa6-08a797bf221b | -11.3525 | -45.7237 | 2026-09-08 12:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 140.7 |
| 000fede9-0eff-37bc-92e6-2fe1c5140d3c | -10.7017 | -45.9016 | 2026-09-08 12:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 128.1 |
| ae496a70-d2fd-3844-8620-5ca538cd7ef6 | -11.3716 | -45.721 | 2026-09-08 12:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 141.6 |
| ebd32d02-5da6-326e-bd87-8d09fe1ba6c9 | -9.7127 | -43.4899 | 2026-09-08 12:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 8861acc2-91a3-394d-9aa0-f5c0ce8c9c29 | -9.7515 | -43.4378 | 2026-09-08 12:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 95.8 |
| dc13daaa-e2df-3578-a0e4-2b9615a33133 | -10.7013 | -45.9244 | 2026-09-08 12:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 232.5 |
| f73d1cff-2d26-3d56-8c4b-590f9a5f6eab | -9.7705 | -43.4354 | 2026-09-08 12:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 115.8 |
| 078ea498-4d53-3f0e-843d-9f227142f637 | -9.7138 | -43.4192 | 2026-09-08 12:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 97.0 |
| 21e978e0-3cf6-3c0e-b1e4-21570f36fe0e | -11.2764 | -45.7113 | 2026-09-08 12:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 116.9 |
| bee42201-9be9-3ec2-8837-eea84be971c0 | -9.7508 | -43.485 | 2026-09-08 12:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 101.9 |
| 10ceb3de-bcb1-3b7b-94dc-7266c3f93c0e | -11.2767 | -45.6885 | 2026-09-08 12:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 101.5 |
| 933d8c33-e50e-31db-a4ec-2f5027bd0dd0 | -2.7582 | -49.4771 | 2026-09-08 12:40:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 88.1 |
| ac1d7c27-34ca-3e86-a67a-ddfdb24d8cb6 | -9.7698 | -43.4825 | 2026-09-08 12:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 133.4 |
| 5db9fdbf-0845-363d-b103-f00dc1f5d709 | -9.7705 | -43.4354 | 2026-09-08 12:50:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 6728b3b3-ce95-329c-a92a-e3a15fd9cc97 | -3.5406 | -48.1889 | 2026-09-08 12:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 100.1 |
| b792a96a-4cad-3f3e-9a14-98d472eda47e | -2.7582 | -49.4771 | 2026-09-08 12:50:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 146.2 |
| d10ba2ca-0e03-3f3c-ac2d-949aa27b09dd | -7.6968 | -44.3247 | 2026-09-08 12:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 912e446e-0fca-3979-bc46-7e34fd5be09f | -11.3521 | -45.7465 | 2026-09-08 12:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 220.9 |
| c58be558-67eb-335a-8e13-f403f850c48f | -11.3716 | -45.721 | 2026-09-08 12:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 304.4 |
| fa193f29-350a-3915-a918-8f46b0e44dda | -2.7582 | -49.4983 | 2026-09-08 12:50:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 94692ee9-25c2-3fca-a490-fe17aa8095e1 | -11.3713 | -45.7439 | 2026-09-08 12:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 253.9 |
| 95c10385-68e3-396a-ac9d-d00ff9241c6b | -9.7138 | -43.4192 | 2026-09-08 12:50:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 92.3 |
| 9f0b3763-b349-31f1-8351-0b7c1bfa2200 | -9.7141 | -43.3956 | 2026-09-08 12:50:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 85.3 |
| 0272cd96-e244-326b-9eb1-8299e9368ec8 | -3.5407 | -48.1673 | 2026-09-08 12:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 78.2 |
| af25cefb-f353-31f2-bf46-cbdc317b4bf9 | -11.3713 | -45.7439 | 2026-09-08 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 348.8 |
| f9b626b0-ab7c-39fa-ba51-498cf34934e4 | -11.3521 | -45.7465 | 2026-09-08 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 188.5 |
| 907d370c-82cc-3bb4-bded-5b6fc5b34c3d | -2.7582 | -49.4771 | 2026-09-08 13:00:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 116.0 |
| 84637be1-1f2c-3dbf-aaf3-3ebc5b8d47b5 | -3.5592 | -48.1666 | 2026-09-08 13:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 022616b7-a35b-3c8e-95cf-7f3942ef4602 | -9.7702 | -43.4589 | 2026-09-08 13:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 187.5 |
| 3f5acec6-ce55-3993-93ac-d7438d72a5a3 | -11.3525 | -45.7237 | 2026-09-08 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 327.7 |
| b5478dde-2362-322d-95e0-dc3308647794 | -9.7705 | -43.4354 | 2026-09-08 13:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 113.0 |
| db6cc0ee-c846-363e-8288-fe2f622573d3 | -10.7013 | -45.9244 | 2026-09-08 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 159.6 |
| 203049c5-2961-3636-836d-43d9a8386fe3 | -11.3716 | -45.721 | 2026-09-08 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 475.9 |
| 3fff9a9a-bb72-36cc-99db-396d6354764f | -3.5591 | -48.1882 | 2026-09-08 13:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 112.0 |
| b6b314cb-7739-337a-94f0-d5cb5019cf8d | -3.5407 | -48.1673 | 2026-09-08 13:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 85.5 |
| 1051df16-7b7c-3ee9-9acf-d81c416a3dcc | -9.7698 | -43.4825 | 2026-09-08 13:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 108.8 |
| 206cc35d-21d2-33d3-852d-fbb868f79ae6 | -10.7208 | -45.8992 | 2026-09-08 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 152.4 |
| 59e83613-a941-3c84-90b1-147211a5ab9b | -7.6968 | -44.3247 | 2026-09-08 13:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 105.0 |
| af257f59-e882-397e-b54e-add45382c769 | -3.5406 | -48.1889 | 2026-09-08 13:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 131.5 |
| e585ea3f-dd56-3960-a579-e676adb533f0 | -9.7705 | -43.4354 | 2026-09-08 13:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 117.6 |
| af1d10cb-bdea-332d-be9e-657e26a9a2ba | -8.71 | -44.7249 | 2026-09-08 13:10:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 86ec0a53-0d7c-3e60-8595-a56df7ff8770 | -2.7582 | -49.4771 | 2026-09-08 13:10:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 167.5 |
| f246ad92-5bd2-377b-bb21-1f478cfbc992 | -10.8233 | -60.8019 | 2026-09-08 13:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 3cf2fa2d-3f70-3f83-b14b-dfeae74c83cf | -3.5407 | -48.1673 | 2026-09-08 13:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 171.4 |
| 8ed419db-507e-393d-ac0d-64c39ecceb68 | -3.5406 | -48.1889 | 2026-09-08 13:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 209.1 |
| ec5af611-b27c-35e2-a71c-3c5914bb6192 | -8.691 | -44.727 | 2026-09-08 13:10:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 145.4 |
| 57ddd986-7461-314c-bcb3-7fb3737460e3 | -11.3521 | -45.7465 | 2026-09-08 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 262.5 |
| e15d127b-28b6-3335-85d1-be831db7dd83 | -7.697 | -44.3016 | 2026-09-08 13:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 9557ce57-96c3-351f-9ec9-1a8cfaaf9376 | -9.7141 | -43.3956 | 2026-09-08 13:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 139.3 |
| e3fda53f-a557-3898-a6f9-190d6ee987bf | -11.3525 | -45.7237 | 2026-09-08 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 331.0 |
| 5355b0d2-915d-3a0f-9795-76936599a8ad | -3.5591 | -48.1882 | 2026-09-08 13:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| abf9f3f3-7a5d-3250-a606-abb5001d38a5 | -2.7582 | -49.4983 | 2026-09-08 13:10:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 35b9ccf5-3bf8-33cc-a079-5e1f89a8c700 | -10.0964 | -45.728 | 2026-09-08 13:10:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 538bac71-ac09-3475-86dd-2fc006c8497a | -7.6968 | -44.3247 | 2026-09-08 13:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 152.0 |
| b0d1359b-591b-3aed-978b-e2336920184b | -9.7138 | -43.4192 | 2026-09-08 13:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 167.3 |
| fbf1ad77-490d-3301-ba11-76aa8b894f8b | -9.72 | -43.46 | 2026-09-08 13:15:00 | MSG-03 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7692b577-c6d7-382f-b0b2-26b4ddac02df | -10.71 | -45.92 | 2026-09-08 13:15:00 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9b86265b-8b7b-33c5-9924-764d484acc3b | -9.69 | -43.46 | 2026-09-08 13:15:00 | MSG-03 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 76bd89f8-9abd-38d3-a4ff-51e09bbafb84 | -10.68 | -45.91 | 2026-09-08 13:15:00 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8cd8ad84-5307-31dd-a23c-0f9b0c8cf351 | -10.71 | -45.97 | 2026-09-08 13:15:00 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README28.md)

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

## Dados Diários - Página 106

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1d345c51-9790-3328-b4f8-fe3d65246ab6 | -16.79927 | -57.40794 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 41182c02-5d92-36ff-937a-e3b5f49430ac | -16.79887 | -57.41039 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 0a60f8ff-8179-3029-aa5c-ab7930007fce | -16.79884 | -57.4385 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.3 |
| 61734389-ecef-313c-af23-f048d6a9d3ec | -16.79862 | -57.44109 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 46ed5d3b-fc07-35c4-b603-3b977af31297 | -16.79818 | -57.4128 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 9c87f197-c019-3f9c-bd2b-ce836bc9e93c | -16.79781 | -57.41527 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| e05e5ae2-4157-33f3-913d-0040670a5a97 | -16.79465 | -57.42989 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| d28ba0f9-ac77-338f-bc1f-12ef58d01fc0 | -16.79384 | -57.43225 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 7274a455-ccb8-34e1-ab33-443e6e55c15d | -16.79359 | -57.43476 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 5c704c56-5b71-3346-9f8a-fab80c0c3675 | -16.79253 | -57.43967 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 3048b1ba-7646-3729-8183-1bbaad953e24 | -16.79166 | -57.442 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| ba670773-aa45-3289-9f09-a5d7be7ceed4 | -16.79147 | -57.44457 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 02b6fc61-1c63-3bec-a51d-c79c4f370fb0 | -16.78775 | -57.43086 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| ac9d2c5e-0e3d-3bae-9824-466d78c6d415 | -16.7875 | -57.43336 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 7a17b8d0-934c-3b6c-a9b2-d26de655cae1 | -16.78111 | -57.4628 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| efc77cbd-a686-39f2-9992-c75e44f0fccc | -16.78007 | -57.4651 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.7 |
| a1ceb047-1cc8-383a-9214-58c1f03d48c8 | -16.78005 | -57.46772 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 2f9c815a-2b15-37b2-9bf2-44939c8bbb3f | -16.77898 | -57.47263 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 8fdb230c-a580-3a06-ae54-d8a9de9db703 | -16.77787 | -57.47491 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 58ff1c2f-b476-3038-abf1-3503325e2221 | -16.77715 | -57.45153 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 775a7af0-c375-3419-9be8-08660f8a3f14 | -16.77502 | -57.46138 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 944c7c63-2de9-3e0a-bc57-b4a4061849a1 | -16.77455 | -57.40474 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| a80214e8-157a-3f4d-9d9b-41365f555447 | -17.13446 | -56.85091 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 202ba611-a547-3553-8acb-7daf2d9b68ed | -17.13055 | -56.84903 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 09b4e730-9ce9-3247-a50b-84af9bee91e6 | -17.1296 | -56.85348 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| f2200271-c47c-32f2-883c-31630dd6a18c | -17.1247 | -56.84769 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 24d31078-32d0-34ba-9627-055e4ea0e8d5 | -17.12375 | -56.85213 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| bd168711-c045-3931-af08-8a38b42c9aea | -17.11695 | -56.85522 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 438b9747-5e28-34f9-ab30-a49ac49684e3 | -17.116 | -56.85964 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 8341983e-0839-314d-a0ac-0d13d9907442 | -17.10525 | -56.8525 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| fd41fffc-b1d6-3393-bda0-7277a5b95e45 | -17.10429 | -56.85693 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| d81e0a0b-87b4-3396-b020-5195b2035f90 | -17.10334 | -56.86137 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 2f7ef278-de24-3eca-8933-e06a9456b922 | -17.0994 | -56.85116 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 43794a42-a736-3c11-9f6e-defed25b5b23 | -17.09844 | -56.85559 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 201fe5fa-6739-3bcb-bb93-da27ce32a6fc | -17.09749 | -56.86 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| b261f2ad-9056-3d54-b91a-7716a35e1209 | -17.09653 | -56.86443 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 2e30a1a9-a523-39bf-a5c3-9779ecf1f1e2 | -17.09557 | -56.86885 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 0ef36ef3-ce71-39b1-8a9f-d0f8285b5eb2 | -17.0926 | -56.85421 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 0bf86f4b-098f-3c04-b132-4d4a9acb187b | -17.09164 | -56.85864 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 3e2a80e2-bed5-304b-afa4-c158d1ea7dd8 | -17.09068 | -56.86306 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| df6a81f5-562a-3e1e-aa65-2eada28ee658 | -17.08866 | -56.84402 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 0d124179-09cb-3f99-9760-41821bfe6fe2 | -17.08771 | -56.84843 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 681fc213-99b5-358a-8126-306d98ac49c8 | -17.08675 | -56.85285 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 5ce59acf-c6bc-3cc8-8a64-db14e3688535 | -17.08579 | -56.85728 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| db5535ba-b58a-34b9-ba3a-a7c1ca6542a9 | -17.08482 | -56.86172 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| c1d625bf-7f6c-341c-9faa-bc9a0d04a90e | -17.08386 | -56.86617 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| a4b2ed09-3824-3532-8eab-7f3dcb90423d | -17.08289 | -56.87062 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 12c9de9b-4c4d-3310-bcd6-9817e53f7f28 | -17.08281 | -56.84269 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 040bb5d4-8977-3891-9c05-2d3c3d87f713 | -17.08185 | -56.84711 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| e67385d4-6905-3e90-ab83-4e76d2974266 | -17.08088 | -56.85156 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 51cdef3d-cfff-33fc-950a-41b538a6d8d1 | -17.07992 | -56.856 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 3a2c120a-79cb-3114-b3c7-288eab7f1e61 | -17.07896 | -56.86042 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| a709a925-8008-3a50-be97-2e3fbec80cb0 | -17.078 | -56.86484 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 92a53a22-e147-3b3a-855f-321c5226c445 | -17.06526 | -56.83866 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 443f545c-4e27-3cc1-b8df-6948756887d2 | -17.06429 | -56.84309 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 39f0b44f-78ce-33a8-b1b9-2ac8e4609fe5 | -17.13384 | -57.36663 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 6f103326-25d5-30bc-a5c2-2ebb7f03cdd4 | -17.13006 | -57.32575 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 8cfeae15-e250-36ba-ab4a-180eab51420a | -17.12902 | -57.33051 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| e85a5316-179f-3b09-bea2-709b41613d6e | -17.12696 | -57.34002 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.9 |
| 0dd9b476-2502-3749-8031-a31bdf0f2258 | -17.12678 | -57.36996 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.9 |
| a301f882-34e2-39e5-b7c4-a2533dde9703 | -17.12593 | -57.34476 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 7d32f9a7-cf4b-322d-80ec-8c25b7178b29 | -17.12075 | -57.36856 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.9 |
| 0e53c850-0380-3dd3-88b5-2fee5081743e | -17.11971 | -57.37334 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 16.8 |
| 7996756b-3ad3-3849-824d-99511a2d9465 | -17.11576 | -57.36241 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.3 |
| 6ee5ab65-6747-37f8-8776-796ca54bd28f | -17.11473 | -57.36714 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.3 |
| c6677675-eeab-36ce-9224-f67c38f20e6c | -17.10973 | -57.361 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.3 |
| 413b079f-d3c6-3099-93c6-8c328b4548fe | -17.09687 | -57.33298 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.0 |
| a065c6dc-d3e6-33a7-8d22-1be91bc45cdd | -17.09583 | -57.33776 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 69fdce70-b1c1-3d6b-85e4-5847fda53e49 | -17.08981 | -57.33635 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| d67844b6-b94c-3486-bf4b-07b543504c2e | -17.08772 | -57.34585 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| fabf5a00-1386-3334-b1d3-22277cb2bb58 | -17.08667 | -57.35061 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| a9900888-58f5-3355-a4dd-43999dd012b6 | -17.0775 | -57.36351 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.4 |
| 3ec62992-3758-3aed-99bf-4018d70258b3 | -17.07645 | -57.36829 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.4 |
| 53a87369-1e67-3d70-beda-29516d7dd2f5 | -17.07539 | -57.37305 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.6 |
| 66acb280-04a6-39af-9e13-ffdc7c9488df | -17.07147 | -57.36211 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.4 |
| 82ce2954-9ed3-33c8-99fb-08af46c4997e | -17.07041 | -57.36689 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.4 |
| a4d42818-d35a-34b4-928f-f0fa1b65c30f | -16.92244 | -57.48793 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.0 |
| fe2655bd-6fc5-30eb-94b2-8056877d8ab7 | -16.91741 | -57.48156 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.0 |
| 7f7b9a8b-225e-3b4d-9aa9-c3324bdc3294 | -16.91689 | -57.48336 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.2 |
| 4a11c516-02a3-321e-b77a-d4464a4c8a7d | -16.91636 | -57.48647 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.0 |
| ce438e1b-7dd5-3ae8-bc5d-e74c1b774f6b | -16.9158 | -57.48826 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.7 |
| 10846c8b-ce53-3b9c-866e-d0afb99c0cc7 | -16.9749 | -57.48149 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 33.1 |
| 13abe624-fefc-3424-900d-e9d945c32ce4 | -16.9545 | -57.487 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 14.0 |
| 69fbcd9f-2fa2-3204-af50-13ddf1b18de2 | -16.95235 | -57.49678 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 29.1 |
| ea40c74f-b507-37a9-97e2-86254700c563 | -16.95127 | -57.50168 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 29.1 |
| b616cb0e-6dab-32bf-982f-777a2cb06603 | -16.94841 | -57.48559 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 14.0 |
| c619247a-b0c3-3bae-bf04-dac957a454d8 | -16.94626 | -57.49537 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 29.1 |
| 6eca03e9-f254-34a2-ad03-4b4c021b0a72 | -16.94341 | -57.47927 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| c8b8030e-1b88-39f5-80b7-6234d778e6c6 | -16.93909 | -57.49884 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 17.9 |
| d7b41d10-5d31-3d22-8ac4-a3195975a094 | -16.938 | -57.50376 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 20.1 |
| 5d81d084-3e9d-3f51-ba6f-5085d7321ff3 | -16.93645 | -57.68642 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 893127c0-1a70-371e-ab81-4c74733fabd0 | -16.93535 | -57.69147 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 64543fd2-60a4-31ba-82cd-1e569c5cf4ba | -16.93424 | -57.6965 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 9a3702af-249b-3223-8175-0de750b7f8a4 | -16.93407 | -57.49254 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 17.9 |
| f11343c3-9e36-3f8c-8fe5-8bd55aae2934 | -16.93314 | -57.70155 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| c862c91f-0cc1-356c-8477-facf6d2943f6 | -16.93299 | -57.49743 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 17.9 |
| 5b92304b-4d9c-3d09-b12f-b0415c61751c | -16.9319 | -57.50233 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 20.1 |
| 124c31e3-4c41-3ae2-85f6-2a69dc4f35fc | -16.93029 | -57.68498 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 55d6a255-64d0-3c5d-b7ea-ab8f906b1586 | -16.92919 | -57.69002 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 80e21904-2b1b-3aca-98cf-02d79959a99e | -16.92906 | -57.48623 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.1 |


[Clique aqui para ver as próximas entradas](README107.md)

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
| 068409a4-0e9c-3088-bbd2-280101ccb097 | -16.3185 | -53.8094 | 2025-06-19 12:10:00 | GOES-19 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 154.6 |
| 021eb79e-486f-34ac-a33b-739e00aa5cb2 | -8.5911 | -51.5537 | 2025-06-19 12:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 14c2e509-9e79-33b1-aa78-24cd7243f0f8 | -16.3189 | -53.7883 | 2025-06-19 12:10:00 | GOES-19 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 108.8 |
| 3a255e69-4d10-395b-9891-652484883240 | -4.8375 | -43.1919 | 2025-06-19 12:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 122.5 |
| 05c6ff8c-ecf1-3a99-862e-1552d64fcfc0 | -4.8375 | -43.1919 | 2025-06-19 12:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 136.2 |
| ff1b367c-3115-3cf6-b6c6-39a938b4d015 | -16.3189 | -53.7883 | 2025-06-19 12:20:00 | GOES-19 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 117.4 |
| 3e7106ed-5926-3563-bc39-5d9854c1740c | -16.3185 | -53.8094 | 2025-06-19 12:20:00 | GOES-19 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 156.1 |
| bedeaddd-a6b8-3357-9f52-c8f3daf166de | -4.00718 | -43.23979 | 2025-06-19 12:23:00 | TERRA_M-T | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 22c5c44d-5ca2-3c0d-b7ba-32745c562651 | -7.31678 | -45.38837 | 2025-06-19 12:25:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| da6b9d99-be35-3897-acf6-518e9cd3435d | -6.84823 | -45.57336 | 2025-06-19 12:25:00 | TERRA_M-T | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| ae9283b2-7c7c-3e7f-9160-28752e27b039 | -6.24202 | -44.65094 | 2025-06-19 12:25:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 94a146b4-0b89-3800-a610-2259abf63d47 | -7.13823 | -43.2878 | 2025-06-19 12:25:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 18.8 |
| 21d37333-d4f1-3f5f-b96b-388f8b7aff42 | -5.97001 | -43.75654 | 2025-06-19 12:25:00 | TERRA_M-T | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 28.2 |
| 6a6f18f7-63bf-3383-bc0c-766f92b291a3 | -7.08732 | -49.5939 | 2025-06-19 12:25:00 | TERRA_M-T | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 1dcf448e-eb23-3b7a-a61e-c22425de4f8c | -7.08577 | -49.60438 | 2025-06-19 12:25:00 | TERRA_M-T | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 5bbb90ea-a289-3058-9c00-625452552106 | -7.31812 | -45.37881 | 2025-06-19 12:25:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 56.9 |
| d979003f-36fa-35ff-b4fe-73aacdcc83a4 | -6.23261 | -44.64971 | 2025-06-19 12:25:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 40.0 |
| ecd41afd-1bcb-323c-b911-8f44fa7f6706 | -7.32706 | -44.72751 | 2025-06-19 12:25:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| cc977431-2589-372e-8616-0c1d71bbef1b | -5.442 | -43.50985 | 2025-06-19 12:25:00 | TERRA_M-T | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 995fa540-27bc-3dca-8043-c4fd97f55737 | -6.68937 | -43.20948 | 2025-06-19 12:25:00 | TERRA_M-T | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 17.7 |
| 4aea4bd0-104f-3e0c-a5c2-d141f97de400 | -7.15364 | -44.06491 | 2025-06-19 12:25:00 | TERRA_M-T | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 42.7 |
| b38050e4-cf0a-37b8-8ba6-d8dd22b921f9 | -5.48522 | -45.04222 | 2025-06-19 12:25:00 | TERRA_M-T | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 8d6c6b2d-7054-3c25-9d81-c2894e208576 | -5.45245 | -43.58054 | 2025-06-19 12:25:00 | TERRA_M-T | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 7d3a781d-3615-37f2-8d8d-9166f8602835 | -7.83198 | -44.79088 | 2025-06-19 12:25:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 3fd89aa2-0c4c-3ff6-a87c-2bed238c8de1 | -5.77399 | -43.47349 | 2025-06-19 12:25:00 | TERRA_M-T | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 25.7 |
| b28af5bd-8a95-3079-9831-b5cc7acc0151 | -7.00269 | -43.37702 | 2025-06-19 12:25:00 | TERRA_M-T | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 83bbba30-2183-3e17-9f57-017c07738664 | -4.8297 | -38.54831 | 2025-06-19 12:25:00 | TERRA_M-T | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 54.9 |
| 3550b2d0-3635-3f7b-82b8-c95d697b376b | -7.00434 | -43.36471 | 2025-06-19 12:25:00 | TERRA_M-T | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 13.4 |
| f9327b17-9e3c-3d51-b95e-e72f96050486 | -6.97007 | -44.06131 | 2025-06-19 12:25:00 | TERRA_M-T | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 2e9c320a-da25-3764-aacd-ca396402cbb1 | -6.69107 | -43.1971 | 2025-06-19 12:25:00 | TERRA_M-T | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 12.5 |
| 298a1a2a-9bfc-3966-9e5b-f3c909b53535 | -4.84153 | -43.19596 | 2025-06-19 12:25:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 153.0 |
| 348a5eb9-81e8-3eb8-91ba-41bb50fc6402 | -7.15738 | -44.04934 | 2025-06-19 12:25:00 | TERRA_M-T | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 3635b314-0be6-3dda-b645-b6a7f7d3099d | -5.86332 | -45.49835 | 2025-06-19 12:25:00 | TERRA_M-T | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 5d96d0bc-c98a-3102-a59b-3958039cb5a2 | -6.43248 | -41.22134 | 2025-06-19 12:25:00 | TERRA_M-T | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 18.8 |
| fe33037f-c810-3cb6-9311-ec2fb247397e | -6.97248 | -44.05678 | 2025-06-19 12:25:00 | TERRA_M-T | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 80aef8ee-95df-3c24-82b4-159c901f223e | -5.5696 | -43.47432 | 2025-06-19 12:25:00 | TERRA_M-T | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 19.2 |
| d22eb1f6-10f5-3107-ba27-d63d59f61928 | -4.82617 | -38.57499 | 2025-06-19 12:25:00 | TERRA_M-T | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 30.0 |
| aee9b3c5-abc9-33df-8b38-381c61584599 | -4.84317 | -43.18416 | 2025-06-19 12:25:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 07c6d097-7d5e-3270-a05f-511c20c99e0d | -7.31948 | -45.36922 | 2025-06-19 12:25:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 9b7c1fa0-5847-3422-8796-13f8a217c7ef | -6.84766 | -42.8031 | 2025-06-19 12:25:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 14.0 |
| 56d4cac0-3fa3-31c5-9599-7b1567a08e79 | -5.45404 | -43.56916 | 2025-06-19 12:25:00 | TERRA_M-T | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| fd441f5a-0350-31bb-bd5a-638bff252ab9 | -6.6222 | -45.67194 | 2025-06-19 12:25:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 6eb9359b-bef7-3061-89cc-ba949617ab9d | -6.11596 | -43.95835 | 2025-06-19 12:25:00 | TERRA_M-T | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| e32f6b67-edfd-362b-b9f7-fd53b289734e | -6.95482 | -42.80227 | 2025-06-19 12:25:00 | TERRA_M-T | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 24.0 |
| 0feebcc0-fc70-33b0-8dcf-7304a1daa882 | -6.95158 | -42.79545 | 2025-06-19 12:25:00 | TERRA_M-T | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 26.5 |
| 8977802b-f33c-3861-a244-72379ba6efae | -5.77557 | -43.46183 | 2025-06-19 12:25:00 | TERRA_M-T | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 24.2 |
| 6a67010b-c4f5-3a12-bf2c-bd97666a32f2 | -7.26437 | -45.36171 | 2025-06-19 12:25:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 4f5bf006-13b3-3b21-8947-4363f4b1ec8d | -6.32719 | -43.76144 | 2025-06-19 12:25:00 | TERRA_M-T | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 371578a0-ddb0-310d-bdaf-2d8d2b763902 | -6.85753 | -45.57115 | 2025-06-19 12:25:00 | TERRA_M-T | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| e37be030-d69e-3461-b2eb-f9f6e7234017 | -4.5522 | -48.00589 | 2025-06-19 12:25:00 | TERRA_M-T | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 16b9c60a-46ce-3ca9-97bd-40c2acec37d7 | -7.15588 | -44.06053 | 2025-06-19 12:25:00 | TERRA_M-T | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 47.0 |
| 30c1bc62-d8c7-388b-9c85-2cf6c966780a | -5.85257 | -45.96094 | 2025-06-19 12:25:00 | TERRA_M-T | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 77321dab-f9a1-33b5-97a0-76cb36ace07c | -7.41703 | -47.47166 | 2025-06-19 12:25:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| f0b2f55b-de18-3c84-b38b-e69dc4d9fa80 | -4.8314 | -43.19463 | 2025-06-19 12:25:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 67.5 |
| c683cb0b-aeaa-336e-a41b-479521b61bc8 | -6.24701 | -44.65751 | 2025-06-19 12:25:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 97ec8bf1-ebe1-3b94-a1c9-2cb7ecbc1c8b | -8.12635 | -43.13286 | 2025-06-19 12:25:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 15.9 |
| 0a688816-4297-3967-a90d-eac4116600d6 | -6.84957 | -45.56401 | 2025-06-19 12:25:00 | TERRA_M-T | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| f59b5f61-af37-3f87-95e8-a7ba8db349af | -7.31095 | -44.70438 | 2025-06-19 12:25:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 0cfc4fa6-4097-37f4-b9af-0f381fbcd6b9 | -7.55664 | -44.50021 | 2025-06-19 12:25:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 942da01c-963d-34f4-8b1f-c7f441dff9d5 | -5.12817 | -45.0263 | 2025-06-19 12:25:00 | TERRA_M-T | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| e3a3efdd-fc0d-3167-85b2-64824d712156 | -8.07073 | -43.10612 | 2025-06-19 12:25:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 81.3 |
| bd99c618-97a3-3512-8fcc-bb9c5e3e42d3 | -6.32874 | -43.75021 | 2025-06-19 12:25:00 | TERRA_M-T | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 4f7dd93b-f74c-3ec6-ab06-dd13e307b571 | -5.44042 | -43.52123 | 2025-06-19 12:25:00 | TERRA_M-T | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 837aa342-7528-3f9e-91b3-958758be193e | -7.21712 | -43.22733 | 2025-06-19 12:25:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 13.4 |
| 59e3677d-fef2-3838-8b65-063359257f3d | -7.22284 | -43.41859 | 2025-06-19 12:25:00 | TERRA_M-T | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| e015aa0b-35dc-3463-a84c-8731ee865033 | -6.56508 | -44.03836 | 2025-06-19 12:25:00 | TERRA_M-T | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 32.0 |
| 6139b423-61e4-347a-8df9-146b48059363 | -6.26956 | -45.42768 | 2025-06-19 12:25:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 7f9ed0d0-45ab-3180-9036-064b77668e05 | -6.83692 | -42.80163 | 2025-06-19 12:25:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 13.3 |
| f4673ca0-c252-3dc2-a2a3-340d8bca96dc | -7.2361 | -43.0861 | 2025-06-19 12:25:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.5 |
| 0f09fe8e-e52b-3b87-8b55-741fd13224b5 | -7.15519 | -44.05386 | 2025-06-19 12:25:00 | TERRA_M-T | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 36.2 |
| 1f6a7c7d-37ee-3113-b9f8-6dc2ab23f90d | -5.77717 | -45.90736 | 2025-06-19 12:25:00 | TERRA_M-T | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 74d7f1a4-ae63-39e9-80e8-57f45edf2aac | -4.82546 | -44.35382 | 2025-06-19 12:25:00 | TERRA_M-T | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| f35cabed-c392-308f-b336-d792c472180c | -6.27863 | -45.42899 | 2025-06-19 12:25:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| f4914b05-11b6-3f2b-9e2f-7012703ecb87 | -6.6235 | -45.66274 | 2025-06-19 12:25:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 33.7 |
| fdf3ee1d-a2af-3644-92f8-43568bfcb919 | -6.24061 | -44.66094 | 2025-06-19 12:25:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| d3337fed-d2f4-3e1f-b83b-4f2f68f12b9e | -14.62886 | -46.83771 | 2025-06-19 12:27:00 | TERRA_M-T | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 829fe1a7-383d-3d0b-9e38-e6b661266c27 | -11.56783 | -47.32562 | 2025-06-19 12:27:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 1f6f8b7f-4482-3dda-bbbd-3590d15c64b4 | -8.53027 | -47.67787 | 2025-06-19 12:27:00 | TERRA_M-T | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 074dc6f4-0af7-3733-9efc-a359ded4e722 | -12.23782 | -44.22154 | 2025-06-19 12:27:00 | TERRA_M-T | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 53.9 |
| ef12a5af-219b-3dd7-be9e-60f1b61659da | -8.20086 | -47.15379 | 2025-06-19 12:27:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3dd4cb6b-b5e7-3322-a836-d7a16a8df86c | -8.61824 | -45.02728 | 2025-06-19 12:27:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 002294ac-6260-317c-9297-5c8c4625543c | -11.46194 | -47.29488 | 2025-06-19 12:27:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ff17f662-115d-30f4-9e59-e93a12e5def1 | -8.75031 | -45.40628 | 2025-06-19 12:27:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 9c39d875-f140-3214-a7a2-3a84da0a6469 | -7.75364 | -47.61965 | 2025-06-19 12:27:00 | TERRA_M-T | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 26.3 |
| 2328fca8-29f9-381b-823e-6efbd1f36807 | -8.6277 | -45.02858 | 2025-06-19 12:27:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 25.9 |
| ef5c1758-f994-3cb1-b4a9-98fcd80576eb | -11.28794 | -48.69207 | 2025-06-19 12:27:00 | TERRA_M-T | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 5df558b6-c45a-3d7f-9d14-0551cc2bf7fd | -10.83544 | -54.00887 | 2025-06-19 12:27:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 86.5 |
| 1e491a1f-d3b4-329c-8d4e-a5bcaa9bd848 | -11.80141 | -43.79501 | 2025-06-19 12:27:00 | TERRA_M-T | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 7335a67f-8f9e-3aec-8d0b-41ecceebc661 | -11.17912 | -47.40232 | 2025-06-19 12:27:00 | TERRA_M-T | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 33.8 |
| c1e5f15e-f781-3e39-bbf9-3b103e0c81ac | -10.13243 | -46.26637 | 2025-06-19 12:27:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3f889ee2-9f76-3cb8-a573-1af7e5ae3f84 | -8.72447 | -47.99734 | 2025-06-19 12:27:00 | TERRA_M-T | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 06f11ba6-fdfa-31ea-8901-6eda70ca6297 | -8.59366 | -51.56107 | 2025-06-19 12:27:00 | TERRA_M-T | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 6a5078a8-8b6b-3b94-92c0-7d4d9616499d | -11.58846 | -44.66181 | 2025-06-19 12:27:00 | TERRA_M-T | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 78c63ec6-f349-305e-b343-60d65cbd5405 | -8.25378 | -46.3891 | 2025-06-19 12:27:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 5773546f-46af-3e98-aca8-06b160da57bb | -12.80158 | -44.90455 | 2025-06-19 12:27:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 8c87c72e-988d-3fd5-bb84-0b431dd451ce | -9.80124 | -47.17714 | 2025-06-19 12:27:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 3811c74c-2115-3671-bb06-c3378995d92f | -11.57953 | -47.63721 | 2025-06-19 12:27:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 696b6485-faba-3634-909f-59ba024306fb | -12.4023 | -46.36358 | 2025-06-19 12:27:00 | TERRA_M-T | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| dc25169d-0618-3b52-b47e-fc31002ffa45 | -8.58385 | -49.51797 | 2025-06-19 12:27:00 | TERRA_M-T | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| c6ca4c83-2230-3a43-9776-1021f0f1a1b8 | -12.31543 | -50.03846 | 2025-06-19 12:27:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 18.7 |


[Clique aqui para ver as próximas entradas](README28.md)

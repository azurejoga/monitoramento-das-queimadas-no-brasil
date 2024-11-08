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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fa20e685-c11c-3418-a9d0-6090e60d7865 | -1.1494 | -52.01768 | 2024-11-08 01:36:00 | TERRA_M-M | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 48.8 |
| ed70a311-de9b-3a70-bad2-defaecf98496 | -2.45176 | -53.69942 | 2024-11-08 01:36:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 13c696f9-946f-3ace-9dd6-443e0ae675b9 | -2.80097 | -52.95831 | 2024-11-08 01:36:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 119.4 |
| 85ddb46a-68b9-3a84-bb6b-f023b666e8e3 | -1.38852 | -52.20756 | 2024-11-08 01:36:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 26.0 |
| 8736b6eb-5481-3036-bf50-ee8f5fc571be | -2.15853 | -53.6649 | 2024-11-08 01:36:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 22.3 |
| 90a6343d-5e18-357d-b3e2-1dfefa12060c | -3.05814 | -57.10783 | 2024-11-08 01:36:00 | TERRA_M-M | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 052a3c4b-b3c0-3319-bcb7-8440fd6e5c91 | -2.28439 | -53.81001 | 2024-11-08 01:36:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 4a85b3e6-9bd9-3605-8189-9609cfe8fb93 | -1.46577 | -53.41386 | 2024-11-08 01:36:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 6bba485c-775c-3536-8be3-78262b4114ab | -7.68842 | -61.05672 | 2024-11-08 01:36:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 89bd776b-fb0b-3205-b93b-fb1a61732bb1 | -2.79785 | -52.93731 | 2024-11-08 01:36:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 190.6 |
| d2420720-9373-3344-8dc5-955696d851ae | -2.93832 | -52.71539 | 2024-11-08 01:36:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 3a370c48-19a0-3d8e-9107-45fba01ce8a3 | -1.14562 | -51.99125 | 2024-11-08 01:36:00 | TERRA_M-M | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 59e421b3-aa02-3cf0-8150-f0979c5a60d4 | -3.15445 | -54.48805 | 2024-11-08 01:36:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 34.3 |
| 74aa2944-d9aa-392f-af06-1378ee75c4a2 | -3.04528 | -53.27922 | 2024-11-08 01:36:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 95d5ac37-45a3-3e65-993d-a4cd50c0e616 | 1.00639 | -60.58491 | 2024-11-08 01:38:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 9.1 |
| d4657989-1a4b-39fd-9d7c-040ff2d4a8fc | -1.14661 | -53.64989 | 2024-11-08 01:38:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 79dc2285-3102-3b5d-b352-d2686b1105cc | -1.33626 | -54.62091 | 2024-11-08 01:38:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| d727aa4c-fbdd-39c1-b08b-66b25d37300c | -1.14702 | -53.65565 | 2024-11-08 01:38:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| cd03afd6-2bd3-33a4-94d0-b024c2411c27 | 0.74239 | -59.76951 | 2024-11-08 01:38:00 | TERRA_M-M | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d8f1e7b7-5783-3ad3-93a1-8ac4008d480a | -1.68836 | -60.14785 | 2024-11-08 01:38:00 | TERRA_M-M | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 26eaacb3-15d4-31c5-87f3-9ea5e2ee5fc0 | 0.74116 | -59.77837 | 2024-11-08 01:38:00 | TERRA_M-M | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 42714e25-5f7d-327e-9e43-de07784ec535 | 0.62053 | -59.91739 | 2024-11-08 01:38:00 | TERRA_M-M | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5a1b27b1-fb72-31ee-82ff-3e175cb6f8a9 | -1.25237 | -53.38175 | 2024-11-08 01:38:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 32.3 |
| d9f33ddd-3c21-3f24-9788-ed26ddf9f71d | -0.63981 | -52.39344 | 2024-11-08 01:38:00 | TERRA_M-M | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 15.9 |
| c8f5ee6f-1e67-3f82-b34c-b348eaa4998b | -3.5632 | -47.3629 | 2024-11-08 01:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 533d6785-0e63-34db-a289-5dac3f510fa1 | -3.5447 | -47.3636 | 2024-11-08 01:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 1836d16e-7b1b-3cb1-a402-2f2867ffc032 | -4.521 | -45.658 | 2024-11-08 01:40:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 134.8 |
| 196eecc9-2360-3209-8187-fadf5cf5c775 | -3.5446 | -47.3855 | 2024-11-08 01:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 102.4 |
| 0bea67dc-1816-321b-8078-90b7dae43de7 | -2.8016 | -52.9414 | 2024-11-08 01:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 225.3 |
| 9fd58887-96ed-31d0-ac9e-abf62d14bb15 | -3.1642 | -54.4654 | 2024-11-08 01:40:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 60978089-ac44-3512-9ba3-4db72640890e | -2.82 | -52.9409 | 2024-11-08 01:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| cc220bcb-5d56-3889-a4e3-c747e0a69d14 | -3.7254 | -41.6987 | 2024-11-08 01:40:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 66.8 |
| 1ed74019-ef79-3fb1-8f79-56d05710cddb | -4.6834 | -46.4296 | 2024-11-08 01:40:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 11454b83-aac5-36c4-94e5-5fd5f7b78abf | -3.967 | -48.15 | 2024-11-08 01:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 85.3 |
| 986d60d7-2986-3cbf-b86a-c1d0fb999071 | -3.1641 | -54.4854 | 2024-11-08 01:40:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 46.9 |
| a2d7cf48-0b4b-353e-8228-9c8ac13d33da | -4.5207 | -45.7029 | 2024-11-08 01:40:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 174.6 |
| 292692c9-b197-3184-872e-1ee27d73ab9a | -5.9911 | -46.08 | 2024-11-08 01:40:00 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 66.2 |
| fbcabc26-a1f4-33bc-8e93-e74a0afcfb4f | -3.5631 | -47.3847 | 2024-11-08 01:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 105.3 |
| 7305f578-f475-3ef6-88b0-8ae3b65e7af0 | -4.5022 | -45.6815 | 2024-11-08 01:40:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 134.8 |
| f668c803-1a01-3834-b5ef-7c06959bbbaf | -2.8016 | -52.9617 | 2024-11-08 01:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 120.3 |
| 0f7ecfa9-0b0c-32eb-bd42-a3f56ba3183d | -4.5395 | -45.6794 | 2024-11-08 01:40:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 102.8 |
| d99bed1a-d056-356a-9608-e1fc6a9434e9 | -3.9669 | -48.1716 | 2024-11-08 01:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 149.3 |
| 0552623c-bf7c-3b42-b5f7-07ac359dd4b2 | -2.82 | -52.9613 | 2024-11-08 01:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 43185de2-d8e5-3199-802f-ca4c0d777e36 | -4.5209 | -45.6804 | 2024-11-08 01:40:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 417.6 |
| 505ded1a-8ca0-3136-af9e-fb11518fdb7f | -3.9483 | -48.1724 | 2024-11-08 01:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 90a5e252-4a64-313c-b0e5-3d86c015cd64 | -3.9854 | -48.1708 | 2024-11-08 01:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 8d10e180-f6c1-3500-9b47-142e1f9a31af | -2.9239 | -45.146 | 2024-11-08 01:40:00 | GOES-16 | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 58.7 |
| ca21f9e7-766f-3fe7-a2b8-2ac884e98e91 | -4.6832 | -46.4518 | 2024-11-08 01:40:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 151.8 |
| a0ff5034-46e4-3242-a4e0-11fcd5ff9df5 | -4.5395 | -45.6794 | 2024-11-08 01:50:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 105.8 |
| 098f581b-5a91-323b-9e28-65539b3bf4a4 | -4.6832 | -46.4518 | 2024-11-08 01:50:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 134.4 |
| 9327f909-5fcb-3ff1-948a-91d12bd98c5e | -4.521 | -45.658 | 2024-11-08 01:50:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 103.3 |
| 94c05b4b-7ba1-3e5d-b609-e7eb0638e5dc | -4.5022 | -45.6815 | 2024-11-08 01:50:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 158.2 |
| 39650b06-4a28-3d2c-9185-f10eb8cc85de | -2.82 | -52.9613 | 2024-11-08 01:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 1d5693aa-c6b3-3a86-8762-c62c99418c73 | -4.6834 | -46.4296 | 2024-11-08 01:50:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 97.8 |
| 5e93b17b-d1de-3cc1-b34f-009b75f4fddb | -3.5447 | -47.3636 | 2024-11-08 01:50:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 1b74f51a-4cac-3dda-81f7-6f01118db1bd | -3.5446 | -47.3855 | 2024-11-08 01:50:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 83.0 |
| f25dc94c-e0ae-31bd-8801-405fdd35a9dd | -3.1641 | -54.4854 | 2024-11-08 01:50:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 95b6d4e4-42eb-3071-bf1c-b1e2e7878cac | -4.5209 | -45.6804 | 2024-11-08 01:50:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 314.5 |
| 15fa17ef-c6e4-308d-8d41-63f3a9c15c5b | -3.5631 | -47.3847 | 2024-11-08 01:50:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 101.3 |
| bc6e3e3e-3f7a-3c7f-90c2-f9c7b2bb1516 | -4.5207 | -45.7029 | 2024-11-08 01:50:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 145.4 |
| 9bd566b9-ca7f-38c4-90c1-8bef07b560e6 | -3.1642 | -54.4654 | 2024-11-08 01:50:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 72c599e3-668e-3577-b699-59cd3b8b0e5c | -2.6228 | -51.3038 | 2024-11-08 01:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 24459007-680c-3f90-8aa1-8c6c34d0a2e7 | -3.5632 | -47.3629 | 2024-11-08 01:50:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 66.1 |
| ab34b4a5-224c-3c92-9b7d-af27517e8dfb | -2.8016 | -52.9617 | 2024-11-08 01:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 100.3 |
| bb257df7-c324-316d-995a-1b90885c9826 | -3.967 | -48.15 | 2024-11-08 01:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 86.0 |
| c96b0ab6-05ba-360a-b3fb-ff88c403500c | -2.82 | -52.9409 | 2024-11-08 01:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 109.2 |
| 93bebf13-0f45-3de1-9e7d-4e13bea6864c | -4.5021 | -45.7039 | 2024-11-08 01:50:00 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 59413123-e9c0-3bef-83bf-8fca45638645 | -2.8016 | -52.9414 | 2024-11-08 01:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 230.6 |
| 866d17f0-1b94-3d60-9c32-af8f2216d39c | -3.9669 | -48.1716 | 2024-11-08 01:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 158.4 |
| 959dfee8-6fc7-330b-b488-af0ab35f08f3 | -7.9228 | -61.464699 | 2024-11-08 01:53:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 59d59682-3cda-303d-ba48-a797dc2e898f | -4.5209 | -45.6804 | 2024-11-08 02:00:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 302.4 |
| 69292521-acc6-3346-ade2-278774502c6e | -2.82 | -52.9613 | 2024-11-08 02:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 3a678b3c-a267-31ef-90ed-027e65cd3055 | -4.521 | -45.658 | 2024-11-08 02:00:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 113.5 |
| a12bd906-6d00-35f0-a46c-50c7979090fd | -3.5446 | -47.3855 | 2024-11-08 02:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 105.2 |
| b07b8c59-b6b8-315e-98c0-bcff076c3deb | -4.5022 | -45.6815 | 2024-11-08 02:00:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 138.9 |
| 2c15d7f4-c0af-3e65-aa48-82fd39d91a27 | -3.5631 | -47.3847 | 2024-11-08 02:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 117.7 |
| f43ff0c5-04b0-34a3-88a6-c2474da88460 | -4.5395 | -45.6794 | 2024-11-08 02:00:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 830216ee-da7d-3d81-b462-bf99162aa4af | -2.7832 | -52.9418 | 2024-11-08 02:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| ec4e0240-e6c7-3f01-9671-54eb7af158f5 | -4.6834 | -46.4296 | 2024-11-08 02:00:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 69.8 |
| ddf9e79b-10e2-30ab-95a4-909dfe47c1a8 | -2.8016 | -52.9617 | 2024-11-08 02:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 106.1 |
| 0c7f7fd8-67d9-377c-99d1-36a3cef7978b | -3.9485 | -48.1508 | 2024-11-08 02:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 4f8756eb-a415-3a6f-944d-9c3909d9b680 | -2.8016 | -52.9414 | 2024-11-08 02:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 205.8 |
| 9b0cf219-faa7-3d2c-ab3b-73d08dd6f16a | -3.5632 | -47.3629 | 2024-11-08 02:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 44065758-ea49-38a2-bbd3-c7ecd7f5c4b0 | -3.9669 | -48.1716 | 2024-11-08 02:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 155.7 |
| ebb19f8a-5abd-334c-95f7-067be61bd2c6 | -3.967 | -48.15 | 2024-11-08 02:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 82.5 |
| 03206b50-aa8a-3b19-bb4e-4f2df47bf444 | -4.6832 | -46.4518 | 2024-11-08 02:00:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 111.2 |
| 9d065421-bda9-3eac-a052-1ab42b107eae | -3.5447 | -47.3636 | 2024-11-08 02:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 7daea188-ead3-3254-9f61-2e0f3271dc0c | -4.5207 | -45.7029 | 2024-11-08 02:00:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 129.3 |
| 1c3885e5-0109-360b-9c10-70cd659c3bd7 | -2.6228 | -51.3038 | 2024-11-08 02:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 210b7660-9874-3501-a281-66d04910f463 | -2.82 | -52.9409 | 2024-11-08 02:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 116.8 |
| 58500e58-48fe-313d-b116-75127865aedb | -4.49 | -45.7 | 2024-11-08 02:00:00 | MSG-03 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6df30d37-3eea-3806-a077-42d5cc07c410 | -4.52 | -45.7 | 2024-11-08 02:00:00 | MSG-03 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| defee967-4562-3efa-91bc-cfef95c54490 | -4.5207 | -45.7029 | 2024-11-08 02:10:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 125.0 |
| fc82b1b5-9c5e-3ca4-a6b0-01b86d9e6116 | -3.967 | -48.15 | 2024-11-08 02:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 79.9 |
| c2e9d0e9-b795-38b3-a0e0-3130e6833ae6 | -3.5631 | -47.3847 | 2024-11-08 02:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 118.2 |
| de88be8a-aaae-3eac-869c-59c4bcce2d9e | -2.8016 | -52.9617 | 2024-11-08 02:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 85.6 |
| 03d4835f-ecfd-316b-8deb-5563333df5d1 | -4.6834 | -46.4296 | 2024-11-08 02:10:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 778542ff-53eb-3e94-baa1-351ba6349f7a | -3.5632 | -47.3629 | 2024-11-08 02:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 786ecfdb-9d3e-3364-a3b6-3ce5753be5b8 | -3.1641 | -54.4854 | 2024-11-08 02:10:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 929132aa-6867-3249-b974-58b083941900 | -3.1642 | -54.4654 | 2024-11-08 02:10:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 48.0 |


[Clique aqui para ver as próximas entradas](README11.md)

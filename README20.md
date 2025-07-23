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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 00ac6fa7-bf4e-3d8d-9192-e65e007300c4 | -3.16491 | -49.45853 | 2025-07-23 05:55:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 29d755eb-f58c-311a-827f-e1e21fb95215 | -7.75348 | -44.01118 | 2025-07-23 05:55:00 | AQUA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 4f3bf5bf-f10b-37ce-8364-c34d7e028e1f | -9.05474 | -45.06527 | 2025-07-23 05:55:00 | AQUA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 32.2 |
| 91cebee0-bced-3d2f-9112-f300faf002fa | -4.04635 | -42.52259 | 2025-07-23 05:55:00 | AQUA_M-M | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 26.8 |
| ffb49f08-b337-3d9d-a464-f65ce9bff06e | -13.69867 | -45.68948 | 2025-07-23 05:57:00 | AQUA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 13.1 |
| a099144e-0d22-3b3b-a6a6-b253657c518d | -13.70907 | -45.69093 | 2025-07-23 05:57:00 | AQUA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 14.5 |
| e48cb571-6516-301f-890d-4f8f3880ca54 | -17.56998 | -47.50623 | 2025-07-23 05:59:00 | AQUA_M-M | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 12.8 |
| a6a25558-f20e-31bb-97ec-401af9f4327a | -3.1833 | -49.4429 | 2025-07-23 06:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| a7a729ce-a348-3338-b16f-f9ba2ae4c102 | -3.1649 | -49.4435 | 2025-07-23 06:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 1b8cbb15-586f-32d3-b71f-2cab38ec21ee | -3.1648 | -49.4648 | 2025-07-23 06:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 4fcf7ffc-bd21-33f4-be7a-4716657cafba | -3.1832 | -49.4642 | 2025-07-23 06:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| c461cb0c-dec8-37d3-a677-96b8021b9401 | -3.1648 | -49.4648 | 2025-07-23 06:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 07bd32cc-f8cb-351d-bd0e-1a5fc520b8dc | -3.1832 | -49.4642 | 2025-07-23 06:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| cce97af9-136e-32fc-bffb-37870d4710a7 | -3.1649 | -49.4435 | 2025-07-23 06:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 53f849be-a630-3456-b8fc-c9823699b184 | -3.1833 | -49.4429 | 2025-07-23 06:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| ec0a9ba4-219b-3555-b4fa-614fbe09f56c | -9.11622 | -60.74811 | 2025-07-23 06:14:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 416d4f24-8618-306d-85f8-6c3069c95ad9 | -9.46074 | -63.14886 | 2025-07-23 06:14:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e2ee6527-5eae-32b7-8b4c-2ed373b08e4f | -7.93913 | -71.47614 | 2025-07-23 06:14:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 741d3467-a3e9-393a-8409-1ccd4510c20e | -9.12298 | -60.75335 | 2025-07-23 06:14:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4a5befb9-da95-37d9-98de-8d4df4bcab76 | -7.26154 | -60.18045 | 2025-07-23 06:14:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e5a576a3-66d6-3172-8a63-7482e72b48af | -9.11606 | -60.7526 | 2025-07-23 06:14:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 95c636ca-a74c-3183-bf2e-7a382be2fa7b | -7.2607 | -60.18723 | 2025-07-23 06:14:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 116a09d1-7ed7-3eaf-b4df-b0e30da847c9 | -9.11689 | -60.74567 | 2025-07-23 06:14:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 23ebbf5b-f080-387e-badc-f47c014636f7 | -8.29766 | -70.87328 | 2025-07-23 06:14:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f3d90f0f-aaca-3e83-880e-71720c9bdde2 | -12.35595 | -63.41877 | 2025-07-23 06:16:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 7825a0b9-40fc-3054-a478-e5285239577e | -12.35463 | -63.42329 | 2025-07-23 06:16:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 341db837-4700-3009-a5ad-2354a29fc53f | -9.76541 | -65.09486 | 2025-07-23 06:16:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 881b294a-c1fe-3438-b1ad-af30b56cd4c2 | -12.35543 | -63.4235 | 2025-07-23 06:16:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3e4c500d-5e24-39c0-bbde-ad49ec230bed | -12.34932 | -63.42274 | 2025-07-23 06:16:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 051afa76-13c4-3a41-9853-faad3c70d462 | -10.29697 | -60.54185 | 2025-07-23 06:16:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a925fcb7-234f-329f-b6ac-a4d00a161598 | -10.03154 | -67.74696 | 2025-07-23 06:16:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9213123a-aa30-340a-be2e-7b1662128d34 | -9.76013 | -65.09411 | 2025-07-23 06:16:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1df9cd7f-8b65-33f8-ad73-6699caebcde0 | -12.34852 | -63.42255 | 2025-07-23 06:16:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 37d3dcb6-9ebd-37ef-b1bf-395264822e6b | -12.35518 | -63.41858 | 2025-07-23 06:16:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 33169694-2729-3af7-8114-9cd0a3cc7202 | -10.29067 | -60.53405 | 2025-07-23 06:16:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2bfb94ba-cc11-39ee-8a55-f2d0d8d63a45 | -3.1832 | -49.4642 | 2025-07-23 06:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 76477064-3d0f-311c-a314-3bdce57d025b | -8.29346 | -70.87421 | 2025-07-23 06:42:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1e596dde-a2c6-3171-87e6-6382f2ffbe16 | -3.1648 | -49.4648 | 2025-07-23 07:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| bf46ee90-40a5-3ac3-9b40-b8a9ab42796f | -3.1832 | -49.4642 | 2025-07-23 07:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 2461bcdf-e135-32a4-9c00-239336900d95 | -3.1833 | -49.4429 | 2025-07-23 07:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| fbb7bbda-a4ce-32a0-86dd-c6e9a7805aec | -3.1832 | -49.4642 | 2025-07-23 07:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 15d3d244-3e18-3956-9253-10946aa69878 | -12.3439 | -63.4255 | 2025-07-23 09:30:00 | GOES-19 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 2c007824-a331-3ca1-9e1e-51b43a861285 | -12.3628 | -63.4245 | 2025-07-23 09:30:00 | GOES-19 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 9ae6eed6-7b87-3e10-8764-0d7c4e43cbdb | -12.3628 | -63.4245 | 2025-07-23 09:40:00 | GOES-19 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 9d98f040-1e8c-3e17-b5b4-0d35b4cbc722 | -12.3439 | -63.4255 | 2025-07-23 09:40:00 | GOES-19 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 58.5 |
| f167358c-d4b0-38c2-80c4-b677791caf3c | -12.3628 | -63.4245 | 2025-07-23 09:50:00 | GOES-19 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 83.3 |
| 10742695-16e8-3f8e-8d36-ff4f85440235 | -12.3439 | -63.4255 | 2025-07-23 09:50:00 | GOES-19 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 240cc93b-3deb-3292-b5a0-0305f4e7665c | -6.9804 | -42.7854 | 2025-07-23 11:00:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 112.2 |
| 18206bc1-a13c-3c6a-ab41-c4cb47e1fda7 | -6.9804 | -42.7854 | 2025-07-23 11:10:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 135.4 |
| 0e5fd8ed-0027-3c31-9578-94098dcba109 | -7.2822 | -44.3876 | 2025-07-23 11:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 128.2 |
| 271b3ba4-0cb2-3f22-974c-34fc74d0e18b | -6.9801 | -42.809 | 2025-07-23 11:20:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 95.0 |
| ab93ad8d-e39c-3ec6-87a8-b3e7a54f724c | -6.9804 | -42.7854 | 2025-07-23 11:20:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 105.1 |
| f43904fa-80fc-3934-9a92-1bdf093664ed | -6.9804 | -42.7854 | 2025-07-23 11:30:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 92.9 |
| e67e2c46-1989-3347-a3d6-121c236d0698 | -7.2822 | -44.3876 | 2025-07-23 11:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 109.2 |
| af7fc7bb-1b17-3f1e-a0f4-d7cc407a3092 | -6.9804 | -42.7854 | 2025-07-23 11:40:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 85.6 |
| d15243d0-a5b3-325b-8988-4f5c988ee140 | -4.61204 | -43.31226 | 2025-07-23 11:49:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 6ba12633-92c6-380e-87b2-ba86c2c09217 | -3.53063 | -39.77868 | 2025-07-23 11:49:00 | TERRA_M-M | MIRAÍMA | CEARÁ | Brasil | 2308377 | 23 | 33 | nan | nan | nan | Caatinga | 7.7 |
| fb8d1b49-cfbf-3be5-bd0c-d333dc631c02 | -4.19757 | -38.36745 | 2025-07-23 11:49:00 | TERRA_M-M | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 32.6 |
| 1644161e-155c-35e4-b317-c8a00b24272d | -3.93185 | -43.16211 | 2025-07-23 11:49:00 | TERRA_M-M | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 6db4f90a-3a84-35f2-83b3-ac7cb7528765 | -4.19883 | -38.35869 | 2025-07-23 11:49:00 | TERRA_M-M | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 65a1fc86-e01a-34fc-890a-dda2e3607f45 | -4.05291 | -42.52374 | 2025-07-23 11:49:00 | TERRA_M-M | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 64.6 |
| 8cb70662-11fd-33a4-8135-1ee09ac3d450 | -4.05489 | -42.51071 | 2025-07-23 11:49:00 | TERRA_M-M | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 36.3 |
| 6f89c0b3-8e86-3abb-a1d3-ba644fc7b009 | -4.04821 | -42.51701 | 2025-07-23 11:49:00 | TERRA_M-M | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 88.9 |
| d2ae1829-03f3-39b1-825e-d7d37f008371 | -3.82662 | -43.02185 | 2025-07-23 11:49:00 | TERRA_M-M | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 41.3 |
| e32bd004-0d69-32c6-b511-8c268335e528 | -4.11936 | -38.33228 | 2025-07-23 11:49:00 | TERRA_M-M | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 7c787d38-e477-34df-9ea4-feab4c46eeb6 | -4.04631 | -42.53014 | 2025-07-23 11:49:00 | TERRA_M-M | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 3345032e-20b7-399b-ba66-af31926154d8 | -4.60983 | -43.32689 | 2025-07-23 11:49:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 6dd2a7cd-991d-3b97-b314-08db07697f4b | -4.98762 | -42.39212 | 2025-07-23 11:49:00 | TERRA_M-M | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| f1435a3e-037a-3622-993b-084bb3cb2d4d | -3.52926 | -39.78796 | 2025-07-23 11:49:00 | TERRA_M-M | MIRAÍMA | CEARÁ | Brasil | 2308377 | 23 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 760a1fd8-5351-3a5a-bb17-bedd6febb3af | -6.9804 | -42.7854 | 2025-07-23 11:50:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 119.8 |
| d5faa99a-2860-3269-a746-cf446f2f98b1 | -6.9801 | -42.809 | 2025-07-23 11:50:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 99.8 |
| 449cfcb5-9ee5-3e6e-bc23-593037c8df0e | -7.2824 | -44.3646 | 2025-07-23 11:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 88b1693f-07f4-328c-9aac-0fa531208539 | -7.2822 | -44.3876 | 2025-07-23 11:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 130.6 |
| b768751f-f6e2-3367-a15c-953522712005 | -7.26037 | -44.30196 | 2025-07-23 11:51:00 | TERRA_M-M | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 23.7 |
| c9562914-f941-3ffa-9fb0-ee1b9ae8c556 | -10.53509 | -46.16091 | 2025-07-23 11:51:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 5859ae7d-3e1d-300f-ba9b-b0e47979fa29 | -12.27098 | -42.46286 | 2025-07-23 11:51:00 | TERRA_M-M | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 24.8 |
| fdff7939-8196-319b-b203-7517a51ad51b | -10.62635 | -45.22803 | 2025-07-23 11:51:00 | TERRA_M-M | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 48.5 |
| bc20b58a-9513-388a-8cea-af0dfebdb05a | -9.30692 | -40.6152 | 2025-07-23 11:51:00 | TERRA_M-M | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 9.3 |
| f3073c53-55aa-37a1-a391-32799d50b07f | -8.82776 | -44.51442 | 2025-07-23 11:51:00 | TERRA_M-M | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 566ad7d9-b763-3388-a0b7-9e89068eeddb | -9.0645 | -45.06702 | 2025-07-23 11:51:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 05a1055b-4715-39c8-896f-a75cc61a886c | -6.74057 | -45.46053 | 2025-07-23 11:51:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 46.4 |
| 3459047a-757e-3dbb-816e-7427105777b6 | -8.07433 | -43.1215 | 2025-07-23 11:51:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 10.7 |
| ad9ee756-a340-338f-a8b2-3e5d2ce32f48 | -6.74315 | -45.44708 | 2025-07-23 11:51:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 12b0a09f-5a62-30cb-abde-30d243405988 | -13.31383 | -42.35342 | 2025-07-23 11:51:00 | TERRA_M-M | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 9f241ed4-1de3-3f59-9627-c2984d222200 | -5.79281 | -43.72741 | 2025-07-23 11:51:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| c28c188b-60e6-3a17-b782-270f155201f0 | -12.27257 | -42.45261 | 2025-07-23 11:51:00 | TERRA_M-M | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 02fdd7c5-02bd-38c1-b573-c07cf5fd8065 | -8.07623 | -43.10899 | 2025-07-23 11:51:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| d2f80a76-381a-35c6-a49d-d76e890d62e1 | -6.74006 | -45.4664 | 2025-07-23 11:51:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 24.7 |
| d9e2015b-eb15-3a5f-b4c5-2db0fc79d9f0 | -7.27143 | -44.38514 | 2025-07-23 11:51:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 68db4d1f-0358-35fa-afca-665050c29a31 | -7.28188 | -44.37634 | 2025-07-23 11:51:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 68.8 |
| e83d99fa-afb6-323e-931a-676d35a6289b | -6.90263 | -42.80057 | 2025-07-23 11:51:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.0 |
| 8403c765-23d7-3d82-9319-296b5f0f4c59 | -8.99042 | -41.01078 | 2025-07-23 11:51:00 | TERRA_M-M | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 13.4 |
| 27e38084-3f15-35b1-96b3-b96bc9a59e84 | -10.66853 | -47.24163 | 2025-07-23 11:51:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 19.3 |
| a39bea14-757f-3a6e-9c95-eae54909288c | -6.98544 | -42.79388 | 2025-07-23 11:51:00 | TERRA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 189.0 |
| a7400f4b-e35e-37ab-af06-8bdc10607151 | -8.82528 | -44.5299 | 2025-07-23 11:51:00 | TERRA_M-M | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 16.7 |
| d203853c-e6d7-36a6-8f18-f43a2980be9b | -9.6461 | -40.63377 | 2025-07-23 11:51:00 | TERRA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 7.2 |
| e53a5896-4d19-3e9a-9c3f-ec4f60d6c72f | -10.63801 | -45.23001 | 2025-07-23 11:51:00 | TERRA_M-M | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 1a7a2226-3ac5-3a14-a2c4-b96917ce036f | -6.74354 | -45.441 | 2025-07-23 11:51:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 25.2 |
| 59fca1c4-511b-3bfa-a8ec-877dc5699e08 | -10.62807 | -45.23912 | 2025-07-23 11:51:00 | TERRA_M-M | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 46.8 |
| 537a241e-7789-386f-b269-ab995af11999 | -5.78287 | -43.71922 | 2025-07-23 11:51:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |


[Clique aqui para ver as próximas entradas](README21.md)

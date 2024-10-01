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

## Dados Diários - Página 103

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0c6894fc-3d19-3ba8-97ce-bdd828e359da | -7.927 | -61.55768 | 2024-10-01 05:06:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 17285a6f-8e5f-3670-ad3b-bc077a50f737 | -11.8544 | -62.75046 | 2024-10-01 05:06:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 806982e3-8738-3fe4-83fb-1e010e0a9803 | -11.85302 | -62.75086 | 2024-10-01 05:06:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e41a89dd-977b-3545-afcd-928830b6a56f | -11.85023 | -62.74971 | 2024-10-01 05:06:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d9bedbef-3dd4-3904-a9f8-950660278f17 | -12.27248 | -62.3147 | 2024-10-01 05:06:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1ee5caa2-3dc3-3063-bfb9-2d7474622d0c | -12.85611 | -62.84796 | 2024-10-01 05:06:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 49fc2d0e-ba75-302b-9265-86b6c829e872 | -12.84647 | -62.85411 | 2024-10-01 05:06:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| dd2746f6-2d95-308c-8dd3-f0dedfe64f6c | -12.84578 | -62.85793 | 2024-10-01 05:06:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 950d27d0-2388-305c-a290-cb37bb5a83bc | -12.84029 | -62.81746 | 2024-10-01 05:06:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 081f04ac-e9f8-31e0-af66-9cecfb93ddef | -12.81952 | -62.88487 | 2024-10-01 05:06:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 5ec5dce9-9722-3e6d-9cb0-dff8ac2e59f7 | -12.80934 | -62.88348 | 2024-10-01 05:06:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d1a32886-1e10-3d5a-b95b-f5af9fb11908 | -12.77969 | -62.90594 | 2024-10-01 05:06:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c372703c-fed8-3de3-a6e1-39dad5a18466 | -12.77554 | -62.90517 | 2024-10-01 05:06:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 141b031f-0e79-3fad-8a3e-259ff23f0414 | -12.77276 | -62.89667 | 2024-10-01 05:06:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d9dbef48-0a8c-3d69-9f2d-24ae33f137a8 | -12.77207 | -62.90054 | 2024-10-01 05:06:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 073f4622-5782-3915-9c92-20384ed08542 | -12.77139 | -62.90441 | 2024-10-01 05:06:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 225f667e-d06a-34ab-b5f8-e6f2c7c7d625 | -12.76239 | -62.90675 | 2024-10-01 05:06:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 88650523-5c03-3b4d-92b2-3de70647abcb | -13.00165 | -62.71508 | 2024-10-01 05:06:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2a94e10f-5d25-3fbd-b7e0-82413cc03260 | -12.99757 | -62.71432 | 2024-10-01 05:06:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 78eddb78-37c9-30fd-951d-337e0245145a | -12.9969 | -62.71805 | 2024-10-01 05:06:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4216a635-56a8-36f0-af68-ba52e79c91e6 | -12.98457 | -62.69265 | 2024-10-01 05:06:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2c3942e4-1600-3ea7-bd14-34b4e43a257a | -12.9839 | -62.69639 | 2024-10-01 05:06:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 0d12d99c-a12a-3e01-9007-7a15f0b6c5db | -12.98324 | -62.7001 | 2024-10-01 05:06:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 10.1 |
| beae59ac-2f79-3c40-8c2f-eaff3da69344 | -12.9819 | -62.70757 | 2024-10-01 05:06:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 7c1a13e8-d644-3e01-85dc-2cc54d04d188 | -12.98122 | -62.71131 | 2024-10-01 05:06:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 192b3caf-9fb1-3bb0-823f-3a7e12fe0a58 | -12.97848 | -62.70308 | 2024-10-01 05:06:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 5f282b8d-57c1-3a95-8c1c-6e4e110f0a47 | -12.9199 | -62.68027 | 2024-10-01 05:06:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 8.5 |
| a92a517d-3f7f-37dc-a087-602d4b128b61 | -12.91581 | -62.67952 | 2024-10-01 05:06:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 8.5 |
| ee82b304-a9cf-3976-ab1c-8ad7aa2799c8 | -12.91515 | -62.68325 | 2024-10-01 05:06:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 7.2 |
| db71fdd1-7331-361e-b800-bfe5ccdae7e9 | -12.91041 | -62.68624 | 2024-10-01 05:06:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| de734551-9442-39c3-ab7f-8624fee97b66 | -12.84716 | -62.85027 | 2024-10-01 05:06:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 2f878ffd-b3f8-336c-a173-deface4d86ac | -12.84095 | -62.86101 | 2024-10-01 05:06:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d5cf7d7d-0eff-3542-be5d-14d358da08fc | -12.83681 | -62.86025 | 2024-10-01 05:06:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8721ffba-5780-33fd-89c1-d5387c8d636e | -12.82436 | -62.88177 | 2024-10-01 05:06:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8f2410bb-820c-3379-9b40-e3f686878bc7 | -12.78589 | -62.8951 | 2024-10-01 05:06:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e4817ab3-0acf-3876-b596-2a08c6466e52 | -12.78521 | -62.89897 | 2024-10-01 05:06:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 141457e1-0bb7-3cec-bf69-18f5e862b2ba | -12.78452 | -62.90283 | 2024-10-01 05:06:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 19c9798c-f9fa-308f-b903-6ed994f9fb3f | -12.78106 | -62.8982 | 2024-10-01 05:06:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 78db265d-16bd-3464-97d0-6f048955d774 | -12.77691 | -62.89744 | 2024-10-01 05:06:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 6904eddd-aa5b-3ddc-9bf7-7d840f61a138 | -12.86093 | -62.84488 | 2024-10-01 05:06:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cc3ae5fc-1b93-3b0c-b987-db99f141aed9 | -12.85473 | -62.85561 | 2024-10-01 05:06:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c064c459-8016-33ea-9eb1-8e1d1b96568e | -12.8506 | -62.85486 | 2024-10-01 05:06:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 15e7ae7f-a501-3688-8e67-7c2ed47efcc5 | -12.84785 | -62.84644 | 2024-10-01 05:06:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c4dfeefe-3ffb-3029-a5f4-ba9c422a8b94 | -12.8299 | -62.87483 | 2024-10-01 05:06:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6a4be7ab-79b1-31ed-b413-b29ad449b601 | -12.82576 | -62.87408 | 2024-10-01 05:06:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 58d3cf4b-ae03-3b1d-b367-074091c838f5 | -12.82022 | -62.88102 | 2024-10-01 05:06:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 858a8849-bb01-3875-91c0-818a9fde98b8 | -12.78037 | -62.90207 | 2024-10-01 05:06:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a26f7b9c-1aeb-35ea-80d8-d8f1d95b8459 | -12.77622 | -62.9013 | 2024-10-01 05:06:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1b85ae39-9a2b-353a-a439-2bafe4916c94 | -12.7707 | -62.90827 | 2024-10-01 05:06:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 45d85b44-f77a-3ac6-9d4c-b0f23729e1fa | -12.76861 | -62.8959 | 2024-10-01 05:06:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| afaecddf-3b28-3154-a775-869a8a167546 | -12.75893 | -62.90211 | 2024-10-01 05:06:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3c25a0e2-d82f-35a9-b0aa-4581919d4940 | -12.75824 | -62.90598 | 2024-10-01 05:06:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fbb36070-6626-36e1-a47b-ca45eb64d982 | -12.33555 | -63.717 | 2024-10-01 05:06:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6857fcec-70de-33a3-86dc-d6c5e2ee9802 | -12.33136 | -63.71791 | 2024-10-01 05:06:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4f57253b-f661-351d-b963-a25917f7a016 | -12.33114 | -63.71617 | 2024-10-01 05:06:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 55265a8f-8551-382e-b652-8f2ff1d63d5c | -11.63492 | -64.02229 | 2024-10-01 05:06:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1a5b474c-9f3b-3dba-bb46-89f9c2875eca | -11.57609 | -63.80095 | 2024-10-01 05:06:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d90ecab4-648c-360e-863b-0e3d80526248 | -11.57523 | -63.80559 | 2024-10-01 05:06:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a851668f-79f1-34b8-83b9-e9447bea4b6f | -11.57074 | -63.80474 | 2024-10-01 05:06:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 410dbec8-cffe-3010-beff-fe90d1885bb6 | -11.56988 | -63.80939 | 2024-10-01 05:06:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 102336ce-ba2a-35d7-a8b7-ee3df72f9cce | -11.56903 | -63.81405 | 2024-10-01 05:06:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 03a2d305-c6ac-3182-8a2c-8e3b11da8837 | -11.56817 | -63.8187 | 2024-10-01 05:06:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0271b7e2-c8bd-3430-b89e-9b99fcc6a02e | -11.56367 | -63.81783 | 2024-10-01 05:06:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e0b10763-179c-34ad-996b-0b7948026d4d | -11.56282 | -63.82248 | 2024-10-01 05:06:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 785c7b9e-9b5f-3a53-8599-8dc5721c9423 | -11.56196 | -63.82715 | 2024-10-01 05:06:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 6bc35c6c-14b6-3200-8c6f-ea0eb2cbcb7b | -11.54952 | -63.84401 | 2024-10-01 05:06:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| da72402c-3241-3369-a965-5cd06d5324a7 | -11.54866 | -63.84865 | 2024-10-01 05:06:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d10900b3-97d4-3dde-b722-9825c45ab180 | -11.5394 | -63.71067 | 2024-10-01 05:06:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 290ebffd-ca1a-37a6-9466-070f16e65552 | -10.99349 | -63.93402 | 2024-10-01 05:06:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 18595f3e-067f-300d-a2a6-de044bed6890 | -11.66164 | -64.99915 | 2024-10-01 05:06:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 299d0424-1d27-3c7c-aa9d-ae00a5030562 | -11.65936 | -65.00034 | 2024-10-01 05:06:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 11.5 |
| fd1f1991-9e70-35a9-8536-393c270ccf45 | -8.79215 | -69.02637 | 2024-10-01 05:06:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 083c69cd-5727-3b14-84dd-e3bb9e7477b1 | -10.71216 | -69.41054 | 2024-10-01 05:06:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e88d1e76-e19d-342a-891f-077f42d6fc63 | -10.71137 | -69.40919 | 2024-10-01 05:06:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4bc6bd8f-cddf-3607-8577-90152abc8f4e | -10.71105 | -69.41616 | 2024-10-01 05:06:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 40e2cfce-514d-3542-831b-56b30b390ffa | -10.71023 | -69.41477 | 2024-10-01 05:06:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 93bd9514-80eb-3993-b58d-bdb999aa1e43 | -10.70992 | -69.4219 | 2024-10-01 05:06:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 4.0 |
| edd2b734-d43b-38fe-bc95-463269435ed4 | -10.70907 | -69.42048 | 2024-10-01 05:06:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c7f52f08-f962-3974-956e-24b748d455e6 | -10.70789 | -69.42625 | 2024-10-01 05:06:00 | NOAA-21 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 30e05849-ff3f-3d31-b2d5-97ee8626c911 | -10.7056 | -69.40939 | 2024-10-01 05:06:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bc891b73-c867-3206-af70-ed60209b1f9f | -10.70448 | -69.41508 | 2024-10-01 05:06:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e87e483f-746f-3dae-a26f-b194de4f86e4 | -10.70334 | -69.42085 | 2024-10-01 05:06:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 775bd4bb-d674-3fb2-a160-d15f78c04b20 | -10.70249 | -69.41946 | 2024-10-01 05:06:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 58ce7f74-dd7a-345e-8e9f-4f8e83d4af27 | -10.68397 | -69.38171 | 2024-10-01 05:06:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 4.2 |
| df6e6697-777a-378f-904f-201e1241f2f4 | -10.68333 | -69.38047 | 2024-10-01 05:06:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 2f20ca4e-8921-3c33-b203-6b3956f8c9ef | -10.54405 | -69.30512 | 2024-10-01 05:06:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c4663679-37cb-3352-847f-b2cd0fc2c5c4 | -10.54292 | -69.31075 | 2024-10-01 05:06:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 72715754-1a0f-3d0f-895b-58197a2b14c1 | -10.53756 | -69.30374 | 2024-10-01 05:06:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5839ea4c-dced-335e-827a-24b932a35bf5 | -10.43049 | -69.23592 | 2024-10-01 05:06:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a170d15d-8efa-3494-bb05-55ebbd3a1452 | -10.42954 | -69.23946 | 2024-10-01 05:06:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fcb93b26-825f-3dda-8d81-15666e6a9ad3 | -9.32213 | -66.5461 | 2024-10-01 05:06:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4bc59995-84c9-37de-b449-58c99979d093 | -9.32033 | -66.5432 | 2024-10-01 05:06:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c6bad407-a0c7-3540-bd82-652efcbc61b9 | -9.69976 | -66.85208 | 2024-10-01 05:06:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e44084ae-7ba2-3216-a33e-15e9a00287ca | -9.69764 | -66.85243 | 2024-10-01 05:06:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 16c7198d-2001-3627-9ab9-f341b1ff467f | -9.61486 | -67.16976 | 2024-10-01 05:06:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 96539a59-41bb-331a-a26f-aedaed46d669 | -9.61476 | -67.16856 | 2024-10-01 05:06:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 866722b8-2c9d-387d-8211-b2da60f2eda6 | -9.60984 | -67.16445 | 2024-10-01 05:06:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9d555fed-84b7-34f2-ae34-9b8af763f434 | -9.60977 | -67.16329 | 2024-10-01 05:06:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 20041927-311a-3150-94ca-3a5a31859024 | -9.57476 | -66.64886 | 2024-10-01 05:06:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d9b3afe8-cb6b-390f-b7fe-3ef9e8a48cfe | -9.27378 | -67.6069 | 2024-10-01 05:06:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README104.md)

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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 86efce34-3c4d-3990-b64e-b538c9b3797b | -5.1531 | -41.271 | 2025-11-06 13:50:00 | GOES-19 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 101.7 |
| 08eb105f-28d0-38a6-919c-c3371b58eebc | -5.9229 | -41.354 | 2025-11-06 13:50:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 98.1 |
| a0bb8bc2-44a8-3775-920f-985446bca506 | -5.1533 | -41.2468 | 2025-11-06 13:50:00 | GOES-19 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 123.3 |
| a050d9ec-db82-34ca-8437-fd63e09d0979 | -5.9045 | -41.3072 | 2025-11-06 13:50:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 108.4 |
| 2bc15af6-ae08-34e5-85ef-c5a641c84528 | -5.7589 | -40.81 | 2025-11-06 13:50:00 | GOES-19 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 112.3 |
| 1a387211-cb12-3ea8-9493-def84aa53963 | -5.9231 | -41.3298 | 2025-11-06 13:50:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 118.2 |
| 87e78ff8-410f-325e-9e89-8c798e5b0cf1 | -5.9231 | -41.3298 | 2025-11-06 14:00:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 127.7 |
| ecf73bf6-063c-3877-a49c-a46f9d7d749e | -5.1345 | -41.2482 | 2025-11-06 14:00:00 | GOES-19 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 119.9 |
| 686beda9-2100-3d58-9c02-69f2c190e565 | -5.9229 | -41.354 | 2025-11-06 14:00:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 105.8 |
| 7ad3cda3-54aa-392f-b6f9-8af4c84d0e8a | -5.6243 | -41.113 | 2025-11-06 14:00:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 82.0 |
| a266cc3a-c7f0-39a4-bb0d-19bd020b5d94 | -5.942 | -41.3282 | 2025-11-06 14:00:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 94.5 |
| 75a8760a-c540-3a6e-be52-ccdde4b51e4a | -5.9234 | -41.3056 | 2025-11-06 14:00:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 126.1 |
| d29d9256-ccd7-3052-aca5-7f4515d277d5 | 2.016 | -50.9018 | 2025-11-06 14:00:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 73.7 |
| e69f21ab-32fc-3d01-b5fe-d002612bab77 | -5.9045 | -41.3072 | 2025-11-06 14:00:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 113.3 |
| e5e0f98a-a5c2-3bc5-a27c-abb656a4d161 | -5.9045 | -41.3072 | 2025-11-06 14:10:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 115.3 |
| 8e7f1219-e700-3ddf-8950-7078b4581bc7 | -5.1535 | -41.2226 | 2025-11-06 14:10:00 | GOES-19 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 96.1 |
| acf35c7b-7605-3731-a8e4-3f0d47489ac9 | -7.545 | -39.8419 | 2025-11-06 14:10:00 | GOES-19 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 97.3 |
| 8fad3cdf-4ff1-39b2-9092-1c72f3b6ddce | -5.9231 | -41.3298 | 2025-11-06 14:10:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 131.2 |
| ceafbf92-a9b1-3f6c-aebd-04e6803248df | -5.9234 | -41.3056 | 2025-11-06 14:10:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 134.6 |
| f0e4e601-c1b2-336c-b86b-a15d3b473188 | -5.9229 | -41.354 | 2025-11-06 14:10:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 110.7 |
| 05e375b7-a34d-3a0b-acfa-e3bf39f3e0ae | -5.5304 | -41.0964 | 2025-11-06 14:10:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 83.1 |
| 907ef89c-7fc7-3b90-ac6d-334a61fc9068 | -5.9045 | -41.3072 | 2025-11-06 14:20:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 122.5 |
| 3777e0b2-b1db-36d2-9789-475adfe1e54f | -5.1535 | -41.2226 | 2025-11-06 14:20:00 | GOES-19 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 91.2 |
| 167dac20-ce60-3c01-b15d-56026bcd3b45 | -5.9231 | -41.3298 | 2025-11-06 14:20:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 130.5 |
| be07e9f5-241d-37da-9079-761899574cb5 | -5.5304 | -41.0964 | 2025-11-06 14:20:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 85.2 |
| a2d351d1-d926-36fa-969f-176eb8115369 | -5.6202 | -41.5479 | 2025-11-06 14:20:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 90.4 |
| 35a3d01c-2b93-3f9a-af3e-025a6cfa3126 | -5.9234 | -41.3056 | 2025-11-06 14:20:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 134.7 |
| 3a919486-28ae-33da-a8f7-3a41bb1000c1 | -5.6245 | -41.0887 | 2025-11-06 14:20:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 113.5 |
| 54348041-8d82-386e-a3b0-6a9e3fe02983 | -0.083 | -49.4735 | 2025-11-06 14:30:00 | GOES-19 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 84.5 |
| 0a2e1394-cded-34ba-9bf0-4f02ab896d3d | -5.5112 | -41.1464 | 2025-11-06 14:30:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 113.5 |
| 0926ff44-3fe5-36a6-8230-65d66048fbd0 | -6.4371 | -39.111 | 2025-11-06 14:30:00 | GOES-19 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 91.2 |
| 417b4d6c-76cc-3c52-ad1e-fc5d98c08371 | -5.6243 | -41.113 | 2025-11-06 14:30:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 86.9 |
| f612e260-52da-3ad6-868b-eae196621701 | -5.9231 | -41.3298 | 2025-11-06 14:30:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 134.1 |
| 14bed388-587d-30f0-95ad-b42ae8c4dc6c | -5.9234 | -41.3056 | 2025-11-06 14:30:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 136.4 |
| 803cd8ae-6e88-37ea-a218-119e2050e765 | -6.4368 | -39.1363 | 2025-11-06 14:30:00 | GOES-19 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 87.3 |
| e5e8c7ec-8e5e-3096-9ccb-bc973b86865d | -3.6884 | -41.6289 | 2025-11-06 14:40:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 84.3 |
| 58211fc4-fbf7-34e2-ad9b-1df75a2e3236 | -5.6202 | -41.5479 | 2025-11-06 14:40:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 87.3 |
| 6963fa58-1a2a-3a71-ac59-5b164d215c5c | -30.3278 | -51.927 | 2025-11-06 14:40:00 | GOES-19 | SÃO JERÔNIMO | RIO GRANDE DO SUL | Brasil | 4318408 | 43 | 33 | nan | nan | nan | Pampa | 112.4 |
| 6cdc49e6-c1a6-3712-80c5-a84f1d14d4f9 | -5.9234 | -41.3056 | 2025-11-06 14:40:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 136.9 |
| 6906e432-ed0e-379c-95b9-079cfd3d1393 | -5.9231 | -41.3298 | 2025-11-06 14:40:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 135.8 |
| 73c0cca4-9d36-39c6-9760-5078948db9d9 | -5.5112 | -41.1464 | 2025-11-06 14:40:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 95.0 |



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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 273090a1-e329-3455-892f-396810e89d90 | -12.8044 | -48.16256 | 2025-08-28 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 3562e84a-aca3-325e-9b32-62d9cb01202b | -9.5471 | -65.69041 | 2025-08-28 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5f39f2ce-1d1a-34d4-81c3-72328de0f545 | -13.37484 | -51.76885 | 2025-08-28 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ad59945d-83e8-3a2d-92bf-add8bc04de61 | -12.68979 | -48.18348 | 2025-08-28 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 642e21ce-80c5-3968-88db-0cc41cb2c4d7 | -15.62458 | -52.71093 | 2025-08-28 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dc46e85f-b4b4-39a0-95ff-09acd3154e00 | -10.25224 | -64.49489 | 2025-08-28 04:59:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 83dd5be3-c8b6-3922-8a9d-07755f92ea24 | -9.49438 | -62.38487 | 2025-08-28 04:59:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f286ff87-998b-379d-af82-feae99011442 | -11.80875 | -46.81694 | 2025-08-28 04:59:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b3c85be0-34fa-33b4-a8b8-4c28946dbfe7 | -15.62275 | -52.75233 | 2025-08-28 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fada9919-8026-3409-bc6f-b8cb4c2d1a52 | -13.42787 | -46.9888 | 2025-08-28 04:59:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| eb386099-dbaa-3bda-9dae-b0f1d53c8375 | -11.57185 | -46.40024 | 2025-08-28 04:59:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| af1d0f4e-142c-3943-9e28-b0a298376a08 | -12.82147 | -48.14293 | 2025-08-28 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 860aaab4-b511-3264-8b51-813836dd5bbe | -12.70663 | -48.16537 | 2025-08-28 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c9385b0b-ad86-3380-a9cb-232d7c002358 | -13.10317 | -57.12368 | 2025-08-28 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8f0a7303-992d-305c-b3a1-fba94ce0b8d0 | -13.53621 | -46.88865 | 2025-08-28 04:59:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ceee6a3e-91d6-3c78-86fb-446313a7b5fc | -13.4274 | -46.99273 | 2025-08-28 04:59:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 587f5ded-0edd-3a82-be4e-cf8c24818564 | -13.63831 | -48.23941 | 2025-08-28 04:59:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e3d2b722-cd70-3fad-85b8-1f850bb206ad | -13.46094 | -46.84885 | 2025-08-28 04:59:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3ed24e34-1da3-3402-84bb-96f3e8f2f34e | -10.81484 | -60.77172 | 2025-08-28 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 13.9 |
| bf64c58f-cf4d-3705-99ad-704d84af952f | -9.39237 | -60.52303 | 2025-08-28 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c2fcda33-3769-39e0-b7f4-9d430869418d | -8.57507 | -63.93026 | 2025-08-28 04:59:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e494a4e9-c504-36c2-9aed-c0e3ce055da6 | -13.63131 | -48.21127 | 2025-08-28 04:59:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 288ce3c5-5819-3772-8b82-9e16df8d1cbc | -8.94569 | -65.9474 | 2025-08-28 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5044ef63-cead-328b-b076-806fecc8d5b7 | -14.27475 | -53.06926 | 2025-08-28 04:59:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| da68d229-8d10-30f6-b022-f8416859c208 | -12.78337 | -48.17527 | 2025-08-28 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| dea16953-1d47-3619-88e8-012505ec530f | -13.59746 | -48.21384 | 2025-08-28 04:59:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0cbfed1c-bc86-3d06-bd57-cc2455827fde | -13.08747 | -46.31891 | 2025-08-28 04:59:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f3835474-99f7-3da4-aee5-516e136886e9 | -9.13681 | -65.28813 | 2025-08-28 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 11.7 |
| b550f1b9-6350-3133-be08-97b1177b97d8 | -9.53078 | -62.39642 | 2025-08-28 04:59:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 56670a8a-448f-3db7-b591-27962350d321 | -14.27217 | -53.07565 | 2025-08-28 04:59:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 17417340-d7b5-36ae-a14e-5f75924e3ac1 | -11.57059 | -47.62303 | 2025-08-28 04:59:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0d61286f-4ba4-375c-b1db-63d72fe05b06 | -13.60568 | -48.22639 | 2025-08-28 04:59:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| d7858273-88a1-3091-aeb1-9657b45336e6 | -13.5557 | -46.90448 | 2025-08-28 04:59:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 50408031-c319-3f15-a966-426f6daeff4e | -11.32823 | -43.52164 | 2025-08-28 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5f4b0da2-a60c-31b2-ab7f-91e65261e6af | -13.98835 | -46.3422 | 2025-08-28 04:59:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| d5309738-4d6a-3fab-80bb-d6ad8528cf84 | -12.93972 | -46.34041 | 2025-08-28 04:59:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 478d3a9d-3cc8-3b11-8dc6-89643b18e57a | -10.32458 | -46.78676 | 2025-08-28 04:59:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 10267c38-11f3-39f1-a748-69957e54fe60 | -9.31264 | -57.69265 | 2025-08-28 04:59:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b7c6c88f-1816-3947-a226-90e913f237ab | -11.32633 | -43.53741 | 2025-08-28 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1b6429c3-759c-3051-b6aa-ea042e3c4b39 | -12.81377 | -48.12651 | 2025-08-28 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 3f41ec26-a339-3994-9c62-6aee53ea3ac4 | -13.46028 | -46.98446 | 2025-08-28 04:59:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9e5a9dd2-5c4c-3a00-b7af-bbc7a82ca70a | -14.26697 | -53.0724 | 2025-08-28 04:59:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 158.2 |
| 9e7f8a21-017a-37b0-9f49-d45985a3fc2f | -13.44441 | -46.8526 | 2025-08-28 04:59:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d15a5668-151b-3049-a9f6-f77b91f2573f | -9.48234 | -62.39808 | 2025-08-28 04:59:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0684882d-50aa-3321-a9ee-4223f2e4115a | -11.92939 | -46.70474 | 2025-08-28 04:59:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0ad76be0-c5d4-3d84-a0a0-813513217848 | -11.64269 | -46.38695 | 2025-08-28 04:59:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2213ac6b-0a52-3499-9d17-280ddb52a275 | -13.06374 | -56.92067 | 2025-08-28 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| de519fb4-f735-37c9-b85e-f870cff5e678 | -14.33207 | -51.91371 | 2025-08-28 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7ba452f1-185e-3305-b4ec-b12fd6582eec | -10.88817 | -55.77402 | 2025-08-28 04:59:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8bb4f3a6-896e-3a26-839c-453404d79431 | -9.59669 | -55.37885 | 2025-08-28 04:59:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ab015d4f-4fd6-38e8-83e3-d5ae7a3d8965 | -13.47616 | -46.85305 | 2025-08-28 04:59:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 66932ab2-bfbb-34a1-a082-13e94bb5c3c4 | -12.89307 | -48.11573 | 2025-08-28 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| f6cfa8f2-88a1-3826-97e8-b0eff3598c25 | -15.61226 | -52.73026 | 2025-08-28 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9711dea2-24ad-3bb0-bbf3-964c61e6e596 | -11.80915 | -46.81369 | 2025-08-28 04:59:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3d72e59e-f193-3473-952c-8435e0f4a0eb | -9.08921 | -65.73711 | 2025-08-28 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 4a0ce55e-3842-30f9-8156-c77edc39dcc1 | -10.47128 | -57.955 | 2025-08-28 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2ffe2142-7469-3e38-aadb-a089faa8afa6 | -14.34276 | -53.34558 | 2025-08-28 04:59:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| eb261675-8fdd-33fb-bdc4-7493176f4992 | -10.53868 | -46.70674 | 2025-08-28 04:59:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 785c4cab-d1ba-3b1a-ba9c-31915e8fb86d | -9.55834 | -55.38344 | 2025-08-28 04:59:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 9ea5b134-9279-3d73-b734-f4b6681f528a | -15.62578 | -52.74165 | 2025-08-28 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fe0c1ccf-8c5e-3b7c-bd29-f889ebabf1c5 | -14.36488 | -53.06823 | 2025-08-28 04:59:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ae58dc99-1370-378c-a45d-9a45a3884521 | -8.9409 | -64.15299 | 2025-08-28 04:59:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 86e36fe1-d901-3c59-b963-8bc306649a35 | -11.34913 | -43.53208 | 2025-08-28 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| cc58e7f0-dbd5-38c0-9df4-91e19a049749 | -15.62208 | -52.74107 | 2025-08-28 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| db103e4f-6b70-398e-a33d-55c196f7e2bf | -13.73385 | -51.9072 | 2025-08-28 04:59:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| eb3f65fe-4f76-30f0-b097-a7bf70654bdf | -11.80671 | -46.79089 | 2025-08-28 04:59:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e39c888b-3a2c-3e84-9c1a-167462761371 | -9.45961 | -60.30656 | 2025-08-28 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 659102e1-1a6e-393e-837b-9b3049d32157 | -9.2462 | -64.41147 | 2025-08-28 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.3 |
| e531ddc5-46fb-38d3-a842-dae42f994a95 | -14.34626 | -53.34529 | 2025-08-28 04:59:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ddeab320-93e1-3a57-aa57-8e85abd34ffc | -8.92676 | -65.93216 | 2025-08-28 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 415defec-9f70-3b32-818f-284401cdcfde | -14.264 | -53.0676 | 2025-08-28 04:59:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 53de47cd-6f60-384f-97d1-801748d1a00f | -10.59411 | -54.89209 | 2025-08-28 04:59:00 | NOAA-21 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5ab226d6-d63d-39b5-a455-9871c505bf8a | -13.38909 | -46.86756 | 2025-08-28 04:59:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 067d19ab-e8cf-33fb-a7d7-3b9ea56caf6b | -13.97616 | -46.35134 | 2025-08-28 04:59:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| accc87bc-1244-3fb0-9cc3-435e9f4c91a2 | -8.60843 | -64.07579 | 2025-08-28 04:59:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0408ccd1-73e9-34af-9079-ee00a4b295ea | -9.40194 | -60.51693 | 2025-08-28 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5d37adb9-502f-38e3-af07-fb6c3ad5da4a | -10.4748 | -57.95557 | 2025-08-28 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 18e934c5-afe5-3fcd-a531-aadfd78f6075 | -12.78327 | -48.17434 | 2025-08-28 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fe41b0c1-fd81-3451-b684-599a0317dcf3 | -13.55084 | -46.90042 | 2025-08-28 04:59:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 04cf4356-9efa-3a6d-9eed-530a30df2785 | -8.89022 | -60.75516 | 2025-08-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c2eae4e3-bc93-356f-98f4-80089ea60bdb | -9.11361 | -67.70764 | 2025-08-28 04:59:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| acf9bae3-71d3-3b96-b387-939675ee2881 | -8.60783 | -64.07912 | 2025-08-28 04:59:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7a1e4d54-7b1e-3071-af99-b5191fd10db3 | -8.90864 | -62.47871 | 2025-08-28 04:59:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cfea2e7b-cba4-3ba6-84e7-577b91b96aad | -9.11607 | -65.78019 | 2025-08-28 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 34.3 |
| 7d1d7ea9-cb2e-37e5-8c93-5c8f14b5a8eb | -10.46231 | -57.96575 | 2025-08-28 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 67eb5edc-cad9-35e3-a6f3-70e80cef89cf | -12.68505 | -48.18258 | 2025-08-28 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 245adbb8-f851-3f58-9cda-ec76b587bbc8 | -14.59711 | -54.51112 | 2025-08-28 04:59:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fe24902f-fa34-3c9c-a415-3a90995e14ef | -11.22521 | -55.05386 | 2025-08-28 04:59:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 1a42c8b3-3104-355b-8286-342b29b814c3 | -14.27896 | -53.06553 | 2025-08-28 04:59:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 33.2 |
| e4f486d1-1c26-30d5-8471-82efdca0b8ea | -10.61619 | -54.90276 | 2025-08-28 04:59:00 | NOAA-21 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4e40e4e5-7a2d-313c-9617-f3da4a671f76 | -10.47331 | -57.94636 | 2025-08-28 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 61b077fa-1a5a-3807-a5d7-3ba94a849c74 | -12.6906 | -45.08411 | 2025-08-28 04:59:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a3537102-cf18-3209-96f8-505870f64597 | -10.81203 | -46.36448 | 2025-08-28 04:59:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5cd8d94e-ca59-3a6a-bc3d-12a871a9d74f | -9.4023 | -60.56345 | 2025-08-28 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a7f62dac-d2d9-358f-a6f8-c09b2ba89c46 | -8.9415 | -64.14964 | 2025-08-28 04:59:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ede939a0-a72a-3000-948a-4cab224629bc | -11.93422 | -46.70864 | 2025-08-28 04:59:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 49db11a3-fc8c-34ef-8e14-b66d54b822fc | -13.46549 | -46.99076 | 2025-08-28 04:59:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fec45ebc-0382-33dc-b878-52b2649a7de9 | -13.63147 | -48.21636 | 2025-08-28 04:59:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ebd12030-d3d7-3b0f-bbf3-06d3709a4bb0 | -15.08957 | -48.51247 | 2025-08-28 04:59:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 7dc2698a-4657-3dcb-94ca-e1eb89c9eeec | -8.95079 | -65.9529 | 2025-08-28 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |


[Clique aqui para ver as próximas entradas](README58.md)

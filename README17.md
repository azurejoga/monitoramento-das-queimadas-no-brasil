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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 70c099c0-bce4-3e12-8c64-61f4d6b73473 | -12.79392 | -46.38385 | 2025-11-15 03:38:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c8a6d40b-5151-309a-aa0f-b634039b3f81 | -12.92608 | -43.0914 | 2025-11-15 03:38:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 3cffdcfb-da7a-3a55-8bce-11551ae565df | -17.29568 | -46.82602 | 2025-11-15 03:38:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 61e7f160-a394-35aa-8913-d748591062a9 | -13.54986 | -43.72597 | 2025-11-15 03:38:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 747accd2-57c5-32c8-ae71-28b8edf479ab | -12.92391 | -43.08955 | 2025-11-15 03:38:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b1b57b0b-abcd-36f6-a81f-5dc9613aa613 | -18.33522 | -47.19023 | 2025-11-15 03:38:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 77816b5e-81b5-304c-b839-1a640c811561 | -12.76151 | -43.6536 | 2025-11-15 03:38:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 59453324-8b07-3417-8c3e-8ee38aea1cb4 | -13.1097 | -43.70174 | 2025-11-15 03:38:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 235670cc-b564-3334-ae3d-c91d2ec7508b | -11.80263 | -48.08117 | 2025-11-15 03:38:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d812eaf6-ff1e-3602-badf-856bc5026d67 | -11.71442 | -44.44373 | 2025-11-15 03:38:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2b56e616-3d5c-3313-ab08-d9b937dd39f1 | -12.90868 | -45.10479 | 2025-11-15 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cd149e58-9ee7-32fe-b436-cb5c1b4c4c95 | -13.73871 | -43.62945 | 2025-11-15 03:38:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 514f2b26-1d8b-3bb8-b433-e77238cded88 | -12.48121 | -43.73334 | 2025-11-15 03:38:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 6823c86e-738c-39d7-b07a-ae67f1a76902 | -11.71373 | -44.44733 | 2025-11-15 03:38:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bc29ee5c-7755-3fa1-9b60-c8500fd625ea | -13.54879 | -43.72575 | 2025-11-15 03:38:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1a4c578b-7e2b-396d-bb28-15f5eb43ed99 | -12.38428 | -48.10985 | 2025-11-15 03:38:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ca1cf08b-de0c-32b2-84c1-31c45135a335 | -12.97407 | -48.84173 | 2025-11-15 03:38:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a28b9c05-7e1f-36b8-aa00-0e69bdcbe273 | -12.6756 | -46.77286 | 2025-11-15 03:38:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 96ae8e10-094e-3ff4-bfca-c40907752f76 | -12.77621 | -46.95501 | 2025-11-15 03:38:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 49208589-5424-310a-acb9-bd4ce0d8c95e | -12.41814 | -48.11552 | 2025-11-15 03:38:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a4a07ee6-51c3-3988-8613-c664457b66f2 | -12.65139 | -43.25055 | 2025-11-15 03:38:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 01b75391-28b6-3c5d-88de-820eace7d2ac | -14.98792 | -42.41453 | 2025-11-15 03:38:00 | NOAA-21 | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 2a8bdc66-0e79-340f-9768-a719ba04d476 | -12.02654 | -43.72735 | 2025-11-15 03:38:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6aec1a9d-3afb-30eb-8f58-0f4ebf39ccd9 | -14.68621 | -46.61732 | 2025-11-15 03:38:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1531d148-1591-3110-9ea8-f19ac7b65dca | -14.94996 | -47.51179 | 2025-11-15 03:38:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 090c5324-92c5-3777-81a5-5e6c72d91652 | -12.68379 | -46.76432 | 2025-11-15 03:38:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 62341e47-3e8d-3a44-a68c-4bb3716e4215 | -11.79583 | -48.07991 | 2025-11-15 03:38:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5f2920cf-0f8d-3a57-bb0a-9a341684ebde | -12.43897 | -47.88288 | 2025-11-15 03:38:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1548a91c-03ae-3440-9d2a-7a085c30b2aa | -12.36602 | -43.70156 | 2025-11-15 03:38:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| af29f74c-2f87-390b-b5d9-d5700f24981d | -14.6881 | -46.60814 | 2025-11-15 03:38:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4281475e-4ece-322b-9ea3-c2894b27f211 | -12.36661 | -43.69843 | 2025-11-15 03:38:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 32d65896-555c-3229-9cb2-e75e6bdd216c | -12.46519 | -43.7516 | 2025-11-15 03:38:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 39cf14d9-81af-334e-8a04-6931864df921 | -5.2397 | -44.3448 | 2025-11-15 03:40:00 | GOES-19 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 80.0 |
| a1f0609b-bdd8-3a3f-a02e-7092633eeb1d | -2.5238 | -47.8115 | 2025-11-15 03:40:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 0eb11eb4-a4c1-3223-bded-3a42a2e1f607 | -4.538 | -43.2341 | 2025-11-15 03:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 52.7 |
| 96a217f7-2a06-3eca-b626-e3e34e3330b1 | -4.7342 | -47.1547 | 2025-11-15 03:40:00 | GOES-19 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 56.0 |
| e6b41fa3-5ec2-35e0-bf0f-92025fb2d333 | -4.5381 | -43.2107 | 2025-11-15 03:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 62.2 |
| edd99fb8-b984-3da1-8558-bbdd7fa9841c | -11.8486 | -49.2218 | 2025-11-15 03:40:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 130.2 |
| 367e7cf7-322e-333f-989e-36e86579cb51 | -11.849 | -49.2 | 2025-11-15 03:40:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 107.2 |
| 6172f8ac-7f4f-3fb8-b1b6-a49a24500225 | -18.48699 | -47.51999 | 2025-11-15 03:40:00 | NOAA-21 | DOURADOQUARA | MINAS GERAIS | Brasil | 3123502 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6b41a615-f7ba-36e6-9048-947d59d15689 | -19.51144 | -45.87067 | 2025-11-15 03:40:00 | NOAA-21 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0b9751fd-c71d-39ff-a7ed-f23e015490e0 | -18.48798 | -47.51545 | 2025-11-15 03:40:00 | NOAA-21 | DOURADOQUARA | MINAS GERAIS | Brasil | 3123502 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f782e111-7d8e-3c38-af7d-7e22c5ca6040 | -19.08259 | -46.65137 | 2025-11-15 03:40:00 | NOAA-21 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ddedc8da-3d37-3dfe-be66-011707bbee41 | -19.08181 | -46.65495 | 2025-11-15 03:40:00 | NOAA-21 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a33b270b-1ed1-3be9-9494-9098947b5294 | -19.19638 | -47.87088 | 2025-11-15 03:40:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b86df611-0853-373d-a3e1-27d653fab172 | -19.19535 | -47.87555 | 2025-11-15 03:40:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c8639376-fd5a-3aad-b1b9-35f0a8e6c342 | -11.8486 | -49.2218 | 2025-11-15 03:50:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 99.3 |
| fc352758-2bb8-347e-a410-91a27d440b9c | -5.2397 | -44.3448 | 2025-11-15 03:50:00 | GOES-19 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 9a3e43f6-2c5a-3ff5-98ae-a7fd774f8d71 | -12.6745 | -46.7605 | 2025-11-15 03:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 650894dc-b887-30ad-afec-24ea47b0281c | -4.5568 | -43.2096 | 2025-11-15 03:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 51.5 |
| 4baca4d2-c6df-3476-93d7-00c611b3bb19 | -4.5381 | -43.2107 | 2025-11-15 03:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 154d0df9-41a5-3ae9-8e6c-7a4c5da30325 | -11.849 | -49.2 | 2025-11-15 03:50:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 4c9384a1-b36c-31d8-bc1b-7393e4eb8671 | -4.5381 | -43.2107 | 2025-11-15 04:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 56.4 |
| c12ffa5c-0ba3-3d63-93ce-745aaae14b4a | -2.5238 | -47.8115 | 2025-11-15 04:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| a97c8e1f-fcd6-3c5a-9510-1b7a6dd35e23 | -11.849 | -49.2 | 2025-11-15 04:00:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 77da14c8-b101-3125-9331-8431d12f89af | -5.2397 | -44.3448 | 2025-11-15 04:00:00 | GOES-19 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 10d24151-2a93-3004-a605-0cfd07604b66 | -11.8486 | -49.2218 | 2025-11-15 04:00:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 125.2 |
| c5fa1572-c4ad-3d5c-b984-1ef85173b410 | -4.7342 | -47.1547 | 2025-11-15 04:00:00 | GOES-19 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 3d700c05-bf08-3ee9-8c70-b95eb578c4b2 | 2.33743 | -51.65161 | 2025-11-15 04:01:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 79296ccc-f588-3663-b2af-395456b0e6b9 | -7.45769 | -42.76254 | 2025-11-15 04:04:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 891efd8a-1bfc-34a9-88f6-297317df92cf | -5.06131 | -42.71959 | 2025-11-15 04:04:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f2977f13-4ba6-3de0-8eef-5b1ae412b0e0 | -4.04765 | -48.09774 | 2025-11-15 04:04:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dd13d41c-1d9a-350c-aeed-235a879ca73d | -1.50039 | -47.80472 | 2025-11-15 04:04:00 | NPP-375D | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0111d108-fbd2-3567-abeb-de46342e44a8 | -5.31224 | -47.28843 | 2025-11-15 04:04:00 | NPP-375D | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 28e414e4-848b-3f39-b781-d2b1ede96b73 | -5.3787 | -45.36756 | 2025-11-15 04:04:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b662f03a-cc67-338f-9a9b-e79d9e743f85 | -5.60764 | -45.18605 | 2025-11-15 04:04:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ab60280f-1f92-357a-837d-a2469a97cb7a | -7.17405 | -38.45384 | 2025-11-15 04:04:00 | NPP-375D | SÃO JOSÉ DE PIRANHAS | PARAÍBA | Brasil | 2514503 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| fdaeedde-26e0-3d63-9815-9cd5e336f1e5 | -6.46212 | -45.6542 | 2025-11-15 04:04:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 30e44e90-2367-3df5-80f3-702de34ba43e | -3.05468 | -47.11408 | 2025-11-15 04:04:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d52ab378-3cbd-3b10-84c2-fee48a65b001 | -6.14963 | -48.04681 | 2025-11-15 04:04:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| a25e162d-4a29-368e-8cb1-f541a9d2a012 | -4.3492 | -46.49186 | 2025-11-15 04:04:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d7d14781-f97a-386c-b2b5-7af65fc5428d | -5.0511 | -44.68177 | 2025-11-15 04:04:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 13f7f854-4fb5-3b2e-8d0a-520fec1f7956 | -5.42991 | -40.66623 | 2025-11-15 04:04:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 8453fb5e-9858-38a1-a95b-fa5773aaa31e | -5.62731 | -43.92664 | 2025-11-15 04:04:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 339ebdaf-4b0b-3e84-a73e-aacd298bb1c0 | -5.09632 | -41.47805 | 2025-11-15 04:04:00 | NPP-375D | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a43cb0d4-d82c-38e1-b8d3-7de642427daf | -5.47204 | -41.40054 | 2025-11-15 04:04:00 | NPP-375D | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 1e187fc0-ab5f-3f25-a92e-a938b8ed56c9 | -7.49106 | -42.55612 | 2025-11-15 04:04:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 9e422d87-e745-37de-bdfd-e392fe6530d6 | -7.74941 | -36.95375 | 2025-11-15 04:04:00 | NPP-375D | SUMÉ | PARAÍBA | Brasil | 2516300 | 25 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 06cd39e7-2bc9-354e-b7e2-dda28b980dbe | -5.1636 | -44.8515 | 2025-11-15 04:04:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ad23b5f0-1a3a-33f1-9188-f9df87409a12 | -4.19083 | -45.45224 | 2025-11-15 04:04:00 | NPP-375D | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 77b2ca77-2f13-39e5-9f36-8368cb2ac693 | -4.8124 | -41.61682 | 2025-11-15 04:04:00 | NPP-375D | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 90c83d59-b4c3-3db5-9c86-82f45f4f642f | -7.67539 | -42.64443 | 2025-11-15 04:04:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 09315c3f-12ca-329b-8325-40c5405a478e | -4.80895 | -41.61628 | 2025-11-15 04:04:00 | NPP-375D | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 98f6426a-636a-38ce-b12a-d0f927caec6d | -4.00043 | -44.17451 | 2025-11-15 04:04:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e6bce1c3-4a93-37c3-ac0f-208d7219657a | -6.64269 | -46.54236 | 2025-11-15 04:04:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5dd47cd1-54c4-31b7-a61e-b6eeea6a8042 | -7.1011 | -42.73598 | 2025-11-15 04:04:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| c4bc82df-1df0-3c58-9989-c736f68a5b9a | -4.64559 | -47.95197 | 2025-11-15 04:04:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3a36aa69-5d26-3e93-ac16-2ab83c33f05c | -5.76204 | -40.13533 | 2025-11-15 04:04:00 | NPP-375D | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a1885f6f-d6a4-3c66-87a4-60c766a6358d | -4.74893 | -41.57193 | 2025-11-15 04:04:00 | NPP-375D | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 5c480316-1678-32df-9173-9315e2959f76 | -4.0427 | -46.52279 | 2025-11-15 04:04:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f6c0695a-ac95-3f4c-a61d-9d94e14b60f8 | -5.52067 | -41.77323 | 2025-11-15 04:04:00 | NPP-375D | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 293627f1-17f1-340d-a65a-b3f097892f48 | -6.6037 | -50.06781 | 2025-11-15 04:04:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2b7296fd-8fbd-358a-b841-d679389f94a9 | -7.43871 | -42.76844 | 2025-11-15 04:04:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 75ff9ae8-1d7c-3aaa-bda4-0686cd7884c6 | -6.24139 | -46.39104 | 2025-11-15 04:04:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f9c4a360-69fd-34a9-9291-9d105bd8003f | -4.68569 | -45.85617 | 2025-11-15 04:04:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0383d8a1-48f6-3a17-a0e4-15999219079a | -4.70459 | -40.12413 | 2025-11-15 04:04:00 | NPP-375D | CATUNDA | CEARÁ | Brasil | 2303659 | 23 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 562e3177-9799-3006-b3ba-919246c31b9b | -2.74313 | -45.29471 | 2025-11-15 04:04:00 | NPP-375D | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 88a9009e-ba47-345d-a4a7-43f24d3db619 | -4.33511 | -47.57313 | 2025-11-15 04:04:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 6cb82390-24ba-380c-acd5-34376fb5a7d0 | -2.7323 | -45.30582 | 2025-11-15 04:04:00 | NPP-375D | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 00efc5b7-4a43-31f8-b204-3bddc34546a5 | -6.07968 | -41.62047 | 2025-11-15 04:04:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |


[Clique aqui para ver as próximas entradas](README18.md)

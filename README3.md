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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 60a7c64d-9f6a-3284-833f-40a3f12e874d | -5.17954 | -35.8605 | 2026-05-23 03:45:00 | NOAA-20 | PEDRA GRANDE | RIO GRANDE DO NORTE | Brasil | 2409506 | 24 | 33 | nan | nan | nan | Caatinga | 2.0 |
| b70a0480-8ab2-357f-b2d4-b41a1eb94006 | -4.47631 | -37.81345 | 2026-05-23 03:45:00 | NOAA-20 | FORTIM | CEARÁ | Brasil | 2304459 | 23 | 33 | nan | nan | nan | Caatinga | 5.0 |
| d75be53a-b615-34ac-8e3f-7ff8e193760c | -10.48211 | -42.41061 | 2026-05-23 03:47:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| d9291d81-2549-3805-9c1d-4bf70cd2e8c9 | -9.28963 | -45.48994 | 2026-05-23 03:47:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 088429c9-e253-3258-ac39-038481dc1533 | -9.29988 | -45.4958 | 2026-05-23 03:47:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8f811387-bc4f-3adf-b980-4bd5f8549e07 | -9.2992 | -45.4994 | 2026-05-23 03:47:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 5e105a7d-6902-36ae-8200-af6ea890f84c | -10.48133 | -42.4149 | 2026-05-23 03:47:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 3a6f33ba-22e4-32c9-ad6a-8fac15cf04d6 | -10.48288 | -42.40632 | 2026-05-23 03:47:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| f6ba448f-875d-3d35-bab0-6c6c76c90e7d | -10.48648 | -42.41142 | 2026-05-23 03:47:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 9b55b398-2b8c-3727-87db-ecf697ba3e30 | -20.3724 | -41.91003 | 2026-05-23 03:47:00 | NOAA-20 | MANHUMIRIM | MINAS GERAIS | Brasil | 3139508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| e476add5-2e4d-372b-9f9c-60f3acc639a4 | -9.29442 | -45.49466 | 2026-05-23 03:47:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e6e8bdaf-3991-325d-803d-511e0d8a14ee | -21.51897 | -48.62205 | 2026-05-23 03:49:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 768dc1a9-d205-3b41-bb67-0d0c5877a50e | -21.51664 | -48.6209 | 2026-05-23 03:49:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ed6af937-e4e0-3f31-be61-dd89f8b333d0 | -21.52192 | -48.62226 | 2026-05-23 03:49:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 613c2b2e-6351-3cf3-b4d5-be2df9b6e6db | -11.1903 | -55.9101 | 2026-05-23 04:20:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 55.8 |
| f021a954-524a-337f-bf99-8b7dd6e4a35b | -11.1903 | -55.9101 | 2026-05-23 04:30:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 9fb87fc7-b6bc-35e8-917f-9f30ac96934e | -4.65933 | -42.43575 | 2026-05-23 04:32:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 0039858d-2e99-3425-9719-073b976c096f | -5.95624 | -43.48668 | 2026-05-23 04:32:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 095c8637-5c53-33e8-8a71-a248d8e9d793 | -5.95243 | -43.48611 | 2026-05-23 04:32:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e4fce763-d98f-3289-92d3-595f7789d99f | -4.47595 | -37.81092 | 2026-05-23 04:32:00 | NOAA-21 | FORTIM | CEARÁ | Brasil | 2304459 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 64cbc20b-a0fe-3b5a-a05b-392c339a5fd4 | -4.47707 | -37.80965 | 2026-05-23 04:32:00 | NOAA-21 | FORTIM | CEARÁ | Brasil | 2304459 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2250ec8b-e70f-3267-a33e-a3c879b5a5a3 | -4.6588 | -42.43921 | 2026-05-23 04:32:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 7bb257f6-fde1-318f-b33b-29957d7bc49c | -5.95556 | -43.49134 | 2026-05-23 04:32:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 77b47d41-40bc-32e1-8638-05f11ca22fe6 | -5.11838 | -42.60635 | 2026-05-23 04:32:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| efab8555-e711-32fa-a275-08ce0683f197 | -5.77919 | -45.13287 | 2026-05-23 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 033c4993-6a2f-37fb-ac83-141852305033 | -5.95175 | -43.49077 | 2026-05-23 04:32:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 8c8a67b2-1038-30ad-9cd7-1f7cf596309e | -4.47543 | -37.8145 | 2026-05-23 04:32:00 | NOAA-21 | FORTIM | CEARÁ | Brasil | 2304459 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 59e6bf92-adeb-313e-95ae-09a016ff58e8 | -5.77629 | -45.12846 | 2026-05-23 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 69f322c8-732f-36e8-996e-976357427bcb | -4.47657 | -37.81324 | 2026-05-23 04:32:00 | NOAA-21 | FORTIM | CEARÁ | Brasil | 2304459 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 782baab4-b8db-3d32-839b-779d080f4bdb | -4.47608 | -37.8168 | 2026-05-23 04:32:00 | NOAA-21 | FORTIM | CEARÁ | Brasil | 2304459 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 471970d4-86d2-3543-ab32-773be1fcd4a4 | -4.4749 | -37.81805 | 2026-05-23 04:32:00 | NOAA-21 | FORTIM | CEARÁ | Brasil | 2304459 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| b4eed5ba-3293-3417-91cc-d85c64b1cea8 | -5.35212 | -45.18826 | 2026-05-23 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 3a9e61e4-068b-339c-b1a4-42900e6678ed | -11.92692 | -43.87309 | 2026-05-23 04:34:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 03f54999-2b1c-388c-9a0f-fe741eda54b3 | -11.5488 | -56.94192 | 2026-05-23 04:34:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| da4ff38f-1f34-3127-9cdb-36833a593302 | -11.50555 | -45.05877 | 2026-05-23 04:34:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2c902f6d-d910-3833-9f16-fa045a1c5713 | -11.30929 | -47.55872 | 2026-05-23 04:34:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7480d659-791f-30e9-be1d-3ddb1889dc5b | -9.06639 | -44.76736 | 2026-05-23 04:34:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bc82165d-630e-30c4-85f2-2773093e0ce8 | -9.95442 | -52.4272 | 2026-05-23 04:34:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 94bb70e4-88cd-3461-8aa5-f941b09efc5a | -7.64439 | -45.30366 | 2026-05-23 04:34:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 27fbde2e-09a0-30d8-a5ca-75613afefac8 | -11.75036 | -47.74443 | 2026-05-23 04:34:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1096ae99-ef4d-3c7b-b5e6-17edadd62844 | -11.05563 | -46.69933 | 2026-05-23 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 493aa319-9614-32c8-8913-d567b91a8554 | -9.29193 | -45.49149 | 2026-05-23 04:34:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 93f50a3b-614b-336f-9527-f6a3867e0106 | -6.03906 | -46.75194 | 2026-05-23 04:34:00 | NOAA-21 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d49d9cd0-95c7-3bf4-8f64-7967e284538f | -11.44321 | -52.92323 | 2026-05-23 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| fc0781e4-33c2-3442-91fd-1e65f33c28bb | -9.2194 | -48.59039 | 2026-05-23 04:34:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5ac0b276-1c6e-3106-a989-ee3377357544 | -11.9274 | -43.86949 | 2026-05-23 04:34:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 43a758c7-9cc8-33f0-8e4b-48be400901d7 | -11.054 | -46.80375 | 2026-05-23 04:34:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ea40bfad-3256-38db-ab02-3028825481d4 | -11.5122 | -56.12087 | 2026-05-23 04:34:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 427e4996-a953-32eb-afee-c09ad4c121a9 | -11.18105 | -55.91478 | 2026-05-23 04:34:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 14.4 |
| e68900d3-09cc-3d73-a84a-758e7948fb6d | -11.44618 | -52.92849 | 2026-05-23 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| dd033f50-5bfa-390f-9982-6ed2130b53a9 | -10.47914 | -42.41729 | 2026-05-23 04:34:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 4.6 |
| b487872c-d04a-37d5-ab20-d96d2fc93be8 | -7.3008 | -47.05882 | 2026-05-23 04:34:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6d900f8a-dcb1-3dff-b6b8-e1c0ce7b90f9 | -12.29955 | -47.91135 | 2026-05-23 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| efea8406-34e0-32f8-a105-2f6309b78140 | -10.60664 | -44.33707 | 2026-05-23 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f8fa2772-3a85-36b4-be31-76667be3d63d | -9.46001 | -47.05248 | 2026-05-23 04:34:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 66d5507f-ab8c-3c9f-a9c3-082286b215f2 | -11.5585 | -56.94389 | 2026-05-23 04:34:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a32f96d4-bfd3-3d9d-b560-9b79c754a454 | -12.3089 | -47.84988 | 2026-05-23 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3e0202ac-933c-3b92-b4a2-7f2c6b4db712 | -9.14311 | -51.28513 | 2026-05-23 04:34:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 48b27d62-b08d-3c68-aea8-6597089b8917 | -6.75024 | -47.12322 | 2026-05-23 04:34:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| da1fbbc9-e8e3-37a3-a348-9000c34936e1 | -11.0289 | -46.8077 | 2026-05-23 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dfe119dd-dde4-3c17-9a3b-4f416743237b | -11.55898 | -56.32542 | 2026-05-23 04:34:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d66082e7-a2d2-3c93-90b2-b7b8d6bb3dd0 | -10.70905 | -56.24287 | 2026-05-23 04:34:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0e690996-c5b8-3612-9646-f777b02ca0b3 | -8.59551 | -45.94728 | 2026-05-23 04:34:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b0a1deae-30dc-3e5b-9fe8-ca6087f8bf29 | -12.31225 | -47.85042 | 2026-05-23 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9324b350-a440-374a-ad2e-f6fcce2f5720 | -6.21939 | -46.88326 | 2026-05-23 04:34:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7913c74a-01c8-3137-8db2-99268d117e09 | -8.73582 | -50.24002 | 2026-05-23 04:34:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 738c9f7e-f3c7-351a-8b19-9c5b5dec9a1a | -10.65314 | -49.72529 | 2026-05-23 04:34:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fefc4d92-9c52-3ca9-b19a-19585f23c25a | -11.56938 | -54.53246 | 2026-05-23 04:34:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e21ec6cc-0712-33ae-b37d-1acd0022d04e | -9.29254 | -45.48741 | 2026-05-23 04:34:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8558706d-9974-34a4-bc6c-fff396e6fafd | -11.0665 | -46.69717 | 2026-05-23 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 63260b30-c684-390e-8961-8461e717778c | -7.00787 | -45.008 | 2026-05-23 04:34:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 017636ba-0144-35fd-a1ef-0779a7e336a4 | -10.47972 | -42.41303 | 2026-05-23 04:34:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 57e7335d-a14d-3442-b358-5c8afb58addd | -11.05572 | -46.83884 | 2026-05-23 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| acfb3e91-bef0-355c-98dd-38605b464bc7 | -10.48902 | -42.41004 | 2026-05-23 04:34:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 95000cd7-b20c-31e8-9b01-92e9b809f831 | -11.44697 | -52.92387 | 2026-05-23 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 89f4324d-8f53-3a27-9c09-602e3cb4e9b5 | -11.55216 | -56.9402 | 2026-05-23 04:34:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 66d79914-b530-38fb-994b-7a94ffbe87a3 | -7.87926 | -46.90179 | 2026-05-23 04:34:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7269accc-76ab-3bec-907c-d3fb18a0c22b | -11.05458 | -46.84637 | 2026-05-23 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 66465342-696f-3083-abdc-c69990151854 | -11.51131 | -56.1257 | 2026-05-23 04:34:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 17ccd628-e0f3-33b3-9c60-02fb292a5f45 | -10.64924 | -49.72831 | 2026-05-23 04:34:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 2b96ca09-9b22-3560-9e86-debdd474a1ff | -11.18562 | -55.91559 | 2026-05-23 04:34:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 5ca85358-844c-32ed-a0bf-262bbbbb667f | -6.39433 | -44.16759 | 2026-05-23 04:34:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 039c1f43-91fd-372a-8cd2-fd2e567af441 | -9.10962 | -50.53521 | 2026-05-23 04:34:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f0cf6f3e-40e3-3daa-ad8e-874122aa19e8 | -11.61083 | -55.33008 | 2026-05-23 04:34:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4fa43770-fcd3-38d1-b332-75958c0ae2c8 | -11.71222 | -54.63025 | 2026-05-23 04:34:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3d8283d8-4d80-3d7e-b1fe-713cac8ee8d7 | -11.34864 | -51.41181 | 2026-05-23 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6c87d553-e101-3f60-9519-729f38515dc1 | -9.29549 | -45.49201 | 2026-05-23 04:34:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e157d521-439b-320d-a3a7-a9def241dbc7 | -9.302 | -45.49714 | 2026-05-23 04:34:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 4795589a-c3eb-366a-931c-2151a4881793 | -11.5511 | -56.94577 | 2026-05-23 04:34:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 85b96254-182d-3e76-b3f4-91b78ba89557 | -11.07795 | -46.69117 | 2026-05-23 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d9d00ff7-d37d-3eb6-8750-6433d9c59165 | -11.55595 | -56.94675 | 2026-05-23 04:34:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 02324095-0f06-3039-9363-200f47a906f2 | -10.48467 | -42.40941 | 2026-05-23 04:34:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 932716b2-eb3e-3820-b98e-ec4cbac6ae76 | -10.22612 | -52.66572 | 2026-05-23 04:34:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3dd8054c-8cdd-3f83-bff3-4fc56bf1877d | -10.79891 | -49.40771 | 2026-05-23 04:34:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d75f8d09-c16e-33f3-847f-d58978ffdcb3 | -6.64409 | -43.91734 | 2026-05-23 04:34:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 41fa3ef3-ddf2-37e9-9013-5db142c25187 | -6.81617 | -44.14534 | 2026-05-23 04:34:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 256fed9a-0ba5-3ff6-bcba-0f94bd287517 | -10.01858 | -48.54768 | 2026-05-23 04:34:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e472aac0-2178-3992-aeac-6f70e5521dcc | -11.45149 | -55.11312 | 2026-05-23 04:34:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f027be2d-8275-3e9f-9025-d4c07a8fc08b | -8.59897 | -45.94781 | 2026-05-23 04:34:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4243728d-de5e-3874-9090-27e67bdc9ae1 | -6.03852 | -46.75541 | 2026-05-23 04:34:00 | NOAA-21 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README4.md)

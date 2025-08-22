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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 427738a9-c15c-31c1-b261-8658edef6d8b | -21.24072 | -44.58811 | 2025-08-22 04:23:00 | NOAA-20 | NAZARENO | MINAS GERAIS | Brasil | 3144508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| b06678a4-3bbe-3ac8-a8d5-09b49f14f0b3 | -23.24244 | -46.59221 | 2025-08-22 04:23:00 | NOAA-20 | MAIRIPORÃ | SÃO PAULO | Brasil | 3528502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 138c00ec-d67d-3a48-ae2b-7cbd0ff00daf | -23.20824 | -44.90187 | 2025-08-22 04:23:00 | NOAA-20 | UBATUBA | SÃO PAULO | Brasil | 3555406 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| d744b141-4adf-318e-8573-0c6351c8891b | -22.78234 | -47.08685 | 2025-08-22 04:23:00 | NOAA-20 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a7391434-dc96-3af9-b48e-acaa416acaec | -22.29259 | -48.21017 | 2025-08-22 04:23:00 | NOAA-20 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 90dc11ac-d4cc-391d-9733-ed6d142d3c30 | -22.37766 | -49.06783 | 2025-08-22 04:23:00 | NOAA-20 | BAURU | SÃO PAULO | Brasil | 3506003 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f44e5488-4c97-32e3-a457-07bbd5ae3e21 | -23.29977 | -47.46966 | 2025-08-22 04:23:00 | NOAA-20 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 7976b6e9-1bab-38eb-874a-d8ecdde69a01 | -22.78753 | -44.79353 | 2025-08-22 04:23:00 | NOAA-20 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 78ae3e91-bff5-3616-911c-a1c237373a77 | -21.32091 | -44.87427 | 2025-08-22 04:23:00 | NOAA-20 | ITUMIRIM | MINAS GERAIS | Brasil | 3134301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 698109e1-bf3b-353d-ae2b-26bc787c653a | -21.59505 | -48.98811 | 2025-08-22 04:23:00 | NOAA-20 | BORBOREMA | SÃO PAULO | Brasil | 3507407 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3424c01c-06e8-3f97-b8db-119c60b483be | -23.47542 | -46.22318 | 2025-08-22 04:23:00 | NOAA-20 | MOGI DAS CRUZES | SÃO PAULO | Brasil | 3530607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 69898355-5f4c-3b70-a934-8854f92bab8f | -23.29247 | -47.47233 | 2025-08-22 04:23:00 | NOAA-20 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 2dc50ea3-0465-3b9e-9baa-34ea61246879 | -22.29317 | -48.20644 | 2025-08-22 04:23:00 | NOAA-20 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cd512adc-da2c-34eb-9d96-48c0883454b7 | -20.74559 | -47.89941 | 2025-08-22 04:23:00 | NOAA-20 | ORLÂNDIA | SÃO PAULO | Brasil | 3534302 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b2475033-90e8-30dd-9b86-0077d9d482db | -21.95862 | -44.97525 | 2025-08-22 04:23:00 | NOAA-20 | SOLEDADE DE MINAS | MINAS GERAIS | Brasil | 3167806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 2cde5f9a-87ec-3309-a0ff-2bf813976683 | -22.02807 | -46.5379 | 2025-08-22 04:23:00 | NOAA-20 | ANDRADAS | MINAS GERAIS | Brasil | 3102605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 724b7219-3bb3-3794-b406-331b7fdd8290 | -23.97483 | -46.46747 | 2025-08-22 04:23:00 | NOAA-20 | SÃO VICENTE | SÃO PAULO | Brasil | 3551009 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 766205a0-795c-3ead-b1b8-3282018f84ea | -27.11246 | -50.58015 | 2025-08-22 04:25:00 | NOAA-20 | CURITIBANOS | SANTA CATARINA | Brasil | 4204806 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| ed785548-2a20-346b-bed5-31e127e6abdf | -27.10977 | -50.57555 | 2025-08-22 04:25:00 | NOAA-20 | CURITIBANOS | SANTA CATARINA | Brasil | 4204806 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| e14a6a4f-65dd-3764-aec7-28478ba48f0c | -15.8955 | -43.4523 | 2025-08-22 04:30:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 141.0 |
| b74f3f52-d6f3-3bb3-89de-cbf3b38abb84 | -15.8955 | -43.4523 | 2025-08-22 04:40:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 113.8 |
| 59366b56-a3c5-3d04-93c1-e489c6d6c01e | -13.0288 | -46.3213 | 2025-08-22 04:50:00 | GOES-19 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 2bffb9d1-e936-3459-aaf6-059d2dc3984a | -15.8955 | -43.4523 | 2025-08-22 04:50:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 103.5 |
| 72a362cd-de9e-3694-992c-7496b8c620d8 | -15.8955 | -43.4523 | 2025-08-22 05:00:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 109.9 |
| 3779b350-4ff5-3991-a207-1b615e3b583d | -12.9921 | -45.2252 | 2025-08-22 05:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 40.2 |
| ba4724b8-d220-34ec-81df-65547653f37a | -10.8571 | -50.8183 | 2025-08-22 05:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 42.7 |
| a78fcf48-2453-330c-95a3-26cdd4c12281 | -15.8955 | -43.4523 | 2025-08-22 05:10:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 84.2 |
| fee5aa36-3430-3214-aaf7-69beac9e6f44 | -12.9921 | -45.2252 | 2025-08-22 05:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 40.8 |
| 6e94279b-6daf-3b1d-9660-9054df58a219 | -5.87754 | -53.6255 | 2025-08-22 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 95fc1fc7-f607-32fe-9266-33d67c914b4a | -5.43532 | -60.18255 | 2025-08-22 05:10:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0a9464f4-63aa-3769-b2de-970dcbb75340 | -3.04131 | -49.44463 | 2025-08-22 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d38410b3-3c16-3e4d-a01a-2c0c54f5bc00 | -2.78895 | -49.59397 | 2025-08-22 05:10:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5913057d-e446-3c2a-b8e0-2174e4d5af3e | -6.55243 | -45.52597 | 2025-08-22 05:10:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3750ca34-5736-3863-889a-2d56f706ad0a | -3.83118 | -47.7353 | 2025-08-22 05:10:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 21f26195-65b8-355c-bb54-38b862193279 | -5.75385 | -52.32045 | 2025-08-22 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| da621ab5-64b6-3369-a1cf-fce7ec8fbcc5 | -6.43607 | -44.5214 | 2025-08-22 05:10:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 430116af-d481-3480-96dd-96833eb81862 | -7.62287 | -46.24638 | 2025-08-22 05:10:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3dc2c4ef-519a-311e-a4cc-bda5270a7b0e | -5.4479 | -60.17218 | 2025-08-22 05:10:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 521f82a8-407f-3508-a1f8-e9c552d12a13 | -4.60852 | -55.75019 | 2025-08-22 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1a92a061-0f85-351a-a9c2-fccd9b682605 | -5.79969 | -59.21689 | 2025-08-22 05:10:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 21f0df4c-27e8-33f6-9677-68616f25f5aa | -2.81211 | -49.20689 | 2025-08-22 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5f7ae43a-4899-3be6-943e-9645b8527844 | -4.77049 | -45.32258 | 2025-08-22 05:10:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 52930bd9-ac7f-35c3-b45b-a47942c49a78 | -6.44386 | -53.38336 | 2025-08-22 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 67ac5f72-b88d-3328-9cc0-49e28d76888e | -7.62626 | -46.25668 | 2025-08-22 05:10:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1ee2a285-d05d-3e78-bc3c-30015fb2316b | -5.3875 | -51.42912 | 2025-08-22 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2a4eb814-889a-3bf4-98b4-5693c513d1bb | -3.78253 | -51.82733 | 2025-08-22 05:10:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 017c33f2-8eac-3b88-be8e-e73e40093805 | -3.48384 | -47.68377 | 2025-08-22 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 31ed2ea9-6cbc-3bd5-a176-40bcb152a929 | -6.43783 | -44.51717 | 2025-08-22 05:10:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f184cf7a-8de6-3956-b0c6-a2f037b4171f | -7.86809 | -47.0004 | 2025-08-22 05:10:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f8f09086-09a9-3682-a2fa-24e77dc3973d | -6.55417 | -45.52119 | 2025-08-22 05:10:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 97effcf8-9466-33ee-800b-6529ec500c31 | -5.46498 | -46.47293 | 2025-08-22 05:10:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1fbcbfd8-369c-38f2-9da8-456c9947b270 | -6.2681 | -53.68447 | 2025-08-22 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3d316224-66ba-3ec4-8ab9-03670248c6b5 | -3.44016 | -47.55031 | 2025-08-22 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7ce5a3ed-df50-3f99-9685-1936459aca92 | -5.80991 | -59.2185 | 2025-08-22 05:10:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b259dc78-c3d6-3879-aa26-fcccce370766 | -4.10394 | -56.34894 | 2025-08-22 05:10:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4de6fe18-6fbf-397f-96bd-2d53b3f5a824 | -6.29741 | -43.70451 | 2025-08-22 05:10:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9ede231f-e52f-3bb4-96f2-f258a1d3daf8 | -2.91942 | -48.30419 | 2025-08-22 05:10:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bb18b416-81b6-3749-9d8a-6ef3f4e2a5c2 | -4.07801 | -46.92998 | 2025-08-22 05:10:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1c99da12-ca59-35a8-b899-5e10e327ff18 | -7.86321 | -46.99107 | 2025-08-22 05:10:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6d0890a5-c825-31bb-88fc-bb5f7b6aff32 | -7.58847 | -49.5704 | 2025-08-22 05:10:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0043b19a-199e-31c6-87ad-ff84278a2b74 | -5.88567 | -53.62218 | 2025-08-22 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6bfccc0b-befd-3716-9218-f59f5cbd82da | -5.88433 | -53.63116 | 2025-08-22 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0a195a03-daf5-30ec-9ba1-a40b0bf46b05 | -2.69285 | -48.20622 | 2025-08-22 05:10:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2cb233c2-2a28-3403-b74f-f33789cd89ba | -5.80592 | -59.22164 | 2025-08-22 05:10:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3581e0dd-b33c-3ae6-a4a9-2a92fe072ee3 | -2.25741 | -47.85056 | 2025-08-22 05:10:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| ee47b2a4-c84e-313d-ad63-f6348244f458 | -2.30779 | -48.14777 | 2025-08-22 05:10:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e64f0f07-ca2b-34d9-803f-b5f7d9d03c69 | -6.12139 | -53.86879 | 2025-08-22 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| af1a5382-6b29-3eee-9669-7a1015a1abeb | -5.8782 | -53.62103 | 2025-08-22 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 02a9104c-0f87-3264-b446-9059e1fe64da | -6.63671 | -47.90494 | 2025-08-22 05:10:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 03d44c84-6300-39e8-a445-8d78fd491b60 | -5.3115 | -55.92715 | 2025-08-22 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8a3374d7-4a3f-375c-8829-5ee425df14f1 | -4.13539 | -56.3437 | 2025-08-22 05:10:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c190cdb7-716d-3bfa-97f8-6655178e926d | -2.91897 | -48.30717 | 2025-08-22 05:10:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 637ae99a-9f56-3546-90d1-5e8c4ae2d960 | -5.45899 | -46.47213 | 2025-08-22 05:10:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7643a2a1-44cf-31b4-a599-9b05fabc5518 | -5.13509 | -56.97813 | 2025-08-22 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 42d7bdf6-0225-3016-b96d-d90f4bda4695 | -5.88366 | -53.6356 | 2025-08-22 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2b2a03cb-2e2e-33e3-8f0c-a13722294a91 | -5.88194 | -53.62159 | 2025-08-22 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6300f64e-5dfe-3de8-9c61-70b0c1ec6f58 | -2.83177 | -54.55998 | 2025-08-22 05:10:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 40f1c528-bd94-34e3-a491-d3dbe319191c | -4.14132 | -46.45255 | 2025-08-22 05:10:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b1909cf2-ab9a-33b9-9249-5da6d5e240f7 | -5.88127 | -53.62607 | 2025-08-22 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 47ae0d79-9cbb-36e6-95e1-cea246efd774 | -4.24788 | -54.92794 | 2025-08-22 05:10:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 98492b8e-0d5c-33f4-9bf0-67b060418681 | -3.73998 | -53.98061 | 2025-08-22 05:10:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ffd46106-e197-3f7d-91a6-eb9aea6200cd | -6.93869 | -44.29025 | 2025-08-22 05:10:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 4e5cd555-dbc3-317b-b59f-c3ae1ef00b5b | -2.4736 | -47.76747 | 2025-08-22 05:10:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 847fbf03-452c-38b6-8df3-3e2d6f0018b6 | -6.43859 | -44.51114 | 2025-08-22 05:10:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 906bae60-1d98-3610-9d11-a2e6f5260d98 | -2.38767 | -47.66131 | 2025-08-22 05:10:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1231703e-8e00-33da-9bef-ea6bc1552730 | -6.7099 | -51.41705 | 2025-08-22 05:10:00 | NOAA-21 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ea967a34-f587-3384-b17b-c046e9959f73 | -6.4291 | -44.67654 | 2025-08-22 05:10:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 44aaff80-1aa8-3a03-a44d-86e3cac90887 | -5.15396 | -62.52666 | 2025-08-22 05:10:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f903b081-6eae-34a1-8010-03d0ba4b9592 | -5.81108 | -59.21113 | 2025-08-22 05:10:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2a223f3f-6c50-3826-ae1b-c2c2cad894ca | -3.38694 | -47.6129 | 2025-08-22 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 82f5d323-da74-393b-b63c-a48c47ac4022 | -6.90064 | -52.86677 | 2025-08-22 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2d1ae011-15ee-30dd-94f0-e501414f5988 | -2.25695 | -47.85374 | 2025-08-22 05:10:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| bd11c443-5183-3a68-a84a-55e428f3bf1e | -1.97228 | -56.51626 | 2025-08-22 05:10:00 | NOAA-21 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d531f5ad-bfe7-3857-8d3f-6f1f6151cc3d | -4.32897 | -55.13129 | 2025-08-22 05:10:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 92586eb1-9830-3c8e-a1af-4617e104f66e | -2.81282 | -49.2029 | 2025-08-22 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1ea48460-36f3-38df-9e03-dafb4c6cde97 | -6.74631 | -50.96053 | 2025-08-22 05:10:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 58bb18df-dc5f-3a7b-b1ca-cd2cc75b4fcc | -5.87313 | -53.62944 | 2025-08-22 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7aae817c-e0b7-3d5e-ad78-ab0adfc4fafe | -6.5531 | -45.52111 | 2025-08-22 05:10:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f8eb8dab-9d25-3844-b20b-981f195811ca | -7.86158 | -47.00377 | 2025-08-22 05:10:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7132eb30-5b80-3317-9f7c-d64d4131fcff | -6.45461 | -53.38981 | 2025-08-22 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README42.md)

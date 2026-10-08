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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 951211f0-9fd7-34c3-8f7a-d1608f0ac13c | -3.0319 | -53.9021 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4ed31062-d32e-30b1-9a65-e4e2a3d7fb24 | -3.3054 | -54.699402 | 2026-10-08 00:26:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8a9fdf1b-a2d5-37fe-9438-a88f73c70c5d | -2.5059 | -56.135502 | 2026-10-08 00:26:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ca2caee7-24e2-3580-9794-1b0814ee2335 | -4.7551 | -55.645599 | 2026-10-08 00:26:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fcb9c5cb-e103-337f-8e20-47263dbb11c7 | -3.1716 | -50.550201 | 2026-10-08 00:26:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d78b3f0a-bd44-36c0-84d7-b145b3448797 | -3.169 | -54.097099 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 273e6d69-0b63-3c67-af3f-3a368f418120 | -3.2713 | -54.6856 | 2026-10-08 00:26:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a00db4ac-253f-357f-af85-2c3714e5d894 | -3.5107 | -59.2043 | 2026-10-08 00:26:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 010ffe1f-9b7b-3359-9954-a672887fa915 | -3.5875 | -54.5793 | 2026-10-08 00:26:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a0083b09-ff39-315f-9673-2f397b6d176a | -2.9882 | -56.5854 | 2026-10-08 00:26:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c86411de-8bb3-3b05-b8be-c4b90083ee48 | -3.0424 | -57.4706 | 2026-10-08 00:26:00 | METOP-B | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cca91c8d-f708-36c1-b2ef-9eef9904cc18 | -2.9594 | -54.172901 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cc57c6cd-b6cd-37ee-b7bb-0bf1b162132f | -2.0459 | -56.883999 | 2026-10-08 00:26:00 | METOP-B | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 411abe02-f041-3e01-93c6-317f7ee83e18 | -4.965 | -55.112 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dbb043bc-27d9-31e8-9e63-3b66d0f39634 | -1.603 | -55.1492 | 2026-10-08 00:26:00 | METOP-B | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f1f22c8d-ddd2-3eab-bd35-ca2ce7c2d110 | -2.5024 | -56.165501 | 2026-10-08 00:26:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 13574725-56df-34d2-8a8c-0d4bd9233a87 | -3.6541 | -54.053902 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 406d3bdd-4b06-32d2-93cd-61733ee30de4 | -2.6468 | -56.5331 | 2026-10-08 00:26:00 | METOP-B | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6b7dddeb-76f9-39ce-883b-3e784fef074f | -3.4842 | -54.623798 | 2026-10-08 00:26:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 09c282c4-6c94-3a5d-af95-c0625718ce6b | -2.9882 | -54.7556 | 2026-10-08 00:26:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2f0ca362-6277-33f8-9215-930fc35a289c | -2.8474 | -57.473 | 2026-10-08 00:26:00 | METOP-B | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d0ac55f6-d156-396a-91b9-afc138dd2d7d | -3.4694 | -59.574299 | 2026-10-08 00:26:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5946517c-fb61-3b47-b7bb-c68d60b42eb0 | -4.2767 | -50.784801 | 2026-10-08 00:26:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ae45d51a-f4bd-3754-8dcb-6cf8bf19666a | -7.7582 | -54.936501 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1677e22a-12c4-3d2b-808e-23b175cb7e2d | -2.9444 | -54.1978 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fb39ae9f-c996-3c3f-8cdc-7de9d0c856fe | -4.915 | -55.853901 | 2026-10-08 00:26:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 10c5023e-50f7-3b7d-a45c-46dc2c7a0c3c | -3.5394 | -54.640099 | 2026-10-08 00:26:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 55293613-60e6-30ce-8b77-116315786c84 | -2.4717 | -58.0009 | 2026-10-08 00:26:00 | METOP-B | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 463acafa-0f4f-38ce-b614-d284fabf3b67 | -3.0203 | -54.123001 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b80c87a6-9cbf-319d-92f7-b52662aad4d3 | -3.2907 | -53.997299 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4b7d0c9d-997e-350a-ad75-747c0e7d137e | -2.9319 | -54.1427 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cba1afab-4015-36a3-832b-d5cc54d830f9 | -5.9869 | -55.351101 | 2026-10-08 00:26:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8b395dba-c997-3d5d-bbe2-e615f3541339 | -4.2963 | -50.780399 | 2026-10-08 00:26:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b340de6e-0b4b-3e7e-a2fa-d1579b037645 | -4.1316 | -54.25 | 2026-10-08 00:26:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 87fc5723-9903-32ad-9ca9-2d317a718db8 | -3.4924 | -54.614799 | 2026-10-08 00:26:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fdf56ec0-66e9-316b-9597-1bbb7e3de0c2 | -9.156 | -49.814301 | 2026-10-08 00:26:00 | METOP-B | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6d98830a-2671-3ff1-bd05-3a7de12987a2 | -3.591 | -54.685902 | 2026-10-08 00:26:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aa3010af-52e5-3f7c-b7f5-263199306779 | -2.7822 | -57.6418 | 2026-10-08 00:26:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ff3c91a2-18e4-3b23-8ff3-b8f344d4cb3d | -3.5833 | -54.651798 | 2026-10-08 00:26:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 75f5e040-28a3-3624-b847-53aebca94279 | -3.9962 | -56.2579 | 2026-10-08 00:26:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a33d5eb8-af37-39fc-8a15-d68f9d3ee792 | -6.1018 | -55.6814 | 2026-10-08 00:26:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 97b3e189-3c51-3219-b598-da4d914f538a | -3.1128 | -54.1675 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 876729fc-a33f-3465-a8ca-cd1a9b9b2c82 | -4.1169 | -59.859402 | 2026-10-08 00:26:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5798041b-2a9a-37ef-aa4a-5ca9b83792c3 | -5.8198 | -53.8288 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4bcbb182-536b-3f2d-a968-d02a0285879e | -1.5177 | -54.817799 | 2026-10-08 00:26:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b64395e8-8107-38e2-99ac-8d9354a33c83 | -3.0614 | -59.261902 | 2026-10-08 00:26:00 | METOP-B | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 99032c5e-a755-3eba-ac81-2d3d43a12727 | -2.8806 | -54.872501 | 2026-10-08 00:26:00 | METOP-B | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9bf7946d-e809-3a87-a1b1-6ae86c0b5642 | -5.8496 | -53.459702 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 02dc60ac-0980-37d0-aee7-8f11d0ec01c5 | -3.0579 | -53.925499 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1545f1c9-dcf0-3f68-8bf9-ff35076a77d1 | -10.4232 | -47.262001 | 2026-10-08 00:26:00 | METOP-B | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 233064ac-f06b-3a81-b20b-122f107547dc | -3.1706 | -54.104 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1700e877-27bf-35dc-983a-e9b96e576bca | -6.1597 | -52.647999 | 2026-10-08 00:26:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5452d667-d1d5-3d9f-8e05-57eaa41021d7 | -2.8731 | -54.155899 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ad426571-aeac-370e-947b-957123bcf31e | -2.9573 | -54.209499 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 85980612-3ad0-3a88-9bc2-705771d746ac | -1.3427 | -55.456699 | 2026-10-08 00:26:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f0f1dc71-045f-31e3-b989-d6dc3b140223 | -2.8864 | -54.123901 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 97f03ff9-b1df-3e80-9f1c-4c6fe54c37e1 | -3.1113 | -54.160599 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fbcf7334-4c98-3c11-97d5-c865ea04461c | -6.7455 | -55.058399 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7b5d60ea-8c45-3d88-9839-1025be651fde | -2.9366 | -54.163399 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3e813e68-7de3-3077-85be-a225525d5720 | -3.04 | -54.256001 | 2026-10-08 00:26:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b59998f8-5177-3b86-9727-ec5fcb45b7e1 | -7.3885 | -55.218201 | 2026-10-08 00:26:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 697b0d00-379d-3861-bd55-6a6167fc22c6 | -6.3202 | -55.321602 | 2026-10-08 00:26:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cd26b6bd-3313-3877-95a3-874f01dc0ded | -2.877 | -54.082401 | 2026-10-08 00:26:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8500c466-bcc7-3c1a-8563-99b223c19baa | -13.7995 | -52.788601 | 2026-10-08 00:26:00 | METOP-B | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d7640a14-287b-3b65-b4fb-666edee37465 | -3.1145 | -53.7663 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8d0ae6c8-2667-37c9-9821-4bd078658db4 | -3.74 | -59.4524 | 2026-10-08 00:26:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7c3e65f4-6c23-3baf-8f50-3f283bf7460b | -5.7122 | -53.490601 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 57683526-a027-30c0-9943-dfb3aab4ba1a | -2.9931 | -54.049198 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a7ed85b4-b2f6-3301-9d48-9f9b504604b0 | -13.6927 | -49.119301 | 2026-10-08 00:26:00 | METOP-B | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b8b2b559-73a7-3cea-a730-5a145d8b5794 | -1.5291 | -54.822498 | 2026-10-08 00:26:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7512e9a2-ac24-3295-9b6b-c2242bc94357 | -3.1587 | -50.583302 | 2026-10-08 00:26:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 26767a64-6162-33f5-913a-a6141fcaf3e1 | -5.2594 | -45.388401 | 2026-10-08 00:26:00 | METOP-B | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fcaea032-efed-372a-9d50-2728e370e3b4 | -2.513 | -56.258598 | 2026-10-08 00:26:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ead0c9de-b12d-3394-b486-58f8eeeefd05 | -3.3524 | -59.8801 | 2026-10-08 00:26:00 | METOP-B | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 20636a67-bbaf-337f-a361-f8fa3a482b0e | -1.7182 | -55.430599 | 2026-10-08 00:26:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c27d3f51-63ef-3b7b-bd2d-3cad7ca8a65a | -2.9303 | -54.135799 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 88f21b60-8cc4-3ea2-99ba-8304b65310a4 | -3.2214 | -54.374001 | 2026-10-08 00:26:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6232ffb9-4e9c-38b1-bf9d-9ea258367920 | -3.8525 | -55.984798 | 2026-10-08 00:26:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b190074d-0249-3964-a32f-0f41d9bb1de4 | -4.1521 | -54.022099 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2edc59c4-d57c-379f-a840-1aa22638223e | -3.0909 | -58.009701 | 2026-10-08 00:26:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ca9a31c4-388f-30ec-b477-19f14992f03b | -3.3486 | -50.469398 | 2026-10-08 00:26:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 046b9127-f8df-3fc5-90de-b8fe28c865e2 | -1.4468 | -54.459099 | 2026-10-08 00:26:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dd7223ff-7b74-31de-871f-209a98aaf9ae | -2.9904 | -54.1731 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 88da953b-ea50-3724-b8c1-e1b9e42c2861 | -2.9536 | -54.1017 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3d52a6a3-8737-3ed5-8b3f-97ca04a27f40 | -6.8699 | -43.6954 | 2026-10-08 00:26:00 | METOP-B | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 32eb2070-f6c9-378b-a5b6-b0e086c96a76 | -14.2263 | -48.536701 | 2026-10-08 00:26:00 | METOP-B | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 99288f5a-c8c9-312c-b877-cff2db50dc6f | -3.5069 | -54.633099 | 2026-10-08 00:26:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c5345a7f-804e-310d-8458-63bfa9dfd1f8 | -6.0421 | -52.765301 | 2026-10-08 00:26:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 16c327b7-383a-3891-86d4-b9093161172b | -7.3854 | -55.204102 | 2026-10-08 00:26:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eef864ca-0c76-32cc-85bd-29f378ee4900 | -6.2283 | -52.858002 | 2026-10-08 00:26:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 791555c4-6395-3692-bbf7-d8f5795255c0 | -10.6147 | -60.473801 | 2026-10-08 00:26:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 72bef73e-2daf-3618-a823-0c482c7ddcbc | -3.0191 | -54.072498 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 189d23c4-ce70-3cbf-9820-b60ebea62e07 | -3.1045 | -54.176601 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4f861cbd-f727-3574-9e1c-4f5d2145ca30 | -3.586 | -54.572498 | 2026-10-08 00:26:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2c463f74-de53-3a97-8bb0-f7f1b3642d40 | -2.9127 | -54.1035 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 472070c3-770c-3d43-9cbc-b579461e325b | -3.0998 | -54.155899 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ab7c5842-1e32-39de-bdfc-ffa3a9233efe | -10.466 | -47.225498 | 2026-10-08 00:26:00 | METOP-B | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 577ebe0b-f6c1-3911-82e5-b1f1d40aeeea | -3.024 | -54.230701 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ca069981-e116-3bf3-80c7-462ae72e3542 | -2.123 | -54.805 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 689706ea-2ef1-3160-b7d5-dcdcf58e8504 | -1.3756 | -56.881302 | 2026-10-08 00:26:00 | METOP-B | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README20.md)

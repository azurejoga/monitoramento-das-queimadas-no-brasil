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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d8e96878-746f-31ea-a66c-3cc5d18a1eb7 | -18.5675 | -56.8109 | 2026-07-21 05:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 56.7 |
| 66107d61-0ce4-3352-903a-74793b81d12d | -18.5476 | -56.8135 | 2026-07-21 05:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 144.8 |
| dfc38d9b-67e1-316a-8989-53fdd23be4ed | -13.3 | -45.14 | 2026-07-21 05:15:00 | MSG-03 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c5a45896-f170-3f99-8200-54b876d6f545 | -18.5675 | -56.8109 | 2026-07-21 05:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 73.9 |
| 9c766923-fc85-32e3-b768-42fc7c0bc068 | -13.3221 | -45.1246 | 2026-07-21 05:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 131.8 |
| 4a14703d-68cd-311a-be30-33f46e349681 | -13.3028 | -45.1278 | 2026-07-21 05:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 113.0 |
| b2406d5a-f4ce-36cb-986f-873e5d49b202 | -18.5671 | -56.8317 | 2026-07-21 05:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 64.4 |
| ef6d985d-a75b-36a4-9e5d-faa55c99e9c2 | -18.5472 | -56.8343 | 2026-07-21 05:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 80.2 |
| d3cd88e1-2210-3539-8075-cc7861dcb80f | -13.3032 | -45.1045 | 2026-07-21 05:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 47.6 |
| 7fe13efd-1400-3b6d-b868-79d5d6a7d5ee | -18.5476 | -56.8135 | 2026-07-21 05:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 104.3 |
| bb6e74ed-c7ed-3f6e-86fa-8fd3abf5efe7 | -13.3226 | -45.1013 | 2026-07-21 05:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 45.3 |
| c383233f-2ca9-3b5f-a332-89c4569d2376 | -2.79926 | -49.52367 | 2026-07-21 05:21:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e48ad0e8-1700-3543-a16e-68d6dedba932 | -3.14706 | -48.58033 | 2026-07-21 05:21:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ae70df6f-1db6-3969-978d-97c3fd46123e | -3.14684 | -48.15554 | 2026-07-21 05:21:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2c695c4e-78bd-3890-9c9e-0839e40b6519 | -3.14169 | -48.15067 | 2026-07-21 05:21:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ed744d5e-b622-3d36-8708-19dfe1d7fe7c | -3.15265 | -48.5811 | 2026-07-21 05:21:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 11eb5ad9-b163-34eb-a993-f2706a7d4ccd | -2.79404 | -49.52293 | 2026-07-21 05:21:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7b962de0-cb99-3f0e-9ae1-6e6273d0927a | -2.46413 | -54.69062 | 2026-07-21 05:21:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fae528aa-b2a4-3c52-ac23-15679dbc88c1 | -17.57846 | -47.50265 | 2026-07-21 05:23:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3c066689-b2fb-3a75-a1cb-7fb295312af3 | -10.8236 | -50.42727 | 2026-07-21 05:23:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2a99aa83-e781-3926-a6f3-f3a9314f6bc7 | -12.66528 | -48.20407 | 2026-07-21 05:23:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e498a78f-dcf0-3810-8b91-265401a3982b | -12.66586 | -48.199 | 2026-07-21 05:23:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8742e457-7bf9-37a3-9d59-e7fb2e651191 | -10.06909 | -60.49704 | 2026-07-21 05:23:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 162fbef6-7aae-3f50-9d96-cd4db18141a2 | -12.00819 | -50.54872 | 2026-07-21 05:23:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5fcc11fa-8a07-3465-9536-1ff12b426c87 | -9.10116 | -71.27143 | 2026-07-21 05:23:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ee993e32-72ba-3d3b-90cf-7ad9d334ce6f | -9.49498 | -63.30698 | 2026-07-21 05:23:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 336a906c-a4d5-30eb-a9ed-0e5fd2f8b2d9 | -8.75198 | -49.08442 | 2026-07-21 05:23:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| f7c842e5-2199-30a7-873f-edd95a7211db | -7.63326 | -49.75138 | 2026-07-21 05:23:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| bd200711-35be-3980-abe6-9a8986d37999 | -17.58141 | -47.51406 | 2026-07-21 05:23:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 017a358c-e473-32df-9ac8-c9100ee64742 | -9.10126 | -59.40088 | 2026-07-21 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 28b67d99-ac58-30c8-a79a-cfdd41352384 | -10.26257 | -59.03053 | 2026-07-21 05:23:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9bf47be5-b9a3-33fe-a16b-3b0b07706778 | -10.51598 | -50.28881 | 2026-07-21 05:23:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0e91dba4-f346-3184-9b49-3dec61cd9c7a | -9.10457 | -59.40141 | 2026-07-21 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| be0007e7-280e-39c3-ad9f-01d9b3ee7a7a | -12.13798 | -48.258 | 2026-07-21 05:23:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c73f42ea-8763-34f2-b697-b1180eeb57b1 | -7.86628 | -61.49056 | 2026-07-21 05:23:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| aec9a7fe-566c-3609-b45f-197e81e0c645 | -7.63878 | -49.75216 | 2026-07-21 05:23:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 17169e8d-4357-3579-84d9-648a41391bcf | -7.63277 | -49.75504 | 2026-07-21 05:23:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| e53ea824-4a31-3894-a451-4b354722a22d | -10.63355 | -47.48866 | 2026-07-21 05:23:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 718c05d4-fdc8-33b3-b1ae-ef78cf836d9f | -12.08759 | -53.33818 | 2026-07-21 05:23:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a3e96149-7d1a-3381-b668-cc655b1dc796 | -10.55662 | -56.32839 | 2026-07-21 05:23:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8a84a0e9-c065-3a7a-a48e-08b65aa0f85a | -10.8461 | -50.42653 | 2026-07-21 05:23:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3b530828-7549-3878-a714-69a8f0a2d5b8 | -10.50996 | -50.2918 | 2026-07-21 05:23:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b8064d0d-ae31-32b3-b6fc-ae941e813d6c | -10.54998 | -56.33363 | 2026-07-21 05:23:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 388bc353-f4d9-3617-8852-a49fcf232e42 | -10.01957 | -65.05096 | 2026-07-21 05:23:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0ad26073-b460-3881-b862-839c789aff8a | -10.52803 | -50.28289 | 2026-07-21 05:23:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8abdfae2-40b2-3752-bbc7-268141291a59 | -9.53347 | -57.37586 | 2026-07-21 05:23:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 63a80013-8e7e-3ca8-aaf6-678200e45af5 | -7.68561 | -55.36985 | 2026-07-21 05:23:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 28295337-911d-3463-bd18-d2eba7222297 | -6.13042 | -55.80571 | 2026-07-21 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d1ee1f9f-912e-340a-b1b4-529d9846b750 | -12.66589 | -48.20122 | 2026-07-21 05:23:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bb128a33-4dca-34d3-9e4f-13d25d091cd2 | -10.85759 | -50.42433 | 2026-07-21 05:23:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 235edd6d-5236-38e1-9ba3-7374f72338ca | -10.63427 | -47.48271 | 2026-07-21 05:23:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8aae9e73-f041-3c2f-9622-da712ef5d869 | -9.10016 | -59.40784 | 2026-07-21 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8e2fe911-2e5a-3af1-b7e6-599d8c56e60c | -17.58857 | -47.51431 | 2026-07-21 05:23:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3f413fb1-9be3-31f8-ac8f-2839f5daf09c | -10.52852 | -50.27923 | 2026-07-21 05:23:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 93cb94ec-a04c-37ad-b4a0-15b6daa2b361 | -9.49571 | -63.30264 | 2026-07-21 05:23:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 01e4e33a-55c6-3525-9fee-93483c1c5d10 | -6.4303 | -54.71716 | 2026-07-21 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2cd29148-9cf9-35de-8771-2e07e65c173f | -10.54791 | -56.3362 | 2026-07-21 05:23:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b655f0e7-3bc7-32ce-a9a8-fc3fbbe894d1 | -10.54855 | -56.33171 | 2026-07-21 05:23:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 78d5d26f-836a-3166-893c-5116d187d9e7 | -17.58561 | -47.50307 | 2026-07-21 05:23:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1e2b65ae-4944-3776-9373-a135b836ae67 | -12.52098 | -48.25771 | 2026-07-21 05:23:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5237e1ca-9574-3857-8405-08e74d7e54ea | -9.25864 | -59.82513 | 2026-07-21 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6b205a54-7246-303c-971f-0ef35dcd4d55 | -10.01092 | -65.053 | 2026-07-21 05:23:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aca46adb-dcc1-33fc-b504-970f3d3c7d8c | -10.84656 | -50.42289 | 2026-07-21 05:23:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4b03ddc5-e79a-308f-93ba-c36456b3bdff | -9.08761 | -50.58613 | 2026-07-21 05:23:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3c9db0e0-2f12-320f-a617-3ed42e7bc237 | -11.34391 | -47.99805 | 2026-07-21 05:23:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 39feeb90-ab4a-3dd8-b393-c2f0f07d9073 | -10.79048 | -50.42348 | 2026-07-21 05:23:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| db026002-7937-32fb-8b4f-195f0aaab9c9 | -10.86311 | -50.42505 | 2026-07-21 05:23:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 41e27aae-72f3-34a9-afee-e76347656d5d | -6.12979 | -55.80987 | 2026-07-21 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 08358500-f4a7-38df-a2fb-3d2635dd70bd | -10.86357 | -50.42139 | 2026-07-21 05:23:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6880b4de-d9e8-3dfc-b9d7-836f76f4fedf | -10.6269 | -47.48804 | 2026-07-21 05:23:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d6b30ff8-c334-3b60-b5c5-ffe468c54341 | -7.68628 | -55.36526 | 2026-07-21 05:23:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c07c6823-c930-331c-bcd1-8fbf3f844423 | -10.51593 | -50.28723 | 2026-07-21 05:23:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d1744ed7-5b60-3972-bd70-c66448f8094e | -10.85162 | -50.42725 | 2026-07-21 05:23:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ddc12298-bfc8-3282-956e-415b961a09cd | -7.68696 | -55.36065 | 2026-07-21 05:23:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e8eca603-95b3-3d9d-bc8c-c70aa4367868 | -10.46945 | -62.45099 | 2026-07-21 05:23:00 | NOAA-20 | JARU | RONDÔNIA | Brasil | 1100114 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 148b03b9-fbb5-334a-93d7-910f6aae498e | -8.75202 | -49.07944 | 2026-07-21 05:23:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a0431da7-9803-3e79-be9d-62180b429b6d | -8.75837 | -49.08112 | 2026-07-21 05:23:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7c14a696-10a5-3d78-9cd0-dd012a34d889 | -10.55597 | -56.33287 | 2026-07-21 05:23:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| beede344-b835-3632-81b2-b7c2fc5f862b | -12.08298 | -53.33756 | 2026-07-21 05:23:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 61183919-bf16-325b-98ba-baa917db9502 | -7.63828 | -49.75581 | 2026-07-21 05:23:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 11dc4219-8fa7-3e3e-87fe-2ec571b685a3 | -7.62775 | -49.75058 | 2026-07-21 05:23:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b5ede2e1-c196-3856-989c-2941105b9bbb | -6.13106 | -55.80151 | 2026-07-21 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ec15df1d-13d0-322a-b004-6577fcdf9d4f | -9.25919 | -59.82165 | 2026-07-21 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8b5defdb-fce1-345e-b7b4-b6b16c840f8a | -10.85207 | -50.42361 | 2026-07-21 05:23:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 272e8b1c-c744-3e66-b96f-26f8d20d281d | -17.58436 | -47.51668 | 2026-07-21 05:23:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 6dd227e0-390a-344d-a439-b811f81b7bb4 | -9.91889 | -65.0049 | 2026-07-21 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9cafae45-c389-31e0-be79-4c3b9555e027 | -9.09795 | -59.40035 | 2026-07-21 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 072d1f77-8440-3002-ab10-7959ebe45c0a | -7.34992 | -49.6023 | 2026-07-21 05:23:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 79b33c0c-d6f7-3ebb-9d9b-ee6fa4212834 | -8.75786 | -49.08035 | 2026-07-21 05:23:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7b7bb720-c757-30fa-8822-1b4882ee6903 | -10.85713 | -50.42797 | 2026-07-21 05:23:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a8bd446c-b7fa-3d30-a054-b939806b1565 | -10.63215 | -47.48486 | 2026-07-21 05:23:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d2256650-2caf-357b-a655-6cb7ecfd3769 | -9.10248 | -71.26815 | 2026-07-21 05:23:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 85e01cd5-8b20-3b27-a7c3-b6d9ea8b8736 | -17.58915 | -47.50754 | 2026-07-21 05:23:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| bbc920fa-9640-3552-bc11-8d4f24195e12 | -7.69006 | -55.36584 | 2026-07-21 05:23:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 006b282c-acc6-3e92-ab3e-d345e51bcb19 | -12.5216 | -48.25224 | 2026-07-21 05:23:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b0ba0d5c-b135-3551-afd2-7fc5e2de426c | -17.58496 | -47.51017 | 2026-07-21 05:23:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 15cdb4db-b994-3ba0-89d3-bd1350c8b6ee | -7.68318 | -55.36005 | 2026-07-21 05:23:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b44f27cd-1e77-3791-9eb9-065a349dcec0 | -9.10212 | -71.26648 | 2026-07-21 05:23:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 21f3960d-f195-329a-8aef-57bb17b3ca66 | -10.56033 | -56.32899 | 2026-07-21 05:23:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 23cc4fbc-8867-3ba4-9a7b-0c28b6bcafdf | -10.01495 | -65.05376 | 2026-07-21 05:23:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README15.md)

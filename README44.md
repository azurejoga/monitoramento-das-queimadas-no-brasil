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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 07c8ece9-2773-3f23-a0c6-e6a5556c54a7 | -11.02541 | -48.27625 | 2024-10-23 04:53:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 7515a11f-1566-32fd-8227-57e9b12bb3d8 | -11.0249 | -48.28003 | 2024-10-23 04:53:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| c38279a6-d5af-3846-aaef-12d027a6932d | -11.12111 | -48.10143 | 2024-10-23 04:53:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6930728b-84fc-3fb1-8d77-9489f3958f78 | -11.12057 | -48.10525 | 2024-10-23 04:53:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9b9622ce-20b0-3ca9-bb8b-5b4ac1c6da6d | -10.96034 | -47.82961 | 2024-10-23 04:53:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f1b15c50-1ce4-3f86-ad7a-3a50713d0d83 | -10.95673 | -47.82466 | 2024-10-23 04:53:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fb82487b-a644-3a48-8474-f3d6aa02499c | -10.95258 | -47.82358 | 2024-10-23 04:53:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 52b1a557-7243-34a1-8c11-0eaa0db493d6 | -10.95202 | -47.82751 | 2024-10-23 04:53:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9cf6a56e-c0db-37cd-ac40-f3e63d5820a7 | -10.95149 | -47.83133 | 2024-10-23 04:53:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7633cbfd-0173-3628-9ce0-b6cc2c6115f2 | -10.9382 | -47.83406 | 2024-10-23 04:53:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 310d2201-0f75-348a-809d-bcf95052f875 | -10.93763 | -47.83818 | 2024-10-23 04:53:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7cb4ea56-7fc4-3bfa-8211-f8d9359f2670 | -10.93079 | -47.82549 | 2024-10-23 04:53:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e4d8494a-d528-3d31-b725-33b362c33209 | -12.61449 | -48.5254 | 2024-10-23 04:53:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9182f0c0-7806-38c4-923a-8af17a5e5c31 | -12.49071 | -49.46956 | 2024-10-23 04:53:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 302c4094-daae-348d-b930-440afa115752 | -12.19781 | -50.36522 | 2024-10-23 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 7a4ff243-a40b-3ac4-b032-278fb982ac36 | -12.13369 | -50.28786 | 2024-10-23 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c36d83f4-18fb-3b25-905a-34020f9bf41e | -12.13131 | -50.28444 | 2024-10-23 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a4b230af-3388-3912-b56d-e133f80666d2 | -12.13 | -50.28731 | 2024-10-23 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4b318cb0-dfa4-3e63-96ff-715679dbee89 | -12.12763 | -50.28389 | 2024-10-23 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6692081e-4e08-30a6-bf81-92a14205e4ba | -11.59447 | -49.8282 | 2024-10-23 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0c90acee-b16d-3fe1-bbc1-be2b5499f2b3 | -11.58631 | -49.83168 | 2024-10-23 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7c0a6540-7bac-30c5-b0c4-b411f7fe7e40 | -15.0028 | -51.07592 | 2024-10-23 04:53:00 | NOAA-21 | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d021634d-f2ae-3c93-8970-c782a7832777 | -14.26347 | -51.12379 | 2024-10-23 04:53:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| aedccb18-6adc-3611-8ef2-45ea50e964d6 | -14.26286 | -51.12807 | 2024-10-23 04:53:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1147727e-6e10-3a2c-92e5-23b530955094 | -15.78703 | -50.51932 | 2024-10-23 04:53:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aa299025-e22d-3c32-8aa3-65b10937504e | -15.78619 | -50.80922 | 2024-10-23 04:53:00 | NOAA-21 | ITAPIRAPUÃ | GOIÁS | Brasil | 5211008 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ac529abc-1fdc-3b60-a330-0983d471ae16 | -15.6975 | -50.46888 | 2024-10-23 04:53:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c88a8664-8152-31b5-97b8-e96e49455b42 | -10.74436 | -51.80973 | 2024-10-23 04:53:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e5083233-9246-341b-a7a1-e902b1abecca | -9.54984 | -51.73386 | 2024-10-23 04:53:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eb64d31c-19fb-31c8-b718-9830344a99fd | -14.19895 | -51.64236 | 2024-10-23 04:53:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 90118126-5b10-3cf2-ab93-bbb7dd3c2b2d | -13.29461 | -53.75879 | 2024-10-23 04:53:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 90047e14-69d5-340d-8de5-f44e3db0fc93 | -14.33395 | -54.05139 | 2024-10-23 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 51ec34d3-f1ad-376e-ac25-71e3f0b10974 | -10.76415 | -54.22815 | 2024-10-23 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 24f7f044-8bf1-359d-b40d-47060a49924f | -10.76377 | -54.10201 | 2024-10-23 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2abfa102-c77a-3588-a589-659ec8fcc3ea | -10.67319 | -54.8995 | 2024-10-23 04:53:00 | NOAA-21 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 16a32601-7a02-3f3f-8005-b80ab5e7f86a | -10.31556 | -55.0873 | 2024-10-23 04:53:00 | NOAA-21 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fcd2624b-87a6-3525-a1f3-0a6b824ed0db | -10.07175 | -54.85297 | 2024-10-23 04:53:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7654b50f-a089-3bd4-9d7c-f8634a4ef33a | -10.02279 | -55.13374 | 2024-10-23 04:53:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| db084209-ba1e-329a-ae49-e4fa72419736 | -11.87582 | -55.44986 | 2024-10-23 04:53:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5dc2f605-d036-3859-a06b-a1e4f2eeeac8 | -11.60252 | -54.49979 | 2024-10-23 04:53:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2f0b60ae-ef92-38ca-bf01-24842e352691 | -11.51563 | -54.34017 | 2024-10-23 04:53:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0733c3b1-d47b-3dab-a8f1-39103d4754c1 | -11.51232 | -54.33964 | 2024-10-23 04:53:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c978b674-54b6-3f55-92ad-bdb5cc28c6fa | -11.47661 | -54.98793 | 2024-10-23 04:53:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c1af3bb2-a0b4-317e-a807-37cf0b57e850 | -11.47268 | -54.99098 | 2024-10-23 04:53:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 84b5d00f-24a2-37a6-89a1-8197d137ad0d | -11.4296 | -54.3045 | 2024-10-23 04:53:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d643b4bb-045b-386b-b0b1-791b30432e44 | -11.42242 | -54.30695 | 2024-10-23 04:53:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0a556de2-8086-328a-9d24-953db1fa971b | -11.33643 | -54.35447 | 2024-10-23 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 69284960-9b7b-331b-8243-9405785afe01 | -11.33368 | -54.3504 | 2024-10-23 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 101afb41-2cb5-345b-9e79-ff4905fc83d9 | -11.33312 | -54.35393 | 2024-10-23 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 3540a8d1-3370-33e3-86fc-3cad12c97069 | -11.31662 | -54.32954 | 2024-10-23 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| b786ff04-847c-38f4-97da-10079a6e13d9 | -11.31331 | -54.32899 | 2024-10-23 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 6760be08-281e-3b4f-bf00-d71c03a51356 | -11.27692 | -54.23654 | 2024-10-23 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 12aa0f43-38d7-3cd9-ae79-f862e32d4f21 | -12.50534 | -54.43133 | 2024-10-23 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 14a600ca-d2d4-3872-9ad4-c088d4992a80 | -12.50478 | -54.43486 | 2024-10-23 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1545908c-b52d-39b2-86ba-f0cfbe336a56 | -12.50147 | -54.43431 | 2024-10-23 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f54af352-d989-3f06-8c94-e27cf1dee75c | -12.48963 | -54.39941 | 2024-10-23 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f8b48c7d-caba-3a91-b99d-90809608024c | -10.64661 | -56.76972 | 2024-10-23 04:53:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3426e7fe-e8a6-366c-9b39-4219cc57aabc | -10.48372 | -55.60403 | 2024-10-23 04:53:00 | NOAA-21 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| db37b3cf-1b83-3281-98ca-13b9a922d7d4 | -10.36736 | -55.58519 | 2024-10-23 04:53:00 | NOAA-21 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f348f963-2358-36e6-aefd-1cd40f2115b4 | -10.29708 | -55.39184 | 2024-10-23 04:53:00 | NOAA-21 | NOVA GUARITA | MATO GROSSO | Brasil | 5108808 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2cc4f965-32ac-30b4-9926-99560db07b82 | -10.08543 | -55.39613 | 2024-10-23 04:53:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d13e11e0-f00a-3ced-98f4-ad7ca6c6d4a9 | -10.79593 | -55.48118 | 2024-10-23 04:53:00 | NOAA-21 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d00d0c4e-a8d2-3926-a5b9-1f5435e9186d | -10.66392 | -56.64372 | 2024-10-23 04:53:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b7a5bec9-2d3d-3257-a425-059baeccb1ec | -11.88294 | -56.41324 | 2024-10-23 04:53:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 487de109-e7c3-3b18-8cff-0c5295cf7fd7 | -11.87879 | -56.41659 | 2024-10-23 04:53:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6c56d636-03f5-3d5f-9c88-55d3f5ef2b6a | -11.87529 | -56.41599 | 2024-10-23 04:53:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 29413f05-4380-3453-8563-639ee65f6ed2 | -11.87464 | -56.41993 | 2024-10-23 04:53:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 96ba378d-7225-309f-9ce7-d649377f7e13 | -13.44191 | -56.93413 | 2024-10-23 04:53:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 31889335-460f-3b9d-97c6-261894c72183 | -14.4167 | -56.21177 | 2024-10-23 04:53:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b22a35b6-77eb-36fb-b919-b72152ffbd51 | -9.35627 | -57.6012 | 2024-10-23 04:53:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a1df94ac-3e3c-303c-91f1-8f0c014e4bc1 | -9.35548 | -57.60598 | 2024-10-23 04:53:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7486c43e-3b36-34a5-b493-651f4b8cb901 | -9.35514 | -57.59925 | 2024-10-23 04:53:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a7bcde79-aae9-3ea4-92f8-8e5e5fea78d4 | -9.35431 | -57.60404 | 2024-10-23 04:53:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| de11e25e-e53c-3fdb-b52c-17510f04ef9d | -9.35164 | -57.60533 | 2024-10-23 04:53:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 55997894-ee52-3bca-8eb3-934838194373 | -9.24466 | -57.60732 | 2024-10-23 04:53:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 30c99fc8-24fc-3eca-b448-445ebce32863 | -9.24307 | -57.60455 | 2024-10-23 04:53:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 8852985c-0cf6-30c1-b173-142536174ae4 | -9.24082 | -57.60664 | 2024-10-23 04:53:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 89f8a934-cc57-3a62-b0f7-c2bb0781a54c | -9.17892 | -57.63309 | 2024-10-23 04:53:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fbd46f23-ae87-3f7a-8609-2b94bb5ac8a5 | -10.58613 | -57.79953 | 2024-10-23 04:53:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3b125626-8182-3338-8eb8-1a4e998c6714 | -10.5823 | -57.79895 | 2024-10-23 04:53:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f114070b-52ab-37de-9cfa-aad7638c5d31 | -10.46786 | -57.76244 | 2024-10-23 04:53:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 332c320e-95e7-34e4-a4c8-6044f65a7849 | -10.46 | -57.46854 | 2024-10-23 04:53:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c261bc07-1ec3-3aba-b31d-097e635fcf98 | -10.45938 | -57.4658 | 2024-10-23 04:53:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 20116544-b3d1-32f8-88df-4d3806ca6438 | -10.258 | -58.21021 | 2024-10-23 04:53:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e405c1d7-5c58-300f-99c3-cd89abddcf8f | -10.18386 | -57.91706 | 2024-10-23 04:53:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cafdc0f4-8666-3d00-b819-d7c4e41b3b5f | -10.1093 | -58.01852 | 2024-10-23 04:53:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 89f09525-abdc-3078-8b0a-177e535447a2 | -10.10844 | -58.02354 | 2024-10-23 04:53:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 75d8661e-a601-3eb9-90d2-b0b39e3e7c3b | -11.72172 | -57.43712 | 2024-10-23 04:53:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3f820541-d10b-3dbb-9dc9-3ccf429c3914 | -11.44715 | -57.76958 | 2024-10-23 04:53:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 49747bcc-d781-31cd-8d2a-6404f8d7799e | -10.92585 | -57.54165 | 2024-10-23 04:53:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 3628484b-45e0-35eb-9100-b6fea8e3e4c2 | -10.68018 | -58.74625 | 2024-10-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5127e055-c03b-3558-9c8e-7eccf1a3fd41 | -10.67954 | -58.74981 | 2024-10-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bf451d46-b5ad-3923-a352-764a8512a782 | -10.67933 | -58.74615 | 2024-10-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cf3d430a-fc59-3f53-933b-6eb476972f4e | -10.67891 | -58.75338 | 2024-10-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8c06aa2c-9a7b-3525-b8b6-8739365a5fe7 | -10.67872 | -58.74972 | 2024-10-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5446205e-5ba3-365d-b596-6336b48bd7c6 | -10.67811 | -58.7533 | 2024-10-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c1e1ebc5-788a-3ea7-aa20-c8831daf06a7 | -10.67677 | -58.74201 | 2024-10-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 12b8ade6-bde0-3a58-9ac3-44cf86317e02 | -10.67613 | -58.74558 | 2024-10-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c688ba81-01c2-3f43-990f-d06056a34621 | -10.67589 | -58.74191 | 2024-10-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2ed34e10-b53e-3f88-b0ee-a43fd50b2f83 | -10.6755 | -58.74914 | 2024-10-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README45.md)

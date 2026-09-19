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

## Dados Diários - Página 90

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dfe2d7da-4e78-31e3-a4fc-e47af57cd58d | -13.38853 | -48.03957 | 2026-09-19 04:59:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 11763913-50bb-3967-916d-ca302ddd3b02 | -15.05832 | -48.58904 | 2026-09-19 04:59:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 68a3c613-4f22-33bd-9f14-b67b8fdef107 | -14.93643 | -49.93693 | 2026-09-19 04:59:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 361a141b-72cd-3a7c-8493-9fd13d867166 | -10.92388 | -53.97609 | 2026-09-19 04:59:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 57a6fde5-6088-3fe9-9605-a7d67083d414 | -13.00848 | -46.96686 | 2026-09-19 04:59:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 730c4b5e-2b49-3db7-872c-a7debabbf23a | -14.5133 | -49.61197 | 2026-09-19 04:59:00 | NOAA-20 | SANTA TEREZINHA DE GOIÁS | GOIÁS | Brasil | 5219704 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c136d87b-8269-31e2-b2fa-151d0185e68c | -12.9813 | -46.97628 | 2026-09-19 04:59:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 001f879f-43b2-37e4-b52e-74e20bb933be | -13.61595 | -46.9708 | 2026-09-19 04:59:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0dd404ee-5f9d-3641-9db1-1a147dfc0247 | -12.28528 | -49.17054 | 2026-09-19 04:59:00 | NOAA-20 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 10a93fe0-0b93-3ca6-8f77-cbd18e0f3200 | -13.30254 | -51.64495 | 2026-09-19 04:59:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 16585f74-6205-3953-a331-916a6857f310 | -11.27762 | -54.12334 | 2026-09-19 04:59:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6559b1c0-b7a9-300b-bcb7-a70441c7ec7a | -13.74101 | -48.79512 | 2026-09-19 04:59:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| eb2aa881-1eb0-35dd-9456-635113818c47 | -10.71063 | -60.73823 | 2026-09-19 04:59:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2b173e25-b72e-38c4-a5b6-ff02f175580b | -13.62247 | -48.29939 | 2026-09-19 04:59:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8171354c-2e10-38ce-a55c-1cfbe4ea4d3b | -11.24398 | -54.09987 | 2026-09-19 04:59:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d7bf31ed-b726-3668-976c-7b2aa950bbd2 | -10.71145 | -60.73357 | 2026-09-19 04:59:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 053582c8-5a8b-377a-a32a-a6185d8c1ed8 | -10.71338 | -60.72727 | 2026-09-19 04:59:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 298082b9-7e1d-30ac-8f67-2ea245680216 | -12.59448 | -50.88438 | 2026-09-19 04:59:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| fa81f589-5adc-3648-8351-a10eb6142f8b | -12.33577 | -50.71339 | 2026-09-19 04:59:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5a585b05-ab0a-3f3e-9a6b-419bbc9f5a36 | -11.90954 | -50.11689 | 2026-09-19 04:59:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 51cf8dd5-e832-3a6b-bcf4-8bd131829f53 | -14.12807 | -45.55583 | 2026-09-19 04:59:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c47aa106-1875-3588-ba34-7b49ee31ecdc | -14.16887 | -47.84861 | 2026-09-19 04:59:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 24bb551e-fd66-3a3e-8247-8cd679a72c88 | -13.60844 | -48.30552 | 2026-09-19 04:59:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ca14524e-3565-3940-879b-89622e4c8d08 | -10.86542 | -54.00247 | 2026-09-19 04:59:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 217e30fc-7af1-3675-a051-55881e080a5d | -10.88457 | -54.07379 | 2026-09-19 04:59:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8bea3523-f6eb-3735-9299-ab6866970757 | -14.15932 | -45.17215 | 2026-09-19 04:59:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7b9ad8c1-32ba-3526-9174-9fb7c948d1a2 | -10.88798 | -53.98821 | 2026-09-19 04:59:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a0f2a84c-6dd1-3348-8bb1-c6d92fb4e6b8 | -11.27099 | -54.12225 | 2026-09-19 04:59:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 52d5b9bd-a4a0-3938-8921-7be20b161617 | -13.87752 | -48.60915 | 2026-09-19 04:59:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 19095992-1df0-3df7-887e-7ae974623be9 | -12.70373 | -45.94954 | 2026-09-19 04:59:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c00c3032-2a26-30c5-9460-9365dddb7b91 | -10.43649 | -54.45427 | 2026-09-19 04:59:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fcd9597e-d0eb-325c-b3df-e23660b4a32b | -13.01732 | -46.93512 | 2026-09-19 04:59:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| cb0e5612-7e26-3407-a097-4325f547bb62 | -16.30894 | -53.85686 | 2026-09-19 04:59:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d94b568b-653a-3cb4-8dad-d5145d773572 | -10.93384 | -53.95615 | 2026-09-19 04:59:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1099a9a7-4560-3889-a77d-56fc38a1d395 | -13.62226 | -46.95949 | 2026-09-19 04:59:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 601b7290-1512-386f-a122-9d55c635ba98 | -11.41747 | -51.45129 | 2026-09-19 04:59:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2000f7e1-465c-31c4-ba3d-f0e7f57ba9e1 | -10.86599 | -56.18433 | 2026-09-19 04:59:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 44dcb974-24c9-346b-b1a8-a7629832cb55 | -12.28176 | -49.16645 | 2026-09-19 04:59:00 | NOAA-20 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| e67d7997-98fb-3ffb-845b-d1068680d555 | -12.12261 | -47.00211 | 2026-09-19 04:59:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 92052d77-28af-31e8-9a01-02ac58f4c840 | -12.20011 | -52.86909 | 2026-09-19 04:59:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6f0d022e-7098-358d-98ab-9ea6a7245d84 | -12.14036 | -47.0104 | 2026-09-19 04:59:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cf1e6f34-e457-3278-9de2-5c5dfd990ff9 | -10.86873 | -54.00301 | 2026-09-19 04:59:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 07fb47b0-e4e3-319a-b051-4b3d83be043f | -14.79434 | -48.57859 | 2026-09-19 04:59:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d8ccac73-4b87-3dff-9f21-17007549289c | -11.94284 | -55.91526 | 2026-09-19 04:59:00 | NOAA-20 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ca5e25e7-59a5-3c9f-9284-88b737ec30d1 | -12.86091 | -46.34316 | 2026-09-19 04:59:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 6a179a33-a763-3850-a542-112b5445030c | -17.3185 | -46.62662 | 2026-09-19 04:59:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 78be5899-d373-30b2-8114-032468eeec99 | -12.12788 | -47.00589 | 2026-09-19 04:59:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c613a5a8-29d3-3d74-91a6-51b4ecbc06bc | -10.70692 | -60.73272 | 2026-09-19 04:59:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 1bf12e59-4ca3-3566-bcec-9e6e8ec66420 | -12.5893 | -49.09773 | 2026-09-19 04:59:00 | NOAA-20 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| d35f0bde-bd46-3359-8790-04cf44938888 | -11.06141 | -49.76078 | 2026-09-19 04:59:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 82b7ce32-6661-310d-bbb3-577571f7d90c | -10.70155 | -60.73653 | 2026-09-19 04:59:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 13299331-9d73-3113-9cc5-e1cf75fb9d4c | -11.91331 | -50.11745 | 2026-09-19 04:59:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2e31dc5d-b12b-3dcf-b6e1-dd21d13b2c5b | -12.34869 | -50.70193 | 2026-09-19 04:59:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| b942ceb7-70b2-36c5-8e2f-48ab5b338c30 | -12.70408 | -45.94667 | 2026-09-19 04:59:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7792d6dc-b5cd-3045-809b-8c91dec419ec | -13.62457 | -48.31655 | 2026-09-19 04:59:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fef8c1a3-9fe9-313c-a88b-2b8277e86dd3 | -10.85925 | -56.20319 | 2026-09-19 04:59:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 98f827a6-dab7-3c3f-8fb0-50acc9aaa165 | -12.58525 | -49.09716 | 2026-09-19 04:59:00 | NOAA-20 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| bbd60529-63e3-3ce5-a0f5-243081148f67 | -14.81773 | -48.56819 | 2026-09-19 04:59:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cf01dcb1-682f-3016-ab9a-1fcceaf210c5 | -11.06452 | -49.76605 | 2026-09-19 04:59:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 78d2c3e5-a71a-3e26-9981-1415d01af0e3 | -13.62566 | -48.30841 | 2026-09-19 04:59:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d5a90497-9b26-3d45-93c6-515c9ccca972 | -14.15663 | -45.1724 | 2026-09-19 04:59:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0a0e349f-0e17-3689-b7c1-90be2ef05b8b | -16.83162 | -47.64448 | 2026-09-19 04:59:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fb64330f-5afe-336a-89ca-bd47e20d25c7 | -14.95872 | -47.5337 | 2026-09-19 04:59:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3982f460-4124-3bc0-bc11-bcf1ad49d109 | -12.33385 | -50.72645 | 2026-09-19 04:59:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| d1cc9b06-fc58-3e4f-be70-b36635c7da22 | -14.81603 | -48.56285 | 2026-09-19 04:59:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 79781405-b966-3732-ace3-c375d7dff972 | -11.82897 | -46.8348 | 2026-09-19 04:59:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e7a9f8b9-2909-374b-9c1b-5f5930108978 | -15.02889 | -48.56459 | 2026-09-19 04:59:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 138b2a00-5a7c-39f7-a685-72d178544bbc | -11.55825 | -46.89875 | 2026-09-19 04:59:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d2a6bc3e-9ac8-3641-bdab-d54ca2b086ab | -12.6917 | -45.96441 | 2026-09-19 04:59:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c22158a3-d6ce-33fe-ac31-e5e820fcd850 | -12.34805 | -50.7063 | 2026-09-19 04:59:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| dcf13584-f19d-34c8-b21b-c5da60e0a4cd | -11.24729 | -54.10041 | 2026-09-19 04:59:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eed87c69-d7f4-304a-8b94-64793a7ae117 | -15.58572 | -56.55701 | 2026-09-19 04:59:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 55721b65-866d-3a4e-ab56-a367614c4fb5 | -12.12576 | -46.97766 | 2026-09-19 04:59:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0fbb78c3-1e3b-371c-8138-3e9d0970b64d | -13.62835 | -48.32117 | 2026-09-19 04:59:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9e430a2d-9aef-3870-8143-2ac996df3d55 | -11.90889 | -50.12151 | 2026-09-19 04:59:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 7907707c-46a6-3477-b5ba-09b55e0fb5d2 | -10.85861 | -56.20704 | 2026-09-19 04:59:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 39e30d4b-8334-3bcd-af79-f00f8f247b05 | -9.38885 | -60.35299 | 2026-09-19 04:59:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e839809b-7bda-3bb2-81c7-a95b53781350 | -13.00788 | -46.97155 | 2026-09-19 04:59:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a08c9d14-ae52-39c4-afe5-551168332192 | -13.609 | -48.30127 | 2026-09-19 04:59:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d3449e79-7c77-351b-b197-eeae12ee1e96 | -12.13519 | -47.01398 | 2026-09-19 04:59:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d7e82351-622d-30a4-965b-e27f57b1a89c | -12.02031 | -55.548 | 2026-09-19 04:59:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| be369b13-d112-3fce-a064-86094f56ac46 | -10.88792 | -54.05279 | 2026-09-19 04:59:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 338a7b4d-9234-392d-9b73-034ea8e8e634 | -11.19551 | -55.03581 | 2026-09-19 04:59:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 95828e95-185d-3055-81ac-17990cdde443 | -12.13256 | -46.9717 | 2026-09-19 04:59:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a0d7108e-158b-39fc-b8fb-a0f31b10e2b1 | -12.33943 | -50.71394 | 2026-09-19 04:59:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e0033192-d1b6-3690-a59d-bf0993c31315 | -13.02107 | -48.64032 | 2026-09-19 04:59:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9ee0ebba-4d66-3022-a954-661dc5c9ac1d | -12.53944 | -47.09632 | 2026-09-19 04:59:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| a6e91ac6-13b6-321a-89b6-b39e3d86a49b | -11.81921 | -46.86117 | 2026-09-19 04:59:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4027d690-d3b0-3f21-b02a-136859d238a0 | -11.02152 | -54.13168 | 2026-09-19 04:59:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 217188f9-9de8-30e0-96d6-79967a6a0ee8 | -11.14358 | -54.02575 | 2026-09-19 04:59:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5e51987e-59ce-3ff5-bc89-12dce4f9726a | -10.89129 | -53.98875 | 2026-09-19 04:59:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 32f90ca5-5208-3b82-9010-ae52e4fff3b9 | -14.67763 | -46.65597 | 2026-09-19 04:59:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1e58330c-1204-3a96-ab17-099c5d28d724 | -15.45431 | -52.82048 | 2026-09-19 04:59:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5f787ef8-b082-3761-bdd7-7acc41612a05 | -10.86426 | -56.216 | 2026-09-19 04:59:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 90392263-4f81-31ec-8280-2d2c269e55df | -11.29869 | -54.88048 | 2026-09-19 04:59:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 87695315-467f-3a52-bbce-b61bc7aa4638 | -11.81629 | -46.85818 | 2026-09-19 04:59:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 95180fc3-077f-3b47-aeb1-c6a3585bad8e | -12.1291 | -46.98829 | 2026-09-19 04:59:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 236ce3c1-644e-3aa3-ad3a-448208fe0a49 | -13.00616 | -46.98504 | 2026-09-19 04:59:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 67d76632-e764-37c2-9645-67ad1dcd9233 | -10.92001 | -53.97905 | 2026-09-19 04:59:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 65e9cd66-4384-3994-b76c-faca25053fe7 | -14.92529 | -49.92987 | 2026-09-19 04:59:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |


[Clique aqui para ver as próximas entradas](README91.md)

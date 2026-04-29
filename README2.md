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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d1b714ce-4e3c-34ee-ac18-59232565167c | -11.65038 | -48.10025 | 2026-04-29 04:36:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ad012ab6-ba27-3658-82ea-8f6106cdf7e6 | -12.44297 | -44.75711 | 2026-04-29 04:36:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fc152c36-ca96-3a14-aeb1-613bac18ba42 | -8.57603 | -44.09981 | 2026-04-29 04:36:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 15a469c7-5bf4-3872-a80e-226ccf4e37cd | -8.1523 | -46.6441 | 2026-04-29 04:36:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3fe98e6b-0282-3d0a-b9b9-394d1738a6f1 | -12.83861 | -43.81373 | 2026-04-29 04:36:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7d07461a-87a7-32b1-8bba-1abc3fd9cc22 | -13.68438 | -44.29457 | 2026-04-29 04:36:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a259a1a3-ed64-3399-8691-1344c471ff4e | -8.57533 | -44.10458 | 2026-04-29 04:36:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 61d8e55d-0494-308e-a644-c4886115b2e8 | -11.94283 | -58.08479 | 2026-04-29 04:36:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a356afd6-3957-345b-8b0c-c2ac9759c98e | -11.13276 | -45.13506 | 2026-04-29 04:36:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0589d46d-377a-3be1-a5d6-1d1b4a5168ca | -8.15569 | -46.64463 | 2026-04-29 04:36:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a05125fc-2913-3e96-bea8-97fefa80b2a8 | -8.15286 | -46.64046 | 2026-04-29 04:36:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0907cd0e-fda5-3546-9e9b-bd85cd28f062 | -10.60598 | -44.9603 | 2026-04-29 04:36:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 771e2d57-dd38-3861-ad30-d7dd938f97b2 | -13.44947 | -46.6903 | 2026-04-29 04:36:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a1eeb34d-31d1-3f87-b4f3-c7f2bba855a9 | -12.66255 | -46.63868 | 2026-04-29 04:36:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3a9e2e69-8e5d-31f3-8759-722d693680f2 | -12.84275 | -43.81432 | 2026-04-29 04:36:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 261bcaa1-123f-351b-af31-0ada6f902e7c | -12.54935 | -54.61685 | 2026-04-29 04:36:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0f717312-3586-32f7-b14b-187d48921a16 | -11.53648 | -49.1735 | 2026-04-29 04:36:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9bb76840-f564-3840-8b71-ea6028efe0a2 | -11.94223 | -58.08799 | 2026-04-29 04:36:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3aed8d65-c789-384d-a4ec-01b1b4acdc69 | -12.83809 | -43.81756 | 2026-04-29 04:36:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f6c973e0-81f1-3cec-aee2-7dc343bd35e3 | -12.83343 | -43.8208 | 2026-04-29 04:36:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9017fe8f-6487-356b-8526-171b0e4ad533 | -12.44378 | -44.75926 | 2026-04-29 04:36:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fbcacadc-234b-3ac4-ad67-f88c83f2fa24 | -13.6852 | -44.29096 | 2026-04-29 04:36:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 088e3d7a-9b00-33ab-837d-8c4b6b1c2ed7 | -11.1321 | -45.13961 | 2026-04-29 04:36:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2dcc7cdb-4627-3651-8fea-b3fad2aa02c6 | -12.68292 | -43.82697 | 2026-04-29 04:36:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 266d742f-2c1f-3214-897e-ea605051ed57 | -12.6788 | -43.82637 | 2026-04-29 04:36:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 585b1751-414b-3059-9caf-9d88d15e5464 | -8.15852 | -46.6488 | 2026-04-29 04:36:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8e1ea866-e16a-3f54-b2ea-23013a8cffc6 | -14.05563 | -44.08983 | 2026-04-29 04:36:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| aeb54810-6f3c-3f2d-93ed-6e236f970b4b | -16.67022 | -41.84696 | 2026-04-29 04:38:00 | NOAA-20 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 8245130f-9bae-3010-b741-14a237d3fecf | -18.00772 | -48.17833 | 2026-04-29 04:38:00 | NOAA-20 | GOIANDIRA | GOIÁS | Brasil | 5208509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bda1c52b-6448-3dc7-9f3e-3d021a3080c2 | -14.47688 | -46.99407 | 2026-04-29 04:38:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 78659c00-42c5-30a8-9bb0-907dab67e5eb | -21.046 | -48.66741 | 2026-04-29 04:38:00 | NOAA-20 | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 98d35776-cead-3c4b-bbad-7693ce034c51 | -20.6034 | -49.75642 | 2026-04-29 04:38:00 | NOAA-20 | TANABI | SÃO PAULO | Brasil | 3553401 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2f6719c1-6f39-3af5-aa32-17e01ca336b4 | -18.03463 | -53.0317 | 2026-04-29 04:38:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4816e456-84b2-388a-af72-73596927f6ad | -17.22345 | -44.30619 | 2026-04-29 04:38:00 | NOAA-20 | CLARO DOS POÇÕES | MINAS GERAIS | Brasil | 3116506 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 275808df-4494-3f7d-8947-d1b9442e4bfb | -16.67404 | -49.49247 | 2026-04-29 04:38:00 | NOAA-20 | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 108c077b-2745-362b-b7da-ac08b4339afb | -21.09884 | -48.49987 | 2026-04-29 04:38:00 | NOAA-20 | TAIAÇU | SÃO PAULO | Brasil | 3553104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 6d685e6c-3daa-3f60-8e39-80224c3589b7 | -15.79462 | -41.33992 | 2026-04-29 04:38:00 | NOAA-20 | DIVISA ALEGRE | MINAS GERAIS | Brasil | 3122355 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| b8c7eb64-34ce-30ad-9f2f-33211d41dfc9 | -16.67048 | -41.84778 | 2026-04-29 04:38:00 | NOAA-20 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 40c8f39a-21d1-3fbd-9839-01265ab20fe6 | -19.74014 | -43.99342 | 2026-04-29 04:38:00 | NOAA-20 | VESPASIANO | MINAS GERAIS | Brasil | 3171204 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fbd1d1e0-814f-328a-b910-fae328eea196 | -21.0495 | -48.66799 | 2026-04-29 04:38:00 | NOAA-20 | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| c94ca079-06e8-3e8b-8709-77d8539a9706 | -17.49405 | -48.01286 | 2026-04-29 04:38:00 | NOAA-20 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 598a312c-76a2-3bac-8780-be000faa191e | -17.22771 | -44.30679 | 2026-04-29 04:38:00 | NOAA-20 | CLARO DOS POÇÕES | MINAS GERAIS | Brasil | 3116506 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7ae2e695-1c6c-3c9c-8ce0-be5e58e594c4 | -14.79008 | -42.81025 | 2026-04-29 04:38:00 | NOAA-20 | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 58efe5d9-34ad-3e35-8da4-47cd68ef80ec | -15.89071 | -43.46988 | 2026-04-29 04:38:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ed905204-27dd-3f96-84a8-9dd50b8376ef | -19.74187 | -43.99612 | 2026-04-29 04:38:00 | NOAA-20 | RIBEIRÃO DAS NEVES | MINAS GERAIS | Brasil | 3154606 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 70563490-0092-3fb1-a2d1-1e98db010a3b | -14.71857 | -46.5983 | 2026-04-29 04:38:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ff9ab901-d7d1-354b-b1b9-b9dd443225d2 | -18.03185 | -53.02703 | 2026-04-29 04:38:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7b6493b4-2703-345a-b5c0-96c81ae8df0b | -16.6085 | -43.37098 | 2026-04-29 04:38:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 85918828-95be-36e5-ba05-c3434568a211 | -18.39726 | -51.43112 | 2026-04-29 04:38:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6634f538-3cc8-366b-b171-f248cc3142b7 | -18.39999 | -51.43537 | 2026-04-29 04:38:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 00b32647-0ff3-3e15-a960-a1b6a75440b5 | -16.67793 | -49.48941 | 2026-04-29 04:38:00 | NOAA-20 | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ebae8b79-7fda-3440-a3e8-60b0e5ef0356 | -14.47395 | -46.9895 | 2026-04-29 04:38:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 27337dd2-367a-3458-91d7-adc3b6acb152 | -18.40059 | -51.43171 | 2026-04-29 04:38:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7ef3734e-99bf-3029-bbe4-8e73903808af | -18.93234 | -48.06647 | 2026-04-29 04:38:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| df4fd42f-e5f3-3f47-bc87-5571ea27fa33 | -16.61049 | -43.37315 | 2026-04-29 04:38:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 32c3a61b-cefe-30c2-87f6-e6b560fd6faf | -14.47748 | -46.99003 | 2026-04-29 04:38:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 17e1842d-b702-347a-8aa9-04db89ccc967 | -15.88685 | -43.46484 | 2026-04-29 04:38:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5cd07677-c9c6-33c5-91ba-14a2b4bd8895 | -18.02906 | -53.02235 | 2026-04-29 04:38:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4af8d697-46f5-3a67-8648-24545aa53217 | -17.50798 | -44.73836 | 2026-04-29 04:38:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a0a297d9-aac9-3519-a885-ded2090f6aa3 | -20.21458 | -46.47483 | 2026-04-29 04:38:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e9463fae-03ed-342d-9be9-6f2cc4b57fb6 | -19.31538 | -40.05605 | 2026-04-29 04:38:00 | NOAA-20 | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 7395c977-5772-3fb4-a01b-22c407f77304 | -16.03247 | -49.84053 | 2026-04-29 04:38:00 | NOAA-20 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a356149e-9afb-3ed4-aef0-1f2adfc65209 | -20.21979 | -46.46513 | 2026-04-29 04:38:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 56124ad3-6fdb-392c-a046-2de9284bf552 | -16.67736 | -49.49303 | 2026-04-29 04:38:00 | NOAA-20 | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 914a008a-f612-3ad8-888c-67af7a8791ca | -15.21875 | -57.65678 | 2026-04-29 04:38:00 | NOAA-20 | LAMBARI D'OESTE | MATO GROSSO | Brasil | 5105234 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5d175463-5431-35f0-abee-b45505659ae5 | -15.89127 | -43.46545 | 2026-04-29 04:38:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0833ccbd-22bf-36e8-8b87-2eab351b3fa8 | -16.606 | -43.37251 | 2026-04-29 04:38:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c0322ff6-29ff-3989-9de5-739bff77827e | -17.55072 | -39.78324 | 2026-04-29 04:38:00 | NOAA-20 | TEIXEIRA DE FREITAS | BAHIA | Brasil | 2931350 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| d7982151-bb64-39a8-a6c4-d92135386dd9 | -20.60734 | -49.75317 | 2026-04-29 04:38:00 | NOAA-20 | TANABI | SÃO PAULO | Brasil | 3553401 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f6fc74d9-a5af-3b90-9aed-c068a4b821af | -15.79426 | -41.343 | 2026-04-29 04:38:00 | NOAA-20 | DIVISA ALEGRE | MINAS GERAIS | Brasil | 3122355 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 6a18355c-7824-3137-a4b4-8cb86dfffea4 | -14.71556 | -46.5937 | 2026-04-29 04:38:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 50601a38-278f-3190-8c78-794836fee26f | -20.60677 | -49.75698 | 2026-04-29 04:38:00 | NOAA-20 | TANABI | SÃO PAULO | Brasil | 3553401 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b7c7ccf5-0838-3f39-940f-e44e3e56f0c6 | -14.71916 | -46.5942 | 2026-04-29 04:38:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2c25f4f0-8cce-3f43-9129-419c2de21682 | -18.29093 | -54.60648 | 2026-04-29 04:38:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4c281c09-3749-39a3-8f58-ceff7027bc4e | -20.21845 | -46.47538 | 2026-04-29 04:38:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d34e2e05-f834-34db-b3fb-21b9e132fdaf | -18.788 | -51.93358 | 2026-04-29 04:38:00 | NOAA-20 | APORÉ | GOIÁS | Brasil | 5201504 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4dce5cb4-f813-3283-abf3-01a26ade7240 | -20.21525 | -46.46967 | 2026-04-29 04:38:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c20fb79e-1244-3d86-8c60-8f0db90d8a93 | -18.03254 | -53.023 | 2026-04-29 04:38:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| aa00c485-9030-3df7-a78e-d6b270a4bd0b | -21.0501 | -48.66383 | 2026-04-29 04:38:00 | NOAA-20 | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 73ff7ead-8051-3f89-9875-29449d9679a4 | -19.31476 | -40.05696 | 2026-04-29 04:38:00 | NOAA-20 | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 40767290-6f2a-36da-b259-3d6417fabb89 | -20.21592 | -46.46452 | 2026-04-29 04:38:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 638bdf7d-522f-30f9-b8bd-d1fc46b336bc | -16.03304 | -49.83695 | 2026-04-29 04:38:00 | NOAA-20 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ca19d957-f7d2-32fb-a54e-12017858b7eb | -21.7072 | -48.42771 | 2026-04-29 04:40:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1f255f87-b179-3fb2-900b-496d7fddf1ba | -21.8455 | -50.55982 | 2026-04-29 04:40:00 | NOAA-20 | TUPÃ | SÃO PAULO | Brasil | 3555000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| fab356fa-ebe3-349b-a33b-76e441449d21 | -21.70364 | -48.42719 | 2026-04-29 04:40:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 050e28ef-dd3e-3b06-a7a1-42da5be8da89 | -21.70424 | -48.42284 | 2026-04-29 04:40:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4ea3685e-d5ca-3643-a0ee-cee4a9eef96e | -21.9952 | -45.67527 | 2026-04-29 04:40:00 | NOAA-20 | CAREAÇU | MINAS GERAIS | Brasil | 3113602 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| b7fcc94f-5dc6-3653-adca-ddeb726bc872 | 3.45862 | -59.95358 | 2026-04-29 05:23:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 283a3dcc-7ab4-3be3-ae33-f8adea618584 | 1.86165 | -60.45327 | 2026-04-29 05:23:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0355bcaf-9d54-3d41-9965-90adfa6d2143 | 1.82205 | -60.87273 | 2026-04-29 05:23:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 08b7eb7f-4af6-39c4-ba65-a8b35f5f002f | 1.94449 | -60.37689 | 2026-04-29 05:23:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bf21feda-a4a4-3d58-9390-14030b94f4fd | 1.3153 | -60.84395 | 2026-04-29 05:23:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 09854b55-a679-3000-ba61-621abbec8b49 | 1.01817 | -60.60371 | 2026-04-29 05:23:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 18bfae60-e28a-300f-95a5-51f6c436a178 | 1.94506 | -60.38054 | 2026-04-29 05:23:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 31a742a6-5bc9-3d8d-8a51-db903bbd75b3 | -2.73812 | -58.19477 | 2026-04-29 05:23:00 | NOAA-21 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1d9328ee-6c9e-3a8c-b8e9-6553de69bdec | 1.82146 | -60.86893 | 2026-04-29 05:23:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3126c6d8-46be-3ec7-bc0f-00d5781ef324 | -6.27312 | -57.90765 | 2026-04-29 05:23:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 94e76015-c9d1-3e0e-86f2-aca743f5cdd5 | -15.22267 | -57.6562 | 2026-04-29 05:25:00 | NOAA-21 | LAMBARI D'OESTE | MATO GROSSO | Brasil | 5105234 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 42b379e5-0ab4-3f8e-8ae4-e0f7f2a59551 | -16.25685 | -60.03294 | 2026-04-29 05:25:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| cdd1132d-b52b-3434-87f5-b835f2f60b7d | -16.41792 | -54.91989 | 2026-04-29 05:25:00 | NOAA-21 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README3.md)

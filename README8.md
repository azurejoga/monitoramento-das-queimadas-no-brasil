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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 48f0f1eb-b56f-3c8a-88cd-b8e571a7c1d5 | -4.38306 | -41.91873 | 2025-06-29 03:42:00 | NOAA-21 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| dc43cc25-e395-3eb5-9b6d-09957e5163cd | -3.77738 | -41.68134 | 2025-06-29 03:42:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| cc09013a-b903-3f2b-97f4-e5ef5f111dc4 | -7.18973 | -43.70186 | 2025-06-29 03:42:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0d655a8f-f8d0-3fe6-8501-5c7b7e7eeaea | -5.74846 | -46.25901 | 2025-06-29 03:42:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 64dfff96-fadf-376d-a080-10c6cf4710ca | -7.09442 | -43.65714 | 2025-06-29 03:42:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aeccf02b-2b19-3f6e-aa54-8b0eb5e6bce5 | -3.41855 | -43.16684 | 2025-06-29 03:42:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b0f2e772-41e4-343e-b5f0-b6e057873772 | -7.18924 | -43.70469 | 2025-06-29 03:42:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9675861f-3c6d-3486-a375-20dbe23ff99f | -6.62399 | -47.29002 | 2025-06-29 03:42:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 5bdef1ad-aee8-3a63-a376-f29e494cb12a | -6.62588 | -47.27974 | 2025-06-29 03:42:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 0c535433-0974-39c6-a6e6-eb987edf69ac | -7.19871 | -43.70924 | 2025-06-29 03:42:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 919ade2b-6f22-33c0-a4f3-6726bccd0a43 | -4.38423 | -41.91622 | 2025-06-29 03:42:00 | NOAA-21 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 02047500-c38a-3077-8fe6-0d9fd26a1d32 | -5.0621 | -43.25189 | 2025-06-29 03:42:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 417c4106-3994-3c76-b1b0-b2ae8a653dde | -7.4777 | -34.84217 | 2025-06-29 03:42:00 | NOAA-21 | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 47bff0d6-d998-3fe3-91cf-13812aa59277 | -3.77816 | -41.67665 | 2025-06-29 03:42:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d3888aa2-e0c5-30bd-b000-9fada4c4e5ef | -4.54476 | -48.0178 | 2025-06-29 03:42:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| bed0cf7e-4ddf-3d2f-969f-9b87a702321d | -5.57329 | -45.2196 | 2025-06-29 03:42:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9c6da148-7a3f-3b44-8973-70d8155d33ba | -4.56067 | -48.00746 | 2025-06-29 03:42:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 197b0c0c-f720-30e8-904f-f95e85f91007 | -6.62493 | -47.28489 | 2025-06-29 03:42:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 90c4f14a-f013-3c97-8ca7-dbad0d928bf6 | -7.10225 | -44.36486 | 2025-06-29 03:42:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 71b6441e-bb5a-394f-a233-1c5c72d592b6 | -6.44904 | -44.57195 | 2025-06-29 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2f556a5a-17c0-3d83-a719-d428f021ba1a | -6.63128 | -47.28588 | 2025-06-29 03:42:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 1b21a2a2-c109-3270-8b96-0f88776aeabb | -11.59207 | -44.6657 | 2025-06-29 03:45:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cd93d51f-b43e-3255-9625-597522a4de81 | -9.43077 | -47.95216 | 2025-06-29 03:45:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 28a7dceb-25b3-3ebe-98e1-729a0cd5df0b | -7.55048 | -45.84869 | 2025-06-29 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c64deb73-a106-3aa8-ac91-fafe53637fed | -9.98199 | -47.8009 | 2025-06-29 03:45:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2822e24c-6f04-3ff3-920c-ffaba8f5e7ab | -11.84555 | -43.80107 | 2025-06-29 03:45:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 22e74858-69d9-3e14-95cc-f15baf34d6ce | -10.92711 | -44.16034 | 2025-06-29 03:45:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ba6009a4-e8e3-3ba5-836e-10a9194556c3 | -12.21293 | -38.98281 | 2025-06-29 03:45:00 | NOAA-21 | FEIRA DE SANTANA | BAHIA | Brasil | 2910800 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 00e0ddb6-60e4-30b3-9ac2-49f6dc464cca | -11.84004 | -43.80515 | 2025-06-29 03:45:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c211771b-0b38-3bfa-998d-d66818a8e7f6 | -13.76514 | -40.52899 | 2025-06-29 03:45:00 | NOAA-21 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c4618965-1a74-332f-a344-f354cc7e8ec8 | -10.54311 | -42.53883 | 2025-06-29 03:45:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| b502a935-d920-3a7b-8065-300124a6d45e | -13.46079 | -47.38528 | 2025-06-29 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 271d1744-7749-3b6c-9250-28db6ef0c48d | -9.46752 | -40.34669 | 2025-06-29 03:45:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| a85e86a1-2355-3796-ac77-7f9c441b8fe6 | -11.63475 | -41.69846 | 2025-06-29 03:45:00 | NOAA-21 | CANARANA | BAHIA | Brasil | 2906204 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 15d3f576-797d-3425-88c4-ff661257bca3 | -10.97895 | -45.11654 | 2025-06-29 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 25.6 |
| 5f4a20ac-1727-3908-8db7-20096c84cbfc | -12.06073 | -48.47926 | 2025-06-29 03:45:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| e4477bde-abd3-3877-abb3-e09d94d924ad | -9.46834 | -40.34188 | 2025-06-29 03:45:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.6 |
| eac39eb3-9d83-3bbb-a695-d88adafb9735 | -9.27711 | -40.44381 | 2025-06-29 03:45:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ba936d76-cf57-312e-ad64-94e597ee8c3a | -13.69184 | -47.1349 | 2025-06-29 03:45:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 77a1954e-dd1d-3d94-82b0-b8ffe36ee367 | -9.14887 | -46.38423 | 2025-06-29 03:45:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| dceef92c-c156-370a-a9f8-4269772f53bb | -14.22048 | -45.51003 | 2025-06-29 03:45:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 263b611c-432c-32fe-b836-226aa48de726 | -12.04701 | -48.07904 | 2025-06-29 03:45:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a0e8a68c-8473-31b7-b787-b03cdbd3bc64 | -12.06305 | -48.47733 | 2025-06-29 03:45:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| a10939b6-246f-3de0-8b78-8b58a8767145 | -9.15606 | -40.99434 | 2025-06-29 03:45:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 511d2420-f139-3998-8ca0-74b758408f3b | -12.82229 | -38.41857 | 2025-06-29 03:45:00 | NOAA-21 | SIMÕES FILHO | BAHIA | Brasil | 2930709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 2e34ddc1-2c0d-38f8-aa69-6986fc7b9bad | -9.79213 | -48.56848 | 2025-06-29 03:45:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b2198602-0431-353b-9473-3525d8ddef28 | -10.97254 | -45.10944 | 2025-06-29 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| ca79ef16-b095-3d00-8161-779353890bcf | -12.05784 | -48.47105 | 2025-06-29 03:45:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 572db344-c466-3819-9003-6e434e9729e7 | -7.55908 | -45.83358 | 2025-06-29 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e44523ed-67f3-3e94-a81e-eecdab1447a5 | -7.55621 | -45.84952 | 2025-06-29 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b9322a34-571f-3e12-b498-882af7c60d66 | -9.97586 | -47.79948 | 2025-06-29 03:45:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1119116f-a253-3acc-a1c7-daafc58c6de0 | -12.18253 | -44.34145 | 2025-06-29 03:45:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 153d973d-ac59-3697-b704-b82a6e524856 | -14.21554 | -45.50901 | 2025-06-29 03:45:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b3b64a87-0459-34a1-babf-3b5edc08266d | -13.64651 | -46.81564 | 2025-06-29 03:45:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fd5e545c-6f5c-369a-b295-c67cae8ccb83 | -11.58027 | -44.83606 | 2025-06-29 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e46a2060-84cf-3b02-a416-cdc57c31e23b | -10.97382 | -45.11568 | 2025-06-29 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 736fcb83-4bc0-37c8-b3d3-0368af60c267 | -12.05684 | -48.4761 | 2025-06-29 03:45:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 9be18c5e-9027-36ab-9faf-ad9bbc95816e | -9.43362 | -47.95342 | 2025-06-29 03:45:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b1542efb-0fb1-3ee7-94ac-63c5400663f6 | -12.06177 | -48.47417 | 2025-06-29 03:45:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 19256db2-c9bb-37f0-9a0a-8f93542b9f02 | -8.9459 | -39.98133 | 2025-06-29 03:45:00 | NOAA-21 | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| abbb223b-f0b5-3af4-a53a-aa0787f00a61 | -9.46368 | -40.34605 | 2025-06-29 03:45:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| f686d190-2314-3166-bd7e-4758552fe7cb | -10.53876 | -42.53811 | 2025-06-29 03:45:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| ab06ac79-787f-3df4-a5a8-38b4d1427943 | -9.4645 | -40.34124 | 2025-06-29 03:45:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1e7ec5c8-cbd4-3d7f-a5f2-0b48fe311c9f | -12.12869 | -45.57371 | 2025-06-29 03:45:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 79c7131f-7d5f-3a57-a0de-18496a4a5bae | -9.42733 | -47.9522 | 2025-06-29 03:45:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d6cd8afc-92c2-3272-8087-83d4444607b7 | -10.92805 | -44.15507 | 2025-06-29 03:45:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f9c721b0-c75f-3a99-bdf9-b350edeee0a3 | -7.55266 | -45.83658 | 2025-06-29 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 428af09e-d8d1-3700-91e3-5037076f9ebe | -10.98014 | -45.11028 | 2025-06-29 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 15.5 |
| c89abe9f-fa4a-37e5-954f-bc0ba65f6105 | -10.92696 | -44.15691 | 2025-06-29 03:45:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 704ddb7e-79e5-3d9b-8346-2cdf49cdd488 | -9.14242 | -46.38697 | 2025-06-29 03:45:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4901a4ad-30a1-3d78-88e0-2082de3ea6d7 | -13.69248 | -47.13165 | 2025-06-29 03:45:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b7fd1519-468e-3147-a8a8-b97c90c3c894 | -9.79325 | -48.56287 | 2025-06-29 03:45:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 48d6247c-1567-3a76-abe7-58d234b2134c | -9.64738 | -48.78991 | 2025-06-29 03:45:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 02d304d6-476a-3f74-9491-2245f3d1bf28 | -7.55406 | -45.82886 | 2025-06-29 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b32bb155-7769-3c47-b8ce-63648e3b2f35 | -11.58082 | -44.83316 | 2025-06-29 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5f5415bb-dc99-39be-98bf-0fbb455f7101 | -10.97501 | -45.10942 | 2025-06-29 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 4d389c08-5885-39fb-8703-4c33ae832189 | -9.14807 | -46.38849 | 2025-06-29 03:45:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8346aea7-5897-342c-9d90-8820ca344039 | -10.97441 | -45.11258 | 2025-06-29 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.0 |
| decaa82c-ac78-3fd3-a31c-ce91c0ff43fe | -12.06406 | -48.47223 | 2025-06-29 03:45:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e21686d1-73ed-3702-925a-62a424786962 | -12.05555 | -48.47301 | 2025-06-29 03:45:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d7ffe9a4-9ba1-3d60-b403-97639a5d6459 | -7.55695 | -45.84543 | 2025-06-29 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b7cdf483-c768-3e88-b0e6-18d06cdc99a2 | -12.05452 | -48.47803 | 2025-06-29 03:45:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3e185ae5-1743-3506-a3c5-1340d7d1fcd4 | -7.55194 | -45.84059 | 2025-06-29 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 918cfce6-8699-329b-9b20-6550a1e2f320 | -12.76468 | -44.39999 | 2025-06-29 03:45:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 15f61239-9286-3b11-95f2-d6e9596a42ea | -10.97561 | -45.10624 | 2025-06-29 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.6 |
| cbcdd1fe-58b8-347f-876c-36a3788acae6 | -9.64627 | -48.7955 | 2025-06-29 03:45:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e9070a1a-77a6-33ad-b5f3-ecf454944076 | -12.12929 | -45.57058 | 2025-06-29 03:45:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 954cc570-df82-30af-924f-d3774facab56 | -12.04605 | -48.08378 | 2025-06-29 03:45:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ff66dbc7-b826-3d7a-9721-55375ba9df40 | -10.97954 | -45.11343 | 2025-06-29 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 25.6 |
| 9f18e0e5-81aa-38a3-995c-9476776cfd6d | -9.43702 | -47.95353 | 2025-06-29 03:45:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0056395c-03c1-3298-9de0-338021b7f891 | -9.15419 | -46.35596 | 2025-06-29 03:45:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| cc406494-cd95-3ce0-815f-e7a6fa16dac5 | -10.96511 | -40.88044 | 2025-06-29 03:45:00 | NOAA-21 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 970edf94-3658-34e3-8765-7864b23805cc | -10.95868 | -48.15277 | 2025-06-29 03:45:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d15e2d97-7e44-393e-b3d1-caf2279ab2ff | -10.94706 | -45.60041 | 2025-06-29 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b64da566-fbb5-3730-b1be-4aa37d0d0dc5 | -10.97196 | -45.1126 | 2025-06-29 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 0981da82-e468-3915-9351-c8ba5bd99161 | -11.59056 | -44.6638 | 2025-06-29 03:45:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f8bbc6fe-6846-3dc4-9c01-6c9b9d4d85cb | -12.1281 | -45.57685 | 2025-06-29 03:45:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a7cf0f39-b15f-343b-8c0c-5f8cb8e73763 | -7.56268 | -45.84626 | 2025-06-29 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dd9324b4-77b4-3863-9c83-c27b52844b52 | -11.57529 | -44.83516 | 2025-06-29 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5c7af699-d133-3685-8cab-77b8acb027ad | -22.90235 | -43.75219 | 2025-06-29 03:47:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |


[Clique aqui para ver as próximas entradas](README9.md)

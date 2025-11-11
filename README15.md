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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b42b347a-d517-3d9d-abe7-4ed89bf0114e | -16.69288 | -51.83713 | 2025-11-11 04:04:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5f424e76-98c4-3ba3-95bc-8eff32d58959 | -18.47323 | -53.4047 | 2025-11-11 04:04:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 9926492c-fe3a-34ce-bd22-72860cffe74e | -19.75578 | -58.02524 | 2025-11-11 04:04:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.2 |
| 8cb8fa84-4d02-34ba-847c-d24dd8f430be | -19.30844 | -50.50108 | 2025-11-11 04:04:00 | NOAA-20 | LIMEIRA DO OESTE | MINAS GERAIS | Brasil | 3138625 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 065d662e-d6c5-3471-9b19-dd603c0b0d2b | -18.38823 | -54.9831 | 2025-11-11 04:04:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9a8d0c1e-4f36-3e7e-8133-43020ef37b38 | -20.80789 | -49.83731 | 2025-11-11 04:04:00 | NOAA-20 | MONTE APRAZÍVEL | SÃO PAULO | Brasil | 3531407 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 6c7335a3-f398-326c-bbd8-f5b4e16cda07 | -19.78392 | -58.03337 | 2025-11-11 04:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 456240c8-fc95-3021-ae3a-989da8a2f979 | -27.75052 | -48.62106 | 2025-11-11 04:06:00 | NOAA-20 | PALHOÇA | SANTA CATARINA | Brasil | 4211900 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 7f5fa982-645e-30c8-a5fa-aa5922cd3e6f | -23.59656 | -49.01226 | 2025-11-11 04:06:00 | NOAA-20 | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9842241b-2632-3db5-9d72-70b7634b2fa1 | -22.67649 | -50.44455 | 2025-11-11 04:06:00 | NOAA-20 | ASSIS | SÃO PAULO | Brasil | 3504008 | 35 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 09943240-f742-31b0-8449-e6cffda43eee | -23.02555 | -47.49068 | 2025-11-11 04:06:00 | NOAA-20 | CAPIVARI | SÃO PAULO | Brasil | 3510401 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| b14a2e90-6dbc-399e-b838-1139b4e4d0d4 | -26.6111 | -53.16881 | 2025-11-11 04:06:00 | NOAA-20 | SANTA TEREZINHA DO PROGRESSO | SANTA CATARINA | Brasil | 4215687 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| c875eef0-ca7e-3669-b54d-1cd99dde26ae | -26.62393 | -51.84313 | 2025-11-11 04:06:00 | NOAA-20 | PASSOS MAIA | SANTA CATARINA | Brasil | 4212270 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| b3512461-b19a-320a-9df2-1e42c1bbefa5 | -19.8078 | -58.03929 | 2025-11-11 04:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| d21f8896-a8cd-3b9f-8246-3c4faa406432 | -22.89678 | -43.65624 | 2025-11-11 04:06:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 08cddc60-8ad6-3956-813d-cd16e15c8acd | -19.79799 | -58.03746 | 2025-11-11 04:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| ed1821ae-ed4f-396a-86d8-c1983d0efc4a | -22.5178 | -48.5544 | 2025-11-11 04:06:00 | NOAA-20 | IGARAÇU DO TIETÊ | SÃO PAULO | Brasil | 3520004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 5351eb8f-37eb-359c-85cb-904f81e2b0b4 | -26.69566 | -52.46796 | 2025-11-11 04:06:00 | NOAA-20 | IPUAÇU | SANTA CATARINA | Brasil | 4207684 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 5de12706-9df6-3601-af2f-46d066f5f400 | -19.81484 | -58.04129 | 2025-11-11 04:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 9a24320b-322e-3495-ae63-7939f45729df | -19.79373 | -58.03524 | 2025-11-11 04:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| deaebf60-f0a8-36e0-9f12-005c18a8d042 | -22.98053 | -47.23864 | 2025-11-11 04:06:00 | NOAA-20 | MONTE MOR | SÃO PAULO | Brasil | 3531803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 40575715-13cd-38a4-a216-9253e0c5a627 | -19.79096 | -58.03541 | 2025-11-11 04:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 80d183a1-5032-3b85-9dc7-feb7700e7a3b | -22.82801 | -47.14797 | 2025-11-11 04:06:00 | NOAA-20 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 364c507f-00b3-3982-aece-614212b7c2ae | -22.88964 | -43.2663 | 2025-11-11 04:06:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 669529b3-da71-396a-ac57-4258477c0884 | -22.38643 | -46.81495 | 2025-11-11 04:06:00 | NOAA-20 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b22b2f77-f692-3e19-bda0-58015f48133a | -29.77544 | -51.17984 | 2025-11-11 04:08:00 | NOAA-20 | SÃO LEOPOLDO | RIO GRANDE DO SUL | Brasil | 4318705 | 43 | 33 | nan | nan | nan | Pampa | 2.4 |
| 6f3d6b4c-9f6d-3e37-a635-aea739badb5b | -18.3827 | -54.9942 | 2025-11-11 04:10:00 | GOES-19 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 93e1a5c7-ca99-39a3-9539-f66572d6d79f | -18.474 | -53.4058 | 2025-11-11 04:20:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 83.9 |
| a9d0a17e-2eef-3a8c-ba26-a6f6f1160332 | -4.7204 | -46.4497 | 2025-11-11 04:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 21959374-cf7d-3435-a845-2a86fbeef90e | -4.7204 | -46.4497 | 2025-11-11 04:30:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 72.9 |
| e201b4e8-1be3-3507-b6ad-d85cb9d9a48a | -4.7204 | -46.4497 | 2025-11-11 04:40:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 3d6a2205-dbbf-3ea9-bdef-d448b7882409 | -4.7204 | -46.4497 | 2025-11-11 04:50:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 64.3 |
| fb60913a-6c56-3645-a6c4-76f82803e0b5 | -4.26875 | -45.96349 | 2025-11-11 04:50:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5e4bd5b3-cda1-37af-8e80-af25ec1cae4c | -6.09147 | -41.56582 | 2025-11-11 04:50:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 62e37b9a-04bd-3314-826a-53f51fab4715 | -5.60819 | -47.28106 | 2025-11-11 04:50:00 | NOAA-21 | DAVINÓPOLIS | MARANHÃO | Brasil | 2103752 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d73baa38-1d1d-317d-8b5d-c624b4bccced | -1.43241 | -51.51384 | 2025-11-11 04:50:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 93d049c3-a6e8-3f79-a0c4-040c1dd8482c | -2.43569 | -46.45332 | 2025-11-11 04:50:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 77032c5e-04cc-3aa7-8015-22a182221708 | -4.38602 | -49.65357 | 2025-11-11 04:50:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1f89aa12-c164-3db5-b880-150c59866464 | -3.39828 | -49.55916 | 2025-11-11 04:50:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 57c5462c-5115-3e9b-a843-f83031dee686 | -3.89826 | -52.28253 | 2025-11-11 04:50:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 07c5c60a-735d-3abe-aacf-637fb5139412 | -4.73759 | -49.53094 | 2025-11-11 04:50:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 60c921af-67dc-3421-a43f-cdc779e4dbf8 | -4.92259 | -50.00074 | 2025-11-11 04:50:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f13478d6-dc4c-3b4a-86d9-4ca7345a7d3b | 0.27825 | -50.31356 | 2025-11-11 04:50:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8d596245-3dec-33dd-ae76-a133090fd480 | -4.44733 | -49.24698 | 2025-11-11 04:50:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c3bc71f3-6e4d-3fc9-b248-ef71bdc9c7f8 | -2.49368 | -50.25312 | 2025-11-11 04:50:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 58d2a93c-8795-3de1-9d18-8c3ad2d65543 | -4.12444 | -52.07838 | 2025-11-11 04:50:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ab062c9c-bd40-3a16-9fdf-481d1f16e22b | -2.55311 | -48.39249 | 2025-11-11 04:50:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 14a05f23-a158-31c0-9a7a-d825b06eb80b | -6.44186 | -45.66349 | 2025-11-11 04:50:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a08f4ade-2f4f-3db6-91da-aaf1d0c7e196 | -5.64014 | -43.92136 | 2025-11-11 04:50:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aac87b26-b8f9-3ffb-a7ae-3625a7dafe9a | -2.02701 | -46.99594 | 2025-11-11 04:50:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c235e789-007d-3384-98a2-64049bfddbda | -6.37496 | -41.0775 | 2025-11-11 04:50:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 5d5f3c57-0bc0-3279-9451-8dbc678728c5 | -5.77019 | -51.42744 | 2025-11-11 04:50:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cd74b542-dcf8-3148-bcbe-b6a3f9ecc888 | -5.48678 | -44.02708 | 2025-11-11 04:50:00 | NOAA-21 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e6d7704e-7783-329c-9e61-08e94129aca0 | -6.09091 | -41.57005 | 2025-11-11 04:50:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 84eea777-3085-3482-9cc4-5f99c45e941a | -4.44448 | -45.51576 | 2025-11-11 04:50:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 21507c76-cec7-39bf-932f-b54b9c8f0a0b | -2.48362 | -50.25157 | 2025-11-11 04:50:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2da35cae-7f48-3ddf-83d4-797da6d685de | -2.15459 | -50.7044 | 2025-11-11 04:50:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 4416ac69-2668-3a75-acda-a3c8e0640dc4 | -7.30015 | -45.06682 | 2025-11-11 04:50:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b76122b2-3206-3831-bac3-db2c5c36be20 | -3.40586 | -46.90546 | 2025-11-11 04:50:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8d47c0fb-ce1a-3d30-a244-5a77c334e65d | -2.15513 | -50.70092 | 2025-11-11 04:50:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1f4ec3c9-23a9-33f0-81f2-9c9a5ad47eb8 | -3.96506 | -49.29545 | 2025-11-11 04:50:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a87278b8-ed88-3312-8516-7eb437dac506 | -4.20738 | -50.62985 | 2025-11-11 04:50:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bcb4654a-308a-327b-9d3d-c5c92a4bef73 | -5.12753 | -44.72374 | 2025-11-11 04:50:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8ce44f26-119b-39a2-9646-7c695d4ea293 | -4.17857 | -43.83038 | 2025-11-11 04:50:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8217fb09-9e54-3ff0-8cfd-88e04a00b7d1 | -6.33741 | -42.83534 | 2025-11-11 04:50:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 8b94f6a4-e055-31be-9613-0adc57915ee0 | -3.81254 | -46.00217 | 2025-11-11 04:50:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1cee1ec8-eeb2-3ebd-bf95-a62a4ccd0461 | -0.19353 | -50.472 | 2025-11-11 04:50:00 | NOAA-21 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b526cc11-edc7-3b9a-9cba-aa2db77177d3 | -2.87237 | -45.42702 | 2025-11-11 04:50:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 1c4beca0-d28d-33ec-926c-e997acdb9500 | -4.24341 | -49.8771 | 2025-11-11 04:50:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9c65a9f7-ae3c-3404-a2b3-dde041383ef6 | -3.80769 | -46.00548 | 2025-11-11 04:50:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 96d48115-1412-3957-b3bf-7cfdf5f209ef | -5.40106 | -45.23899 | 2025-11-11 04:50:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c6212bb7-4ed6-3c48-9d67-70717da55b99 | -2.44136 | -46.30703 | 2025-11-11 04:50:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2a3750bf-81fe-3842-a087-a9807c5a894b | -4.74109 | -49.53152 | 2025-11-11 04:50:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4a007be7-d388-3630-b0ec-53cbebe10001 | -2.97411 | -47.8959 | 2025-11-11 04:50:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 53ca7b59-731a-311b-9929-bfe7c6115b98 | -3.83738 | -52.30054 | 2025-11-11 04:50:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 841502af-9aab-3dd9-bc90-c1054e97c63b | -4.27548 | -50.53757 | 2025-11-11 04:50:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 28bbdf3e-18fe-3de1-97a0-99a88871f4b7 | -1.506 | -55.47286 | 2025-11-11 04:50:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4eec3e9a-3a8b-386a-bfdc-22256fe7a518 | -5.14921 | -50.8722 | 2025-11-11 04:50:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4e5868ff-05b2-3cb4-8fdf-13ed6bd0ec46 | -3.22328 | -61.23999 | 2025-11-11 04:50:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f10dcede-cd9d-3834-b95c-ba31b3a9e93f | -3.95497 | -50.52144 | 2025-11-11 04:50:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a26e9f04-cb55-3a0c-b8ba-d1f669bb1f00 | -0.85522 | -48.66558 | 2025-11-11 04:50:00 | NOAA-21 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fed31d35-e1a6-3835-971b-768f4e89e471 | -3.85518 | -41.57907 | 2025-11-11 04:50:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 50adf4a6-35ec-33cd-9929-179ce6a7681d | -4.71925 | -46.45105 | 2025-11-11 04:50:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 749eef92-e4ca-3d80-a8c9-182927ac8ae1 | -1.48415 | -45.62266 | 2025-11-11 04:50:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1f765f5f-6e5a-39c0-abbc-440eeb595bdb | -4.13924 | -50.64842 | 2025-11-11 04:50:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9415da5b-5b57-305e-8411-3fae1099b381 | -4.20402 | -50.62933 | 2025-11-11 04:50:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9e1c06c6-aebf-3ce9-a961-5d541fc2c061 | -5.20121 | -47.73733 | 2025-11-11 04:50:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| db3cebd6-9c93-32d0-8dac-e61f139aa1bf | 0.53088 | -50.75235 | 2025-11-11 04:50:00 | NOAA-21 | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1596e18e-0bf2-37a8-b57b-dbd8b21afec8 | -2.93369 | -45.40623 | 2025-11-11 04:50:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a02762c0-3483-3fd3-8c58-d0280df923cb | -2.868 | -45.42632 | 2025-11-11 04:50:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| f9879c89-f75c-31d7-b17e-3ed9c8af5cf5 | -7.29941 | -45.07206 | 2025-11-11 04:50:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a7ac4bea-a2be-3141-8c72-bc8fe11754e9 | -4.44378 | -45.5204 | 2025-11-11 04:50:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 3a246021-f1df-39c2-a46e-06977e24e2c3 | -4.91596 | -44.32349 | 2025-11-11 04:50:00 | NOAA-21 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dc6df77b-ef8a-3691-ac96-8ebbaf9f984f | -1.94417 | -52.00633 | 2025-11-11 04:50:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 074fa52e-3c4a-3e04-a40b-a5eb5fa231ed | -3.85461 | -41.58306 | 2025-11-11 04:50:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b5d01562-b4bd-3a62-870d-c23607eed50e | -1.55242 | -47.76103 | 2025-11-11 04:50:00 | NOAA-21 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 705ca167-d88e-3372-99c3-99e1d6e8fa84 | -2.43229 | -48.54361 | 2025-11-11 04:50:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 06951c44-fa75-34bb-afe9-d5b80fc9fa6c | -2.69884 | -49.11493 | 2025-11-11 04:50:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4521b954-e2a3-3b4d-abc1-ae85c652e39c | -4.68495 | -43.24685 | 2025-11-11 04:50:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 656f8081-b8fb-39fb-a56b-944e00a89820 | -4.44006 | -45.51485 | 2025-11-11 04:50:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |


[Clique aqui para ver as próximas entradas](README16.md)

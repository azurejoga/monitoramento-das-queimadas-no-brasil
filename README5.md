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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e18c4933-683b-3ab1-ac09-f54d4cec4ce7 | -10.8743 | -47.18096 | 2025-07-06 04:02:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4b303074-d6ec-3f4c-be77-5765c7e2ed62 | -10.56013 | -49.1316 | 2025-07-06 04:02:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 59e79ac3-e631-3663-b5c8-d131a11478ff | -10.56994 | -49.13363 | 2025-07-06 04:02:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 29779f68-c1fe-3e38-b031-6baba412f54b | -16.43004 | -42.18435 | 2025-07-06 04:02:00 | NOAA-20 | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 8b11c464-51c5-3bd5-8dd9-7187c15355d1 | -11.44807 | -45.10403 | 2025-07-06 04:02:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 8aa0dd19-11ad-30a7-977a-3650c3c24792 | -15.79929 | -47.64774 | 2025-07-06 04:02:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c46fa3bd-625b-3eac-af20-0d7b5933e320 | -10.65094 | -46.48281 | 2025-07-06 04:02:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 1862c3a8-fabb-3af7-a83d-1429c1a66151 | -15.71729 | -43.48973 | 2025-07-06 04:02:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 61e4ad5a-4869-315c-80f1-f551324b0341 | -11.44886 | -45.09946 | 2025-07-06 04:02:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 43e41317-a354-3f7f-8ae6-d48d18efcb8b | -9.0925 | -47.95803 | 2025-07-06 04:02:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 40dfdde8-daca-3d00-92e9-3531fed2c9a1 | -11.88642 | -44.88868 | 2025-07-06 04:02:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 60ce279a-80eb-321d-bd6e-b406f528e213 | -11.32769 | -51.45276 | 2025-07-06 04:02:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b40ade5f-e18b-348f-a43a-0b36c3b0ef23 | -9.19688 | -45.33284 | 2025-07-06 04:02:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 848f9405-8d0b-377e-8539-5c7187a4f615 | -9.41321 | -40.36576 | 2025-07-06 04:02:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ead9020f-8bb7-324b-be4a-ff8eb9caa7aa | -12.016 | -47.78123 | 2025-07-06 04:02:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a44ac96f-0b1f-3e60-9437-3d88a4a1f819 | -9.09163 | -47.96286 | 2025-07-06 04:02:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a475ff67-90fd-32ae-b682-ebf8e8666e99 | -10.64937 | -44.48551 | 2025-07-06 04:02:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 344cd45c-8a35-3621-9baa-5212e762acb2 | -10.57981 | -49.13531 | 2025-07-06 04:02:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3d2a0330-1817-3897-b3e3-07e74cbe5093 | -13.65643 | -45.75382 | 2025-07-06 04:02:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 08ec9859-5156-3626-b314-aaeed39529f4 | -11.88631 | -44.89492 | 2025-07-06 04:02:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 73626576-6e58-34bf-a223-579953e81f1d | -10.98794 | -44.32215 | 2025-07-06 04:02:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 45191c99-dd12-31e4-b85c-f984c61051c0 | -10.65007 | -44.48299 | 2025-07-06 04:02:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0a7f812d-ac30-3fbc-8220-5781b60feb2f | -9.19655 | -45.33376 | 2025-07-06 04:02:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 295543d0-0fd7-3781-ae21-3103ba7e7a3e | -11.32989 | -51.45405 | 2025-07-06 04:02:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| def2c6af-9c04-32b7-9980-27a6241a5f74 | -10.65011 | -44.48119 | 2025-07-06 04:02:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7213cb35-9361-36e1-8809-81a0821f645d | -12.01677 | -47.77694 | 2025-07-06 04:02:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 7875a3a9-c8e6-39d8-a212-1ad585db5a2e | -11.45259 | -45.10012 | 2025-07-06 04:02:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 65e6d524-9500-37fd-b007-c7e600e50fbb | -9.4099 | -40.36524 | 2025-07-06 04:02:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 66ef1d5e-5b0f-3084-9bbb-421834a639dd | -11.88334 | -44.89006 | 2025-07-06 04:02:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 31a94778-c8c3-3ddf-a53e-b8466e38e58f | -9.2008 | -45.33353 | 2025-07-06 04:02:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f4b5a0a8-54f4-301d-bf66-d59e4d4c9c58 | -16.4306 | -42.18076 | 2025-07-06 04:02:00 | NOAA-20 | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 0ef28b71-a498-3797-94fc-bb887beaec40 | -9.09716 | -47.9589 | 2025-07-06 04:02:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1620ac85-63b7-34a7-9bfb-3c264bc3eae2 | -11.33067 | -51.45016 | 2025-07-06 04:02:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 525c291a-bc9c-382d-91ef-8d820796723d | -10.6457 | -44.48668 | 2025-07-06 04:02:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8aeef821-4a16-33e9-8c10-4498bd3aa6e0 | -11.00063 | -42.79123 | 2025-07-06 04:02:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c546c45d-5dd3-3a3f-bde9-153f4044914e | -8.51968 | -47.49612 | 2025-07-06 04:02:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a635198f-ddb8-32a3-94b0-d5104eb5e9aa | -9.87045 | -48.45255 | 2025-07-06 04:02:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3fb949c5-c5e2-307a-b7ff-ce0ec8ec2b5a | -8.50432 | -47.50299 | 2025-07-06 04:02:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e68f6085-eaa4-3c64-bf30-5160f8c625a8 | -9.79646 | -47.74254 | 2025-07-06 04:02:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 170822c3-a32f-3bda-8936-964c5110f479 | -11.44728 | -45.1086 | 2025-07-06 04:02:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 331bfa76-5d70-3bf5-8edd-3416d71b1046 | -9.20438 | -45.33514 | 2025-07-06 04:02:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f0dcdd1c-8d06-3ef3-aa02-e6394afe5080 | -10.64935 | -44.48731 | 2025-07-06 04:02:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 33a7bf48-8899-37ec-a01d-fc15fb61a831 | -10.65454 | -40.81044 | 2025-07-06 04:02:00 | NOAA-20 | MIRANGABA | BAHIA | Brasil | 2921401 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 467b58d6-2a5f-32d7-952a-ad3e9a3b53d8 | -10.57487 | -49.13449 | 2025-07-06 04:02:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 35b163f6-eaec-3c46-aa14-cf85af733d87 | -10.64497 | -44.4892 | 2025-07-06 04:02:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a9ee2f4d-c755-3c4b-a0e3-ebee00d5b31b | -8.52051 | -47.49145 | 2025-07-06 04:02:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1096615b-2fb7-3a76-85fb-4ca0eadc8a79 | -12.01239 | -47.77612 | 2025-07-06 04:02:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 7e556a87-152d-3f3f-abd8-399a3174ccf7 | -9.20046 | -45.33445 | 2025-07-06 04:02:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c693a1dd-df35-30ca-b5be-f54e0298291b | -11.3228 | -51.44769 | 2025-07-06 04:02:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 64ae5f0c-f12f-3a9a-861d-bb2e1eb3df05 | -11.33259 | -51.4578 | 2025-07-06 04:02:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 264da662-189b-3c18-b70d-57f4e5126f41 | -11.4518 | -45.10469 | 2025-07-06 04:02:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 370a306c-078c-3e0b-8f20-db1974df88d2 | -9.9468 | -47.95821 | 2025-07-06 04:02:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ab4fae17-e7b9-3bee-b3f6-d2e5e49d308b | -10.25368 | -48.16203 | 2025-07-06 04:02:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 88271d9c-4ab0-308c-a277-4a952792b952 | -13.39744 | -47.82975 | 2025-07-06 04:02:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6debcc55-020a-3391-ad81-2758db61e573 | -22.43729 | -46.78313 | 2025-07-06 04:04:00 | NOAA-20 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| aebe56dc-dca9-3990-ad27-aae1e60b2921 | -19.45235 | -45.30532 | 2025-07-06 04:04:00 | NOAA-20 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 13c79b48-f99e-3766-b4cd-9c1aa2f0fdb6 | -20.4158 | -43.55174 | 2025-07-06 04:04:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| cf593ca0-4b5a-3539-a8be-c94b889ea073 | -20.84987 | -46.70876 | 2025-07-06 04:04:00 | NOAA-20 | FORTALEZA DE MINAS | MINAS GERAIS | Brasil | 3126307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 213fa2cc-7f92-366d-9282-3cd3e5db364a | -23.59398 | -47.43716 | 2025-07-06 04:04:00 | NOAA-20 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 5702f7d9-b542-3e81-8e18-48ee54a3e15b | -20.1392 | -44.90001 | 2025-07-06 04:04:00 | NOAA-20 | DIVINÓPOLIS | MINAS GERAIS | Brasil | 3122306 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b039c096-ffdf-3775-a8aa-efdd88009286 | -17.67719 | -42.74082 | 2025-07-06 04:04:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 176a65ec-3c4e-368d-94cd-ae6c2f0692fc | -20.57982 | -44.57603 | 2025-07-06 04:04:00 | NOAA-20 | PASSA TEMPO | MINAS GERAIS | Brasil | 3147709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 6c30a028-cf5c-3d85-92fc-ca3ece30a823 | -19.45579 | -45.30595 | 2025-07-06 04:04:00 | NOAA-20 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e4acfd08-a1ed-3ad1-85e3-76327bd5f1ae | -20.19823 | -50.70866 | 2025-07-06 04:04:00 | NOAA-20 | ASPÁSIA | SÃO PAULO | Brasil | 3503950 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| 4fefaf28-7275-3e9f-8653-5190c2461591 | -17.26613 | -49.00575 | 2025-07-06 04:04:00 | NOAA-20 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5dd96a71-f4fe-3ee3-a962-30692af16ced | -21.28221 | -46.17471 | 2025-07-06 04:04:00 | NOAA-20 | ALTEROSA | MINAS GERAIS | Brasil | 3102001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| df4d2f9b-a6c0-3060-8ed6-4bc97ebcc97e | -21.36293 | -46.93145 | 2025-07-06 04:04:00 | NOAA-20 | ARCEBURGO | MINAS GERAIS | Brasil | 3104106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 4183ae23-b7a1-3565-ba0c-f5541bac845c | -19.71645 | -40.35225 | 2025-07-06 04:04:00 | NOAA-20 | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 6961b864-67aa-3131-b990-4b0ddfe955ed | -21.62519 | -43.46492 | 2025-07-06 04:04:00 | NOAA-20 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 18a4bb9c-657c-3f31-a5be-de6fe20ef82c | -21.19399 | -44.93748 | 2025-07-06 04:04:00 | NOAA-20 | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 57edcf79-a870-354e-a188-4817aee3981f | -20.26822 | -43.64656 | 2025-07-06 04:04:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 1716c48f-b294-344a-83aa-8e254c7071da | -16.6803 | -43.88361 | 2025-07-06 04:04:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1595a540-0653-3ba5-b3e6-88684190d24e | -17.38469 | -42.65758 | 2025-07-06 04:04:00 | NOAA-20 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cc06373f-43ff-352e-9868-834757092e48 | -20.76314 | -46.77061 | 2025-07-06 04:04:00 | NOAA-20 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 9b2c0446-d532-383f-9185-5bbc4aa25488 | -21.18039 | -43.97916 | 2025-07-06 04:04:00 | NOAA-20 | BARROSO | MINAS GERAIS | Brasil | 3105905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| f11561e6-ff52-39e8-add1-1ee983d2207a | -21.68927 | -49.72435 | 2025-07-06 04:04:00 | NOAA-20 | LINS | SÃO PAULO | Brasil | 3527108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 20d27114-7abe-37ba-922e-7f0a9de68c59 | -22.53956 | -48.81494 | 2025-07-06 04:04:00 | NOAA-20 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ed84276f-11dd-39d8-8af6-dd26ccb4d1d4 | -17.76163 | -50.93414 | 2025-07-06 04:04:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5c50cfc3-8669-35ef-a8c9-1fcd066c1de1 | -16.72122 | -43.80288 | 2025-07-06 04:04:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4d5f6d90-5388-3c54-af2b-2e55c2e3c909 | -19.4383 | -44.34097 | 2025-07-06 04:04:00 | NOAA-20 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ad8127d7-6e62-3aee-b167-f45e14a1f948 | -22.51917 | -47.15783 | 2025-07-06 04:04:00 | NOAA-20 | ENGENHEIRO COELHO | SÃO PAULO | Brasil | 3515152 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b1e7272a-d6a9-3c23-a07f-f6b045989975 | -19.78794 | -46.30489 | 2025-07-06 04:04:00 | NOAA-20 | PRATINHA | MINAS GERAIS | Brasil | 3153004 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3eee3b69-a05d-3fdd-b0cc-82bd19e54a69 | -20.17588 | -43.71373 | 2025-07-06 04:04:00 | NOAA-20 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 8228cb60-5bd8-3233-b05c-29f93385defb | -22.67559 | -42.85332 | 2025-07-06 04:04:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 71db09c8-d5db-3898-88b3-652bd4af2eb3 | -17.09449 | -43.80229 | 2025-07-06 04:04:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 886016f5-a602-3c58-b182-40e6c5796ff0 | -18.03881 | -39.92536 | 2025-07-06 04:04:00 | NOAA-20 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 2199c64b-1a34-3885-9aaa-92415dd07cfe | -22.86303 | -46.53159 | 2025-07-06 04:04:00 | NOAA-20 | BRAGANÇA PAULISTA | SÃO PAULO | Brasil | 3507605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| a92bf6ca-8175-3bd8-ba39-3fbca1820139 | -17.77839 | -42.80919 | 2025-07-06 04:04:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 58eead3f-3160-3e16-861e-5ce249379e6c | -22.94615 | -43.02074 | 2025-07-06 04:04:00 | NOAA-20 | NITERÓI | RIO DE JANEIRO | Brasil | 3303302 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| b909cd84-2433-3763-8223-36cdb06e5855 | -21.62461 | -43.46862 | 2025-07-06 04:04:00 | NOAA-20 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 71e696ce-aa4c-3479-a501-1a10d40ef69b | -21.68991 | -49.72306 | 2025-07-06 04:04:00 | NOAA-20 | LINS | SÃO PAULO | Brasil | 3527108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 618e6df2-0356-3285-b8f3-49d6081f8624 | -21.32515 | -44.24093 | 2025-07-06 04:04:00 | NOAA-20 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 24.0 |
| 9e13c494-573b-3ad8-9596-794718e83b4c | -17.73049 | -42.68249 | 2025-07-06 04:04:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 7405ba13-7d33-3fcf-99f6-65ae1b85f966 | -21.68909 | -49.72718 | 2025-07-06 04:04:00 | NOAA-20 | LINS | SÃO PAULO | Brasil | 3527108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| d90b66ae-8f4e-349c-9595-522891fbb506 | -23.33709 | -46.7732 | 2025-07-06 04:04:00 | NOAA-20 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| b7e5624f-3eed-3388-853f-f989e39965d3 | -25.19193 | -49.32494 | 2025-07-06 04:06:00 | NOAA-20 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 384f8188-7696-3725-a23b-b20b74f48340 | -24.24298 | -50.74157 | 2025-07-06 04:06:00 | NOAA-20 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| cc951dff-4e91-3851-bbb7-b2abfb72a388 | -29.95287 | -51.61505 | 2025-07-06 04:08:00 | NOAA-20 | CHARQUEADAS | RIO GRANDE DO SUL | Brasil | 4305355 | 43 | 33 | nan | nan | nan | Pampa | 0.5 |
| 8e18e84c-21ea-39d8-b770-009afbeb1e85 | -12.0266 | -57.0845 | 2025-07-06 04:10:00 | GOES-19 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 51.4 |
| d23db71d-2856-3e52-985c-6df94f9bea3e | -12.0266 | -57.0845 | 2025-07-06 04:20:00 | GOES-19 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 48.9 |


[Clique aqui para ver as próximas entradas](README6.md)

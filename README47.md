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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2cf5ae80-88fd-3293-a6f8-842a4c17fe1e | -13.9106 | -48.57804 | 2026-09-21 04:21:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3248bd56-5d68-3468-96be-c522f4cde477 | -13.03666 | -46.96279 | 2026-09-21 04:21:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d8d134d9-fa4f-3815-b129-2e20587ad765 | -11.02627 | -48.31763 | 2026-09-21 04:21:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 17963520-78d4-3c8b-92b1-82f66edb34b6 | -10.40316 | -50.2352 | 2026-09-21 04:21:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 15.1 |
| f768c826-4e94-3be4-a2ec-3a709e5805a2 | -10.71294 | -54.01735 | 2026-09-21 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| acdc7c42-8d1d-37ca-b55d-7a2659cbf771 | -11.80803 | -49.81221 | 2026-09-21 04:21:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| dec48d0a-4c87-3999-80ac-e27f3ea5d2e6 | -10.36471 | -50.45046 | 2026-09-21 04:21:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8db37d5f-c62b-393d-a584-3db519de6f18 | -10.79158 | -50.77074 | 2026-09-21 04:21:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 2661b3c8-b912-3ec2-9064-3e3a64f8a366 | -10.36744 | -50.22262 | 2026-09-21 04:21:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6b874cf9-efca-34d9-97b0-3d49b439280a | -11.7217 | -54.5735 | 2026-09-21 04:21:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 653573d9-b1f8-3ee3-948b-4b4b701572de | -16.03735 | -52.51185 | 2026-09-21 04:21:00 | NOAA-20 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 50.0 |
| 5658e7af-79cc-3420-bbd1-1047547eeebb | -10.79943 | -50.82512 | 2026-09-21 04:21:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cac1c354-49e3-3230-aeb4-9a0f2378dbf2 | -11.43634 | -45.40474 | 2026-09-21 04:21:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1d8ebcbb-ef8b-35da-9c73-021a74b3e35e | -10.67661 | -48.72537 | 2026-09-21 04:21:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 71247696-d287-3dd2-b23c-ca82f7c5262b | -11.35309 | -51.43085 | 2026-09-21 04:21:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e7523305-c82f-34ea-b58d-119a83e17398 | -14.91855 | -49.90539 | 2026-09-21 04:21:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 34712beb-9b6e-319e-bfd3-d16d499e36eb | -11.12875 | -54.01569 | 2026-09-21 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7c17f8ec-5f40-30e1-8e53-c83e50da0cc3 | -10.91649 | -53.96526 | 2026-09-21 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 38d11b37-7984-302c-81a3-60b2ab079fbe | -10.37557 | -48.90783 | 2026-09-21 04:21:00 | NOAA-20 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 3a9de1cb-e75e-37e2-9b60-ffd80dbc1dfd | -11.83787 | -46.82357 | 2026-09-21 04:21:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| adde2314-4065-33ae-b7e1-dafbf2f43765 | -17.58958 | -43.6918 | 2026-09-21 04:21:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 20b24196-7420-386a-8e1c-60c607f02e00 | -11.02471 | -48.32977 | 2026-09-21 04:21:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6ae824b2-32a0-3841-900d-570ff8ca3c3c | -12.54444 | -50.0714 | 2026-09-21 04:21:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b1e2f3f4-9ad8-355c-9625-2295b1e22e02 | -9.67451 | -54.33885 | 2026-09-21 04:21:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 91f1aab7-bbe9-3a95-b0a7-665691a0bc8a | -13.06329 | -50.62772 | 2026-09-21 04:21:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 130d8527-9137-3c2f-9440-ab538b21510f | -16.0356 | -52.5212 | 2026-09-21 04:21:00 | NOAA-20 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 19.4 |
| a126b7c7-5acb-3fbe-a7df-e48e608f07a6 | -8.6038 | -54.61645 | 2026-09-21 04:21:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b5af0f6e-43a3-3a4f-90d1-237d9623f31e | -11.85716 | -46.87873 | 2026-09-21 04:21:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| aa0a23f2-6656-319e-b036-a05e73115da2 | -11.17018 | -54.12436 | 2026-09-21 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0b3d12bd-c7f2-340a-a703-8da01093cf41 | -16.68762 | -49.384 | 2026-09-21 04:21:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 65c3ecca-9683-336b-9ca9-8f090dc83bc1 | -11.77831 | -49.81424 | 2026-09-21 04:21:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 54c61446-d553-3bd9-92b9-329cd75f7772 | -16.03199 | -52.51552 | 2026-09-21 04:21:00 | NOAA-20 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 57.2 |
| 86866122-59b3-34a6-bf76-a08e660bd346 | -17.07368 | -43.19903 | 2026-09-21 04:21:00 | NOAA-20 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b739f594-c6dc-37ca-a516-bc2a46a25300 | -14.17961 | -47.86552 | 2026-09-21 04:21:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7d7b6d32-34ef-3ac3-8e4b-237995ac83c7 | -12.39395 | -47.00822 | 2026-09-21 04:21:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 192235e6-74ea-3220-8064-5df2ec87ce51 | -14.09442 | -52.13648 | 2026-09-21 04:21:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 8.7 |
| de172739-5b03-31db-bf23-14e7ed44ec2f | -15.46186 | -48.4688 | 2026-09-21 04:21:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 14becb85-e8b2-3270-b770-0b2e6df1fe26 | -9.82726 | -48.31714 | 2026-09-21 04:21:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| f1490e60-ad8d-35b9-938b-8d454e2b1b02 | -10.14097 | -45.55695 | 2026-09-21 04:21:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 805f54fa-44b9-3c66-9ae7-85554fbc9dae | -12.68149 | -50.95794 | 2026-09-21 04:21:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ad1199d8-1a65-3bb2-a115-0312e6f2b3b9 | -12.02648 | -51.49379 | 2026-09-21 04:21:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 47395761-b73d-39db-98f2-d7f44ee0e924 | -11.99477 | -44.89038 | 2026-09-21 04:21:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5ab3c7cf-de32-3b50-a47b-3f4bd198787c | -14.79379 | -48.52513 | 2026-09-21 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 96272a37-12dc-313b-b38e-4db2905c39ba | -11.05096 | -47.67873 | 2026-09-21 04:21:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d9e91c9a-cbcb-3244-b0c3-6077c5162be5 | -11.33522 | -47.28702 | 2026-09-21 04:21:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d242ad89-734b-3422-a4d2-2fef5d18d09b | -11.10025 | -54.01757 | 2026-09-21 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1d2dc032-77e6-36eb-b122-fd75b0cbf5d7 | -10.4594 | -50.29201 | 2026-09-21 04:21:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| de5bd4b7-a7d4-3410-8fa9-60187ed3327a | -12.11075 | -47.04953 | 2026-09-21 04:21:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1ca52c52-a0ef-3d06-9725-2c2aa0c1743a | -16.02391 | -52.50887 | 2026-09-21 04:21:00 | NOAA-20 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 647f9982-187f-3362-aa2f-1d60c6adceeb | -10.85202 | -50.15536 | 2026-09-21 04:21:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 97b96d80-28dd-3260-a8e3-0944ea46308d | -14.61026 | -52.11068 | 2026-09-21 04:21:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 47d40f5e-e2bc-3fbf-bf7b-8eb8e4810e34 | -10.78226 | -50.74652 | 2026-09-21 04:21:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 32a2a60e-1316-38b2-8050-02d82512b8fe | -11.09262 | -51.06505 | 2026-09-21 04:21:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1180886e-63de-3c51-adc5-ca6a21541739 | -10.55417 | -46.73361 | 2026-09-21 04:21:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f255d8b5-5e5b-3420-a410-4895a480c183 | -10.8595 | -54.1141 | 2026-09-21 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a56edf37-4c17-35e7-9423-b201aae97271 | -12.77455 | -52.85198 | 2026-09-21 04:21:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 00e78fef-ba3f-3b4d-b73e-7f9dfdeca3cd | -10.73928 | -50.78349 | 2026-09-21 04:21:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f3fa8354-305f-3200-92e2-441c79818222 | -10.38035 | -48.90351 | 2026-09-21 04:21:00 | NOAA-20 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ef3e5cdd-becf-31cf-9e78-fbac12c46ea6 | -11.11179 | -54.01613 | 2026-09-21 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2a42d4f8-d690-346b-8f7b-78f1ee192f3f | -15.46246 | -48.47563 | 2026-09-21 04:21:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 3eb3bffe-2b3b-30bb-9342-a6cdb3c5c1ca | -11.46603 | -47.7536 | 2026-09-21 04:21:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 85747096-1bdf-3240-963b-2d7d6515a997 | -10.85623 | -50.15615 | 2026-09-21 04:21:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5a0194a2-1913-3ce4-a50d-f17778301bc9 | -9.73465 | -54.81388 | 2026-09-21 04:21:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 331631d5-2b07-319a-9acf-70beceb9f2b9 | -10.74132 | -50.79742 | 2026-09-21 04:21:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9bb07716-1e79-3b15-8547-49e25f4273e2 | -10.5425 | -54.49858 | 2026-09-21 04:21:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2ab24538-31c0-3d96-99d4-27a2ba11f5da | -11.09341 | -51.06055 | 2026-09-21 04:21:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0ccea9d6-cb22-3476-ae34-035135f9cb94 | -12.89249 | -50.96888 | 2026-09-21 04:21:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b32cf317-c237-35a3-9a05-603fed9db1c4 | -10.90292 | -53.97733 | 2026-09-21 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 741134f4-e215-30c1-a5cd-2140820d9df7 | -9.75144 | -46.24213 | 2026-09-21 04:21:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 52c631c2-397f-3781-9ae6-77668a635b63 | -11.03988 | -54.90972 | 2026-09-21 04:21:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e96a8141-2c43-395d-946f-86df81d8460d | -10.26866 | -49.98968 | 2026-09-21 04:21:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9facbda6-9128-37f4-9d9b-59dde3c9ba1c | -12.50916 | -49.80083 | 2026-09-21 04:21:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 805b0e56-8cfb-3357-bc2f-21b558d889dd | -10.88005 | -50.93607 | 2026-09-21 04:21:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d38f2ee5-83de-3ac3-bfc3-639d5c0763e3 | -15.45607 | -48.46982 | 2026-09-21 04:21:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4bf2974e-b432-33d8-8257-923ffac3572d | -11.79585 | -49.80995 | 2026-09-21 04:21:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 82d29b31-2f4d-3cc3-95da-7403a0403cfb | -10.72474 | -50.71341 | 2026-09-21 04:21:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 73a75ab8-e769-3457-8a8f-bc6ef779a7fd | -10.27287 | -49.99045 | 2026-09-21 04:21:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ec545645-5e63-311a-a65e-e1e0be5a6d81 | -13.17325 | -43.56489 | 2026-09-21 04:21:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 17.7 |
| bba564e9-1a5a-3608-a5dd-62cdeffacba2 | -13.62189 | -48.28979 | 2026-09-21 04:21:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c84aa829-51c9-394b-a6a6-9bdadfdc0a82 | -9.82753 | -48.44332 | 2026-09-21 04:21:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| c80ed876-f3a2-3a83-92a7-fb424f057fb5 | -12.81032 | -54.05091 | 2026-09-21 04:21:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a83a1ec9-dd03-3f1b-b616-6a42497f5290 | -10.44797 | -51.24504 | 2026-09-21 04:21:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8a0d1db8-22cf-3152-811d-763a7e1f1ce3 | -10.75739 | -50.80947 | 2026-09-21 04:21:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d6ce8a9b-44db-354f-9e2a-b0eef9295eed | -13.88939 | -48.56968 | 2026-09-21 04:21:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6f42f184-06c7-37c5-a740-3b244b4f01b2 | -8.60803 | -54.62624 | 2026-09-21 04:21:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9a068790-47ba-347c-bd3b-528007ee712e | -10.16457 | -46.54607 | 2026-09-21 04:21:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 18be3869-e0b2-3cfb-af1d-d697e6315c44 | -16.02932 | -52.51219 | 2026-09-21 04:21:00 | NOAA-20 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 29.1 |
| 063669a0-2135-30f0-88db-eafc5e5d728b | -10.87817 | -54.07639 | 2026-09-21 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 63622494-a0b2-3c3b-b1f0-8ea339c72a4c | -11.84414 | -46.89256 | 2026-09-21 04:21:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 55db2d77-bdd4-36cd-a8b7-9aef71569575 | -10.12064 | -48.44021 | 2026-09-21 04:21:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 39757419-7db7-3d7e-bdad-916d80c0bcaa | -11.65008 | -47.77188 | 2026-09-21 04:21:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 762a05b9-1056-36aa-a6e9-8877804f275c | -13.03881 | -46.97113 | 2026-09-21 04:21:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 9348c723-6fd3-31b4-abd7-2065e5307d3a | -10.09379 | -50.26779 | 2026-09-21 04:21:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 02195f17-0547-349a-918c-764cf1d9f8e3 | -14.92735 | -49.90108 | 2026-09-21 04:21:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 15e05cfc-520b-3647-ac41-b390e5c594dd | -10.1496 | -47.6824 | 2026-09-21 04:21:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 741dd50a-3485-3817-a04a-a1c861ffb05e | -16.03561 | -52.50389 | 2026-09-21 04:21:00 | NOAA-20 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 41ccdab4-eadf-3228-a1f7-0c1ab2e23ba2 | -11.02101 | -48.32588 | 2026-09-21 04:21:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3db7cb91-40f1-3694-8369-dae2a03da263 | -10.33543 | -50.20405 | 2026-09-21 04:21:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 015f39a1-9cef-3d99-ba2d-c86e1cc94097 | -13.92558 | -47.84532 | 2026-09-21 04:21:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ee247f21-4dd6-3679-94e3-398163c72c28 | -10.34325 | -50.2097 | 2026-09-21 04:21:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README48.md)

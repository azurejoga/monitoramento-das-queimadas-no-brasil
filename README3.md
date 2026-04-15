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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9ac12d08-7792-3205-9cad-475b93f2cf47 | -20.22494 | -46.46128 | 2026-04-15 04:02:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d9f7a395-8c7c-306e-b0c2-b16ee826e2cd | -20.53802 | -49.50515 | 2026-04-15 04:02:00 | NOAA-20 | MIRASSOLÂNDIA | SÃO PAULO | Brasil | 3530409 | 35 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 4d537209-9c4a-3e22-a2cc-ad51984de5f2 | -20.16659 | -46.57764 | 2026-04-15 04:02:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 103301e5-a35c-3c60-9157-dab79beca542 | -20.18752 | -46.57462 | 2026-04-15 04:02:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d5ccd3db-2f51-39b0-b86b-4204bc6af0fd | -20.16958 | -46.58339 | 2026-04-15 04:02:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c73eafe2-3f4a-3ccc-bb82-5bebc8b5cecf | -21.11684 | -42.38919 | 2026-04-15 04:02:00 | NOAA-20 | MURIAÉ | MINAS GERAIS | Brasil | 3143906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 30148be9-40df-3067-9805-023613cb429d | -22.87572 | -48.64549 | 2026-04-15 04:02:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2d787ada-a107-3b9c-b2ca-3f650185976b | -20.24536 | -46.54774 | 2026-04-15 04:02:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d1020d70-9816-3f9c-8920-ac211702be5e | -26.72857 | -50.26521 | 2026-04-15 04:02:00 | NOAA-20 | MONTE CASTELO | SANTA CATARINA | Brasil | 4211108 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 9757f405-7d5c-3d7a-860c-93c2330ad354 | -20.22783 | -46.46743 | 2026-04-15 04:02:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3e77522d-a592-3da3-a3ed-4db7567b70e4 | -25.64956 | -50.11912 | 2026-04-15 04:02:00 | NOAA-20 | SÃO JOÃO DO TRIUNFO | PARANÁ | Brasil | 4125100 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| b8d95ac7-bb2c-3677-bdb1-f7021c3844cb | -21.48709 | -48.66871 | 2026-04-15 04:02:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ffc5c71a-05bc-394d-a392-d1cea988617c | -20.53334 | -49.50414 | 2026-04-15 04:02:00 | NOAA-20 | MIRASSOLÂNDIA | SÃO PAULO | Brasil | 3530409 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fc360f97-243d-32e2-b507-a6cf41e37740 | -30.27122 | -50.97578 | 2026-04-15 04:04:00 | NOAA-20 | VIAMÃO | RIO GRANDE DO SUL | Brasil | 4323002 | 43 | 33 | nan | nan | nan | Pampa | 1.4 |
| 26c3036f-6bb7-3300-af89-17a124e4ec1b | -30.13574 | -52.56056 | 2026-04-15 04:04:00 | NOAA-20 | RIO PARDO | RIO GRANDE DO SUL | Brasil | 4315701 | 43 | 33 | nan | nan | nan | Pampa | 1.1 |
| fd4a3f00-69e7-31cf-92ef-adf475a85ca3 | 3.23928 | -61.21471 | 2026-04-15 04:44:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 2f9c3f7c-4923-35ac-b062-7afe38bca2c3 | 2.94085 | -60.17562 | 2026-04-15 04:44:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 52985e35-fd44-3983-8747-0ffbca5a8436 | 1.47909 | -60.92029 | 2026-04-15 04:44:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 71b633d5-692b-32f9-bab7-6d2ec1d1e5b2 | 3.22604 | -61.21667 | 2026-04-15 04:44:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 2f4d8ec7-bff0-3353-92e4-687a61927023 | 3.23349 | -61.22135 | 2026-04-15 04:44:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 5.4 |
| f774da16-1444-3ddb-ac19-1d5f6611aea3 | 2.56346 | -60.55187 | 2026-04-15 04:44:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 725a80cd-63a8-3a4e-a50b-fd9e5eb2ecfc | 1.9055 | -61.09573 | 2026-04-15 04:44:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3646b589-ad35-3d5c-9153-bc47acb8efe4 | 3.23266 | -61.21567 | 2026-04-15 04:44:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 390f5487-cfe6-3057-a3c5-933e755d0890 | 2.94704 | -60.17477 | 2026-04-15 04:44:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 5.4 |
| e6396d6d-4477-321e-a567-ba14639dddf5 | 2.56977 | -60.55099 | 2026-04-15 04:44:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 49141052-a039-3048-9169-63ff0aa527c6 | 1.10282 | -60.51604 | 2026-04-15 04:44:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4c7d5128-0c5a-3b8a-abec-b1c9fdcfa8f3 | 1.10355 | -60.52075 | 2026-04-15 04:44:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4e74961f-9d9b-3dca-b5c0-208e9c1278d4 | 2.57492 | -60.32817 | 2026-04-15 04:44:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 96ebe107-2f5c-32f4-9159-0155b0c56f59 | 2.56589 | -60.54889 | 2026-04-15 04:44:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 2f50806d-7688-33e9-ba4e-bcef84868546 | 1.48544 | -60.91936 | 2026-04-15 04:44:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b99f4869-3eab-3b0f-8dc4-87b2ccea6479 | 2.56668 | -60.55399 | 2026-04-15 04:44:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 3e9b4519-e874-3211-9827-9ae36c3eac99 | 1.90445 | -61.09485 | 2026-04-15 04:44:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1de5ec80-99d4-30c1-8d54-b26b75bbd518 | 3.24011 | -61.22038 | 2026-04-15 04:44:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 5.4 |
| c782007b-b530-35d9-8ce3-b3594e0ab446 | 2.5742 | -60.32334 | 2026-04-15 04:44:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| badd9c56-83eb-3450-8674-fe380b787c38 | -9.01278 | -46.12125 | 2026-04-15 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 69491fee-4c65-31b5-9a0a-614bee7174c8 | -9.01331 | -46.11745 | 2026-04-15 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 50d918ff-1ea3-3f13-a371-d5ef2ec53cb1 | -11.78717 | -43.61574 | 2026-04-15 04:49:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8d39363f-d40a-33a8-ad57-b9cf1fe8f094 | -11.78132 | -43.62107 | 2026-04-15 04:49:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 72ae4614-ebab-3d31-87be-da1d3e1fa9a1 | -11.57339 | -54.57602 | 2026-04-15 04:49:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e3171ff6-a1f2-3fa4-bda8-fcccda8bf89a | -11.43279 | -55.09698 | 2026-04-15 04:49:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| eb429878-c600-30e0-a4ac-e2c0a3e1887c | -11.78171 | -43.61805 | 2026-04-15 04:49:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 27d2f652-81b7-3695-af35-79d2845efcd6 | -11.79576 | -43.62933 | 2026-04-15 04:49:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 03c230dc-0f22-3f62-90bf-787838d255a2 | -12.45358 | -43.7823 | 2026-04-15 04:49:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0fed8c03-5257-3cbe-bc18-847be759bcfb | -11.79146 | -43.62253 | 2026-04-15 04:49:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| aa0161e1-8899-3e8b-9ba5-fead755ab71f | -15.28643 | -43.06581 | 2026-04-15 04:49:00 | NOAA-21 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 477ebc65-c254-3788-8bec-36bbe6f84da5 | -11.79693 | -43.62022 | 2026-04-15 04:49:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 41cd385f-a502-3e34-b9bc-e0550be43b94 | -12.99343 | -54.68228 | 2026-04-15 04:49:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 80451a41-37fe-3ae4-ac8e-521bd7df93e1 | -11.79615 | -43.6263 | 2026-04-15 04:49:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 8f396e29-230c-32a3-9f04-9ac6d6ef948f | -11.79108 | -43.62556 | 2026-04-15 04:49:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 64b8c71c-6d38-3c91-9da6-c2729d027b1d | -11.42852 | -55.10055 | 2026-04-15 04:49:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3bf81f06-3130-3d21-ba12-a05422bb524a | -11.7903 | -43.63163 | 2026-04-15 04:49:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 92fab012-fa06-3e08-aa35-92837d244a18 | -11.79069 | -43.62859 | 2026-04-15 04:49:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3846084e-73e8-35b6-b450-de3323a0eb63 | -11.802 | -43.62094 | 2026-04-15 04:49:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 428f223b-50ea-31f4-a96c-fc1d99beaad0 | -12.29115 | -57.39086 | 2026-04-15 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8cb9ecec-303e-3780-8f47-5d9c9ca76149 | -11.70899 | -44.74934 | 2026-04-15 04:49:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6cd38375-50aa-3702-b152-7ea1bbf71af9 | -11.70965 | -44.74429 | 2026-04-15 04:49:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fd753404-7d53-3b75-827e-8186d927180f | -11.78639 | -43.6218 | 2026-04-15 04:49:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| dfb66de9-2e54-3f0f-8fec-5d0acdeb191f | -12.99688 | -54.68288 | 2026-04-15 04:49:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 10d1b9ae-f2de-3a15-9f63-60e45ca8cd16 | -11.42921 | -55.09638 | 2026-04-15 04:49:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ce1c5e00-94de-3c5d-b313-6f1aa31a4538 | -11.431 | -55.0997 | 2026-04-15 04:49:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f926d3c5-c3d7-3ddb-abc3-e489123150b1 | -12.01698 | -49.27458 | 2026-04-15 04:49:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0ca45b79-52ba-3792-9059-e4479c9f3a23 | -11.57404 | -54.57207 | 2026-04-15 04:49:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7e0da176-91a2-3714-8924-9505d27ff6d4 | -11.79186 | -43.6195 | 2026-04-15 04:49:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4ba885af-67ee-3743-9070-994cd6e65f6e | -12.09524 | -51.22054 | 2026-04-15 04:49:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 23d8fb4e-f37f-3194-9d86-d2471ec1211b | -11.79654 | -43.62327 | 2026-04-15 04:49:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 6de61549-d631-34a3-9f62-92cfa7c5c640 | -15.55161 | -43.14895 | 2026-04-15 04:49:00 | NOAA-21 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b743c578-b8c7-3180-9099-4cc0f42477a2 | -11.43171 | -55.09555 | 2026-04-15 04:49:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 23751049-0434-3707-8040-91ee821a328e | -12.01581 | -49.27714 | 2026-04-15 04:49:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 6f0ea067-2844-30a8-b50d-1647c60c7682 | -15.28656 | -43.06557 | 2026-04-15 04:49:00 | NOAA-21 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 900e0c35-a9e5-3064-9264-613e8f260a32 | -13.44326 | -43.85387 | 2026-04-15 04:49:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ad1c8df9-5ea1-30d9-9b7f-017ab056c395 | -11.34253 | -55.30608 | 2026-04-15 04:49:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b34d4622-0f14-32dc-af1d-4b1bb1662f14 | -15.66151 | -43.31538 | 2026-04-15 04:49:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 5743dc48-7512-3533-97b5-77800cbbe4fe | -20.22869 | -46.47245 | 2026-04-15 04:51:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 25a4d342-54cd-3554-aecf-24a7bb460183 | -16.59204 | -58.21729 | 2026-04-15 04:51:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.2 |
| 779c74e0-e00e-38ec-b94d-388570ee25d1 | -18.50692 | -55.52143 | 2026-04-15 04:51:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| af774749-d43d-3c08-99e7-1434f3a0603f | -21.48649 | -48.67015 | 2026-04-15 04:51:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5ce8aa41-a353-3c23-9ee4-506aa659ee80 | -21.69577 | -56.3079 | 2026-04-15 04:51:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 43f90a9b-89f5-3160-a6dc-5f6f0578e958 | -18.7324 | -49.79116 | 2026-04-15 04:51:00 | NOAA-21 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 511da2e9-1f11-30bb-9208-93c9436500e5 | -20.24684 | -46.54413 | 2026-04-15 04:51:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f1f55b1d-b714-3f60-bd5a-ad361746cd07 | -16.66155 | -50.05995 | 2026-04-15 04:51:00 | NOAA-21 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 28551ef5-58e1-3ac4-8099-7a868534e7a2 | -20.53948 | -49.49746 | 2026-04-15 04:51:00 | NOAA-21 | MIRASSOLÂNDIA | SÃO PAULO | Brasil | 3530409 | 35 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 61f5e8ce-1022-3bf8-968a-6e656f70a161 | -20.22457 | -46.4668 | 2026-04-15 04:51:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e386ba3d-67c4-32cf-9cda-72162bf94c94 | -22.8315 | -47.14897 | 2026-04-15 04:51:00 | NOAA-21 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 617dbe20-c9fd-34bf-914c-cfe707f5797b | -20.95264 | -48.93457 | 2026-04-15 04:51:00 | NOAA-21 | NOVAIS | SÃO PAULO | Brasil | 3533254 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 6e52a063-3898-32d4-9f08-8a43f89fa4f3 | -18.47116 | -48.25308 | 2026-04-15 04:51:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 60d14691-468b-38ba-af9f-3436cf7e1af0 | -20.32481 | -55.00517 | 2026-04-15 04:51:00 | NOAA-21 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 76d257c9-d5ba-3a05-b938-809407f3efdf | -21.41299 | -48.61435 | 2026-04-15 04:51:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 0002f28a-a6db-3f41-9634-59f556e3b8a2 | -20.18886 | -46.57185 | 2026-04-15 04:51:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 246b49c5-ea6e-330c-827f-9caa3f44828d | -20.7454 | -47.90215 | 2026-04-15 04:51:00 | NOAA-21 | ORLÂNDIA | SÃO PAULO | Brasil | 3534302 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5398b2a2-d63d-3d25-9b50-c6a93088ee9d | -23.54123 | -47.63217 | 2026-04-15 04:51:00 | NOAA-21 | ARAÇOIABA DA SERRA | SÃO PAULO | Brasil | 3502903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b85936a7-d696-3432-9c39-7547232affc8 | -21.6985 | -56.31248 | 2026-04-15 04:51:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e7887199-e7b3-3397-82fe-70ad92ce50ea | -16.59599 | -58.21803 | 2026-04-15 04:51:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 524765c8-4c8d-3414-872e-95074284991b | -20.54014 | -49.49217 | 2026-04-15 04:51:00 | NOAA-21 | MIRASSOLÂNDIA | SÃO PAULO | Brasil | 3530409 | 35 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e4f8c244-03cb-30e7-b5f3-d8a1b1a52ea8 | -20.16873 | -46.58226 | 2026-04-15 04:51:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5be2a789-affc-36ac-9a6d-7ec15cdd1003 | -21.88512 | -56.267 | 2026-04-15 04:51:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 17aad38c-e67e-30e1-a9e4-abb9db6f521a | -17.71844 | -48.97995 | 2026-04-15 04:51:00 | NOAA-21 | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b06030a1-6f6c-3b3b-b700-e3feb98efe55 | -20.16815 | -46.58747 | 2026-04-15 04:51:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 2c04c7fe-cf42-3461-97e1-64a595f4d0f7 | -21.03725 | -48.55114 | 2026-04-15 04:51:00 | NOAA-21 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 38a9fdbf-ef0d-30bf-8cfe-a3a6526edebf | -22.87794 | -48.64826 | 2026-04-15 04:51:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 9767c469-df6f-3164-af75-2a46b3472e0c | -20.08054 | -50.61998 | 2026-04-15 04:51:00 | NOAA-21 | PARANAPUÃ | SÃO PAULO | Brasil | 3535903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |


[Clique aqui para ver as próximas entradas](README4.md)

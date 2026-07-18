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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d8e92ef2-0e2e-3e13-9e7e-6a2d34618c91 | -9.51958 | -47.1292 | 2026-07-18 04:38:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| eb26eedf-0226-310e-b1fe-e0e20abc34cc | -9.60873 | -47.75785 | 2026-07-18 04:38:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dd652310-ee83-36f2-bd36-8a6c2b6c067b | -8.94954 | -47.60737 | 2026-07-18 04:38:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7ba91cca-10ff-3cb6-a2fa-eb3b85b53d5b | -8.93358 | -47.60499 | 2026-07-18 04:38:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 61eb962e-cd42-3da1-913a-8a63aa137772 | -12.80023 | -46.56722 | 2026-07-18 04:38:00 | NOAA-20 | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a4e2106e-9afe-3de6-a13e-e66367ce9116 | -9.99829 | -43.43188 | 2026-07-18 04:38:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d3802130-1b26-3cc9-b6d5-e568688aeb86 | -10.52808 | -48.15651 | 2026-07-18 04:38:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 26d69479-8128-35e4-9924-8a61faeff075 | -9.82412 | -57.85077 | 2026-07-18 04:38:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fe04cd79-32e3-3bcb-96da-6b0469b58efb | -9.52804 | -47.11926 | 2026-07-18 04:38:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9e942cb0-bdca-3fea-99b0-342e2b3905ef | -8.71505 | -49.6064 | 2026-07-18 04:38:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4656b08c-d5ea-3196-b93a-059395e44d23 | -12.79727 | -46.56253 | 2026-07-18 04:38:00 | NOAA-20 | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d8a8c8f5-0f90-3502-be80-ae82b00c871a | -12.50213 | -48.25545 | 2026-07-18 04:38:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e9e6debc-ad61-3eb0-b3ba-7bf9bfe43fe5 | -8.12434 | -47.86971 | 2026-07-18 04:38:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bce12f16-ee42-3bfd-8434-4c57dce8a95d | -12.01276 | -50.57051 | 2026-07-18 04:38:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 6ff20085-775c-3242-8bbc-b57d61c91ff4 | -13.3221 | -45.1246 | 2026-07-18 04:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 90.3 |
| a3f61c26-9424-3e00-96f1-20cd335514e8 | -13.3028 | -45.1278 | 2026-07-18 04:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 44.1 |
| 81a64804-e030-355a-b043-986d85440f5b | -13.3217 | -45.1479 | 2026-07-18 04:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 225.2 |
| 8cfe3e56-20aa-3540-be41-817748f54d0f | -13.3023 | -45.1511 | 2026-07-18 04:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 104.0 |
| e2ec6715-6fab-3d2f-abd3-0f1a08e9ebeb | -18.7364 | -54.1988 | 2026-07-18 04:40:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 05a7f9d1-5b1a-3386-b926-41a1ad5dad63 | -13.31227 | -45.14176 | 2026-07-18 04:40:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 14.7 |
| adb1a632-2900-3d31-881a-a6992279ecef | -13.7314 | -51.87812 | 2026-07-18 04:40:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 96d4660f-4cf5-3b7d-8e7c-e146aac59761 | -13.98797 | -54.00354 | 2026-07-18 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5d7463f5-e9f3-3ac6-ac4d-331d5e5df6c1 | -18.73206 | -54.20726 | 2026-07-18 04:40:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b088dd5e-7771-373a-8d38-2f63e3f8c108 | -13.31988 | -45.15542 | 2026-07-18 04:40:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a58ca8ff-5cf6-3610-966f-d77361cda176 | -20.63115 | -41.39685 | 2026-07-18 04:40:00 | NOAA-20 | ALEGRE | ESPÍRITO SANTO | Brasil | 3200201 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 08897821-b36e-3192-81d3-eb8d735eee10 | -15.24096 | -48.57666 | 2026-07-18 04:40:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 398f875f-88e0-3575-baa5-ea26dc9dd99f | -19.35509 | -45.15739 | 2026-07-18 04:40:00 | NOAA-20 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 33a59cd8-0f11-3257-aa45-519365291511 | -18.2384 | -55.38215 | 2026-07-18 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 2004a4ca-c2bb-351d-9706-b503fdfc943a | -20.07237 | -43.70576 | 2026-07-18 04:40:00 | NOAA-20 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 26eb82d5-8a9d-36b4-8d6c-e5a8cffbde18 | -18.72997 | -54.19787 | 2026-07-18 04:40:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 17.2 |
| ba9c36bf-0e6f-393f-883d-19f96c8f79a9 | -19.78369 | -48.25794 | 2026-07-18 04:40:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7f7b1ec3-a24f-30cf-941c-d65378d7aea3 | -13.98879 | -53.99878 | 2026-07-18 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9415e116-363e-3fac-81c4-b8bf2a0af7ea | -13.31472 | -45.15221 | 2026-07-18 04:40:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 67645cbe-2347-398b-907d-86c9de5a375e | -13.31085 | -45.15166 | 2026-07-18 04:40:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 6e188a3d-ebd0-3774-a353-62aaaf319329 | -13.99961 | -53.998 | 2026-07-18 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e4eecd68-0b1c-3b0a-85d5-c0cfac999dd0 | -18.67665 | -48.17928 | 2026-07-18 04:40:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 0140d8d6-59c9-31c8-a2b6-4329a2ccd4e9 | -18.73282 | -54.20287 | 2026-07-18 04:40:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 9115132a-591a-35f0-af94-09e1b488b2d8 | -18.41305 | -43.72061 | 2026-07-18 04:40:00 | NOAA-20 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 831a0990-45a6-34c3-bf50-e91d6529a2bf | -13.31858 | -45.15276 | 2026-07-18 04:40:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 2f5a284f-3287-389a-961b-bcaa971dcc92 | -12.45645 | -49.58821 | 2026-07-18 04:40:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| dfe70221-eea0-3079-be90-ad52bdd99ac8 | -15.2449 | -48.57347 | 2026-07-18 04:40:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4781ba69-47d5-3d6b-84dd-355a46bf3043 | -17.70636 | -46.28025 | 2026-07-18 04:40:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a658f482-40a6-381e-9566-0b8fcaa32906 | -20.32343 | -41.51344 | 2026-07-18 04:40:00 | NOAA-20 | IÚNA | ESPÍRITO SANTO | Brasil | 3203007 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 10dfb94f-1cd2-3fac-8015-3721ba11b569 | -13.73075 | -51.88199 | 2026-07-18 04:40:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 87c8d960-4edb-3f2d-91c1-d9538b168279 | -19.84419 | -51.54349 | 2026-07-18 04:40:00 | NOAA-20 | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3d717eb4-f22b-39a6-aa33-a6c118314a63 | -17.30126 | -51.71161 | 2026-07-18 04:40:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 23dee0ab-49f2-3ff8-b191-bd771346fbd6 | -20.63556 | -41.39453 | 2026-07-18 04:40:00 | NOAA-20 | ALEGRE | ESPÍRITO SANTO | Brasil | 3200201 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 63fa7867-f152-396e-8162-d0181c5677c9 | -12.66275 | -48.22152 | 2026-07-18 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b694b371-a030-3a34-a242-9ae3c1c3fc40 | -11.74648 | -57.81564 | 2026-07-18 04:40:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 19db3de7-cc62-3cc3-bdcd-a04654ef45a7 | -16.47716 | -47.96002 | 2026-07-18 04:40:00 | NOAA-20 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7d3686ab-ce80-3c21-b11e-8017c7c1a77c | -12.45258 | -49.59119 | 2026-07-18 04:40:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| b985ad36-fe37-38a5-890f-2d288e7cc75d | -16.62493 | -49.39918 | 2026-07-18 04:40:00 | NOAA-20 | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7d4512da-73d9-32c8-8c76-52cc32ab2443 | -20.06985 | -43.71158 | 2026-07-18 04:40:00 | NOAA-20 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 8ada88ce-399c-3fe7-91ac-347fe66169ec | -18.73643 | -54.20346 | 2026-07-18 04:40:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 23.9 |
| a4c44d2a-f258-3d1d-b97d-e0af4c1e66c2 | -13.73419 | -51.8826 | 2026-07-18 04:40:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7d58b80d-0a63-3f27-a4fd-fc88093c1d87 | -13.31156 | -45.14671 | 2026-07-18 04:40:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 79f56166-0794-376a-867f-9222f4bbfc32 | -12.45589 | -49.59173 | 2026-07-18 04:40:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 02dfd1b4-c16f-3ffe-b31a-a8a907bcc887 | -12.44984 | -49.58712 | 2026-07-18 04:40:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 67c813b4-44b6-3abb-8b64-b372141b030b | -19.78308 | -48.26217 | 2026-07-18 04:40:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1880cb0d-29c8-3628-8316-062a8e343524 | -13.12025 | -52.51084 | 2026-07-18 04:40:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 985739e6-a0e8-36d1-96b8-5c0fcda76635 | -17.30461 | -51.71221 | 2026-07-18 04:40:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 28b42159-fe05-33ef-a386-b275b311e321 | -12.45314 | -49.58767 | 2026-07-18 04:40:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| afb6d969-c1aa-35c9-8572-1c21db48d8e5 | -13.31283 | -45.14935 | 2026-07-18 04:40:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 52cf586b-6df2-3941-8842-e009deb30fc4 | -19.71711 | -50.2107 | 2026-07-18 04:40:00 | NOAA-20 | ITURAMA | MINAS GERAIS | Brasil | 3134400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 3dba8e95-8ad1-3442-b2d6-516dada50af3 | -20.07183 | -43.71035 | 2026-07-18 04:40:00 | NOAA-20 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| eb5d6c82-d2ad-30bf-8edc-cee5db56a68b | -12.93439 | -56.64787 | 2026-07-18 04:40:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2137d3ef-f18e-3815-9ae8-cf6d2b36bb55 | -13.43825 | -43.85099 | 2026-07-18 04:40:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 44bfe51e-4548-3734-9cfc-85105ce881f3 | -15.3931 | -47.50383 | 2026-07-18 04:40:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1132ee2d-57e6-36c8-8deb-df61bc66fc17 | -16.51796 | -47.73275 | 2026-07-18 04:40:00 | NOAA-20 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 94966138-9e6a-3a64-96a1-a6f95292d166 | -13.55473 | -47.78265 | 2026-07-18 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0414d757-c3b9-381a-8f12-500ce1a689b6 | -13.314 | -45.15715 | 2026-07-18 04:40:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 64e82a3c-2f6d-39dc-a06d-ebc7b7520700 | -20.63148 | -41.3934 | 2026-07-18 04:40:00 | NOAA-20 | ALEGRE | ESPÍRITO SANTO | Brasil | 3200201 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 9b1ec4fa-c557-3e0a-aca0-6bec215242bf | -13.31614 | -45.14228 | 2026-07-18 04:40:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 000f9085-9ab2-3e5d-a247-eaf4638f7f80 | -13.57008 | -47.81948 | 2026-07-18 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e9545a68-ad7a-3628-931a-35fe5a3995bf | -13.55131 | -47.78219 | 2026-07-18 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 15252071-3ec8-31bd-aaf4-7913a12c32e2 | -18.7292 | -54.20226 | 2026-07-18 04:40:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 15c64d31-afa3-3587-a08c-09cc36080925 | -13.99877 | -54.00274 | 2026-07-18 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1bdb9287-474e-351d-a024-3c5d421628b9 | -13.31738 | -45.14492 | 2026-07-18 04:40:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 11501870-cf4f-30ad-8d41-59859cce21ac | -13.56665 | -47.81909 | 2026-07-18 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 098e8bf4-370d-3cdc-855f-69dd2ec4ea9b | -14.87978 | -48.46066 | 2026-07-18 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 19a6d3f2-0a68-365c-8739-f61d3af339be | -13.3135 | -45.14439 | 2026-07-18 04:40:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 75.7 |
| c51c44e2-bbc3-3070-8bf2-d8139a6f4ed4 | -18.73567 | -54.20786 | 2026-07-18 04:40:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 12a9d354-8b10-33bd-9fc5-3d43d92c33be | -13.31215 | -45.1543 | 2026-07-18 04:40:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| cf0e39aa-7254-3c69-a30c-149e47148e6c | -20.35538 | -48.31711 | 2026-07-18 04:40:00 | NOAA-20 | GUAÍRA | SÃO PAULO | Brasil | 3517406 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9b92815b-a01b-3c56-b7d6-852ee5d7797f | -13.31601 | -45.15487 | 2026-07-18 04:40:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 84f40e61-3656-3ed0-91e2-e8fa7985df55 | -14.00256 | -54.00347 | 2026-07-18 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ffd7d97a-b3f7-3220-ac36-bf6d8d8db8e4 | -16.06995 | -48.06 | 2026-07-18 04:40:00 | NOAA-20 | NOVO GAMA | GOIÁS | Brasil | 5215231 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 3ccdca36-37ee-3b69-8014-69a1753cfb9a | -13.3193 | -45.14777 | 2026-07-18 04:40:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 25.4 |
| b073cc8f-2932-34b5-9f42-9efdb6b31b88 | -15.66932 | -56.25019 | 2026-07-18 04:40:00 | NOAA-20 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1a3843d3-ba8d-3d08-8ae2-300192183ab7 | -14.31258 | -48.68602 | 2026-07-18 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 52c68fb3-c1fe-3fa6-9df8-8cb2c5e7fb73 | -18.73719 | -54.19909 | 2026-07-18 04:40:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 23.9 |
| bc3733d9-2138-3520-ac4b-8e3e07593f0a | -13.55815 | -47.78315 | 2026-07-18 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5164abfc-9398-3b2c-8a3e-260d9d0296c4 | -12.6594 | -48.22098 | 2026-07-18 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 97989bcd-fdee-3e5a-96df-7f17e9f9f096 | -13.57691 | -47.79749 | 2026-07-18 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f2e33a80-cfee-30fe-81f5-d0d7785fbc89 | -13.55984 | -47.79501 | 2026-07-18 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c0868419-687e-37a8-be41-efa6ae03151d | -20.63084 | -41.39997 | 2026-07-18 04:40:00 | NOAA-20 | ALEGRE | ESPÍRITO SANTO | Brasil | 3200201 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 8fbc5f09-280d-34f5-a628-51fd47d78650 | -20.52717 | -42.35827 | 2026-07-18 04:40:00 | NOAA-20 | PEDRA BONITA | MINAS GERAIS | Brasil | 3148756 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 386a0555-c75e-3bb0-b2cc-5f48f664ba3b | -15.99222 | -54.47742 | 2026-07-18 04:40:00 | NOAA-20 | JUSCIMEIRA | MATO GROSSO | Brasil | 5105200 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2c7fa550-25b7-36a3-be6c-bb6211407c70 | -15.24434 | -48.5772 | 2026-07-18 04:40:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4efd3a86-7528-38c0-a829-5e2d742dff12 | -20.32375 | -41.51026 | 2026-07-18 04:40:00 | NOAA-20 | IÚNA | ESPÍRITO SANTO | Brasil | 3203007 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |


[Clique aqui para ver as próximas entradas](README13.md)

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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 494a3883-9590-344f-b1f9-dbcdc2fa576f | -9.44478 | -46.81052 | 2025-09-05 04:57:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a093105a-de94-3570-8966-a211ce933054 | -12.71467 | -45.08124 | 2025-09-05 04:57:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 10412bfd-5e61-393b-a27f-cff6b03aee95 | -5.90383 | -57.72357 | 2025-09-05 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5aeb1872-e8bb-3b4e-9981-1ac714d9c5d1 | -7.88958 | -45.30419 | 2025-09-05 04:57:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7e556ef9-aced-371c-8e2c-bb59f4346395 | -9.63957 | -47.09894 | 2025-09-05 04:57:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8b6be195-1ad0-376e-8e58-e4800a3b40e3 | -5.95832 | -53.7975 | 2025-09-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 22491d25-bf5f-33e9-8ed4-191e4f770992 | -9.33861 | -55.21322 | 2025-09-05 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 58ac68d7-5dfd-3290-942e-9c23faa716d6 | -8.06856 | -52.37372 | 2025-09-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 963e7025-6b3d-3b90-a0cf-78bea452c4a6 | -13.27243 | -51.85161 | 2025-09-05 04:57:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1f41b309-8eac-3b94-b168-7460e75f0b59 | -12.9698 | -54.78408 | 2025-09-05 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aac33bda-000b-35e2-8f82-b75b2f8de9e5 | -7.76186 | -48.79154 | 2025-09-05 04:57:00 | NOAA-20 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 5264bfaa-b04f-30ca-80d3-20eb1d9bd242 | -10.51513 | -57.78054 | 2025-09-05 04:57:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d7e5370f-a906-3a23-bcc1-e96266a6c092 | -5.85815 | -57.76979 | 2025-09-05 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 5dc83676-efa1-3fe4-ac88-5301f6c4851e | -8.75412 | -46.11083 | 2025-09-05 04:57:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 985b900f-a417-3290-acf5-780106279523 | -12.98708 | -54.80524 | 2025-09-05 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bf8d19b8-8038-3c67-8b23-8f5d96400a3b | -11.20022 | -55.01452 | 2025-09-05 04:57:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 51196f06-d8e5-30f1-a0cd-80675a240ed2 | -12.98987 | -54.80936 | 2025-09-05 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| be6d986d-afac-3aab-9e19-0fa2ab129ad2 | -10.09288 | -54.78001 | 2025-09-05 04:57:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c5afa461-23bb-3ec1-ae8b-293630a7092d | -11.96558 | -46.77537 | 2025-09-05 04:57:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5f1e6541-2eab-35ef-a5ba-70385d2bbfd1 | -11.65534 | -46.86039 | 2025-09-05 04:57:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ee17de83-fe00-35bc-b65d-6f2b0e388656 | -7.68301 | -50.26252 | 2025-09-05 04:57:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 9108af62-0aa3-3b52-ac84-d5455d0851d2 | -12.48532 | -53.84401 | 2025-09-05 04:57:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0dbb6728-ef25-38ae-ae05-b6d87c39243c | -7.69595 | -50.30856 | 2025-09-05 04:57:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4eca4677-a218-3d4d-b58d-15db42e00375 | -9.05032 | -54.95263 | 2025-09-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 077f528d-ea64-33ec-8d16-c3d94dfb16c3 | -9.50442 | -57.82101 | 2025-09-05 04:57:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bbadcd74-3944-3cd4-99c8-57c2697f3d26 | -7.77674 | -51.08424 | 2025-09-05 04:57:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| acd0ef0c-eeba-3418-b1f0-72b3d7710030 | -12.52615 | -48.06689 | 2025-09-05 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f847eea1-f25b-30b5-84ce-260f534d8cb8 | -5.91193 | -57.72043 | 2025-09-05 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 40d604e8-996e-36d3-bf4d-df43765c42ba | -11.67337 | -57.34704 | 2025-09-05 04:57:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 860fb417-a478-390c-8932-8123369d835b | -11.03149 | -52.04919 | 2025-09-05 04:57:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 64a53b35-86c8-3b35-afbb-0501d6bbbfa9 | -7.05179 | -50.85802 | 2025-09-05 04:57:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8db1d6fd-5b74-33b2-ace8-68abc601da95 | -10.97017 | -45.96425 | 2025-09-05 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 152f4d76-5059-36bb-a852-8fb06c2ce8bd | -9.43906 | -46.81535 | 2025-09-05 04:57:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| aacb3d37-001e-3499-ab95-076ed201a485 | -12.71418 | -45.08541 | 2025-09-05 04:57:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 13.9 |
| ab370a83-e122-3438-8293-006edfa5aeb6 | -7.7976 | -52.13202 | 2025-09-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 2121f385-af84-3855-b6f4-52cbf8b246ec | -13.85641 | -46.26138 | 2025-09-05 04:57:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f83ee5dc-bb70-3ae6-b00e-18a7f69f2bf3 | -8.02184 | -44.77512 | 2025-09-05 04:57:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 83c15ef6-6777-3ef1-9afa-6c05fc55807d | -9.99331 | -60.0102 | 2025-09-05 04:57:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7b7843a9-e7c7-3734-a541-4c5d69951053 | -10.47536 | -53.62248 | 2025-09-05 04:57:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d5d73245-39ed-34a2-8d6c-de12d802766a | -9.98316 | -51.63754 | 2025-09-05 04:57:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 53e50e68-ad9f-3026-87c1-75dc7b6e993f | -10.47254 | -53.61829 | 2025-09-05 04:57:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3614259c-3266-34eb-8ef1-84ca723baef0 | -6.74077 | -58.73783 | 2025-09-05 04:57:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a406b928-8e28-3c24-8808-15dd509a093a | -11.1033 | -52.01968 | 2025-09-05 04:57:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 40839271-b437-3b75-b6ae-8dc9bbc33261 | -8.15875 | -54.94197 | 2025-09-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5af058e9-d1ab-3f1d-9444-0f5481290024 | -12.98763 | -54.80165 | 2025-09-05 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4beda83b-f6a1-33e5-a9d9-5a153460d457 | -12.90793 | -57.00383 | 2025-09-05 04:57:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 96cbf09a-83bb-3b77-9ba0-7c87f79038c0 | -9.07139 | -50.43021 | 2025-09-05 04:57:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| bde22aba-fb4a-311a-b748-b120ce455a5f | -11.55133 | -47.3163 | 2025-09-05 04:57:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4271b8bb-3fdd-3d88-be70-931535afeeb3 | -11.6342 | -52.21745 | 2025-09-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bb23014a-3ea5-3518-8fe4-b1d003c01e07 | -10.23152 | -50.54216 | 2025-09-05 04:57:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4ed377db-33ec-3025-adea-9e629184033b | -10.30411 | -54.14228 | 2025-09-05 04:57:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 221270ff-7a64-3956-8ed3-d4c49c675999 | -6.26163 | -53.44285 | 2025-09-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ed3f7b69-c8fb-384a-ad16-b0f29566f808 | -9.50691 | -57.78386 | 2025-09-05 04:57:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aa05d708-b3ff-3662-99e1-d224afe54018 | -7.89256 | -45.24116 | 2025-09-05 04:57:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1df48b1a-9db1-322f-a5a6-fd37e1696f96 | -12.88204 | -56.95087 | 2025-09-05 04:57:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e2a327c8-a9cd-3a44-b2e9-8ab388b4082a | -11.65154 | -54.53581 | 2025-09-05 04:57:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a1e26ff9-8850-341d-8ad5-4458f037dd5b | -9.07717 | -47.00042 | 2025-09-05 04:57:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| beea0081-645e-321e-a1e3-29ee431fd778 | -11.63058 | -52.21691 | 2025-09-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 583f96b1-5d89-3f04-9fba-44d77baf0ed7 | -13.85599 | -46.26492 | 2025-09-05 04:57:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 35c13c88-7cc9-3966-96cc-b9819fae4c05 | -8.89131 | -45.88434 | 2025-09-05 04:57:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c6fdbee3-2fdf-38fd-8334-6c8daaafe46c | -8.48256 | -45.07254 | 2025-09-05 04:57:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 52291b89-7460-3e67-9aa4-2ed7e094fe1c | -7.77414 | -50.97726 | 2025-09-05 04:57:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c7c33f4f-14aa-39b3-9df1-5a4ee6af65a3 | -10.97603 | -45.96127 | 2025-09-05 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a83ca5a6-7671-303f-8589-6bcbab9778e1 | -10.52631 | -57.77837 | 2025-09-05 04:57:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e2156d64-3916-325c-81f7-a836ca4dace5 | -11.00074 | -45.91622 | 2025-09-05 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 60a29422-e34c-3de5-8915-20c84265d6da | -7.36421 | -44.32127 | 2025-09-05 04:57:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 597fb146-acdd-37ae-8a07-b565b76c7d44 | -12.99046 | -54.82782 | 2025-09-05 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| dbd5574b-d24f-39b6-91bf-4b00eeae1df7 | -12.49101 | -53.85257 | 2025-09-05 04:57:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 98e40098-befb-3343-81c2-99e4fb85d4c3 | -13.30055 | -46.85119 | 2025-09-05 04:57:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 79a97f71-70c5-375d-a50a-1a4a9cbe3161 | -13.00936 | -45.2311 | 2025-09-05 04:57:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0dcf665b-bb42-3e2d-b2ff-efeca22532e5 | -11.64711 | -54.54242 | 2025-09-05 04:57:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 922f6f98-5b96-35f4-af3d-0603f74015e1 | -12.9663 | -54.79114 | 2025-09-05 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| d6ce8af8-31d6-39eb-80ca-57635a2d6572 | -10.97024 | -45.98552 | 2025-09-05 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 34476d9f-2dcf-3f7b-88c1-ca90fde1e83b | -11.17416 | -50.02417 | 2025-09-05 04:57:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b1ae8632-61d0-3a83-bff5-c4d7e97b000f | -11.58315 | -52.18098 | 2025-09-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3f479a12-e6b9-3c22-99d4-ea2f473f2e73 | -13.34012 | -54.38834 | 2025-09-05 04:57:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e8027717-120a-381c-a585-bfb8f863b470 | -12.981 | -54.82263 | 2025-09-05 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 90fd1064-bb32-3efd-aaf4-8cb424fd09f6 | -7.79701 | -52.1359 | 2025-09-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2d1f0b08-21fe-3590-8f10-999696a4f0b9 | -10.24794 | -61.78816 | 2025-09-05 04:57:00 | NOAA-20 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 77d3a481-d534-3f3d-bfe6-57693f34ef97 | -15.99627 | -55.95127 | 2025-09-05 04:59:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| a559e59e-174b-34fa-b427-120f8950ec43 | -16.3177 | -52.94565 | 2025-09-05 04:59:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0a562591-af7c-33ed-b9a5-67fbf77adeb6 | -17.66239 | -52.28506 | 2025-09-05 04:59:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 20b18b6e-b050-3685-8e83-2a96560a34b9 | -19.68473 | -54.80389 | 2025-09-05 04:59:00 | NOAA-20 | CORGUINHO | MATO GROSSO DO SUL | Brasil | 5003108 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8eba0ce5-5f45-3dd3-8e4b-d93cc163d333 | -15.8472 | -56.2318 | 2025-09-05 04:59:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2750c273-fb53-376b-bceb-76a388da812f | -18.46415 | -53.03891 | 2025-09-05 04:59:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 214403d4-888c-35d4-ada7-211e34a454aa | -16.30604 | -52.94853 | 2025-09-05 04:59:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 49196973-b9f5-3048-9f55-175b34a732e8 | -15.24281 | -59.00296 | 2025-09-05 04:59:00 | NOAA-20 | VALE DE SÃO DOMINGOS | MATO GROSSO | Brasil | 5108352 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 95619c5a-e3e6-3769-b27a-459f5c0a3447 | -15.24351 | -58.99883 | 2025-09-05 04:59:00 | NOAA-20 | VALE DE SÃO DOMINGOS | MATO GROSSO | Brasil | 5108352 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 891757ca-3669-37b6-ab38-596d49dea641 | -16.32071 | -52.95093 | 2025-09-05 04:59:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 900e80a2-108d-3b1b-83a0-e8dce2cc9c02 | -18.61393 | -44.26511 | 2025-09-05 04:59:00 | NOAA-20 | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 607af456-2f3e-3ae1-8b28-badf701a182c | -16.32316 | -52.96025 | 2025-09-05 04:59:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7d9d7951-ff43-30fe-8da6-8e9f944a2d65 | -19.68661 | -54.80975 | 2025-09-05 04:59:00 | NOAA-20 | CORGUINHO | MATO GROSSO DO SUL | Brasil | 5003108 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ff5dc055-3b17-3e5a-a0e5-edd092da5c08 | -19.68415 | -54.80801 | 2025-09-05 04:59:00 | NOAA-20 | CORGUINHO | MATO GROSSO DO SUL | Brasil | 5003108 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 923ad372-9c81-3384-8fbd-bc420c587a32 | -20.24044 | -51.30908 | 2025-09-05 04:59:00 | NOAA-20 | APARECIDA DO TABOADO | MATO GROSSO DO SUL | Brasil | 5001003 | 50 | 33 | nan | nan | nan | Mata Atlântica | 13.3 |
| 8bfd95f7-2fcd-3cb5-8c8a-7948659903ce | -19.68312 | -54.8092 | 2025-09-05 04:59:00 | NOAA-20 | CORGUINHO | MATO GROSSO DO SUL | Brasil | 5003108 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bec53595-bf17-399a-9bcc-daeeb8316f18 | -15.9896 | -55.97229 | 2025-09-05 04:59:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 51625a0b-4cb9-37e4-bc6b-e71f882c2fd5 | -19.68721 | -54.80563 | 2025-09-05 04:59:00 | NOAA-20 | CORGUINHO | MATO GROSSO DO SUL | Brasil | 5003108 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 90f305c2-562e-30b0-9c05-9a5dab5de2d5 | -18.46479 | -53.03419 | 2025-09-05 04:59:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 6f6e49e0-0414-3582-b72e-41b5aef532b7 | -16.32136 | -52.94632 | 2025-09-05 04:59:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6de4d51e-2cdd-3b30-9fd3-eea9c157d150 | -15.98848 | -55.97949 | 2025-09-05 04:59:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |


[Clique aqui para ver as próximas entradas](README56.md)

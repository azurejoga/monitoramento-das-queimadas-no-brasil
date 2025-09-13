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

## Dados Diários - Página 69

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 04b3b484-3094-3be5-8d60-b36f8b43ab29 | -22.79393 | -47.80208 | 2025-09-13 04:10:00 | NOAA-20 | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d7ebd0de-7a17-3388-8581-67b49c9daf3b | -15.20005 | -56.68735 | 2025-09-13 04:10:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| f7c89f04-9807-3639-8032-579b7cf78f1e | -16.25451 | -50.0746 | 2025-09-13 04:10:00 | NOAA-20 | AMERICANO DO BRASIL | GOIÁS | Brasil | 5200852 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3ee6e283-cc3b-3fdb-85c4-f344dc0df9f5 | -17.41595 | -49.25949 | 2025-09-13 04:10:00 | NOAA-20 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 2b119804-4a38-3806-8971-e69ddeab04bc | -15.02648 | -50.1412 | 2025-09-13 04:10:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 418c7991-6326-31f7-8851-4443100271fb | -15.57971 | -54.75605 | 2025-09-13 04:10:00 | NOAA-20 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 09cb0048-4b12-3589-8f38-208f12c46156 | -15.16206 | -52.48286 | 2025-09-13 04:10:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e84fe0c2-49af-37be-bb3d-ac0a5314e5de | -15.10915 | -52.50713 | 2025-09-13 04:10:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8f6288d1-faff-343c-82b2-9c3f28c07c48 | -15.68293 | -49.90032 | 2025-09-13 04:10:00 | NOAA-20 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 38.5 |
| f9f37e1d-6a36-345d-874b-049fe6832646 | -15.59266 | -54.77281 | 2025-09-13 04:10:00 | NOAA-20 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ef39c0be-5c60-3270-8f3d-25ebcbbe31d1 | -18.32999 | -50.97292 | 2025-09-13 04:10:00 | NOAA-20 | CACHOEIRA ALTA | GOIÁS | Brasil | 5204102 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 094617c9-8078-3f4d-92cc-e5fb0c7b4047 | -17.31369 | -46.66578 | 2025-09-13 04:10:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cabefdea-d00e-3d71-95d2-bf6b8ea155de | -16.08323 | -49.99273 | 2025-09-13 04:10:00 | NOAA-20 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6034e252-73c9-3d8f-92c7-3c1c4f35a15e | -22.22429 | -48.60804 | 2025-09-13 04:10:00 | NOAA-20 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 6e743875-d250-3e2c-a080-2d40eb7c906e | -16.08155 | -49.95404 | 2025-09-13 04:10:00 | NOAA-20 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| ecae2d23-c6f2-30f8-8fd8-9e6286d5e01d | -17.42513 | -49.23183 | 2025-09-13 04:10:00 | NOAA-20 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 59d9654e-a6ff-3c29-b55c-9e6080edbab6 | -17.41524 | -49.24066 | 2025-09-13 04:10:00 | NOAA-20 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 594ab9bf-2e5f-3814-ae1f-f0df19170400 | -22.54456 | -47.37053 | 2025-09-13 04:10:00 | NOAA-20 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d9035c84-e9b5-3eea-a914-ba2dc6547595 | -22.22868 | -48.60427 | 2025-09-13 04:10:00 | NOAA-20 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| e8f7aff7-5528-34c0-880f-1ef962733427 | -17.28748 | -47.25761 | 2025-09-13 04:10:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 17c0933e-e18d-3eaa-9863-1122e2424ea8 | -16.40517 | -49.03917 | 2025-09-13 04:10:00 | NOAA-20 | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 46707b68-dbee-3439-9773-b598cdff3b88 | -15.13287 | -52.49546 | 2025-09-13 04:10:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f3213c53-486e-3d1e-a5aa-60980cbbeec6 | -17.44321 | -49.24623 | 2025-09-13 04:10:00 | NOAA-20 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| efaa2c7e-8ceb-31bf-8e3a-be1f225b5028 | -17.71762 | -40.26218 | 2025-09-13 04:10:00 | NOAA-20 | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| e7b5a107-761b-366f-abae-799c10d132f1 | -18.89464 | -47.05811 | 2025-09-13 04:10:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ab81709c-8ff5-337c-81ff-c29da6cbdab6 | -19.63672 | -45.08264 | 2025-09-13 04:10:00 | NOAA-20 | LEANDRO FERREIRA | MINAS GERAIS | Brasil | 3138302 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| aef3973d-779d-36bc-9941-39e3954a9bb9 | -16.09579 | -46.95706 | 2025-09-13 04:10:00 | NOAA-20 | CABECEIRA GRANDE | MINAS GERAIS | Brasil | 3109451 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d5015017-6a55-30cb-865b-d1316bce6ade | -16.64539 | -47.7429 | 2025-09-13 04:10:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 836b4ba5-fb61-3864-9d9b-5262ba22d919 | -19.63731 | -45.07896 | 2025-09-13 04:10:00 | NOAA-20 | LEANDRO FERREIRA | MINAS GERAIS | Brasil | 3138302 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a789f600-7df9-35a8-ac19-7c5dc41b3563 | -18.39029 | -44.09701 | 2025-09-13 04:10:00 | NOAA-20 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9f816264-b35b-39dd-9352-a6ab025679e6 | -16.33628 | -51.52992 | 2025-09-13 04:10:00 | NOAA-20 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| e7e4e527-ccf4-3ddc-8e1a-aa7f51069e78 | -15.10165 | -50.17974 | 2025-09-13 04:10:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 763a5ce4-d06d-3f68-aa25-50ccaa9b23f5 | -14.63823 | -52.09247 | 2025-09-13 04:10:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 36681a13-9797-3c58-a2ad-725fe442c988 | -15.13464 | -52.48661 | 2025-09-13 04:10:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 369a0669-f96c-36d4-9ded-5acbae3b5e19 | -17.14176 | -48.50539 | 2025-09-13 04:10:00 | NOAA-20 | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ca7524a8-5856-3f4d-9ef5-1a034cb49d4d | -16.35817 | -51.51794 | 2025-09-13 04:10:00 | NOAA-20 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 95e37d48-c5a7-38ed-b6b4-951e27aad51b | -17.41255 | -49.23272 | 2025-09-13 04:10:00 | NOAA-20 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 977c0a5e-ea55-3756-af16-c24249e7056f | -21.30039 | -44.93538 | 2025-09-13 04:10:00 | NOAA-20 | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| ffb5846d-eac6-3147-ae8c-f8ccc071664b | -17.30828 | -48.73997 | 2025-09-13 04:10:00 | NOAA-20 | SANTA CRUZ DE GOIÁS | GOIÁS | Brasil | 5219209 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7827feaa-5792-393b-8a36-90dc4387b442 | -16.01934 | -47.93716 | 2025-09-13 04:10:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.9 |
| aacfb44b-d576-360f-9a79-75b31e4d9381 | -14.6369 | -52.09919 | 2025-09-13 04:10:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7504f7ec-84ad-358c-befc-30d5291a210f | -16.35777 | -51.54563 | 2025-09-13 04:10:00 | NOAA-20 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4be04b60-a3f4-3201-be04-ad0ac00076f2 | -15.70049 | -50.57832 | 2025-09-13 04:10:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8554e047-e7f9-34ea-bc1f-8f85ebbeb306 | -15.04516 | -50.16351 | 2025-09-13 04:10:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2dc2818b-97db-3af9-a144-db61e58c16f6 | -17.99573 | -46.9237 | 2025-09-13 04:10:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 84be5ab5-c018-3111-92ba-3f3ddd598066 | -15.70495 | -50.57936 | 2025-09-13 04:10:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c4ccd747-34f0-3b76-b45e-d4a0b5cf5afd | -16.41181 | -49.04816 | 2025-09-13 04:10:00 | NOAA-20 | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 45c39831-f384-3316-84f3-cc8dbbb1785a | -15.59533 | -54.76933 | 2025-09-13 04:10:00 | NOAA-20 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 92bb5813-53d4-3831-9e3a-c3eb2f8e9827 | -20.10174 | -46.92061 | 2025-09-13 04:10:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1a57a577-3844-3ddb-97f3-89130f360ef5 | -20.0249 | -47.63947 | 2025-09-13 04:10:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 756514fe-a21c-3843-a1fc-11370ec030d7 | -21.32213 | -44.99243 | 2025-09-13 04:10:00 | NOAA-20 | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| baeac61b-113b-36c4-b0ef-1d26ff1630e4 | -17.1351 | -48.51216 | 2025-09-13 04:10:00 | NOAA-20 | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e936ba7c-9344-3253-b53f-6132852b541b | -16.65774 | -40.8438 | 2025-09-13 04:10:00 | NOAA-20 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 7864559b-1901-3c09-9833-cd5752e47a95 | -16.49103 | -55.14616 | 2025-09-13 04:10:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| cfc00369-7d94-3ccf-8371-2b320df2d584 | -18.00349 | -46.94173 | 2025-09-13 04:10:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 37fd7456-6c94-39c6-a56a-323d96e5d703 | -16.56855 | -49.31394 | 2025-09-13 04:10:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e585b6d5-8d30-3948-90e5-56f09ecb754e | -18.04475 | -45.42531 | 2025-09-13 04:10:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c7372258-f4cc-38c7-b2d3-5281a92a633c | -16.13191 | -48.88372 | 2025-09-13 04:10:00 | NOAA-20 | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3ca5e08f-23e9-356d-8b68-5a239c6df059 | -21.49801 | -45.72073 | 2025-09-13 04:10:00 | NOAA-20 | PARAGUAÇU | MINAS GERAIS | Brasil | 3147204 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 783abe53-9a64-3306-a7a4-e9f300e1e600 | -19.25352 | -51.43147 | 2025-09-13 04:10:00 | NOAA-20 | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8f5b0e2d-4c0c-3765-95c0-c859c7b9b0fb | -16.55983 | -49.22264 | 2025-09-13 04:10:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e251a141-49a5-3c46-a982-38047ff43f7b | -19.64587 | -45.97028 | 2025-09-13 04:10:00 | NOAA-20 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 36193ed4-f460-36cc-b813-756664363193 | -20.44955 | -46.44374 | 2025-09-13 04:10:00 | NOAA-20 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5b060e5c-4dc9-3297-bdda-e6937e135bc4 | -15.13919 | -52.49056 | 2025-09-13 04:10:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 272bb0a4-ca2c-37de-a7ad-2a3433d9bfad | -17.23642 | -50.23074 | 2025-09-13 04:10:00 | NOAA-20 | JANDAIA | GOIÁS | Brasil | 5211701 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a7154cff-82ea-3ff3-b342-d5c8cd04d3ef | -21.58422 | -48.42329 | 2025-09-13 04:10:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 6c1e97d0-6c06-3305-95e4-4868b01558e7 | -15.76478 | -53.4926 | 2025-09-13 04:10:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9610d105-263b-394c-915e-0834c42f4a18 | -18.85338 | -46.8288 | 2025-09-13 04:10:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ca8272e3-81c3-35ba-8332-f10206b7b719 | -15.37644 | -52.10319 | 2025-09-13 04:10:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c25378b5-73ef-3f33-983c-fa9b3f17f670 | -16.06593 | -49.99022 | 2025-09-13 04:10:00 | NOAA-20 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 97e0d093-ad00-3450-8a0a-5f4297e47084 | -20.42203 | -50.7438 | 2025-09-13 04:10:00 | NOAA-20 | PALMEIRA D'OESTE | SÃO PAULO | Brasil | 3535200 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 4765b0b0-442b-361a-8200-97a88b77ada3 | -17.29767 | -47.24176 | 2025-09-13 04:10:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8a7c5d74-4294-333b-afad-fa98f7b52974 | -19.06735 | -46.64034 | 2025-09-13 04:10:00 | NOAA-20 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| eb0fa2bc-5004-35ac-8644-47a2732df7a3 | -17.35185 | -43.17945 | 2025-09-13 04:10:00 | NOAA-20 | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ff18b339-fba8-39ae-a273-3577162061f1 | -17.28776 | -46.09242 | 2025-09-13 04:10:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4ea17f57-974e-3326-80e0-f2e0f9bd2234 | -15.77436 | -52.23668 | 2025-09-13 04:10:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4b79d912-84c8-318c-be47-b40ad9093a2a | -21.58142 | -48.41809 | 2025-09-13 04:10:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 7173a0c2-e823-3b96-b7dd-198e4b5a85ce | -16.53061 | -51.75183 | 2025-09-13 04:10:00 | NOAA-20 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fab1c43d-51c2-3591-8b99-26f171b924dd | -18.00679 | -48.65401 | 2025-09-13 04:10:00 | NOAA-20 | MARZAGÃO | GOIÁS | Brasil | 5212907 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| baaba8ab-1aa8-3a9e-b466-ec6d7f759edb | -17.41126 | -49.23976 | 2025-09-13 04:10:00 | NOAA-20 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 22dce338-290e-3857-846b-efb8120b15a9 | -22.7974 | -47.80274 | 2025-09-13 04:10:00 | NOAA-20 | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d66c68f7-b968-3023-a9b5-37fa829c1b17 | -17.71326 | -40.26628 | 2025-09-13 04:10:00 | NOAA-20 | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 6ab93c53-bf9f-3360-9543-c002e7120769 | -19.98232 | -46.92017 | 2025-09-13 04:10:00 | NOAA-20 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 84834a42-b39a-37ee-a4f4-7ec52e5515ad | -16.26992 | -46.78217 | 2025-09-13 04:10:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d7d1bc90-4c7a-3150-99f4-ef1f67f6faf4 | -17.29183 | -47.25399 | 2025-09-13 04:10:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dcdf3944-ed8f-3179-b54f-73b7d9ecca54 | -20.01688 | -47.64764 | 2025-09-13 04:10:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5be708a4-3430-3af2-8a17-097d8fbf9d91 | -17.38996 | -43.52502 | 2025-09-13 04:10:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aa8246dc-f7b4-36a9-ba45-c00a61e7916e | -15.21196 | -56.69613 | 2025-09-13 04:10:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 61e99778-6e5e-3ae1-ac16-b709c97f7ae7 | -16.34207 | -51.52527 | 2025-09-13 04:10:00 | NOAA-20 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| bb3744ae-c0d9-38da-8cb7-33be4d15ac8c | -16.08232 | -49.94991 | 2025-09-13 04:10:00 | NOAA-20 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| dd4d4bf5-685b-34b1-a3c5-20f06d5220ab | -16.29685 | -50.03843 | 2025-09-13 04:10:00 | NOAA-20 | AMERICANO DO BRASIL | GOIÁS | Brasil | 5200852 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 919dbd72-8394-3315-84be-dea3c1abbc72 | -16.08006 | -49.96204 | 2025-09-13 04:10:00 | NOAA-20 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 21034813-166d-35e2-95cb-97b513e12d16 | -21.02176 | -48.41542 | 2025-09-13 04:10:00 | NOAA-20 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d26a9bc1-d782-3dc4-8565-d2f6038add35 | -18.70272 | -43.39156 | 2025-09-13 04:10:00 | NOAA-20 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 15784e6c-0a64-34e7-85b3-33c473a1aeeb | -15.08804 | -48.09844 | 2025-09-13 04:10:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d74b9eab-bcbd-3beb-b4ba-b885802bbb97 | -17.28615 | -47.24405 | 2025-09-13 04:10:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0bcf5d04-3009-3a1e-939e-73739dea3873 | -16.87646 | -49.34624 | 2025-09-13 04:10:00 | NOAA-20 | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9c7f82cc-24e7-35c5-a4d3-8969d4bdb95d | -18.77928 | -43.8007 | 2025-09-13 04:10:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b042c5e0-c934-316d-8bf1-4ac1a9b78ca7 | -18.43753 | -45.93501 | 2025-09-13 04:10:00 | NOAA-20 | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7b5afd2b-d6e8-3472-81aa-3f91f2912f99 | -16.8155 | -42.21836 | 2025-09-13 04:10:00 | NOAA-20 | VIRGEM DA LAPA | MINAS GERAIS | Brasil | 3171600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |


[Clique aqui para ver as próximas entradas](README70.md)

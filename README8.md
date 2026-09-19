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
| 3f43c393-9871-3f1c-811c-3344650298fa | -15.3647 | -49.021801 | 2026-09-19 00:19:00 | METOP-B | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 8171c6a6-e65f-34cf-88bd-b9ef2bb0d898 | -14.6694 | -46.6506 | 2026-09-19 00:19:00 | METOP-B | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| eeb0abc0-cb28-3445-b63b-299a3f3f2f3a | -1.2204 | -55.7131 | 2026-09-19 00:19:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 61a48b00-a781-34ff-ad7b-b37b0fbda9cb | -11.3706 | -44.1077 | 2026-09-19 00:19:00 | METOP-B | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8388c323-5a84-31e9-a31c-41541ad099c4 | -12.4847 | -50.010101 | 2026-09-19 00:19:00 | METOP-B | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7ffdf5a7-5ce7-3999-b87c-c4c09a3ea72e | -3.8159 | -50.744301 | 2026-09-19 00:19:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a8844115-a590-3a25-98db-315551aef290 | -10.7003 | -60.7188 | 2026-09-19 00:19:00 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 792d6fe4-2bd7-3187-9a1d-89b8b7b3c9f6 | -10.3626 | -48.896301 | 2026-09-19 00:19:00 | METOP-B | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2d1b619c-471d-3090-924b-a8895d9fe62d | -9.7761 | -45.049301 | 2026-09-19 00:19:00 | METOP-B | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 88efb238-f949-3c9b-b7a5-f977e80fafbe | -12.1226 | -46.980301 | 2026-09-19 00:19:00 | METOP-B | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0809d90d-c427-3087-ada6-a7e9ce6d7410 | 1.2661 | -50.954498 | 2026-09-19 00:19:00 | METOP-B | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 5ddfaeb3-bca9-3a72-b2a8-c8fa385edda0 | -1.6392 | -55.1497 | 2026-09-19 00:19:00 | METOP-B | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fdffa859-a1a9-3887-b0f7-0710fc3171a0 | -11.298 | -47.248798 | 2026-09-19 00:19:00 | METOP-B | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b9463c51-835b-38f0-8ac2-14054acd7c43 | -10.8929 | -54.0452 | 2026-09-19 00:19:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c0e0010d-4aca-3dce-af96-5dea8f337420 | -11.4381 | -51.455601 | 2026-09-19 00:19:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5ebd6b1c-cc4a-3a93-9ffe-f68bc8a60a0b | -11.4412 | -51.469601 | 2026-09-19 00:19:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 082ec6f0-3914-3e0f-96ce-d52860a8d32a | -5.5034 | -43.780499 | 2026-09-19 00:19:00 | METOP-B | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bd320c2e-c57d-37ec-8189-37244ad8c148 | -6.3589 | -58.2598 | 2026-09-19 00:19:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 79ba5a70-f96e-31e7-9ad3-067d5437a515 | -3.5568 | -50.287601 | 2026-09-19 00:19:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4ae62cd2-eef8-3815-a43f-4608cd7551d3 | -8.3586 | -47.217201 | 2026-09-19 00:19:00 | METOP-B | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6224ee9c-1841-3b64-8bd6-e94bf64ecbf4 | -10.9135 | -50.8587 | 2026-09-19 00:19:00 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e73412e2-3ea3-33d4-83fd-878ac4883eb1 | -10.3608 | -48.888599 | 2026-09-19 00:19:00 | METOP-B | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bc29e4d8-8f5f-31bc-b72a-73bd3632fc86 | -13.7428 | -48.7855 | 2026-09-19 00:19:00 | METOP-B | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 0359736b-8c34-3dde-a474-2e490c335853 | -7.847 | -44.875401 | 2026-09-19 00:19:00 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 4299a125-e3d3-3f4a-b768-54f0a2b71be2 | -10.9003 | -53.984001 | 2026-09-19 00:19:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 983e834b-e61d-3713-b2a4-d6458d57f87d | -12.3989 | -45.047001 | 2026-09-19 00:19:00 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| fcc0bf13-eff3-3314-8510-6678f65a0791 | -13.0643 | -47.378799 | 2026-09-19 00:19:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 016ebaa6-ea87-3ade-ae3e-7f252094ed23 | -6.3263 | -55.2757 | 2026-09-19 00:19:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b6278bc3-b56f-3ec6-9653-8ae7a6f2639a | -3.2622 | -54.2617 | 2026-09-19 00:19:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5aecc8c5-811e-32e1-8891-a38c5f20c687 | -14.6854 | -46.674599 | 2026-09-19 00:19:00 | METOP-B | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ac9b5708-a75e-3c40-bb99-bf9e3e7f762f | -13.6316 | -46.937901 | 2026-09-19 00:19:00 | METOP-B | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ba0e9553-1489-3ccb-95b8-cbfd040efad3 | -7.7755 | -44.878201 | 2026-09-19 00:19:00 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f28abcd4-6fa7-32de-8225-9c329ca66fa8 | -9.3904 | -45.371101 | 2026-09-19 00:19:00 | METOP-B | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 741fc591-38e8-397e-b486-60ea338acb98 | -1.5871 | -54.461399 | 2026-09-19 00:19:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0e6a98ed-fbaa-3f83-87f8-c4130b8f63e9 | -3.3407 | -59.7878 | 2026-09-19 00:19:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e67e9276-6aec-3982-8db6-b42518c4f958 | -13.6039 | -48.317699 | 2026-09-19 00:19:00 | METOP-B | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 1bf79335-47a5-3639-bdae-437fdd61af20 | -10.9202 | -48.408798 | 2026-09-19 00:19:00 | METOP-B | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9048ae80-5cd8-3a2b-b480-16b6faba598d | -11.9444 | -50.128201 | 2026-09-19 00:19:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f3c52e9a-86c0-36f7-93b8-dd5da6c3e208 | -5.8721 | -52.035198 | 2026-09-19 00:19:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7ec285e3-7aa3-3971-98c4-bb33c37e8e9c | -4.3874 | -55.244202 | 2026-09-19 00:19:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 76e8e460-06c0-3101-808f-91f43fb68338 | -5.8809 | -53.542301 | 2026-09-19 00:19:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1b41e2a9-e23b-31b0-a563-ad8ca7bfca06 | -12.1421 | -46.975498 | 2026-09-19 00:19:00 | METOP-B | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9856a9b3-2646-36b5-abdc-edbb76dd6f25 | -3.356 | -50.4459 | 2026-09-19 00:19:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| da3bb984-66f7-3759-ba3d-3cb5e8dbebd9 | -7.5567 | -61.2994 | 2026-09-19 00:19:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d72fb444-cf68-3888-8616-e7b46b8c58ba | -7.5539 | -49.599998 | 2026-09-19 00:19:00 | METOP-B | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1fa2cfe0-819e-32f8-bb8e-80b798ede321 | -3.3304 | -50.109299 | 2026-09-19 00:19:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 85b0a1e3-7163-3165-b795-0866911cc467 | -2.6614 | -49.483398 | 2026-09-19 00:19:00 | METOP-B | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 36aed5bd-7e14-30d6-a7b7-f75a661ba748 | -9.8813 | -49.090401 | 2026-09-19 00:19:00 | METOP-B | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d5863c22-29b5-309a-b6b0-aedada496d03 | -5.6091 | -45.238701 | 2026-09-19 00:19:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a320d0f6-0f87-3310-bbb4-f07f430005cb | 1.2607 | -50.9786 | 2026-09-19 00:19:00 | METOP-B | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 465aab8f-df67-3f5d-9d2d-e45cba521bf7 | -10.9104 | -50.844799 | 2026-09-19 00:19:00 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 29a995a6-02c9-3916-a124-d56292988b2d | -10.5998 | -46.1012 | 2026-09-19 00:19:00 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e6a448e0-f27b-3349-8718-72b47ce4e505 | -9.705 | -54.817699 | 2026-09-19 00:19:00 | METOP-B | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6ab4d8b6-f250-3b47-ae4c-e5aacecc7cd9 | -10.928 | -53.969601 | 2026-09-19 00:19:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f61a479e-cc97-385e-b559-410ea8656db2 | -11.0519 | -48.309799 | 2026-09-19 00:19:00 | METOP-B | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 795af21c-349a-33b1-b452-74770774709b | -7.2219 | -49.636501 | 2026-09-19 00:19:00 | METOP-B | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1eacda81-433d-375a-bf5f-a6f275475c9a | -9.0239 | -48.7309 | 2026-09-19 00:19:00 | METOP-B | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| bbfeabb6-24ce-3e31-960d-d3aeca69c2d4 | -1.7029 | -54.883701 | 2026-09-19 00:19:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6621afbd-36f4-3aeb-95f9-cd781a638a55 | -6.0119 | -51.787601 | 2026-09-19 00:19:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aa78eee4-984f-3897-9e68-d8e34fb0b7ea | -12.9775 | -46.969002 | 2026-09-19 00:19:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 73f5cc1c-b509-37a4-8eec-77b58687c8c8 | -8.3524 | -50.8358 | 2026-09-19 00:19:00 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c807a1bd-acc0-3ea0-a459-378cb12354fe | -1.232 | -55.718601 | 2026-09-19 00:19:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3670768f-2857-3388-acb9-e72eaf494526 | -3.3783 | -52.993301 | 2026-09-19 00:19:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0be3c0fd-b2e5-3ba2-be56-cc6ee6328cd1 | -1.68 | -54.919102 | 2026-09-19 00:19:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 359539fd-e9db-3c54-9c17-225e96a3a80d | -13.2334 | -46.9151 | 2026-09-19 00:19:00 | METOP-B | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ee3dec3f-e8d0-3a80-8821-51fc011c21c3 | -12.1312 | -47.016499 | 2026-09-19 00:19:00 | METOP-B | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f0099844-03c2-37cc-97b0-2f2d5bb53584 | -8.499 | -57.618301 | 2026-09-19 00:19:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 54e1a125-e475-31a5-b4df-58b542426981 | -11.0642 | -49.748699 | 2026-09-19 00:19:00 | METOP-B | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 48f505c4-2f1c-3461-86be-1a8baf2e3834 | -13.612 | -48.307701 | 2026-09-19 00:19:00 | METOP-B | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 60d4e484-dfad-3efa-85b0-9243da04a6a5 | -7.8567 | -44.873001 | 2026-09-19 00:19:00 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1c6f23bf-e38a-3329-ae51-98d2c8ef23a2 | -12.5425 | -47.0951 | 2026-09-19 00:19:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 300807e9-f2c5-338f-ac15-1e5af718291c | -11.8519 | -50.0383 | 2026-09-19 00:19:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5525ee8a-1df5-3999-8c74-960e6287ecc7 | -11.4598 | -47.671001 | 2026-09-19 00:19:00 | METOP-B | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d9100c8c-f6b1-3704-ba7a-3199bcacda1f | -11.0577 | -49.7654 | 2026-09-19 00:19:00 | METOP-B | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5f6e09be-5a8a-39e8-81f0-897f0bd6b4e2 | -7.8728 | -46.433601 | 2026-09-19 00:19:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 887d75d4-d7f6-3bd1-b77c-cff8140c630d | -1.5922 | -55.535301 | 2026-09-19 00:19:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e35dbf15-27bb-3398-bcf9-21a995f186cc | -4.4892 | -55.471298 | 2026-09-19 00:19:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0f0e5a62-a0d1-3626-8848-0df08b3e039f | -14.1785 | -47.8573 | 2026-09-19 00:19:00 | METOP-B | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 035208ee-88e5-3669-9c78-7c43c229030a | -6.0878 | -55.545799 | 2026-09-19 00:19:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ee32cd4c-f4a1-3f88-8d32-22cac0d05b65 | -10.874 | -56.187401 | 2026-09-19 00:19:00 | METOP-B | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1a449ad6-686f-3e52-b1d4-47859dd3de69 | -11.9362 | -50.1376 | 2026-09-19 00:19:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7850c326-652d-30f5-904f-bbbf8b5c70cd | -4.8763 | -56.059502 | 2026-09-19 00:19:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e5af5ffa-4896-3a46-8829-f08d6e183fe4 | -12.6072 | -50.925201 | 2026-09-19 00:19:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e63157f5-aa14-3f89-8a7f-e84dcbc95761 | -4.4009 | -43.630199 | 2026-09-19 00:19:00 | METOP-B | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| da4e0a86-a12a-3055-a4a1-c15cab6b03a6 | -10.897 | -50.877102 | 2026-09-19 00:19:00 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b81707e8-6afa-32cb-a3de-21ff78c4c59a | -8.1645 | -54.807999 | 2026-09-19 00:19:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 53dca67d-af83-3c2b-9fcf-01399f8f04d1 | -9.5593 | -45.471401 | 2026-09-19 00:19:00 | METOP-B | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| becc860b-eb05-3550-8ad0-c02e47cf30f0 | -10.1815 | -48.516899 | 2026-09-19 00:19:00 | METOP-B | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| dbd18543-ffff-363b-8868-d1267a77bdcc | -5.2518 | -49.410801 | 2026-09-19 00:19:00 | METOP-B | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6c032afc-3c31-3e9f-a5b1-53610653d7f6 | -10.5867 | -46.605 | 2026-09-19 00:19:00 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9f7ec28d-8430-303d-8971-75357f4a6d1a | -17.319 | -46.6171 | 2026-09-19 00:19:00 | METOP-B | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| bfa5ad7d-7f79-3de4-a49d-eec4f47ef1ee | -1.7012 | -54.876499 | 2026-09-19 00:19:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dfc4be0d-054c-3359-83d6-b29fa9e8a046 | -5.2223 | -47.556801 | 2026-09-19 00:19:00 | METOP-B | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ab21901d-d782-3d91-9543-041470a0bd0c | -5.9118 | -52.1199 | 2026-09-19 00:19:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e7f4535d-6570-38bf-8b6f-aec73ea4a95e | -12.997 | -46.964199 | 2026-09-19 00:19:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 46ace330-4493-3499-8b98-2ab1fac68efe | -5.9954 | -51.805698 | 2026-09-19 00:19:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eb2f0f76-20fc-35e2-8218-f291e0edef22 | -5.7597 | -57.424999 | 2026-09-19 00:19:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d2e70e26-385b-30b1-a89f-91dfa8db1fbb | -6.6205 | -55.681702 | 2026-09-19 00:19:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5af3927d-664d-31f6-abfb-2d741a7ce18e | -3.4528 | -50.599098 | 2026-09-19 00:19:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0358d36d-a93e-3c9b-8166-79a35b7231cb | -6.9365 | -55.0145 | 2026-09-19 00:19:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README9.md)

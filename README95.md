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

## Dados Diários - Página 95

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2c9e8ae3-16be-310d-a22a-98b7faf24494 | -15.72417 | -47.5986 | 2025-09-30 05:10:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 11.8 |
| d3e1e441-021f-3a32-a4e7-84688264d81c | -14.50769 | -48.46256 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e88d671e-b388-33e0-8a1f-b28917411633 | -14.5373 | -48.25027 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ade04469-2a9e-33ab-bbca-49bc79a3cb9b | -16.38707 | -47.03468 | 2025-09-30 05:10:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6fc01bdc-aa36-34eb-8bad-a7351da710a4 | -21.22836 | -47.13672 | 2025-09-30 05:10:00 | NPP-375D | CÁSSIA DOS COQUEIROS | SÃO PAULO | Brasil | 3510906 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b9959454-2e9d-36ab-a875-0b395b133957 | -15.20114 | -49.55337 | 2025-09-30 05:10:00 | NPP-375D | CERES | GOIÁS | Brasil | 5205406 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a5fbd664-3f51-3107-9360-688764e10102 | -14.51948 | -48.3865 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 09b9dcdb-51bc-3f8e-aafb-7ff19f72659e | -14.55119 | -48.2607 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| ffc58bfd-a44d-3f4f-be0c-8da79f3f1e07 | -14.70908 | -48.15953 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 9e5ae0db-c683-3887-9a9d-800842e10aea | -13.8323 | -47.50533 | 2025-09-30 05:10:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 458d4bd8-95c7-312a-87d7-9074342936ce | -16.42938 | -47.03591 | 2025-09-30 05:10:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 667fa460-5181-3ea6-a2f3-f26f0751e6a8 | -14.5158 | -48.46133 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f057fd90-767b-3127-8395-a321043868f7 | -15.28473 | -49.26769 | 2025-09-30 05:10:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9057ce55-432a-3b64-87f6-cad1b5504da0 | -17.40788 | -47.14858 | 2025-09-30 05:10:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3534977b-2472-387a-8f39-ed2c9b33ebe5 | -16.42497 | -47.02016 | 2025-09-30 05:10:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 07bc1b95-c617-3234-99d6-e2bf84a5666b | -15.27438 | -47.89111 | 2025-09-30 05:10:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ad5b4edb-8616-365e-9014-7f15dd54c4fb | -15.27398 | -49.25241 | 2025-09-30 05:10:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 73b6d805-d2b0-3254-81e0-1882d4b8c6f0 | -17.38917 | -47.15286 | 2025-09-30 05:10:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9113c155-cc48-393e-93f0-3a3a9ab72adb | -15.26863 | -49.49253 | 2025-09-30 05:10:00 | NPP-375D | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ed19a142-0c9d-3d58-96f8-f48686a0c3cd | -17.7528 | -51.34031 | 2025-09-30 05:10:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8821ce8b-44b6-3cc2-8c23-b22d114b594d | -16.38106 | -47.03416 | 2025-09-30 05:10:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f81034bb-3a60-300f-b5e0-23911202090d | -14.39199 | -47.13496 | 2025-09-30 05:10:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 38515aef-496a-302f-b02e-4ed091ae330d | -14.5322 | -48.48466 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b7e44b63-c71b-352f-a3fd-ccaff9b5213c | -13.81933 | -47.46933 | 2025-09-30 05:10:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 71843f70-f4a9-3564-b80e-92f1a1dfeba6 | -15.30166 | -46.40857 | 2025-09-30 05:10:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| eb26c113-2e2e-36ec-9df8-bbbef94d35c9 | -15.91746 | -46.24509 | 2025-09-30 05:10:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e0e28b21-b1e5-320f-b41a-35c4f863ae8d | -14.53971 | -48.22902 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cae92fbf-6115-3326-b071-933c961b3a73 | -12.79298 | -56.96075 | 2025-09-30 05:10:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4890bbe0-0874-36cb-94f4-e32c9b81dca9 | -13.72819 | -48.6865 | 2025-09-30 05:10:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| db9c5055-9beb-3f66-84e5-dd10faa2da87 | -13.82703 | -47.50148 | 2025-09-30 05:10:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1c92b3cd-b2af-36b4-84eb-fa5810387eea | -14.55347 | -48.25287 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3ee3b222-f923-3e5b-901e-6ab3813aa15e | -13.03284 | -56.89717 | 2025-09-30 05:10:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 98287602-0f31-31bc-9d1e-340f1638cf0d | -14.58823 | -48.28432 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eef30737-82c3-372e-b155-51687451158c | -15.27128 | -49.24953 | 2025-09-30 05:10:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2d28a472-7457-392c-8e33-3b5b99a9a3f4 | -13.84312 | -47.51043 | 2025-09-30 05:10:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a37abe4e-85f9-37f9-827b-d5a93897f40b | -16.20942 | -52.82484 | 2025-09-30 05:10:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c2d14123-4fdb-3798-8a63-b889cac52485 | -15.27997 | -47.89187 | 2025-09-30 05:10:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9a17b307-5029-3503-bd1d-5e9b3fda778e | -14.16639 | -52.86004 | 2025-09-30 05:10:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 54545538-36b1-33f0-b8d1-cb0ebbd62d74 | -14.57706 | -48.28606 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| baef9f4c-4e6d-38cd-a98b-e089b2466649 | -15.11679 | -46.4611 | 2025-09-30 05:10:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b85fc849-a896-32ca-82e7-67fb85f6b68a | -15.9297 | -59.50882 | 2025-09-30 05:10:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ad56e5fe-ee08-364b-9bfd-66597419f3c0 | -14.72931 | -45.22844 | 2025-09-30 05:10:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 63764249-1902-3998-b746-c327418def91 | -14.70985 | -48.15289 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 28c53ef0-bfb8-3193-93cf-36eabd20cdc5 | -14.50732 | -48.46578 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5c03d082-4749-3ef7-a1d6-381fd550d825 | -15.24694 | -49.71752 | 2025-09-30 05:10:00 | NPP-375D | IPIRANGA DE GOIÁS | GOIÁS | Brasil | 5210158 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 58a008b3-4e40-3325-bd2b-d5194138f42e | -15.72021 | -59.50776 | 2025-09-30 05:10:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 33216bd4-53cf-3554-9773-51f5e4908c29 | -17.91816 | -57.59128 | 2025-09-30 05:10:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 2ef5ac2f-326e-3926-a723-6ed38fe84a85 | -15.27696 | -49.27028 | 2025-09-30 05:10:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 849ece47-de0b-3d44-a26e-cf65b7f939a8 | -17.91537 | -57.58707 | 2025-09-30 05:10:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 37ff0d83-9adf-3784-a809-6daa9f77b1e3 | -12.70073 | -54.96743 | 2025-09-30 05:10:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3798236a-45ae-3208-97f6-df86ebd9ebaa | -15.92294 | -59.50752 | 2025-09-30 05:10:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| feffbc87-53bb-3991-8373-a4405eb6aae0 | -14.66564 | -48.1433 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ab14018b-1969-3ce6-8186-5c0cd5d9c3ac | -15.82282 | -48.16904 | 2025-09-30 05:10:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ebdec3df-9cf7-3256-874e-66ee34a7e935 | -15.06794 | -45.06129 | 2025-09-30 05:10:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7806558c-f081-3253-ad90-b65e98d85fab | -14.54167 | -48.24867 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5cc30d7d-641a-3343-bcf5-6a3d5f4341f7 | -15.79547 | -59.51658 | 2025-09-30 05:10:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e0b54568-c5ad-3f8f-bba9-890c68b93222 | -14.85895 | -54.76432 | 2025-09-30 05:10:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9cf681a4-6ccf-3604-af21-adcf813c7b9f | -14.80997 | -59.70678 | 2025-09-30 05:10:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 28735691-7a26-3236-9723-2abb04a118ea | -15.72463 | -47.59446 | 2025-09-30 05:10:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 5b721e0d-f31c-3982-a9c0-b538d25cb4aa | -14.78576 | -48.31323 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7164f041-fa7e-31d9-bb7d-b54273cb232f | -15.3379 | -47.83315 | 2025-09-30 05:10:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 59f2ab03-b0a9-3cc1-881a-47ae394c9396 | -15.27438 | -49.24914 | 2025-09-30 05:10:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2db616f5-9a3e-3fce-8791-60c29b98ccd1 | -13.80491 | -47.97258 | 2025-09-30 05:10:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| df62ffa5-b5ad-35a3-8bef-38a59e580088 | -17.90529 | -57.58551 | 2025-09-30 05:10:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 0a38ca3b-c2ed-33b5-8a3b-4835a19cec01 | -14.52291 | -48.42429 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d2cd0e0f-b0f5-395f-8344-6542d8249eb8 | -14.52761 | -48.38321 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| dc24277f-c03c-30fa-8e0f-bf07fb0411dc | -14.52824 | -48.47207 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 69beebc4-ea05-3c75-85d1-1156cd35d7a1 | -14.69485 | -48.23441 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5781d042-21bb-312d-96cc-ee948713c9f3 | -15.66131 | -51.3317 | 2025-09-30 05:10:00 | NPP-375D | SANTA FÉ DE GOIÁS | GOIÁS | Brasil | 5219258 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3fe484d7-079e-3696-9ac2-3c1635a5bd22 | -13.22893 | -50.93027 | 2025-09-30 05:10:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 9.2 |
| eac19b6b-cf1b-3902-b4a8-eeec477f0884 | -14.7416 | -45.66136 | 2025-09-30 05:10:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c8dc8eb4-f244-3268-b033-415473ab6af2 | -14.55737 | -48.2667 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d77ac2e3-2762-3570-8fb9-eae2ef748afd | -15.17508 | -56.51403 | 2025-09-30 05:10:00 | NPP-375D | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0fa6ae81-3d55-3cdc-a06b-9c0487e8a15c | -15.25056 | -56.79812 | 2025-09-30 05:10:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7ebb34c1-957b-3bb4-96d5-3610d35bc000 | -13.76749 | -48.32504 | 2025-09-30 05:10:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 243818d3-11a0-342b-b8e4-8b9859af76ad | -16.67574 | -44.56312 | 2025-09-30 05:10:00 | NPP-375D | CORAÇÃO DE JESUS | MINAS GERAIS | Brasil | 3118809 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0c9beb61-fe23-39c6-bd02-0ba57516288d | -12.39699 | -57.57861 | 2025-09-30 05:10:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b9e366bf-2fe0-3767-a111-46db91f3bed7 | -17.3959 | -47.14664 | 2025-09-30 05:10:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5d185ef8-494c-39ed-bea5-190a6d632ae5 | -13.71788 | -48.64161 | 2025-09-30 05:10:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0ab39b46-463e-3057-b785-2393d7b99b70 | -13.73375 | -48.6843 | 2025-09-30 05:10:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| a285401b-f149-3270-87cf-c10cd2620f29 | -14.57906 | -48.22163 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fe004771-3c6d-350a-954d-384b0fc55f87 | -13.80563 | -47.96661 | 2025-09-30 05:10:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dd8bcfb9-8485-3005-9f39-c7d1e550839d | -15.27919 | -49.2707 | 2025-09-30 05:10:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7cd885b2-26fd-370d-a5b3-9d9bc5ed2ff8 | -13.72313 | -48.64195 | 2025-09-30 05:10:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a8e6853c-acea-3bc7-b94a-8ab675104b80 | -13.82235 | -47.49268 | 2025-09-30 05:10:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e3e799cc-6c06-343d-943f-d68f16f8aa22 | -16.41109 | -52.17576 | 2025-09-30 05:10:00 | NPP-375D | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 85c985c0-4581-3b98-a0f9-930e413499d9 | -17.39157 | -47.14136 | 2025-09-30 05:10:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1d82f33e-7fbc-3db7-9d3f-875922b7a9e5 | -17.41442 | -47.15661 | 2025-09-30 05:10:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e1eb81a1-d446-3eaa-904d-cb19b90c2c34 | -15.71834 | -59.51914 | 2025-09-30 05:10:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5689b7b3-fb8e-3929-9641-db29a94570b7 | -14.70254 | -48.16821 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 032f2058-3c40-37c6-98bd-2c63d5b32643 | -15.92575 | -59.46928 | 2025-09-30 05:10:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 57be3842-e7e6-32d5-8965-84525075658c | -17.71852 | -56.76323 | 2025-09-30 05:10:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.5 |
| 63609209-5d17-3d89-86ef-18ae90891443 | -16.65554 | -49.53328 | 2025-09-30 05:10:00 | NPP-375D | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cdfccc34-40da-3b89-b0b3-076e3843403d | -17.40738 | -47.15326 | 2025-09-30 05:10:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4e6c242e-5a28-32c9-b57e-19a6e5dbdd07 | -13.63162 | -48.03098 | 2025-09-30 05:10:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6854c373-6963-3bfb-8772-2222394354a8 | -15.25029 | -48.74219 | 2025-09-30 05:10:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 55a6fdf6-475d-3221-9f0e-f1096166743b | -13.23277 | -50.9353 | 2025-09-30 05:10:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c8f34dad-4bae-3ea1-be18-22b732a24a41 | -15.92803 | -46.20271 | 2025-09-30 05:10:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| da1ab591-5e55-35c3-807f-6cb35b50b072 | -15.17744 | -46.40823 | 2025-09-30 05:10:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f9ed52b2-b6a1-3554-b71f-ff4057550c9f | -14.54618 | -48.25674 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |


[Clique aqui para ver as próximas entradas](README96.md)

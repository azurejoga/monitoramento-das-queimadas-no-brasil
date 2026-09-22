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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a7b4eab7-d7e0-3eba-b163-285268d0e5fc | -11.88085 | -46.84402 | 2026-09-22 04:49:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 05a6c174-c91a-3e77-ae28-7c9ddca16d94 | -14.6675 | -45.66471 | 2026-09-22 04:49:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9e97743e-502a-3257-9c1a-b07349e27646 | -11.43439 | -47.34688 | 2026-09-22 04:49:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ca1fcab6-9dd5-3fa0-9a78-d997377e161e | -11.04343 | -54.14965 | 2026-09-22 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8627b035-5549-38c0-b528-bd7f39408354 | -15.3627 | -48.10956 | 2026-09-22 04:49:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ce9682ef-83d9-3be3-8289-0608979d86d0 | -11.44089 | -47.32911 | 2026-09-22 04:49:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 89385447-6940-3454-ae7c-64d7ca6f9c1c | -11.42929 | -47.35453 | 2026-09-22 04:49:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5bfb55e8-af85-3fa4-b84f-424925c0546b | -12.93637 | -51.04274 | 2026-09-22 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 342a85bf-85c0-3fbb-a9d8-7797bfd21c3c | -9.55675 | -66.04214 | 2026-09-22 04:49:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 29fbf155-cd4e-3b5f-854f-3b66a8d52b6e | -11.93868 | -46.51416 | 2026-09-22 04:49:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c6116e5b-a93a-346f-b939-270adf8087d7 | -14.9173 | -49.89574 | 2026-09-22 04:49:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 27f07300-a151-3936-ba58-0687033f6561 | -9.56765 | -66.04088 | 2026-09-22 04:49:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7518b76a-1253-3465-98f5-326cc97eb0d1 | -12.1449 | -61.17348 | 2026-09-22 04:49:00 | NOAA-21 | PARECIS | RONDÔNIA | Brasil | 1101450 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 55d04a6e-4f19-3e7c-8b7a-05b1d4f59e66 | -9.56102 | -66.02044 | 2026-09-22 04:49:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7f2560fc-434c-3bed-afd2-4b1f635060a6 | -13.86931 | -48.56961 | 2026-09-22 04:49:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dede5fd8-555e-312c-a91e-640935554763 | -11.46732 | -47.75203 | 2026-09-22 04:49:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6520f033-12a6-3904-add7-bf4185ed38be | -12.93844 | -50.91336 | 2026-09-22 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0520a5ae-f4af-3915-9b1b-6f6b9b1cf81f | -12.93012 | -51.01515 | 2026-09-22 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 02a38ecc-cf70-3f2c-9847-4d144bb7aaf1 | -11.50589 | -51.51115 | 2026-09-22 04:49:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f640ecd6-6515-3cd1-aebe-483e075ac1d6 | -12.14143 | -47.3954 | 2026-09-22 04:49:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0567308c-d4a8-3818-9f1f-6d07aad7a65f | -11.50365 | -51.50351 | 2026-09-22 04:49:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9960793f-03d2-3a3f-8d81-92a7d0f49db0 | -12.93564 | -50.93206 | 2026-09-22 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 89f25969-377e-351c-871e-119ce2ab7c7c | -13.29554 | -51.76286 | 2026-09-22 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 23c59873-929d-3e26-bc5e-888a3f12b4d3 | -10.90921 | -53.95987 | 2026-09-22 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ad609f57-f029-3250-b8f2-052144356413 | -11.9432 | -49.76987 | 2026-09-22 04:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| eeb4082e-c44e-3dcf-9ef7-f00aae0dd400 | -12.66678 | -50.95188 | 2026-09-22 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a071597c-4a2a-3614-a6d2-71af16960997 | -13.33056 | -51.28823 | 2026-09-22 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| cfdfa996-4785-3b6c-96a2-c67c7da76657 | -12.31705 | -54.11915 | 2026-09-22 04:49:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 12624fef-4e39-3d0d-b48e-c96ebeb9b922 | -12.95092 | -50.92296 | 2026-09-22 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 111b50ec-29be-38c6-a643-b439412b4b38 | -11.27955 | -54.12681 | 2026-09-22 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5aa42d53-26e7-3ea9-8906-736a793e596a | -9.56051 | -66.03961 | 2026-09-22 04:49:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0aac3895-fdcc-3622-9f5b-9f90f6038d42 | -11.32522 | -54.0391 | 2026-09-22 04:49:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 1c142fc9-f45a-3294-9eba-bbc66aae7cf3 | -12.88638 | -50.93586 | 2026-09-22 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 00bac752-21f8-3daf-8e7d-4991c0350f3c | -11.75771 | -50.81759 | 2026-09-22 04:49:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 51cff7e0-e717-3caf-83f5-6ae773ad7ede | -12.19952 | -47.03538 | 2026-09-22 04:49:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 999d3e0f-b526-3ba0-b2de-ca7cf4dd9b3f | -11.70024 | -50.99249 | 2026-09-22 04:49:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 21.8 |
| aca68407-d228-36f1-b258-5b4bf01b7d6b | -10.90476 | -54.07348 | 2026-09-22 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8af3d4c7-f343-30ec-aefc-df95ef633545 | -9.56528 | -66.03634 | 2026-09-22 04:49:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 473fd50a-00e8-326f-a432-f22fc9bc5991 | -11.33034 | -51.37035 | 2026-09-22 04:49:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 267bc0e3-9336-39ab-aa6a-5e00a425e266 | -10.60829 | -53.99446 | 2026-09-22 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| fa9689ad-2a0c-3b2f-aa19-b67c5f7eed09 | -12.89769 | -52.07674 | 2026-09-22 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 088e2b58-480a-367f-86db-48d6bb86d843 | -16.67586 | -41.85362 | 2026-09-22 04:49:00 | NOAA-21 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 943bbda3-6209-3377-a79f-d55ab0c707a7 | -11.01276 | -54.14454 | 2026-09-22 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aa62ec78-9dfb-34c9-957c-c0302216c18b | -11.41737 | -47.35201 | 2026-09-22 04:49:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2f2db0ae-c99e-30ad-9b0c-21ff6ab1e228 | -10.91719 | -53.9536 | 2026-09-22 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 57572d8d-8553-391e-bd54-f6a6dcc6ab58 | -15.44208 | -48.47526 | 2026-09-22 04:49:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 761264b9-19f6-3802-b768-34be15998095 | -13.90529 | -48.5642 | 2026-09-22 04:49:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| dbbc0b8c-d121-3e4a-8841-ca28e0921fc6 | -12.14242 | -47.3883 | 2026-09-22 04:49:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7a93b05b-45dc-3f57-ae4d-2105d30e7fab | -11.35372 | -51.39591 | 2026-09-22 04:49:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6af37f9a-b879-3af8-9ad5-9a2bccfcc146 | -13.40082 | -49.47649 | 2026-09-22 04:49:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b3c8f6f1-c703-3dfb-8f0a-2c0ab745c4da | -12.95606 | -50.95819 | 2026-09-22 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5f4f6ce2-6f93-3ed1-8ef3-3e2c080ff38a | -12.40599 | -47.07322 | 2026-09-22 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| b82db8a7-cee1-352c-8543-2db590f9dd94 | -10.41484 | -53.79955 | 2026-09-22 04:49:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 862bf518-7ac1-3ad1-af96-f3467557493f | -13.20516 | -51.68636 | 2026-09-22 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 90f62e2b-2956-3473-8ec6-8aa79883e276 | -13.46793 | -46.90939 | 2026-09-22 04:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a6ffdae9-9ba4-3532-a9e3-9ca142507fc8 | -13.28281 | -51.77928 | 2026-09-22 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0d75b9be-5229-3ae7-982e-576f185fc98a | -16.78921 | -49.41204 | 2026-09-22 04:49:00 | NOAA-21 | ABADIA DE GOIÁS | GOIÁS | Brasil | 5200050 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 77d4761a-406f-373f-9de0-38a9f1a3240b | -15.45983 | -48.40336 | 2026-09-22 04:49:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a9eed67c-c6ca-3c29-93bb-eac36d3d453a | -12.14695 | -47.3853 | 2026-09-22 04:49:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| bb945308-cd6d-3555-822d-f7aaace155b5 | -12.35436 | -50.22188 | 2026-09-22 04:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8db72466-9265-353c-b458-526e8e970315 | -15.85994 | -49.88432 | 2026-09-22 04:49:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 0140e6a0-24a6-3ee9-9991-2e56060fedec | -11.32143 | -51.36165 | 2026-09-22 04:49:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 81000802-5db7-3acb-94d4-17c7b0278379 | -10.54308 | -57.44012 | 2026-09-22 04:49:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 35317ebc-7fa5-3e6b-94ad-464e6dad94e0 | -11.03381 | -54.1442 | 2026-09-22 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bec69cae-45e7-3472-853e-d49cabfa49cd | -11.75476 | -54.5723 | 2026-09-22 04:49:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bdb9758a-d2e8-36f6-99d7-abbe3771c7b7 | -11.42132 | -47.35303 | 2026-09-22 04:49:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f874d793-2bc2-39b0-a421-0b66c133d6dd | -10.71434 | -54.01183 | 2026-09-22 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4214fad1-5670-3197-9753-70ae5e5d86bf | -12.43778 | -47.01117 | 2026-09-22 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d6167188-aa8f-388c-94c3-586fea583506 | -9.27895 | -60.63673 | 2026-09-22 04:49:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e7e9331e-42ff-3c0f-8159-587258b6123a | -11.03721 | -54.14478 | 2026-09-22 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 92149486-55a6-3128-a150-0354231f6f7f | -11.96369 | -46.5148 | 2026-09-22 04:49:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a6547d11-360e-30f2-8fc1-5de8c727fcc0 | -11.33143 | -51.36322 | 2026-09-22 04:49:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1f008f89-e1df-3063-a4ae-a6877d59ff63 | -11.95888 | -46.51841 | 2026-09-22 04:49:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8da05b7f-bf76-3bb6-ac86-06ba7203a82f | -10.72353 | -53.99807 | 2026-09-22 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1d3ce866-6f59-32da-bd86-da269f1a7ccf | -12.68316 | -46.39125 | 2026-09-22 04:49:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b20511eb-2b6d-34eb-bd03-40bf7306e1d2 | -13.27169 | -51.33548 | 2026-09-22 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 42db237d-1ffa-3ac8-b916-aaaaac62d611 | -14.16737 | -51.79251 | 2026-09-22 04:49:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ad74ff55-69cf-3b58-9656-1d73b4b868ba | -15.45325 | -48.48175 | 2026-09-22 04:49:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b739f511-0894-3b59-9c2d-455c4f548b11 | -9.55906 | -66.04673 | 2026-09-22 04:49:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 04f8d45c-ecb4-3f43-93ae-3794074e5e00 | -12.94983 | -50.95339 | 2026-09-22 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6b16dda9-b5dd-3a1c-b987-81c2d3829279 | -11.44138 | -47.32552 | 2026-09-22 04:49:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c45631f5-ddf3-3a02-a560-743eea48b5a4 | -11.50202 | -51.51418 | 2026-09-22 04:49:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b878c090-77ba-331a-864f-5f9578384118 | -10.60429 | -53.99762 | 2026-09-22 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3b4494ee-3c04-3a18-aea5-446cd0f16df8 | -11.50257 | -51.51062 | 2026-09-22 04:49:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 31777a22-36d0-39ff-8424-754358371cf8 | -14.77059 | -48.44191 | 2026-09-22 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 81e4ff14-c7a3-383c-8778-bfec16b8bb76 | -11.69687 | -50.99196 | 2026-09-22 04:49:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 14.6 |
| af23a8b8-60d6-37d9-80c9-63ac382da023 | -11.27894 | -54.13054 | 2026-09-22 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| eff8a388-d44b-3a35-a4c0-a29991e5c56a | -14.92052 | -45.14623 | 2026-09-22 04:49:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 858fbc08-5709-3f29-b4ea-f654147b3012 | -13.63299 | -42.48003 | 2026-09-22 04:49:00 | NOAA-21 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b1f270e8-52c5-3b75-bc4e-54026fd32e7c | -14.68567 | -45.67225 | 2026-09-22 04:49:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 9f31e4b6-083c-361a-8bc6-dd0672445ea1 | -10.8753 | -53.95431 | 2026-09-22 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a1758b7d-12fa-35db-afc0-ef6817e2ca96 | -12.28953 | -50.73122 | 2026-09-22 04:49:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| de2cad05-65af-3abb-adda-2be5c609c470 | -12.24144 | -54.285 | 2026-09-22 04:49:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eb66b748-9301-3869-9185-d5fd8d0a1ab3 | -12.56064 | -45.96149 | 2026-09-22 04:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 36.0 |
| 9ce4a074-58b0-3322-b8f6-aaed5da8a28e | -14.66689 | -45.66981 | 2026-09-22 04:49:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b01a7b8a-f81b-3838-974f-c929544883c6 | -11.44843 | -47.33386 | 2026-09-22 04:49:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| fe980d99-9dbc-3c94-9b37-e14344ed40c8 | -15.44028 | -48.45875 | 2026-09-22 04:49:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| aa0b73d0-a117-3c22-8c23-1e023a95cc04 | -10.87727 | -56.24068 | 2026-09-22 04:49:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 07132e4e-9b58-390e-835d-d9b03c34d7d4 | -10.2249 | -59.40347 | 2026-09-22 04:49:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4ebff670-a35b-3d76-a4b1-961aa1bc3564 | -10.90416 | -54.0772 | 2026-09-22 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README68.md)

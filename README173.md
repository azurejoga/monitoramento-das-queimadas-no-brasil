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

## Dados Diários - Página 173

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8f69ff17-a639-3439-a851-be3b19ecaf21 | -12.63365 | -53.11651 | 2024-10-09 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 60d190bd-ccc1-3f90-a8ac-07157ddbb267 | -12.63054 | -53.11129 | 2024-10-09 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 613069bf-7137-3296-86db-52657868f6cd | -12.62987 | -53.11595 | 2024-10-09 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ed82b7e7-dc0f-32f1-9881-8f14004ac6ee | -12.62941 | -53.50069 | 2024-10-09 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f9c14877-3bc8-3256-8305-2204df0f65a9 | -12.6292 | -53.12062 | 2024-10-09 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4971a218-7d1e-30d9-b0bf-7de7bb0c8bf5 | -12.62852 | -53.12532 | 2024-10-09 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 04004bbe-db30-388d-ab8c-98247d44a660 | -12.62542 | -53.12006 | 2024-10-09 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a11c2d6b-3e44-33a9-bd94-b5d182d1f21b | -12.61547 | -53.02746 | 2024-10-09 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2690ed45-a4d9-3f37-8b59-647d2f6aa30c | -12.61167 | -53.02689 | 2024-10-09 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8fe94dcb-6dde-37c0-aee2-36588adfe5b1 | -12.611 | -53.03162 | 2024-10-09 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7ad60c82-0033-3e72-b0fe-b3264800955b | -12.60721 | -53.03105 | 2024-10-09 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f48a766d-0142-3718-9d9b-e24c3408bb0c | -12.60653 | -53.03579 | 2024-10-09 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9698f513-46ed-3695-a163-824e0b2d1575 | -12.60274 | -53.03522 | 2024-10-09 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6df8a02a-89da-3b42-b6ed-aea37b8158dd | -12.60143 | -53.12607 | 2024-10-09 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 06ff8c80-e422-34cb-b487-0cdfa2dcc71b | -12.60077 | -53.13074 | 2024-10-09 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6128a655-9455-3351-9155-8aca67c9e41e | -12.6001 | -53.13542 | 2024-10-09 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f5cb0c10-7549-30ff-92c7-fd935f6af065 | -12.59766 | -53.1255 | 2024-10-09 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3470f21f-b283-3210-91dc-36f981e5a62d | -12.58357 | -53.06137 | 2024-10-09 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 82d9cb09-0f0f-3a85-97c4-7d75219752b4 | -12.58291 | -53.06605 | 2024-10-09 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d6aff3ba-6d91-3264-b7e6-a003b35c21ea | -12.58225 | -53.07074 | 2024-10-09 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2c7318ff-9fc8-3d97-8af4-1b7349f8e5d8 | -12.57913 | -53.06548 | 2024-10-09 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 8526e7d5-6afa-3b56-a80d-0c69b6a45a7a | -12.57847 | -53.07018 | 2024-10-09 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 07107d24-d4fe-3459-beaf-615ea3b7ec71 | -12.57534 | -53.0649 | 2024-10-09 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 3bece853-ebf9-3ac2-afff-8e89ed05a1ba | -12.57468 | -53.06963 | 2024-10-09 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 5e7c2461-ebd9-326f-89f9-7bfd01908107 | -12.57156 | -53.06432 | 2024-10-09 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7d2854a2-05b1-3aab-850f-23dfcf1e00c0 | -12.5709 | -53.06908 | 2024-10-09 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 105a0944-0620-3a07-a610-4292c02817b2 | -12.56777 | -53.06375 | 2024-10-09 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f393770a-b955-37ab-be1a-dfec5b6bd1c0 | -12.56711 | -53.06851 | 2024-10-09 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 35470ab7-887e-383d-945a-2225f66464c4 | -12.56332 | -53.06794 | 2024-10-09 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bf83c7ed-01e7-394a-8e6e-36ae756cd04e | -12.47841 | -53.14899 | 2024-10-09 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 00c0ffaa-cce7-3a4c-bc60-4bfb77928d12 | -12.47465 | -53.14844 | 2024-10-09 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a5da190f-b11f-3355-a723-5f3e7565350b | -12.87822 | -54.03073 | 2024-10-09 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 66339a4e-3970-31c7-a24b-e8ae79e3a191 | -12.87462 | -54.03018 | 2024-10-09 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d48e79bb-86bd-3c0b-8f98-c58f14960a12 | -12.87401 | -54.03441 | 2024-10-09 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 81038387-75da-3b61-ac9d-47a55c519a3f | -12.8734 | -54.03864 | 2024-10-09 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9d54a904-6bc0-3dd8-86d0-5d8776555102 | -12.70396 | -54.11857 | 2024-10-09 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f9d3f297-4afa-36c2-8977-025589ff6f71 | -12.70037 | -54.11805 | 2024-10-09 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f1206a0b-c9c8-33dc-bb8d-a6cd76f7cea5 | -12.69679 | -54.11751 | 2024-10-09 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f95e9b54-0c3f-3390-a96b-a26296f23793 | -12.69381 | -54.11281 | 2024-10-09 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 778ab717-db2a-35da-9a81-68ea8994203a | -14.83494 | -53.9051 | 2024-10-09 05:04:00 | NOAA-20 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2a349f94-1729-3d6b-ae0d-14538df21292 | -14.79846 | -53.93353 | 2024-10-09 05:04:00 | NOAA-20 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c3815e55-4ec2-39d0-8a23-2dd772705214 | -14.79411 | -53.93746 | 2024-10-09 05:04:00 | NOAA-20 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c61b1eae-291b-36ba-b436-38576c6cf28e | -14.78301 | -53.9357 | 2024-10-09 05:04:00 | NOAA-20 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e686dce5-3e30-3aff-975f-6fb05775f7f0 | -9.31895 | -54.52987 | 2024-10-09 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f706f1cb-25b8-315d-9156-2497074640a2 | -9.3161 | -54.5256 | 2024-10-09 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5b0648ca-a815-36e9-a5f9-4638f335c1f9 | -9.31553 | -54.52935 | 2024-10-09 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3468fe1a-b7c1-30fa-b282-f7c951164668 | -9.31497 | -54.53308 | 2024-10-09 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cd907329-0310-343c-85c3-6a20b1774760 | -9.31212 | -54.52882 | 2024-10-09 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a570f727-b7f1-3ecf-abfd-d787ec358cc3 | -9.31156 | -54.53255 | 2024-10-09 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2eadc9bb-8820-33e8-a929-3688289a59fe | -9.30871 | -54.52829 | 2024-10-09 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 14fa8a29-6f70-31d6-a9ed-d12063418924 | -9.30815 | -54.53202 | 2024-10-09 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| afbf4004-e957-3903-9aa4-5a2f479d7464 | -9.3053 | -54.52775 | 2024-10-09 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9f9b4f9d-2e0e-381f-bac6-c627075b94fe | -9.30474 | -54.53147 | 2024-10-09 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 54769e01-036f-3681-957e-9b5c7b00ce02 | -8.88169 | -54.57453 | 2024-10-09 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 59146a36-d48d-3d1b-914c-a15b6fa18036 | -8.70429 | -54.83475 | 2024-10-09 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 68e8d90a-4da4-3ce1-b54f-f8acb19ae101 | -8.70094 | -54.83414 | 2024-10-09 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bb61a89c-0671-35f4-9f0c-c26e03693b35 | -8.69815 | -54.82994 | 2024-10-09 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5504363f-9c9f-35de-be80-9daae71979b6 | -9.65295 | -54.31412 | 2024-10-09 05:04:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 727034e8-f362-3376-b257-189be9ece268 | -9.65207 | -54.31326 | 2024-10-09 05:04:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b64ac614-0991-35fa-8b15-506f3cdc6afc | -10.68494 | -54.47694 | 2024-10-09 05:04:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2b2079ea-13ee-361e-bb23-39a3874edfaf | -10.61892 | -54.61112 | 2024-10-09 05:04:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| db1faa0c-55c1-3536-a15d-fddcc4ebd639 | -10.61842 | -54.2452 | 2024-10-09 05:04:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c61b3689-1895-34f5-9a2b-6495c7eb6516 | -10.61551 | -54.24082 | 2024-10-09 05:04:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1aaa364e-04dc-349f-9dd9-99d06f0fc66e | -10.61548 | -54.6106 | 2024-10-09 05:04:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 110060a3-bfec-353f-87c1-78a728b65339 | -10.61493 | -54.2447 | 2024-10-09 05:04:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eb3fd8ae-74b5-33bc-8cc8-d03792b23a42 | -10.57188 | -54.24632 | 2024-10-09 05:04:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e17a4ab7-1646-322a-8fcf-0805ebebe5c5 | -10.4876 | -54.53371 | 2024-10-09 05:04:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 32ac2032-0fe8-3cc6-a9fe-94d4e938c317 | -10.48683 | -54.5329 | 2024-10-09 05:04:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ae3a6066-8136-30cb-b592-3b74dfb483a8 | -10.42137 | -54.3869 | 2024-10-09 05:04:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c0770d04-3706-324b-8264-f0a2509c5697 | -10.2399 | -54.96644 | 2024-10-09 05:04:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3a80e5ed-893b-3ef5-9434-30985c19b5af | -10.22576 | -54.26785 | 2024-10-09 05:04:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 48e12bac-5e57-38cf-99d8-345a6c226b0d | -10.22229 | -54.26735 | 2024-10-09 05:04:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c68a2a75-9098-315f-8f00-9b8f4ed58193 | -10.21596 | -54.15554 | 2024-10-09 05:04:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 974b0e34-3dd2-3c3c-a6a6-3c8ce5969ca0 | -10.21247 | -54.15501 | 2024-10-09 05:04:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6422bf88-5f62-36e8-a9a0-7ca0a366b886 | -9.99558 | -54.8437 | 2024-10-09 05:04:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d42b7f60-c78f-392f-b23e-0085cd13911e | -9.5036 | -54.6982 | 2024-10-09 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 352a191c-ba67-3380-976a-6307d4caef4b | -11.89264 | -55.51837 | 2024-10-09 05:04:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a28f4636-9e3d-3d5e-bc6d-c7b3c4705607 | -11.6141 | -55.02153 | 2024-10-09 05:04:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a3f4d9f6-a910-30c0-a853-a590de976a70 | -11.59968 | -54.69659 | 2024-10-09 05:04:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ad5e9146-15af-3f71-ab36-38d43bc1b335 | -11.42004 | -55.21718 | 2024-10-09 05:04:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a69b67b9-58ef-3ef9-b279-b57c07f44bfc | -11.40472 | -55.18069 | 2024-10-09 05:04:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 15c3030b-f8be-31a9-a6b8-76274290872b | -11.40416 | -55.18437 | 2024-10-09 05:04:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a5f69392-1990-3d6d-9621-d8b299572f42 | -11.34669 | -55.23609 | 2024-10-09 05:04:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3e4ff5c2-04fe-3604-8b60-8533ec4ef67d | -11.3433 | -55.23557 | 2024-10-09 05:04:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dadb7739-6cd5-38fe-beac-58c064f7e011 | -11.32635 | -55.21028 | 2024-10-09 05:04:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8a9bfc0d-7b0c-31d7-8cf7-fde42f4036a6 | -11.32352 | -55.20605 | 2024-10-09 05:04:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 203b69dd-9ff4-33e5-bbc2-318c818393e6 | -11.19118 | -54.87804 | 2024-10-09 05:04:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3fd3a43a-61b0-313c-969a-036a7d7ccbe2 | -11.19061 | -54.8818 | 2024-10-09 05:04:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bd414758-fedc-3a3d-911e-f8e6e798ab03 | -11.18718 | -54.88128 | 2024-10-09 05:04:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 08ec3513-bef7-34bb-9734-b4ad9a2f02ca | -11.18439 | -54.76087 | 2024-10-09 05:04:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5339d5b8-5467-3700-8347-327a61dbc0e6 | -11.18381 | -54.76469 | 2024-10-09 05:04:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| da18f3e8-901b-315c-8ec8-c7c4bbdc4d34 | -11.17637 | -54.76742 | 2024-10-09 05:04:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f8a02c56-8c86-317d-a11c-7e10aff72dd3 | -11.17464 | -54.77884 | 2024-10-09 05:04:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0927f985-328d-35a7-ac05-5a6b6a232642 | -11.17407 | -54.78261 | 2024-10-09 05:04:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 371f04c5-bcc8-3103-ace2-c21ef633df87 | -11.17121 | -54.77831 | 2024-10-09 05:04:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7c253e4b-e8f3-3a47-86a8-366fe89c26fd | -11.17064 | -54.78208 | 2024-10-09 05:04:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d2fa40a8-1b61-3ebc-9898-7e6cc7220dc9 | -11.16778 | -54.77777 | 2024-10-09 05:04:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2f3fd91b-311b-32cc-b383-e726c9de248b | -11.16492 | -54.77343 | 2024-10-09 05:04:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fc678c19-9932-3159-8d9a-54b5de6cc58d | -11.16434 | -54.77724 | 2024-10-09 05:04:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ac23e968-fd02-36be-9c69-23ef781ec7a6 | -11.00115 | -54.25127 | 2024-10-09 05:04:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README174.md)

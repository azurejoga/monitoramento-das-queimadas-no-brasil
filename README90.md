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

## Dados Diários - Página 90

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eb401c23-9f4c-3647-8601-b87e796392eb | -12.56365 | -53.08026 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5de3d44a-656c-3c79-b138-f8bfe755789c | -12.56306 | -53.08423 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 02145e49-7b30-3bab-ac0a-6c2cc54cc971 | -12.56075 | -53.07575 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5dd7211b-e9cf-3577-ad33-ea1acb024486 | -12.51012 | -53.24868 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1117e500-6123-35a2-9bae-e4ae07982563 | -12.41892 | -53.13099 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fe19c171-351a-3e81-bbda-e3056c71f289 | -12.32241 | -53.44874 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3ca09762-dc50-3ee5-a411-10ef3933d4cb | -12.27475 | -54.00053 | 2024-10-12 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 01f95fdc-041e-3de4-b961-6ecaa86e3c89 | -12.27419 | -54.00421 | 2024-10-12 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5cee0303-9d3c-3427-b1cc-d6ca0a242f76 | -14.83584 | -54.61233 | 2024-10-12 05:01:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 37309049-5b0e-307a-8a80-1df79e94c999 | -14.83246 | -54.61181 | 2024-10-12 05:01:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 295352b7-3ab4-3b9e-be6a-8da5b43136e2 | -14.8207 | -54.62116 | 2024-10-12 05:01:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fa300676-6a33-34c0-b428-88f286dad952 | -14.81024 | -53.94223 | 2024-10-12 05:01:00 | NOAA-21 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ba20c269-f6a3-3b1d-9e49-86cbf4f3abdf | -14.81002 | -54.62331 | 2024-10-12 05:01:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5b992e39-fe87-3519-85d1-7a80fa6b230c | -14.80832 | -54.61167 | 2024-10-12 05:01:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d56ced2a-3664-38ee-9155-6d145ca0bf95 | -14.80664 | -54.62281 | 2024-10-12 05:01:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a2a932bb-0668-38f9-911e-d99a3ab46b1b | -14.80383 | -54.61859 | 2024-10-12 05:01:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 36674c27-26a5-3a27-8d25-aa7fd5a9bbbd | -14.80327 | -54.6223 | 2024-10-12 05:01:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f7c7b8b1-f4f4-3f8c-ae46-2e10bcd56c82 | -14.79983 | -54.57631 | 2024-10-12 05:01:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f727f0e4-bbbd-316d-9734-28784780094c | -14.79928 | -54.57998 | 2024-10-12 05:01:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 92782ca2-d8e8-3ab9-8740-1e24f1418cde | -14.79873 | -54.58366 | 2024-10-12 05:01:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| a1c71995-6a0b-3155-9e72-ab5d8d2a40b0 | -14.79591 | -54.57939 | 2024-10-12 05:01:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 85cd99ea-4114-3c24-92ce-5069c22f80ab | -14.79536 | -54.58307 | 2024-10-12 05:01:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| d826dbc8-63d5-3e67-9110-212fe1a13974 | -14.79481 | -54.58674 | 2024-10-12 05:01:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 947d6328-eff0-3b77-a1e7-a10dae887e37 | -17.67729 | -56.32138 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 69ee4af8-e91b-3ac7-8624-2248eaf2ca28 | -17.67683 | -56.25823 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 95fa7714-e5eb-34b1-9e11-83121b06ba0c | -17.67673 | -56.32499 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.8 |
| 852aed50-b804-3111-af0e-a0eec088f973 | -16.41214 | -55.9273 | 2024-10-12 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 702c5e3d-63bf-369f-9a5b-ab2e2a30a765 | -16.40938 | -55.92315 | 2024-10-12 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 7ea53e31-2d6f-35ad-b07d-9ab443955acb | -17.73097 | -56.25986 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 44d3f4a8-d0fb-3797-afea-e5235c2ec066 | -17.72322 | -56.26601 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| f77c8ab3-0bca-36fe-b979-5cb8901436a6 | -17.71112 | -56.23423 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 85052972-6baa-3dcc-87de-d9f4330fb11a | -17.70993 | -56.28608 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 81227068-f50f-3269-91c2-e7bc634edd5f | -17.70781 | -56.23367 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 6a963226-b077-3cd9-9086-e9999bd6dcf7 | -17.70725 | -56.2373 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| eed5f489-82a2-3d28-8080-eceec1bdf22a | -17.70661 | -56.28553 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 31937e01-352a-353b-80f1-6e468e0a6275 | -17.70605 | -56.28915 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| dd96b92b-cb56-3375-a917-cc3f76de1c41 | -17.70505 | -56.22949 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| cac4790c-08ee-33e9-9e0b-0cc388c5a59f | -17.7039 | -56.25905 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 9a893a69-cedd-3864-96cd-f316af17a7bd | -17.7033 | -56.28497 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 1b78f32e-3027-32c0-93a6-bf8e1ff30fcd | -17.70274 | -56.2886 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| a802b926-eb5f-3470-9b83-3454a6760470 | -17.7027 | -56.31088 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 55e5b72f-ef73-369f-83a5-c49f4d6544f6 | -17.70226 | -56.24762 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| c687d8a7-88f4-3dad-94bc-acb798c1388b | -17.69727 | -56.25794 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 59272d00-39f8-3c48-be3b-d603dd1416b1 | -17.69671 | -56.26156 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 81fcede4-1c79-3d24-a80d-e063b25279f1 | -17.69395 | -56.25738 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 118342b1-fa0b-383f-943a-0015beffaed2 | -17.69176 | -56.24958 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 479a4adc-fca7-3444-88ea-c20e61f1b28e | -17.6912 | -56.2532 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| a7d529cf-bb5f-3c3e-90ca-05dec5dc4812 | -17.69064 | -56.25682 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| ce8dbb83-a790-3093-a2f6-679ab6cd43fa | -17.68733 | -56.25627 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 93c1ad96-50e3-374a-b051-d17e120ce6d9 | -17.68621 | -56.26352 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| e6f54b48-fb9b-3859-9b9c-e54462f26fc5 | -17.67958 | -56.26241 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 9c203625-112c-3d1f-8016-0544a9214240 | -17.67738 | -56.25461 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 0249609b-e79b-35f2-972b-b8f68f8c7aec | -17.67574 | -56.24318 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| d57a97a9-ad6b-3846-bcdb-6e8fe0b44cec | -17.67463 | -56.25043 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 5a1a8f7a-6675-3cda-9a38-ab29d5f569ed | -17.67295 | -56.2613 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| ce499ea3-1854-3f7d-a863-535c852bf294 | -17.668 | -56.24931 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 8cfa408b-4817-3ffc-87d3-25c40532c37b | -17.66688 | -56.25656 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 95394d2c-3f33-3b45-a4a7-f410a10908eb | -17.66633 | -56.26019 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| d3312115-19ee-398e-ab33-af95a49975a8 | -17.66304 | -56.23732 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 57b5aa9c-9b3c-330c-8423-f72c6805f5e4 | -17.66301 | -56.25963 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 1ef434aa-1929-34db-bf44-09131ed59083 | -17.6619 | -56.26688 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 2efa7ca7-d9fd-3979-9478-1c218ba4bc24 | -17.6597 | -56.25908 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 65adef41-bd35-3f76-aeae-886b099b18a7 | -17.65635 | -56.28082 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| a33998c0-c771-3394-8e0a-27f9fa463558 | -17.65471 | -56.26939 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 0000d69a-4e28-33fc-8ff8-29747d86672b | -17.6492 | -56.26103 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| b733dbf8-c10d-3fbc-9cec-9037b0ed9090 | -17.70557 | -56.24818 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 1b1ee373-1daf-3423-9080-f0f5223beba8 | -17.7017 | -56.25125 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| b1320032-4b21-3102-a05b-1d6a102a3b8a | -17.70114 | -56.25487 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| e5bd563b-fa8a-3ec0-8a50-e268f8261d09 | -17.70058 | -56.25849 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| c8b9d3e6-34bf-3b1f-a9da-95ab92b3daa7 | -17.69999 | -56.28442 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| f1c8d7d3-3280-3a19-91a7-196cbb8daade | -17.68401 | -56.25571 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 1a6a9e24-81d3-3cbb-b71b-3a3644681a32 | -17.6785 | -56.24736 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 97b0f3f3-ead8-36db-9bcd-e574617f1be3 | -17.67794 | -56.25098 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 09830339-302d-39e8-97cd-8257ae1730f6 | -17.67627 | -56.26185 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 468edd13-ab0b-3674-b533-92868727b442 | -17.67407 | -56.25405 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| c74f0b13-0992-361d-82f9-4f9b3e740a49 | -17.67351 | -56.25768 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 75d8299f-b0fc-3cac-90fd-c15eaad20647 | -17.67243 | -56.24262 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| b974e59f-29c9-3278-b4cc-9bbc85f961d4 | -17.66911 | -56.24206 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| eadedcab-dab3-302f-b4dd-dc9260f70cc9 | -17.66524 | -56.24513 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| baa3f3a3-256c-3e9f-87dd-debedea940b5 | -17.66413 | -56.25238 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 6ea114a8-9d89-3cd4-b316-2da2307c440a | -17.66248 | -56.24095 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 48a6cc89-c7ba-3468-ab16-939075119789 | -17.66192 | -56.24458 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| a21614cc-3a93-33fa-9a31-0b2619134b56 | -17.66026 | -56.25545 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 1c7f3cb0-ca80-3083-a4ed-9a276f557057 | -17.65914 | -56.2627 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 21e57a23-d670-3f30-b78c-6985c261cc44 | -17.65911 | -56.28499 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| a39b2069-3fa5-3121-965c-43bdc07dc251 | -17.65861 | -56.24402 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 4b5bed64-d620-3540-a2be-2983a554e456 | -17.65858 | -56.26632 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 6257b481-0e9e-30e8-ad9e-487356f9e509 | -17.65527 | -56.26576 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 3f5f914d-2342-391b-8870-4511400d6863 | -17.65196 | -56.26521 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| d92b8696-a752-3dee-a19e-e3e0bae8f368 | -17.6514 | -56.26883 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 060f46d8-75b0-327e-8a57-c5c110600cfe | -17.64911 | -56.32778 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 2a7dd090-1244-3a8b-837f-435979aecfcb | -17.64691 | -56.31999 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| d18a731d-6124-36c8-9f17-d78ecc1a8b6d | -17.64636 | -56.3236 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| b0b8bd3d-1f9a-3467-951a-88d7952035ab | -17.6458 | -56.32722 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.1 |
| 47512cef-cff5-3231-af90-561b08786b62 | -17.64533 | -56.2641 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| a3963f1c-5eda-3057-adc5-f584da510c5a | -17.64472 | -56.3122 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| d8b0860b-91a6-3c6e-aec3-46857232a23b | -17.64305 | -56.32305 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 9eb095ed-f21e-35b1-beac-62fe9190cf20 | -17.63973 | -56.32249 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 3f124c76-5a6b-328a-9cf6-668b5d16356c | -17.63642 | -56.32193 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 20e98a54-2f3a-3cef-af1d-dc344cc7c839 | -17.6353 | -56.32918 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.8 |


[Clique aqui para ver as próximas entradas](README91.md)

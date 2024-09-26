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

## Dados Diários - Página 120

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c44f8cd2-1673-3627-8fcf-807f2aa94789 | -12.77268 | -51.33539 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0f1bc554-bb1d-3976-b40a-ff0b4c7fd224 | -12.7702 | -51.33322 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| db47f457-1251-3072-8fed-9cf83ea4ca1c | -12.76914 | -51.31338 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5c0d1245-075b-360c-8638-59fdb9f4c78d | -12.76844 | -51.31821 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4735f87e-7734-3107-a266-5758964a1329 | -12.76832 | -51.31011 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ae5e6115-cb43-367c-b29e-4a94844a6184 | -12.76766 | -51.31495 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 43e7c683-5a81-3a63-bc0c-65a0aacc65c9 | -12.76706 | -51.32784 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5391a860-e947-3c7c-962b-b40051e396c1 | -12.76637 | -51.33266 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 33c72392-b144-333b-966f-1979a2008f1b | -12.76635 | -51.3246 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 93134d83-4d1b-3273-8178-809b3da86931 | -12.76569 | -51.32943 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c4a28e6c-c83f-3a8d-8c31-5fb3a145b88e | -12.76393 | -51.32246 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 94cfccb4-d262-3caa-a4ab-76caae163e73 | -12.76324 | -51.32727 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fcc2e7ba-4c27-375f-8e25-b701de075e35 | -12.76318 | -51.31921 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a0e6c0a4-c3f9-3a89-9474-2c54b84177f3 | -12.76255 | -51.33209 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 93af24bc-1d8c-3c6d-b47a-b1832c2c02b8 | -12.76252 | -51.32403 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f8646e58-d3ad-3438-a754-34b671739038 | -12.76186 | -51.32886 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 726d1ef4-787e-3ffe-8530-1989c4af6516 | -12.75942 | -51.3267 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f14424dd-c5de-3c11-a4f8-f792173cf946 | -12.75559 | -51.32614 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 405a8b5e-3462-30e1-b8e7-3c11ed830fb3 | -12.69609 | -51.91628 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5d72b712-d006-3d56-9172-d870b89e8c8e | -12.85851 | -51.16893 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 17577ec1-5774-381a-bae1-a76fc8ce2244 | -12.85782 | -51.17385 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 277.5 |
| 602e2f8b-ccb3-3ffe-b7f5-0620953b66a1 | -12.85534 | -51.16342 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c9b73030-608c-3a97-bedb-06f18033af14 | -12.85465 | -51.16835 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ca510328-448a-3ace-843f-47e0bbc219ce | -12.85396 | -51.17328 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 277.5 |
| df166baf-94ad-37b3-9166-ce5e5e9af4c9 | -12.85147 | -51.16284 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 14.7 |
| c34e7976-b355-382d-b315-f30185e607bf | -12.85078 | -51.16778 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 14.7 |
| ad2c44e1-6fea-32fa-93b6-0bb25b756da3 | -12.85009 | -51.17271 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 158.7 |
| 8d0fd4fb-6b01-31d8-824e-303f0209414b | -12.84941 | -51.17764 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 158.7 |
| 02d88f55-df70-3ef3-b58a-75f5e6fbe041 | -12.8476 | -51.16227 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 14.7 |
| b56372fa-77ee-34b2-9945-91b754ffb50f | -12.84692 | -51.16721 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 85a5bb8e-d4ee-367a-80b4-97f7d89cdc1e | -12.84623 | -51.17214 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 158.7 |
| 40754370-0fbd-3d27-a1e8-0a52f8004696 | -12.84554 | -51.17707 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 158.7 |
| 818ac187-98f3-38cd-b5c0-1bc95f4f98ac | -12.84374 | -51.1617 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 112.8 |
| 7ee262ec-6616-3a1c-8a1a-50c726a8214f | -12.84305 | -51.16664 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 112.8 |
| 6e24b2b9-7847-37a5-b59e-140dbad7e020 | -12.84237 | -51.17157 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 54fd5903-a41a-3a4c-bfb8-52f08e83ae82 | -12.84168 | -51.1765 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 222085e2-98f3-3292-953c-6e8e2320d58b | -12.84056 | -51.1562 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f0b87a17-48ae-3b9e-96df-28db1bf295d7 | -12.83987 | -51.16114 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 112.8 |
| 2f7aa9f7-30ea-3e5a-949b-22408d81d046 | -12.83918 | -51.16607 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 112.8 |
| b46a7cf0-ac79-32f7-a73c-01e234a37fdf | -12.8385 | -51.17099 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| abc57b4b-2969-3542-ac3d-d19773d4148a | -12.83782 | -51.17592 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7ab24cd2-d2bc-3f3e-a355-8240c691146b | -12.83669 | -51.15562 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3049e675-af04-3120-bc4f-a1e8a738c9df | -12.83532 | -51.16549 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 152.8 |
| 92bc145a-a6af-3f23-82d9-05718020329e | -12.83464 | -51.17042 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c000319f-edef-35a1-981c-b0910b253f76 | -12.83395 | -51.17535 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d8b8b99a-7eae-3552-8dda-e5eafe77c1a4 | -12.83145 | -51.16492 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 152.8 |
| 2c664a53-a7f1-3b44-9f26-724eab019496 | -12.83009 | -51.17478 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 95ce7147-8ebb-330a-9f2f-aee9e1494866 | -12.82759 | -51.16434 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 2b98d277-5ceb-3d38-bb77-ff64d0ea6fc2 | -12.82372 | -51.16377 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 39588a4e-d4ad-3a71-a69a-abeca6b63e73 | -12.82236 | -51.17363 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 42880cc8-3da6-3301-ad19-d942b9d6c168 | -12.81986 | -51.1632 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 28.7 |
| 61e0991e-5150-3d77-946e-09c7349da54b | -12.81918 | -51.16813 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9c876347-2a34-3ffd-b7e1-3fb199c8da0b | -12.81667 | -51.15769 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 28.7 |
| 990ae9f5-b600-3c56-9bab-54e963c21483 | -12.81599 | -51.16262 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 28.7 |
| 38887237-3e3f-3563-a083-edff6926ca40 | -12.8128 | -51.15711 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 89298df1-7b5e-3439-bb46-fda5308635cc | -12.81213 | -51.16205 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 654545f7-f6ab-3617-b181-c1fbdae6de2e | -12.80826 | -51.16148 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7329c3ce-203b-3ea6-933f-4783ab3b2773 | -12.80439 | -51.16091 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c09e6d5b-26e9-3ef6-9c90-5f727a82a24b | -12.80053 | -51.16033 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3e20d9dd-2035-3ca0-aba2-f4ee6e2b848c | -12.79986 | -51.16527 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 67858986-e2af-32df-9e08-cd13bbc413ea | -12.79918 | -51.1702 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 7b8f8e19-086d-3abe-bdaf-313958e502d7 | -12.79847 | -51.1634 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ec9ad7f4-aa29-39b9-ac9d-73ca4f0a62b7 | -12.79776 | -51.16832 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5e6758c7-4df4-315c-b2db-c7716582ccb6 | -12.79532 | -51.16962 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c0bc7d3f-cbf8-3bc0-9ad0-8fab5aab90b4 | -12.79465 | -51.17455 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2873450d-16ad-376c-ae0e-fccb06bbc48a | -12.7939 | -51.16776 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ab796ef9-0b49-3dd3-a233-261cca0abd11 | -12.7932 | -51.17267 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5be39f41-bdd1-30fb-bd7c-1e8ffa11a97f | -12.79249 | -51.17759 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 82acc226-7280-3025-abe3-78bf07b30d7f | -12.79079 | -51.17398 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b0a92f97-a9f0-3a1e-9390-2186d0e0c2ad | -12.78863 | -51.17702 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1357a0d6-cbea-3487-b8d7-9fd6f971b282 | -12.85892 | -51.19412 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 267.1 |
| 076ebddc-16d7-3d24-869d-af21fbe6635a | -12.85823 | -51.19904 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 267.1 |
| 1d4853cf-a635-3b7c-832d-0d95c0c3a031 | -12.85713 | -51.17878 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 277.5 |
| 55cfdff5-09e4-3ff8-9bbb-9583ee3d25a8 | -12.85575 | -51.18863 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 425.0 |
| e546e029-b657-3d7b-9911-47562193686f | -12.85506 | -51.19355 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 53.2 |
| 47970e47-e6b9-3dc0-9708-dba537277c81 | -12.85437 | -51.19847 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 53.2 |
| e91727c3-b574-3a35-a8a3-c4dcca9c5995 | -12.85369 | -51.20338 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.0 |
| f6aad1d2-9617-366a-8253-d0a159cf6fe9 | -12.85258 | -51.18314 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 425.0 |
| 4b267e58-faf4-3d56-88fa-0c228654d5e2 | -12.85189 | -51.18806 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 425.0 |
| 7ded793b-83b1-381d-baa9-73500b3249fa | -12.8512 | -51.19298 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 53.2 |
| 89fd2c18-4f95-313d-947a-0b6665b48e7c | -12.85052 | -51.1979 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 53.2 |
| ff8acf3e-c2d3-3754-bde8-cd5a1f681bdf | -12.84983 | -51.20281 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 053c1ec0-276d-3ffd-a399-515f549b3a61 | -12.84872 | -51.18256 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 17.8 |
| f6dc9075-70f0-35ad-8233-638fa302cadf | -12.84803 | -51.18749 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 17.8 |
| b0703e41-9b6e-3983-83d0-5be51faa5e37 | -12.84734 | -51.19241 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 1ea78f4c-72c7-3bda-b2de-7416d5deaec3 | -12.84666 | -51.19733 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.7 |
| dee93fc3-2df0-3914-94f9-a68e9d2bc1f2 | -12.84597 | -51.20224 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a21b28b4-d03e-36ac-9f05-2a9857e354f7 | -12.84486 | -51.18199 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 17.8 |
| c39689eb-2259-3897-8511-101625ab797e | -12.84417 | -51.18692 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 17.8 |
| f047cdbf-41ba-3539-be5c-fee087ee3cfc | -12.84348 | -51.19184 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 604baba7-da64-37b4-a031-54a8b7ef5ec8 | -12.8428 | -51.19675 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 0c85b879-8890-3553-9dfd-4b9eedc0b18f | -12.84211 | -51.20167 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 585f029a-3ac8-3da1-87d1-437ef875a874 | -12.84099 | -51.18142 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 84b58fab-2d73-3a62-8a68-6f6346f39531 | -12.84031 | -51.18635 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4cfde8d3-bd32-3ef5-893b-94d43ac96faa | -12.83962 | -51.19127 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bed41bdc-0599-3cee-96e4-fff78f161a38 | -12.83894 | -51.19619 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 82407317-f4c4-3cf8-8ddf-4583b889cbe9 | -12.83508 | -51.19561 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 52ed72df-21ec-3a11-aa7c-a4c9640cf2f9 | -12.82168 | -51.17857 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e537c1b4-e3f3-3c89-b4ac-f4e068c0e224 | -12.80103 | -51.18555 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e160794f-b67c-357b-9c02-05cf93e1f85b | -12.79109 | -51.18742 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.3 |


[Clique aqui para ver as próximas entradas](README121.md)

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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 85033283-2e2e-3ccd-b125-ab7c4cd88cb3 | -4.73483 | -46.67471 | 2024-11-29 04:04:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 68fd6193-b3c0-379f-9031-6fab27c5bcd3 | -4.78408 | -46.1193 | 2024-11-29 04:04:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 88520f0d-bb6f-323a-9805-709abea4803b | 0.94418 | -50.7318 | 2024-11-29 04:04:00 | NOAA-20 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f5d2fc44-80b4-3435-8f27-d363104669d9 | -3.32785 | -50.22314 | 2024-11-29 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 916f09c2-9406-3ee6-bfc0-a155b5f2fc45 | -3.97591 | -46.98914 | 2024-11-29 04:04:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 513d7f9e-69f9-39e2-964f-72f421567486 | -4.36494 | -47.25421 | 2024-11-29 04:04:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 45bd0453-8878-32f5-a062-b0d2badfa806 | -4.01489 | -46.9953 | 2024-11-29 04:04:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7cef45a6-06ba-3b86-907f-50534b558e21 | -4.43733 | -46.58533 | 2024-11-29 04:04:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 3c0f670b-c1d3-3e3a-873a-06cd9ed5d72f | -1.68004 | -45.79543 | 2024-11-29 04:04:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 85444545-f016-327b-98e8-c989068ccb54 | -5.12244 | -41.55653 | 2024-11-29 04:04:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 3756b14d-85f9-39c3-b325-9469bcd0106c | -2.56924 | -49.09568 | 2024-11-29 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 41a8aa94-7ae5-32a2-ae77-a9a7ecdfd043 | -4.52145 | -45.73897 | 2024-11-29 04:04:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cfcadf33-8f0b-3e3f-a490-f58c708ab04c | -1.66438 | -52.73695 | 2024-11-29 04:04:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 44df900f-941e-3c5a-b0ed-091d196fc024 | 0.74166 | -50.87375 | 2024-11-29 04:04:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a2d8928f-242b-34bc-b9e2-183a804d1657 | -1.5986 | -52.28925 | 2024-11-29 04:04:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 653c8a2d-98d3-36eb-bcdd-b071c030707d | -3.77458 | -46.69271 | 2024-11-29 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9ee71992-cad8-3def-9c43-4d20ee32b73e | -2.84842 | -46.8195 | 2024-11-29 04:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2ca6ce9a-535b-3d8f-9397-87c8ef5d27e0 | -2.97061 | -53.28529 | 2024-11-29 04:04:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| bcf8a56d-3482-3e97-b854-ab2ec906c73e | -3.20025 | -46.57164 | 2024-11-29 04:04:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 8.2 |
| bad9c27e-778b-3996-92a7-fc03ce7512ae | -4.18453 | -50.68011 | 2024-11-29 04:04:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8f87448f-a0f8-32ec-852d-01ce57d76160 | -5.76248 | -43.3979 | 2024-11-29 04:04:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2d3603c6-4a1e-3ab2-96d4-6e4c3d260d4b | -4.21351 | -43.28713 | 2024-11-29 04:04:00 | NOAA-20 | AFONSO CUNHA | MARANHÃO | Brasil | 2100105 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 740403fe-65da-3c0e-8a3f-60eda3c92885 | -3.68785 | -50.23403 | 2024-11-29 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 16d7e30b-6ebd-314d-b47a-07f848c66509 | -3.80825 | -44.0515 | 2024-11-29 04:04:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 984ca1ea-1978-3f26-9849-a0ad24e3fa7a | -3.11157 | -54.47805 | 2024-11-29 04:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8f83d01a-d67c-3c45-9c07-53b1468f7d60 | -3.11455 | -54.48302 | 2024-11-29 04:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4484b03f-6317-37c2-8476-31664a4e0ca3 | -2.10125 | -50.34696 | 2024-11-29 04:04:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6acad4ef-cfda-3627-8938-b7db514d9f2d | 1.3317 | -50.67494 | 2024-11-29 04:04:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fb2a8ac8-6b85-34ae-b316-17ad8b658453 | -4.25852 | -40.70074 | 2024-11-29 04:04:00 | NOAA-20 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9914f3f1-67c6-32f3-a84e-b46941d8aba4 | -1.14339 | -48.33726 | 2024-11-29 04:04:00 | NOAA-20 | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b6185f16-ae3d-3773-bdb8-2c34b9e1d5ee | -1.71888 | -52.48692 | 2024-11-29 04:04:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a1591ee4-2474-3248-a9fe-8eebdb78ecdc | -3.15451 | -49.43233 | 2024-11-29 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0155171b-3b2b-3a69-a1a6-0b574837b279 | -4.4367 | -46.5892 | 2024-11-29 04:04:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| f322f661-3c87-3fd0-8aa9-07d50873fd45 | -4.23244 | -45.76421 | 2024-11-29 04:04:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6723cc48-4a00-3721-a646-c5ca6de0bfc1 | -2.69247 | -51.98695 | 2024-11-29 04:04:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 31c8b555-d30f-3db1-81d5-4b02266bd9f8 | -3.69441 | -50.22817 | 2024-11-29 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 953a8ea8-51e6-3f42-acb1-2846e41b4f8f | -5.7556 | -43.3968 | 2024-11-29 04:04:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c822f43d-ebc2-3243-b04f-dba0a3b04cfb | -5.22558 | -44.92133 | 2024-11-29 04:04:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f94ea2b1-fcb0-3120-b7db-304134ee7fcb | -3.17538 | -50.28635 | 2024-11-29 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 15961893-afac-3b34-bb8b-2e3dec8f8752 | -3.36681 | -50.82995 | 2024-11-29 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1a17d4d0-b551-390d-b548-fe710a704339 | -2.33409 | -46.87785 | 2024-11-29 04:04:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 49.2 |
| d6d7ec64-4825-39f3-bcb3-e2a0f5031090 | -5.75499 | -43.40057 | 2024-11-29 04:04:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a83a43d8-104e-3e5c-a546-e8e9062e9424 | -4.26558 | -42.60732 | 2024-11-29 04:04:00 | NOAA-20 | MIGUEL ALVES | PIAUÍ | Brasil | 2206209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 696e1923-cba0-356c-83db-2d9d1b7bd71c | -2.65401 | -48.80023 | 2024-11-29 04:04:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f32412ec-6faa-3f56-a440-c367b7bdc43b | -4.02926 | -42.28276 | 2024-11-29 04:04:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b96759a4-ed18-3c74-972c-d96bad4fadae | -4.17754 | -48.62838 | 2024-11-29 04:04:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b18b9a20-dd64-3f0e-9181-fbb193acb9dd | -5.04479 | -43.61614 | 2024-11-29 04:04:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2a8fb57a-93cc-3e47-8131-f43478ebb5ef | -3.68953 | -42.0429 | 2024-11-29 04:04:00 | NOAA-20 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4780e192-1160-370a-9c15-3bcefebea5ab | -3.44234 | -40.8364 | 2024-11-29 04:04:00 | NOAA-20 | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2148cb75-9b62-3d40-88a6-713cc6aec937 | -6.16079 | -44.42396 | 2024-11-29 04:04:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b942527e-9e88-33c0-a0f3-d697a3493ab5 | -5.54417 | -41.42494 | 2024-11-29 04:04:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 52aae7d9-d654-3e78-9fac-b920768330a2 | -5.716 | -43.83925 | 2024-11-29 04:04:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 36baa094-387c-3709-8dbb-188feec67a49 | -1.04828 | -51.74369 | 2024-11-29 04:04:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c1cac090-e63e-3d29-aaa8-a02d92aba978 | -4.33846 | -47.57592 | 2024-11-29 04:04:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 2c9e2b21-32d1-3cb2-948a-aa0471ad354f | -1.64993 | -52.50008 | 2024-11-29 04:04:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8efb3169-6361-35cd-81d3-f524019e460d | -5.85258 | -40.80182 | 2024-11-29 04:04:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 60d6fb43-69ea-3d71-a515-f174a21f3453 | -5.65393 | -45.19909 | 2024-11-29 04:04:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6994a0b6-3993-3d4f-8eff-0764865818d9 | -4.31325 | -48.09025 | 2024-11-29 04:04:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 84d1aa1d-9224-3fc5-be86-9041c84cc66f | 0.9449 | -50.7363 | 2024-11-29 04:04:00 | NOAA-20 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 836540c1-609a-39ad-86d8-2b86d77f227a | -3.80961 | -44.04316 | 2024-11-29 04:04:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 95da262e-743d-3269-96c6-5d5ddef9d899 | -4.26048 | -47.61686 | 2024-11-29 04:04:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 24939e62-878a-324a-9a51-be17e080c129 | -5.97589 | -45.36223 | 2024-11-29 04:04:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8ad41275-95a4-38d7-8b71-b27117ed8c49 | -3.35675 | -45.41354 | 2024-11-29 04:04:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 954ea891-0e80-3171-bfe8-d6b488aa88a7 | -4.81559 | -39.93969 | 2024-11-29 04:04:00 | NOAA-20 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 43edb475-c8c7-3d46-90dd-ae395b20fd43 | -3.70733 | -47.13813 | 2024-11-29 04:04:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4cfb4c09-b5b5-3137-97b8-8779898d16f6 | -3.1189 | -53.26521 | 2024-11-29 04:04:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b104279e-7bac-3e09-8e21-93dee99f2c93 | -1.36331 | -51.97274 | 2024-11-29 04:04:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 358db6f4-aebd-3b4c-9ea5-323d19417c6b | -3.17085 | -46.29936 | 2024-11-29 04:04:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 497279cf-c42c-3292-af4e-5fa0bb15df30 | -3.62405 | -41.57967 | 2024-11-29 04:04:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 618f1bf0-8aeb-3437-b043-03bdc751714e | -3.24975 | -50.61415 | 2024-11-29 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 03c4591a-bfcb-352d-bac7-f94ebaa7c40e | -3.47279 | -50.54017 | 2024-11-29 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9cafaa2e-d7eb-37fd-a9e9-2e887156a8b8 | -3.40724 | -49.52922 | 2024-11-29 04:04:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| eae085d4-3955-352c-a4fd-8266e894279a | -4.41392 | -43.75799 | 2024-11-29 04:04:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 81ada86b-4041-3e01-a5b3-e34e10ad3976 | -3.28067 | -48.76826 | 2024-11-29 04:04:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 026386ac-652d-3490-96bc-c122704d9b67 | -4.88109 | -44.64636 | 2024-11-29 04:04:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d83cfb1d-501a-3231-a91a-82fa278bdb2e | -1.3283 | -51.92769 | 2024-11-29 04:04:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7f11af7a-515b-35ea-bdf5-719256d6c580 | -3.24888 | -50.59621 | 2024-11-29 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3888928f-040a-38ff-8287-33a2aba63943 | -3.37247 | -50.83099 | 2024-11-29 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f22d67cc-1216-3115-8ae7-0f43a1608209 | -3.80893 | -44.04733 | 2024-11-29 04:04:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 34bc86ef-cadf-3503-9b44-7325cd34ce3a | -2.69221 | -51.99504 | 2024-11-29 04:04:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4cb6b80f-2da9-36f1-ab91-88b3af1fe6a4 | -2.84023 | -46.86994 | 2024-11-29 04:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fea03d73-1aa1-3ef9-82e0-6c7254d998d9 | -4.16789 | -48.62671 | 2024-11-29 04:04:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| bb173f5a-164a-3de1-bc4c-60bed82ffa0e | -2.80364 | -47.5853 | 2024-11-29 04:04:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8612375b-e6bf-3672-af33-850f42aad57c | -2.96408 | -45.23447 | 2024-11-29 04:04:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0911af97-b2c7-3d09-aaa8-777201db86bf | -4.53715 | -43.57819 | 2024-11-29 04:04:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1d9fee63-e715-3dfd-a4ee-f19586a56596 | -3.78736 | -46.69468 | 2024-11-29 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b085704f-905f-3ff4-8cad-b9d7d9a4dade | -1.58455 | -52.2859 | 2024-11-29 04:04:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 5fe98a94-935d-3ccc-b440-7052335887aa | -4.90956 | -44.03016 | 2024-11-29 04:04:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 64b15075-16ab-3d9c-b0ae-0df6f8307cb7 | -3.94306 | -46.69346 | 2024-11-29 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7aea5167-436c-34c6-acfb-7f26dbf94684 | -1.52961 | -52.67054 | 2024-11-29 04:04:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| e9dbbe8b-2e44-3ff8-8fbe-c333f23aae13 | -3.59018 | -50.37723 | 2024-11-29 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 578a2aef-28d8-3f9d-8f23-0660b64277af | -3.41456 | -50.17301 | 2024-11-29 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| af2a1009-5b15-31e5-ae92-e41168b02bcb | -3.70311 | -50.51261 | 2024-11-29 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0227bdcf-04ff-3d0d-bf2a-8647c134ac95 | 0.94701 | -50.73852 | 2024-11-29 04:04:00 | NOAA-20 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c70711d7-6a4a-3ffa-8ac5-a922a426e22e | -3.02194 | -54.02381 | 2024-11-29 04:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 20830cf1-4430-39ba-aca7-f3ca0261fedb | -3.24911 | -50.61791 | 2024-11-29 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f81001d0-0ec8-3b48-b43e-e6a5183a04c7 | -3.37984 | -50.11373 | 2024-11-29 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e13b4a6a-a9b4-3c5c-8caf-62d66e0c33e3 | -3.77885 | -46.69332 | 2024-11-29 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7cf489a8-fa8d-32f3-970b-523df81a4986 | -1.16926 | -53.67661 | 2024-11-29 04:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ae5eef7c-29db-372f-aebc-4e607eafdf7b | -2.86754 | -45.53883 | 2024-11-29 04:04:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |


[Clique aqui para ver as próximas entradas](README31.md)

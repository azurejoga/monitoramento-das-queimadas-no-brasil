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

## Dados Diários - Página 73

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1fc02c6a-4fe4-3978-93ac-dfe12cae70b6 | -20.44842 | -43.10305 | 2024-10-07 04:04:00 | NOAA-20 | DIOGO DE VASCONCELOS | MINAS GERAIS | Brasil | 3121704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 33f50762-bb6a-387b-b55a-f4745b1ec5fb | -20.41339 | -43.36832 | 2024-10-07 04:04:00 | NOAA-20 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 7fd2f657-5b96-3964-9efe-64fb910697bb | -20.34396 | -43.20529 | 2024-10-07 04:04:00 | NOAA-20 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| dbc8808d-1e9e-32cf-b241-e966c7184092 | -21.06978 | -43.61946 | 2024-10-07 04:04:00 | NOAA-20 | SENHORA DOS REMÉDIOS | MINAS GERAIS | Brasil | 3166204 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| c4c52c48-15e9-3677-82bc-df7d106e9cc4 | -21.06646 | -43.61888 | 2024-10-07 04:04:00 | NOAA-20 | SENHORA DOS REMÉDIOS | MINAS GERAIS | Brasil | 3166204 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 178734e3-d1e5-3863-8b45-9783a9f7a8e4 | -22.09332 | -43.09103 | 2024-10-07 04:04:00 | NOAA-20 | TRÊS RIOS | RIO DE JANEIRO | Brasil | 3306008 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| cae85564-fcd7-3b2a-9276-b62596d6fcba | -22.0662 | -43.09008 | 2024-10-07 04:04:00 | NOAA-20 | CHIADOR | MINAS GERAIS | Brasil | 3116209 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 2c9fd9f0-52ba-3e9e-b2e5-314806bfd6de | -22.06345 | -43.08576 | 2024-10-07 04:04:00 | NOAA-20 | CHIADOR | MINAS GERAIS | Brasil | 3116209 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 61df88fe-4cf6-3440-bc6b-c4770a159d5d | -22.03285 | -42.88962 | 2024-10-07 04:04:00 | NOAA-20 | SAPUCAIA | RIO DE JANEIRO | Brasil | 3305406 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 2d40a863-e887-3b61-8439-91fbf24e4b49 | -22.0301 | -42.88534 | 2024-10-07 04:04:00 | NOAA-20 | SAPUCAIA | RIO DE JANEIRO | Brasil | 3305406 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 0e694ab3-7199-320b-9f99-7a7ba915bb8c | -22.02953 | -42.88906 | 2024-10-07 04:04:00 | NOAA-20 | SAPUCAIA | RIO DE JANEIRO | Brasil | 3305406 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 6987a433-11c4-306d-9964-434af3abf37a | -21.80774 | -42.51607 | 2024-10-07 04:04:00 | NOAA-20 | VOLTA GRANDE | MINAS GERAIS | Brasil | 3172103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 097305dc-2b5a-3228-b28e-5c139a03cf4e | -21.80496 | -42.51173 | 2024-10-07 04:04:00 | NOAA-20 | VOLTA GRANDE | MINAS GERAIS | Brasil | 3172103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| a17c2866-8509-365d-93c1-1fd0163d4767 | -21.80162 | -42.51117 | 2024-10-07 04:04:00 | NOAA-20 | VOLTA GRANDE | MINAS GERAIS | Brasil | 3172103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 0895b324-ec7c-3b98-aa61-033d621363d2 | -21.78718 | -42.49327 | 2024-10-07 04:04:00 | NOAA-20 | VOLTA GRANDE | MINAS GERAIS | Brasil | 3172103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 57ea1e5b-7bb7-3408-8310-7868daeec596 | -21.78662 | -42.49705 | 2024-10-07 04:04:00 | NOAA-20 | VOLTA GRANDE | MINAS GERAIS | Brasil | 3172103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 45e16064-37eb-3ccb-9b2a-7f9a2876f29c | -21.78385 | -42.49269 | 2024-10-07 04:04:00 | NOAA-20 | VOLTA GRANDE | MINAS GERAIS | Brasil | 3172103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 8364fd88-8427-347f-a6f2-dd912bb26d60 | -21.73399 | -43.02186 | 2024-10-07 04:04:00 | NOAA-20 | GUARARÁ | MINAS GERAIS | Brasil | 3128501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 00fe463f-45e4-3eff-a300-ea17b554e484 | -21.73342 | -43.02557 | 2024-10-07 04:04:00 | NOAA-20 | GUARARÁ | MINAS GERAIS | Brasil | 3128501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| c3134228-73d5-3a34-b3fa-740fd23afb57 | -21.62716 | -43.46735 | 2024-10-07 04:04:00 | NOAA-20 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 1514778e-0453-390f-b8ae-2b8e4fec5bbd | -21.60808 | -42.55973 | 2024-10-07 04:04:00 | NOAA-20 | LEOPOLDINA | MINAS GERAIS | Brasil | 3138401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| afd9f24b-868d-3632-a291-1e55a01003c6 | -21.55356 | -42.33823 | 2024-10-07 04:04:00 | NOAA-20 | PALMA | MINAS GERAIS | Brasil | 3146701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b5ce1bd9-2ba3-3a21-a63d-49e3a20790c6 | -21.55022 | -42.33767 | 2024-10-07 04:04:00 | NOAA-20 | PALMA | MINAS GERAIS | Brasil | 3146701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 059925ce-3082-3a28-b795-80537f474932 | -21.25362 | -43.09871 | 2024-10-07 04:04:00 | NOAA-20 | PIRAÚBA | MINAS GERAIS | Brasil | 3151305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 8af5d6c4-ae42-30b6-a5d6-34a0955ec6d4 | -21.00943 | -43.4007 | 2024-10-07 04:04:00 | NOAA-20 | ALTO RIO DOCE | MINAS GERAIS | Brasil | 3102100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| a4573700-3b6b-326d-a017-d07a211f6696 | -20.98789 | -42.99573 | 2024-10-07 04:04:00 | NOAA-20 | DIVINÉSIA | MINAS GERAIS | Brasil | 3121902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 54fbbac3-b93f-3c81-a3a0-168eab576f64 | -22.90326 | -43.75365 | 2024-10-07 04:04:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 18440b7d-dbea-3979-8ad2-8271ce3d4009 | -22.89995 | -43.75304 | 2024-10-07 04:04:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 8092e232-9f87-3e78-982b-1970e45e0a53 | -22.85682 | -42.98002 | 2024-10-07 04:04:00 | NOAA-20 | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| c6172eae-5619-3837-810a-9d706e28077b | -22.4761 | -44.04977 | 2024-10-07 04:04:00 | NOAA-20 | BARRA DO PIRAÍ | RIO DE JANEIRO | Brasil | 3300308 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| bbf87397-55af-3f88-ae49-edbf08e42f07 | -20.34465 | -44.68662 | 2024-10-07 04:04:00 | NOAA-20 | CLÁUDIO | MINAS GERAIS | Brasil | 3116605 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3b3717c5-9ff6-37a1-a967-713a5152e0d1 | -20.344 | -44.69046 | 2024-10-07 04:04:00 | NOAA-20 | CLÁUDIO | MINAS GERAIS | Brasil | 3116605 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b4653e10-9a83-360d-9221-64f9d1e2f97f | -20.34127 | -44.68601 | 2024-10-07 04:04:00 | NOAA-20 | CLÁUDIO | MINAS GERAIS | Brasil | 3116605 | 31 | 33 | nan | nan | nan | Cerrado | 11.3 |
| bb3eaebb-771e-3fd4-921f-585a6f0e1e53 | -20.34063 | -44.68985 | 2024-10-07 04:04:00 | NOAA-20 | CLÁUDIO | MINAS GERAIS | Brasil | 3116605 | 31 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 58ad6f7f-1baf-3553-8a77-79df5d62dd56 | -20.23112 | -44.88012 | 2024-10-07 04:04:00 | NOAA-20 | DIVINÓPOLIS | MINAS GERAIS | Brasil | 3122306 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 5e50bb1e-2c41-3329-8f8b-3ef090ba8cca | -20.90763 | -43.7426 | 2024-10-07 04:04:00 | NOAA-20 | CARANAÍBA | MINAS GERAIS | Brasil | 3113107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 59389885-d143-372e-a0ec-203bf9ee8eb4 | -20.90431 | -43.74201 | 2024-10-07 04:04:00 | NOAA-20 | CARANAÍBA | MINAS GERAIS | Brasil | 3113107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| 8c7c647a-ebe6-3b66-a579-badf50317180 | -20.89855 | -43.82064 | 2024-10-07 04:04:00 | NOAA-20 | CARANDAÍ | MINAS GERAIS | Brasil | 3113206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 0aa6f083-7e7f-3115-bd04-5f1cfb00d516 | -20.72004 | -43.83065 | 2024-10-07 04:04:00 | NOAA-20 | CONSELHEIRO LAFAIETE | MINAS GERAIS | Brasil | 3118304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| b90a5dce-b78b-3830-aa84-046500fd9d5b | -20.71944 | -43.83434 | 2024-10-07 04:04:00 | NOAA-20 | CONSELHEIRO LAFAIETE | MINAS GERAIS | Brasil | 3118304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 85b003e9-133b-3b7c-8cf9-937ac1ff5d71 | -20.66984 | -44.03527 | 2024-10-07 04:04:00 | NOAA-20 | ENTRE RIOS DE MINAS | MINAS GERAIS | Brasil | 3123908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 63dfb442-103a-3368-a19a-c25eab70e640 | -20.62437 | -43.98181 | 2024-10-07 04:04:00 | NOAA-20 | SÃO BRÁS DO SUAÇUÍ | MINAS GERAIS | Brasil | 3160900 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ace752a8-89b8-37b6-a97e-ab24448f7d57 | -20.48754 | -43.64928 | 2024-10-07 04:04:00 | NOAA-20 | OURO BRANCO | MINAS GERAIS | Brasil | 3145901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 7ebf1153-fac1-3bac-b921-1536b8cb1dcf | -20.48696 | -43.65295 | 2024-10-07 04:04:00 | NOAA-20 | OURO BRANCO | MINAS GERAIS | Brasil | 3145901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 102ca889-afe1-36d9-84aa-597880547e17 | -20.48423 | -43.64868 | 2024-10-07 04:04:00 | NOAA-20 | OURO BRANCO | MINAS GERAIS | Brasil | 3145901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 87a2ffef-b8d2-3b08-af4c-451b9714c09e | -20.4489 | -43.8055 | 2024-10-07 04:04:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| aec89bb0-49f1-3627-a9bc-e41b7a9a6a7a | -20.42014 | -43.7509 | 2024-10-07 04:04:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| bc4866d8-f13b-3886-965b-7a812a8d8339 | -20.41681 | -43.75032 | 2024-10-07 04:04:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| d39c23e2-0bee-3de7-876a-6830bc4e117e | -20.41623 | -43.75398 | 2024-10-07 04:04:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| c828d34a-f84f-34ad-ab74-5dbb0a789959 | -20.39273 | -43.92078 | 2024-10-07 04:04:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 9b9bef71-b06f-31a7-a402-8c51cc006461 | -20.38422 | -43.8889 | 2024-10-07 04:04:00 | NOAA-20 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 1cbc6db6-9786-3e66-bb38-a0c783ca08be | -20.30294 | -43.6129 | 2024-10-07 04:04:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| fa43c8a3-37b5-34d2-8bae-70b2730f4fc1 | -22.11267 | -44.84346 | 2024-10-07 04:04:00 | NOAA-20 | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f347be74-2491-38f3-8cfa-2fc85cddf49f | -21.95691 | -45.37654 | 2024-10-07 04:04:00 | NOAA-20 | LAMBARI | MINAS GERAIS | Brasil | 3137809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.6 |
| 83796188-5e76-3a70-b794-7bcd4e81c1d7 | -21.95418 | -45.37194 | 2024-10-07 04:04:00 | NOAA-20 | LAMBARI | MINAS GERAIS | Brasil | 3137809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.6 |
| 3b574e55-97f1-3961-9713-c058c8977d6d | -21.95354 | -45.37574 | 2024-10-07 04:04:00 | NOAA-20 | LAMBARI | MINAS GERAIS | Brasil | 3137809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.6 |
| 7f00d474-6bdd-3012-b1d3-97b882f5b3f9 | -21.95208 | -45.36355 | 2024-10-07 04:04:00 | NOAA-20 | LAMBARI | MINAS GERAIS | Brasil | 3137809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 32a9ab7a-4543-37ec-9824-4a1f05f04bd9 | -21.95144 | -45.36737 | 2024-10-07 04:04:00 | NOAA-20 | LAMBARI | MINAS GERAIS | Brasil | 3137809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 428e4feb-46ac-348e-8853-874b7f020942 | -21.94936 | -45.35884 | 2024-10-07 04:04:00 | NOAA-20 | LAMBARI | MINAS GERAIS | Brasil | 3137809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 7f4782a4-b058-3274-907e-6bdbdc62291e | -21.94872 | -45.3627 | 2024-10-07 04:04:00 | NOAA-20 | LAMBARI | MINAS GERAIS | Brasil | 3137809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| ca1ccc8e-2fbf-34ea-bed9-50cc28b6678b | -21.94806 | -45.36658 | 2024-10-07 04:04:00 | NOAA-20 | CAMPANHA | MINAS GERAIS | Brasil | 3110905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 14b15558-578c-3b6b-b039-a179920017d0 | -21.94534 | -45.36189 | 2024-10-07 04:04:00 | NOAA-20 | CAMPANHA | MINAS GERAIS | Brasil | 3110905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| 23a0f709-63cb-3fb5-9393-9e2018353819 | -21.40054 | -45.3433 | 2024-10-07 04:04:00 | NOAA-20 | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| da8ed76c-665c-30a6-9add-9a8d5caf95c0 | -21.19448 | -44.93949 | 2024-10-07 04:04:00 | NOAA-20 | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 44391a6d-34be-3cf5-b731-f3f561871fc3 | -21.68111 | -43.98321 | 2024-10-07 04:04:00 | NOAA-20 | LIMA DUARTE | MINAS GERAIS | Brasil | 3138609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 1a0b03c8-4219-3bf9-9e43-d44b48d38a68 | -21.68051 | -43.98693 | 2024-10-07 04:04:00 | NOAA-20 | LIMA DUARTE | MINAS GERAIS | Brasil | 3138609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 0cea6ec4-0013-3d18-a49b-538be3ad1e97 | -21.6772 | -43.98632 | 2024-10-07 04:04:00 | NOAA-20 | LIMA DUARTE | MINAS GERAIS | Brasil | 3138609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| c47d9b1d-7b70-3d88-be7e-a0e957f67bda | -21.6715 | -44.00058 | 2024-10-07 04:04:00 | NOAA-20 | LIMA DUARTE | MINAS GERAIS | Brasil | 3138609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| be2a0089-e61d-340e-99fd-20fa0568c1e2 | -21.6709 | -44.0043 | 2024-10-07 04:04:00 | NOAA-20 | LIMA DUARTE | MINAS GERAIS | Brasil | 3138609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 7ffef8be-7e38-30b5-8375-423e62d22ec5 | -21.6703 | -44.00802 | 2024-10-07 04:04:00 | NOAA-20 | LIMA DUARTE | MINAS GERAIS | Brasil | 3138609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 1bf90865-5951-3429-87e2-061cfa8fe6ad | -21.66758 | -44.00369 | 2024-10-07 04:04:00 | NOAA-20 | LIMA DUARTE | MINAS GERAIS | Brasil | 3138609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 48c18cda-97b7-31c6-8b89-8b4f524362d3 | -21.66699 | -44.00741 | 2024-10-07 04:04:00 | NOAA-20 | LIMA DUARTE | MINAS GERAIS | Brasil | 3138609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 9232d063-12d7-3db3-9645-cf5d25f67684 | -21.66487 | -43.99936 | 2024-10-07 04:04:00 | NOAA-20 | LIMA DUARTE | MINAS GERAIS | Brasil | 3138609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d01e8933-decb-372a-a5dd-c896a7eaa6a7 | -21.66427 | -44.00308 | 2024-10-07 04:04:00 | NOAA-20 | LIMA DUARTE | MINAS GERAIS | Brasil | 3138609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c5c9773d-513d-3aa2-8687-ac5e99479ad6 | -21.66156 | -43.99874 | 2024-10-07 04:04:00 | NOAA-20 | LIMA DUARTE | MINAS GERAIS | Brasil | 3138609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 9ec7fee1-06af-339d-a75a-bf1c69805c63 | -21.53301 | -43.97586 | 2024-10-07 04:04:00 | NOAA-20 | IBERTIOGA | MINAS GERAIS | Brasil | 3129400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| d9e2bcf1-db7d-3d72-b6d2-0388bd97d09c | -21.53208 | -43.9604 | 2024-10-07 04:04:00 | NOAA-20 | SANTA RITA DE IBITIPOCA | MINAS GERAIS | Brasil | 3159407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 086d4968-4afc-37fd-8ccd-69413c3a2300 | -21.3895 | -44.27175 | 2024-10-07 04:04:00 | NOAA-20 | MADRE DE DEUS DE MINAS | MINAS GERAIS | Brasil | 3139102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| bf7fef67-c996-39ec-8a81-71a9e968d533 | -21.18201 | -44.27262 | 2024-10-07 04:04:00 | NOAA-20 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 966cfe2f-4480-322d-b7ab-99393c64d28c | -21.1786 | -43.98169 | 2024-10-07 04:04:00 | NOAA-20 | BARROSO | MINAS GERAIS | Brasil | 3105905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 318096d5-e65a-38a3-8479-7d5f328e1c35 | -21.06554 | -44.19868 | 2024-10-07 04:04:00 | NOAA-20 | CORONEL XAVIER CHAVES | MINAS GERAIS | Brasil | 3119708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 4e5dc775-6ef9-3fb6-a17d-670f205b869f | -21.05949 | -44.19371 | 2024-10-07 04:04:00 | NOAA-20 | CORONEL XAVIER CHAVES | MINAS GERAIS | Brasil | 3119708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 00b4f882-a3df-33b5-a5ee-c6c406878fd0 | -23.16092 | -45.55287 | 2024-10-07 04:04:00 | NOAA-20 | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 15.9 |
| 9da50332-bd8b-3b72-a594-66335e6be094 | -20.62445 | -45.832 | 2024-10-07 04:04:00 | NOAA-20 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9620df28-0751-338d-90af-194937ada5fc | -20.62376 | -45.83603 | 2024-10-07 04:04:00 | NOAA-20 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f1e9e5fb-1451-306c-ba4f-ad7925f418de | -20.59838 | -46.00336 | 2024-10-07 04:04:00 | NOAA-20 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3630ecc9-f0e7-35be-b55c-68f6bf364725 | -20.59765 | -46.00754 | 2024-10-07 04:04:00 | NOAA-20 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9746f78e-b0cc-3f3a-b005-a0418e7fe190 | -20.48639 | -45.9782 | 2024-10-07 04:04:00 | NOAA-20 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8d971cdc-00c0-3f9e-b259-d128b98d126e | -20.31129 | -45.58496 | 2024-10-07 04:04:00 | NOAA-20 | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7a98872d-7b50-3d7f-8565-2b3a788927fe | -21.8437 | -46.9391 | 2024-10-07 04:04:00 | NOAA-20 | VARGEM GRANDE DO SUL | SÃO PAULO | Brasil | 3556404 | 35 | 33 | nan | nan | nan | Cerrado | 4.2 |
| bca1f643-7552-31f2-b2b5-9260348fff9a | -21.84009 | -46.93835 | 2024-10-07 04:04:00 | NOAA-20 | VARGEM GRANDE DO SUL | SÃO PAULO | Brasil | 3556404 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 76deabb8-0270-3b18-b102-fcf068faeb73 | -21.08156 | -45.73012 | 2024-10-07 04:04:00 | NOAA-20 | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9f1aed55-a02f-3181-88f7-f63bcf792dc5 | -21.79043 | -46.41859 | 2024-10-07 04:04:00 | NOAA-20 | CALDAS | MINAS GERAIS | Brasil | 3110301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 4136018f-0515-342b-b5f6-9cba731f9609 | -21.78968 | -46.42283 | 2024-10-07 04:04:00 | NOAA-20 | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| b26c1023-ed6a-3767-b913-c4561a155842 | -21.78706 | -46.41919 | 2024-10-07 04:04:00 | NOAA-20 | CALDAS | MINAS GERAIS | Brasil | 3110301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| cbaa4cd6-a818-3beb-b889-18bbe79d22ce | -21.7869 | -46.41793 | 2024-10-07 04:04:00 | NOAA-20 | CALDAS | MINAS GERAIS | Brasil | 3110301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| bdd3ed06-dd4d-3a0e-9341-fb232a1b12f3 | -21.78632 | -46.42344 | 2024-10-07 04:04:00 | NOAA-20 | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 53baae65-9333-3c9e-b97b-59e0f396642d | -21.78614 | -46.42218 | 2024-10-07 04:04:00 | NOAA-20 | CALDAS | MINAS GERAIS | Brasil | 3110301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| e60dac0f-1d86-3e21-b7c0-facc235b022c | -21.5838 | -46.85507 | 2024-10-07 04:04:00 | NOAA-20 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 1dfb45ca-563e-3481-9b65-c081226f2064 | -21.58021 | -46.85426 | 2024-10-07 04:04:00 | NOAA-20 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |


[Clique aqui para ver as próximas entradas](README74.md)

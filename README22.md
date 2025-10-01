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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a9ead260-2d6a-3ed5-bdd2-df4deb887a52 | -18.77351 | -39.95118 | 2025-10-01 03:32:00 | NOAA-20 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 81e78445-4440-3f11-b28f-8b34928ede08 | -14.7859 | -45.77642 | 2025-10-01 03:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| aeda8f4d-09af-32ad-a3c8-bd77dd043d3a | -19.93244 | -43.89354 | 2025-10-01 03:32:00 | NOAA-20 | BELO HORIZONTE | MINAS GERAIS | Brasil | 3106200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 346acabe-ae5a-37ad-9276-d766ce56d70f | -20.62275 | -46.20457 | 2025-10-01 03:32:00 | NOAA-20 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1e96c3eb-d682-3787-80e2-14fd3ac52b18 | -16.49434 | -43.73508 | 2025-10-01 03:32:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f8a783e7-845f-34c4-88d1-2a5255219d7a | -15.28206 | -47.84241 | 2025-10-01 03:32:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1fcfc763-2f1b-3675-8ce4-959d10cf1a88 | -22.1118 | -44.69363 | 2025-10-01 03:32:00 | NOAA-20 | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| f9ccc852-1cb5-3fbc-84e1-430b9501e4ec | -15.53791 | -42.66405 | 2025-10-01 03:32:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 80f98762-deec-31ba-b325-fc7982cf6fcf | -15.7799 | -43.69978 | 2025-10-01 03:32:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c5f0749b-bd08-3ca4-970c-a1cc565edc3e | -14.99702 | -46.95261 | 2025-10-01 03:32:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 34ed8641-9792-3155-a50b-2ef4cfaa543b | -14.62581 | -46.98085 | 2025-10-01 03:32:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0202b479-d271-3c87-aa03-2db5af255b2d | -18.43471 | -43.80111 | 2025-10-01 03:32:00 | NOAA-20 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4f14066c-67e5-31aa-991c-513645cbeace | -14.74797 | -45.78123 | 2025-10-01 03:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1d4562a2-047b-34ae-8285-7862d82f2304 | -22.25547 | -43.42548 | 2025-10-01 03:32:00 | NOAA-20 | VASSOURAS | RIO DE JANEIRO | Brasil | 3306206 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| d10e42f1-f302-345e-97cf-71b3deb0f9d0 | -15.17655 | -46.40173 | 2025-10-01 03:32:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4c68a3c8-5153-3004-b04b-9bc17ef6781f | -20.43385 | -43.59785 | 2025-10-01 03:32:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| af6502e3-becc-3d1b-9387-e4bc2c6d4208 | -14.72656 | -46.83581 | 2025-10-01 03:32:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 494068bc-97cc-3ae1-b265-587e1afc71b7 | -20.61189 | -46.21908 | 2025-10-01 03:32:00 | NOAA-20 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| b40307f7-a510-32e4-98be-f1c8c9b3d234 | -16.40323 | -47.06406 | 2025-10-01 03:32:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| fd6d8d9e-e673-35d6-a346-651c4d2b5fc0 | -14.5421 | -48.25203 | 2025-10-01 03:32:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1390c118-3182-3087-88e4-957d7f461ef4 | -20.01204 | -44.12816 | 2025-10-01 03:32:00 | NOAA-20 | IBIRITÉ | MINAS GERAIS | Brasil | 3129806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ec43284e-7491-3ad4-a646-eda6ca9159a2 | -19.85911 | -42.58633 | 2025-10-01 03:32:00 | NOAA-20 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| e0fa3254-43e3-326f-a1cb-38dd74061ae4 | -16.39941 | -47.05107 | 2025-10-01 03:32:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e862a2ba-d6c1-3923-b906-c9c9576d5605 | -14.79994 | -48.32745 | 2025-10-01 03:32:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 21d3b59b-b6b8-30a5-85b4-00422f0bbf9c | -20.62836 | -46.18003 | 2025-10-01 03:32:00 | NOAA-20 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3d2dc1ee-fb9b-319f-bb11-c1a45ce8421b | -16.37679 | -47.0629 | 2025-10-01 03:32:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 3344c986-f7a3-3f72-b128-08de4d391e99 | -21.21899 | -43.92356 | 2025-10-01 03:32:00 | NOAA-20 | BARROSO | MINAS GERAIS | Brasil | 3105905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| d9fe3bf9-2d62-3e10-b033-3071dabc7a88 | -14.51344 | -48.37777 | 2025-10-01 03:32:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b3c6da3e-70ea-3dbe-a194-369a35eb8713 | -15.29947 | -46.40186 | 2025-10-01 03:32:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 473159b4-5b92-3751-a5b3-bef67589c56c | -19.86396 | -43.82158 | 2025-10-01 03:32:00 | NOAA-20 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| ca826d28-fe18-3a9c-8d10-ec9be7ba7ca2 | -17.5332 | -43.44925 | 2025-10-01 03:32:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eac36f57-f3d9-37ff-bf8e-8a93b4f99b1e | -16.59063 | -40.92231 | 2025-10-01 03:32:00 | NOAA-20 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| a292b24f-01ad-3057-8b53-d4e83a7b4523 | -20.1269 | -44.02665 | 2025-10-01 03:32:00 | NOAA-20 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 5cba9394-86fd-39a1-a0b8-d7d8a42a31a1 | -17.38722 | -47.14416 | 2025-10-01 03:32:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bd3bd210-f212-30cc-9a48-a0fa5649d16f | -14.02884 | -47.96339 | 2025-10-01 03:32:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c244580d-a247-3728-b565-7e2c7d3ceec1 | -14.72252 | -48.1598 | 2025-10-01 03:32:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7071dea0-6930-3927-858a-01d32990c25a | -20.12959 | -44.01985 | 2025-10-01 03:32:00 | NOAA-20 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 3f3129c2-4755-395e-9ff1-41c864fe05a1 | -22.11535 | -44.70167 | 2025-10-01 03:32:00 | NOAA-20 | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| feb19b2d-a6a5-3956-94e0-5f66a4d745de | -21.04626 | -45.67966 | 2025-10-01 03:32:00 | NOAA-20 | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b70fed1f-1e1b-34c6-846b-2cf968b3467b | -20.68634 | -43.37644 | 2025-10-01 03:32:00 | NOAA-20 | PIRANGA | MINAS GERAIS | Brasil | 3150802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| fdb77f10-98f0-3c29-93b3-ba731ef157b4 | -14.79102 | -45.78268 | 2025-10-01 03:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d6ea739f-0327-3c18-afcc-1c5fdcab5252 | -14.53951 | -48.25032 | 2025-10-01 03:32:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 40c9f4d1-61c3-3b7f-a239-7adc9c2d229a | -20.96433 | -45.00229 | 2025-10-01 03:32:00 | NOAA-20 | SANTO ANTÔNIO DO AMPARO | MINAS GERAIS | Brasil | 3159902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 60eaafe3-6096-38ef-a7dd-5ab80c1ce0f0 | -14.54818 | -48.24489 | 2025-10-01 03:32:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 17ba6fa1-79a7-3fe0-a288-41958e626708 | -17.40317 | -47.16243 | 2025-10-01 03:32:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dd54d066-1223-3095-ae2f-3198d00b5dea | -14.78488 | -45.78121 | 2025-10-01 03:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2b5a1810-6c17-3a51-a06b-089df806b6d9 | -20.43105 | -43.59852 | 2025-10-01 03:32:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 707d16ed-eb14-3c0b-9373-32279d7689d3 | -14.78695 | -45.80172 | 2025-10-01 03:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 066afe74-daf5-393e-b236-2cf5cdf643f7 | -14.78593 | -45.80651 | 2025-10-01 03:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9d2a1f94-935c-3392-97ce-7f5f7533ff9b | -16.37966 | -47.01958 | 2025-10-01 03:32:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0c387203-e243-3b54-bbd0-1c5ed7ff31fb | -14.5926 | -48.16084 | 2025-10-01 03:32:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 69fbea87-1bb2-325a-9563-fa709282c298 | -20.63005 | -46.22496 | 2025-10-01 03:32:00 | NOAA-20 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 1ad68f8c-57f7-3be4-8f06-543264e07784 | -15.76132 | -43.73613 | 2025-10-01 03:32:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c71e7e58-abdf-3e4b-9bc6-1869bf8d9255 | -14.51512 | -48.3704 | 2025-10-01 03:32:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 05f8d850-0930-35fa-a3f8-68ffcc917a0a | -20.3325 | -43.04418 | 2025-10-01 03:32:00 | NOAA-20 | BARRA LONGA | MINAS GERAIS | Brasil | 3105707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 77f0de03-df39-38a1-9bff-60d56626823f | -19.89422 | -44.49888 | 2025-10-01 03:32:00 | NOAA-20 | FLORESTAL | MINAS GERAIS | Brasil | 3126000 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 5dd83ba9-46b1-373e-ace1-dfb3ac92bcff | -14.89831 | -48.1378 | 2025-10-01 03:32:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 10.1 |
| ba3a50a9-79cf-3ff8-8d7a-a98bce77bbe4 | -18.32331 | -44.77818 | 2025-10-01 03:32:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 42ebe33f-e229-33bc-8c14-e77577fc5909 | -14.61072 | -48.32369 | 2025-10-01 03:32:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e8a95689-64c0-300f-be80-7c576b870e93 | -14.69648 | -48.27565 | 2025-10-01 03:32:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 58103b5f-7cbd-33e4-92ac-2d6d7b9dd319 | -18.32544 | -44.77126 | 2025-10-01 03:32:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 85120d29-cf38-396a-8f88-89822fed1a92 | -22.25081 | -43.42455 | 2025-10-01 03:32:00 | NOAA-20 | VASSOURAS | RIO DE JANEIRO | Brasil | 3306206 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| ce07b817-4fb9-35d4-91b4-898d995c8585 | -14.75724 | -45.75958 | 2025-10-01 03:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a2d9a646-77b7-30e9-a9dc-2eb15e6a3501 | -15.10512 | -44.95539 | 2025-10-01 03:32:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 15382d4c-bdbd-38ab-81c0-6f5fd74bd8c4 | -15.48944 | -45.91232 | 2025-10-01 03:32:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bc3d030d-ce34-352f-afdf-e3cddb80a799 | -19.88686 | -42.63245 | 2025-10-01 03:32:00 | NOAA-20 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 79a1d81a-7a5f-3070-bf15-fba4231c6de8 | -17.95508 | -45.02542 | 2025-10-01 03:32:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ee4a7b3a-4330-3d2a-a593-0ed8b5dae522 | -20.02675 | -44.54299 | 2025-10-01 03:32:00 | NOAA-20 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| 48c814a7-6ac8-3a1c-b74b-7d04341f22b1 | -15.61247 | -46.91311 | 2025-10-01 03:32:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0a714256-c5b7-3deb-b7be-3e54d756421c | -17.28065 | -44.9226 | 2025-10-01 03:32:00 | NOAA-20 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3594d05b-dfc2-338c-99cb-76dc7d4a1f62 | -18.33479 | -41.80837 | 2025-10-01 03:32:00 | NOAA-20 | CAMPANÁRIO | MINAS GERAIS | Brasil | 3110806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| f67de259-b702-3c77-834d-ba99608b8979 | -14.35924 | -47.13787 | 2025-10-01 03:32:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 66dfbbbe-e591-3b5f-ac61-83e7cc3e631f | -21.33537 | -45.878 | 2025-10-01 03:32:00 | NOAA-20 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| b2fc44ab-03f0-34c4-ac11-db054c7affd3 | -19.8581 | -42.59137 | 2025-10-01 03:32:00 | NOAA-20 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| b0fc6d5c-48b6-3eb8-92d0-60e752a4ac16 | -15.40544 | -47.05843 | 2025-10-01 03:32:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6c0b4919-6459-3bfa-bb12-56761ae09eda | -14.75002 | -45.77145 | 2025-10-01 03:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2bbee5ce-fbca-3bbf-8e9b-5ca4ce5d6096 | -19.31627 | -43.88236 | 2025-10-01 03:32:00 | NOAA-20 | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bcb719aa-b394-3eae-8fc9-4b336031b1b0 | -14.34453 | -45.91072 | 2025-10-01 03:32:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| cd29b192-2f2c-3d9b-8708-3a153888d522 | -14.68135 | -48.12876 | 2025-10-01 03:32:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1a046b23-fc26-3963-bb03-13c5f15e0dfc | -14.89606 | -48.12962 | 2025-10-01 03:32:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7aa4f615-bc26-3b1e-bbd0-6ef43721d051 | -13.93962 | -48.12973 | 2025-10-01 03:32:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| fc939797-aed0-396e-8ab8-86dc9cb3a631 | -15.3632 | -46.10904 | 2025-10-01 03:32:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b56b3b71-7423-3bf4-b21a-eee66ea61e2e | -18.32921 | -41.81287 | 2025-10-01 03:32:00 | NOAA-20 | CAMPANÁRIO | MINAS GERAIS | Brasil | 3110806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 2fcdde14-de0f-3629-b4d6-1b73a52f93dd | -15.75324 | -43.69392 | 2025-10-01 03:32:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e7e70014-9883-3566-9a0b-644e7d2da71d | -18.96327 | -43.71151 | 2025-10-01 03:32:00 | NOAA-20 | CONGONHAS DO NORTE | MINAS GERAIS | Brasil | 3118106 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bb814d1b-41de-38fa-a3b6-b443bb344be6 | -17.28149 | -44.91863 | 2025-10-01 03:32:00 | NOAA-20 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 049d586d-3887-302d-99ce-d27bc58469cb | -15.53184 | -45.22183 | 2025-10-01 03:32:00 | NOAA-20 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b40078b5-1008-3de4-9245-737e257c7deb | -14.95183 | -47.51947 | 2025-10-01 03:32:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 67f2a513-58c5-37ce-b440-da5cb656d97b | -20.01267 | -44.12518 | 2025-10-01 03:32:00 | NOAA-20 | IBIRITÉ | MINAS GERAIS | Brasil | 3129806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 175665e0-7be2-314c-b6ba-f51502cc7008 | -19.86468 | -42.58242 | 2025-10-01 03:32:00 | NOAA-20 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| e655a63e-80ae-355a-a060-9c9c67ad4d10 | -22.11023 | -44.70094 | 2025-10-01 03:32:00 | NOAA-20 | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| f59f5db5-ec7b-3a50-b1c3-b7441f8dcd76 | -20.61828 | -46.19802 | 2025-10-01 03:32:00 | NOAA-20 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 78c7a0d9-3784-3691-97d5-2ef0cff8a48f | -15.48737 | -45.92213 | 2025-10-01 03:32:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a704aed5-5142-36d6-8faa-2ac08cc88c10 | -17.40448 | -47.15666 | 2025-10-01 03:32:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cb8adaaa-07c1-3d9c-b0c5-009ac3d7c708 | -14.98125 | -46.9616 | 2025-10-01 03:32:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 102b1841-2651-3d73-a3a3-bc85428a44f6 | -22.1235 | -44.68819 | 2025-10-01 03:32:00 | NOAA-20 | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| 1e5e663b-88ef-319d-9f1e-10ce30856e72 | -15.54072 | -44.33566 | 2025-10-01 03:32:00 | NOAA-20 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 3ffff42a-76c6-3ed9-89f4-0028f9cb7049 | -13.92368 | -48.10064 | 2025-10-01 03:32:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4bf7fa17-2510-3311-9ccf-16e084880f7d | -17.95415 | -45.02971 | 2025-10-01 03:32:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e155edac-06b2-3ad2-a815-ce1abc076c91 | -15.33006 | -47.9433 | 2025-10-01 03:32:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README23.md)

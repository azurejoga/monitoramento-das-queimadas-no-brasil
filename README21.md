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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e4a6ef93-4c4f-3905-a17c-628504eeb462 | -6.38536 | -53.35329 | 2025-07-29 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7079333a-cdac-3e4c-b501-9b5c9aeb7639 | -7.74569 | -51.10276 | 2025-07-29 05:10:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e3d5c369-172a-3cfb-9594-b90529aa16c7 | -4.12873 | -54.89802 | 2025-07-29 05:10:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d830476d-4285-342e-bbfc-9ac276854bb6 | -7.93624 | -44.0907 | 2025-07-29 05:10:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| c1d8195d-ff53-3571-9278-8cd5df45765c | -6.39851 | -53.36952 | 2025-07-29 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 581a5cb8-cf79-328e-921f-7b086529e424 | -6.54378 | -56.19749 | 2025-07-29 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2bd72134-3401-39e7-b754-e9f3db7aa9b6 | -10.34612 | -57.508 | 2025-07-29 05:10:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 271e8aff-51a2-33d8-ab68-b9a1d41e70be | -7.91838 | -44.08892 | 2025-07-29 05:10:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1e453f27-54d9-3f6c-b8b8-01e26edde15a | -10.51423 | -50.25722 | 2025-07-29 05:10:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b195a540-9054-39d0-8fc2-8458eabe0e7d | -6.42347 | -53.35893 | 2025-07-29 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 86fd262b-b84f-38f8-861a-76d3d4d26936 | -6.42036 | -53.35371 | 2025-07-29 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f1669978-d1aa-3354-8d9d-cafc2ea2a8ac | -6.54434 | -56.19392 | 2025-07-29 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 93e567fd-c8c6-3a25-ab86-2461a9e4e5f1 | -6.54826 | -56.19084 | 2025-07-29 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bc5b97d9-6a69-36ea-b45d-546039c60eed | -6.39267 | -53.33036 | 2025-07-29 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 75821e1c-a658-3bf8-8ca7-8a023dbae2a4 | -6.39508 | -53.34035 | 2025-07-29 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c6d96134-3142-32b7-9fff-69f47a7239a7 | -6.52365 | -56.21635 | 2025-07-29 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2dd89964-cd8d-34a2-b7fe-d79201b33e9f | -6.39127 | -53.33979 | 2025-07-29 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 725a8e43-6f67-3ef4-86f7-254e7f952bdd | -7.72411 | -51.11092 | 2025-07-29 05:10:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 50576b74-8ade-38e2-9a3b-39bd894642e0 | -11.42764 | -45.12112 | 2025-07-29 05:10:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 26.5 |
| 9ba5a061-bf2f-3e77-816a-f0f77758e95d | -9.70745 | -48.61544 | 2025-07-29 05:10:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 57d781b6-b5aa-3bdc-afbf-4627dd0acbe9 | -6.5035 | -56.21323 | 2025-07-29 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9305c77f-8663-3ad4-b35e-c4e49aa47cf3 | -6.38605 | -53.34861 | 2025-07-29 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 744e08c4-731f-3c64-97da-1a8ba273aebd | -6.52756 | -56.21328 | 2025-07-29 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 96a6d1dd-d860-374a-8d0c-fcd659b003fb | -6.50014 | -56.21271 | 2025-07-29 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cc65be9f-33e3-3dd8-898f-469c2d6dba11 | -6.49343 | -56.21167 | 2025-07-29 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 15a24056-2397-36c3-9520-d7e7bf2e22d0 | -6.49398 | -56.2081 | 2025-07-29 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e6301e55-7470-3673-8590-68bf630a7a82 | -6.49789 | -56.20504 | 2025-07-29 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9ba5ed0f-d25b-3030-b3cd-541d7df5f2f4 | -8.94848 | -46.74849 | 2025-07-29 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 821584f2-70b2-3feb-847b-8a786d5d2417 | -6.50686 | -56.21375 | 2025-07-29 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| cc5a1a03-f523-3b24-b631-c53f7f1cb98c | -11.43315 | -45.135 | 2025-07-29 05:10:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 25.2 |
| e4ec6600-caaa-30ca-bee4-fc853a8ea001 | -4.22163 | -56.08232 | 2025-07-29 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ac8adbcc-e4a6-3a5b-bcf6-2c1dcdaef45a | -6.38225 | -53.348 | 2025-07-29 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ec2ad4f8-31b7-39d4-aae8-6c1927058c87 | -10.62422 | -45.23139 | 2025-07-29 05:10:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 94257c70-67b1-3943-9754-50b0e4c7254b | -5.99018 | -52.201 | 2025-07-29 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3d6f312e-aa23-3ac7-9a58-0bb35bdfb276 | -6.40442 | -53.35609 | 2025-07-29 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a66dff81-e3d7-3bb3-a8ed-f1784e1f792b | -7.9193 | -44.08172 | 2025-07-29 05:10:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f50ee159-8d8c-3df7-b609-d42817852783 | -9.58906 | -44.46253 | 2025-07-29 05:10:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8651ba37-18e5-39b9-93ff-25912d4655c3 | -9.99941 | -48.12665 | 2025-07-29 05:10:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d6438eea-6dbd-3477-86e6-c6c1c48f068b | -6.4489 | -53.36493 | 2025-07-29 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bd70027f-f5e5-3656-81fb-2de19053dce6 | -10.62372 | -45.22954 | 2025-07-29 05:10:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0eaf8a81-9778-3133-83a5-e1196ff56f5b | -6.40232 | -53.37009 | 2025-07-29 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bbefbba4-2a7d-3e96-9e1c-f9440dc4d4f0 | -6.49845 | -56.20147 | 2025-07-29 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2ebfc77b-fcca-3f6f-8884-bafef5b5320f | -6.55387 | -56.19902 | 2025-07-29 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d73ef915-6582-361d-87fe-67fd4837123f | -7.86419 | -47.87334 | 2025-07-29 05:10:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bd827e68-dd82-3a53-94bc-0a56318c8fea | -10.94981 | -54.37029 | 2025-07-29 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5418ac07-fd19-3e4c-8c7e-cf71e2464f42 | -6.5242 | -56.21277 | 2025-07-29 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5ed1c93a-cfb9-3d31-9d34-942967e79ee8 | -7.93972 | -44.09167 | 2025-07-29 05:10:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| a8d8932f-869c-3e48-9c02-1c3867589a7f | -6.5007 | -56.20914 | 2025-07-29 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 637b7562-d752-374f-b93d-5e45b4433c81 | -6.39649 | -53.33096 | 2025-07-29 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2f1183b3-e71b-3602-a06e-caca34dae64e | -9.46083 | -57.84977 | 2025-07-29 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| cdb0c329-704a-3553-8b1c-f9717361dcab | -7.93536 | -44.0979 | 2025-07-29 05:10:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| c95a5734-d3c4-378a-8ffc-4c1273bf6bb7 | -7.72352 | -51.11503 | 2025-07-29 05:10:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 90b8e527-c641-3a7a-94c8-5266b9bdf9a9 | -6.41966 | -53.35839 | 2025-07-29 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4a821f9b-05c8-3ead-9de1-3dad08339e12 | -6.49509 | -56.20095 | 2025-07-29 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 17d5343b-5613-34cc-ae14-0d4627a91c21 | -7.91577 | -44.0807 | 2025-07-29 05:10:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2680a480-ab3a-3952-942c-bff5228bd7b2 | -6.50741 | -56.21017 | 2025-07-29 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e8e90925-06c9-3f40-9d39-cd1570b0fa6c | -6.49173 | -56.20042 | 2025-07-29 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 13cb074e-01a4-34bf-bf54-71a11f920f30 | -8.95466 | -46.749 | 2025-07-29 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 8802e5fe-7dac-37eb-b70b-658faf319cd7 | -9.45753 | -57.84924 | 2025-07-29 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| fbdada07-fdfa-3939-92a2-64999dea43b9 | -9.7079 | -48.61187 | 2025-07-29 05:10:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f8d6c14f-1415-3bce-9e73-23c973e49bfb | -7.45652 | -49.3962 | 2025-07-29 05:10:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8b189921-223d-351b-a237-5404784a1232 | -7.45612 | -49.39914 | 2025-07-29 05:10:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6e520b50-1917-3cbe-aba8-67bff7288743 | -6.52085 | -56.21225 | 2025-07-29 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b474b0db-b539-304c-bd79-57c7a22462a8 | -6.56198 | -56.18206 | 2025-07-29 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 99e51b3f-3540-3e35-aa09-752f4c56fa0d | -8.94784 | -46.75345 | 2025-07-29 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 1f1f8d4c-f42a-34a3-8a23-34900758b696 | -6.39299 | -53.35436 | 2025-07-29 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| eac5ee3e-9f8c-345d-ad20-e4bd09186501 | -9.45476 | -57.84523 | 2025-07-29 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a1b918a3-b2b5-37f9-9cbe-0398bb618718 | -11.34126 | -51.25383 | 2025-07-29 05:10:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c7bf499e-9b3a-3e51-b23c-b655451349b3 | -6.37983 | -53.33806 | 2025-07-29 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 385fe698-46c2-3f4d-af70-acfc1361f97b | -3.88383 | -54.24141 | 2025-07-29 05:10:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 58803bd3-f3bf-3888-8c6f-ebd92007a427 | -6.45087 | -53.35821 | 2025-07-29 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d0bdc896-54d1-370f-8f0b-a71d331e0bc1 | -7.85782 | -46.73203 | 2025-07-29 05:10:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 6bd2df4b-e13f-379b-ad38-606e1462fc77 | -7.73598 | -51.10652 | 2025-07-29 05:10:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ec7553b2-bbc5-392a-9df4-ce0d77e121d1 | -6.45271 | -53.36549 | 2025-07-29 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 440848d0-d3c4-39ed-b8d2-9c8bb5fe8d3a | -10.55143 | -50.24469 | 2025-07-29 05:10:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6a34db26-6ee0-3369-9993-83fd894301ae | -10.66829 | -56.55256 | 2025-07-29 05:10:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bdd1e4bc-b3a2-3c11-ad7e-6c27f38b7a17 | -9.36247 | -45.7332 | 2025-07-29 05:10:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8f166e60-47d6-3809-90e6-aa1264276f74 | -11.34193 | -51.24878 | 2025-07-29 05:10:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c986368a-c274-3025-b0a8-cfe4c76dfb10 | -6.38987 | -53.34916 | 2025-07-29 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1710960d-3c23-36d4-8949-2827fcad8e14 | -3.88322 | -54.24537 | 2025-07-29 05:10:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 21d8d07e-1741-3d6f-a283-e3d45ecaf8c1 | -6.4534 | -53.36082 | 2025-07-29 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f7455d2a-58e8-38cb-a729-6d9f8c9545c1 | -6.49679 | -56.21219 | 2025-07-29 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 31ae4eba-af3b-38df-872c-b70debbd3e00 | -11.33723 | -51.24813 | 2025-07-29 05:10:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4d3febe9-1710-3d95-9188-49d7e36d364a | -7.92201 | -44.0888 | 2025-07-29 05:10:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| df833581-7a8e-3760-abd3-c2bbf7b76fad | -8.88717 | -47.34267 | 2025-07-29 05:10:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ce507e08-2558-3800-a8d1-2bc047129534 | -11.43387 | -45.12861 | 2025-07-29 05:10:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 25.2 |
| 1cecbf22-895b-36c0-8846-2a7140c6d393 | -7.86187 | -47.87213 | 2025-07-29 05:10:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6e94e22b-1caa-3cc6-a298-5c890a7b2e7b | -10.63111 | -45.23203 | 2025-07-29 05:10:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0083e4e1-fb53-3359-baa2-fcde6bd233e8 | -9.39887 | -45.49269 | 2025-07-29 05:10:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 2a708338-41bd-3994-b582-b87824c934a9 | -6.38745 | -53.33923 | 2025-07-29 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a384bac0-dc5f-3074-83f0-e759bf0b33de | -6.38675 | -53.34393 | 2025-07-29 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e03cfe8b-3162-3ab9-969c-80b03b82ba51 | -6.50295 | -56.21681 | 2025-07-29 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 041e02a2-b3bc-326d-ada2-2b402b1f2f84 | -6.50125 | -56.20556 | 2025-07-29 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 84b03b9e-4a63-34b2-ae7e-9aa1698d6dc8 | -5.35611 | -45.27103 | 2025-07-29 05:10:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7da1ed84-e77e-387d-96e1-ba889eae435b | -7.46117 | -49.39991 | 2025-07-29 05:10:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6e00777f-58a9-3940-bbf6-2480ea381b06 | -10.63062 | -45.23012 | 2025-07-29 05:10:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cf1a7b31-3d3f-3b66-aaf3-e427f2ffae0a | -6.49007 | -56.21115 | 2025-07-29 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a95219ba-e455-3615-894a-a4b2a08b6e46 | -11.42621 | -45.13378 | 2025-07-29 05:10:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 25.2 |
| 3d1e7660-eb22-35c6-9ddd-d920f4dc81db | -7.85843 | -46.72741 | 2025-07-29 05:10:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 85815dd5-fea4-3741-a7e2-3d3f820afac3 | -10.95077 | -54.36856 | 2025-07-29 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README22.md)

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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 86deea50-cb2d-31b1-8b90-0b9ce736a95f | -17.04915 | -56.74806 | 2024-09-30 04:34:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.6 |
| 487c4f74-f519-3ee3-a695-9ecfc8ea99f6 | -17.04833 | -56.75246 | 2024-09-30 04:34:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 7d310d9a-795a-3fbf-8210-df140d174083 | -17.04811 | -56.72958 | 2024-09-30 04:34:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 235afe6d-e437-3ba0-ba07-9c2ff0507807 | -17.0475 | -56.75686 | 2024-09-30 04:34:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| a716ea1e-e460-3c89-9826-d6f8996847da | -17.04728 | -56.73396 | 2024-09-30 04:34:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| e7f17cfc-2a5a-350c-b62c-51a068728cac | -17.04646 | -56.73835 | 2024-09-30 04:34:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 94152e77-b92c-3aa2-8316-650c70aafa25 | -17.04376 | -56.72867 | 2024-09-30 04:34:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 200c4fad-26e7-3cff-b273-fe44ed9ca099 | -17.04293 | -56.73306 | 2024-09-30 04:34:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 26202cfe-eebe-3e8a-a2c7-1a0cf90df06a | -16.85379 | -56.72561 | 2024-09-30 04:34:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 0767ecbd-4a5c-3e1e-972e-a9fa07561d8f | -19.152 | -57.47803 | 2024-09-30 04:34:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.4 |
| ee934baa-47dd-3bd3-a008-e2015b77fc79 | -19.14758 | -57.4772 | 2024-09-30 04:34:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 446b90c8-0346-34de-9fa5-16dbdf0be39a | -19.13877 | -57.4755 | 2024-09-30 04:34:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 5eb395ee-7e39-3dae-8938-1d4324c950b1 | -19.13436 | -57.47464 | 2024-09-30 04:34:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 1da97594-a352-3943-a00f-d70b7ab4c12b | -19.12994 | -57.47382 | 2024-09-30 04:34:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| b26cbf41-be19-36b7-860d-2fbacf7bc694 | -14.90674 | -57.9696 | 2024-09-30 04:34:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| b3e80b5d-618b-399d-94ac-5bb8f46fd088 | -14.90184 | -57.96854 | 2024-09-30 04:34:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 172e1248-13bd-329a-bfb4-cd88bcfc8851 | -14.90069 | -57.96723 | 2024-09-30 04:34:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| e0239590-84a4-33ba-9c9d-d7267f231628 | -14.88959 | -58.00479 | 2024-09-30 04:34:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d4916f97-f30c-366e-acc0-bda38325c4b5 | -14.88867 | -58.00363 | 2024-09-30 04:34:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 12f82356-3656-3585-92cf-e499cab92bac | -14.88765 | -58.00901 | 2024-09-30 04:34:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| ee7cfe62-86ea-3859-bfe9-f22a8938778a | -14.88765 | -57.9887 | 2024-09-30 04:34:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 14.0 |
| b13947eb-4bc3-3881-98b3-22a0c981222d | -14.88664 | -57.99382 | 2024-09-30 04:34:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 0ea1aac7-9702-3f22-b351-1b89ac2ea78b | -14.88663 | -57.98753 | 2024-09-30 04:34:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| ed99124e-8a34-3487-8b8e-658e59065237 | -14.88564 | -57.99277 | 2024-09-30 04:34:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 65224e41-1fc9-3963-9b2f-da7df8524f6a | -14.88561 | -57.999 | 2024-09-30 04:34:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 775c00e1-bd8e-3a23-abd5-312e97e11455 | -14.88463 | -57.99802 | 2024-09-30 04:34:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 8bd81a8d-f587-3e58-bdd8-a431d87a4c58 | -14.88457 | -58.00425 | 2024-09-30 04:34:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6191bcf4-1b90-381b-ba61-3aba2f7cb053 | -14.88363 | -58.00328 | 2024-09-30 04:34:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 647e8d7a-dd41-332b-8260-a0a67309c011 | -14.88349 | -58.00975 | 2024-09-30 04:34:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 65b2152a-bde0-3bc6-994f-054c443e2574 | -14.88272 | -57.98776 | 2024-09-30 04:34:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 16435857-13fd-397f-a845-9bf28588efbb | -14.88259 | -58.00875 | 2024-09-30 04:34:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f22941bc-5acb-36ed-b29b-ac8908036a97 | -14.88163 | -57.99331 | 2024-09-30 04:34:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 56918c3d-30a7-3b79-b020-f4cd0fa0ed27 | -14.77461 | -58.22106 | 2024-09-30 04:34:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9d589ef6-c4f1-38ed-a2ed-5dfe01941927 | -14.77403 | -58.22402 | 2024-09-30 04:34:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8dc6a548-586d-312f-8d7b-162480730228 | -14.77021 | -58.217 | 2024-09-30 04:34:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8ac36ed3-feef-3d5c-ae62-6c6e47b2daa3 | -14.76903 | -58.22299 | 2024-09-30 04:34:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| db248893-b519-3fa7-bf0b-5c4346d4275c | -14.76845 | -58.22596 | 2024-09-30 04:34:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6ff093cf-1cbd-385a-b2ca-895cda40d0f3 | -14.76787 | -58.22894 | 2024-09-30 04:34:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 422215f3-79e3-33a8-ac1f-b3f059ce3bfc | -15.27897 | -58.18303 | 2024-09-30 04:34:00 | NOAA-20 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3831a9b1-c7a6-354a-b9a8-e2a7de174989 | -15.27852 | -58.18213 | 2024-09-30 04:34:00 | NOAA-20 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f29dcff2-4f68-3dd0-96a2-d0050d51d13b | -20.20132 | -41.96698 | 2024-09-30 04:34:00 | NOAA-20 | REDUTO | MINAS GERAIS | Brasil | 3154150 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 14a81307-7ab9-316c-92a0-cb8a3d5ebcb2 | -20.20101 | -41.96995 | 2024-09-30 04:34:00 | NOAA-20 | REDUTO | MINAS GERAIS | Brasil | 3154150 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| dc09acca-cd12-3dde-80fa-c70fdd3aa937 | -20.16779 | -41.31877 | 2024-09-30 04:34:00 | NOAA-20 | BREJETUBA | ESPÍRITO SANTO | Brasil | 3201159 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 083f3845-46c3-32be-a4df-2e75fd51fa59 | -19.73048 | -41.64167 | 2024-09-30 04:34:00 | NOAA-20 | TAPARUBA | MINAS GERAIS | Brasil | 3168051 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| ceb5fbbc-8d9a-3666-9ffa-ade2d376388f | -19.73013 | -41.64491 | 2024-09-30 04:34:00 | NOAA-20 | TAPARUBA | MINAS GERAIS | Brasil | 3168051 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 9d42027e-339e-3f36-9bc3-c63061bc2c90 | -21.93089 | -41.55436 | 2024-09-30 04:34:00 | NOAA-20 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| da6dfd2e-51ca-3534-be72-ce0087bf15bb | -21.93054 | -41.55805 | 2024-09-30 04:34:00 | NOAA-20 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 386f53f5-bc41-351a-ad84-d5f846d8b65f | -22.70002 | -42.15614 | 2024-09-30 04:34:00 | NOAA-20 | SÃO PEDRO DA ALDEIA | RIO DE JANEIRO | Brasil | 3305208 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 2239bb2b-e5f0-3a72-8718-cc8e4558ce01 | -22.6997 | -42.15955 | 2024-09-30 04:34:00 | NOAA-20 | SÃO PEDRO DA ALDEIA | RIO DE JANEIRO | Brasil | 3305208 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 700215aa-0e68-34b2-9219-0ffc3d495f6c | -22.69477 | -42.15561 | 2024-09-30 04:34:00 | NOAA-20 | SÃO PEDRO DA ALDEIA | RIO DE JANEIRO | Brasil | 3305208 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| db1e385f-2224-3f5e-a43a-774ff5358701 | -22.46318 | -41.92267 | 2024-09-30 04:34:00 | NOAA-20 | RIO DAS OSTRAS | RIO DE JANEIRO | Brasil | 3304524 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 34296710-c6b2-31b3-a838-0eb1714ad598 | -22.46283 | -41.9262 | 2024-09-30 04:34:00 | NOAA-20 | RIO DAS OSTRAS | RIO DE JANEIRO | Brasil | 3304524 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 60c4eef3-c5f6-3a20-b03e-475ff338d547 | -16.00889 | -42.25422 | 2024-09-30 04:34:00 | NOAA-20 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 9804428f-8ad5-36dc-84a8-3e162761492d | -19.04642 | -42.94997 | 2024-09-30 04:34:00 | NOAA-20 | DORES DE GUANHÃES | MINAS GERAIS | Brasil | 3123106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 8d263a83-4404-38f7-ac74-390ddadd4037 | -19.04107 | -42.95456 | 2024-09-30 04:34:00 | NOAA-20 | DORES DE GUANHÃES | MINAS GERAIS | Brasil | 3123106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| fe303c08-71c3-3292-9125-ff382c7d2345 | -20.43107 | -42.33593 | 2024-09-30 04:34:00 | NOAA-20 | SANTA MARGARIDA | MINAS GERAIS | Brasil | 3157906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f3f77d2e-e6d3-3f52-8a35-586562b4b280 | -20.29218 | -43.51416 | 2024-09-30 04:34:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 9daa1eb7-71df-3dac-b4c6-292bf3bf0f0c | -20.29122 | -43.51027 | 2024-09-30 04:34:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| bbff9614-1d11-3deb-884f-5ace9f5a9810 | -20.29055 | -43.51646 | 2024-09-30 04:34:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| da950cab-7e7e-3158-9b92-feb233343583 | -20.09612 | -42.24498 | 2024-09-30 04:34:00 | NOAA-20 | CAPUTIRA | MINAS GERAIS | Brasil | 3112901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 38d9ad21-b536-379b-8a46-32859907914d | -20.07109 | -42.33435 | 2024-09-30 04:34:00 | NOAA-20 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 1227782a-9041-3e3c-990c-70a6f901228b | -19.89467 | -43.17345 | 2024-09-30 04:34:00 | NOAA-20 | RIO PIRACICABA | MINAS GERAIS | Brasil | 3155702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| a2d3c45b-fce5-34b9-be72-801bb81ee9d3 | -19.89407 | -43.17865 | 2024-09-30 04:34:00 | NOAA-20 | RIO PIRACICABA | MINAS GERAIS | Brasil | 3155702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| ee53e429-69bd-3445-9cd0-138bfd7fae97 | -19.89052 | -43.1679 | 2024-09-30 04:34:00 | NOAA-20 | RIO PIRACICABA | MINAS GERAIS | Brasil | 3155702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 1c5a7b02-6f75-32d7-9365-774875c96876 | -19.88988 | -43.17341 | 2024-09-30 04:34:00 | NOAA-20 | RIO PIRACICABA | MINAS GERAIS | Brasil | 3155702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 3c7ada0c-75e1-3088-afa0-6db073886628 | -19.8893 | -43.17845 | 2024-09-30 04:34:00 | NOAA-20 | RIO PIRACICABA | MINAS GERAIS | Brasil | 3155702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 9e6ca3d2-cbf9-3d53-ad6b-49135a5a7aa0 | -19.88577 | -43.16748 | 2024-09-30 04:34:00 | NOAA-20 | RIO PIRACICABA | MINAS GERAIS | Brasil | 3155702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| e2d1b6a7-8f2c-34ba-9ba5-87c3037e15a9 | -19.88513 | -43.17302 | 2024-09-30 04:34:00 | NOAA-20 | RIO PIRACICABA | MINAS GERAIS | Brasil | 3155702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 9bb6d4bf-251b-3b53-9b4a-1046277c1fc3 | -19.88042 | -43.17227 | 2024-09-30 04:34:00 | NOAA-20 | RIO PIRACICABA | MINAS GERAIS | Brasil | 3155702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 209de059-a39f-3f14-b007-a4a900dc38cc | -19.87567 | -43.17194 | 2024-09-30 04:34:00 | NOAA-20 | RIO PIRACICABA | MINAS GERAIS | Brasil | 3155702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 577dd967-e220-3664-93c7-109289d0fa80 | -19.85103 | -42.75296 | 2024-09-30 04:34:00 | NOAA-20 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 1dfad397-4c2d-3c7c-a65a-d1b4648a0bd6 | -19.8503 | -42.75928 | 2024-09-30 04:34:00 | NOAA-20 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 7119d14c-1439-303f-97fc-074f5337d942 | -19.8491 | -42.75381 | 2024-09-30 04:34:00 | NOAA-20 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 31ece42e-65ae-3146-97ad-56f1243b782e | -19.84846 | -42.75985 | 2024-09-30 04:34:00 | NOAA-20 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 68bf8fb0-3bb7-3d1c-970b-bccb704ef0b9 | -19.84623 | -42.75185 | 2024-09-30 04:34:00 | NOAA-20 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| 8cad0d77-3fc9-36dd-8a72-5bc6e29009ba | -19.84555 | -42.75782 | 2024-09-30 04:34:00 | NOAA-20 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| ceec0423-f2d9-3e2f-b590-f6ec5450c897 | -19.8443 | -42.75264 | 2024-09-30 04:34:00 | NOAA-20 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| 023c1539-1435-34eb-af88-8743d5bdda80 | -19.84369 | -42.75837 | 2024-09-30 04:34:00 | NOAA-20 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| cb0e4c68-aadd-3f8d-83a3-3c7e3248d935 | -19.52058 | -42.88088 | 2024-09-30 04:34:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 801aa74b-1712-3957-bacc-e2c2216560b9 | -19.52024 | -42.88298 | 2024-09-30 04:34:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 7c6b84d3-a431-358a-a1c0-49b325087e6a | -22.9028 | -43.66024 | 2024-09-30 04:34:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| fd2437fc-ecb5-3e40-bc2c-0c2f15bb7ac7 | -22.74154 | -43.76689 | 2024-09-30 04:34:00 | NOAA-20 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 38abeaf0-8e06-3491-8cd7-9600228a7a9c | -22.74042 | -43.7653 | 2024-09-30 04:34:00 | NOAA-20 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 424bd245-dcf3-38b7-a2ed-811877cbe4b6 | -22.73681 | -43.76642 | 2024-09-30 04:34:00 | NOAA-20 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 3916978a-91e4-311d-b76c-5ef1931801ea | -22.38814 | -43.39445 | 2024-09-30 04:34:00 | NOAA-20 | PATY DO ALFERES | RIO DE JANEIRO | Brasil | 3303856 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 369c0857-afe5-350e-9773-d783b0ed1332 | -22.38332 | -43.39391 | 2024-09-30 04:34:00 | NOAA-20 | PATY DO ALFERES | RIO DE JANEIRO | Brasil | 3303856 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 04931f49-fdeb-30d9-8dba-4232bf7cbd24 | -16.34884 | -43.69614 | 2024-09-30 04:34:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c8939d11-0e80-331c-8b5c-adf1eceaf6e4 | -17.09565 | -43.80426 | 2024-09-30 04:34:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bbe70580-b8d8-310b-8928-4eae2ee1b96f | -16.68228 | -43.88664 | 2024-09-30 04:34:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eba24a17-61f4-3027-b869-08e39c62b520 | -18.57603 | -43.86481 | 2024-09-30 04:34:00 | NOAA-20 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a8199a41-5033-3728-877b-35b891baec0e | -18.05271 | -44.39223 | 2024-09-30 04:34:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7139e856-69c7-3ab9-bacd-5cb974aa764b | -18.05219 | -44.39659 | 2024-09-30 04:34:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 232b7e77-4333-3309-9443-c5ac18041e93 | -18.01151 | -44.31191 | 2024-09-30 04:34:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 80cc55f8-c21a-3124-919b-9c2f82a6b620 | -18.00673 | -44.31535 | 2024-09-30 04:34:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e910b9bd-245e-3c0b-8a1a-801dfed5443f | -18.00245 | -44.31482 | 2024-09-30 04:34:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8cd24fad-4785-38d1-b3a7-91e401aa3e67 | -18.00195 | -44.31889 | 2024-09-30 04:34:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e6d10f62-fbdd-38c0-919e-a664e3ed3f9b | -18.6098 | -43.38105 | 2024-09-30 04:34:00 | NOAA-20 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 32a1d424-4d61-34dc-be7d-9256fd083d5f | -18.53188 | -43.37008 | 2024-09-30 04:34:00 | NOAA-20 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 8072196d-55f4-38dd-a3d4-b16996db72b3 | -18.52847 | -43.35943 | 2024-09-30 04:34:00 | NOAA-20 | SANTO ANTÔNIO DO ITAMBÉ | MINAS GERAIS | Brasil | 3160207 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 71f48569-268e-3737-b4ca-c4beeef3aa41 | -18.52452 | -43.3533 | 2024-09-30 04:34:00 | NOAA-20 | SANTO ANTÔNIO DO ITAMBÉ | MINAS GERAIS | Brasil | 3160207 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |


[Clique aqui para ver as próximas entradas](README53.md)

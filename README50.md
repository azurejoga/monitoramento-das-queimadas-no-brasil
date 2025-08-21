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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6ee8b81c-3b17-392a-8e1f-4d1cdbca99ee | -12.59582 | -47.08238 | 2025-08-21 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5bcc43b1-8893-3fa2-9eba-bd51b095f7e5 | -13.34179 | -54.39773 | 2025-08-21 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| be6d349f-b546-33f4-8551-76bd20f773bd | -13.16051 | -46.90715 | 2025-08-21 04:40:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3b6cdbc7-1a68-37c1-8670-362a9eaf5811 | -13.03745 | -45.1847 | 2025-08-21 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 62381ccb-8f4c-3c47-95eb-b5d92e085e3b | -13.01796 | -45.17055 | 2025-08-21 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 46.3 |
| 7a6cb0a1-3c72-385c-af6c-c367996fd6aa | -11.73845 | -58.31903 | 2025-08-21 04:40:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1994ccfc-f09a-31a6-809e-28e2a1bbf6f1 | -14.98654 | -54.83242 | 2025-08-21 04:40:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e2d4c424-ce23-3184-968f-1888afc494a5 | -13.03382 | -45.18082 | 2025-08-21 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 891d2da6-63f5-3ad9-a059-28a15b29623d | -13.86884 | -54.06695 | 2025-08-21 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a53552c1-338f-3dc3-a669-416a4dc69e1a | -10.71975 | -48.24188 | 2025-08-21 04:40:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 697a2685-4c2b-3265-ba73-f3e9faf19209 | -13.38236 | -46.22978 | 2025-08-21 04:40:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e10fc284-8e1d-38e1-a2b5-543123113eb8 | -14.64089 | -54.87799 | 2025-08-21 04:40:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d8ef231e-b908-3093-8a54-f2a3c9d50239 | -13.0364 | -45.19278 | 2025-08-21 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a80df044-8ca0-3bf3-910d-786201b928bd | -15.50444 | -48.0476 | 2025-08-21 04:40:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 786ebb69-df07-3625-b8e1-37439c6268a6 | -14.36602 | -51.97636 | 2025-08-21 04:40:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2f42bb4b-7c24-345b-81e9-02a5a4507cc7 | -13.38223 | -47.50171 | 2025-08-21 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5b6b468d-d3f5-334b-89f2-ed5722cfa1c2 | -13.04008 | -45.19799 | 2025-08-21 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fb408e44-4886-3211-b14a-790319d8961a | -12.95011 | -46.23538 | 2025-08-21 04:40:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 90d07fc5-1a66-3a71-841b-c569f0762d2f | -12.9574 | -46.2409 | 2025-08-21 04:40:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d4994b20-908d-3a98-86e8-0741e604db25 | -14.4736 | -48.3732 | 2025-08-21 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5e93e835-db41-3367-a48c-cd7d6d48dea9 | -13.5697 | -47.04251 | 2025-08-21 04:40:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a6a572df-a021-3cb8-a447-d3dc499b3ad0 | -13.04011 | -45.19735 | 2025-08-21 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c9ecadc1-813d-3f6c-b405-b742d4be1f31 | -14.36659 | -51.97279 | 2025-08-21 04:40:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e11b3587-37e7-38e3-8e27-7810a0f4f427 | -13.02572 | -45.20828 | 2025-08-21 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9f45e2dc-6cb9-3e0d-aa6b-d0fee1737640 | -8.87397 | -62.41129 | 2025-08-21 04:40:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2fd529d4-05c7-3c2e-aa5d-50d5cf0f82cc | -13.53807 | -47.04725 | 2025-08-21 04:40:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cf4465d7-cc15-35cf-97ac-2650cf72f824 | -13.03271 | -45.18885 | 2025-08-21 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1fc2a3dd-643c-321e-9931-41e560dd707b | -8.85685 | -62.39634 | 2025-08-21 04:40:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4d1ccb45-59e0-347b-a1b3-f9b599699d38 | -15.8896 | -49.01039 | 2025-08-21 04:40:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4eb3ea13-4397-3a04-8260-f3e3cbdc8ef9 | -10.40866 | -59.37798 | 2025-08-21 04:40:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5384c7b9-01d6-36df-b420-67b89c23db00 | -12.71683 | -44.78494 | 2025-08-21 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9cbc94aa-18b3-3eef-b899-24316fab4c24 | -13.74194 | -52.03433 | 2025-08-21 04:40:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0d1f7c64-6eda-335f-a6af-1ec4a7452765 | -14.65619 | -54.87643 | 2025-08-21 04:40:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 8f398f91-3fe3-338e-88bb-ddcb5cdcbbab | -13.65548 | -45.71501 | 2025-08-21 04:40:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 3f07a7c1-3ab3-3a58-b755-dfa0e2555be9 | -13.03896 | -45.20603 | 2025-08-21 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fe198712-aaf8-38d1-91b8-aaae799e4d54 | -13.02995 | -45.20887 | 2025-08-21 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 144107b1-f3b5-3a5d-bc67-b191581c9f3f | -13.51046 | -50.81586 | 2025-08-21 04:40:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bcad842e-a465-31d7-a28d-a164cdb9383c | -8.8667 | -62.41252 | 2025-08-21 04:40:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 35336bc8-039c-311d-ab33-6dfddd85286e | -8.86028 | -62.41115 | 2025-08-21 04:40:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 20.0 |
| f85a16cc-0f8b-3c52-a009-65d0c0b547ab | -13.49312 | -47.06742 | 2025-08-21 04:40:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c8179946-df2e-3e5d-853c-8a4cb17779bd | -12.58832 | -47.08134 | 2025-08-21 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bbd2a4f1-c0c0-3bbf-9d61-b31265b0cfc0 | -15.86228 | -48.77676 | 2025-08-21 04:40:00 | NOAA-20 | CORUMBÁ DE GOIÁS | GOIÁS | Brasil | 5205802 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fe34b44f-d96e-31de-b1b3-82a2ea03e162 | -12.22269 | -45.40846 | 2025-08-21 04:40:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1663581f-635a-3a65-9dfb-40bdef66a4a5 | -14.85351 | -47.95876 | 2025-08-21 04:40:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 4b68a2d1-2424-3950-ac0b-5c7287427682 | -12.21858 | -45.40777 | 2025-08-21 04:40:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 568d0425-ab5c-3b7b-9a5f-c949357a04f4 | -9.70399 | -57.8815 | 2025-08-21 04:40:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2e63ece5-a553-3740-954d-1003618e1f10 | -8.86465 | -62.42332 | 2025-08-21 04:40:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 24.7 |
| db567a61-5c54-33c9-9e74-88e3a42d9336 | -14.63953 | -54.86415 | 2025-08-21 04:40:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a5e33bd0-63e1-36d7-924e-cb9133c0f27b | -12.94678 | -46.23031 | 2025-08-21 04:40:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7be12462-cf66-3924-9444-633997d7353c | -12.64545 | -46.86778 | 2025-08-21 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d416bd8c-1533-3f3f-9131-89bc36b324d3 | -13.58073 | -47.55378 | 2025-08-21 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b9f4b874-cccc-346d-ab51-67b65faf3271 | -12.98119 | -56.87465 | 2025-08-21 04:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4572633a-d2c6-3c1d-ba36-785cb951127c | -16.21941 | -47.39398 | 2025-08-21 04:40:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 526eb837-46ed-3996-a846-2b7504cd0f71 | -15.50201 | -48.03817 | 2025-08-21 04:40:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 582a9d6b-dbd0-35c4-a96a-05ed597aa113 | -11.28889 | -46.28043 | 2025-08-21 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9a816c8c-6d9e-3d34-8f4e-8c834af0c7b2 | -12.93597 | -46.19161 | 2025-08-21 04:40:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2db17880-9a5c-31b1-929c-5c0f79037bb3 | -17.38995 | -44.24674 | 2025-08-21 04:40:00 | NOAA-20 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 94b026a1-ce48-3c19-8ba9-f050f9060786 | -17.39634 | -46.69825 | 2025-08-21 04:40:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e8d24dd0-ba5b-3ab2-8546-cd3f1515a820 | -9.89936 | -60.28739 | 2025-08-21 04:40:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a4b85a53-4610-3419-9954-dae1861a8a93 | -15.50264 | -48.03371 | 2025-08-21 04:40:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 6.6 |
| caac1036-0dbb-34b4-af66-2a0867a41931 | -13.81196 | -44.19771 | 2025-08-21 04:40:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9764a72d-1dae-3b5b-94d2-14b7cfc93bdf | -12.98552 | -45.21891 | 2025-08-21 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d9f7575e-9b65-3e39-8a4c-e3beaaf8f592 | -13.0211 | -45.17915 | 2025-08-21 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 41826c73-1894-3648-8172-b2ec35055f3f | -13.01686 | -45.17855 | 2025-08-21 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| ac203671-c1f9-35a0-9da4-5df4ce076454 | -13.17635 | -46.90502 | 2025-08-21 04:40:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5eea16ba-a534-34f7-8820-c88e6debbfc8 | -13.58004 | -47.55201 | 2025-08-21 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5963ac34-725c-3996-a9ae-f873dfe3217d | -13.04341 | -45.17389 | 2025-08-21 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 4edf34b7-dde0-314b-946c-dd78f3523395 | -12.98131 | -45.21829 | 2025-08-21 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b8f16e98-1f96-3214-b025-f9d7968c6ee0 | -12.08474 | -47.90569 | 2025-08-21 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 35186ba5-ca47-3478-bfea-b5feeba3ce1c | -13.35264 | -54.39964 | 2025-08-21 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c4f1344d-6173-321d-8ce7-5b9355b27157 | -14.12574 | -45.38303 | 2025-08-21 04:40:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 884aa3b7-4629-3446-bebd-fe5b2afc11d8 | -13.32514 | -54.408 | 2025-08-21 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 226d7513-3a48-3fc4-bd9b-37c8a324f716 | -13.02274 | -45.16714 | 2025-08-21 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 43.9 |
| 7deabd1c-1a19-397b-8e62-ab330979c51e | -11.2959 | -44.94328 | 2025-08-21 04:40:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eb4853d2-998f-3c7e-aa12-f4b1c061d035 | -13.19363 | -46.89272 | 2025-08-21 04:40:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 891d1239-d576-3814-a278-3046a21b70b7 | -8.87314 | -62.41385 | 2025-08-21 04:40:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 7.6 |
| e190ff60-85c2-3ad6-92d5-615db3b4a21f | -14.99815 | -54.83004 | 2025-08-21 04:40:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bb291688-6df0-3589-a0be-8f526c194a67 | -14.34285 | -53.10969 | 2025-08-21 04:40:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ca5cb473-61ed-3e3a-a3da-5ace8cbbb2c4 | -14.64968 | -54.87066 | 2025-08-21 04:40:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| b3886fd6-201b-3d90-a7cc-7d39d4ffe651 | -13.0434 | -46.83387 | 2025-08-21 04:40:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8fb53440-4ab1-3026-a578-7b7c2858374e | -14.75486 | -56.02088 | 2025-08-21 04:40:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cafc75e0-7c6a-3242-955f-c184e7b604f7 | -18.12641 | -43.95201 | 2025-08-21 04:42:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e05d1552-37e7-3cc4-83d7-cf3ab61b6c84 | -18.28641 | -45.51267 | 2025-08-21 04:42:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8dd25612-6743-3266-ada8-c625e4066b14 | -18.72714 | -43.84025 | 2025-08-21 04:42:00 | NOAA-20 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 15d5b7d9-8c68-3d83-a2dc-448d0ccd0175 | -19.80805 | -41.90641 | 2025-08-21 04:42:00 | NOAA-20 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 5d3578fe-b488-3f3d-bd5d-f9ee2f406f40 | -18.29481 | -45.51821 | 2025-08-21 04:42:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 156107de-1702-3041-a401-1175cfe18805 | -22.69324 | -43.73399 | 2025-08-21 04:42:00 | NOAA-20 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 7a020e9f-0337-35db-acf4-ba58c1769bab | -21.61425 | -46.87599 | 2025-08-21 04:42:00 | NOAA-20 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 845f0629-530a-3ad9-8ea7-9854044cd6f5 | -22.69886 | -43.73139 | 2025-08-21 04:42:00 | NOAA-20 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 265c8030-0de5-3ca7-b90d-375e2c4e1f9f | -18.6642 | -46.9725 | 2025-08-21 04:42:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c3730869-7b71-3e4e-aa9b-be47bf1959c6 | -18.28923 | -45.5269 | 2025-08-21 04:42:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a2490c2e-9755-3b83-8a08-d19e93d5ec4a | -18.28585 | -45.51738 | 2025-08-21 04:42:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ed4c8ff4-0838-3b2b-acc4-5410942deef8 | -18.29821 | -45.52761 | 2025-08-21 04:42:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| aaaafe23-0dc4-3950-b019-8ec903eea1a9 | -20.08287 | -46.13406 | 2025-08-21 04:42:00 | NOAA-20 | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3b65b202-b0bd-3884-a2c4-3e55d9d69497 | -17.82102 | -44.42231 | 2025-08-21 04:42:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 080e3651-a574-3d02-ac85-38757d5197f5 | -20.08233 | -46.13856 | 2025-08-21 04:42:00 | NOAA-20 | MEDEIROS | MINAS GERAIS | Brasil | 3141306 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 528728be-6449-3fcb-a59a-1ccab89edca3 | -21.61374 | -46.88015 | 2025-08-21 04:42:00 | NOAA-20 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 714a8944-d466-3042-81b6-e6097147ac89 | -20.74386 | -43.48653 | 2025-08-21 04:42:00 | NOAA-20 | LAMIM | MINAS GERAIS | Brasil | 3137908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 8fba9010-ea47-3e01-8148-e1fca935091e | -19.30071 | -46.02798 | 2025-08-21 04:42:00 | NOAA-20 | SÃO GOTARDO | MINAS GERAIS | Brasil | 3162104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b229f3b9-8d00-3942-b6f6-c75f0eaae5f5 | -18.12996 | -43.95062 | 2025-08-21 04:42:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README51.md)

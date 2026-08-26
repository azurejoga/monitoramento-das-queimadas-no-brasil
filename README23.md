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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ebce3bb6-3b1b-35a7-9e91-ea8d6ce4c77f | -14.55256 | -52.3153 | 2026-08-26 04:10:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ff073b14-2008-359a-85f1-056071337f0e | -20.60118 | -42.11705 | 2026-08-26 04:10:00 | NOAA-20 | DIVINO | MINAS GERAIS | Brasil | 3122009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| a7d80835-889a-3577-b2d1-903b5208bc47 | -13.17371 | -51.3432 | 2026-08-26 04:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ef8ad75c-c450-33b5-aa0e-61f955dbd10d | -13.2387 | -51.39159 | 2026-08-26 04:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 52e4ed36-6ec4-338e-a967-4fcdad36a165 | -13.22861 | -51.38575 | 2026-08-26 04:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| a1b4a24d-e545-37b3-8944-71de364c9052 | -13.64864 | -51.85154 | 2026-08-26 04:10:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3a2805df-afed-3130-beba-dc6b01bb2d7f | -20.51699 | -44.73399 | 2026-08-26 04:10:00 | NOAA-20 | CLÁUDIO | MINAS GERAIS | Brasil | 3116605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 842250f9-e714-3a70-a9a2-69b239900993 | -13.6554 | -51.84659 | 2026-08-26 04:10:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 229d8ce2-26fc-31e3-8129-86e59f758bfd | -20.52035 | -44.73463 | 2026-08-26 04:10:00 | NOAA-20 | CLÁUDIO | MINAS GERAIS | Brasil | 3116605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| c72190a3-0efe-37dd-904e-bc3db7ade1d7 | -14.66626 | -46.8942 | 2026-08-26 04:10:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f608e9e3-d7da-35d9-9dc0-848df00070b5 | -13.859 | -54.08217 | 2026-08-26 04:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| edf7b4e7-92dc-3ee7-971e-2c688132e955 | -14.9391 | -52.62927 | 2026-08-26 04:10:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e2811c88-e60d-3a25-8521-ff03aaa03119 | -14.79076 | -48.80595 | 2026-08-26 04:10:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| da7f6a7c-55d4-34cd-aad3-0a894df97a40 | -13.26468 | -51.46017 | 2026-08-26 04:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| bc9f43cf-0d70-3527-abe8-53524883b765 | -13.25403 | -51.51839 | 2026-08-26 04:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| bbc58dfb-abd4-3ab8-a6e6-c79c74a44aff | -14.79715 | -48.79652 | 2026-08-26 04:10:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 74ca9496-c3c1-318e-8ed4-6e832de8a3d1 | -13.22791 | -51.3893 | 2026-08-26 04:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6592135a-408f-30a4-95e8-fa6d03daafbc | -13.28118 | -51.4681 | 2026-08-26 04:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 082c6337-ac85-360d-b724-65d291572374 | -19.14013 | -46.67058 | 2026-08-26 04:10:00 | NOAA-20 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b2b71a5b-0ee5-3f8a-a555-85e065c14255 | -13.21454 | -51.3717 | 2026-08-26 04:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f68a3e55-c964-395a-9a4c-e040193a215e | -14.21584 | -45.25406 | 2026-08-26 04:10:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f68cbe7f-cfb3-3d01-83cd-f34c3c0322b4 | -14.36358 | -51.75756 | 2026-08-26 04:10:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b5722988-c65d-3765-9a03-35dca2a82d75 | -14.78628 | -48.80532 | 2026-08-26 04:10:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e87e98fe-8ce5-3a7e-bda5-ae56d5d0af3e | -18.94617 | -41.01471 | 2026-08-26 04:10:00 | NOAA-20 | ALTO RIO NOVO | ESPÍRITO SANTO | Brasil | 3200359 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 54d51b2c-0852-3b8a-b7bc-077a117dbec3 | -14.3643 | -51.75398 | 2026-08-26 04:10:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6cf51b98-4e27-3967-bbb2-267a0583d168 | -16.52255 | -49.42809 | 2026-08-26 04:10:00 | NOAA-20 | GOIANIRA | GOIÁS | Brasil | 5208806 | 52 | 33 | nan | nan | nan | Cerrado | 17.1 |
| ba901f87-2ecd-3e5b-a8e9-e73767e4388c | -13.23169 | -51.51308 | 2026-08-26 04:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 6efec83a-9da8-33e7-bd41-d9795023a17d | -13.18105 | -51.34261 | 2026-08-26 04:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 592669df-3c4f-36ab-88eb-17b11440be4a | -14.31852 | -51.72916 | 2026-08-26 04:10:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bdc87618-755a-3f97-b275-e465e79a961b | -20.25015 | -46.32881 | 2026-08-26 04:10:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 72068ecb-ea52-3b10-978c-69f2f8330193 | -13.27649 | -51.46337 | 2026-08-26 04:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2085c526-e45c-3221-ada3-563b3753ebe0 | -13.16763 | -51.34559 | 2026-08-26 04:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b6dbb14b-ec5b-30e1-9a05-9c33e66a8220 | -13.2481 | -51.40099 | 2026-08-26 04:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.1 |
| d66894c6-248e-3c8d-97fe-f5553c940624 | -13.2549 | -51.39503 | 2026-08-26 04:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 21.9 |
| b1b76a6b-24d5-3e96-b1bc-fe7aae835594 | -13.61191 | -49.01382 | 2026-08-26 04:10:00 | NOAA-20 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 600f86a2-52c3-38ea-8e3f-b64a15ad448a | -13.21384 | -51.37523 | 2026-08-26 04:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3b1adca0-fdf1-3d16-b520-1939c19bf27b | -13.23429 | -51.5287 | 2026-08-26 04:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 29ca8977-68b1-3069-84d8-15ad88090e2c | -13.86289 | -54.03291 | 2026-08-26 04:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 788ac687-4bef-3745-82cd-2cd84320e0fa | -13.28012 | -51.50148 | 2026-08-26 04:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8a105c1e-8524-3a43-a66a-ac7cb7c4b6ba | -13.2866 | -51.46926 | 2026-08-26 04:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 5eb38067-0f4e-37f8-9c60-1248751e9a62 | -13.26398 | -51.46375 | 2026-08-26 04:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e166a11d-5288-322e-a059-c27884b27aca | -14.5828 | -52.03 | 2026-08-26 04:10:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0cf85f5d-edc1-3ef6-991b-e3447d2c153d | -20.2509 | -46.3246 | 2026-08-26 04:10:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fc678124-1142-3dcc-af61-b358147c18ca | -14.76359 | -48.78836 | 2026-08-26 04:10:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 96c75df2-6148-39e2-9651-ee10a3fd7d4a | -14.53155 | -52.28768 | 2026-08-26 04:10:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6b769c69-2c62-3277-b855-ad49d317071a | -13.21993 | -51.37284 | 2026-08-26 04:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8bca64b7-a200-3553-8f7a-f00141d41aeb | -13.17302 | -51.34673 | 2026-08-26 04:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3cce8fce-ece4-324b-aac1-2b35a792cf41 | -13.42792 | -51.84924 | 2026-08-26 04:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a044dfd9-7c4f-3f86-a794-a1f245bf1d77 | -13.28732 | -51.46568 | 2026-08-26 04:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 487062c2-2af5-3d83-980f-8d28f3ca2586 | -18.94741 | -47.29079 | 2026-08-26 04:10:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4f6db0ba-f93e-30cb-8a36-e4cd9b73082d | -14.53077 | -52.29163 | 2026-08-26 04:10:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 64c0fdbf-8e98-3a47-be9b-0bc5bc3869ed | -14.29043 | -51.14476 | 2026-08-26 04:10:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 80ed8154-ba11-31f7-90a8-5f3166526dd2 | -20.59781 | -42.11647 | 2026-08-26 04:10:00 | NOAA-20 | DIVINO | MINAS GERAIS | Brasil | 3122009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 567667e3-f1d2-3ff6-a441-6c8f488daf50 | -18.64797 | -47.29021 | 2026-08-26 04:10:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| c7cfd8fa-5820-38dc-8e71-8c4205d152af | -20.11746 | -44.58047 | 2026-08-26 04:10:00 | NOAA-20 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| e95d4f49-6be1-3dda-9e0c-69a610dccf74 | -16.27287 | -42.53176 | 2026-08-26 04:10:00 | NOAA-20 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0c0087a3-aa2f-3527-91b7-2f2056075959 | -13.28483 | -51.50623 | 2026-08-26 04:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 95726e7f-e841-352e-87e6-b6bba199a7e2 | -14.39605 | -51.76463 | 2026-08-26 04:10:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bb55171c-4913-3784-b49e-68467367b5eb | -13.25089 | -51.38678 | 2026-08-26 04:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 7fc5e11e-3efd-31ab-bcf5-e4bda56b8c13 | -13.29887 | -51.46442 | 2026-08-26 04:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 49373e12-81f5-3c88-a451-4e34ad028e30 | -14.58797 | -52.03028 | 2026-08-26 04:10:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 23b69d6a-c44b-3f4a-8139-ac5f053bc7aa | -13.19183 | -51.34485 | 2026-08-26 04:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 4cb7c3ff-5320-3ff6-966b-34354525b887 | -18.76068 | -41.29897 | 2026-08-26 04:10:00 | NOAA-20 | CENTRAL DE MINAS | MINAS GERAIS | Brasil | 3115706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| fa5406a8-379b-31c0-9956-47e73df05ea4 | -13.27107 | -51.46222 | 2026-08-26 04:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 2364f5b3-f6cb-3926-9eb9-6b5056bce2dd | -14.55337 | -52.31135 | 2026-08-26 04:10:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e5d16a26-78ff-37e6-926b-f85ac29c96a8 | -13.66085 | -51.84806 | 2026-08-26 04:10:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 518b1b41-dfff-3450-9149-92335de7eb59 | -13.28093 | -51.46366 | 2026-08-26 04:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| fb7145ce-5ccd-3964-b25e-46f1b3e5bce4 | -17.77971 | -47.09594 | 2026-08-26 04:10:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| bcde1c05-5f3f-3ac3-abaf-b1ef2e68f555 | -15.76309 | -43.37442 | 2026-08-26 04:10:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4659349e-7fbf-3555-9288-61d44b157140 | -13.2467 | -51.4081 | 2026-08-26 04:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2aa1018d-fdaa-3b61-a1d2-fd173ff14bea | -13.60171 | -48.99192 | 2026-08-26 04:10:00 | NOAA-20 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 583419e5-02a4-3bb8-bae6-a625739e6f49 | -13.2495 | -51.39388 | 2026-08-26 04:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 450eaccb-f461-3639-b97b-db2e7f9536f4 | -13.28565 | -51.46843 | 2026-08-26 04:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d5ea3170-d071-3a9f-92aa-30d05af5c6fc | -14.41349 | -53.35659 | 2026-08-26 04:10:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d7e50864-2c07-36e2-a67a-dba7b1c6f198 | -13.23142 | -51.37159 | 2026-08-26 04:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 13.7 |
| da08404a-0bc0-3685-9ca8-73ef3efa56b0 | -16.95478 | -43.25744 | 2026-08-26 04:10:00 | NOAA-20 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0460859c-a4d6-3891-b9ab-3506c6ec036f | -13.2399 | -51.41404 | 2026-08-26 04:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9364274d-a57e-309e-a738-5b480bbe4658 | -15.8807 | -48.3418 | 2026-08-26 04:10:00 | NOAA-20 | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| d2c1b821-992c-315f-bcdf-37c193e5fae3 | -13.60729 | -49.01307 | 2026-08-26 04:10:00 | NOAA-20 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4145082a-0bd1-36f1-b9ca-220e39844e54 | -13.24044 | -51.52624 | 2026-08-26 04:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f2bdfac1-b8ef-3a8b-9855-216d30bc62ba | -13.17233 | -51.35027 | 2026-08-26 04:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b2b748df-4234-3e4d-b763-d018e9b9e4b8 | -14.58206 | -52.03371 | 2026-08-26 04:10:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f5137657-c934-3ca1-b9c0-aa00e589113f | -14.41945 | -53.35796 | 2026-08-26 04:10:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a3f2b199-58fd-36ca-987e-304b091f931d | -14.75818 | -48.76786 | 2026-08-26 04:10:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 45bcb229-c4c8-3960-ae7f-dd8120183954 | -20.51826 | -44.72637 | 2026-08-26 04:10:00 | NOAA-20 | CLÁUDIO | MINAS GERAIS | Brasil | 3116605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.6 |
| 76b9f44a-9401-32bf-bdae-746ef935ca0f | -13.28634 | -51.46485 | 2026-08-26 04:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d53ffb12-cb75-3e55-b3dd-3017db58af07 | -14.28979 | -51.14806 | 2026-08-26 04:10:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 31765a6a-66c0-3b59-8eb0-5c43b2cd2a33 | -13.29744 | -51.47155 | 2026-08-26 04:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 14.1 |
| ce500208-1271-39d8-a107-f9512dfe61e9 | -14.32472 | -47.23935 | 2026-08-26 04:10:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f4df4f42-2d18-36c1-9c43-bf0eb4073205 | -14.8843 | -40.87991 | 2026-08-26 04:10:00 | NOAA-20 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| d68007a8-795e-355a-992c-d9d532b21415 | -14.8016 | -48.79736 | 2026-08-26 04:10:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 34974fc8-dde9-3b11-9704-f363c49c8a49 | -14.53421 | -52.29112 | 2026-08-26 04:10:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b7f6e68e-900d-301c-bd29-e758b8cdf7df | -14.76267 | -48.78439 | 2026-08-26 04:10:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 41122ea7-eec8-3413-a0dd-7df251bf85a7 | -14.79273 | -48.79559 | 2026-08-26 04:10:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6bdba958-00fd-37b4-a791-ae761d89ef63 | -18.64582 | -47.29757 | 2026-08-26 04:10:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 834fd1c3-b858-3d07-94e4-1f586409e2d8 | -13.2708 | -51.45773 | 2026-08-26 04:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 10c0c4e8-2e04-36bd-842c-370b5c7f6a8a | -14.80062 | -48.80251 | 2026-08-26 04:10:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cb22292f-5b24-3b05-9968-81745d48f447 | -13.22533 | -51.37398 | 2026-08-26 04:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8ad649ad-ef44-3491-bd69-d26b007dd36b | -13.2474 | -51.40454 | 2026-08-26 04:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 19c7f770-258b-35fe-940b-c30f81f65f35 | -15.62399 | -48.19978 | 2026-08-26 04:10:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README24.md)

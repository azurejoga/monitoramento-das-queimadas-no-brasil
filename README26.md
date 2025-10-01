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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| acf7e6ea-c1e6-3849-a26a-472af2857025 | -17.96636 | -45.0272 | 2025-10-01 03:32:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 77734ccf-56f7-3807-a001-964821b6492e | -17.87041 | -42.25789 | 2025-10-01 03:32:00 | NOAA-20 | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| e1435de4-a130-35e1-8e89-a526580e0ed0 | -14.69579 | -46.9785 | 2025-10-01 03:32:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| bbec51dd-e484-38cb-a474-51db3aa14592 | -20.83411 | -43.01865 | 2025-10-01 03:32:00 | NOAA-20 | PAULA CÂNDIDO | MINAS GERAIS | Brasil | 3148301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 7039e176-69d3-3253-a5a6-7d3be3a6e07c | -14.62018 | -46.99007 | 2025-10-01 03:32:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 203bdd8e-b5f4-3e56-b699-64ff876d6db1 | -19.4592 | -44.28933 | 2025-10-01 03:32:00 | NOAA-20 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c9a82d5e-4f99-3748-812d-5ca64485c8c0 | -16.39888 | -47.05495 | 2025-10-01 03:32:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f323318f-6b15-3a88-b9b1-c2e69a79b2b6 | -18.7093 | -49.17265 | 2025-10-01 03:32:00 | NOAA-20 | CANÁPOLIS | MINAS GERAIS | Brasil | 3111804 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 16a1acc1-9436-3d50-b18b-676a55048638 | -20.61848 | -46.21629 | 2025-10-01 03:32:00 | NOAA-20 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 18c90e4c-0f2f-3cb4-8923-de821da7da8c | -14.72482 | -46.83308 | 2025-10-01 03:32:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7a7b4920-0246-34e8-8388-c8ab39e34819 | -14.67963 | -45.28827 | 2025-10-01 03:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0086c336-f6db-3f43-a5d9-1823bda9981c | -15.01093 | -46.97284 | 2025-10-01 03:32:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 164be314-2fc7-391e-823a-3fe759a5414a | -15.48332 | -45.90612 | 2025-10-01 03:32:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ff2bf002-cae1-3841-9e60-fa725881cf0b | -14.36891 | -47.13592 | 2025-10-01 03:32:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f1b280af-d818-3031-9087-7adb81c4fa28 | -17.86899 | -42.25728 | 2025-10-01 03:32:00 | NOAA-20 | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 7b98bfe2-2ebd-3644-9985-681841dbe9c9 | -14.35076 | -45.91227 | 2025-10-01 03:32:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1688c564-22f1-3f1c-bea3-6c555a5e71df | -14.72452 | -48.15086 | 2025-10-01 03:32:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b121f30c-bd13-3be8-83d4-4761b0fe91a2 | -17.96725 | -45.02306 | 2025-10-01 03:32:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d678aa0f-84a4-3967-a36c-6ab0028cbf5b | -16.37572 | -47.06771 | 2025-10-01 03:32:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 11b26354-170c-3a48-9197-5900d29cc4f8 | -14.04411 | -47.97697 | 2025-10-01 03:32:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 35bbf866-0ab4-3dc5-a279-940920e3e890 | -20.79445 | -43.52531 | 2025-10-01 03:32:00 | NOAA-20 | LAMIM | MINAS GERAIS | Brasil | 3137908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 6ea94b95-d6fd-3a8c-90b3-fda8cd8c4e7e | -14.7818 | -45.79559 | 2025-10-01 03:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 514450c5-6793-370c-97fb-288095c9e7ce | -20.633 | -46.17764 | 2025-10-01 03:32:00 | NOAA-20 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3924213f-c3d1-3b2b-b63a-fc6f729df46d | -14.34963 | -45.91759 | 2025-10-01 03:32:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 929cbb88-f451-3936-a660-01da274b56f1 | -20.22901 | -43.88887 | 2025-10-01 03:32:00 | NOAA-20 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 03a410e7-ee01-34b9-9f19-6a15ac9e8838 | -20.61349 | -46.21893 | 2025-10-01 03:32:00 | NOAA-20 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 6eb30c0d-8b07-30ef-a3ad-8a5d77966ed0 | -14.52619 | -48.37835 | 2025-10-01 03:32:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 307cbfea-a75f-31de-af02-f1a2c41c9a07 | -19.81063 | -44.07397 | 2025-10-01 03:32:00 | NOAA-20 | RIBEIRÃO DAS NEVES | MINAS GERAIS | Brasil | 3154606 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d6bed600-2342-3b4d-b388-0b5de1598107 | -20.6289 | -46.23005 | 2025-10-01 03:32:00 | NOAA-20 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 25ffcf51-6c80-30d3-85a7-7b6643a497e7 | -14.02729 | -47.97039 | 2025-10-01 03:32:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 27eb4d5f-f710-354e-ad78-d8bff8220a68 | -14.65514 | -48.14679 | 2025-10-01 03:32:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a8c069e5-119f-3de5-8dc6-ab9e0318921f | -19.86192 | -42.5896 | 2025-10-01 03:32:00 | NOAA-20 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 7c359d1d-6d69-3c03-91e4-4c2cf92a40a7 | -14.75815 | -45.7634 | 2025-10-01 03:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 74cb7fcf-1c77-3577-bc91-987ef7b0d423 | -15.93233 | -48.13931 | 2025-10-01 03:32:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 275bb332-1769-3d02-8a21-107d4352b100 | -14.69431 | -48.13712 | 2025-10-01 03:32:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 396a6a78-0805-3d6c-a560-a59609c8094f | -20.62315 | -46.229 | 2025-10-01 03:32:00 | NOAA-20 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b2064e16-dcbf-3f58-83ef-89d5dc152dc0 | -15.60631 | -46.91017 | 2025-10-01 03:32:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 13e489a3-5002-3f8c-b932-12002afe3287 | -20.62008 | -46.21624 | 2025-10-01 03:32:00 | NOAA-20 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 98eed0e9-27cd-3a6c-8944-2e28e39ba033 | -18.70395 | -44.33318 | 2025-10-01 03:32:00 | NOAA-20 | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8c8adcd0-df11-3b55-a979-722362de76ef | -17.95983 | -45.03041 | 2025-10-01 03:32:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 567cdfe4-f141-3b63-9820-d862c53752f4 | -14.36212 | -47.13476 | 2025-10-01 03:32:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| bf1bedeb-845b-37aa-817d-148eb6768647 | -14.79412 | -45.79843 | 2025-10-01 03:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 13.4 |
| db20939f-9374-3af9-8dd3-b6254a9a1589 | -14.78796 | -45.79702 | 2025-10-01 03:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 10.9 |
| a79bb869-31ed-3882-851d-5d3a77577ddb | -14.39176 | -46.22735 | 2025-10-01 03:32:00 | NOAA-20 | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 417e0f51-5403-38d9-8a9c-8b02eed19fd9 | -19.37472 | -42.78071 | 2025-10-01 03:32:00 | NOAA-20 | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 79c4d22a-1809-3787-9d6d-0c7bbb4e85df | -14.68861 | -48.1294 | 2025-10-01 03:32:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b7a9d2fd-7514-3377-b846-79b36a0e6670 | -20.02598 | -44.54655 | 2025-10-01 03:32:00 | NOAA-20 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| b275a753-a5b7-34b1-8b62-4bda7593c3b3 | -20.12757 | -44.02971 | 2025-10-01 03:32:00 | NOAA-20 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| bcd68f3c-6f09-3e81-9fc3-86e2f4370965 | -14.35187 | -45.90703 | 2025-10-01 03:32:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b78fcfdd-3ebd-3c4f-8ec3-8a318a2ba5ab | -15.53848 | -42.66121 | 2025-10-01 03:32:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 001d68c3-c570-3bd1-9824-68c5d957bfb7 | -15.48331 | -45.91088 | 2025-10-01 03:32:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e919887e-d2b5-3088-9e26-34dc82054839 | -18.80619 | -47.54973 | 2025-10-01 03:32:00 | NOAA-20 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 87e1aee8-a706-3605-aece-40543b58f802 | -13.9182 | -48.09174 | 2025-10-01 03:32:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 88614ad8-fc95-3d81-a365-6c4a2c93dada | -14.87002 | -48.32735 | 2025-10-01 03:32:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| b868b1ae-4e88-320f-a106-5502feaaae57 | -14.77664 | -45.78951 | 2025-10-01 03:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 43199100-7dbe-3612-b84f-6cc56fc124eb | -15.81332 | -41.89511 | 2025-10-01 03:32:00 | NOAA-20 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5da69f0e-5a7a-3f3f-8c02-88da5b4cf35a | -14.75617 | -45.76453 | 2025-10-01 03:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 240018b3-c4c6-30b6-b20d-6b1082e2967b | -20.58854 | -45.88493 | 2025-10-01 03:32:00 | NOAA-20 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c9cba188-4c3e-3547-ab11-46eb19436d60 | -17.49339 | -43.47508 | 2025-10-01 03:32:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d129dfd3-26fc-36ca-bb16-fb62d9a44294 | -15.47961 | -45.86429 | 2025-10-01 03:32:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 105e6b0d-4e62-313e-8bed-3f4ac4f7cbfe | -22.11685 | -44.69465 | 2025-10-01 03:32:00 | NOAA-20 | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 8041e0fa-1622-3236-8b01-d05e80b639e4 | -14.95315 | -47.51355 | 2025-10-01 03:32:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 05316146-455c-34ce-bc7a-c8b65ed4cde4 | -15.77776 | -43.71024 | 2025-10-01 03:32:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 20561191-2a05-3264-a951-5701e4be9f1c | -19.93622 | -43.90057 | 2025-10-01 03:32:00 | NOAA-20 | BELO HORIZONTE | MINAS GERAIS | Brasil | 3106200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| da25fc0f-e774-3f2e-86ec-a66451a1fd72 | -20.59753 | -45.88654 | 2025-10-01 03:32:00 | NOAA-20 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8ec7f5a3-a546-30c6-ab30-922620ae9df3 | -15.93543 | -48.126 | 2025-10-01 03:32:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5e89baca-9b18-3d93-a802-4cc828d30678 | -14.65707 | -48.13809 | 2025-10-01 03:32:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4163c097-f627-3dde-aa47-eced8401ffb0 | -20.48203 | -43.94541 | 2025-10-01 03:32:00 | NOAA-20 | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| b0d08527-4f47-3fcf-9233-8ddfdad37734 | -14.68518 | -46.96339 | 2025-10-01 03:32:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c822df6d-de2e-36b0-a248-a28ac1bba6b6 | -22.11332 | -44.68655 | 2025-10-01 03:32:00 | NOAA-20 | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 870e0e94-193e-3b3e-8427-18590084099c | -18.16409 | -46.10657 | 2025-10-01 03:32:00 | NOAA-20 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b93b5787-3571-3785-a908-b43d7c148d54 | -15.63332 | -46.25347 | 2025-10-01 03:32:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fa0ed54b-049c-3b5c-ae99-a23de7b2e263 | -14.90032 | -48.12896 | 2025-10-01 03:32:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 242c3a3f-1775-34fc-aa15-2dd99b71997d | -15.76 | -43.68812 | 2025-10-01 03:32:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 34375eca-fd32-3f1c-8279-b7477f56af33 | -14.59366 | -48.22224 | 2025-10-01 03:32:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 87631e35-6052-34d9-ba78-262895e422a1 | -14.68158 | -45.279 | 2025-10-01 03:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a1a6df52-97d9-3bfe-8325-af01c5f2fc58 | -20.02145 | -44.54164 | 2025-10-01 03:32:00 | NOAA-20 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 22e36fc2-0ab5-3fe5-9bf9-581ac8111fd1 | -16.43092 | -42.40868 | 2025-10-01 03:32:00 | NOAA-20 | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 1918d966-0fc1-3dbd-a588-fe46d41b496a | -14.74587 | -45.78225 | 2025-10-01 03:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| acf7a92d-8c5e-35f4-b5df-772c0ea9228b | -14.35057 | -47.14549 | 2025-10-01 03:32:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 11.8 |
| e97e2675-6c1c-3855-8a55-5a49a328cb17 | -18.33931 | -41.80925 | 2025-10-01 03:32:00 | NOAA-20 | CAMPANÁRIO | MINAS GERAIS | Brasil | 3110806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 0ff5c206-10f8-3f93-a775-39f1647d8a80 | -14.89681 | -47.2181 | 2025-10-01 03:32:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 518ebd2a-0ef3-301b-9509-1ae5536ba2c2 | -15.80169 | -43.32431 | 2025-10-01 03:32:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 39c19201-1b9d-3fcd-8595-ec1d097cb830 | -14.71295 | -48.13639 | 2025-10-01 03:32:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 783a2600-1e12-3255-b1e9-9012cae8bcfd | -15.33114 | -47.94384 | 2025-10-01 03:32:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ee72aea0-c4f9-388c-8623-6c8ea33cc12a | -14.78079 | -45.80029 | 2025-10-01 03:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 056bdb52-5664-3710-904b-66fec416a0fa | -13.93931 | -48.11945 | 2025-10-01 03:32:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 9e5cfbca-97dc-3daf-af33-2093a3f839a1 | -15.82235 | -43.32994 | 2025-10-01 03:32:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8c4be610-fdee-30a9-b6e3-3fef63015a2b | -20.62659 | -46.20666 | 2025-10-01 03:32:00 | NOAA-20 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7d0bbc53-a025-34c0-a555-397cffbd3b52 | -14.38058 | -47.13681 | 2025-10-01 03:32:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8ae7f2b2-1410-307e-9ff7-9bcecb2f25a1 | -15.1256 | -46.45306 | 2025-10-01 03:32:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 403b6dd8-afbe-3bc5-a7df-1acb6da360d6 | -20.61296 | -46.21424 | 2025-10-01 03:32:00 | NOAA-20 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 5a7d2331-458c-3d57-9ab9-ea153d8d98ff | -19.93228 | -43.89071 | 2025-10-01 03:32:00 | NOAA-20 | BELO HORIZONTE | MINAS GERAIS | Brasil | 3106200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 90842b27-3a65-398b-ba95-d7bc06239e9b | -17.38595 | -47.14418 | 2025-10-01 03:32:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 21d1df76-db1a-3b8c-b687-f8affcdd0183 | -18.60643 | -43.27494 | 2025-10-01 03:32:00 | NOAA-20 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| cede9067-e3de-3c63-bdfe-3813d351c131 | -18.70235 | -49.17105 | 2025-10-01 03:32:00 | NOAA-20 | CANÁPOLIS | MINAS GERAIS | Brasil | 3111804 | 31 | 33 | nan | nan | nan | Cerrado | 10.8 |
| a655c02f-f39d-349e-9be0-db15ceade860 | -18.41879 | -43.8172 | 2025-10-01 03:32:00 | NOAA-20 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c58311ad-5aab-3818-be5a-12505e68e3cb | -15.47943 | -45.86847 | 2025-10-01 03:32:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 599adbb0-1c65-3638-8204-72fd22dbd2bd | -15.47152 | -45.87191 | 2025-10-01 03:32:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2f21ede6-8ed5-394b-9f38-aef564779476 | -14.43092 | -46.35863 | 2025-10-01 03:32:00 | NOAA-20 | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README27.md)

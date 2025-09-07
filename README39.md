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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b552e658-c096-3f14-92f6-ecedff2cafbc | -20.35635 | -43.88244 | 2025-09-07 04:02:00 | NPP-375D | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| cd31c5f8-8387-32ab-b289-734cb207f49c | -21.71204 | -44.51415 | 2025-09-07 04:02:00 | NPP-375D | SÃO VICENTE DE MINAS | MINAS GERAIS | Brasil | 3165305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 7ebdccb9-950b-36cf-8615-de7ae6783e55 | -24.15303 | -49.52394 | 2025-09-07 04:02:00 | NPP-375D | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bc7ff04b-c02e-365f-8fc7-be38db7893be | -24.14752 | -49.51577 | 2025-09-07 04:02:00 | NPP-375D | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d0df10c1-fe2c-3847-8017-df7bfdf4cf67 | -20.34388 | -43.89247 | 2025-09-07 04:02:00 | NPP-375D | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 90474a54-10bc-3f5c-881a-fe63145f4b5c | -21.67712 | -45.08531 | 2025-09-07 04:02:00 | NPP-375D | TRÊS CORAÇÕES | MINAS GERAIS | Brasil | 3169307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 2176dc25-1858-3e5e-811e-9c820b1004be | -21.47137 | -43.91384 | 2025-09-07 04:02:00 | NPP-375D | IBERTIOGA | MINAS GERAIS | Brasil | 3129400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 8c372dd8-9968-366a-9e06-0d8aeb9b860d | -20.09643 | -45.3172 | 2025-09-07 04:02:00 | NPP-375D | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 39be7751-c319-3575-83a0-78b701422775 | -20.54525 | -46.44478 | 2025-09-07 04:02:00 | NPP-375D | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 15.8 |
| a2809e4e-f351-3340-8c51-4bc26dc0e558 | -21.63229 | -44.01302 | 2025-09-07 04:02:00 | NPP-375D | SANTANA DO GARAMBÉU | MINAS GERAIS | Brasil | 3158706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 470a0a5a-b6b2-3c61-a479-5522eaca40ee | -22.41872 | -47.43642 | 2025-09-07 04:02:00 | NPP-375D | ARARAS | SÃO PAULO | Brasil | 3503307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| f4d03047-1201-307d-8776-2b2fc7ef2be7 | -23.42825 | -50.79906 | 2025-09-07 04:02:00 | NPP-375D | SÃO SEBASTIÃO DA AMOREIRA | PARANÁ | Brasil | 4126009 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 18e666c8-1cd3-3303-a1cd-5a9c4e2a5d88 | -24.14315 | -49.51457 | 2025-09-07 04:02:00 | NPP-375D | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d914ecb6-07c8-3b3c-9461-32a8ab0dc9e4 | -22.70358 | -46.91717 | 2025-09-07 04:02:00 | NPP-375D | PEDREIRA | SÃO PAULO | Brasil | 3537107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 267fd74b-7153-31e1-bdf7-bbb186f8ee13 | -20.54629 | -46.43925 | 2025-09-07 04:02:00 | NPP-375D | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c2df1941-cbfe-389d-83cd-daf2283a40e4 | -21.71089 | -45.35696 | 2025-09-07 04:02:00 | NPP-375D | CAMPANHA | MINAS GERAIS | Brasil | 3110905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| b46ee1bf-ab9e-3668-a822-7f76b200ab74 | -19.8652 | -57.9058 | 2025-09-07 04:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 65.7 |
| cc46f062-5320-3465-b098-77bda2fcae31 | -19.8656 | -57.885 | 2025-09-07 04:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 78.3 |
| d4a56a0d-eff7-38ce-a81d-044e7450d3fb | -19.8853 | -57.9031 | 2025-09-07 04:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 69.8 |
| f3e124b0-337f-3e68-90e6-c59d5f21aac7 | -19.8857 | -57.8823 | 2025-09-07 04:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 60.4 |
| ebe1a6b0-7730-36ce-bd28-439fd9b465b4 | -5.64247 | -43.11843 | 2025-09-07 04:17:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 621921c7-4d1b-3cf1-8a25-42b9fc6ad8e8 | -4.80341 | -43.05979 | 2025-09-07 04:17:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 21e9b700-0669-3e6c-a270-228f597c0712 | -5.44223 | -42.80603 | 2025-09-07 04:17:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 35473cf1-4be8-3b8e-8b53-e58e55d7b62a | -4.89283 | -41.7556 | 2025-09-07 04:17:00 | NOAA-20 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 149c4d13-40df-3040-b279-b06fbd8189bb | -5.31208 | -42.80547 | 2025-09-07 04:17:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d9f4dedf-efd7-3abc-92f0-ef2f18d903e6 | -5.19817 | -43.70481 | 2025-09-07 04:17:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 270c1dab-848d-36c9-a78a-7189ac97af99 | -5.42156 | -42.68719 | 2025-09-07 04:17:00 | NOAA-20 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 035b3acb-61d8-3951-a7ca-7f659c5382eb | -5.22029 | -43.69397 | 2025-09-07 04:17:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| e1eae928-39e1-3138-93b4-5fc7b7663ded | -3.59386 | -47.51315 | 2025-09-07 04:17:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 777f3507-f7e1-3921-9802-2fc185670569 | -3.5902 | -47.51255 | 2025-09-07 04:17:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 6ad7702c-428b-31c3-86bc-a45179ebe367 | -2.54996 | -48.3959 | 2025-09-07 04:17:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 400ba4c9-2365-35c0-aa4d-53c23827d455 | -1.29178 | -48.43703 | 2025-09-07 04:17:00 | NOAA-20 | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2f4a72a6-5e67-3d30-93a5-1441743ee208 | -3.34631 | -47.60963 | 2025-09-07 04:17:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 3100a7db-722c-355c-a66d-910cf2766acb | -1.28957 | -48.4372 | 2025-09-07 04:17:00 | NOAA-20 | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 41678df8-f5f1-32be-b320-1b49dbcb7f30 | -5.52819 | -43.78836 | 2025-09-07 04:17:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 96fe2af0-7fb5-373c-9823-5cb05b8441bd | -5.45186 | -42.81128 | 2025-09-07 04:17:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 75f9b7f9-8fb4-3d30-86ac-7f2682c533b9 | -3.62626 | -49.19421 | 2025-09-07 04:17:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e1c5eee8-121d-3304-b419-8eb30d6aa128 | -5.55877 | -43.06855 | 2025-09-07 04:17:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Caatinga | 2.7 |
| a0de04e2-a315-30a4-b257-bbb0174b47e2 | -5.75914 | -43.13254 | 2025-09-07 04:17:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 3.2 |
| d7576b9e-7502-3496-83e6-cb8797c49f9f | -5.7361 | -43.91386 | 2025-09-07 04:17:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 54b84206-60fe-3c99-b430-a39b613abdcd | -4.67636 | -41.01993 | 2025-09-07 04:17:00 | NOAA-20 | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 40f4ef3d-ced7-3a43-a1c2-4c6a9ef282df | -5.44111 | -42.81334 | 2025-09-07 04:17:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| f57c6af1-e3fc-3622-8fb0-f2ea40614ee0 | -5.63502 | -42.62057 | 2025-09-07 04:17:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 0ac7290f-4437-3743-971a-feaa8401571f | -2.2611 | -47.85204 | 2025-09-07 04:17:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ac543663-43eb-33d3-90c0-b98a5a62fbc3 | -2.81662 | -49.19728 | 2025-09-07 04:17:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 56e44e3c-cc85-3cd4-97e3-8c57cea81d91 | -5.30811 | -42.78627 | 2025-09-07 04:17:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| faddd32f-8fd7-39c6-abf5-624d489b384d | -5.76784 | -42.34861 | 2025-09-07 04:17:00 | NOAA-20 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 2f5bb378-9adc-3fcb-b30e-61cd7f38962f | -2.43244 | -49.31297 | 2025-09-07 04:17:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e4cbeb8a-f962-36b6-84a9-05e5234e5024 | -2.91468 | -48.67349 | 2025-09-07 04:17:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6c3d513b-4a3f-351d-a44d-5ec5f791c994 | -3.82008 | -54.12605 | 2025-09-07 04:17:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bdc7d694-2a30-30b0-bb4f-8cf12a99fb43 | -4.75147 | -42.6048 | 2025-09-07 04:17:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 77f17c2c-128a-33e2-aee5-0ff153720320 | -5.21256 | -43.69991 | 2025-09-07 04:17:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 7bdc90c1-f3f1-303d-93aa-ea3549b75018 | -3.96671 | -43.24119 | 2025-09-07 04:17:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d5b43508-76bc-3930-b0dc-d0e2f82796c2 | -2.82133 | -49.19426 | 2025-09-07 04:17:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 808610dc-2901-34b5-8a9b-b6994c997199 | -5.75437 | -43.70929 | 2025-09-07 04:17:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a55d6cf0-6eb6-31cf-8903-ecdc67bc067c | -3.82365 | -54.12304 | 2025-09-07 04:17:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7a3c2d11-5f15-3d02-9617-1e8b44df04f3 | -5.45525 | -42.81181 | 2025-09-07 04:17:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 5b7d5d86-1f4b-3d43-b3f7-6260fe79be7b | -5.3774 | -45.97087 | 2025-09-07 04:17:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4f0d02c7-6515-31f2-a4de-95fe9f18c7d4 | -4.68063 | -41.0163 | 2025-09-07 04:17:00 | NOAA-20 | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| fb540ac3-c62c-314e-aa8b-54079c206f09 | -4.17497 | -42.02816 | 2025-09-07 04:17:00 | NOAA-20 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| ef48c84e-4a58-3691-80f9-800f250bec2c | -2.82013 | -49.2016 | 2025-09-07 04:17:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 66fd85b8-30ea-34b7-9f6c-a7d73b453a41 | -5.21752 | -43.68995 | 2025-09-07 04:17:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c82eab00-10a3-3541-8655-49c4ff0b8137 | -5.4988 | -42.66452 | 2025-09-07 04:17:00 | NOAA-20 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 4be00104-1a98-3672-8c76-3de9fcaf996d | -5.43957 | -42.81746 | 2025-09-07 04:17:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 86996949-c816-38b6-a4d1-a696d65ff432 | -5.37574 | -45.95953 | 2025-09-07 04:17:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 239731ee-530a-31d8-91c5-cbf34ccc8a4b | -5.86875 | -43.23788 | 2025-09-07 04:17:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ac90ac9d-c227-363c-ad35-fc7c04c3c406 | -3.48448 | -43.33072 | 2025-09-07 04:17:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2c858edf-5635-3683-9973-a01f368bbb70 | -4.23544 | -48.60811 | 2025-09-07 04:17:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 604851bb-a00e-36d7-8aee-02d7f587e1eb | -5.30924 | -42.80134 | 2025-09-07 04:17:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ee9aedbe-1197-3f35-9c9d-2ff4ff773565 | -3.24283 | -50.80327 | 2025-09-07 04:17:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e8b427fc-13f3-3cc2-977a-96596da7df0e | -2.89341 | -40.24276 | 2025-09-07 04:17:00 | NOAA-20 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 39933e81-4ee0-306d-a5d3-9bfb0c5c4570 | -3.319 | -48.70598 | 2025-09-07 04:17:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4bfd316f-2813-355f-ba76-3c0572686d55 | -5.37568 | -45.98171 | 2025-09-07 04:17:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b45ce065-1d4d-34ae-95f4-aeb803adf387 | -3.58653 | -47.51196 | 2025-09-07 04:17:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 8c4093fd-8b82-3d84-a002-e568ca13e6aa | -5.04091 | -45.45309 | 2025-09-07 04:17:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e8e6223e-e27a-3f32-aa50-96511ee2b454 | -5.86112 | -42.42434 | 2025-09-07 04:17:00 | NOAA-20 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 5efdaefb-7086-3742-8e4b-490142d0173c | -3.5009 | -42.33343 | 2025-09-07 04:17:00 | NOAA-20 | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 53d1dc36-fb0d-3329-81f1-41f01d6fb0e2 | -2.85236 | -49.50326 | 2025-09-07 04:17:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d58b4821-d474-3816-9a49-240b32011786 | -2.78986 | -49.62412 | 2025-09-07 04:17:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0ff6d1b0-9d6e-38ac-ad09-02693038979f | -5.55314 | -43.06029 | 2025-09-07 04:17:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a9a8e372-63db-364f-9c08-4b6e95f888bc | -2.77833 | -41.79766 | 2025-09-07 04:17:00 | NOAA-20 | ILHA GRANDE | PIAUÍ | Brasil | 2204659 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0773ae73-dcd8-3a41-a6ad-39481f064d20 | -2.82067 | -41.86539 | 2025-09-07 04:17:00 | NOAA-20 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| efbd92f9-a928-3c07-a058-ef21b02a4142 | -5.42213 | -42.68351 | 2025-09-07 04:17:00 | NOAA-20 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 84bafc8b-839c-3ab8-917f-7957fdda73dc | -5.37683 | -45.97448 | 2025-09-07 04:17:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| add312db-6bee-31a1-a976-36d5c81bc7cc | -5.1998 | -43.69434 | 2025-09-07 04:17:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1826e2fe-ff59-33db-8407-51a6d04c1724 | -3.11575 | -43.27692 | 2025-09-07 04:17:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bbb20ad7-da57-3aaa-918b-b6a86d81c059 | -3.59318 | -47.51743 | 2025-09-07 04:17:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 77b59798-e1d0-396c-9c77-ae63683e68ca | -2.84756 | -49.50642 | 2025-09-07 04:17:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4ef562ad-2d4a-31f8-b9cf-da3e4f96bb1c | -5.13066 | -44.76043 | 2025-09-07 04:17:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0d8ac110-1b05-3e62-88a5-a74ed5cd42d0 | -2.84695 | -49.51023 | 2025-09-07 04:17:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3fa8b30b-d42f-3195-88e4-6227aac7ad6c | -3.81806 | -54.1218 | 2025-09-07 04:17:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e87e57f0-cb46-32e5-9667-f3c411228459 | -5.48045 | -45.59566 | 2025-09-07 04:17:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d0a435ff-5ca5-3fd0-b84b-0cb608b65313 | -4.27178 | -48.65378 | 2025-09-07 04:17:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 83f3730a-23ef-349b-a2cb-0152e5ed27a2 | -5.44444 | -42.58485 | 2025-09-07 04:17:00 | NOAA-20 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 74b94a53-3ad8-3495-8f92-6644f51a8447 | -1.93537 | -56.59473 | 2025-09-07 04:17:00 | NOAA-20 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 07f76d35-821c-3934-8992-43a8c5f1d2fd | -4.57286 | -46.39884 | 2025-09-07 04:17:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6c91c75f-54d6-3509-b57f-4bafc3fb5574 | -5.28148 | -42.66591 | 2025-09-07 04:17:00 | NOAA-20 | DEMERVAL LOBÃO | PIAUÍ | Brasil | 2203305 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 16c6451d-3410-3d58-ba4a-13fb3ca3735a | -5.55364 | -43.778 | 2025-09-07 04:17:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 78115fb2-0fba-3edc-a757-a0e3f6252e78 | -3.5925 | -47.52172 | 2025-09-07 04:17:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| c0eced6e-7034-3e2d-b1a7-9ac96f14495b | -5.31264 | -42.80186 | 2025-09-07 04:17:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README40.md)

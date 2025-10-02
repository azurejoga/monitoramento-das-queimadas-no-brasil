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

## Dados Diários - Página 108

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 28c90716-4d25-348e-9432-9d187dd77d59 | -8.89749 | -46.62263 | 2025-10-02 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| ae318e21-f91d-36d1-a48d-1fa897964e33 | -3.40461 | -46.90263 | 2025-10-02 04:49:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ff3af84d-6707-3521-abfc-1c950b8ed6b2 | -6.11423 | -41.79695 | 2025-10-02 04:49:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 7209f663-024b-33a6-b094-bbdd2a3daafe | -8.74649 | -47.3385 | 2025-10-02 04:49:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| d5f41f62-5e35-31bd-919d-f36647b3973c | -7.55281 | -42.40626 | 2025-10-02 04:49:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b2900543-a7be-305b-bf20-7ae3e2febec4 | -2.87425 | -52.77485 | 2025-10-02 04:49:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| b6fbdd3a-2dcf-3153-a94d-97b6e44d6ea5 | -8.81253 | -46.68745 | 2025-10-02 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 20ed1fd6-24f9-3fc4-80d2-b7e544a65283 | -5.63548 | -45.96009 | 2025-10-02 04:49:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4d6b45fd-50ab-3f78-aa9e-e21ef34e65e5 | -6.25973 | -43.89188 | 2025-10-02 04:49:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5fda3953-37b2-3629-a387-d8768f7627bc | -5.63868 | -45.96698 | 2025-10-02 04:49:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| adc3f4d3-c2a4-3cb6-b4bf-9bb8f624bb59 | -6.04626 | -42.67695 | 2025-10-02 04:49:00 | NOAA-20 | SÃO GONÇALO DO PIAUÍ | PIAUÍ | Brasil | 2209807 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| df89a670-13dd-3553-81bc-4379359e0491 | -3.4977 | -52.46514 | 2025-10-02 04:49:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6880b021-4343-3153-a178-728ce6f0154d | -8.74229 | -47.33783 | 2025-10-02 04:49:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 47ab4c94-7d80-3a5a-a14b-e06803c4b356 | -4.46037 | -50.68645 | 2025-10-02 04:49:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 77420d16-41e0-3b47-9a1b-054348373ea7 | -8.90155 | -45.04068 | 2025-10-02 04:49:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 36069fb6-8814-3582-870e-74631f64c88f | -6.72779 | -44.14715 | 2025-10-02 04:49:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 97b9afe5-6649-3b84-a44f-48fd3ba73770 | -7.30372 | -42.88944 | 2025-10-02 04:49:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f7a386ef-0604-3566-9589-c0bb34407a37 | -4.39642 | -49.77267 | 2025-10-02 04:49:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 400cef4a-1769-368d-bdfb-ca2060a433a6 | -6.96481 | -45.35962 | 2025-10-02 04:49:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ffd2ca38-2132-3139-ad73-8b1d54277a7c | -6.27582 | -44.05362 | 2025-10-02 04:49:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 64c7a68d-96d0-3e2a-a5dc-b7a2e84e0750 | -6.77485 | -45.5786 | 2025-10-02 04:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7c0c6714-23d6-349a-a35a-e25280fe7fb9 | -9.04205 | -46.68246 | 2025-10-02 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 40f7e59c-72f3-3cd5-ac6b-693f3ae42b7b | -6.96221 | -45.34419 | 2025-10-02 04:49:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5f6843d1-cc9f-31a5-9309-920968e4ea19 | -6.33263 | -43.04241 | 2025-10-02 04:49:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e6f39f7b-e114-3e09-a75d-0013c898cb3e | -4.58615 | -50.28674 | 2025-10-02 04:49:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4dffbb7f-a42b-384c-a90f-5cf726e65fce | -6.77412 | -45.58015 | 2025-10-02 04:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 90d20cd7-4eb9-32e7-acd0-9f5270d849c2 | -8.57787 | -49.60599 | 2025-10-02 04:49:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e7e04348-601a-341a-96c5-cf1a583d65dd | -6.82441 | -47.97774 | 2025-10-02 04:49:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9e406a99-712b-34fe-a764-f1d3bc81430a | -7.77786 | -42.53632 | 2025-10-02 04:49:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 809a0507-4d5c-32a1-996a-28119a8e9764 | -6.25612 | -49.86882 | 2025-10-02 04:49:00 | NOAA-20 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fb6724a6-89ce-3d54-8abf-a6bf31532d7c | -7.03355 | -43.34209 | 2025-10-02 04:49:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 5212ab67-d7a8-3161-8b63-7672b11e57f2 | -8.85641 | -47.66424 | 2025-10-02 04:49:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d1c98e13-b84a-3e17-b820-218a84de11da | -7.77266 | -42.53135 | 2025-10-02 04:49:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 5ffca38f-2da6-3e83-83a3-7dda17b83960 | -3.49576 | -50.27069 | 2025-10-02 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 9a53fc55-527a-37b0-aadc-9d7ff094a47c | -3.34202 | -43.1947 | 2025-10-02 04:49:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e00eb4ff-e733-3de3-a781-d46fa1935910 | -5.63925 | -45.96499 | 2025-10-02 04:49:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 71c09f20-9f0d-3359-80a7-bdd39d5bfe6b | -5.69608 | -42.68866 | 2025-10-02 04:49:00 | NOAA-20 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| af2b5ec4-ee2e-379c-8ec2-cc61e623df51 | -1.57707 | -47.30927 | 2025-10-02 04:49:00 | NOAA-20 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e7dc7bdf-c476-36f7-ac30-db205d0707d1 | -5.62587 | -51.93824 | 2025-10-02 04:49:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c6068b86-99cf-3128-b143-31cda390cd31 | -3.45635 | -50.09337 | 2025-10-02 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3ff662da-03f7-35be-ba51-ea0b289ee3c2 | -8.9082 | -46.06724 | 2025-10-02 04:49:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0a5f0886-2a3d-37e2-91a5-e94ce44c495b | -5.4611 | -42.84135 | 2025-10-02 04:49:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 4eb2b4af-8ac4-3012-8f9f-02443f551ab4 | -7.77842 | -42.5321 | 2025-10-02 04:49:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 4d524ef6-7797-3ef6-aae8-22b9bb726389 | -8.57215 | -48.64468 | 2025-10-02 04:49:00 | NOAA-20 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d7ec7c7f-5a64-3e32-92ff-1a7b6bcdddfa | -3.87911 | -42.51754 | 2025-10-02 04:49:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 55d8dddf-ea8f-33eb-bfda-4610a7028f40 | -9.33418 | -45.70774 | 2025-10-02 04:49:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 1fa6beb3-293b-301f-b471-99d1bbf62a94 | -8.88029 | -46.59119 | 2025-10-02 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 814cf829-52a7-33e0-9c19-cb0db6b4c94a | -8.88411 | -46.5961 | 2025-10-02 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 19369688-2347-3b39-b360-9e3bfe828d91 | -6.46915 | -44.20366 | 2025-10-02 04:49:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c72a36e5-31f9-3d77-8886-e75ef0185689 | -6.38275 | -43.86899 | 2025-10-02 04:49:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 4cb89cf0-1d5f-303f-9bb1-df5a38ab12f1 | -8.82298 | -44.78886 | 2025-10-02 04:49:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 48944516-32b8-3438-8540-d296b7abda4e | -7.54952 | -42.6497 | 2025-10-02 04:49:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1a1da526-7d18-3416-826e-0464e8b62284 | -9.33545 | -45.69815 | 2025-10-02 04:49:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 958eb8e2-e52b-33f0-b49b-123b8c7efe94 | -6.66469 | -42.79639 | 2025-10-02 04:49:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 32099e09-718e-3fd2-ba3b-4c45f6e02aa8 | -1.57636 | -47.31391 | 2025-10-02 04:49:00 | NOAA-20 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 22cd3cda-ab98-31d1-b86a-93f01bbb7aaf | -3.34812 | -43.1893 | 2025-10-02 04:49:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2252c220-b51f-3cec-99ea-62e0e898b70f | -8.7135 | -47.14381 | 2025-10-02 04:49:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 128f7813-a688-36e2-9ce7-a56233e4c435 | -5.46061 | -42.84485 | 2025-10-02 04:49:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 60ce8825-2b14-3443-a65c-8478711c9f16 | -6.78604 | -44.89698 | 2025-10-02 04:49:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d6b379ce-a9f9-3350-bc18-ec5dd14c0219 | -2.92287 | -48.3042 | 2025-10-02 04:49:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 433da8b6-acb1-3f79-a927-0709c4263cfb | -2.49139 | -52.14717 | 2025-10-02 04:49:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4743212a-dbb3-39b9-8935-b84fcffdcf39 | -5.69512 | -42.69558 | 2025-10-02 04:49:00 | NOAA-20 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 18c79169-695f-3a5c-81a9-8234d028b73d | -8.70337 | -47.86669 | 2025-10-02 04:49:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5908c45f-c3a0-3d52-87bf-c5dda04eda5f | -5.46012 | -42.84835 | 2025-10-02 04:49:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2c8ff26c-fee7-3a90-b06b-e5c2aea03195 | -3.35281 | -43.19316 | 2025-10-02 04:49:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 8d4b87a4-42a1-3784-b029-a4eac906a008 | -3.80425 | -51.31907 | 2025-10-02 04:49:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3faf16eb-0b10-3f63-893c-b07e811f28eb | -6.96571 | -45.3196 | 2025-10-02 04:49:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d982e3a7-1c63-3c4c-a9ba-55837b524a49 | -8.66073 | -47.09246 | 2025-10-02 04:49:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e0c9f4f1-b914-35d4-8196-77ef19f93a89 | -7.55626 | -42.64275 | 2025-10-02 04:49:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 98aabe6b-236b-3341-b7ce-d6929861e6d5 | -8.90481 | -46.66761 | 2025-10-02 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4ea73add-fb52-3040-a7c8-6ee954ab67fc | -8.16445 | -46.26187 | 2025-10-02 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 728079e2-048a-327e-8dcf-a3805e0003dc | -7.67431 | -44.8627 | 2025-10-02 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 58b3ecc2-f767-3cde-b853-012964deeca4 | -2.96276 | -48.59855 | 2025-10-02 04:49:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 029e229e-dafb-3a31-bc26-5febeaf986b7 | -8.70332 | -47.86699 | 2025-10-02 04:49:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7d5eb958-c106-3839-9746-06aa0d45439f | -6.68934 | -42.82321 | 2025-10-02 04:49:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 003f3234-736d-320b-91fd-6db245e1400d | -8.5785 | -49.60168 | 2025-10-02 04:49:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| eafd1e63-f8f8-373a-9151-f7031af1923c | -8.89808 | -46.61835 | 2025-10-02 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 71d951c4-4823-337c-9a28-04b95b34b4a1 | -8.87586 | -46.59054 | 2025-10-02 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 34678e4a-1007-34ea-8e33-d48148b1c762 | -3.29747 | -50.01363 | 2025-10-02 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 41537ac4-2862-3404-95d3-08d81bbea362 | -3.46713 | -50.09128 | 2025-10-02 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7128cb9c-6ef1-33a0-b6fb-d5de93d960f8 | -3.82533 | -51.35781 | 2025-10-02 04:49:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 04ff5716-f010-3fe5-8787-5cd21764f136 | -6.16526 | -47.2692 | 2025-10-02 04:49:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1a56e35e-a2b5-300a-9ee7-3e3fd68e40bb | -8.8948 | -46.60928 | 2025-10-02 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 464fb68e-7e3a-358f-9da2-6ce680e16793 | -7.60318 | -45.40612 | 2025-10-02 04:49:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5b33977f-8ef7-368e-b6ca-2ec14f69d8cb | -6.74689 | -50.92375 | 2025-10-02 04:49:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ce59d777-185c-3460-ada7-93a77c44ea43 | -8.45841 | -50.07582 | 2025-10-02 04:49:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c830a491-d6ef-3782-bb28-345dde398bdd | -5.41313 | -41.32444 | 2025-10-02 04:49:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 32d52f1d-c79b-3c2f-9410-6f3bfb6dc95d | -4.26503 | -48.55036 | 2025-10-02 04:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 08736aca-368a-374a-a6fa-22a02fb49651 | -7.79431 | -42.50116 | 2025-10-02 04:49:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| c12ef9c2-db65-3db4-8dbc-2fbce6963ecb | -5.40435 | -41.34305 | 2025-10-02 04:49:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a71024d8-c382-387d-b3f8-5429883067d3 | -4.26069 | -48.55411 | 2025-10-02 04:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 635915d4-59f2-3f7f-b39b-e4d5b09259ef | -6.96976 | -45.32491 | 2025-10-02 04:49:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1bef6dad-887d-3d4f-965e-2f5a1d384930 | -5.96385 | -45.71312 | 2025-10-02 04:49:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 06a4d97c-1cfa-3544-8792-cb02781cc12b | -3.34718 | -43.19547 | 2025-10-02 04:49:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| b1dfc9db-fb63-33e5-b993-fe109bf18ec5 | -7.56547 | -42.39969 | 2025-10-02 04:49:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c7211360-07d9-3d3e-ad92-6d15d4da5e1d | -7.7653 | -42.54263 | 2025-10-02 04:49:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 41fe99c2-f37c-31b6-bd09-1eb4b65e3b3d | -8.88716 | -46.59904 | 2025-10-02 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9c4a233c-da47-302a-9bc5-f2287fc33d6d | -7.58996 | -46.79652 | 2025-10-02 04:49:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b6bcf8a7-86df-3732-9fa2-8b6ceeedfb54 | -3.33661 | -50.09821 | 2025-10-02 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 38350243-5b77-3e98-a896-0785b6224a2d | -3.35434 | -43.19407 | 2025-10-02 04:49:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |


[Clique aqui para ver as próximas entradas](README109.md)

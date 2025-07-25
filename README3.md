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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e9995e24-d3a1-3035-8a4f-126a497f4767 | -9.23217 | -47.54981 | 2025-07-25 00:48:00 | TERRA_M-M | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 937e41d2-48ff-3755-84e1-b663ff603ebf | -7.8855 | -45.56336 | 2025-07-25 00:48:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 4ea1225b-3e3d-3f39-907b-461aa604f761 | -8.0952 | -43.14189 | 2025-07-25 00:48:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 71.0 |
| a897f529-6df7-3fab-8c01-2b07f52bf5f4 | -3.74724 | -49.04454 | 2025-07-25 00:48:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 19.5 |
| e2530a2b-bfa4-3681-b438-e11d051d0149 | -9.25666 | -50.22905 | 2025-07-25 00:48:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 394e9a72-a82e-3087-ad5f-e8ab35699ebd | -4.29246 | -48.06591 | 2025-07-25 00:48:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| bfa1446b-7f4e-38a5-ab84-82fd56b60dd7 | -7.25856 | -43.0725 | 2025-07-25 00:48:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 241.1 |
| fda1eb02-9e21-3e9e-8751-4ab8f383af4b | -9.0743 | -46.63276 | 2025-07-25 00:48:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| d159adfb-d566-34ab-80c6-72becb664051 | -6.22573 | -44.5278 | 2025-07-25 00:48:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 15acb81a-689e-3316-8239-d99b8b50659a | -7.48569 | -49.22968 | 2025-07-25 00:48:00 | TERRA_M-M | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 5c770c7a-93a3-3961-af0b-ea54e58eb963 | -8.89192 | -45.58623 | 2025-07-25 00:48:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 3d1bea02-bd9b-3b5d-aea5-caeab8eeeb49 | -2.38698 | -47.62703 | 2025-07-25 00:48:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 696ca16e-a5bb-3900-98c2-c3bbf274e6be | -4.2907 | -48.05394 | 2025-07-25 00:48:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 0f166d7a-fc38-3578-a2fa-43e9dda7a8cc | -6.49006 | -50.27218 | 2025-07-25 00:48:00 | TERRA_M-M | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 5de763f6-f99b-3ba9-b919-a331d3fb5995 | -8.07095 | -43.17093 | 2025-07-25 00:48:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 44.1 |
| 449ff8f1-b62a-3461-a21a-c29c911d601d | -8.84625 | -45.59371 | 2025-07-25 00:48:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 64dbe5b8-245c-380f-a95b-9e53f5a8b5c4 | -4.10954 | -47.93067 | 2025-07-25 00:48:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| e7d39731-3a52-33eb-9dee-85fcd5da9f83 | -8.84855 | -45.60872 | 2025-07-25 00:48:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 1bffa1da-c65b-3b48-944b-6dba677fff20 | -3.57023 | -49.50438 | 2025-07-25 00:48:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 29251b9d-5423-3605-9d25-dd3c4ba624a1 | -4.99901 | -56.29387 | 2025-07-25 00:48:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| f734ac95-ca1a-3e9a-875e-df2f2a1f600e | -7.14903 | -46.08574 | 2025-07-25 00:48:00 | TERRA_M-M | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| f1a3f227-3350-3909-b7f3-ec236e23f91b | -8.89184 | -45.59602 | 2025-07-25 00:48:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 583b029d-6507-3bda-b2ff-edb58ef0bbd4 | -8.50523 | -43.32267 | 2025-07-25 00:48:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 72.9 |
| db30f392-bb9f-31ec-928a-d59d27558667 | -4.83754 | -45.31138 | 2025-07-25 00:48:00 | TERRA_M-M | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 35.5 |
| 0fed1fde-791d-3752-a345-bc56c751a3e8 | -7.88297 | -45.54705 | 2025-07-25 00:48:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 068e6c26-c5c1-32d3-b422-076103801dae | -7.46425 | -49.40778 | 2025-07-25 00:48:00 | TERRA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 60396bf9-7257-3378-91cc-305f96a4176e | -8.06298 | -43.15339 | 2025-07-25 00:48:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 35.2 |
| b60d671a-dd3a-3e84-ace7-8b13acc9f43e | -7.50167 | -49.22099 | 2025-07-25 00:48:00 | TERRA_M-M | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 616ca819-b7ce-3eeb-9171-ef2a72a0a03e | -7.88042 | -45.53067 | 2025-07-25 00:48:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 49422356-3f8a-351d-aece-eabb3309c0d1 | -8.12024 | -50.47252 | 2025-07-25 00:48:00 | TERRA_M-M | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| a1916a5f-b536-3496-9bd3-2157154d89e1 | -3.05017 | -47.37447 | 2025-07-25 00:48:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 0e626b6c-4827-3201-b5f9-aed5b266c54a | -8.51902 | -43.32037 | 2025-07-25 00:48:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 17.0 |
| 78648fe0-b4d5-35fa-9ba1-f8f06da7ec16 | -8.32965 | -46.28881 | 2025-07-25 00:48:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 5efea011-5f0e-3e18-a13a-ac51212a6ddc | -8.93591 | -47.34554 | 2025-07-25 00:48:00 | TERRA_M-M | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 358a3fda-6677-33d3-8939-41c0d351925e | -3.17063 | -49.45742 | 2025-07-25 00:48:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| e7647a5c-7f5e-3075-9de4-f6fea2ce87af | -7.91375 | -44.07809 | 2025-07-25 00:48:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 84.8 |
| d498645f-7533-38fc-92c9-ede53b01ce09 | -6.57503 | -49.5022 | 2025-07-25 00:48:00 | TERRA_M-M | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| fcf78db2-011a-3597-820e-d6dc8922dfcb | -5.66511 | -51.36415 | 2025-07-25 00:48:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 440cfdf5-2deb-3328-9f65-c7f6bf8c44e1 | -7.25441 | -43.04628 | 2025-07-25 00:48:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 31.0 |
| ebd01421-71bd-35ff-ba93-3f22cb44dd42 | -8.89417 | -45.60132 | 2025-07-25 00:48:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 1ed78681-cc52-3b33-8555-c3d6e5fd3aef | -7.85636 | -48.22382 | 2025-07-25 00:48:00 | TERRA_M-M | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 40cad1d5-bbeb-36d3-b4dc-015448c275b2 | -5.89904 | -49.34837 | 2025-07-25 00:48:00 | TERRA_M-M | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| ca2db90d-dec8-33ae-8bfe-82936fb8a98d | -2.90778 | -48.24083 | 2025-07-25 00:48:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 33.7 |
| 5c73ed34-f1c3-3894-aa63-09ac927ac3fc | -7.46291 | -49.39831 | 2025-07-25 00:48:00 | TERRA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 07b0b470-355d-3500-96bf-eadf6fd46519 | -8.13525 | -49.59066 | 2025-07-25 00:48:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| e25a51b5-6cb0-3d6f-a342-6c0b19616f2d | -10.04573 | -59.10247 | 2025-07-25 00:48:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 33.1 |
| 685350d7-5880-38d5-917a-149629134060 | -4.7738 | -45.32677 | 2025-07-25 00:48:00 | TERRA_M-M | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 0080b24c-8e98-341d-9319-124abd3e3a1c | -4.35186 | -47.69782 | 2025-07-25 00:48:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 30.5 |
| 328a14c7-daab-3285-9eb4-bc0dce51e150 | -4.04542 | -42.51546 | 2025-07-25 00:48:00 | TERRA_M-M | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 21.0 |
| f130c579-765b-38db-877c-595358a53cfb | -4.77657 | -45.34551 | 2025-07-25 00:48:00 | TERRA_M-M | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 30.3 |
| 0f3fa282-a41c-3d36-a017-30dce304b10f | -10.04935 | -59.10842 | 2025-07-25 00:48:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 35.1 |
| ba8eca9d-c7f5-38ef-87f4-3aa054041205 | -7.11675 | -47.85098 | 2025-07-25 00:48:00 | TERRA_M-M | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| ece25dcb-be59-35e3-95cd-a2ec2a8a7277 | -7.8579 | -48.23447 | 2025-07-25 00:48:00 | TERRA_M-M | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| a62c8cb4-9039-363c-9888-459dc1f30c4d | -8.37026 | -51.07742 | 2025-07-25 00:48:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 26.0 |
| 10669346-e8b6-3e4e-a3ae-9d84605f1b6e | -9.23381 | -47.56098 | 2025-07-25 00:48:00 | TERRA_M-M | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| e815e644-5983-3fe3-bc59-f3c658bd089d | -4.67294 | -48.87128 | 2025-07-25 00:48:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 72ad9fe8-4c12-30c9-82d1-b0cd7619f98c | -3.31199 | -51.66629 | 2025-07-25 00:48:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| f1b6c9b2-2d07-3663-8203-dc4b409eaa73 | -3.18012 | -49.45604 | 2025-07-25 00:48:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 8f1659c3-228c-3148-b969-56fe235ff8a7 | -6.48879 | -50.26314 | 2025-07-25 00:48:00 | TERRA_M-M | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 2cad5134-d720-382f-9467-46dfcd30a259 | -7.19895 | -45.32816 | 2025-07-25 00:48:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 2e77ffb6-9276-38ee-a731-d7082c65d5a6 | -8.119 | -50.46359 | 2025-07-25 00:48:00 | TERRA_M-M | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 730460b8-6cba-345e-8b20-0b1bbdd97b5f | -2.9181 | -48.23937 | 2025-07-25 00:48:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 80022eb6-2013-3ed6-ae6e-6acee4679f25 | -6.95297 | -44.55769 | 2025-07-25 00:48:00 | TERRA_M-M | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 138.2 |
| d8dbb980-5c29-3079-9e31-1a04a2874c76 | -7.86598 | -48.22245 | 2025-07-25 00:48:00 | TERRA_M-M | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 6e45c7d0-0947-394f-ac4b-c9d1fe9633d2 | -9.04632 | -46.62963 | 2025-07-25 00:48:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| fe80f4f2-e41c-3ce1-9067-12f4c3fdad54 | -8.12996 | -50.46512 | 2025-07-25 00:48:00 | TERRA_M-M | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 2aafde65-16ea-35c9-bf54-98fb78f91bcb | -6.62773 | -49.74439 | 2025-07-25 00:48:00 | TERRA_M-M | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 17.6 |
| b2d9510c-a545-3ac8-b2ed-33602a2b756f | -8.08506 | -43.16886 | 2025-07-25 00:48:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 136.4 |
| 410e07de-5247-30d2-addf-b8a187e55b0f | -3.32278 | -48.71812 | 2025-07-25 00:48:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 412b39e4-a2da-3810-b4d4-839940b705ca | -3.12461 | -47.01239 | 2025-07-25 00:48:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 4b344194-079d-3dbe-bc2d-b760b71258ab | -7.15134 | -46.10093 | 2025-07-25 00:48:00 | TERRA_M-M | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 666146c4-4898-3bb6-8ef7-44de64dbe6db | -8.08109 | -43.14418 | 2025-07-25 00:48:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 170.2 |
| b162cf8f-64fa-364c-bec2-6bdc2edd4fe9 | -9.13364 | -49.67687 | 2025-07-25 00:48:00 | TERRA_M-M | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 89c05878-912e-3c6f-a75a-a3ce925f4c33 | -3.05215 | -47.38831 | 2025-07-25 00:48:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 22.9 |
| 7fe2aaef-fc7f-3447-9ab7-6ce792cd49aa | -9.0513 | -46.62305 | 2025-07-25 00:48:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 22.8 |
| a40d530b-e443-3d44-9853-1f6cc087f946 | -8.33176 | -46.30299 | 2025-07-25 00:48:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 30cb6d1d-4a43-3272-a688-607cf7eb5a99 | -7.9171 | -44.08343 | 2025-07-25 00:48:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 104.5 |
| f632d2e8-0b78-3426-bdc6-9f7627876c97 | -8.0883 | -43.1667 | 2025-07-25 00:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 125.7 |
| 0b806265-0b53-3928-a578-4fe3e327ce31 | -11.458 | -45.1357 | 2025-07-25 00:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 118.2 |
| 4c5f2986-006e-3ec8-86b9-c8276d8c2e69 | -8.0886 | -43.1431 | 2025-07-25 00:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 206.3 |
| 21fe6ee8-0ce2-3b2f-bb67-1c6c4904391c | -11.9329 | -58.7588 | 2025-07-25 00:50:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 60.6 |
| b0a2cde1-3e2d-3218-a373-4f925143a0da | -11.9518 | -58.7574 | 2025-07-25 00:50:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 122.7 |
| fc8b5797-3661-3b23-9785-a0758afc6336 | -7.9259 | -44.0706 | 2025-07-25 00:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 159b7a36-7c41-3df2-a9a0-86e1e55f87e3 | -7.9256 | -44.0937 | 2025-07-25 00:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 3dd6da22-085d-3c7b-9f5c-fa448ef696e3 | -10.6438 | -44.7645 | 2025-07-25 00:50:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 27c62e92-4c96-34db-a979-c37de2685b2c | -7.8894 | -45.539 | 2025-07-25 00:50:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 37.4 |
| 750abeb3-5ba5-3ec5-a1e0-1148cdaeb0bb | -6.9607 | -44.5775 | 2025-07-25 00:50:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 389de368-72af-3421-98ea-5b04cd92ba79 | -7.2597 | -43.0645 | 2025-07-25 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 162.4 |
| 071fa322-7d26-3fe5-a167-c91a2e6af7e7 | -2.9108 | -48.254 | 2025-07-25 00:50:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 72.1 |
| e1afdffc-5cc6-32c0-8d80-8c624116a74b | -6.9422 | -44.5562 | 2025-07-25 00:50:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 103.4 |
| bdd423e9-1641-3655-9f18-c3a19176c917 | -7.9068 | -44.0957 | 2025-07-25 00:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 65.0 |
| cfc04f97-72da-3c7d-bdce-6157fcf61d4b | -8.0696 | -43.1452 | 2025-07-25 00:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 93.7 |
| 24ae3f51-d1af-3e39-9e5a-ffcbadb56b62 | -6.961 | -44.5546 | 2025-07-25 00:50:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 110.6 |
| fb5e1fab-5824-38e6-aaa7-45dc61821bba | -11.9516 | -58.7771 | 2025-07-25 00:50:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 57.3 |
| f7730d7c-87bd-3e6e-adcd-dfa41986aab0 | -14.9518 | -46.9845 | 2025-07-25 00:50:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 4365f1ae-fbc8-303e-b964-8973e017d310 | -7.907 | -44.0725 | 2025-07-25 00:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 3bf106ae-4aee-3a21-8cf0-62164c421242 | -13.7169 | -45.6833 | 2025-07-25 00:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 50.6 |
| 7c246903-d2e4-320a-9617-07e56a6c5a4e | -11.4584 | -45.1126 | 2025-07-25 00:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 153.0 |
| 1921114f-2244-3b47-9cf4-5dfb4b728c0a | -16.8201 | -47.6013 | 2025-07-25 00:50:00 | GOES-19 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 46.4 |
| a1c56e5e-466a-3235-9837-cf6238a0272b | -11.458 | -45.1357 | 2025-07-25 01:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 96.0 |


[Clique aqui para ver as próximas entradas](README4.md)

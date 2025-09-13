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

## Dados Diários - Página 101

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| edd934ee-27a0-3c50-b300-65863ccf7a75 | -11.08894 | -51.43401 | 2025-09-13 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 12.2 |
| b876e4c0-0573-3fc4-8fa5-53a027bf49da | -11.83304 | -50.55035 | 2025-09-13 05:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 771bd389-cf26-37d8-9010-6d81150d2645 | -7.86966 | -61.15213 | 2025-09-13 05:25:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6a162ea6-5005-37fd-a3c4-929a05e4b51d | -11.10655 | -51.43232 | 2025-09-13 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 7850b49f-ad3c-3768-b139-eea8ca50d19d | -9.51723 | -54.62635 | 2025-09-13 05:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 21.3 |
| 14c4c7bd-4659-35a9-9dd1-75cdd44940d4 | -9.48992 | -55.99295 | 2025-09-13 05:25:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b842f09c-f5e7-3263-ba6d-9ebde6b1dba1 | -11.18946 | -51.42686 | 2025-09-13 05:25:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e8704162-9c04-3574-a168-f5a46b27acf0 | -11.10656 | -51.41785 | 2025-09-13 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| af28cf17-a05f-3e76-8131-bcd6096f2cc2 | -9.27498 | -59.39538 | 2025-09-13 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1b84f46d-b868-3afd-aef0-1f557e4e10dd | -11.37422 | -47.33317 | 2025-09-13 05:25:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 7b8cd5c7-95d5-36a5-af1f-ae0344c9a793 | -10.42375 | -48.60181 | 2025-09-13 05:25:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| a56e4c83-bfb3-356f-acdb-ef856ddbcb83 | -11.8852 | -50.58049 | 2025-09-13 05:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 19b50a48-1f39-3973-9d15-479816a153f5 | -7.54437 | -52.51514 | 2025-09-13 05:25:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2183ddb9-1ff7-354f-8998-f662f184118f | -10.00525 | -59.97646 | 2025-09-13 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 32f54616-8a22-366b-9e90-4faea7332176 | -10.50797 | -51.54891 | 2025-09-13 05:25:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 949f57e9-0d60-341c-b4c1-1845a916858e | -11.08689 | -51.43534 | 2025-09-13 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 305f0bd5-cf86-3720-affc-e5364da007a6 | -10.58493 | -60.19976 | 2025-09-13 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a5431b3c-1982-38bf-9755-859aece7272a | -9.80375 | -61.51585 | 2025-09-13 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cf57a874-c257-37be-8bb1-a3c6fe1ecc06 | -7.85635 | -61.17148 | 2025-09-13 05:25:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e4a0b367-fdcd-3a79-b1e4-52b03af039b2 | -7.76163 | -61.12775 | 2025-09-13 05:25:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ad02b3ac-e3b0-30c0-8ef5-04d687dcaae3 | -11.13847 | -50.69132 | 2025-09-13 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| bdea8de5-2c96-3bf7-878e-78348ba2dedf | -9.54181 | -59.0606 | 2025-09-13 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1d87fa85-b35e-3322-bf1e-842b80c9efde | -9.02439 | -47.04634 | 2025-09-13 05:25:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9965b606-2474-3d22-9b8d-0971a27eed90 | -11.37493 | -47.33145 | 2025-09-13 05:25:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 12db87c5-9cd1-34db-9477-a9c2742a1833 | -10.33034 | -48.81924 | 2025-09-13 05:25:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| de5f16fa-205b-324c-a06d-fd4646c548f2 | -11.86801 | -50.56893 | 2025-09-13 05:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| b06f6388-599d-36f5-9511-667e2c84d84a | -11.18898 | -51.43083 | 2025-09-13 05:25:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4f711a60-3983-3805-8354-074c146ca44f | -9.83259 | -54.53295 | 2025-09-13 05:25:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2e578005-a70c-3762-9667-d59210003ec6 | -11.40705 | -50.74175 | 2025-09-13 05:25:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| ae4fe8bd-a73f-3e02-bb23-08d3ad63032d | -11.18516 | -51.41418 | 2025-09-13 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 26.8 |
| e34f2f16-f465-35b4-8f2a-d81da54b22c1 | -7.5398 | -52.51778 | 2025-09-13 05:25:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a23dad9d-3f86-39f4-b88d-9cabc9478c11 | -9.80407 | -59.10757 | 2025-09-13 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b44b0588-fa26-38d3-903b-98cf0ced16d2 | -7.90525 | -55.26643 | 2025-09-13 05:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 12b5a928-f327-3277-bf08-5bc2244298cc | -11.76645 | -51.51617 | 2025-09-13 05:25:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 55c99a19-b0a7-3f54-ad18-36fcb36b2eb6 | -11.40061 | -50.47663 | 2025-09-13 05:25:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d67103d4-f056-37bc-b969-74dd47cfc1cf | -11.79572 | -50.54669 | 2025-09-13 05:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 511a2005-867b-39ff-a466-7a92a9e05acb | -11.38898 | -50.47047 | 2025-09-13 05:25:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9cbc0e07-50e8-300b-a6dd-814cae83841e | -9.27384 | -59.40283 | 2025-09-13 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1902e630-4f5d-31f0-a024-169c78c9bcce | -11.27195 | -51.13279 | 2025-09-13 05:25:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dcfe796f-425f-3387-9e08-363eb5c76249 | -9.7406 | -65.00995 | 2025-09-13 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c7693e76-830c-3897-bc6b-9afdb52b30b3 | -9.27328 | -59.40656 | 2025-09-13 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 209961f7-5569-3e2a-aec5-8aafb5e1213d | -11.1314 | -50.69939 | 2025-09-13 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 14.0 |
| f4b827e9-1391-333a-8ccd-09028fe68fd9 | -11.09832 | -51.4368 | 2025-09-13 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 4b7f7cf3-e307-3647-8180-c5c19c5ae8f9 | -9.23699 | -51.22153 | 2025-09-13 05:25:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d5260d6d-bd48-3e0c-b844-b1dbda8ce6d3 | -11.03796 | -51.40898 | 2025-09-13 05:25:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d53ce19d-1643-3414-a8d4-f9738292cba6 | -11.01764 | -51.3377 | 2025-09-13 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8a635308-0d42-3aa6-99b9-62a294f0cafd | -11.18994 | -51.42288 | 2025-09-13 05:25:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 9e76413a-ef86-34a1-9b37-127aa8f3d37c | -9.25687 | -57.06553 | 2025-09-13 05:25:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6e14c2a7-8165-35c9-9af2-9b75e9902770 | -10.21022 | -60.04919 | 2025-09-13 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9f0d95fe-30f3-3a2c-bdcd-a36b2251bd09 | -11.87411 | -50.56971 | 2025-09-13 05:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| cf461e1b-47a7-3860-8e9c-74fef55cc24a | -11.09322 | -51.44656 | 2025-09-13 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d92b13cd-1817-39a7-9693-c0d36b1a84ce | -10.36539 | -50.50193 | 2025-09-13 05:25:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 275a5d4a-6d02-34ba-9211-2bc74865a2e7 | -9.74035 | -51.01507 | 2025-09-13 05:25:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0084b1f8-4d06-3245-91b3-fbd8ea3bb8c3 | 0.69103 | -50.65147 | 2025-09-13 05:25:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 57a1c1de-7b83-3feb-a0be-37040ca0b16d | -11.19089 | -51.41494 | 2025-09-13 05:25:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 26.8 |
| 3973f676-3082-391d-b77e-fc5da2ce3fe0 | -9.26587 | -59.4092 | 2025-09-13 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 24.1 |
| 0f9e1ac3-b5e4-3d79-947d-de68304681e8 | -10.77387 | -50.51837 | 2025-09-13 05:25:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e972edb6-f231-37c0-bcac-35f20d335319 | -9.52053 | -54.63577 | 2025-09-13 05:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 55f49ec5-383e-3e28-9308-a0549ff7dbae | -9.26473 | -59.41663 | 2025-09-13 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8ccb7f8f-4b85-376b-8230-7b777df765ce | -9.91042 | -51.89202 | 2025-09-13 05:25:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e6af70a3-3c60-3954-9636-d45a19203326 | -10.35518 | -50.50431 | 2025-09-13 05:25:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f0d6cda1-fcc7-3723-9afd-db93002a9f0c | -9.88527 | -58.33094 | 2025-09-13 05:25:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b53b8390-f3e7-31aa-834f-0924206ce295 | -11.21768 | -54.98782 | 2025-09-13 05:25:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 039dc7f0-9efe-34b3-b5ce-b6f457cda4f7 | -9.90745 | -57.06342 | 2025-09-13 05:25:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b2dc5254-09a8-30ff-9b76-9e8387c062ea | -11.86637 | -50.58283 | 2025-09-13 05:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| e5ab6dee-096e-3e9a-a404-a26aae0a2cfb | -11.5694 | -50.57115 | 2025-09-13 05:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| cd1b2303-cc26-37dc-a27b-bff8dc1dcb12 | -9.81096 | -61.51342 | 2025-09-13 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 079c721b-4f97-3519-ace0-37843d89a8ca | -9.26756 | -59.39804 | 2025-09-13 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9c59df61-09ac-3f43-901d-ffed374b4a72 | -11.86191 | -50.56816 | 2025-09-13 05:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 1d0a8bea-193b-3c0c-9824-6608935b4466 | -9.3061 | -65.59464 | 2025-09-13 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c1bb5de8-8cf5-3627-b6ab-96319a406f8a | -11.1025 | -51.44934 | 2025-09-13 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f78bbe53-fc1b-3f7a-9655-b87cd9263fa6 | -4.93108 | -55.78088 | 2025-09-13 05:25:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 72e520b6-9e99-3903-8a5b-14e308dc721c | -7.75552 | -61.12321 | 2025-09-13 05:25:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b85933d1-5c64-3141-bee4-df01faec0d22 | -10.24387 | -48.63938 | 2025-09-13 05:25:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 54e3c9dc-8f5b-3648-98f7-620f600962a6 | -10.09758 | -59.16956 | 2025-09-13 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 78450224-117f-3bfa-853e-8a2918856128 | -11.58265 | -50.56351 | 2025-09-13 05:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 16.8 |
| aa5a4a79-dca7-3651-86d1-57fa87a6e3e4 | -10.00186 | -59.97593 | 2025-09-13 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6973124a-6c04-33aa-8ccb-550ff507e24e | -10.50363 | -51.5381 | 2025-09-13 05:25:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ecfce841-07fc-313f-9f60-8d022990842b | -11.18533 | -51.40648 | 2025-09-13 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 4d7039b5-a57d-3bcc-91f3-809c7ea44bad | -11.2783 | -51.12932 | 2025-09-13 05:25:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9669fb30-c06f-35f7-ad32-32ff9813e2d0 | -3.0586 | -58.96704 | 2025-09-13 05:25:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| db97d018-3349-3ab3-8129-755038f8a294 | -9.25305 | -57.06498 | 2025-09-13 05:25:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bb1ee836-dff7-385c-b798-e6fad09534c1 | -11.10707 | -51.41391 | 2025-09-13 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e3965680-9d7b-394a-90e2-bce715fa7505 | -9.23922 | -51.24871 | 2025-09-13 05:25:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 27.8 |
| 172191e8-34cf-327e-bc32-ac056fe79943 | -10.50315 | -51.54181 | 2025-09-13 05:25:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 83984ba3-2bc0-385b-91c4-da4e9f96a723 | -11.19041 | -51.41891 | 2025-09-13 05:25:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 37de18fa-9855-378a-9be1-696c8c8e7a18 | -9.96297 | -50.39182 | 2025-09-13 05:25:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 432158f1-81c7-385c-abc4-b620b9186b15 | -10.69922 | -54.4483 | 2025-09-13 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 375b4504-5b1e-32d2-bc1c-3c885e996b8d | -11.80792 | -50.54822 | 2025-09-13 05:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| ede4f0d3-8a92-326f-ab16-e3fad0f5a21e | -11.10896 | -51.41256 | 2025-09-13 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4ce3decc-b649-3f22-87ad-39301545d6d4 | -7.86246 | -61.17604 | 2025-09-13 05:25:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 538d67a8-90d9-36d3-9acf-1a1b0fd32b4b | -9.21152 | -59.55975 | 2025-09-13 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f274c60a-9cac-330d-b019-822688d8dfb8 | -11.1791 | -51.40969 | 2025-09-13 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 25.5 |
| 90e3156b-d81d-3950-9297-c7798bbc07f3 | -9.73159 | -65.01768 | 2025-09-13 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ebb0af46-a978-3ea2-b878-0c05698da308 | -11.0879 | -51.42746 | 2025-09-13 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 54f9d40a-74d0-3f29-88b7-6c917b2d8617 | -9.26015 | -59.40069 | 2025-09-13 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 21.2 |
| a8f5bc11-0fde-3439-819f-92293a6f6f98 | -7.89688 | -61.42511 | 2025-09-13 05:25:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4ed26e94-cfb3-3fe5-9667-1c23cd95f74e | -3.38899 | -64.70416 | 2025-09-13 05:25:00 | NPP-375D | TEFÉ | AMAZONAS | Brasil | 1304203 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1fd141f9-fdc7-36f3-89ea-f92b8494e987 | -9.48845 | -55.97413 | 2025-09-13 05:25:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c913432f-5213-300e-985f-37b6e1c27046 | -10.84958 | -48.18415 | 2025-09-13 05:25:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |


[Clique aqui para ver as próximas entradas](README102.md)

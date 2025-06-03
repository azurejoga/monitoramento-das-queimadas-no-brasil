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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 06a1e2f4-fff6-3de4-a2fa-12085deca7e8 | -12.36856 | -54.16661 | 2025-06-03 03:57:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 190790fc-8f01-390e-b33d-c024ec17814d | -11.25306 | -49.49666 | 2025-06-03 03:57:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 562f2fd7-2ee8-3e38-933a-a1b8c751050b | -9.54822 | -48.69021 | 2025-06-03 03:57:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 31af3d7a-1e10-3f15-a0d4-501ee9a0104c | -10.13622 | -52.14235 | 2025-06-03 03:57:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e98a8645-bdca-3985-8fde-d4ec008de032 | -8.91496 | -48.90666 | 2025-06-03 03:57:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 02c6fe83-a3d0-3d83-a38d-7b8391b0b428 | -10.14019 | -52.13752 | 2025-06-03 03:57:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c8487b23-5074-358c-af85-5beaa5c87ad9 | -8.97142 | -47.96949 | 2025-06-03 03:57:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9eb06401-d4b4-339a-a551-5b1732cee2ec | -12.37243 | -47.32304 | 2025-06-03 03:57:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b43a8c25-11f3-3cdb-b842-9485a9952f57 | -12.3692 | -54.16811 | 2025-06-03 03:57:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9e6ff2c2-6ae0-307a-b6e5-70794b746fa5 | -11.7962 | -47.38036 | 2025-06-03 03:57:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 48b257ff-5fca-3b22-a1ee-925956f49980 | -10.36214 | -48.7331 | 2025-06-03 03:57:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 07591f96-94e5-3c77-be0c-8a83250fcd39 | -8.56422 | -48.8721 | 2025-06-03 03:57:00 | NPP-375D | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 83d70ec6-6af9-3e18-ab37-7d824ebdf545 | -9.3782 | -48.41766 | 2025-06-03 03:57:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 81333859-8cc7-308a-8afe-54a9eef3f7ab | -16.30433 | -42.75414 | 2025-06-03 03:57:00 | NPP-375D | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 598af2a2-15c0-32a6-8cb9-2e13870d25ff | -13.41696 | -43.75209 | 2025-06-03 03:57:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d1446ca6-5218-305b-b577-94be5e706d1b | -9.0302 | -46.59683 | 2025-06-03 03:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 34d55952-a497-3e88-a0ef-dfc391d44cd1 | -13.08286 | -45.27062 | 2025-06-03 03:57:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a2d9b10a-96b4-341f-99d3-2b69bf798b23 | -15.34294 | -46.95366 | 2025-06-03 03:57:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 142b9163-f393-3f40-9d54-861980fb1e71 | -15.98916 | -43.27102 | 2025-06-03 03:57:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bbcc691f-eca9-3a74-8f5c-afd07daf550a | -11.5758 | -47.45517 | 2025-06-03 03:57:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f289ed5d-6f9e-301a-bb9a-50f30c39e155 | -9.19124 | -49.6937 | 2025-06-03 03:57:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4c53be9d-fea9-3070-92ea-4bfa64ea5e22 | -12.36044 | -54.17373 | 2025-06-03 03:57:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 33e51405-ab6b-3f4e-a3ec-c30854b64236 | -9.39082 | -48.4095 | 2025-06-03 03:57:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 58faa91c-5cc5-3015-8d35-776dd6ed7225 | -10.139 | -52.14344 | 2025-06-03 03:57:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 47c25d7a-a4e5-3c85-b4b6-7f2d425ff261 | -16.68188 | -43.88539 | 2025-06-03 03:57:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9fda3124-8344-3a34-af41-f59ab1131a86 | -16.02844 | -43.6793 | 2025-06-03 03:57:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 36f24386-413b-3384-9a8b-3666bc1048d4 | -13.41617 | -43.75661 | 2025-06-03 03:57:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cf3e0bd0-b369-3896-830d-6f0caf963d6f | -20.69075 | -56.68119 | 2025-06-03 04:00:00 | NPP-375D | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0367b6bb-aaa3-33cb-b45a-caf7ec3877e9 | -18.34517 | -53.25009 | 2025-06-03 04:00:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a887b6a0-5338-33e3-86a9-9242f94eebf1 | -20.72601 | -56.62976 | 2025-06-03 04:00:00 | NPP-375D | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ed5bc6e8-a02b-3dd1-ae38-c27267c0dc2d | -20.57957 | -44.57639 | 2025-06-03 04:00:00 | NPP-375D | PASSA TEMPO | MINAS GERAIS | Brasil | 3147709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 0f0a1071-73b0-3b23-ba6f-998fdeea22b8 | -18.34404 | -53.25515 | 2025-06-03 04:00:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 475fcc5f-55c1-3ecd-8349-f457069694c5 | -20.72439 | -56.63632 | 2025-06-03 04:00:00 | NPP-375D | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 97cd6b88-e0bc-345c-8739-e6a8d254a300 | -20.7173 | -56.63465 | 2025-06-03 04:00:00 | NPP-375D | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f6fdaa71-ff95-3e5c-8860-ed4858a5a602 | -20.71895 | -56.62799 | 2025-06-03 04:00:00 | NPP-375D | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ffe1feb9-263f-3297-b7f3-aa68738d8c09 | -20.22757 | -45.71901 | 2025-06-03 04:00:00 | NPP-375D | IGUATAMA | MINAS GERAIS | Brasil | 3130309 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 44dce366-1b9a-34bd-8bf8-844a271e09dc | -21.27668 | -45.48222 | 2025-06-03 04:00:00 | NPP-375D | SANTANA DA VARGEM | MINAS GERAIS | Brasil | 3158300 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| beb5dceb-d01c-3390-90f0-47b6872fa635 | -21.34361 | -48.67167 | 2025-06-03 04:00:00 | NPP-375D | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| c0436cc8-a55f-3bcc-b738-20e28e34319b | -20.72104 | -56.6336 | 2025-06-03 04:00:00 | NPP-375D | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6ade85a2-03fd-35b2-82f8-63a2e0979df7 | -20.687 | -56.67878 | 2025-06-03 04:00:00 | NPP-375D | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2460aa80-565e-3cef-894b-c0058bb56eb7 | -20.54779 | -54.11736 | 2025-06-03 04:00:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 765093cb-6de9-308b-a7aa-4b3274c639eb | -18.86146 | -53.63402 | 2025-06-03 04:00:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3974bf70-149f-37a6-bb9d-f62508c9ddc6 | -22.39571 | -43.10844 | 2025-06-03 04:00:00 | NPP-375D | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 6677bc6c-cb0b-3e36-bc57-93826ede2dc8 | -20.71018 | -56.63315 | 2025-06-03 04:00:00 | NPP-375D | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1fbc73ef-f4c5-3431-9a98-6dd4c7b37655 | -20.72269 | -56.62709 | 2025-06-03 04:00:00 | NPP-375D | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 37d6873d-3d97-3423-857b-f6782244dc3f | -20.7139 | -56.63216 | 2025-06-03 04:00:00 | NPP-375D | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 18f1aa92-d69d-39e1-836c-540fe1990c48 | -18.86768 | -53.63547 | 2025-06-03 04:00:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ef81ed1b-936b-3ec1-abb5-f514a6acd9b2 | -18.86646 | -53.64082 | 2025-06-03 04:00:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 5ba418e4-d8a7-398f-8c05-2da86c57f2f5 | -20.69235 | -56.67477 | 2025-06-03 04:00:00 | NPP-375D | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 672df79d-c1f2-3cb2-a1d6-249224764b9e | -22.67563 | -42.85643 | 2025-06-03 04:00:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| f2921fdb-8324-39fd-ac25-ed9014ead6ac | -22.39905 | -43.10907 | 2025-06-03 04:00:00 | NPP-375D | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 3d27ba74-8784-3ef9-91d2-6682ebb60b0f | -20.45153 | -44.1843 | 2025-06-03 04:00:00 | NPP-375D | PIEDADE DOS GERAIS | MINAS GERAIS | Brasil | 3150406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| fecd46c3-92fe-3fee-9826-f8d8a0636b6f | -20.6887 | -56.67212 | 2025-06-03 04:00:00 | NPP-375D | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 82e75d0c-1cb6-3936-bc45-510f7e30c381 | -20.45573 | -44.18085 | 2025-06-03 04:00:00 | NPP-375D | PIEDADE DOS GERAIS | MINAS GERAIS | Brasil | 3150406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 2322a8d7-95f3-3c43-8c5f-b17b378e11d8 | -19.97007 | -44.21465 | 2025-06-03 04:00:00 | NPP-375D | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 0beac59f-0292-3ad9-bfe3-baacdbdfd10f | -21.34797 | -48.67275 | 2025-06-03 04:00:00 | NPP-375D | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| f100a11a-cd64-3526-87a5-5f82784cd187 | -20.3103 | -45.58541 | 2025-06-03 04:00:00 | NPP-375D | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0d226872-df3b-352b-aae2-cca7552ad6ba | -21.91166 | -42.26379 | 2025-06-03 04:00:00 | NPP-375D | CANTAGALO | RIO DE JANEIRO | Brasil | 3301108 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| 0ffb64f6-0120-3a5b-972d-3826b4bc5919 | -21.34271 | -48.67622 | 2025-06-03 04:00:00 | NPP-375D | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| d0174c70-9fcd-3927-96e0-646a464716b2 | -18.83476 | -47.6798 | 2025-06-03 04:00:00 | NPP-375D | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e581af28-7276-39c3-ad62-dc6f0f6a68c1 | -17.75372 | -42.8954 | 2025-06-03 04:00:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b56d9450-db90-3cb0-ba4a-6d623c349a51 | -18.83908 | -47.68068 | 2025-06-03 04:00:00 | NPP-375D | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| cb9d28eb-9741-3b9b-a122-35a7ca9a7624 | -18.83397 | -47.68396 | 2025-06-03 04:00:00 | NPP-375D | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 24dd6147-5fb6-3622-a972-723ad0f0170f | -17.67396 | -42.74303 | 2025-06-03 04:00:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ba4307f2-405c-306d-ba8f-02e17f5d8d01 | -19.90576 | -41.84595 | 2025-06-03 04:00:00 | NPP-375D | SIMONÉSIA | MINAS GERAIS | Brasil | 3167608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| f267dd73-6c52-3be1-8444-b61d7823ed7d | -18.83828 | -47.68484 | 2025-06-03 04:00:00 | NPP-375D | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| edb16538-bba5-370a-9cce-db4ab30ead73 | -17.77873 | -42.80855 | 2025-06-03 04:00:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 48edb73e-d36d-3be7-9874-9be8e6a7f28f | -17.7503 | -42.8948 | 2025-06-03 04:00:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 61d76711-1edb-3d56-bc30-ddeda70b375e | -23.59538 | -47.43711 | 2025-06-03 04:02:00 | NPP-375D | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 0ed1a8d6-ddae-3093-864c-398d289066ef | -18.8679 | -53.6218 | 2025-06-03 04:10:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 885318bb-f28e-3123-9172-eab7959bbb77 | -18.8675 | -53.6434 | 2025-06-03 04:10:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 175.4 |
| e200d65c-3a29-3a9d-9be5-daacfab9ab76 | -18.8875 | -53.6402 | 2025-06-03 04:10:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 109.1 |
| ee6d9bbb-a5db-3a53-b525-50aae949fdf4 | -18.888 | -53.6186 | 2025-06-03 04:10:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 6686d152-0403-36f5-b18d-6323b0ff7d23 | -7.95838 | -43.2365 | 2025-06-03 04:17:00 | NOAA-20 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a69f3245-72d0-35a5-beb2-a6fa6c05e09a | -6.1023 | -43.95636 | 2025-06-03 04:17:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9cab3c32-91ec-3cc3-97eb-f4e42b99f680 | -5.18666 | -48.07952 | 2025-06-03 04:17:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 52e1f06b-5a6b-3635-a337-2087ba5afe61 | -7.71208 | -46.31963 | 2025-06-03 04:17:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b12e7800-48d2-3d34-ac59-2829792c220d | -7.08551 | -46.55515 | 2025-06-03 04:17:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4e0b0183-fd46-3847-ab4b-fcab5a114a01 | -7.88651 | -46.223 | 2025-06-03 04:17:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 099a723a-f6ba-34bf-a3a7-1b7de305b988 | -4.80937 | -45.26157 | 2025-06-03 04:17:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| da150284-f742-3bac-8830-69d5fcb8fa7f | -6.97257 | -42.90703 | 2025-06-03 04:17:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.9 |
| 128b568c-1f98-3fe9-8fc9-e993c1b274a8 | -6.97314 | -42.90333 | 2025-06-03 04:17:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 237691c5-427d-35d5-ae48-258f5a4932ad | -7.20373 | -45.35181 | 2025-06-03 04:17:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3607eaae-d0d2-3ab0-b772-b2b1b244d1e1 | -5.82961 | -46.36068 | 2025-06-03 04:17:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4fe63049-4402-3993-8baa-47f751a4aef8 | -7.0209 | -44.57377 | 2025-06-03 04:17:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 09c792b5-556b-3af6-b96f-01dbddf009c8 | -8.02236 | -46.22603 | 2025-06-03 04:17:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 706a0bb1-9c5c-3fad-a37e-9caa3a7a29c8 | -7.02145 | -44.57031 | 2025-06-03 04:17:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6795f974-ca8a-306f-964c-fac0b4a9c2ea | -5.49449 | -45.24829 | 2025-06-03 04:17:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 55ed46f6-620c-3985-98e1-cd42da247037 | -6.10176 | -43.95985 | 2025-06-03 04:17:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 77401aed-5bd7-3955-a4f4-bad4209cc2c9 | -6.97199 | -42.91074 | 2025-06-03 04:17:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.9 |
| 7f9d8264-b28a-3fe5-9a74-2482e54ad7b4 | -5.83362 | -46.35754 | 2025-06-03 04:17:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7890a913-cef8-30e7-89cf-999e2963e306 | -7.0176 | -44.57324 | 2025-06-03 04:17:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 923b4f93-92d9-3026-93d9-651877fdc896 | -7.01814 | -44.56978 | 2025-06-03 04:17:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 43639cc4-7a38-333a-bd35-5cb7c98c626c | -7.22201 | -43.12976 | 2025-06-03 04:17:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| c4481e63-831c-3a6c-9974-264592aa57e1 | -6.96915 | -42.90652 | 2025-06-03 04:17:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.9 |
| 35cdd9b1-2fec-3a8a-ae09-b40383dd39ee | -7.68288 | -44.57544 | 2025-06-03 04:17:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6207a595-f8f5-3ba8-8bc7-a166f71635a7 | -7.22994 | -43.12347 | 2025-06-03 04:17:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 7e29d567-1ba4-360d-a56a-6eadb06a8ae7 | -7.01048 | -44.59695 | 2025-06-03 04:17:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 8e95a20b-ad43-309a-aba4-8aa24c38569c | -6.72838 | -42.90088 | 2025-06-03 04:17:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 1894cd09-22a6-3393-9613-3ec9bf74f465 | -6.96799 | -42.91394 | 2025-06-03 04:17:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |


[Clique aqui para ver as próximas entradas](README8.md)

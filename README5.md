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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d0d5b034-b670-383a-9d54-1340a2de4eaf | -4.35579 | -47.76748 | 2026-06-18 03:57:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 362fa117-ff06-3405-b959-13be9d7c1f1b | -5.52219 | -37.62053 | 2026-06-18 03:57:00 | NOAA-20 | FELIPE GUERRA | RIO GRANDE DO NORTE | Brasil | 2403707 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| b7b51621-6dfa-3594-bcc1-b803c882a8ce | -7.5939 | -46.47507 | 2026-06-18 03:57:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 44991bfe-c78d-34ef-9fad-283f86276ec7 | -7.72387 | -44.16842 | 2026-06-18 03:57:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 09c85e43-4b57-3b69-ac13-6bbce2a2cbb3 | -5.2995 | -43.69588 | 2026-06-18 03:57:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3c0d3676-155d-3d00-9bbf-a62f9b3bb2ee | -7.5955 | -46.47447 | 2026-06-18 03:57:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 3d360b41-8533-3730-822f-4aaccf528a3f | -7.36074 | -49.86118 | 2026-06-18 03:57:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bf4de4fe-98e9-31f0-aac7-245e098b7589 | -7.7156 | -44.16701 | 2026-06-18 03:57:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2ebd15ec-247c-34e3-b475-1c1589c651d0 | -5.80683 | -45.07155 | 2026-06-18 03:57:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b113abdc-0dd1-360a-8c4d-cb31960b4279 | -5.29661 | -43.68759 | 2026-06-18 03:57:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e1b22644-729b-33ae-8cbc-b64aaab62557 | -7.60453 | -46.47149 | 2026-06-18 03:57:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 478a3a2c-d309-3299-bfde-148866fca09e | -7.80321 | -46.46074 | 2026-06-18 03:57:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0b84bce8-25bc-3207-8b17-0acc1f7bc0eb | -5.29051 | -43.95738 | 2026-06-18 03:57:00 | NOAA-20 | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 4aa81745-4ede-3b15-b7dd-f5a3fd676124 | -6.56226 | -47.88798 | 2026-06-18 03:57:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 540e02a7-9798-3e74-ba3f-5814acff00a7 | -6.16024 | -48.50316 | 2026-06-18 03:57:00 | NOAA-20 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 947e30e6-8a95-30f5-a386-a75efd0e7530 | -7.71689 | -44.15949 | 2026-06-18 03:57:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 8cd382b9-9129-33d9-b138-83efd9366ddd | -5.29181 | -43.69068 | 2026-06-18 03:57:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7f17da71-fce2-33ac-8e25-8a00bff6c712 | -4.3515 | -47.75922 | 2026-06-18 03:57:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3c6987f6-1fe4-3bdf-8212-bd4c3437f239 | -4.35718 | -47.76743 | 2026-06-18 03:57:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b2094d42-d005-367f-891f-b40b20efcb5b | -4.35643 | -47.76378 | 2026-06-18 03:57:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d2d91219-8038-32cb-b863-a0cc6566d21b | -4.3516 | -47.76648 | 2026-06-18 03:57:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e414b399-2942-3365-8cc7-90e46a8383b1 | -6.03371 | -43.99864 | 2026-06-18 03:57:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4b96246c-b642-3a5f-a17e-bcad450004bb | -7.35988 | -49.86582 | 2026-06-18 03:57:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5f8e5787-6170-31ca-b9a0-1e0f7b9b922c | -6.10724 | -44.74355 | 2026-06-18 03:57:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9198045a-d2b3-389f-8d38-49d8aa34a71f | -6.28573 | -43.63762 | 2026-06-18 03:57:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 469ee462-7899-3aea-8b2d-7be2bdd5513d | -7.59873 | -46.47595 | 2026-06-18 03:57:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 5a07c362-5d07-3ef6-b613-77d53ae802fe | -6.394 | -44.17745 | 2026-06-18 03:57:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4fff39cf-ba27-3468-ba2b-f8634e63ca43 | -7.91806 | -48.24846 | 2026-06-18 03:57:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3d796057-c585-3d54-860b-4dccdb3f7553 | -7.8401 | -48.39074 | 2026-06-18 03:57:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fbb8a220-1c2e-3289-9faa-7db2ce577128 | -5.92433 | -43.47866 | 2026-06-18 03:57:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fb7bb9c5-c8c2-36ae-90ec-3b9fd892092c | -5.29534 | -43.69516 | 2026-06-18 03:57:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ee255ca6-c148-31d5-ae84-993c0caf81e9 | -5.80604 | -45.07618 | 2026-06-18 03:57:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 57a1f918-667d-3f2c-bf44-163746a5c5fc | -7.5997 | -46.4706 | 2026-06-18 03:57:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 44dd8eae-e761-33c3-ad4b-628a19c72f7b | -5.2954 | -43.95419 | 2026-06-18 03:57:00 | NOAA-20 | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| a921df73-c17f-3043-985f-491ceefbb202 | -7.84076 | -48.38715 | 2026-06-18 03:57:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a4a49f64-f7e8-3735-8ef7-1934d8c7b7b0 | -5.29886 | -43.69967 | 2026-06-18 03:57:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dc777249-21a3-3853-8f8f-a0a01be0daee | -5.30013 | -43.6921 | 2026-06-18 03:57:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4c6442a9-6836-32f7-809e-6e74656157be | -6.39468 | -44.17351 | 2026-06-18 03:57:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 88bc069d-0ff3-3019-8c1a-a33eaaa75753 | -4.35085 | -47.7629 | 2026-06-18 03:57:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8a138d5d-054a-398d-85ca-5c376e6e2616 | -7.3668 | -49.8623 | 2026-06-18 03:57:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 23341a72-f7c4-3417-b045-e01260147722 | -6.03432 | -43.99496 | 2026-06-18 03:57:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5cd9b0e7-cc38-3536-8c01-5430ada6f524 | -9.41156 | -36.86702 | 2026-06-18 03:57:00 | NOAA-20 | CACIMBINHAS | ALAGOAS | Brasil | 2701209 | 27 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 00d379f0-ddcc-3e38-9755-3a9a17039b77 | -5.81054 | -45.07713 | 2026-06-18 03:57:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 83654139-8827-315a-ae23-f0ccaa5692c5 | -7.83944 | -48.39438 | 2026-06-18 03:57:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 32383b7d-bd75-3d9b-a216-8aabc8375b1c | -5.80974 | -45.08176 | 2026-06-18 03:57:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c26effc2-0f7a-33a2-89ea-239de65d2856 | -7.60126 | -46.47 | 2026-06-18 03:57:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 6510587e-68ff-3f69-ab38-3c340fc1ee6a | -7.72451 | -44.16467 | 2026-06-18 03:57:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d3a34beb-7bd6-3882-8c5c-999a0792c751 | -6.28163 | -43.63705 | 2026-06-18 03:57:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 302ab4ca-10ab-3304-8ccc-21697dcb33fa | -7.92143 | -48.25189 | 2026-06-18 03:57:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9282854c-ce59-3297-9ec6-ac80a745ef4f | -6.83627 | -47.91443 | 2026-06-18 03:57:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5edc89a6-95d7-3eaa-a55d-ffd51acde3ae | -6.97533 | -42.88429 | 2026-06-18 03:57:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 94803d17-0a67-31db-a44e-acf6c12b366f | -5.80524 | -45.08081 | 2026-06-18 03:57:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 305a4be5-7d60-3a0f-8694-2f94ac85ee6c | -3.35195 | -43.16966 | 2026-06-18 03:57:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 635dd78e-6fd0-3ffd-9afb-fc16666bc383 | -5.80762 | -45.06696 | 2026-06-18 03:57:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c3dbbf3b-d471-3bdc-b967-5f1d88b506f7 | -6.84627 | -46.34405 | 2026-06-18 03:57:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8337333e-247a-3350-a047-c4f3a4198e5d | -3.3567 | -43.16659 | 2026-06-18 03:57:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dcae214b-16c5-363c-b2bf-0e4322dc0a61 | -5.61095 | -37.53148 | 2026-06-18 03:57:00 | NOAA-20 | CARAÚBAS | RIO GRANDE DO NORTE | Brasil | 2402303 | 24 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d4910943-6bea-357b-8126-d30591d5bb1f | -7.79585 | -46.45162 | 2026-06-18 03:57:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ef81f8f9-084d-356a-aae0-57a0eaf61383 | -3.50818 | -48.03478 | 2026-06-18 03:57:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5640d9f4-6f93-38d1-ac28-b2eeef200745 | -9.41214 | -36.86317 | 2026-06-18 03:57:00 | NOAA-20 | CACIMBINHAS | ALAGOAS | Brasil | 2701209 | 27 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 93bf1ac6-b125-38f2-a150-15b16de38646 | -8.25908 | -43.92286 | 2026-06-18 03:57:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9f82bbf0-df64-3970-ab4f-3d2d9f61473a | -7.71625 | -44.16325 | 2026-06-18 03:57:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 9cbf1008-fe24-3acb-a1c4-6c85b172c5cb | -7.79974 | -46.4578 | 2026-06-18 03:57:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0f27bd65-90f9-3012-86e5-cccdad57852d | -7.60033 | -46.47536 | 2026-06-18 03:57:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 5e1933fd-32e7-38fd-8e10-cfcb8288a25c | -6.84101 | -47.9191 | 2026-06-18 03:57:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ce02a13f-3e22-3bf2-8367-2b4117e9edbd | -5.29181 | -43.94955 | 2026-06-18 03:57:00 | NOAA-20 | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 2ac29a76-5398-3837-952a-f7754030cb4c | -8.62547 | -36.88389 | 2026-06-18 03:57:00 | NOAA-20 | VENTUROSA | PERNAMBUCO | Brasil | 2616001 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 531722d6-59ac-35a5-a305-275235ca69f2 | -6.1539 | -48.50595 | 2026-06-18 03:57:00 | NOAA-20 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 90915ad0-32da-3cd4-a0b5-4e437458678f | -5.29597 | -43.69137 | 2026-06-18 03:57:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a652251d-367a-3cc3-8829-df1fa55b5ac2 | -7.79937 | -46.45454 | 2026-06-18 03:57:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 260ed296-76ea-3142-aa5d-de835c13f086 | -7.72165 | -44.15649 | 2026-06-18 03:57:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b2fa8bfb-daed-39f4-824e-1bdd94f2a596 | -6.15614 | -48.50623 | 2026-06-18 03:57:00 | NOAA-20 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 863c6b82-6406-3f13-adc5-40463bca0b4b | -4.35222 | -47.76281 | 2026-06-18 03:57:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 69994e99-7b0c-38a3-a04b-00ce1ae8ed70 | -5.29116 | -43.95345 | 2026-06-18 03:57:00 | NOAA-20 | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 3fe5942c-9924-371b-8e39-7b4e62f1b2b5 | -5.7954 | -45.08366 | 2026-06-18 03:57:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 132d7a3d-6bd9-327c-a60e-9d75b5b9278c | -7.36156 | -49.8567 | 2026-06-18 03:57:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 85f1e428-5a75-3926-8d81-35b0fb03c863 | -12.8354 | -44.3657 | 2026-06-18 04:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 41.1 |
| dee76175-0cc5-3960-b46b-a6fc6052b295 | -10.9164 | -56.8536 | 2026-06-18 04:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 151f6a53-84ba-3f47-b4f2-a8cdb03c3af4 | -12.84299 | -44.37032 | 2026-06-18 04:00:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| e1cf6cc6-b327-32cc-ad9f-3321ab4f1a84 | -11.2123 | -46.57635 | 2026-06-18 04:00:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a313ab73-7258-3145-8672-8d7994f76531 | -11.81758 | -47.33766 | 2026-06-18 04:00:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 21d4503b-9c5e-35b5-bd1d-a41a0cc8e13b | -10.91452 | -46.37148 | 2026-06-18 04:00:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c1715534-cf66-35d8-8999-f99ff3a6ac74 | -8.99191 | -47.03288 | 2026-06-18 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f75a8367-c708-3d4e-9655-6d35b4ea46ed | -12.06813 | -47.55189 | 2026-06-18 04:00:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 362987c6-650f-38e7-a4a7-da22cfb43e05 | -10.6548 | -49.20414 | 2026-06-18 04:00:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 98152c7b-9020-3bca-a90b-ddbbb2023ba3 | -9.53795 | -40.33503 | 2026-06-18 04:00:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 68.5 |
| 83bad1db-e60f-36ff-a75b-66ed7340437b | -10.98601 | -47.75207 | 2026-06-18 04:00:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 00c3af9f-4dc3-3a45-a2af-8d76bdf65ccd | -14.40839 | -42.60088 | 2026-06-18 04:00:00 | NOAA-20 | PINDAÍ | BAHIA | Brasil | 2924504 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ce1cece3-cdeb-3cc3-9138-b852604b7e8d | -13.58949 | -43.35728 | 2026-06-18 04:00:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 37d52b52-dd56-390a-950d-d92e020c0e78 | -12.42159 | -49.09808 | 2026-06-18 04:00:00 | NOAA-20 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f884de24-8b7e-327a-a374-2ccb16d3db5a | -8.93765 | -48.00082 | 2026-06-18 04:00:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4e44bc04-a495-3106-a70b-b1b558ba0232 | -9.5413 | -40.33558 | 2026-06-18 04:00:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 68.5 |
| e9d806e5-ae4d-3495-89eb-196a9243dfa2 | -10.99099 | -47.75293 | 2026-06-18 04:00:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ce0657da-e65c-39df-8116-2deeeab54783 | -12.21212 | -52.78152 | 2026-06-18 04:00:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c5a7f582-df10-32a6-9bdb-0930e0246965 | -8.61443 | -45.99447 | 2026-06-18 04:00:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ff63f804-d606-3c25-9a96-2ac382873878 | -12.84205 | -44.36903 | 2026-06-18 04:00:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 2b0f0cff-3419-3ef0-a42c-f6d808e3ebe1 | -10.74689 | -48.53691 | 2026-06-18 04:00:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 97f50925-ff00-3b4c-9abc-e9588dc1446c | -10.81109 | -48.77004 | 2026-06-18 04:00:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d0335f99-43b7-39bd-9b92-d369040d1408 | -9.28427 | -43.163 | 2026-06-18 04:00:00 | NOAA-20 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ce51e948-6524-3488-ac3f-e6ca5f98e7de | -12.42222 | -49.09473 | 2026-06-18 04:00:00 | NOAA-20 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README6.md)

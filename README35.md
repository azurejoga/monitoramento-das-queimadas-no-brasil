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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9f414d15-dc15-3221-ba00-cb07ab7b5853 | -5.85387 | -53.52213 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0a556c13-a6dd-3a1f-b401-388f13c19ce9 | -9.79357 | -45.06091 | 2026-09-20 04:19:00 | NPP-375D | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| be76155b-ea44-3427-857b-a40eef74a65e | -6.68266 | -43.0141 | 2026-09-20 04:19:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f49a0405-5ca1-3295-a9e1-a0da5c08ef64 | -9.83815 | -46.4347 | 2026-09-20 04:19:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| cacbc54b-c51f-3d9b-bca6-544784e8b6c7 | -6.93779 | -43.10322 | 2026-09-20 04:19:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3b0755a2-bac4-3c68-b01d-0aea563b7644 | -7.36953 | -44.86589 | 2026-09-20 04:19:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c7e6b594-eda7-35e1-9385-b0ce5651ab1b | -9.90006 | -46.53385 | 2026-09-20 04:19:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 827cd639-ee95-34f7-93ff-b1e6d1445bfc | -9.27942 | -44.39541 | 2026-09-20 04:19:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4df84ed9-d52c-32a3-ac4a-3166878c4e87 | -9.23725 | -46.23981 | 2026-09-20 04:19:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| be424e4d-6563-3cd7-89c7-a58f25626dff | -7.6858 | -44.66601 | 2026-09-20 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c520ad36-39e7-3c7b-96d1-6098633a3ad3 | -6.91809 | -42.89682 | 2026-09-20 04:19:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 3561a2a0-335f-3b8c-a3e1-b3bfc4e7ef58 | -8.4463 | -45.86501 | 2026-09-20 04:19:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9fb2fbb5-2b40-3a9b-aef1-4bf4ec389ba5 | -8.29317 | -46.86869 | 2026-09-20 04:19:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e4d1f88a-70f8-3416-96c9-5246d655677c | -8.71025 | -45.44648 | 2026-09-20 04:19:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 631fa504-0ab8-3571-9ec8-afeca2298959 | -7.49167 | -46.71632 | 2026-09-20 04:19:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dd24a6d3-71b5-3937-baa7-a47e2a15bcb4 | -6.19261 | -45.33347 | 2026-09-20 04:19:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1b739e2c-98d2-3a44-bcb0-5104b498a4f5 | -5.65991 | -43.37368 | 2026-09-20 04:19:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e8290d03-ab47-3bc3-a87a-4cc867755bb2 | -5.84898 | -53.54843 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b66d1dec-2e97-30c1-b43c-efba97c96d20 | -7.97023 | -44.07679 | 2026-09-20 04:19:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0f8174b0-9c56-35b8-b66d-6562d16446f4 | -4.72975 | -46.12918 | 2026-09-20 04:19:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b55b9952-7f38-3e63-b33a-da0585485851 | -5.60245 | -44.37905 | 2026-09-20 04:19:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bf70bd9a-2e46-37b6-b019-c8f6b8313707 | -9.23888 | -46.23022 | 2026-09-20 04:19:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 2fe2dd26-6817-38bb-accd-97983a7e6510 | -9.28574 | -48.19704 | 2026-09-20 04:19:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d9e89b08-bfac-3bec-8512-1b60e0f05796 | 1.26831 | -50.73749 | 2026-09-20 04:19:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 768e3966-909c-3756-9b66-c79d54a016ac | -6.98734 | -43.37718 | 2026-09-20 04:19:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 32ba7316-e7b7-3243-a159-14e236906ed9 | -8.87285 | -45.94896 | 2026-09-20 04:19:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1cc1d656-c310-3ce1-be9e-182579b50ef2 | -9.26338 | -46.20089 | 2026-09-20 04:19:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| cd98a34b-41a3-3c8a-9d8a-b9bfb06a7dd9 | -7.4995 | -46.13504 | 2026-09-20 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6db2845d-2389-37d8-861d-9d9c2fc8fa20 | -8.49921 | -47.43781 | 2026-09-20 04:19:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 98d38c47-958c-3725-9214-11171a964dda | -10.4706 | -45.08989 | 2026-09-20 04:19:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0c018da2-0bee-3845-8c3d-24d0a8ab0a71 | -10.29965 | -45.43075 | 2026-09-20 04:19:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 58d64cdb-4d24-3b87-8c5b-f981bc795d1d | -11.1541 | -42.79018 | 2026-09-20 04:19:00 | NPP-375D | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a653fd36-1116-38b2-b217-fa36b5d79954 | -11.44682 | -45.32156 | 2026-09-20 04:19:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 6c5a4d1d-8edc-393d-ae75-70b1122792ae | -11.65945 | -43.43513 | 2026-09-20 04:19:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dd71fd7c-a8a1-329f-8507-6f9fba3df216 | -10.07349 | -45.64477 | 2026-09-20 04:19:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 48ab75fb-49be-35fc-b941-a1ad4d4457d2 | -6.04208 | -44.03635 | 2026-09-20 04:19:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 93c0e3d1-5d6d-37ab-bb56-44b9a6be6457 | -5.40865 | -44.28609 | 2026-09-20 04:19:00 | NPP-375D | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2d4eee89-4fcb-32f0-9dc7-e72fadae71fa | -9.12906 | -45.71143 | 2026-09-20 04:19:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c98806cb-ad46-3101-99b3-d6f835a8f3b8 | -5.89055 | -53.65007 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 32d9421b-a731-32df-90c8-325ee4c42457 | -5.40641 | -44.27736 | 2026-09-20 04:19:00 | NPP-375D | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5768dae3-9b4e-376b-a3e2-d12dd3bf6e71 | -11.08026 | -48.31802 | 2026-09-20 04:19:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c9a7cb59-10e2-3a51-85cf-c4dfe77d9a42 | -7.62744 | -45.42408 | 2026-09-20 04:19:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 91685a63-4f2b-35f3-9946-ccf4d42cd55b | -10.56309 | -46.55873 | 2026-09-20 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e5773c9f-297a-3aed-b542-9d286db274cd | -11.44614 | -45.32559 | 2026-09-20 04:19:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 07d20e60-000a-3322-92c0-40b0d2a40a3a | -7.35132 | -44.61416 | 2026-09-20 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4be5ed61-2360-3f3f-b5d5-f436d15b3156 | -8.76152 | -48.66577 | 2026-09-20 04:19:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 6.4 |
| f47bddc7-e297-3c87-85bd-c748cb2400a2 | -9.26262 | -46.20544 | 2026-09-20 04:19:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 674bb165-efca-30f3-9c87-4e85c70a7330 | -7.74941 | -46.76427 | 2026-09-20 04:19:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e47fcee5-a2f8-3f4f-ae72-82f9e6759311 | -8.05267 | -46.25002 | 2026-09-20 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| bc4c7bc3-871c-34a4-bf81-0295928c9b71 | -6.25837 | -42.72125 | 2026-09-20 04:19:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 9.9 |
| 5691afdf-1d58-3bf5-8820-11b9bc29656f | -6.99352 | -45.67951 | 2026-09-20 04:19:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2d1b4fe2-1c8e-32f3-9c85-f09a0a082abe | -10.93775 | -50.58616 | 2026-09-20 04:19:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| b3217c27-455e-38df-b827-81eada3a956d | -10.31156 | -50.26904 | 2026-09-20 04:19:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0d9c8301-de01-3e78-b2c4-ad081562236b | -10.3886 | -48.99433 | 2026-09-20 04:19:00 | NPP-375D | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| a40a4a3d-c84a-30c1-b09b-ae47044c4885 | -8.76236 | -48.66109 | 2026-09-20 04:19:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 211ba191-e8fe-349a-bc93-21c002915a1d | -6.19861 | -45.32271 | 2026-09-20 04:19:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 15f73f0f-bfaa-3efa-817f-1ff5a8400f8f | -10.19073 | -44.15106 | 2026-09-20 04:19:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9f08c053-68f6-3160-bdc5-4598086acc7c | -9.98095 | -46.62415 | 2026-09-20 04:19:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6220d8fd-9e08-35a7-9898-7451d7b4539f | -11.44664 | -45.38768 | 2026-09-20 04:19:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 550900e7-6a14-3b2b-8d9b-f9fbcc0907ae | -7.41091 | -49.84591 | 2026-09-20 04:19:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 6e4d9ddb-d40c-336e-8514-b48f376fea83 | -6.30129 | -47.62978 | 2026-09-20 04:19:00 | NPP-375D | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f850bf43-cda1-377b-a441-0980c9cf333b | -5.66681 | -43.37478 | 2026-09-20 04:19:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ffdfdcb4-3227-39f0-bb9d-dd37159096e4 | -7.10401 | -42.09016 | 2026-09-20 04:19:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 6f1d511a-2829-3d58-9820-049704af3d49 | -10.32636 | -48.0033 | 2026-09-20 04:19:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5df248c7-f5c3-3a27-9c72-019dadcef8b6 | -9.28275 | -48.19951 | 2026-09-20 04:19:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 848cbc9a-f8a7-30fe-9804-babaeb32d728 | -7.96864 | -44.06477 | 2026-09-20 04:19:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cf48c0ab-5072-3a3a-b867-f8496ad6df26 | -7.55661 | -45.45023 | 2026-09-20 04:19:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 943d8bfe-757b-372b-9ef9-8ae913b53da5 | -6.92028 | -42.91158 | 2026-09-20 04:19:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| f3a8c4c8-5bf3-3070-8be4-5b268d361266 | -6.68555 | -43.62843 | 2026-09-20 04:19:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 28cbf11f-b937-371b-b4ec-d6f9d91ac169 | -6.91548 | -44.90448 | 2026-09-20 04:19:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2700a07a-797f-3ccb-8fec-1d851462cfab | -11.05874 | -49.73883 | 2026-09-20 04:19:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1e53ea22-0f69-311b-af05-5770ab4a212f | -7.75857 | -44.88369 | 2026-09-20 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8bdb62e6-d6f5-3410-86f7-fe56cfb9abcd | -9.12462 | -45.71527 | 2026-09-20 04:19:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 227c5dd6-48f6-3286-9738-be477b618dfe | -10.82623 | -50.93108 | 2026-09-20 04:19:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d19939ad-c67d-38e0-84fc-93862a29d0a3 | -8.44033 | -45.83151 | 2026-09-20 04:19:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f68cdae4-eae3-359c-bc6d-fa1fd716d3b1 | -9.79578 | -45.06965 | 2026-09-20 04:19:00 | NPP-375D | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fa43444b-e13f-3491-8901-fd1e166646a8 | -10.77827 | -46.16264 | 2026-09-20 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8544dc38-33e2-3ed7-a09d-e690cca76e43 | -11.49652 | -47.79126 | 2026-09-20 04:19:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5a2c2058-6d9f-3183-b976-52126c83a17b | -10.77931 | -50.88485 | 2026-09-20 04:19:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2ebd764e-14fc-39d6-8908-c67eecb667e4 | -10.56852 | -46.55003 | 2026-09-20 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c3990bb8-67f6-3002-a86c-e66872573290 | -5.93606 | -35.62044 | 2026-09-20 04:19:00 | NPP-375D | SÃO PEDRO | RIO GRANDE DO NORTE | Brasil | 2412708 | 24 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 581eb923-da7f-3ab8-860e-580500fbf720 | -11.21962 | -48.36069 | 2026-09-20 04:19:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4d10f25f-ba92-3318-9da9-be3975142268 | -9.12238 | -45.72859 | 2026-09-20 04:19:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| a191c57f-5476-36a7-a958-10f298f30978 | -10.40061 | -48.90154 | 2026-09-20 04:19:00 | NPP-375D | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7985f074-f9f5-3010-8a09-999a4c31982d | -9.26641 | -46.20608 | 2026-09-20 04:19:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 21053fa7-2a1c-3244-80b6-d41259dfa2c6 | -6.26193 | -41.65977 | 2026-09-20 04:19:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e95f6f15-9fc4-3043-b4db-d351717bf2e7 | -9.01858 | -44.92062 | 2026-09-20 04:19:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e68f1fe6-e1ed-384a-a1a5-e4a6471f1e6b | -9.69847 | -48.31876 | 2026-09-20 04:19:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 668a6dd3-0eff-3b9e-a556-0b7b5ca50eb0 | -8.76514 | -48.67131 | 2026-09-20 04:19:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 93dc3881-32dc-3a4e-bd4b-54886cd2d905 | -7.57731 | -44.89704 | 2026-09-20 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 140716a2-8140-38b2-a3f0-b7af30247767 | -6.99006 | -43.73017 | 2026-09-20 04:19:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c25fc57e-5eeb-36ee-a8ad-cbfc50c7bae8 | -7.36883 | -44.87003 | 2026-09-20 04:19:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 96ea126d-33e6-3762-8f61-918f164b1835 | -8.62744 | -47.62311 | 2026-09-20 04:19:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6e7f6345-ddbb-36da-adf8-fda0bfb0db06 | -9.79068 | -45.0563 | 2026-09-20 04:19:00 | NPP-375D | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8f5c5f81-2c18-3d5c-a2c2-194838798bd4 | -9.53958 | -45.77946 | 2026-09-20 04:19:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 056a9471-be6f-361f-be0a-d34e085ca6a9 | -8.05468 | -46.28544 | 2026-09-20 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 19abafc4-296b-3fe4-be3f-76fa329f8683 | -8.1642 | -54.75907 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1a6cb26e-4584-30c1-b5d8-8d157b25a1c2 | -10.47662 | -46.29604 | 2026-09-20 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 52e95914-3cec-30ec-a149-4bc03b7e45c8 | -11.45183 | -45.71624 | 2026-09-20 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f7dfbb7a-8bfd-3c6e-b590-b7d75f93973e | -3.55605 | -50.28847 | 2026-09-20 04:19:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README36.md)

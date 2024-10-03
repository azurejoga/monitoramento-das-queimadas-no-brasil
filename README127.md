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

## Dados Diários - Página 127

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6c40fa59-abef-3762-82ea-debae4e2fa12 | -13.00507 | -51.12996 | 2024-10-03 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cd107844-7468-3f6d-850f-257cefeb0cb8 | -13.0027 | -51.12113 | 2024-10-03 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ba8f7c97-5b57-3252-8f54-9df936155f74 | -13.00209 | -51.12528 | 2024-10-03 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0b1559c3-48c7-3342-b8b1-3fe4301833d8 | -12.99911 | -51.12059 | 2024-10-03 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| f603a376-75d6-3620-944f-5c293ae292cc | -12.99851 | -51.12473 | 2024-10-03 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 45bef344-f40e-3ed9-b476-18e5df66241c | -12.99791 | -51.12887 | 2024-10-03 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 87a36ec5-4717-3dcb-b475-7cdb0766318d | -12.97643 | -51.12563 | 2024-10-03 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bd7b4de7-9345-316f-acc0-a1586a7e2504 | -12.97285 | -51.12508 | 2024-10-03 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2c1474fe-2f18-303a-9f46-689e297ed517 | -12.96927 | -51.12453 | 2024-10-03 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d0475b07-2765-3043-85ef-20c0c0d98451 | -12.96569 | -51.124 | 2024-10-03 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2e818f35-172d-391c-833a-84a469a78ec9 | -12.79468 | -50.58657 | 2024-10-03 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9bb3fefb-e2f5-3ead-bf95-7c3337ba097b | -12.79101 | -50.58603 | 2024-10-03 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cd8b4ac5-3e56-3f7d-a8cc-15acbb6d25d9 | -12.78734 | -50.58548 | 2024-10-03 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 201a7430-af72-33ec-8030-086b6d88c4c7 | -12.78368 | -50.58493 | 2024-10-03 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0809047c-52a2-3edf-bdc2-bebee9e4d704 | -12.76711 | -50.59579 | 2024-10-03 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 51077803-c212-3a18-ba6d-e78b2fa2d8d3 | -12.41948 | -51.01079 | 2024-10-03 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a9057e61-2f90-3b39-b51f-c81342af2ec6 | -12.40099 | -51.01219 | 2024-10-03 04:51:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8eda8441-5ffc-3a7a-a359-4dd7fbc2f531 | -12.40038 | -51.01631 | 2024-10-03 04:51:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2d54ea2a-0534-3ad7-9dd1-fb14d347e34c | -12.39977 | -51.02043 | 2024-10-03 04:51:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 83d35b13-6418-316c-b7f6-e7fece520f3c | -12.39741 | -51.01165 | 2024-10-03 04:51:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4169f02c-a09d-3b9b-8fd8-d58fd0d2669a | -12.3968 | -51.01577 | 2024-10-03 04:51:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ecfcb378-81f9-385b-8fd0-6f3ef561ceb4 | -12.39459 | -50.95629 | 2024-10-03 04:51:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 9.3 |
| fa62fca4-34c4-321c-89e6-ced1fbce4b47 | -12.39383 | -51.01111 | 2024-10-03 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0f9a7d91-11ff-3318-9008-06752d43bc00 | -12.39322 | -51.01522 | 2024-10-03 04:51:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c94acf70-eb93-3226-ac01-bbab67f4638e | -12.391 | -50.95575 | 2024-10-03 04:51:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6f2c843d-e274-3714-86d4-f6efec7b6e61 | -12.38735 | -50.98059 | 2024-10-03 04:51:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e44e96b7-c6d4-304e-a849-bbcde6285f04 | -12.38377 | -50.98005 | 2024-10-03 04:51:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4261ad38-ea3b-305b-b459-88c363f20e74 | -12.38316 | -50.98417 | 2024-10-03 04:51:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8748051c-176a-3378-b200-65ae6bb0f9e6 | -13.1365 | -51.19497 | 2024-10-03 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 64d7c909-ae60-302e-93f3-ae0f1704b0c5 | -13.13292 | -51.19442 | 2024-10-03 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 8cbd53b9-09f7-3caa-a0a9-c164f6a77356 | -13.12935 | -51.19388 | 2024-10-03 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| b1414b58-d6ee-3093-a1b0-69edb02b21bb | -13.12578 | -51.19334 | 2024-10-03 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f4d77749-3085-3bbe-ab79-afcfc791bce7 | -13.10614 | -51.17769 | 2024-10-03 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b748fbba-473d-3188-adc4-8533d28975f1 | -13.10554 | -51.18182 | 2024-10-03 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 31408b3e-a313-3ffa-abf3-c267b959217f | -13.10196 | -51.18128 | 2024-10-03 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c14f3d23-e5bf-32a7-a7a8-af059139a77b | -13.09782 | -51.15952 | 2024-10-03 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 19d3f091-9e7b-3f0e-abde-826017eb5fb8 | -13.09722 | -51.16366 | 2024-10-03 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 16.8 |
| d23a631e-b31f-3a39-a091-5bebcde4cf44 | -13.09662 | -51.16779 | 2024-10-03 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 27227868-49dc-3f43-aac8-afd0fc0243a2 | -13.09485 | -51.15484 | 2024-10-03 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 42c9802a-71e9-32b2-a7a5-68a3adf7e02a | -13.09424 | -51.15898 | 2024-10-03 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 8be78d74-e0a4-3cae-aec7-4734844dacd8 | -13.09364 | -51.16312 | 2024-10-03 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 94.7 |
| e0f71525-8053-3107-a2b4-89fea4cfafec | -13.09304 | -51.16725 | 2024-10-03 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c400ee46-264b-31f9-a78f-f07c48d63409 | -13.09244 | -51.17138 | 2024-10-03 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 72fadcd3-16d0-38cb-be94-07ef13ba6751 | -13.09127 | -51.15429 | 2024-10-03 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 56953ad0-6334-3ff4-80a5-dc3c80353f28 | -13.09067 | -51.15844 | 2024-10-03 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 2317c23d-b86b-388d-98e8-6e103332cdee | -13.09007 | -51.16257 | 2024-10-03 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 94.7 |
| d94d8943-6040-308f-98d1-59a6b968fd26 | -13.08947 | -51.16671 | 2024-10-03 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 407dde91-339c-3a68-be60-7236f463ac40 | -13.08887 | -51.17085 | 2024-10-03 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d0df5b18-e641-3f04-aa59-3c44a32ec934 | -13.08826 | -51.17498 | 2024-10-03 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d178a6d4-1dbb-34ed-a7fe-75851b18df9a | -13.08769 | -51.15375 | 2024-10-03 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7943defd-082c-3b68-a20f-b9a2f390ee92 | -13.08709 | -51.15789 | 2024-10-03 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 0a118ae9-c57a-34c4-9cb8-0823d7cc40fe | -13.08649 | -51.16203 | 2024-10-03 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 20.2 |
| be5907f9-b166-3992-9309-d05ebfc01904 | -13.08589 | -51.16616 | 2024-10-03 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| eed88c19-56c4-3481-84b2-1bc28c243e50 | -13.08351 | -51.15734 | 2024-10-03 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 20.2 |
| a0d656dd-54ba-3120-b60c-da1eba4d6168 | -13.08231 | -51.16562 | 2024-10-03 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 09c701b9-a58a-3df7-b1ef-a3a51baf1f69 | -13.07933 | -51.16094 | 2024-10-03 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 22.3 |
| ad27a71a-2728-3675-bfb9-128c00264b16 | -13.07635 | -51.15625 | 2024-10-03 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 6e5a7396-cf38-3866-b0bb-368277828172 | -13.07576 | -51.16039 | 2024-10-03 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 22.3 |
| faf69587-bdf8-3e07-a9e4-1c6bc80a468f | -13.068 | -51.16343 | 2024-10-03 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a3dedd50-f7ad-318f-a874-08c7dd5b753b | -13.05846 | -51.15353 | 2024-10-03 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 5e90772e-52a7-3ba1-9f9d-0a300af09020 | -13.05548 | -51.14884 | 2024-10-03 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 153e48a0-353c-30ed-9e47-35da224d62eb | -13.05488 | -51.15298 | 2024-10-03 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 22.4 |
| fe751438-1913-3f66-8a67-5d8c9f06cadd | -13.05429 | -51.15712 | 2024-10-03 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 22.4 |
| b69032ae-be84-366a-96b5-a3ac8ca6fad9 | -13.05334 | -51.14998 | 2024-10-03 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 52bf8e9e-8e43-3041-b316-52e1039500cd | -13.05273 | -51.15411 | 2024-10-03 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 9b260a44-0617-32bd-8792-a70dfe31ce64 | -13.05211 | -51.15825 | 2024-10-03 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.2 |
| f76fc5c9-8bb3-3c17-8e0c-5ec7fbeffb27 | -13.04977 | -51.14944 | 2024-10-03 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 27f75c40-346a-3e9c-9823-817fd8c774f3 | -13.04832 | -51.14775 | 2024-10-03 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 23.6 |
| a1d4fd7a-4bba-3637-9056-fb9eab5986c1 | -13.04773 | -51.15189 | 2024-10-03 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ad139afe-857b-3f8f-91a0-590bb0f6da61 | -13.04619 | -51.1489 | 2024-10-03 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 28.2 |
| caf8750a-d593-33cc-bcad-0f27c3fb47ad | -13.04557 | -51.15303 | 2024-10-03 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4ddcda32-2204-3111-8756-5edc3a454be2 | -13.04261 | -51.14835 | 2024-10-03 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 28.2 |
| 239e67d2-b13c-39bd-ac1a-daeeb6022f4d | -13.042 | -51.15249 | 2024-10-03 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9c09425a-d296-35e5-8be6-0df78674547b | -13.03903 | -51.14781 | 2024-10-03 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2a971105-be5f-3efa-973a-1aa8adc4ba7c | -14.89975 | -51.56768 | 2024-10-03 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4278d0c2-f73e-31e1-9aff-6dcedf4bc835 | -14.08548 | -50.36237 | 2024-10-03 04:51:00 | NPP-375D | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 129038e8-b6cd-3cf6-adf2-1f20b5c832f8 | -13.9329 | -50.88385 | 2024-10-03 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 469f1605-5bc2-399f-8513-6635b1ab7938 | -13.92924 | -50.8833 | 2024-10-03 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7271a285-aad9-39d5-90ff-a9da805af516 | -13.72236 | -51.05663 | 2024-10-03 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9d3193d9-06bf-3c67-bba0-4c37e596ccf7 | -13.70863 | -50.86725 | 2024-10-03 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5d144043-8a35-3927-bb11-c9fb9e39ed9b | -13.70801 | -50.87159 | 2024-10-03 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2adc984c-dc53-3d10-8b9e-8c0cfda1e5c0 | -13.70766 | -50.95093 | 2024-10-03 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 84f3456c-368f-3d49-89dd-77003329ddaa | -13.70464 | -50.94609 | 2024-10-03 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d8efcc9b-1ed2-3dc8-bfaf-a94a98304a9e | -9.11441 | -51.52925 | 2024-10-03 04:51:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 14c98269-b597-3c66-a937-48c4a2dcaa7a | -7.78712 | -50.22836 | 2024-10-03 04:51:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| c71c8135-8253-3c61-9092-cf2aaf82d5df | -8.59775 | -51.39405 | 2024-10-03 04:51:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bbd67265-fa14-300b-88ac-d6c5e554a3a1 | -8.52704 | -50.97258 | 2024-10-03 04:51:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0ba6ac95-1bed-3f5b-922c-529144b9f420 | -8.52646 | -50.97636 | 2024-10-03 04:51:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c88068d2-ffb1-36f9-8fe0-c835785037ae | -8.40244 | -50.75579 | 2024-10-03 04:51:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 05c7ae7e-c3cb-3b00-8e47-dceb9f450c24 | -8.40188 | -50.75951 | 2024-10-03 04:51:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 48b73c9d-96dc-31c0-80a6-6ab001c14663 | -8.39841 | -50.75891 | 2024-10-03 04:51:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1c9c80bc-d3b6-35a1-a465-bbdcb079f979 | -8.27675 | -50.87062 | 2024-10-03 04:51:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 82b2ba86-6a8a-3015-bc14-66693b9329e2 | -8.07932 | -51.13966 | 2024-10-03 04:51:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 93378691-d131-38e4-a486-d2acf58fd3bd | -8.07875 | -51.14335 | 2024-10-03 04:51:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9e5c4f63-b739-324e-8514-9dfb2e953732 | -8.07533 | -51.14281 | 2024-10-03 04:51:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7b5264d5-5230-3589-870c-c82d44484a39 | -8.07476 | -51.14649 | 2024-10-03 04:51:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 927ed37d-4b80-3943-b1e2-c596f49f04a1 | -9.42486 | -50.67982 | 2024-10-03 04:51:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5ea449a7-7748-3280-a938-c298dff04480 | -9.32433 | -51.13235 | 2024-10-03 04:51:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 69f6ca83-afd8-3463-93b5-3798ac62847c | -9.30064 | -51.07808 | 2024-10-03 04:51:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6c558e46-9b3c-3a11-b7e6-0bbbbf580fcf | -9.29832 | -51.06993 | 2024-10-03 04:51:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README128.md)

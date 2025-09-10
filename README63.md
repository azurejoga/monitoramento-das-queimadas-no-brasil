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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 431c3792-920e-3eeb-8b68-62619ff1865f | -9.69527 | -46.81803 | 2025-09-10 04:42:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 1f89eebc-370e-366f-ad08-f851e55f4ada | -9.97843 | -50.2966 | 2025-09-10 04:42:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 083f5a44-9acb-38f7-8379-85f08383afee | -11.13848 | -48.35448 | 2025-09-10 04:42:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1371a635-1a6b-3434-95a3-bcf5d7e4482b | -7.71519 | -45.14911 | 2025-09-10 04:42:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5516b1a8-30f8-3c45-a174-911d4e858a16 | -11.68134 | -46.89877 | 2025-09-10 04:42:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 2126df64-05b1-3181-9b6c-9807f5c564b7 | -8.46817 | -48.95161 | 2025-09-10 04:42:00 | NPP-375D | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0a6d2b21-0657-384b-b5b8-e2713e0e9324 | -7.35523 | -44.31049 | 2025-09-10 04:42:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9a7327ca-0c0e-3c20-b54b-cd47a870f4fb | -8.18929 | -47.16436 | 2025-09-10 04:42:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 80811c03-d984-3beb-bb6e-58fbea79c948 | -11.66139 | -46.90515 | 2025-09-10 04:42:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3f1f0a09-cddb-34cd-83ce-3e4aa1058de9 | -7.37506 | -47.43619 | 2025-09-10 04:42:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 2cfc83e8-acd7-3974-9c14-6c1cd17aceaa | -6.85134 | -44.89359 | 2025-09-10 04:42:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8d77af37-b08b-3cb3-9394-e44eebb38c6d | -11.45488 | -49.2823 | 2025-09-10 04:42:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3642f0dc-3966-32ca-8394-f9c6232411ed | -6.33773 | -47.0978 | 2025-09-10 04:42:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 289df4e0-a3ba-3dc5-bd80-346885ebdc1e | -10.27351 | -48.8218 | 2025-09-10 04:42:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d47fc1e5-c78b-3f6a-8b3c-5c1f3a941ca0 | -9.08219 | -47.06301 | 2025-09-10 04:42:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| abfe5d7f-24f5-39cd-af51-d22e1c1d6fc0 | -9.71291 | -46.82515 | 2025-09-10 04:42:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 95f6cfdc-65ba-3887-9841-bcaf585a473d | -7.0826 | -43.8812 | 2025-09-10 04:42:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| edeada75-2e5b-3786-b158-e1d0ad208505 | -6.41309 | -44.44363 | 2025-09-10 04:42:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 538cc8ae-4382-353a-b276-5c2a8fc67431 | -9.17753 | -51.81811 | 2025-09-10 04:42:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0cf66850-9d65-32e3-a45d-ba6673ab339b | -11.39403 | -43.53606 | 2025-09-10 04:42:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3feb7d49-8957-3e05-9b4f-6cc9de7a1f11 | -6.83164 | -44.89048 | 2025-09-10 04:42:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5253362f-40da-3fb8-92b1-85f45d073e62 | -8.85058 | -47.26659 | 2025-09-10 04:42:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4ae83388-276d-331c-9532-7162315683d9 | -6.93549 | -43.91533 | 2025-09-10 04:42:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9763941c-bcc9-34c6-ac32-d476bef6403e | -9.087 | -47.05534 | 2025-09-10 04:42:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| e960f401-3985-3882-bfbe-585b44e5cba1 | -7.72633 | -50.35532 | 2025-09-10 04:42:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 83f687c4-f391-3cb4-ac4b-890f872aedaf | -6.85793 | -47.92463 | 2025-09-10 04:42:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1cebc060-3db4-3236-a25e-531b67d73de5 | -7.76842 | -46.07283 | 2025-09-10 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d40c207c-29b4-3a8b-8ac7-79bf4d08e213 | -7.79273 | -46.06316 | 2025-09-10 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e4446d99-bdbe-3d13-acba-3e6227c18e28 | -11.11737 | -48.44848 | 2025-09-10 04:42:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ba64297c-2e04-3be7-9a19-fb6571eff9c2 | -9.14509 | -45.5664 | 2025-09-10 04:42:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5153685e-f4e1-382a-96b5-db36e89d4a34 | -6.33833 | -47.09397 | 2025-09-10 04:42:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c2517bad-019a-3b6b-98ee-b7c21587ca50 | -9.06097 | -50.47606 | 2025-09-10 04:42:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3367530c-814f-3e43-b079-fb69f32905e0 | -11.1633 | -48.35453 | 2025-09-10 04:42:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c58128cc-fc8a-3098-b4e9-69d4dc47d471 | -11.47118 | -49.26629 | 2025-09-10 04:42:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ab26b22b-44e7-35fd-bf60-56209961cd93 | -7.70655 | -45.15313 | 2025-09-10 04:42:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1c4d01bf-6f5d-38ba-9348-679a1d41c0cd | -10.30938 | -48.81569 | 2025-09-10 04:42:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ca7b7152-4886-37cc-b793-652ea704958b | -9.21825 | -50.52639 | 2025-09-10 04:42:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d2fc28e8-a851-3804-89b1-c60fcbff0435 | -10.65113 | -48.61026 | 2025-09-10 04:42:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6b03f76a-6080-3509-aac7-4ee86cb4d5ec | -11.1372 | -46.34867 | 2025-09-10 04:42:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 69bc2974-a6f0-354a-b4ef-f63da20d58eb | -8.51892 | -45.70932 | 2025-09-10 04:42:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 054dce20-0a4c-3486-8616-1dc0cfa4b8f0 | -6.09455 | -47.22519 | 2025-09-10 04:42:00 | NPP-375D | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 099f2b27-7fca-3420-bb0d-60f021123a8e | -8.03568 | -47.27656 | 2025-09-10 04:42:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 65228724-6aec-32a7-acd9-c972515fefee | -9.21433 | -50.55098 | 2025-09-10 04:42:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aa1d498b-9adb-3bd7-9f08-6e4c1516df41 | -10.72127 | -48.28069 | 2025-09-10 04:42:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 437f5ccc-0846-3264-bea8-90249d216979 | -8.32911 | -44.86776 | 2025-09-10 04:42:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cb7acb9c-3eb7-3cbf-948c-72d1b710f7ac | -8.04528 | -48.70064 | 2025-09-10 04:42:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c5567abf-0a1d-3b6f-b9b9-524d04866efe | -6.84828 | -47.91945 | 2025-09-10 04:42:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7e4910d5-e85b-3fde-b48a-597e22e585ff | -10.14308 | -46.1834 | 2025-09-10 04:42:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 61c49126-4e15-38b0-9f7c-a16a32e7f7dc | -8.06365 | -48.65936 | 2025-09-10 04:42:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3d5fa142-6d5b-3d83-afcc-38af1bbbf186 | -10.02505 | -51.67908 | 2025-09-10 04:42:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ed7c8c8f-76e5-3570-aada-76485976ccb9 | -5.42097 | -51.53576 | 2025-09-10 04:42:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0d88d364-07c0-3057-a0fa-b6a85737d819 | -6.85225 | -47.93871 | 2025-09-10 04:42:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 974df034-bb6d-3ecf-9c08-7bb41bb15561 | -9.01126 | -46.05178 | 2025-09-10 04:42:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5cfe4c4e-665a-3030-ac0b-aa4437f0d2c2 | -9.07329 | -46.97394 | 2025-09-10 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a4a89f75-1fe1-399f-8be2-ebf3b9263261 | -8.06727 | -50.19093 | 2025-09-10 04:42:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 35534a47-7704-3afd-9ff1-491122c71b4d | -9.0144 | -49.54646 | 2025-09-10 04:42:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5bb4c7e1-214c-31d9-8578-f19b73581849 | -7.78863 | -46.1014 | 2025-09-10 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b826cc71-8b6d-3e47-a6bf-758ccc2d96b6 | -8.42787 | -49.12289 | 2025-09-10 04:42:00 | NPP-375D | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fb0a5d7f-c556-3514-9716-ac022409277b | -8.48975 | -44.64495 | 2025-09-10 04:42:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4c4422de-05d8-3a5b-be6b-1c14ef2f849c | -9.31525 | -46.71743 | 2025-09-10 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 5c936189-3938-3013-b430-6f133e6069c4 | -9.03086 | -49.7895 | 2025-09-10 04:42:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 17e4384d-542b-3ab2-aff9-339c5440aedf | -7.86112 | -46.25064 | 2025-09-10 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cc106682-f5d9-3dba-83d4-27657bb508dd | -11.11906 | -48.43718 | 2025-09-10 04:42:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7ff3644f-9337-3526-9f9e-94c8d7c9e821 | -6.39345 | -44.43713 | 2025-09-10 04:42:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0d5ce3b9-6145-33e2-9290-725aaaad67b2 | -6.41545 | -44.40059 | 2025-09-10 04:42:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 96f848bf-9271-30c9-93eb-f58ff5a77c2d | -9.07122 | -50.47052 | 2025-09-10 04:42:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 809df71a-83bf-3068-8c9a-ce909211fcfc | -10.08924 | -48.1762 | 2025-09-10 04:42:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a67b37ac-3359-350b-8472-779a559f79b4 | -8.05808 | -48.67308 | 2025-09-10 04:42:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5503e211-b898-32e5-a271-2b40b4af4aa9 | -7.37335 | -47.43674 | 2025-09-10 04:42:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3b6d20d4-fa17-3b8c-b35b-5fe507228d7c | -11.11008 | -48.45901 | 2025-09-10 04:42:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2d750a17-6c32-3868-9ee0-50aa73848291 | -7.07538 | -44.86293 | 2025-09-10 04:42:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cf7e9339-d846-3c3e-a166-4d4f639955f0 | -11.46367 | -43.63979 | 2025-09-10 04:42:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a16b0b96-32e8-3e35-ac4d-fb90dd841e29 | -9.99657 | -51.7044 | 2025-09-10 04:42:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 18b52565-3c1b-3323-a974-937521b29806 | -8.52134 | -51.38745 | 2025-09-10 04:42:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 77c69e90-7ed6-39df-9613-a47be0321cf9 | -9.04875 | -50.48847 | 2025-09-10 04:42:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8eb71dd8-5e68-3b1e-8432-f966bee9ed6e | -9.60473 | -48.0418 | 2025-09-10 04:42:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| c9027bb3-1120-3b5c-8a80-98439f4938e2 | -7.78429 | -46.09364 | 2025-09-10 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 76fd9c80-5274-3862-98d3-e92a1bb72dc5 | -7.25232 | -44.45243 | 2025-09-10 04:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9412ef9e-6089-3250-b5e3-d793f167ea7a | -11.57406 | -44.66244 | 2025-09-10 04:42:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c4d4dd0c-dc7e-34b7-a60a-d16f4eb4ee5c | -11.48602 | -48.54961 | 2025-09-10 04:42:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4b2a32b1-255e-36a9-9940-420ffb13ba40 | -8.05655 | -52.329 | 2025-09-10 04:42:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8ad71d64-9dfa-37a4-93c9-b75acc0bf467 | -8.26125 | -49.92841 | 2025-09-10 04:42:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8142acf1-6d51-3b93-a188-a9227c969231 | -9.07146 | -46.9864 | 2025-09-10 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 468d299d-f6a3-3c8b-8582-6b6fc503a776 | -10.55755 | -51.49747 | 2025-09-10 04:42:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c079f1d4-9548-3cc6-93e2-37560586ed9f | -6.85225 | -47.91631 | 2025-09-10 04:42:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 399f6c25-6c33-3147-b4b3-91964c8373e8 | -8.00078 | -46.33067 | 2025-09-10 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 39f492cc-a902-3409-80e5-0dc7a67e676e | -8.24231 | -47.85921 | 2025-09-10 04:42:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a64ef636-13a4-32b3-8540-b12d7b562d1f | -8.0706 | -50.19145 | 2025-09-10 04:42:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 756539d7-547b-3b13-a6a2-0d4ab0f8d407 | -7.88661 | -46.2702 | 2025-09-10 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 55c8c556-69a5-311f-a3b6-81368af7e516 | -10.9724 | -46.80002 | 2025-09-10 04:42:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 26b7795d-d882-3207-a3a3-109f0d27d033 | -9.05764 | -50.47552 | 2025-09-10 04:42:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b892bf20-1495-36c1-85b0-947566e94a0c | -11.13377 | -52.01442 | 2025-09-10 04:42:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 73d1c578-0a79-3ebd-9fac-2c3d437d1661 | -7.55642 | -48.25785 | 2025-09-10 04:42:00 | NPP-375D | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4f1714c4-f319-3313-8bba-1c45aaa5ffb3 | -6.65414 | -44.54988 | 2025-09-10 04:42:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bb33f151-7483-32ab-a470-ed5ce2d27b3d | -6.38997 | -44.43278 | 2025-09-10 04:42:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f16e5b20-644e-3e5e-8ea5-6de92a68f4f7 | -11.8168 | -46.75928 | 2025-09-10 04:42:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ba745f3a-a8b3-3423-b484-859d48a6b055 | -11.46137 | -43.6282 | 2025-09-10 04:42:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 53ee1f34-8cb2-3d12-872b-7a8acea35576 | -8.06524 | -48.62668 | 2025-09-10 04:42:00 | NPP-375D | COLINAS DO TOCANTINS | TOCANTINS | Brasil | 1705508 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c051c5cf-9721-30ea-bd67-9781aab21a69 | -9.31094 | -46.7276 | 2025-09-10 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| b27a18ab-d1aa-3b3c-81e1-279317203877 | -11.34111 | -46.53597 | 2025-09-10 04:42:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |


[Clique aqui para ver as próximas entradas](README64.md)

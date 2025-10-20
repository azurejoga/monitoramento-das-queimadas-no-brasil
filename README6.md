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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4f0b64cf-2472-3134-9e3c-ae139a8c1b12 | -1.43931 | -48.89096 | 2025-10-20 03:49:00 | NPP-375D | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4a656189-9001-3ff7-a946-14f995613b26 | -1.44397 | -48.897 | 2025-10-20 03:49:00 | NPP-375D | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 46d68e6f-5887-3ee0-b963-6324d8fb3c0a | -2.9323 | -39.86523 | 2025-10-20 03:49:00 | NPP-375D | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 3.6 |
| de913cef-9b57-36a3-b83b-749f381ac56d | -2.94338 | -39.82077 | 2025-10-20 03:49:00 | NPP-375D | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| a2049fb7-db1b-3e38-8f7f-6afc1f00aff3 | -1.44504 | -48.89067 | 2025-10-20 03:49:00 | NPP-375D | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 887f320e-3105-3726-868f-6ae91feef311 | -1.44623 | -48.89215 | 2025-10-20 03:49:00 | NPP-375D | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ce7dc2b4-7912-32dd-81c3-44ae8047c683 | -4.8409 | -42.7465 | 2025-10-20 03:50:00 | GOES-19 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 39361831-506f-3b9f-9712-90a8b8610340 | -7.1334 | -44.2402 | 2025-10-20 03:50:00 | GOES-19 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 63.7 |
| ae4e87aa-b8e7-3106-b47a-1fac0f00fb94 | -9.553 | -40.3503 | 2025-10-20 03:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 89.1 |
| dafa40d0-cb01-3da6-818d-65fef6429323 | -2.2527 | -51.9313 | 2025-10-20 03:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 0a35a8b8-21e9-3a88-a3d3-074c4ca76d24 | -9.5534 | -40.3254 | 2025-10-20 03:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 93.9 |
| 96e7d16a-52f0-3524-b0b4-2766375a18f0 | -8.4345 | -44.1324 | 2025-10-20 03:50:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 70.2 |
| cecb9e9a-a114-3fbe-a103-2323688c8256 | -9.5725 | -40.3227 | 2025-10-20 03:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 176.0 |
| 1b0fbf56-1394-3cf3-9b2d-02f2c24e0e24 | -9.5721 | -40.3475 | 2025-10-20 03:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 131.4 |
| 47f641ca-d29f-341d-a3ce-d60db0fe33e8 | -2.2527 | -51.9108 | 2025-10-20 03:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 103.4 |
| 0efa0c8b-cb08-3a17-b782-dfff695c7b7c | -6.1066 | -44.0246 | 2025-10-20 03:51:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f8555afa-2623-3e80-8433-48322b09acad | -6.87754 | -43.59145 | 2025-10-20 03:51:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| a618a102-be9e-3409-a004-c2f66b2a1d10 | -8.33939 | -39.74442 | 2025-10-20 03:51:00 | NPP-375D | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 878b16b8-8d8f-343e-98cd-bff57e3772a8 | -5.54372 | -41.34724 | 2025-10-20 03:51:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| bbe5b0bc-0069-3b9b-b114-74d08e6308c8 | -7.13752 | -44.24549 | 2025-10-20 03:51:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d4fbcea3-58c6-3ab6-800a-c15287181d4c | -7.54363 | -46.08792 | 2025-10-20 03:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ad2569e1-3ce3-39d4-be73-55594ff1eb89 | -6.9757 | -43.99622 | 2025-10-20 03:51:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 98abc5c6-2100-303a-aacb-1df105962589 | -6.88657 | -43.59288 | 2025-10-20 03:51:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 1e6d5f5d-a036-3c50-900e-dde92cb5218b | -5.08607 | -42.75484 | 2025-10-20 03:51:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6fb7e3e6-614e-368b-b668-811f0391c6be | -8.0743 | -48.02488 | 2025-10-20 03:51:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 740d0446-4ef1-35ff-8d6e-0d0ff486eea8 | -4.82622 | -42.74817 | 2025-10-20 03:51:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d1f772aa-696c-31c0-80fa-63a765b87b7e | -4.48491 | -45.30554 | 2025-10-20 03:51:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d32a46a0-5847-3e5d-b506-316d7afa5f3d | -5.29838 | -44.45245 | 2025-10-20 03:51:00 | NPP-375D | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f643f94e-c704-366c-a5ea-6ecc263a73d1 | -6.89109 | -43.59364 | 2025-10-20 03:51:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 30be2238-d832-3c33-a3b0-820b659de9f2 | -9.76602 | -41.92221 | 2025-10-20 03:51:00 | NPP-375D | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 2ab7b4ad-de94-3deb-8f17-fd2ac390b782 | -7.53834 | -46.08701 | 2025-10-20 03:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 80d85691-b22e-3e86-8ce0-7737f3eceb45 | -7.13191 | -44.24981 | 2025-10-20 03:51:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| feecf42a-f04d-3346-ba8f-d8797fbc8a9f | -7.4177 | -40.07013 | 2025-10-20 03:51:00 | NPP-375D | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 8d7f8239-d30b-3846-b462-26f9b08e0481 | -11.09397 | -39.81311 | 2025-10-20 03:51:00 | NPP-375D | QUEIMADAS | BAHIA | Brasil | 2925808 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 4388389b-cd3f-32bf-84e7-de0a0ce8b354 | -3.58802 | -41.6577 | 2025-10-20 03:51:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5f53d296-fa58-3423-8752-71ca5c2c9494 | -4.83133 | -42.74474 | 2025-10-20 03:51:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 625a9834-dc0e-3b53-845d-c84df775bc8b | -5.6244 | -43.64849 | 2025-10-20 03:51:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1119a300-d06d-3df0-897b-7c221ac1b611 | -6.20612 | -41.53744 | 2025-10-20 03:51:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 0536a4ce-1495-3c58-85b2-789fff1d9a39 | -5.36663 | -45.51509 | 2025-10-20 03:51:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fc9c9a39-4cd1-3851-96ec-4c6e54e38b83 | -9.57384 | -40.33656 | 2025-10-20 03:51:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 108.5 |
| 9de88752-bbd3-32a1-a74c-4214e48709b6 | -4.85979 | -45.11861 | 2025-10-20 03:51:00 | NPP-375D | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 847d48f7-6d10-3aae-912c-fcf6dde6b090 | -6.88128 | -43.59669 | 2025-10-20 03:51:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 8e2c16c0-d495-34c4-bb4b-82f0adab9af0 | -3.5891 | -41.65722 | 2025-10-20 03:51:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 1d58c0e3-50a8-3bb4-a3f6-9089cc83287a | -4.39653 | -43.31905 | 2025-10-20 03:51:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| c857b6ff-e610-3977-9f12-d734a6e8ec89 | -7.41872 | -40.06927 | 2025-10-20 03:51:00 | NPP-375D | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 65dbf5be-e85e-38a8-a93e-bd9c7f882964 | -5.99803 | -42.79169 | 2025-10-20 03:51:00 | NPP-375D | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 6556b7c0-1598-377f-ab04-1eb5f5af3295 | -5.16365 | -46.00126 | 2025-10-20 03:51:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0e530b23-84c7-321d-8601-059bc34846bb | -5.65234 | -46.81562 | 2025-10-20 03:51:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2f62c0a6-7edc-3939-9034-ace226a626c4 | -5.33763 | -42.93824 | 2025-10-20 03:51:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d1831d72-3944-3c50-8aa2-6bacd8c0633d | -9.46765 | -41.03656 | 2025-10-20 03:51:00 | NPP-375D | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 76d83fb9-d8ee-3f11-86af-b6a95153e48a | -4.48445 | -45.30244 | 2025-10-20 03:51:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 37a363b6-5ea0-3757-a162-c822e85da10a | -9.57028 | -40.33596 | 2025-10-20 03:51:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 108.5 |
| b4a616f3-8915-318a-b6ba-134a3fad3ad8 | -4.49754 | -43.66948 | 2025-10-20 03:51:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 43a2adfd-f943-32af-9a26-5e01f3000838 | -10.52264 | -43.35862 | 2025-10-20 03:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cb6d047b-9ddd-3e7e-bc0b-b6c5f9cacf9c | -4.39707 | -43.32209 | 2025-10-20 03:51:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 50bd2852-eb41-3aa1-a2c6-cd1716aa4679 | -6.50197 | -39.72075 | 2025-10-20 03:51:00 | NPP-375D | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 7bb88bf4-209a-3fb6-80a3-c8c6f8fdfef2 | -4.83645 | -42.74126 | 2025-10-20 03:51:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| fdf6939b-ac03-3d00-92a4-05b74ee2c980 | -5.38038 | -43.1582 | 2025-10-20 03:51:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d4c687b2-0f4e-3fa1-8548-c9d54f82a968 | -6.46459 | -43.7303 | 2025-10-20 03:51:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a75879ea-c328-3558-94d7-fd76d46cb43d | -7.12807 | -44.2442 | 2025-10-20 03:51:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| f6b62671-2a15-3148-b287-f97c513eee69 | -6.8858 | -43.59742 | 2025-10-20 03:51:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 8486c3e4-0f14-327a-a1d1-0a8f970a0732 | -6.23778 | -44.14852 | 2025-10-20 03:51:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 932edb73-8f89-3368-9670-20743f33653d | -7.13279 | -44.24487 | 2025-10-20 03:51:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 525cee6f-5df6-3b84-9702-0ded72801605 | -6.0941 | -44.01848 | 2025-10-20 03:51:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c897988b-4d7a-3f22-bfe4-123da30f8042 | -6.32162 | -35.07582 | 2025-10-20 03:51:00 | NPP-375D | VILA FLOR | RIO GRANDE DO NORTE | Brasil | 2415008 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 14ef03c6-a76b-3eab-a4aa-0d96d8092fb9 | -7.07122 | -45.21725 | 2025-10-20 03:51:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d310ee75-9703-3355-87ec-7dd987b9f800 | -7.13691 | -44.24269 | 2025-10-20 03:51:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 83d6cf01-a47e-3239-bcb8-2e068d8bffe7 | -4.42084 | -43.89155 | 2025-10-20 03:51:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fa804b97-dedc-3481-b0d6-2219d3a7b0e4 | -6.21471 | -40.97451 | 2025-10-20 03:51:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| fd5142f8-fccd-3161-8b30-2d80357b1bc2 | -4.47964 | -45.30456 | 2025-10-20 03:51:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 05737819-fcb7-3e19-aa02-b572bb6ff561 | -7.11238 | -39.43555 | 2025-10-20 03:51:00 | NPP-375D | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 85eb66c8-32ce-3233-a0ac-f432110d87f8 | -6.21247 | -40.96434 | 2025-10-20 03:51:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 795550a2-e4b3-39c5-8c32-4ba5ddbbb91b | -4.39785 | -43.31731 | 2025-10-20 03:51:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 51e066de-a131-3c6e-b1b3-2b72fd95221a | -8.47157 | -39.50732 | 2025-10-20 03:51:00 | NPP-375D | CABROBÓ | PERNAMBUCO | Brasil | 2603009 | 26 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 79dfbe39-2730-3e1d-a9c1-03e4007fbecf | -6.88425 | -43.60643 | 2025-10-20 03:51:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| af143155-1daf-32ad-80b7-b2a1c79ce871 | -6.13705 | -41.80833 | 2025-10-20 03:51:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 5bbda5f2-f46e-3a84-b053-8cd1a41eaef3 | -4.94403 | -41.56007 | 2025-10-20 03:51:00 | NPP-375D | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3fc440e1-6f77-39e3-b7e5-26b2aaf1cf75 | -9.57095 | -40.33192 | 2025-10-20 03:51:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 24.5 |
| a566208f-b14e-3e2b-9e39-cdc59c1e44cb | -4.87338 | -43.32742 | 2025-10-20 03:51:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4eae9d44-ae11-37fd-a6a8-e03fe48b9b58 | -5.10609 | -43.19749 | 2025-10-20 03:51:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 119e6186-57e3-3fe5-8824-d24736f06e64 | -5.61974 | -43.65577 | 2025-10-20 03:51:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8454930a-50ab-3581-a831-c7fedc14415c | -9.56672 | -40.33535 | 2025-10-20 03:51:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 41.3 |
| c668c4f9-25fd-3dd0-aa0e-47f936942eec | -10.15385 | -42.21132 | 2025-10-20 03:51:00 | NPP-375D | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 4467a6f0-58c3-31a3-9c49-3b3e6e33542c | -6.34597 | -41.55465 | 2025-10-20 03:51:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 83cc03af-b2f1-3f04-ae22-011fef19d65b | -5.36197 | -45.51065 | 2025-10-20 03:51:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f8199ff9-e148-3773-ad79-2a727ec70400 | -7.06586 | -46.20186 | 2025-10-20 03:51:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c0aeb3ed-35d2-3dfa-a9ac-a0f1fb0735a3 | -6.55659 | -41.66166 | 2025-10-20 03:51:00 | NPP-375D | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 1222d1e4-945d-3e34-81e4-71a477102f9f | -5.08668 | -45.89158 | 2025-10-20 03:51:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1c1021f3-db07-32d8-a4f9-e8717b893edb | -7.65852 | -44.73837 | 2025-10-20 03:51:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d7e96321-c163-39f0-8573-fd248bc9e652 | -4.56702 | -43.7813 | 2025-10-20 03:51:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dc5a9a63-a334-32d8-a6cb-8f459d5297e3 | -7.65314 | -46.86362 | 2025-10-20 03:51:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aa05dd99-53ee-3c2b-8f7a-3a7973c991ed | -5.16428 | -45.99764 | 2025-10-20 03:51:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b82a04b6-ad81-3874-86f6-c94497512e4f | -6.88954 | -43.60265 | 2025-10-20 03:51:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7f20a09b-824a-3471-93c5-5b94f8a398cb | -5.28806 | -41.20448 | 2025-10-20 03:51:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9a2f3b60-3c65-3798-b53d-cbc3b51dc846 | -7.99755 | -39.62712 | 2025-10-20 03:51:00 | NPP-375D | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 74c5b812-ab9d-36a6-b5e3-46686b14b347 | -9.56605 | -40.33941 | 2025-10-20 03:51:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 41.3 |
| 9d4d69bf-6e48-30e6-8e9a-d3a769d68e43 | -7.06654 | -46.19806 | 2025-10-20 03:51:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d0c2e442-a83c-3e02-892a-7a2a61780a88 | -4.84305 | -43.02948 | 2025-10-20 03:51:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 54391c96-9a53-320b-9db1-10bf67c6a82c | -8.06921 | -48.01941 | 2025-10-20 03:51:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cb65fa81-cadc-3565-b25c-e5113ae61d05 | -5.09201 | -45.89313 | 2025-10-20 03:51:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README7.md)

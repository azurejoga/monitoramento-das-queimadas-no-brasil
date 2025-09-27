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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cc30f169-8b43-3173-9132-f7e7d29eb59e | -6.48726 | -45.90769 | 2025-09-27 04:21:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e0aeb325-4aad-38e4-9885-3ff165060476 | -7.60592 | -43.95804 | 2025-09-27 04:21:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cc566d94-fc87-3957-b670-839d145c648c | -6.98473 | -42.39428 | 2025-09-27 04:21:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f2f41ce9-bd53-3c9f-ae35-6e71a0219c2e | -5.80306 | -42.44573 | 2025-09-27 04:21:00 | NPP-375D | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 308a44b9-bcce-3791-8d0c-12f12fc6a2f1 | -4.63777 | -46.33591 | 2025-09-27 04:21:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4b88ce0a-90b0-3639-a4d0-574d2aa94bb6 | -3.52244 | -41.15429 | 2025-09-27 04:21:00 | NPP-375D | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 2d07c7c4-0755-3b3c-9c17-8b21f7d17ae2 | -6.19987 | -44.24284 | 2025-09-27 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8bd03b7e-abb1-3d13-8c30-2eae3ed02b62 | -4.32999 | -48.39227 | 2025-09-27 04:21:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5556fe5c-5802-3f20-bd4e-0810a4024cc9 | -6.45959 | -44.05425 | 2025-09-27 04:21:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9ad938cb-1cff-3183-96fb-8a8643db50fb | -3.80214 | -41.56606 | 2025-09-27 04:21:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a29b56b9-590e-3f9f-9444-e9f05cae18b6 | -5.03772 | -42.54725 | 2025-09-27 04:21:00 | NPP-375D | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| dd4bad40-f693-3c4f-b685-6a6c19ca81c0 | -5.97248 | -44.11752 | 2025-09-27 04:21:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b0c1306c-66db-3dd7-bac6-2e9df96ca9c6 | -4.9715 | -43.19491 | 2025-09-27 04:21:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ce8fe9ce-876c-3458-a6d8-cc7e8fe04743 | -6.98357 | -44.85049 | 2025-09-27 04:21:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3093174a-9c2b-31f2-8c5f-b696667b78de | -5.31385 | -42.76919 | 2025-09-27 04:21:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| fd7ca59a-74de-3335-bf8c-69bb5e4e3d09 | -7.20005 | -44.52493 | 2025-09-27 04:21:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1301aed3-953c-3229-be00-f6f043b62b12 | -5.49122 | -43.06482 | 2025-09-27 04:21:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ff5b3a68-6472-3695-9b76-aa9fd7bf0c6a | -3.59716 | -48.99021 | 2025-09-27 04:21:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9c06d685-c942-37d3-b068-8fcb21e21a41 | -5.08439 | -44.85655 | 2025-09-27 04:21:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9ad29c55-50c9-32d5-b9ad-c58d9f8b5e43 | -6.21927 | -47.32792 | 2025-09-27 04:21:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b8b8b451-3a48-3c87-b556-10c338225f23 | -6.36513 | -43.34243 | 2025-09-27 04:21:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0dbaaa3c-c949-3032-9137-8aa907c57b1d | -7.05143 | -46.41894 | 2025-09-27 04:21:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2fb410f5-4c43-35ff-b74c-006d10c633fa | -5.18933 | -43.72327 | 2025-09-27 04:21:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2c2761bb-a3ee-323a-b31d-3b06d9e84eba | -5.48785 | -43.08649 | 2025-09-27 04:21:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 196842e5-bf8b-36cd-b535-d8aca7b3b76d | -5.5387 | -42.7357 | 2025-09-27 04:21:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f4c3536d-2ddf-3dfa-8630-ea5042b83687 | -6.13091 | -43.45681 | 2025-09-27 04:21:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4aada014-bab9-3226-a13b-0194cf6b5f76 | -6.81279 | -44.47449 | 2025-09-27 04:21:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d6a23957-c49f-386b-8e24-b9fc507a7771 | -5.21613 | -50.95189 | 2025-09-27 04:21:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ee956d5c-5893-3873-916e-b4b7350508c5 | -6.9941 | -44.84859 | 2025-09-27 04:21:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4fc89a12-aa89-350d-91f9-503df0a68980 | -6.33753 | -43.36386 | 2025-09-27 04:21:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9fe38fe6-dbee-323e-93b7-36044dd16023 | -4.74113 | -44.61386 | 2025-09-27 04:21:00 | NPP-375D | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e9994b8d-a143-3736-8386-b6ba6e7b57a7 | -4.69873 | -40.48642 | 2025-09-27 04:21:00 | NPP-375D | NOVA RUSSAS | CEARÁ | Brasil | 2309300 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9777ad6b-07f9-337f-a825-1075b2e1ec08 | -5.22346 | -44.49099 | 2025-09-27 04:21:00 | NPP-375D | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a3ea0f7a-8574-359d-9c9d-7791a62c8e80 | -4.61279 | -43.10695 | 2025-09-27 04:21:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 1d5ba67f-d086-3ca2-9f1e-8797cb8613fe | -7.17247 | -42.22824 | 2025-09-27 04:21:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 787fb10d-00a4-3cdd-b562-3253e49b789e | -4.26413 | -48.55239 | 2025-09-27 04:21:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8368082b-82a3-37a4-abae-053594d1b3b7 | -5.24338 | -43.0674 | 2025-09-27 04:21:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9d8f383c-7b06-3351-a220-0b23bfa4422e | -6.62956 | -43.82487 | 2025-09-27 04:21:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e3a122bb-2387-39ce-a501-c670631f3cdc | -6.11013 | -43.90601 | 2025-09-27 04:21:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b304dfeb-5713-3b9d-9824-8e7509d7824a | -6.74838 | -44.71014 | 2025-09-27 04:21:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7da46826-688d-31eb-8a08-c6ad4ed3566c | -4.34763 | -43.01504 | 2025-09-27 04:21:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a35e5910-de7c-37d0-a704-9b95b0163537 | -4.71417 | -40.68603 | 2025-09-27 04:21:00 | NPP-375D | ARARENDÁ | CEARÁ | Brasil | 2301257 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 1529ac54-9081-35c0-89e7-7212070c3ec1 | -5.82322 | -41.29069 | 2025-09-27 04:21:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b235bca2-cfa7-3878-a92e-538651a286aa | -5.86126 | -47.26963 | 2025-09-27 04:21:00 | NPP-375D | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b1ef3c34-e3f0-377e-964a-99de1b525c51 | -4.48058 | -47.67423 | 2025-09-27 04:21:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4b56fb86-150a-3199-8308-dcfab8685f8a | -3.72574 | -39.64931 | 2025-09-27 04:21:00 | NPP-375D | ITAPAJÉ | CEARÁ | Brasil | 2306306 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 04a58188-c6f3-3f51-9bd1-93a334e5321c | -6.57765 | -45.10343 | 2025-09-27 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6fd61bf0-2bb5-3f9a-b89f-d304cc0213a9 | -7.62694 | -43.84457 | 2025-09-27 04:21:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 798aa5ea-2657-3677-9499-bb4ea0caef4e | -3.23918 | -46.8023 | 2025-09-27 04:21:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7f2e754e-673c-3d11-b422-2a6453dd3c8c | -6.93058 | -44.64618 | 2025-09-27 04:21:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b62acf7a-9070-381c-a11a-85a4ac7e7fea | -5.47202 | -43.07667 | 2025-09-27 04:21:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 671dadfd-5bdd-38ea-9a90-8df52819c045 | -5.00234 | -42.73024 | 2025-09-27 04:21:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2d58cb5d-829f-3874-91ed-0ebbedc99079 | -6.0777 | -44.06958 | 2025-09-27 04:21:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4be21f05-6f57-332c-a608-2578441b7684 | -6.31672 | -43.38633 | 2025-09-27 04:21:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4d80d9f2-6c81-37f1-8fcc-3a582e83905a | -5.30604 | -47.22461 | 2025-09-27 04:21:00 | NPP-375D | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 11f06af1-3583-328e-b9be-d50d837f0a55 | -7.26592 | -42.97834 | 2025-09-27 04:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b9868cba-e0eb-31c0-8d20-2b8865731d09 | -5.49948 | -42.19436 | 2025-09-27 04:21:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| be03a155-1132-3b17-8d85-885557a8fcac | -3.92426 | -40.75518 | 2025-09-27 04:21:00 | NPP-375D | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f99a44f6-8fe0-3c11-a77b-3772368ae4ef | -5.31442 | -42.76555 | 2025-09-27 04:21:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 9fd4b434-53a9-388d-875d-a329a8b8c4ce | -3.40119 | -46.90221 | 2025-09-27 04:21:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4536b21c-7fe8-30f8-bd91-c379bd03994c | -6.49572 | -43.64804 | 2025-09-27 04:21:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7da44a94-7cca-3448-b7bd-7e6ec0c6a960 | -3.80506 | -41.57054 | 2025-09-27 04:21:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 9.3 |
| ab9adf87-d52a-3d47-98c4-15f521a0379c | -6.49332 | -43.28385 | 2025-09-27 04:21:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 84788a88-3487-3cd3-a2fa-5183af7e5b23 | -6.70637 | -42.75675 | 2025-09-27 04:21:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 633f702b-1e48-3e00-8039-1d9fca5bfd80 | -7.00587 | -46.99976 | 2025-09-27 04:21:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3905962e-f81c-31b1-823e-17a429d3941c | -3.15968 | -48.60454 | 2025-09-27 04:21:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ea39dc81-1f2e-3521-9bcf-021032db3a65 | -5.12079 | -42.68787 | 2025-09-27 04:21:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 513eba84-1ea7-3757-81b9-02653a6763c4 | -7.2619 | -42.98154 | 2025-09-27 04:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| c140b3e5-8945-39d2-881b-1de6c2662953 | -4.7868 | -45.34392 | 2025-09-27 04:21:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 79223249-982e-3daa-8612-cbd20868cce8 | -7.18517 | -41.70769 | 2025-09-27 04:21:00 | NPP-375D | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c49a5393-1fd7-3ebf-8b29-82dc76c9b170 | -4.70483 | -46.48172 | 2025-09-27 04:21:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 48509480-0761-34fd-ad71-6ab2b7547e64 | -4.77669 | -41.05291 | 2025-09-27 04:21:00 | NPP-375D | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 3.8 |
| c611248c-afc1-398d-a9b4-99c683707858 | -4.70905 | -40.41836 | 2025-09-27 04:21:00 | NPP-375D | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5ce60049-799e-34ee-94a9-633f42c1786a | -3.45377 | -39.04084 | 2025-09-27 04:21:00 | NPP-375D | PARACURU | CEARÁ | Brasil | 2310209 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 24744c72-7aca-3444-b488-7709a27cd28b | -3.58992 | -43.09748 | 2025-09-27 04:21:00 | NPP-375D | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 383b875a-b962-3fbc-9f94-fbbb08d7b4e3 | -6.70464 | -42.7449 | 2025-09-27 04:21:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 462e8db2-b1f7-36f2-950f-9881bdf6ba14 | -6.54058 | -43.83242 | 2025-09-27 04:21:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8c4ce67d-dcf0-3076-a662-afeb671d246e | -3.29686 | -42.18226 | 2025-09-27 04:21:00 | NPP-375D | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| eeabe0d0-321f-3488-af8d-12c4219af15f | -4.61053 | -43.09929 | 2025-09-27 04:21:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 89237f72-c989-3462-863f-1a120c5330a3 | -5.36668 | -42.28794 | 2025-09-27 04:21:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 350c75d4-4299-393c-a903-9b5c069d2c80 | -7.62413 | -43.84044 | 2025-09-27 04:21:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d9cabdfb-9db0-3b03-b767-7b1e20a8a83d | -5.74127 | -44.98151 | 2025-09-27 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 97d70d94-430b-31d8-97f4-9caa88354ec7 | -6.99937 | -42.39257 | 2025-09-27 04:21:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| a5ccdbc4-5adf-3b49-b84b-b68d44ef9834 | -4.48385 | -40.7812 | 2025-09-27 04:21:00 | NPP-375D | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| fe0b1e31-1d9e-36eb-88b7-ba57e74a779c | -5.0855 | -44.84961 | 2025-09-27 04:21:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ab1dbf84-bc8b-3c47-b6d1-aaef7043709c | -4.57887 | -44.07702 | 2025-09-27 04:21:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e9cd724a-ecd8-3b0e-8221-0971f904d49e | -6.49203 | -43.28769 | 2025-09-27 04:21:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 098f5d7a-5db5-330a-a0b3-d6ea84ddf049 | -6.42729 | -43.07632 | 2025-09-27 04:21:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6c674759-5a11-3583-b863-ce5034a89723 | -5.07718 | -44.85897 | 2025-09-27 04:21:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| f4964c48-5b37-3171-9081-cf492c892d58 | -5.37421 | -42.28522 | 2025-09-27 04:21:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 8ea93534-6a93-3099-a06d-8e32a4237d64 | -5.27949 | -45.03358 | 2025-09-27 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e8fc0521-0458-3be6-856f-3ff763e5054d | -5.31024 | -47.22124 | 2025-09-27 04:21:00 | NPP-375D | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3b123372-8831-3512-a1e3-6fdd003615f2 | -7.28773 | -42.97408 | 2025-09-27 04:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 7f11bd8a-387c-35fa-929c-d70adbdbef3f | -5.26313 | -43.49361 | 2025-09-27 04:21:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 002a916b-a05f-3c90-b40a-579a248e53cc | -5.77759 | -45.34897 | 2025-09-27 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a7e6edbe-2f4a-325a-82ec-3bc107397b3b | -6.13653 | -43.465 | 2025-09-27 04:21:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 099afa9b-c441-3ff8-9989-380f903f4709 | -6.22862 | -44.19028 | 2025-09-27 04:21:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 161d95f8-2b36-3891-b485-8b99d2fe7a37 | -5.26368 | -43.49007 | 2025-09-27 04:21:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| aa8322a3-451a-35dc-94aa-a7fb6ba41e5b | -6.15817 | -43.99253 | 2025-09-27 04:21:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a9147fef-46b1-3754-ad63-6eca211802cf | -5.53813 | -42.7394 | 2025-09-27 04:21:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |


[Clique aqui para ver as próximas entradas](README30.md)

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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a418f2d9-fca4-38e8-a755-435cb729cc6a | -5.34581 | -43.75144 | 2025-10-15 03:47:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 86e90ef0-ebc6-3fb9-9605-39168c5c2be7 | -5.39708 | -44.03988 | 2025-10-15 03:47:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5e604616-44c9-36c4-bc13-bac8bd112982 | -6.45693 | -44.58998 | 2025-10-15 03:47:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 711e4557-356e-3c5d-a84e-dcfdecf1135e | -5.46994 | -44.64818 | 2025-10-15 03:47:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| deb1ccdf-3e03-37ec-92c1-48497d06923a | -4.54481 | -45.4214 | 2025-10-15 03:47:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9c9af6a2-bc43-333a-97e5-7ebe994fadbf | -5.85836 | -43.86385 | 2025-10-15 03:47:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5a817386-cd94-38cb-b8e2-23d20931b37e | -5.86582 | -43.85202 | 2025-10-15 03:47:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1e7c1653-ec3a-3f6d-a2c0-35845dd0e0a1 | -10.84282 | -42.75961 | 2025-10-15 03:47:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 2c7e7826-97d3-314e-ac47-d9ecf473822b | -4.91601 | -46.70682 | 2025-10-15 03:47:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3b0e8f14-0f16-31bd-84dd-80b17d23a802 | -5.59067 | -42.84264 | 2025-10-15 03:47:00 | NPP-375D | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 6d3e4cb2-e018-39d1-9dcf-68388e539085 | -5.5679 | -41.31172 | 2025-10-15 03:47:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| d7d0c1fc-20a2-3c81-9727-16ee19163c4d | -5.2457 | -44.47738 | 2025-10-15 03:47:00 | NPP-375D | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1769fd8a-1ef7-3159-9ee9-9570f2ec4bb4 | -8.73104 | -43.86073 | 2025-10-15 03:47:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0bd747fe-0a17-3c64-832e-ab26f19bf0b9 | -7.17333 | -42.20711 | 2025-10-15 03:47:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| c784101a-4749-3766-819f-eb0503244338 | -5.89912 | -38.15379 | 2025-10-15 03:47:00 | NPP-375D | IRACEMA | CEARÁ | Brasil | 2306009 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ae763215-8d7f-3b12-9a96-666960b84902 | -6.98922 | -38.44651 | 2025-10-15 03:47:00 | NPP-375D | SÃO JOSÉ DE PIRANHAS | PARAÍBA | Brasil | 2514503 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f7d762a7-1bbb-3048-a813-71b80ca0dcf3 | -5.42949 | -44.42868 | 2025-10-15 03:47:00 | NPP-375D | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9a9b9d41-1d21-3628-bd53-363ad58111d8 | -4.8235 | -45.45221 | 2025-10-15 03:47:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 09376562-9ba3-3105-9a89-8398e10c0d78 | -5.39838 | -44.04299 | 2025-10-15 03:47:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5f8ce0d3-fb36-3ca6-ac62-e5a4921e0cde | -6.89901 | -43.96415 | 2025-10-15 03:47:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4d1ba064-8767-3672-b99a-7a039df05750 | -4.77323 | -45.73291 | 2025-10-15 03:47:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 0e6ab9df-eadd-3d53-944f-2d5e1d4b70c4 | -7.1601 | -42.49419 | 2025-10-15 03:47:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 77a39b59-d4db-35c0-b9b9-f853206e1756 | -8.28693 | -43.44002 | 2025-10-15 03:47:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 6afe143d-5b39-3e28-8d0e-b4d455cdb1ed | -5.58353 | -44.74461 | 2025-10-15 03:47:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| acb395c5-1687-3701-a444-fb379dfaacd9 | -5.57021 | -41.32469 | 2025-10-15 03:47:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8c07813a-0572-3150-b800-30a55d3ed71f | -5.42967 | -44.23088 | 2025-10-15 03:47:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 07b32564-61bf-35c9-ae75-9ff55f4280b8 | -5.86406 | -43.86196 | 2025-10-15 03:47:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f88d37f7-9dec-352f-a319-a13b267ed613 | -7.57166 | -42.70381 | 2025-10-15 03:47:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 69d964b6-6c31-3b65-bb89-c8c8572c1c9c | -6.91099 | -38.2621 | 2025-10-15 03:47:00 | NPP-375D | NAZAREZINHO | PARAÍBA | Brasil | 2510006 | 25 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 27fd27b2-933e-32c8-b112-4e83655eb40d | -4.90867 | -46.71137 | 2025-10-15 03:47:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7b1ea928-1877-37e0-8d82-3b3b889b4b07 | -6.07124 | -44.30843 | 2025-10-15 03:47:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3f53b281-741b-337f-9551-57aaf042209b | -8.18478 | -44.04111 | 2025-10-15 03:47:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 27c04b2b-ba68-3786-a19c-cddf4e9d4914 | -7.5663 | -43.83627 | 2025-10-15 03:47:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e9f27ef6-6862-3bd0-b39c-158e1a76a5f9 | -10.80864 | -43.94935 | 2025-10-15 03:47:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e58e2c64-18e5-3472-828b-905e96b4dd7b | -8.21001 | -44.01744 | 2025-10-15 03:47:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 88d1b0ba-aa2b-33db-8835-199c272d2a64 | -6.22496 | -44.15977 | 2025-10-15 03:47:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 00c28c32-8e39-3472-bbb6-fc76a51c99c9 | -5.42011 | -44.22216 | 2025-10-15 03:47:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 5633a04a-ac5e-3dd5-90f6-198da8362a16 | -5.25913 | -45.61363 | 2025-10-15 03:47:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2c2e53b1-8559-30c7-838a-0b527ee92f17 | -4.59877 | -47.03547 | 2025-10-15 03:47:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3c1fdae3-6794-348a-b308-881b820f0dbd | -5.59831 | -46.24921 | 2025-10-15 03:47:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d9508c13-5218-30e5-a5f8-84a6b02fbe70 | -6.45745 | -41.84424 | 2025-10-15 03:47:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 213e8b63-cecd-343f-9ebb-8271b5861221 | -5.42068 | -44.21884 | 2025-10-15 03:47:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| c423b90f-bf0d-3a49-b7d1-6b54799e35b2 | -5.58702 | -44.74789 | 2025-10-15 03:47:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cb499873-abcf-335d-b325-97e146814ff0 | -7.50162 | -46.64518 | 2025-10-15 03:47:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9882f79f-0131-38b3-866b-dc953a1b9e2a | -10.82998 | -43.96228 | 2025-10-15 03:47:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 26e05354-1827-3828-a896-a7e99b8ba063 | -8.21399 | -44.02425 | 2025-10-15 03:47:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9efd7f1a-204d-3b68-954a-1d564c3d9f16 | -11.49761 | -42.3946 | 2025-10-15 03:47:00 | NPP-375D | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 4a8be7ce-b320-376e-a4d1-a26e4b2059a2 | -4.66312 | -43.12259 | 2025-10-15 03:47:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 4bc42a12-bb3e-337b-8b1e-4a93a7bc4973 | -8.20765 | -44.0018 | 2025-10-15 03:47:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 55bd3ea5-35ba-3c3f-a3cd-6ac78ad75116 | -6.13911 | -41.75744 | 2025-10-15 03:47:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 7f04c01a-366b-3d96-bbb3-00e41f7aabe2 | -8.45771 | -44.18578 | 2025-10-15 03:47:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 61791be7-a416-3c1a-a443-4d555ae1d555 | -7.94792 | -44.14473 | 2025-10-15 03:47:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b3463987-0867-3e9b-be13-e13145aca564 | -5.39895 | -44.03962 | 2025-10-15 03:47:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 32f32d18-7e85-3f7e-94ba-61bbf2526783 | -8.24692 | -43.3835 | 2025-10-15 03:47:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 792ec08c-fbea-33d2-8b99-4aa00b9ea26b | -7.55046 | -42.71505 | 2025-10-15 03:47:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 014f731c-b715-3c58-a9e4-778cbab87117 | -4.89747 | -43.45599 | 2025-10-15 03:47:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| bc802792-9da3-35ac-b211-89aa50d91efe | -5.9269 | -42.82288 | 2025-10-15 03:47:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 67d950e6-390e-3da7-9bb4-0294c65ebf42 | -8.28206 | -43.43922 | 2025-10-15 03:47:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4b3d1aef-1460-347f-8b34-781639d37e0d | -6.58686 | -41.50888 | 2025-10-15 03:47:00 | NPP-375D | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 354e0936-27d5-3c21-9a93-0c78da049e17 | -5.42407 | -44.42762 | 2025-10-15 03:47:00 | NPP-375D | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 63bc8b8a-9b21-3878-be09-d87abe3ca6fa | -6.45152 | -44.58907 | 2025-10-15 03:47:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 18f51942-8d24-39a7-9c43-846654cbd9dd | -5.87496 | -43.86097 | 2025-10-15 03:47:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 5f0fdcae-227d-3f6d-890b-21f6db3fe5d8 | -7.56126 | -43.89499 | 2025-10-15 03:47:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b853d606-c526-3ec9-931c-4a247928c11e | -10.81277 | -43.94786 | 2025-10-15 03:47:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2af64a64-e22e-302e-9fa3-82ba0e61f623 | -5.38868 | -43.22001 | 2025-10-15 03:47:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 41793244-3e6a-3056-ba62-0392f6f56465 | -4.76646 | -45.73626 | 2025-10-15 03:47:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 19829296-721e-3734-aa28-57a2d09cbe86 | -6.22141 | -42.50048 | 2025-10-15 03:47:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| be5a07b3-2dcb-38d8-b720-ea472504e71f | -8.2188 | -43.31811 | 2025-10-15 03:47:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| ba42d8e9-a0a9-300b-8227-62782a185564 | -5.95207 | -38.63097 | 2025-10-15 03:47:00 | NPP-375D | JAGUARIBE | CEARÁ | Brasil | 2306900 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f9adf1b8-b885-39ab-958b-e67b8c2a5f20 | -7.95143 | -44.13816 | 2025-10-15 03:47:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0ff77ae2-7bee-3dbc-8238-a350d2ceae3b | -5.88889 | -43.75201 | 2025-10-15 03:47:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| f1dc5442-bb43-378e-80ab-0ae6354d2a90 | -4.89125 | -43.46137 | 2025-10-15 03:47:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 00bf2099-60f3-32de-b2aa-d00de9b8af43 | -10.81757 | -43.94877 | 2025-10-15 03:47:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 27e03e99-bbf4-3d09-84f5-7b9ea3543b4f | -5.27639 | -41.04453 | 2025-10-15 03:47:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 3d7e2c43-b68f-3ec6-abf3-b4d01879da5d | -8.214 | -43.31715 | 2025-10-15 03:47:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a17ba6ad-f601-3213-9dfd-3e7ffd6dca32 | -4.85847 | -43.20778 | 2025-10-15 03:47:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d78c1112-558a-31f8-903a-2dc733966424 | -5.95147 | -43.75924 | 2025-10-15 03:47:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0cec87c3-cfba-3867-ab67-3bedc983f68c | -7.48363 | -42.15169 | 2025-10-15 03:47:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| b0eb105d-098f-3364-983f-5ecd75d3eeef | -5.7941 | -43.89161 | 2025-10-15 03:47:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6faf7851-8be9-3cef-8502-f7c6a7829a33 | -7.9444 | -44.1347 | 2025-10-15 03:47:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0af26cc9-41c5-3309-9ccf-a59bec92ae49 | -6.89228 | -43.97229 | 2025-10-15 03:47:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1fcd7df2-ae73-3063-9035-c614bcbc95c8 | -5.58771 | -44.74406 | 2025-10-15 03:47:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8d1a5f23-fd34-3f0f-a23f-f7c33a69b77f | -5.34749 | -43.74213 | 2025-10-15 03:47:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2312d592-c53f-396b-954a-31c80b105f59 | -7.57036 | -42.68324 | 2025-10-15 03:47:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 391c566e-32a8-3f8a-ad46-45df403a9c5b | -8.22006 | -44.07724 | 2025-10-15 03:47:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6ef5e84d-4840-38cb-b9fe-a0d0fc2451a6 | -11.50119 | -42.39936 | 2025-10-15 03:47:00 | NPP-375D | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 69cec08c-fd5c-3b61-9ccb-4ed0060500b1 | -5.56662 | -42.99224 | 2025-10-15 03:47:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 00511d47-0ded-3a1f-8f9b-38c17a1b8487 | -5.34643 | -43.74844 | 2025-10-15 03:47:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cd132827-f7f0-32c9-8c84-fcfb5c6a19c2 | -7.56581 | -43.89886 | 2025-10-15 03:47:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 06176f3b-41b4-308d-8899-6e9e545f3974 | -4.42086 | -47.7589 | 2025-10-15 03:47:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 0aee4f35-0f3f-3ac4-80b0-8c7b601f4cc3 | -8.25258 | -43.35175 | 2025-10-15 03:47:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 2b3918b2-164f-3a58-80c3-97af0d5e5263 | -5.99687 | -44.08564 | 2025-10-15 03:47:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d68a74b5-1c92-3d44-982d-52366dc09496 | -10.5161 | -43.3711 | 2025-10-15 03:47:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2162f6d8-e95b-3e09-8fd3-8e39395ca9b8 | -5.952 | -43.75616 | 2025-10-15 03:47:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8e0cef51-da1a-3e2b-8a19-051b4eec7d92 | -5.94927 | -42.31714 | 2025-10-15 03:47:00 | NPP-375D | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| df84d273-67d2-3673-b318-dd517079ee82 | -5.90488 | -42.83505 | 2025-10-15 03:47:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 0cf19c62-25cb-3319-bd19-d51ab493bac0 | -4.89178 | -43.45825 | 2025-10-15 03:47:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 182ea41c-8ada-34a6-af0f-3ffd62a39ccf | -4.83476 | -42.77336 | 2025-10-15 03:47:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 22249c94-8027-39fc-b02e-0c64e5f0cd93 | -4.64598 | -43.1317 | 2025-10-15 03:47:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 67b96d88-f79d-3e0f-9639-a6ad4cba90af | -5.54374 | -41.32071 | 2025-10-15 03:47:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |


[Clique aqui para ver as próximas entradas](README19.md)

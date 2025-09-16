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

## Dados Diários - Página 87

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e4474175-1d80-374a-8f19-6134493ddd3b | -8.60348 | -46.42495 | 2025-09-16 11:57:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 61.4 |
| c040dd9c-2afc-34ce-9483-f3162816ecc1 | -5.63031 | -39.02552 | 2025-09-16 11:57:00 | TERRA_M-M | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 9.8 |
| f5597361-1ae3-3416-8fd2-8199e2112dda | -8.90961 | -46.15568 | 2025-09-16 11:57:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 804f724c-b06d-385f-b183-ede2d967e237 | -6.40368 | -42.65947 | 2025-09-16 11:57:00 | TERRA_M-M | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 23.4 |
| 92b6d2b2-47af-3c5d-8f1d-b071d2eb0c96 | -10.71163 | -46.49493 | 2025-09-16 11:57:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 45af9f2a-50d7-30da-81d8-316db2160211 | -8.58802 | -46.37962 | 2025-09-16 11:57:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 40.3 |
| bb5dca54-d1ad-3557-b5e3-5b85b34e7773 | -7.68023 | -44.66776 | 2025-09-16 11:57:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 6f76aaf1-f713-362e-82bb-936c03272032 | -7.98076 | -45.66547 | 2025-09-16 11:57:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 2bb6e62a-3fb4-3056-a83e-be022bfcb9b4 | -7.97652 | -43.93182 | 2025-09-16 11:57:00 | TERRA_M-M | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 29.8 |
| 09057bea-8f3c-3c91-9fcf-6c193e451ce6 | -8.11456 | -37.58823 | 2025-09-16 11:57:00 | TERRA_M-M | CUSTÓDIA | PERNAMBUCO | Brasil | 2605103 | 26 | 33 | nan | nan | nan | Caatinga | 13.5 |
| 45570bcb-1e61-37dc-9e08-7dd768fd3394 | -6.45491 | -43.31642 | 2025-09-16 11:57:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| a0b6dadb-221e-3abe-bf16-705fd8a8a769 | -8.60567 | -46.41043 | 2025-09-16 11:57:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 05de993b-56f0-3a37-a8f9-4580840e2622 | -8.95845 | -45.8778 | 2025-09-16 11:57:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 2990eeb4-4856-3526-a952-2e287c768983 | -4.52587 | -42.06033 | 2025-09-16 11:57:00 | TERRA_M-M | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 81d85fa8-8f96-33f2-aadb-8dd5f42d14b9 | -8.02173 | -45.65168 | 2025-09-16 11:57:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 55.5 |
| e988df49-a4be-39d0-9e3d-00b081706d57 | -7.98003 | -45.64552 | 2025-09-16 11:57:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 9373171c-621f-3586-b86a-d5aec9c71d6a | -7.15729 | -47.98858 | 2025-09-16 11:57:00 | TERRA_M-M | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 33be63ab-6600-301d-af74-e25abe3634f4 | -9.53603 | -45.53399 | 2025-09-16 11:57:00 | TERRA_M-M | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 38.5 |
| ce2ad640-9af5-3fcb-97ea-be0f865d8b1f | -7.8123 | -46.1247 | 2025-09-16 11:57:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 749bbf9c-177f-3439-9de6-661f8f76beb5 | -9.06468 | -47.01877 | 2025-09-16 11:57:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 27.0 |
| 479f919c-902a-3b06-9930-744fe35b7128 | -8.67062 | -46.3695 | 2025-09-16 11:57:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 59af5f14-7cf0-3b7d-8e18-6e8b72c6b091 | -7.67738 | -44.47138 | 2025-09-16 11:57:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 6428a2af-e14d-3a00-91a9-13b01e0bda90 | -9.10425 | -44.86263 | 2025-09-16 11:57:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 31.4 |
| d1a6a607-fe9a-3e43-8337-4c3446c51351 | -6.42725 | -43.31238 | 2025-09-16 11:57:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 766e4670-5f85-37c3-a4a4-238a31f38f36 | -9.17418 | -46.98256 | 2025-09-16 11:57:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 26.9 |
| a2a7ae2d-d96b-3245-b3e5-528b0634ebc5 | -4.59135 | -43.31653 | 2025-09-16 11:57:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 27.7 |
| c75ea182-b51f-323e-80ed-63307dc69b8b | -7.69198 | -44.50643 | 2025-09-16 11:57:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 24.8 |
| ba841748-5c59-3f4f-a7de-e958a212c9b1 | -6.75557 | -48.12537 | 2025-09-16 11:57:00 | TERRA_M-M | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 109.6 |
| dc70f484-4db1-3cd5-aa55-d8161212af13 | -8.96786 | -46.02333 | 2025-09-16 11:57:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 58.8 |
| cfe12c8a-30d8-3ddb-b692-ec07da05eddc | -10.55448 | -46.3565 | 2025-09-16 11:57:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 74e5d8c5-32a5-3e6e-9c62-48ffc4c281bc | -9.75871 | -40.06755 | 2025-09-16 11:57:00 | TERRA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 11.5 |
| d8efba6a-f19d-37cd-b5aa-ab2a285545ab | -7.04502 | -44.1187 | 2025-09-16 11:57:00 | TERRA_M-M | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| fb452caf-cfa6-34e3-88c2-41adaff44f83 | -9.76944 | -40.05883 | 2025-09-16 11:57:00 | TERRA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 12.8 |
| eceb870a-3960-3b79-a077-9b9f990212fb | -5.49116 | -39.43456 | 2025-09-16 11:57:00 | TERRA_M-M | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 20.4 |
| a4eec41c-dd5a-3d14-b109-e98e20c3fc62 | -8.88428 | -46.17846 | 2025-09-16 11:57:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 41.1 |
| 3c75d530-2b31-3870-b95c-dc34351145ad | -7.69553 | -44.50262 | 2025-09-16 11:57:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 42.2 |
| d8cdfd5a-7a83-38de-9a68-4bfe7a94606f | -7.31583 | -43.96614 | 2025-09-16 11:57:00 | TERRA_M-M | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 21.5 |
| db05427d-0bcc-3aa5-aa4f-024b65012857 | -10.72422 | -46.51714 | 2025-09-16 11:57:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 24.2 |
| 1bb453f8-0c95-3f05-8d5b-23e428fee915 | -9.10262 | -44.87359 | 2025-09-16 11:57:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 0d64fbfd-55a9-36fb-807b-761da0735c0d | -5.80455 | -43.47992 | 2025-09-16 11:57:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 7a4b2372-7b13-345c-8b0f-2315dccdac48 | -6.70804 | -45.5211 | 2025-09-16 11:57:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 12b5e97a-762d-3154-987d-2e1145fd840a | -4.75097 | -42.60466 | 2025-09-16 11:57:00 | TERRA_M-M | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 9ad8aaef-95aa-3b35-ae60-72bf77af3f6f | -5.78959 | -43.94432 | 2025-09-16 11:57:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 672d0ddd-1df2-3f3e-8d24-64f8d3181e11 | -7.13974 | -40.94679 | 2025-09-16 11:57:00 | TERRA_M-M | VILA NOVA DO PIAUÍ | PIAUÍ | Brasil | 2211605 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 39bddbb6-a2d2-344e-94d6-a885d3f22afa | -6.6342 | -44.73561 | 2025-09-16 11:57:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 633c97bc-b2eb-3044-8587-926c77016aab | -9.49507 | -40.64298 | 2025-09-16 11:57:00 | TERRA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 085f4ce2-7b49-3adf-a52d-6be68b4df8d0 | -8.01981 | -45.66422 | 2025-09-16 11:57:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 383.1 |
| 6dda40c0-fac2-34c7-a712-9942d3cf059e | -6.96605 | -44.44488 | 2025-09-16 11:57:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 1df58ee2-8a77-39bf-9d24-53918b529893 | -3.82893 | -44.11041 | 2025-09-16 11:57:00 | TERRA_M-M | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| aa488b8f-dd5b-3d68-8d2e-cd35b0ed4793 | -7.16618 | -44.34338 | 2025-09-16 11:57:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 1b7c7915-686e-3af2-8337-28feae335448 | -8.13961 | -44.46271 | 2025-09-16 11:57:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 42c18a87-b5a7-3eb6-a9ec-683e5dc8f411 | -7.69357 | -44.49569 | 2025-09-16 11:57:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 40557103-953f-3b8b-84f9-80829d403b4d | -10.7051 | -46.50064 | 2025-09-16 11:57:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 38.0 |
| cb407181-c57c-3e67-80e0-eb83e667f1ad | -6.06821 | -44.68591 | 2025-09-16 11:57:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 15.4 |
| f58ba9c3-4906-3dea-93fe-91355c98f5a4 | -5.96032 | -42.72507 | 2025-09-16 11:57:00 | TERRA_M-M | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| c4e3baeb-4f1e-3562-b35e-3b8cd2d3ae32 | -8.9633 | -45.87185 | 2025-09-16 11:57:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 8896f214-e613-3917-825d-877b0f166f66 | -10.66088 | -46.472 | 2025-09-16 11:57:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 22cc9c9b-e132-38f1-8333-2865ec0d9984 | -6.36524 | -44.41331 | 2025-09-16 11:57:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| e93eb66d-8f06-3ec6-a302-b91fc6120ce7 | -4.6037 | -43.29779 | 2025-09-16 11:57:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 45.9 |
| ea9459bc-39c6-36d9-aade-011045020f88 | -8.5944 | -46.33788 | 2025-09-16 11:57:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 38.9 |
| 17117c16-bd72-333b-b388-a4ffb8ce97c0 | -4.59928 | -43.32791 | 2025-09-16 11:57:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 9fab57d5-d682-3cb7-8ec1-0e8da6e87cef | -8.60959 | -46.40295 | 2025-09-16 11:57:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 33.1 |
| c27e9290-56d3-3809-8db5-8d51c2636146 | -10.72637 | -46.50367 | 2025-09-16 11:57:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 40.0 |
| 2399474c-1c0f-32d3-93ad-d23f08c90299 | -7.69 | -44.6693 | 2025-09-16 11:57:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 25dbb8ad-3672-3a5c-be3c-ec1f6af4d871 | -10.66297 | -46.45871 | 2025-09-16 11:57:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 15.8 |
| e20f97e2-5151-3136-bc22-f7274378f8d9 | -10.70959 | -46.50823 | 2025-09-16 11:57:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 20.4 |
| e401e54f-0874-3d0a-9d02-493f216a7a5d | -8.72684 | -46.67609 | 2025-09-16 11:57:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 39.9 |
| 3d0fe159-dba1-3168-ac29-a8ab68601d5f | -11.02485 | -45.06149 | 2025-09-16 11:57:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 6c7e92af-7ad2-3d2c-b31a-329810996fab | -7.9845 | -45.64046 | 2025-09-16 11:57:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 131.9 |
| ef65eee1-c985-3e65-af61-d64ef4febd15 | -6.07826 | -44.68727 | 2025-09-16 11:57:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 38.8 |
| 0242d950-e81d-3534-aa2d-f5abf76117e3 | -7.14457 | -47.98648 | 2025-09-16 11:57:00 | TERRA_M-M | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 57.5 |
| c71c71c7-8f60-3823-977b-87103d51bb50 | -7.16389 | -44.33667 | 2025-09-16 11:57:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 41ef9967-b3eb-3bbf-888e-e73f72ce5fec | -6.92125 | -44.80383 | 2025-09-16 11:57:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 9d58d099-9089-336a-9073-6d71649d2aac | -8.00741 | -45.67542 | 2025-09-16 11:57:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 168.3 |
| 10499e76-ae97-3095-ac72-957fbf287bd3 | -4.60223 | -43.30781 | 2025-09-16 11:57:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 150.0 |
| dcb837ed-26dc-3446-9855-ce41d5828594 | -9.04938 | -44.83132 | 2025-09-16 11:57:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 27.0 |
| 77a5eedb-4825-3872-88d5-fc7cdf0ae1c1 | -8.66185 | -46.35418 | 2025-09-16 11:57:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 35.8 |
| e0b77f4c-0fac-3553-bb72-d9a9ca04bff7 | -3.83061 | -44.09901 | 2025-09-16 11:57:00 | TERRA_M-M | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| ad34ade7-8e6b-3668-8ece-b6287af068f2 | -8.60736 | -46.41702 | 2025-09-16 11:57:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 92.2 |
| e139535e-35bb-3869-8f9d-e36833619019 | -3.81456 | -41.56291 | 2025-09-16 11:57:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 71798a30-f0c8-32b2-bdb8-647ef664ea9d | -8.96586 | -46.03614 | 2025-09-16 11:57:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 43.9 |
| 480fcf4c-8935-3e0f-9800-9aa3be360f04 | -3.84058 | -44.10041 | 2025-09-16 11:57:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 32e87890-4a3e-3fb2-a58f-406f1ebb0aae | -7.52314 | -39.06855 | 2025-09-16 11:57:00 | TERRA_M-M | PORTEIRAS | CEARÁ | Brasil | 2311108 | 23 | 33 | nan | nan | nan | Caatinga | 21.0 |
| bfc78f36-bc5a-31fd-b22e-6bdd95954560 | -8.9154 | -46.1498 | 2025-09-16 11:57:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 8fa6e99e-0d3d-3584-9e77-8255dbcf8a28 | -7.27763 | -46.59433 | 2025-09-16 11:57:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 767789f5-302e-367d-b191-24e4508b951d | -9.17661 | -46.96738 | 2025-09-16 11:57:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 40.3 |
| d2b76d3e-d2cc-3ae9-9aed-83cef4114e21 | -6.96309 | -44.44898 | 2025-09-16 11:57:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 3bd89ba4-f8fa-3884-9f2a-13cee21db09e | -7.81005 | -46.11763 | 2025-09-16 11:57:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 8c66bf38-b860-30c3-bfca-9412890c8171 | -7.06906 | -44.15401 | 2025-09-16 11:57:00 | TERRA_M-M | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 12f72a5f-486f-3c19-a5d4-24c0aad7fd1e | -9.06409 | -47.02848 | 2025-09-16 11:57:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 865fcfaf-e282-3360-ad57-123add84840c | -7.99885 | -45.66167 | 2025-09-16 11:57:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 25.4 |
| a543cb88-95a6-3122-bad9-06da66195ff1 | -8.6815 | -46.37114 | 2025-09-16 11:57:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 924d536d-3d0a-3b7f-ba15-e61c22d12daa | -7.31738 | -43.95586 | 2025-09-16 11:57:00 | TERRA_M-M | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 689a820e-3b9e-3e30-a13f-568e7eb696a9 | -6.34856 | -43.15757 | 2025-09-16 11:57:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 20.6 |
| fc2b0c96-b4a9-3d3e-891c-f0fb99c4ad9f | -7.69514 | -44.48499 | 2025-09-16 11:57:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 25c99209-97e3-3825-9d8b-a32ebd8f9ce5 | -6.49877 | -38.87232 | 2025-09-16 11:57:00 | TERRA_M-M | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 12.6 |
| 5b41836d-373b-3123-b363-3fcb295c5a6f | -7.14391 | -47.99347 | 2025-09-16 11:57:00 | TERRA_M-M | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 49.0 |
| 4558f6d1-19d0-3d93-b07d-2b43db40eaa0 | -8.93199 | -45.52564 | 2025-09-16 11:57:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 27.1 |
| 405347db-66a8-3e70-8c2a-351080c33a1e | -3.84226 | -44.089 | 2025-09-16 11:57:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 59226e82-2069-3748-8a9f-d16e182f858a | -7.71667 | -45.30276 | 2025-09-16 11:57:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 12.7 |


[Clique aqui para ver as próximas entradas](README88.md)

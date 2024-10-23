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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3696ff54-9803-3899-82d6-61654fb6a7db | -10.99623 | -45.26389 | 2024-10-23 04:00:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1a040ca8-f9f6-32fe-858f-7878d0ba07cb | -6.25013 | -45.8398 | 2024-10-23 04:00:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c3935ae1-5995-3860-8d7a-cd70c6e9d71f | -6.09365 | -46.1295 | 2024-10-23 04:00:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 862559f6-b6b9-39e4-9f97-b003b3ea10c0 | -6.09295 | -46.13373 | 2024-10-23 04:00:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 185e273c-f7c8-3a03-ad1d-b751da038d25 | -5.76342 | -45.55928 | 2024-10-23 04:00:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 182630e3-1f9b-3f44-aca6-83ea191f9784 | -5.76277 | -45.56325 | 2024-10-23 04:00:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d38eeacd-ebae-34e2-bc6f-124272215dbb | -5.7592 | -45.55857 | 2024-10-23 04:00:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 182ee234-7185-3a0f-ac66-23bdf0af2a62 | -5.75855 | -45.56252 | 2024-10-23 04:00:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ab3d5595-1f0c-3cf2-a888-97b8378460c0 | -5.67037 | -45.80251 | 2024-10-23 04:00:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0debf23e-8d6c-30e6-b4b4-8dc342312fd8 | -5.30862 | -45.47723 | 2024-10-23 04:00:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 95da9c6a-dd04-37ea-af01-fa76776c903c | -5.27781 | -45.90446 | 2024-10-23 04:00:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7b9fb4d6-2d3b-35d1-9cac-278a184ff7f3 | -5.24349 | -45.86854 | 2024-10-23 04:00:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 78e541c2-0a3d-35bd-b8fd-6060b3fc421c | -5.22066 | -45.9247 | 2024-10-23 04:00:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d0dfce70-8794-33b3-b332-fbe743fbd7c3 | -5.84501 | -46.24001 | 2024-10-23 04:00:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 371433c9-04f3-341b-8bb1-d23d85a95fa0 | -5.64046 | -46.48233 | 2024-10-23 04:00:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a6c473f2-30f7-30cc-ae65-27fc778d7e8c | -5.45447 | -46.3565 | 2024-10-23 04:00:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5dadc9f5-eec5-3b26-8e4c-37d46c3ef3f5 | -5.44059 | -46.28717 | 2024-10-23 04:00:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f57427f9-0ad2-320b-bda5-bca2be73d8ad | -5.4384 | -46.28925 | 2024-10-23 04:00:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b5ac6a54-c66c-394d-b022-4a152df6b1fe | -5.27346 | -46.17319 | 2024-10-23 04:00:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c1b6df74-8693-3307-b09c-347c8bbdcac3 | -5.27271 | -46.17761 | 2024-10-23 04:00:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6e1220c9-73be-36aa-ad7f-deff05f14a39 | -5.22615 | -46.16366 | 2024-10-23 04:00:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c3c6844c-2701-364a-bec3-080d193960d5 | -5.22242 | -46.1586 | 2024-10-23 04:00:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6d21682e-d636-3ed7-b6f4-d046e0c5bd73 | -5.2217 | -46.16296 | 2024-10-23 04:00:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 50d7eb66-c039-36c4-8855-d4c138ba1d82 | -5.16251 | -46.1352 | 2024-10-23 04:00:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5d322e6b-240d-37bd-ac1b-7b57270676bf | -5.15807 | -46.13451 | 2024-10-23 04:00:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ef7eabc5-c534-38cb-a05e-f6a43615546a | -5.14352 | -46.17406 | 2024-10-23 04:00:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 06fc075d-5513-3c1c-adf9-bce091f40945 | -5.14246 | -46.17252 | 2024-10-23 04:00:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d60d1e49-2b49-31a3-a0ee-e56c532d5d63 | -5.36544 | -45.08383 | 2024-10-23 04:00:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fd2fe65b-d635-32d8-ad6d-374f0e455b2e | -5.36481 | -45.08763 | 2024-10-23 04:00:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 237e04ba-f82e-3fe9-a4bc-e4a1eb0aa68b | -5.36132 | -45.08313 | 2024-10-23 04:00:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 33e71436-5775-3493-b0ac-d7204a2d6ec3 | -5.36069 | -45.08695 | 2024-10-23 04:00:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6c43c15e-81b5-3727-bb57-43b7d208de3e | -5.3546 | -45.04746 | 2024-10-23 04:00:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9d9dddcb-2685-387c-acc5-5e5663e67d77 | -5.31345 | -44.86845 | 2024-10-23 04:00:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 21cc3240-687d-3368-b9fd-afcd33deea2f | -5.3094 | -44.86773 | 2024-10-23 04:00:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 509edd3a-8b4c-3f86-b15d-ba7bc8b9e0ff | -7.82003 | -45.45731 | 2024-10-23 04:00:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d6cfb1a8-09ee-3d7a-9b19-1eb2e0a19038 | -7.42495 | -46.6159 | 2024-10-23 04:00:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2952e781-93f8-3f4b-80bf-9e8a39e57dac | -7.42422 | -46.62021 | 2024-10-23 04:00:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d22b451f-1cdd-3b5d-b33c-e542eea5c771 | -7.41981 | -46.61939 | 2024-10-23 04:00:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 76e0cd49-427d-310d-974f-463ac2cf3287 | -7.41908 | -46.62371 | 2024-10-23 04:00:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 98198be2-0b60-3cbc-9fd2-d3c8917f6b35 | -7.40928 | -45.56967 | 2024-10-23 04:00:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0256f1ab-c99c-3a1f-9c9d-e28f6fcb8bad | -7.40867 | -45.57338 | 2024-10-23 04:00:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b69a49b2-686c-30d8-891a-3c3b955dbd2e | -7.40739 | -45.57223 | 2024-10-23 04:00:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 82f341c6-4c26-30c2-8b0f-766cf24b6278 | -7.39928 | -45.9449 | 2024-10-23 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 62e9a79e-e80b-396b-bfd7-9a9189bfcdfe | -7.37349 | -45.55584 | 2024-10-23 04:00:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0b7e5190-6edb-3865-906c-b84d34f8c781 | -7.19669 | -45.41602 | 2024-10-23 04:00:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 652c3c63-d38c-3c10-ac45-4066217f0ce5 | -7.14272 | -45.4366 | 2024-10-23 04:00:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f8937c9c-dad2-3071-9892-21071c2705d6 | -7.1174 | -46.14476 | 2024-10-23 04:00:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5b0a8f64-3ed4-36d1-bb12-a272ea8fed80 | -7.11669 | -46.1489 | 2024-10-23 04:00:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8e170bda-2a9a-3dbc-88a9-dc47f68e0347 | -7.04787 | -46.44299 | 2024-10-23 04:00:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 42e8e0ec-3340-3c87-9479-fd6607eca57f | -7.04756 | -46.44421 | 2024-10-23 04:00:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cd3fb633-52d9-336d-8cca-82b61aae967c | -7.04349 | -46.44224 | 2024-10-23 04:00:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 74ec2bab-c220-35ef-beea-4a3f46e2a969 | -7.04317 | -46.44345 | 2024-10-23 04:00:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cab09a9f-ea3e-3523-b62c-a28e18257c0c | -7.00342 | -46.70946 | 2024-10-23 04:00:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| be051a48-071c-38d5-a79d-37fe517f14b0 | -7.00171 | -46.70758 | 2024-10-23 04:00:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0eeea7ac-45dd-397d-a257-c7200ad00ef7 | -7.00092 | -46.71207 | 2024-10-23 04:00:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f71094b1-f48f-3fda-b93e-271ea11f5203 | -6.99894 | -46.70869 | 2024-10-23 04:00:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 709f0a39-f287-31af-b699-ba7463b9fa2f | -6.70363 | -46.07858 | 2024-10-23 04:00:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3e1c5c00-b154-3a89-92fb-bba8e73d3e6a | -6.67578 | -46.37343 | 2024-10-23 04:00:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 69715c8c-6302-3de6-a57a-3265ac000adf | -8.51381 | -45.8741 | 2024-10-23 04:00:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8c600b60-d57d-3afc-845a-180634322ad8 | -8.51318 | -45.87781 | 2024-10-23 04:00:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 9b678bb0-cbc8-3f4a-8109-1503f42c1a20 | -8.50966 | -45.87352 | 2024-10-23 04:00:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c2da2a83-b58b-3b6a-af1a-dac930f51f68 | -8.50904 | -45.87721 | 2024-10-23 04:00:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b20a3b2f-009c-3479-94f2-74e388208047 | -8.5084 | -45.88095 | 2024-10-23 04:00:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bf8ebdde-9646-317f-8fe6-3b6030199954 | -8.39456 | -46.62537 | 2024-10-23 04:00:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ab5f34fb-f1d9-3e67-98d7-0895b851690d | -5.00294 | -46.74409 | 2024-10-23 04:00:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b92b845e-4458-3ace-a1c9-ee5d460d0e49 | -6.51546 | -47.04032 | 2024-10-23 04:00:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e4b8ce72-84c4-3dfe-af1e-8ca5f7241a80 | -6.51418 | -47.04279 | 2024-10-23 04:00:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1c95ae92-87ae-3ebd-97cb-496d17df5099 | -6.51085 | -47.0395 | 2024-10-23 04:00:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c7bcd7ad-49a6-30cc-9e07-dc64e3fb0d3d | -6.50957 | -47.042 | 2024-10-23 04:00:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0e49d39f-fecb-3f8e-8ec4-1d105dfd606e | -6.35028 | -47.12477 | 2024-10-23 04:00:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f55da0b3-bb5f-39f6-aa51-874113654a62 | -6.34945 | -47.12963 | 2024-10-23 04:00:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a2972229-e496-380f-9a2f-34e88b91f956 | -5.37176 | -47.50063 | 2024-10-23 04:00:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d4df23c4-a165-3d8c-8e75-5c592aadadf6 | -5.51127 | -46.48676 | 2024-10-23 04:00:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3923d934-1319-3c45-b90b-5d1e8e1df8c3 | -5.50857 | -46.48466 | 2024-10-23 04:00:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0105abf6-7c90-394e-80cb-3036504cddeb | -5.43948 | -46.91058 | 2024-10-23 04:00:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 984d349a-54c5-32f0-874e-40dfdfaba9eb | -5.43483 | -46.90981 | 2024-10-23 04:00:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 84feef2c-d84b-3049-833f-6a4357d71e7c | -5.40808 | -47.11124 | 2024-10-23 04:00:00 | NOAA-20 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5af7988a-907c-3f0c-b896-1e6eb9e14c05 | -5.21255 | -47.19627 | 2024-10-23 04:00:00 | NOAA-20 | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b02ea8b0-c29c-3074-a7c0-f29faa3f5c2e | -7.67814 | -47.31179 | 2024-10-23 04:00:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| add3d2d8-7bfc-32a6-b1f1-eb267e93a3a7 | -7.67353 | -47.31103 | 2024-10-23 04:00:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b05c0d1a-725b-31ff-b455-22ad0a8b28b7 | -7.50133 | -47.35641 | 2024-10-23 04:00:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2e6fceff-1fee-30e4-998e-b8ad3d7c85ea | -9.23676 | -48.32439 | 2024-10-23 04:00:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b79ca447-70c9-32ed-80b5-cc47e4393ee6 | -9.07514 | -47.99097 | 2024-10-23 04:00:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4ac28742-9883-3a33-aef8-fa912507fd9e | -9.07422 | -47.99608 | 2024-10-23 04:00:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ba47b288-37c5-3d1a-9478-3b6dd9fa2ab2 | -9.00935 | -48.72789 | 2024-10-23 04:00:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 55a6fdbd-e32d-38c9-a43d-85e409a95dfc | -9.0086 | -48.72723 | 2024-10-23 04:00:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fcc8bb9d-087b-3ce1-a3d6-503ebbb88250 | -9.54297 | -47.8283 | 2024-10-23 04:00:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2d2a5f4d-b714-3e8f-8237-1cb7b4810d73 | -9.53838 | -47.8273 | 2024-10-23 04:00:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 145a36d7-0da5-392c-ae00-607dadff5607 | -10.00822 | -47.46178 | 2024-10-23 04:00:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7a5d57c7-cec7-3cdf-8eea-96f4807aa109 | -10.8251 | -48.32412 | 2024-10-23 04:00:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 432d789f-35b0-3583-989e-d9ca8b5c0f06 | -10.8224 | -48.32623 | 2024-10-23 04:00:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ba4cf6b3-a08c-3d4d-843a-07bc57470afa | -10.82049 | -48.32293 | 2024-10-23 04:00:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3602966b-511f-348f-95e8-c55aa63ea79c | -10.65815 | -48.61227 | 2024-10-23 04:00:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 10f9722c-fcc7-3991-a95a-a8d13d48ae8d | -10.63958 | -47.68856 | 2024-10-23 04:00:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7577b796-294f-3513-abde-424ae7ec1da2 | -10.63874 | -47.69316 | 2024-10-23 04:00:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9f68e0b2-494d-31ac-a315-cca51531a80e | -11.02868 | -48.27772 | 2024-10-23 04:00:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 9b22f5b8-512c-300f-b4c4-9924ed4ce85a | -11.02782 | -48.2825 | 2024-10-23 04:00:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 241c3c67-e4b9-3be1-a04a-6e1299d4a9fa | -11.02404 | -48.27685 | 2024-10-23 04:00:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 3967416c-cced-3d40-8360-62abe189bb94 | -11.02317 | -48.28168 | 2024-10-23 04:00:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| ca742d10-a4a4-300d-bb2b-e1f409e5739e | -10.93792 | -47.84026 | 2024-10-23 04:00:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |


[Clique aqui para ver as próximas entradas](README27.md)

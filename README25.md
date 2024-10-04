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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e182b6f9-2419-3fb5-bb3b-c074b0f203b7 | -9.01808 | -49.81945 | 2024-10-04 01:09:00 | TERRA_M-M | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 469cf04c-a79c-31b0-ae60-18a48459d066 | -9.00899 | -49.8208 | 2024-10-04 01:09:00 | TERRA_M-M | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 15.5 |
| e6bf917c-1ce4-399d-bcf3-3147183320a9 | -8.91557 | -49.68927 | 2024-10-04 01:09:00 | TERRA_M-M | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 4b2a1e28-6839-3d55-9d17-58fc7068d459 | -8.91418 | -49.67971 | 2024-10-04 01:09:00 | TERRA_M-M | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 0e0b66c1-04ef-3207-a84c-964e7d5a9626 | -8.91279 | -49.67015 | 2024-10-04 01:09:00 | TERRA_M-M | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 6583e0e8-6f68-3fbd-8b8a-9bf3ba501ecf | -8.90438 | -49.66748 | 2024-10-04 01:09:00 | TERRA_M-M | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 59a73dfb-2261-34fc-8fd3-272b24fe5589 | -8.89249 | -49.64966 | 2024-10-04 01:09:00 | TERRA_M-M | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 6e8abd86-800c-326d-9e7b-d88bc1953b74 | -8.7865 | -49.94307 | 2024-10-04 01:09:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| b464128a-ceeb-3b76-880d-9c4510586e40 | -8.77743 | -49.94442 | 2024-10-04 01:09:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| ab397c59-53cb-32ee-8312-72002b1c8923 | -8.65594 | -50.06059 | 2024-10-04 01:09:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 9b6646fe-1c0e-3dc7-87c9-0f36c61d22ed | -8.65461 | -50.05127 | 2024-10-04 01:09:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 37.9 |
| 910606af-4dac-38e2-8568-18bba7923231 | -8.65328 | -50.04196 | 2024-10-04 01:09:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| fa685974-988c-398a-b5f1-0af1fbfa1935 | -8.6469 | -50.06194 | 2024-10-04 01:09:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 26.0 |
| 80d3d482-4fe6-35ef-bcf6-6769c26a0c87 | -8.64557 | -50.05262 | 2024-10-04 01:09:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 80.6 |
| 7923c8d8-89b3-3370-bf35-6f02ef80df71 | -8.64424 | -50.04329 | 2024-10-04 01:09:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 5920ef8b-b814-3f9f-b2b1-03ea98a931a0 | -8.63654 | -50.05398 | 2024-10-04 01:09:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 7c840816-0e66-3f16-8f48-85689a76bb25 | -8.34611 | -49.51454 | 2024-10-04 01:09:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 3c82ee68-02d6-3910-a3b2-fcd4f7939835 | -8.31936 | -49.57451 | 2024-10-04 01:09:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 23.5 |
| b3a17033-3ff8-3ef7-ad8e-4b3d824e5c1c | -8.31796 | -49.56479 | 2024-10-04 01:09:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 548e168b-b7db-3193-b94a-473d1e866941 | -8.31012 | -49.57589 | 2024-10-04 01:09:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 20.6 |
| 22bba712-28ca-31eb-9e13-d2b6fdd7e02b | -8.30872 | -49.56616 | 2024-10-04 01:09:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| e1e11213-a226-3f05-a0ef-976320d21473 | -9.98372 | -49.48092 | 2024-10-04 01:09:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 5bda323d-6102-3443-82a8-c40ecf43ffac | -9.7658 | -50.08702 | 2024-10-04 01:09:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 863f7b9e-74c4-30fa-8d4f-f4a4f37b5be1 | -9.63158 | -50.11285 | 2024-10-04 01:09:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 5027273c-fa97-3c4f-89a9-d3f29e0ae8f8 | -9.63026 | -50.10366 | 2024-10-04 01:09:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 8a2428c3-e8bf-339b-97e1-0ef181ce4fc0 | -9.60229 | -50.10482 | 2024-10-04 01:09:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| fab5a41b-e2c6-35b5-b039-c8c85f32da86 | -9.59479 | -50.18091 | 2024-10-04 01:09:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| ebfff76c-6d53-3bdb-ac6f-5963a922f045 | -9.59349 | -50.17175 | 2024-10-04 01:09:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 5a1638ec-b1f8-316c-853b-9fd14c3d7d4f | -9.58584 | -50.18224 | 2024-10-04 01:09:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 132f716d-73c7-3c50-85d8-ae0c391193ae | -9.57446 | -50.23063 | 2024-10-04 01:09:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 023a9217-77bd-3fa2-b18a-fa8c7c2e13f8 | -9.57315 | -50.22149 | 2024-10-04 01:09:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 13ba2fd8-d039-37e1-8046-3fdd33c2f4be | -9.56551 | -50.23195 | 2024-10-04 01:09:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 2115467e-a971-3890-8bf7-b32ae2f8edd6 | -9.56421 | -50.22281 | 2024-10-04 01:09:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 4aac81d8-7bea-3dc7-86d6-007a6bf5894a | -9.5629 | -50.21367 | 2024-10-04 01:09:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| dc1515ae-2b37-3b55-9dfc-b2823331fa77 | -9.55527 | -50.22414 | 2024-10-04 01:09:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| ebd45ec0-c8f8-3d10-a26c-937fe705c6df | -9.55396 | -50.215 | 2024-10-04 01:09:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 6a8d1b6c-ed52-3a30-858e-6fcaa5e885bf | -10.52199 | -49.12966 | 2024-10-04 01:09:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 96ca18c0-f0fe-397d-9c37-0fdacb6c9e81 | -11.14659 | -49.6216 | 2024-10-04 01:09:00 | TERRA_M-M | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 69c373f5-3167-3fd6-8f80-b9dcda436260 | -11.14525 | -49.61227 | 2024-10-04 01:09:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| f1148ef5-7905-3c1c-b574-33735b7d78bc | -11.12587 | -49.60567 | 2024-10-04 01:09:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 7ff10abe-284f-3253-80cd-386d08ec45d1 | -11.11686 | -49.60704 | 2024-10-04 01:09:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 7f64d1cf-8240-3d84-bcce-ab89080c66db | -11.1155 | -49.5977 | 2024-10-04 01:09:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 74409c32-e7ed-3188-900c-7248f7efcaa6 | -11.08929 | -49.60751 | 2024-10-04 01:09:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 0fe058a7-dc4b-3314-a9af-22794bea26b1 | -11.08027 | -49.60887 | 2024-10-04 01:09:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 9cf870da-c051-36cc-a521-5b920aaff2e4 | -10.97486 | -50.16322 | 2024-10-04 01:09:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 33f1852d-f154-3842-97a4-4f33bfa3e1a3 | -10.87767 | -50.12823 | 2024-10-04 01:09:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b71a4aff-319d-377d-92ca-2a6f2fe7a54c | -10.87509 | -50.11002 | 2024-10-04 01:09:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| f130b84f-9784-3490-bdc1-2ace99de297d | -13.70526 | -49.85765 | 2024-10-04 01:09:00 | TERRA_M-M | AMARALINA | GOIÁS | Brasil | 5200829 | 52 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 6e951bdb-b5aa-327c-8586-62d239a6fc31 | -13.62649 | -51.21648 | 2024-10-04 01:09:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 58fb6989-bfc1-3150-bc83-80e88390d9ec | -13.62523 | -51.20723 | 2024-10-04 01:09:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 233c07c7-9e48-3c00-88ce-cb774f7592ef | -13.62397 | -51.19799 | 2024-10-04 01:09:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 0c4574f6-ae30-3698-999c-dbced4dfdab4 | -13.6227 | -51.18874 | 2024-10-04 01:09:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 15.5 |
| ca999ffa-2705-3669-aae2-3178aa0bae58 | -13.61755 | -51.21779 | 2024-10-04 01:09:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 37.5 |
| c97f9781-822b-3ad1-b2bb-ada0eca7db2d | -13.61629 | -51.20853 | 2024-10-04 01:09:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 32.7 |
| 119d7857-81c4-336e-81c4-30783a66bb62 | -13.61502 | -51.19928 | 2024-10-04 01:09:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 65dbf532-f326-30cd-b4e9-7c4d984b8ecf | -13.56764 | -51.25336 | 2024-10-04 01:09:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 27.3 |
| c9f52d8f-adb8-3498-bc17-c95cb70d6e58 | -13.56639 | -51.2441 | 2024-10-04 01:09:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 88ce1b14-60b2-37fd-a7bc-5f2893638c75 | -13.11453 | -51.1708 | 2024-10-04 01:09:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 18.9 |
| b5fdec4c-00e8-3f1b-b64e-0ad2fa840166 | -13.11328 | -51.16162 | 2024-10-04 01:09:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 117.5 |
| 8b84c567-c8aa-389e-8b0a-d330566bbcfd | -13.11203 | -51.15245 | 2024-10-04 01:09:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 39.0 |
| c3917185-4f80-34fc-b3ba-195937acb81a | -13.10437 | -51.16292 | 2024-10-04 01:09:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 54.5 |
| dcb29718-e207-3a42-891e-7b729b969b68 | -13.10312 | -51.15375 | 2024-10-04 01:09:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 16.7 |
| cefee0fd-6f2b-376a-8ee5-bb9d27618bf5 | -13.09546 | -51.16422 | 2024-10-04 01:09:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 1acae2a6-92e2-388f-b458-9db758007ee7 | -13.07478 | -51.15492 | 2024-10-04 01:09:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 3b278ccb-4e64-31fb-9c06-bce462228974 | -13.07352 | -51.14576 | 2024-10-04 01:09:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 23.4 |
| e62097fe-ac86-3603-8285-a361e47a1e9b | -13.07226 | -51.13661 | 2024-10-04 01:09:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 29.3 |
| 10ac4f3f-3a2e-377f-99e3-18a07b9b9c71 | -13.071 | -51.12746 | 2024-10-04 01:09:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 7c331885-80a1-3172-9e30-b9367289c122 | -13.0621 | -51.12876 | 2024-10-04 01:09:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 31.3 |
| 5ea1733d-50f7-3193-9c8c-7b006d765979 | -13.03538 | -51.13264 | 2024-10-04 01:09:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 558fff5d-c6c1-3874-a5ee-7032d33e1fe6 | -13.02648 | -51.13394 | 2024-10-04 01:09:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 44.6 |
| 1f94c2bd-dead-3d8e-8ff3-5430edf922f8 | -12.98961 | -51.12998 | 2024-10-04 01:09:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| ffe0d8de-c7ae-396d-ba6e-248213f9cb2e | -12.97907 | -51.12801 | 2024-10-04 01:09:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 23.5 |
| f7ae4dcc-7068-3a78-a6a4-e5ee46dae582 | -12.6167 | -49.65121 | 2024-10-04 01:09:00 | TERRA_M-M | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 66923fa0-3493-3eea-ae97-a2b8bc7df924 | -16.09962 | -50.45509 | 2024-10-04 01:09:00 | TERRA_M-M | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 733b1b23-65ee-3d8b-8469-24364533dc18 | -16.09832 | -50.44566 | 2024-10-04 01:09:00 | TERRA_M-M | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 12.0 |
| fcbbf3dd-9f37-375a-851a-d2c9adfb0a4f | -16.0793 | -50.43931 | 2024-10-04 01:09:00 | TERRA_M-M | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| e42255f5-a583-3025-a71a-000199839ce3 | -16.07929 | -50.30698 | 2024-10-04 01:09:00 | TERRA_M-M | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 33.3 |
| 94ec2bdd-bb51-309d-95e2-514bd4db59a8 | -7.82902 | -50.53536 | 2024-10-04 01:09:00 | TERRA_M-M | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 26.0 |
| 4e511194-e0e9-3be4-981f-5f276be4e2f6 | -7.82774 | -50.5262 | 2024-10-04 01:09:00 | TERRA_M-M | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 57fcb307-1496-315b-9df5-85f8b2ebc78d | -7.82007 | -50.5367 | 2024-10-04 01:09:00 | TERRA_M-M | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 35.7 |
| 37d33ae8-03f2-3ae6-8e83-4daea02d69aa | -7.81878 | -50.52755 | 2024-10-04 01:09:00 | TERRA_M-M | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 24.1 |
| 7862f98f-236b-3a15-b071-c6d0e79a0851 | -9.11203 | -51.52963 | 2024-10-04 01:09:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 4f62f5e9-d5f4-3d49-af3d-48eb9702f4f7 | -9.11079 | -51.52074 | 2024-10-04 01:09:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 119223c7-6a20-33ba-8391-ecaa1144b5b2 | -9.1106 | -50.92442 | 2024-10-04 01:09:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9a75573e-51c5-37c8-8b80-f137305c4a1d | -9.10935 | -50.91549 | 2024-10-04 01:09:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 0b85ff36-86fb-32d6-a2b1-e2a58c12cc88 | -9.10318 | -51.5309 | 2024-10-04 01:09:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| accf0f1c-1483-3e4e-a634-212d311d8c4f | -9.10049 | -50.91678 | 2024-10-04 01:09:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 50f97394-c069-3431-8738-b154ce849ae9 | -9.09924 | -50.90785 | 2024-10-04 01:09:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 6b8053c2-d231-3b9b-a2bd-708644105d11 | -8.35703 | -50.87336 | 2024-10-04 01:09:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| ce5c34a6-0578-354a-85c1-90d057ff7dce | -8.35197 | -50.83755 | 2024-10-04 01:09:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d3cdf998-4769-32c4-a4ac-5444512caed1 | -8.34818 | -50.87473 | 2024-10-04 01:09:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| dff1d431-ee46-3ba3-8b4a-ad6afce334ee | -8.29925 | -50.92425 | 2024-10-04 01:09:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| edb97f0d-e18e-3ef4-818e-1c107e8b0d3b | -8.29799 | -50.91533 | 2024-10-04 01:09:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 9ba5667d-565a-334e-8369-ccc59cd0d32e | -8.07864 | -51.12946 | 2024-10-04 01:09:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 0194d4ef-a487-39de-9c21-f64071996148 | -8.01943 | -50.90109 | 2024-10-04 01:09:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 63061b48-9f81-37cd-a810-31f83f40ff60 | -9.42673 | -50.68024 | 2024-10-04 01:09:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b0ecc1fd-8940-3ed6-8be8-c2badd3778c3 | -9.37277 | -50.75813 | 2024-10-04 01:09:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1207f819-411b-3e41-8824-09499f294503 | -9.37151 | -50.74917 | 2024-10-04 01:09:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| e1668c72-908e-3941-a99f-a6d5353e57be | -9.36265 | -50.75048 | 2024-10-04 01:09:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 2c724d07-3200-3b2e-bc1f-8afc8701a144 | -9.32502 | -50.81712 | 2024-10-04 01:09:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 19.8 |


[Clique aqui para ver as próximas entradas](README26.md)

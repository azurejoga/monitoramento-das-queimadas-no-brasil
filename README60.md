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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d78abecb-b8ee-337a-8613-6a30a2979f8a | -9.80044 | -47.79512 | 2025-09-10 04:42:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 19c4751d-1c2e-3b63-8468-a51719f3e1d0 | -6.20846 | -45.61372 | 2025-09-10 04:42:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1e1fa586-3e5e-3579-9be1-02df30cfc93c | -7.77837 | -50.77287 | 2025-09-10 04:42:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f6099b7e-2adf-3277-b2d2-21bd09f1a7f3 | -8.15873 | -46.0921 | 2025-09-10 04:42:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dbdc0a24-01f3-30d9-8a68-5a9d0f0ec4de | -5.78763 | -50.16205 | 2025-09-10 04:42:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fe5e4b76-c118-3779-b629-743113af75c0 | -7.54425 | -44.65908 | 2025-09-10 04:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b2428d47-dc1b-3eb1-9ffb-e80f917ea0e0 | -7.07694 | -45.20459 | 2025-09-10 04:42:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 733125c3-c064-3299-8a67-182532161cf3 | -11.42515 | -43.58458 | 2025-09-10 04:42:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0057d1aa-1835-3adf-a3d5-65945c45e379 | -9.68987 | -46.80393 | 2025-09-10 04:42:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4cfe8064-33a2-37d3-9dcd-6a5ce6f2a159 | -11.15983 | -48.35399 | 2025-09-10 04:42:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9391044f-59fb-3ea9-8581-474d27b6c30e | -7.79689 | -46.07082 | 2025-09-10 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8a443ac7-a288-3b4b-9e86-44d731f6a7bf | -8.31051 | -44.8246 | 2025-09-10 04:42:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8607edd4-d96d-3377-ad01-8e35875a18cc | -11.53597 | -47.31831 | 2025-09-10 04:42:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 81d9def1-cb0f-348b-9d69-dadd84ec38bb | -8.43522 | -47.27705 | 2025-09-10 04:42:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c216c059-ad05-3126-92d7-1af29d9a5e16 | -11.34044 | -46.54069 | 2025-09-10 04:42:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 888d1060-e938-314b-81c8-3d12d067ce4a | -7.78291 | -46.05247 | 2025-09-10 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 633274e1-0b5e-3914-9f15-9c938836da6d | -9.35609 | -46.5033 | 2025-09-10 04:42:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 26bc6ffc-7b5c-3eb1-a72d-f63f58d04ac5 | -9.73988 | -51.08947 | 2025-09-10 04:42:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e8ffa764-04bd-348a-84f2-15d3da48427c | -6.68294 | -51.41294 | 2025-09-10 04:42:00 | NPP-375D | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d61b4d5e-5ab9-32fe-9b4a-02e3c93c1bbf | -10.65454 | -48.61086 | 2025-09-10 04:42:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4a19d0cf-cae2-3fda-8245-18ee1bee136e | -11.18529 | -48.37334 | 2025-09-10 04:42:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f81b643c-b75e-3933-8b5e-5d263f066221 | -8.47876 | -47.29918 | 2025-09-10 04:42:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2dff2a8e-9e0b-3bd3-886c-b6bc16052de6 | -9.05042 | -50.47795 | 2025-09-10 04:42:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e214073c-1993-3993-a909-1bde7a49212e | -8.98281 | -45.72407 | 2025-09-10 04:42:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c3a0994b-04ea-39e6-b979-b34555291378 | -7.25941 | -44.46085 | 2025-09-10 04:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 33c0767b-4142-39d1-82cf-b7c6fff1b3fb | -9.08487 | -45.70656 | 2025-09-10 04:42:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 94438b87-7940-3b55-bb9a-306aab40c17a | -6.18835 | -45.79639 | 2025-09-10 04:42:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 13622c8d-c6a5-351f-9a5c-6a08dd2142bf | -9.06208 | -45.7276 | 2025-09-10 04:42:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 19551606-c69d-3e28-8bdb-cdd23c7a3dfa | -9.06509 | -46.97425 | 2025-09-10 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 1757c535-3569-3b85-93f9-e13c9d465782 | -6.7275 | -51.96075 | 2025-09-10 04:42:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2de0a8c2-3495-3495-98f8-8470a2a61ec8 | -11.67321 | -46.90238 | 2025-09-10 04:42:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f5a772f4-5391-3b3a-8c1f-543dd8a8e298 | -9.44766 | -46.70465 | 2025-09-10 04:42:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 52dd728e-3cf4-3f46-a2af-9757a1425f6c | -11.12196 | -48.44142 | 2025-09-10 04:42:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cdd65046-393c-34b1-8292-34cc748be2a6 | -6.87379 | -47.88993 | 2025-09-10 04:42:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fb134a73-a625-332b-bc88-18d0434eb4df | -9.06678 | -50.47697 | 2025-09-10 04:42:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6de0f391-ae0f-3eac-bd61-42e51597eff3 | -8.04406 | -48.66423 | 2025-09-10 04:42:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 928ce163-1a75-33e0-852d-fd4656cdd361 | -9.44525 | -46.69547 | 2025-09-10 04:42:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b9f0303d-510a-348c-8d7e-09527d2d757d | -9.67958 | -46.89838 | 2025-09-10 04:42:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0cb65c94-e159-34fc-81a4-0197e8de3978 | -8.05026 | -48.67916 | 2025-09-10 04:42:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 4.6 |
| cf903663-7b95-37c0-b2ca-c17c092d0d85 | -9.44704 | -46.7089 | 2025-09-10 04:42:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1e240676-6f95-35b6-8236-3f052bb1e209 | -10.72994 | -48.29377 | 2025-09-10 04:42:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c5fcb54f-8027-35a4-9401-d9635a44bdae | -8.69419 | -48.88867 | 2025-09-10 04:42:00 | NPP-375D | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d3f62c05-537f-3959-8491-05ac9d85b7e8 | -8.04639 | -48.69353 | 2025-09-10 04:42:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 624eef0a-8ef5-3e28-b6c6-509309ba0647 | -9.06375 | -50.48009 | 2025-09-10 04:42:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| addb73ee-658c-327a-aaaf-d0a7532587b0 | -12.41102 | -43.21211 | 2025-09-10 04:42:00 | NPP-375D | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ed1604e0-2767-35b0-a46a-185d8c019e5f | -8.04743 | -48.66475 | 2025-09-10 04:42:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 3.7 |
| cb12ea7e-e784-3b8b-ae6c-f0f5b63be4e7 | -8.04971 | -48.68272 | 2025-09-10 04:42:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 4.6 |
| b4320b8f-9704-32c2-8a33-018c1ce88274 | -10.30765 | -48.8042 | 2025-09-10 04:42:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2e25e23e-20e7-3e72-8004-4e5d17f331f4 | -7.55469 | -48.22426 | 2025-09-10 04:42:00 | NPP-375D | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| db367b07-522a-3bd9-9338-57f7e8f09bd1 | -6.60689 | -43.95373 | 2025-09-10 04:42:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| daa2ded7-d921-3433-8140-40644953db20 | -6.8602 | -47.93243 | 2025-09-10 04:42:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f0539f03-b1ec-3186-ba24-19abf372b7ef | -11.41261 | -43.57311 | 2025-09-10 04:42:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2884f73d-cb07-3aae-94c2-42b2669b88e2 | -10.30992 | -48.81211 | 2025-09-10 04:42:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 552fbbae-59ac-30c5-88b7-444ad475c65d | -9.80426 | -47.7952 | 2025-09-10 04:42:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| df2a91ab-8365-350d-b066-4f5df5d3922b | -6.87787 | -47.88701 | 2025-09-10 04:42:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 686e2b12-9d7e-369f-af57-069d4cbb3be1 | -10.01694 | -51.70767 | 2025-09-10 04:42:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a34c942d-a772-317f-aafe-bc5ef51c24c1 | -8.1075 | -44.8564 | 2025-09-10 04:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e5475fc9-7518-375c-ace0-574177651429 | -11.66885 | -46.90626 | 2025-09-10 04:42:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a2d416f5-b012-3378-a50c-7540e0605b95 | -10.01813 | -51.70033 | 2025-09-10 04:42:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 77c14d35-6b8f-3114-97b5-3ba8bfe8b7b7 | -7.73933 | -50.73717 | 2025-09-10 04:42:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7bad373c-62cb-3048-b241-8aebddad7ba6 | -9.99997 | -51.70493 | 2025-09-10 04:42:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0cf60990-e0a5-32b2-ae1e-45f58fa72e43 | -11.86798 | -47.53662 | 2025-09-10 04:42:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 15581eb5-a161-37bc-893b-3a41b255688f | -10.14688 | -46.18404 | 2025-09-10 04:42:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 63fde2e0-77be-3cdd-a0b5-f58fb97ca7df | -7.07782 | -43.88446 | 2025-09-10 04:42:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e21b04e6-122f-3bb2-8cd0-31f05e30666b | -9.00659 | -49.53084 | 2025-09-10 04:42:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7276ceb1-d745-3106-b101-459be6469da4 | -7.25586 | -44.45668 | 2025-09-10 04:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0d3179d7-db23-3092-a152-34f81729e703 | -7.7371 | -50.72965 | 2025-09-10 04:42:00 | NPP-375D | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 26a04fa0-e3a8-349e-9b2d-16b9eeeb2155 | -10.58079 | -52.0419 | 2025-09-10 04:42:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1b9eaf7e-ad72-3fcb-8e24-2eefc3d3f826 | -10.01373 | -51.68451 | 2025-09-10 04:42:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 26f532a7-cacf-358d-97d4-63fe6d6b1fae | -9.31525 | -46.72387 | 2025-09-10 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 961ba176-50bb-30ae-887a-052cc94e77f2 | -7.70166 | -47.29594 | 2025-09-10 04:42:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| daf7eec5-bf5a-39f0-9a00-ec23fda32360 | -8.74369 | -47.0907 | 2025-09-10 04:42:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d41f5bab-a440-3192-8453-60f05f279208 | -8.21193 | -49.51318 | 2025-09-10 04:42:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ed5e32e7-af60-3243-919d-826f15145d5a | -7.74154 | -50.74488 | 2025-09-10 04:42:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d22b5426-c955-3c95-bf73-f63f167ed9cc | -7.93785 | -44.85371 | 2025-09-10 04:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 24a01089-1e45-3bb2-8a67-6611d0639475 | -9.52909 | -48.26196 | 2025-09-10 04:42:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 217dbfe0-a76f-32fd-9c2c-a9544883c0e5 | -10.00935 | -48.08222 | 2025-09-10 04:42:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 320ffa9f-d39a-388b-a1ab-2c3d6b8afe17 | -7.19611 | -44.93988 | 2025-09-10 04:42:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c3909c19-00af-3f0b-ad41-df8f34200c19 | -11.33732 | -46.53546 | 2025-09-10 04:42:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e16625f2-939b-3c89-93af-f76e27fb8808 | -11.13317 | -52.01809 | 2025-09-10 04:42:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 72bac2a0-15e1-3fc6-8431-924b78cf656b | -8.40287 | -47.30001 | 2025-09-10 04:42:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2ab78db2-8dd0-3025-9d7b-c03eeab46e22 | -11.11606 | -48.40988 | 2025-09-10 04:42:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 53fc27fa-5181-3509-9c9f-3d739fcddacf | -11.75577 | -50.62616 | 2025-09-10 04:42:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a34db574-6ece-3d15-a29d-bc1272a23bae | -11.12458 | -52.02795 | 2025-09-10 04:42:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a978ef3b-6f66-3a4b-a21c-919f37470cab | -7.66931 | -50.27083 | 2025-09-10 04:42:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 74c689cb-9bc2-3980-ac30-9fb9635e94eb | -7.98973 | -46.32902 | 2025-09-10 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 4f4a1581-42ae-3b3c-ba1d-06dd736d91a5 | -9.45316 | -46.71829 | 2025-09-10 04:42:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 167f3d8a-d1c0-39ac-ae80-272ed6e91757 | -10.88288 | -47.26021 | 2025-09-10 04:42:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 43b43b52-6fa6-3a76-87a6-60d26a848f91 | -8.04694 | -48.68998 | 2025-09-10 04:42:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 33.1 |
| 8124e3ac-7d24-3225-a941-52d397fbccc2 | -7.59032 | -49.29314 | 2025-09-10 04:42:00 | NPP-375D | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 135a21cb-2321-3271-9d4b-c9b6f5ff9d8d | -11.19166 | -48.4015 | 2025-09-10 04:42:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c08bccb5-332d-39d7-a065-c99b4d56a875 | -10.01534 | -51.69605 | 2025-09-10 04:42:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d8d6f3a7-51b3-3073-9881-731f2611d72a | -6.46239 | -44.11636 | 2025-09-10 04:42:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 265f7032-a734-3394-bca7-9988c13cba96 | -6.52429 | -44.8401 | 2025-09-10 04:42:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 167da8bb-38b8-38da-b9e5-7234bfc5fcd7 | -10.7259 | -48.29706 | 2025-09-10 04:42:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 350fc3df-a304-3fee-b3c4-33af85efd6fe | -11.10989 | -48.45121 | 2025-09-10 04:42:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7efecde1-d8eb-35c2-b0bb-26eb2d685241 | -9.44829 | -46.70033 | 2025-09-10 04:42:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f4791a42-0aed-34fb-852b-b214c4dbd0e3 | -11.4816 | -50.41557 | 2025-09-10 04:42:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 025fb719-68bd-3052-93ed-e193e891c4e3 | -7.53943 | -48.21076 | 2025-09-10 04:42:00 | NPP-375D | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 06f845a5-37d4-3776-b3e4-d04078cbaaba | -8.43875 | -47.27758 | 2025-09-10 04:42:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README61.md)

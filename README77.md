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

## Dados Diários - Página 77

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d0373eb5-501f-38f6-9c9d-dafa935e97a3 | -12.44327 | -46.64778 | 2025-09-14 12:17:00 | TERRA_M-T | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 27c0d2a0-9ea6-308e-9443-a5bc5925efa2 | -8.43448 | -47.22674 | 2025-09-14 12:17:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 175.5 |
| e50bcb5d-4fba-32f1-91bc-8db856afd8ed | -7.30702 | -43.9408 | 2025-09-14 12:17:00 | TERRA_M-T | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 14.1 |
| a62d98ab-6380-3b8a-9957-fb6449a74eb7 | -12.97242 | -48.04137 | 2025-09-14 12:17:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 27604242-1ea0-333f-8733-e3dcb6c074ba | -11.50443 | -50.79935 | 2025-09-14 12:17:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 27.2 |
| 79abaa55-d564-3072-93a3-445928d741e8 | -7.61255 | -46.72089 | 2025-09-14 12:17:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| e2193951-593f-39d5-8fb8-dce2edea5422 | -6.39182 | -42.80259 | 2025-09-14 12:17:00 | TERRA_M-T | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 18.9 |
| 1fae27e3-86d5-33ca-b37f-ab81545b97c9 | -8.91731 | -46.16873 | 2025-09-14 12:17:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 26.7 |
| 28d634f0-b99d-378c-a8cd-4bc88386bf36 | -6.91799 | -44.5388 | 2025-09-14 12:17:00 | TERRA_M-T | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| ba82e0c3-663f-3d78-8926-e9c48f44a9c1 | -9.00725 | -45.79844 | 2025-09-14 12:17:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 34.9 |
| 5ac4c9da-63ec-315c-b256-6e695f59ab07 | -8.93262 | -46.12499 | 2025-09-14 12:17:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 33.5 |
| 5f476b35-99ff-3844-bc7e-c5d901673fd8 | -10.54421 | -51.48377 | 2025-09-14 12:17:00 | TERRA_M-T | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 27f7973f-3366-3b34-bd17-98a73181b953 | -10.9397 | -47.24458 | 2025-09-14 12:17:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| cba1e4ee-a8da-3743-b369-c522d35d62e5 | -8.98928 | -45.79603 | 2025-09-14 12:17:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 11.5 |
| abc463fd-c12c-33e7-92a6-fddcaf65a81f | -12.73391 | -48.03998 | 2025-09-14 12:17:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 860b87a2-8461-3f9d-aa1b-602db9879ac6 | -12.82069 | -47.17123 | 2025-09-14 12:17:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 76.7 |
| c8e8df34-ff3e-3483-9c02-f248b66b0e98 | -11.46517 | -48.69847 | 2025-09-14 12:17:00 | TERRA_M-T | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 892a529f-43eb-348f-9174-79f976b26048 | -12.44044 | -46.86898 | 2025-09-14 12:17:00 | TERRA_M-T | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| c18ed2a8-ff80-39ff-a770-313cc27f0ab3 | -8.90721 | -45.46035 | 2025-09-14 12:17:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 51.3 |
| 8a52cd9f-bea4-3271-b4f6-c80037c83184 | -11.78982 | -46.6433 | 2025-09-14 12:17:00 | TERRA_M-T | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 15.5 |
| e5499c45-acf8-34ba-b4ab-3a399cf763b9 | -7.2142 | -44.39679 | 2025-09-14 12:17:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 43ec9cad-a609-34ae-8da8-1a9cc839cd46 | -7.19389 | -44.12679 | 2025-09-14 12:17:00 | TERRA_M-T | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 313cb054-cf05-3242-b338-44e28d0aa3f3 | -8.08007 | -44.5159 | 2025-09-14 12:17:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 20.8 |
| c8172712-5e35-3eee-bef7-68fe9389a8d9 | -12.50858 | -44.7699 | 2025-09-14 12:17:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 52.8 |
| af75413c-5542-33d2-9c22-40e4cad2e9a7 | -10.91726 | -45.57413 | 2025-09-14 12:17:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 8ab03aa0-80a8-3fb9-92f9-31f24499d4be | -5.43793 | -45.10155 | 2025-09-14 12:17:00 | TERRA_M-T | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 30.5 |
| 7f1f294e-9206-327e-91ef-9b8654e3be12 | -12.82198 | -47.16216 | 2025-09-14 12:17:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 142.5 |
| c0a90036-767c-3e6e-8d4e-143dae9a8529 | -11.16579 | -43.41763 | 2025-09-14 12:17:00 | TERRA_M-T | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 23.7 |
| c9dc244f-8fa8-30c1-a054-bb2f56219144 | -8.64413 | -44.03949 | 2025-09-14 12:17:00 | TERRA_M-T | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 17.8 |
| af206308-7cb4-307a-8a97-b1f20090a86f | -8.96372 | -46.04329 | 2025-09-14 12:17:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| ab7e5988-2226-3455-9ae2-eca36158d20b | -11.50997 | -50.76394 | 2025-09-14 12:17:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 25.5 |
| 7d293463-ff20-3471-871f-363f4dc9d34c | -11.87387 | -50.46369 | 2025-09-14 12:17:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 18.0 |
| e43ea648-e06d-3c86-a023-045bf0084d97 | -11.37817 | -47.33862 | 2025-09-14 12:17:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 65.0 |
| d93bdfb1-83b1-3f26-94d7-ec84e83092ca | -12.73522 | -48.03093 | 2025-09-14 12:17:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 42.8 |
| a4846b09-8f35-3610-a66b-e3dfcd17c023 | -10.40965 | -48.60088 | 2025-09-14 12:17:00 | TERRA_M-T | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| d7ecdca0-7250-39e5-8495-71464e9df7ec | -8.78089 | -46.0329 | 2025-09-14 12:17:00 | TERRA_M-T | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 40.0 |
| c4e767ad-192f-3768-ae49-d5f1ea8347ee | -9.1132 | -50.54713 | 2025-09-14 12:17:00 | TERRA_M-T | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 835b3dc1-1fb6-3abc-8d10-b1b352ae8144 | -13.55317 | -43.80958 | 2025-09-14 12:17:00 | TERRA_M-T | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 2ffe9015-d5a8-3c02-929b-03962535cbd1 | -11.14 | -47.64843 | 2025-09-14 12:17:00 | TERRA_M-T | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 59c6b0ed-1466-38bf-bc26-089383e3ff01 | -10.39915 | -50.58702 | 2025-09-14 12:17:00 | TERRA_M-T | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 14.1 |
| fdbc67cf-396e-331b-bbf3-bebad38d6117 | -12.57098 | -45.6639 | 2025-09-14 12:17:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 37.5 |
| 3cdc0d75-9991-3901-adf1-7db564f81469 | -10.74837 | -46.45531 | 2025-09-14 12:17:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 37.1 |
| 5043b22f-0049-33ed-a4ef-a347a69993d3 | -11.23715 | -47.61397 | 2025-09-14 12:17:00 | TERRA_M-T | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 1c934555-93d1-3a6e-8200-2b72cf752e26 | -12.82327 | -47.15308 | 2025-09-14 12:17:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 87.7 |
| aeb67e20-50c5-32ec-bccd-a8a1e99a52bf | -11.86235 | -50.47335 | 2025-09-14 12:17:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 17.5 |
| fab6c0c5-1945-339c-83e2-9b16ddb6a2d6 | -10.915 | -45.4547 | 2025-09-14 12:17:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 284ec24a-c0e4-33a8-9d59-202593f5fc6a | -13.4812 | -41.45349 | 2025-09-14 12:17:00 | TERRA_M-T | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 72.3 |
| 7ead4c25-1ade-3e76-bfdc-54f31eecc876 | -11.63136 | -46.91976 | 2025-09-14 12:17:00 | TERRA_M-T | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 16.6 |
| e204538f-bfa6-3233-82e4-261e65575c62 | -8.80811 | -47.13221 | 2025-09-14 12:17:00 | TERRA_M-T | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 3562bc2b-f16c-330c-b994-7405e15e3492 | -8.78217 | -46.02382 | 2025-09-14 12:17:00 | TERRA_M-T | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 29.9 |
| 95ea2f51-d8c7-32b3-acb8-7f892171438f | -11.91671 | -46.52681 | 2025-09-14 12:17:00 | TERRA_M-T | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 43db52dd-202d-304c-958e-1f3179b16e98 | -12.56403 | -47.36173 | 2025-09-14 12:17:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 2be489e0-b3bc-3213-a1e1-127d165ef882 | -12.11738 | -47.5779 | 2025-09-14 12:17:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 8f682e35-99cc-3fff-841e-f50582cf971f | -6.68734 | -45.51877 | 2025-09-14 12:17:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 0a5d3295-b449-3d37-8265-c87821b25e96 | -12.43915 | -46.87811 | 2025-09-14 12:17:00 | TERRA_M-T | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 56.8 |
| baad7ac9-48c4-33d1-ba4b-3f70c61538ba | -12.77953 | -48.03743 | 2025-09-14 12:17:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 19.4 |
| c6c7cfaa-1932-3fd6-8b71-053a99ee24c2 | -10.76108 | -46.49413 | 2025-09-14 12:17:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 3234be5f-3eeb-32c9-97f9-43ccf580cea5 | -13.06213 | -42.24559 | 2025-09-14 12:17:00 | TERRA_M-T | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 38.5 |
| d9de9f7e-bcb3-3310-b78b-a149552fb1da | -10.74709 | -46.46438 | 2025-09-14 12:17:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 3c4c3124-2f1b-3a25-8b39-9aca68d658f8 | -7.20337 | -44.12809 | 2025-09-14 12:17:00 | TERRA_M-T | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 44.3 |
| c22759be-c3bb-3eb0-ad85-da7d77e3a2ff | -11.78348 | -46.62374 | 2025-09-14 12:17:00 | TERRA_M-T | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| f9a1b831-d760-3a87-9cf1-fc79365c76d3 | -10.89383 | -45.47206 | 2025-09-14 12:17:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 3e076f52-11c5-361e-8d3a-baf0840b3ea9 | -11.24462 | -44.77247 | 2025-09-14 12:17:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 14460c82-6f38-35d6-b4ce-f5289e597766 | -5.79273 | -43.88892 | 2025-09-14 12:17:00 | TERRA_M-T | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 0547440b-582c-31a2-a875-454c7824bbd1 | -13.1351 | -43.32415 | 2025-09-14 12:17:00 | TERRA_M-T | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 11.0 |
| 06890541-671d-30b5-a68d-95a69f662d5c | -11.70196 | -46.48418 | 2025-09-14 12:17:00 | TERRA_M-T | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 0fdc6d13-ef14-34f6-bfc9-20df00f8b742 | -11.45075 | -43.90387 | 2025-09-14 12:17:00 | TERRA_M-T | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 1da55306-ee95-37ec-9ebb-bb4be1beefba | -12.44807 | -46.87938 | 2025-09-14 12:17:00 | TERRA_M-T | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 316.3 |
| deeb8992-7cf7-3702-83f2-16fa0509a69a | -11.67124 | -46.508 | 2025-09-14 12:17:00 | TERRA_M-T | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| a12190ca-99d3-3b59-a635-6f255d155d48 | -11.35021 | -43.49352 | 2025-09-14 12:17:00 | TERRA_M-T | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 27.2 |
| ff749193-b7ac-3d3f-8e9c-cd54cc8c3a75 | -8.14336 | -43.66707 | 2025-09-14 12:17:00 | TERRA_M-T | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 1613c322-2df0-323a-b1a9-31fd92375cf1 | -13.13688 | -43.31008 | 2025-09-14 12:17:00 | TERRA_M-T | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 620c857f-76b1-306c-91aa-139f3886ca5f | -10.75601 | -46.46563 | 2025-09-14 12:17:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 38.9 |
| 85f67517-db92-33ef-9386-d4f3b2ba3074 | -12.08329 | -47.56378 | 2025-09-14 12:17:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 658a1935-bcd1-3ac9-bd68-a06eab5157f7 | -9.49292 | -47.93322 | 2025-09-14 12:17:00 | TERRA_M-T | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 194d6c24-a0dc-3efc-863c-d2e85068d0a2 | -9.11512 | -50.53493 | 2025-09-14 12:17:00 | TERRA_M-T | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 60a3a38b-b906-39b9-aad7-a1994418f8cb | -10.75473 | -46.47472 | 2025-09-14 12:17:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 44.3 |
| a2a3ca93-a931-3c9f-b0b7-4738bbddc685 | -8.94716 | -46.16072 | 2025-09-14 12:17:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 30.8 |
| 40442425-10bc-3a22-8352-e41d77f84339 | -12.24866 | -46.7855 | 2025-09-14 12:17:00 | TERRA_M-T | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| eeffccaf-74e5-3c15-95f5-9d0c61189443 | -8.1335 | -43.66568 | 2025-09-14 12:17:00 | TERRA_M-T | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 204dd98e-6083-3584-89f3-bea07afd521f | -6.66239 | -46.08567 | 2025-09-14 12:17:00 | TERRA_M-T | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 601bc2df-c45a-37eb-b9d3-90cc8f7c0d6a | -11.80978 | -50.48813 | 2025-09-14 12:17:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 31.4 |
| 39e05ef1-f93e-3436-89ef-193f2dd963ae | -10.79525 | -45.98672 | 2025-09-14 12:17:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 737cfd1f-5ae7-3f2c-8c49-2a0f0554e471 | -7.51255 | -44.37487 | 2025-09-14 12:17:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 5853afcd-3615-3414-b369-990655652b95 | -12.77592 | -47.99996 | 2025-09-14 12:17:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 5311b0e1-4e23-398d-bf7a-155b0f94acb8 | -11.14488 | -45.32801 | 2025-09-14 12:17:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.9 |
| cdcaf02c-1ac2-3134-afc7-84812e1781f8 | -6.99045 | -44.54452 | 2025-09-14 12:17:00 | TERRA_M-T | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 52a5e474-f77c-3d41-8291-8aeb2e9b2117 | -7.60626 | -46.70193 | 2025-09-14 12:17:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 20.5 |
| f5848be5-d93a-3379-82ed-6b4e938306a0 | -12.81033 | -47.94966 | 2025-09-14 12:17:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 4462e719-5385-3cf3-b2a9-1cba81d461ff | -8.99057 | -45.78681 | 2025-09-14 12:17:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 85757c91-1804-3ce5-bba0-ff013376f962 | -6.67841 | -45.51755 | 2025-09-14 12:17:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 27.3 |
| a6c5db55-bf6f-35a5-b800-c6cbaac621ad | -7.22941 | -43.83767 | 2025-09-14 12:17:00 | TERRA_M-T | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 0bb08907-6500-396f-8892-7a71af492b87 | -12.44981 | -49.70662 | 2025-09-14 12:17:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 3e387e37-9fe9-3e6f-ab45-74ac40d8abdb | -12.93237 | -47.94328 | 2025-09-14 12:17:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 5e140ca5-a0ea-3e27-bc30-fa564b53190a | -7.55576 | -46.72487 | 2025-09-14 12:17:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 31.4 |
| b73667eb-d764-337c-a980-d50125be2a4a | -8.88774 | -45.46737 | 2025-09-14 12:17:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 30.2 |
| fbda7527-e40b-3a08-aa9d-19349cc48e1e | -9.01522 | -47.03794 | 2025-09-14 12:17:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| e769f158-cdec-3938-be35-17c8816cb2d9 | -9.1217 | -44.83431 | 2025-09-14 12:17:00 | TERRA_M-T | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 699beaae-fbad-3510-9f1d-2d56667c3299 | -10.14323 | -47.20147 | 2025-09-14 12:17:00 | TERRA_M-T | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 404d43ea-4de4-3e81-a683-6e36572112f8 | -8.42431 | -47.23439 | 2025-09-14 12:17:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 33.7 |


[Clique aqui para ver as próximas entradas](README78.md)

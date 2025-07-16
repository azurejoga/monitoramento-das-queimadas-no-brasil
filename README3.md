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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9bd7c754-a62e-344e-b73a-b0d168e809ec | -13.015 | -45.036 | 2025-07-16 00:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 9a5b5e79-50fb-38bf-ae70-cc4905c6f3ab | -6.7194 | -44.3231 | 2025-07-16 00:40:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 75.7 |
| ef0f7bfa-c2c1-36e0-9e77-5089b404b427 | -7.9374 | -49.6631 | 2025-07-16 00:40:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 92.4 |
| ebab88d2-5f0e-36d2-b5ed-7f3985bded52 | -7.1837 | -43.1189 | 2025-07-16 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 121.4 |
| 1e652f4e-f643-3a6d-a12e-1eeda2b781ee | -20.0264 | -47.3879 | 2025-07-16 00:40:00 | GOES-19 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 53.8 |
| e36c49d8-e4a7-36e2-a6b4-d21f0e85cbce | -5.7943 | -45.0813 | 2025-07-16 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 820bdc50-6b9f-305a-ae97-b72abd944b89 | -13.0141 | -45.0826 | 2025-07-16 00:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 70.9 |
| a30cb660-86ef-34c9-aaba-d5a2991b8b34 | -12.5661 | -48.877701 | 2025-07-16 00:41:00 | METOP-C | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 77605bcf-8612-3a00-8114-0da810d0b34a | -10.6519 | -49.4757 | 2025-07-16 00:41:00 | METOP-C | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7e25c1f1-b1bb-37d3-a67c-11ab32f2ac9d | -11.181 | -48.6143 | 2025-07-16 00:41:00 | METOP-C | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2463e652-4cfd-3386-9c33-193b11605e45 | -9.8511 | -47.876598 | 2025-07-16 00:41:00 | METOP-C | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a8cd1c19-55d3-38d8-bfca-bb0968048bdb | -18.7929 | -51.310398 | 2025-07-16 00:41:00 | METOP-C | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c098527f-0169-3267-ab84-abc1d64b939b | -5.5318 | -43.876499 | 2025-07-16 00:41:00 | METOP-C | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1521085e-6aef-3a38-b6fa-236ffe15db1c | -20.09 | -47.634201 | 2025-07-16 00:41:00 | METOP-C | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 14c5ac89-8f02-3c67-9704-1b084736c57d | -5.5342 | -43.8866 | 2025-07-16 00:41:00 | METOP-C | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e391aeeb-4f6f-3592-85af-225d711a8a04 | -4.2805 | -46.3601 | 2025-07-16 00:41:00 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f0354b4b-3795-305a-8830-b278d05df3e8 | -12.0372 | -48.763802 | 2025-07-16 00:41:00 | METOP-C | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0e00b729-f09a-37b1-8301-291e69b41ef3 | -12.0756 | -43.470901 | 2025-07-16 00:41:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f58e5285-81c9-3374-8995-82cac6a88f0e | -12.9985 | -44.874599 | 2025-07-16 00:41:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3b4fb4c5-9bb2-305d-b0f9-5214eb471f05 | -7.2163 | -45.323101 | 2025-07-16 00:41:00 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fa7e5708-af15-3815-91ab-5a4c4bf3a660 | -7.9428 | -49.646099 | 2025-07-16 00:41:00 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b42675a0-e98e-306f-a2d0-9a5fb58e712d | -6.7089 | -44.313999 | 2025-07-16 00:41:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7cd11590-79d9-33b5-821b-dcd9fb85d0ea | -12.4898 | -46.920799 | 2025-07-16 00:41:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cecd33c8-c6e4-332a-bcbe-0cb10fc85753 | -13.023 | -45.0676 | 2025-07-16 00:41:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 89ee2470-53be-34af-ac65-3012f955dc1e | -6.9521 | -44.947701 | 2025-07-16 00:41:00 | METOP-C | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cb66d96a-d83e-34ad-a750-73a116d3a10e | -7.3561 | -49.738701 | 2025-07-16 00:41:00 | METOP-C | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4727d06a-7a6b-370e-8d1a-b3dc6fba8742 | -12.0219 | -47.7701 | 2025-07-16 00:41:00 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 22039990-a9c1-3ebb-b415-5f3f9f823a28 | -8.9143 | -47.341599 | 2025-07-16 00:41:00 | METOP-C | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b8af0c6b-43ca-3e5c-9d22-e80f0ce66dc3 | -12.4816 | -46.93 | 2025-07-16 00:41:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4b858bf3-9cca-394f-8f74-89f8d13b78c6 | -12.068 | -43.482101 | 2025-07-16 00:41:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9d485045-bb2b-342d-916e-717214fd9256 | -10.9017 | -49.209999 | 2025-07-16 00:41:00 | METOP-C | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a75d32f6-cd9b-3029-b662-5070f15afd88 | -6.7329 | -44.3279 | 2025-07-16 00:41:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3b0502ae-bf67-33cc-a897-6b9e223391b0 | -7.3468 | -49.605701 | 2025-07-16 00:41:00 | METOP-C | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| af22002c-63b8-3f3b-a97f-86dac972ee62 | -18.800501 | -51.2966 | 2025-07-16 00:41:00 | METOP-C | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 5c9e3b11-c116-3da1-a5d7-dc0f1cce0c3a | -6.6359 | -44.571201 | 2025-07-16 00:41:00 | METOP-C | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4a3f0d33-4534-3d38-bf08-41674ae3043f | -13.0178 | -45.045101 | 2025-07-16 00:41:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 28af81ab-1bd9-39cb-8f03-a592a3cf92bb | -12.4227 | -43.753502 | 2025-07-16 00:41:00 | METOP-C | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2bfa2413-3f77-3f80-bd26-b8cb4a53ff99 | -5.797 | -45.082199 | 2025-07-16 00:41:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 03dd8db0-de14-39c0-a010-b2bc364e72c8 | -20.019199 | -47.392502 | 2025-07-16 00:41:00 | METOP-C | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| bb01ae97-d3ae-308f-8063-d884ebcba09e | -6.7351 | -44.337101 | 2025-07-16 00:41:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 72921311-94d7-3f38-a95f-b55653b57f77 | -13.0195 | -45.052601 | 2025-07-16 00:41:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a15c998c-b9d1-34e3-8afb-b3691e0ac1cb | -12.4702 | -46.925301 | 2025-07-16 00:41:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 542b3011-f67d-34f7-9bca-bef81c52d6a2 | -12.4784 | -46.9161 | 2025-07-16 00:41:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3df3eaee-b0d9-3c1a-8104-6e54087aa1ea | -8.5113 | -43.305199 | 2025-07-16 00:41:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 9e87a987-9990-355f-b339-26e46a2ee2ff | -10.6502 | -49.4683 | 2025-07-16 00:41:00 | METOP-C | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2b6a2e8a-f609-3dcd-a4fb-c955a995c1a0 | -21.1075 | -48.614899 | 2025-07-16 00:41:00 | METOP-C | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e0d4d967-e063-31b3-8435-209af6139a0f | -8.6472 | -47.751301 | 2025-07-16 00:41:00 | METOP-C | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c61f195e-5026-3b42-9fe8-9dc0c46fc3d8 | -8.5089 | -43.2952 | 2025-07-16 00:41:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 4096e4b0-0b51-3e18-919d-fe20c48ed2d5 | -10.2203 | -55.433102 | 2025-07-16 00:41:00 | METOP-C | NOVA GUARITA | MATO GROSSO | Brasil | 5108808 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 70e5627e-7017-3010-9697-225963631296 | -5.5769 | -46.520599 | 2025-07-16 00:41:00 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3520458f-85fc-3535-8bb6-5afb5dd86da5 | -4.7815 | -45.326599 | 2025-07-16 00:41:00 | METOP-C | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f15586dd-9ad0-30a3-92b3-8e09504dbd29 | -2.9178 | -48.227001 | 2025-07-16 00:41:00 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e5481029-df41-3fd5-8eaf-a04add4bc369 | -13.0132 | -45.069901 | 2025-07-16 00:41:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c1a3aa9e-53c3-3021-a853-5cf32b18cd42 | -7.2182 | -45.3312 | 2025-07-16 00:41:00 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f4e7ba81-b0a4-3b1e-b7a1-ba40cc914ac8 | -8.9159 | -47.348598 | 2025-07-16 00:41:00 | METOP-C | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a8df5482-1b7b-335a-b936-9cc609f3fb67 | -7.1989 | -43.128502 | 2025-07-16 00:41:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 037fa6a8-90f4-36d7-8c56-720ce0fc8bb3 | -20.0256 | -47.3745 | 2025-07-16 00:41:00 | METOP-C | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 22a76419-464e-3a3d-871e-64042ee4d745 | -3.0395 | -48.979801 | 2025-07-16 00:41:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 131d194b-cd10-3b64-88ce-fd3690081573 | -13.1575 | -50.768101 | 2025-07-16 00:41:00 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ea58d4dd-2358-3d57-b359-b8f56ddd7172 | -6.9501 | -44.939201 | 2025-07-16 00:41:00 | METOP-C | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f4a17dae-c11c-3178-b04b-47c036b302b1 | -7.3088 | -45.760399 | 2025-07-16 00:41:00 | METOP-C | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ab1edcd4-7cd4-3d54-a2d8-bb2836e3a73f | -11.4583 | -45.0914 | 2025-07-16 00:41:00 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6f985e7f-d36d-3637-b4d0-d4018eb30307 | -11.4763 | -47.315701 | 2025-07-16 00:41:00 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1cd15215-c87a-3694-b824-62c0221f5943 | -21.109301 | -48.624001 | 2025-07-16 00:41:00 | METOP-C | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e9d211af-6cd4-3bb4-b737-05c52b0b8aad | -9.4951 | -48.1245 | 2025-07-16 00:41:00 | METOP-C | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b8904c1e-4fa1-302c-8766-dce58faf7167 | -6.6337 | -44.562302 | 2025-07-16 00:41:00 | METOP-C | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f57fef28-a97f-3468-a781-f59c0f4bbdd0 | -12.5677 | -48.885201 | 2025-07-16 00:41:00 | METOP-C | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 70e99dca-191c-39de-9876-b35c4d3af704 | -11.9488 | -48.4114 | 2025-07-16 00:41:00 | METOP-C | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9e5edfce-6b43-3520-a65d-40c54a724d8a | -10.5653 | -49.131001 | 2025-07-16 00:41:00 | METOP-C | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c28a36ef-5eee-33f8-a660-b652ca5db110 | -10.5669 | -49.138302 | 2025-07-16 00:41:00 | METOP-C | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2cb62f07-1a1d-3f6d-b1a7-012fbe00b4d4 | -11.1826 | -48.621399 | 2025-07-16 00:41:00 | METOP-C | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d9384f19-3be3-315f-8a61-b3dec7bb4e52 | -13.0097 | -45.054901 | 2025-07-16 00:41:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8f1e0a4e-1545-36ec-82b2-901c203082f7 | -11.4913 | -48.067799 | 2025-07-16 00:41:00 | METOP-C | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 602b80b9-7c85-3406-b53b-f5760d30ff50 | -20.358 | -41.495499 | 2025-07-16 00:41:00 | METOP-C | IÚNA | ESPÍRITO SANTO | Brasil | 3203007 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| fdb00c01-2017-334a-a4cc-5f223e392c93 | -8.246 | -44.9175 | 2025-07-16 00:41:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 36afbb64-c8e0-3734-adb5-04a9b3cb4efa | -12.4718 | -46.932301 | 2025-07-16 00:41:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4d7e3b70-3130-3f95-b44f-2f4c23d97078 | -4.0339 | -48.056099 | 2025-07-16 00:41:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 424d47d7-abf3-31df-8d9b-a2323268a718 | -7.9444 | -49.653301 | 2025-07-16 00:41:00 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dc8a015a-ff24-383f-b332-b8d8fc3a6d65 | -4.1083 | -48.199501 | 2025-07-16 00:41:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7ba2cbd5-c7f9-3c60-8d82-40ca67c2faca | -13.0982 | -47.287601 | 2025-07-16 00:41:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e4323cb4-9db3-3d2f-a0b7-242683f7eca3 | -5.7253 | -44.822102 | 2025-07-16 00:41:00 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2a81e144-433c-36e3-b457-7dc9e0489792 | -12.48 | -46.923 | 2025-07-16 00:41:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2cae4a38-feaf-3f68-8490-7404346bc2cd | -18.790701 | -51.298599 | 2025-07-16 00:41:00 | METOP-C | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 5c2e38dc-7f28-33e0-9c4b-896cf4699c68 | -10.287 | -47.617199 | 2025-07-16 00:41:00 | METOP-C | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5a56d38a-dea2-3879-8e01-5e642c26c7ff | -4.1098 | -48.206402 | 2025-07-16 00:41:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a6a82c73-6173-380d-8731-c59d34ca18c2 | -12.0235 | -47.7771 | 2025-07-16 00:41:00 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 476e17ce-51f4-3d62-8339-165d654faea9 | -12.025 | -47.7841 | 2025-07-16 00:41:00 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8e56fcd8-9f7e-3fdf-90a4-10aea36b27b6 | -20.0819 | -47.644501 | 2025-07-16 00:41:00 | METOP-C | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| a4709d02-c8e7-371c-99bb-80dd1ce1682c | -10.8902 | -49.2048 | 2025-07-16 00:41:00 | METOP-C | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4fd76b74-7e80-3d9e-a8bf-8fa2d057f18a | -10.5702 | -49.106899 | 2025-07-16 00:41:00 | METOP-C | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4ba5cedd-1611-3f33-98a7-9244a78c41e7 | -4.7835 | -45.335201 | 2025-07-16 00:41:00 | METOP-C | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4f9e2edf-0c2b-3e57-8c6a-51c1b604d3c6 | -10.5718 | -49.114201 | 2025-07-16 00:41:00 | METOP-C | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 47d9d333-6039-3056-9980-ed68a62d8749 | -5.5366 | -43.896801 | 2025-07-16 00:41:00 | METOP-C | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2fdeb181-9170-3d2d-89f9-c3d50fafbb98 | -4.2919 | -48.056301 | 2025-07-16 00:41:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9827b0cc-e25d-369c-9e4c-406b49284f6d | -5.6685 | -43.7146 | 2025-07-16 00:41:00 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 60e40c95-2635-3071-b8bc-97e89115f457 | -8.9127 | -47.334702 | 2025-07-16 00:41:00 | METOP-C | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f0292751-adc1-3268-ac55-daf5bb6f4091 | -13.0998 | -47.294601 | 2025-07-16 00:41:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bf048a61-a6ea-3f39-8e5f-e8492100e811 | -4.303 | -48.104698 | 2025-07-16 00:41:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bcd32eae-9b24-3b9b-9e76-e6abd6c516e1 | -14.1595 | -42.846802 | 2025-07-16 00:41:00 | METOP-C | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 7dd360f2-5d67-32f2-b4f6-d7432d75fe75 | -5.4633 | -45.330299 | 2025-07-16 00:41:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README4.md)

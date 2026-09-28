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

## Dados Diários - Página 126

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 37cee18c-db50-3e5e-9ed5-7cc02682d2d2 | 3.41747 | -51.52394 | 2026-09-28 16:30:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 6.9 |
| d7d64b93-afd7-35da-b85e-9cc07b332c8c | 3.73683 | -51.72663 | 2026-09-28 16:30:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 28a5d4f5-3415-343e-a9aa-f2dccef4ff58 | 4.00636 | -51.64299 | 2026-09-28 16:30:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 11.5 |
| f7200aea-065d-36d6-95b7-bad7c63450c4 | 4.01081 | -51.64368 | 2026-09-28 16:30:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 85e774c9-6d3e-3c6f-910a-7745ebe13841 | 4.00708 | -51.63861 | 2026-09-28 16:30:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 7.9 |
| e13e81ec-f5d9-3c0a-951d-52a91b69077d | 3.42122 | -51.52904 | 2026-09-28 16:30:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.4 |
| f886df8c-8e82-3c5b-94c6-f12307eeb30e | 3.42192 | -51.52466 | 2026-09-28 16:30:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 6.9 |
| bf71cf97-3955-3d0b-8ee7-ec2b327e6e20 | 3.48177 | -51.48497 | 2026-09-28 16:30:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 839eca1f-58ee-3fff-bc81-9961e84999d8 | 3.4862 | -51.48567 | 2026-09-28 16:30:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 1972cfd6-4017-353c-aec6-48292ee5f63e | 3.97535 | -51.69225 | 2026-09-28 16:30:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 7.2 |
| d9a625d8-e260-3247-ab91-23ec0c6be2e6 | 3.73447 | -51.71257 | 2026-09-28 16:30:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5b097c47-ea1b-3fd7-bda9-bd3da0027e01 | -11.9777 | -50.7371 | 2026-09-28 16:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 113.0 |
| 508ecfdd-fe68-3448-b763-03564681a5e0 | -11.924 | -50.5081 | 2026-09-28 16:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 103.7 |
| 5093c9fd-0d6d-3ce1-aaa2-db97cf3b5d20 | -10.2565 | -50.5185 | 2026-09-28 16:40:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 101.7 |
| e7b5063c-31a3-3c32-a270-33b2544b109d | -1.3008 | -49.0826 | 2026-09-28 16:40:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 82.7 |
| d06ff25d-1faa-3557-9150-22545d8bc022 | -11.9968 | -50.7349 | 2026-09-28 16:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 110.1 |
| 160afca6-7fb5-37e2-9a30-4c52295af864 | -12.1175 | -50.3135 | 2026-09-28 16:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 102.2 |
| bcfe362d-60c5-396d-99e2-bfc171933a35 | -12.1553 | -50.3305 | 2026-09-28 16:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 106.3 |
| ffc8763a-bb3f-372a-bd6b-1394b16390a4 | -11.9586 | -50.7393 | 2026-09-28 16:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 123.7 |
| 983cf074-c0a9-3317-aea2-7ffd9cc17d63 | -11.077 | -51.3462 | 2026-09-28 16:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 101.5 |
| a38fab92-5da3-355b-8674-e0d3ba859a25 | -11.905 | -50.5103 | 2026-09-28 16:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 107.1 |
| 86665bb5-ffac-3596-acfd-ebd5797a4165 | -11.7141 | -50.5538 | 2026-09-28 16:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 119.3 |
| 61645031-33b7-38f3-b6f7-ce032540a135 | -12.1872 | -50.7339 | 2026-09-28 16:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 88.5 |
| a79632e0-f90f-35bc-b0cb-950ed4f28078 | -12.1741 | -50.3497 | 2026-09-28 16:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 4042c495-ac8e-391b-96c0-ee9edc752cc4 | -1.3008 | -49.0613 | 2026-09-28 16:40:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 90.3 |
| 6d769f3f-dd3d-3562-8de5-df80314a1a54 | -11.9402 | -50.6987 | 2026-09-28 16:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 85.0 |
| b7b0e2aa-2c3e-3876-a117-3b003a2d5ed7 | -10.7115 | -60.7312 | 2026-09-28 16:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 104.2 |
| 69bbdc7e-5180-3331-bf40-2393ab4b0591 | -11.7329 | -50.573 | 2026-09-28 16:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 116.7 |
| 5b460daf-c3eb-3b14-982e-58503113347a | -12.0609 | -50.2773 | 2026-09-28 16:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 117.3 |
| f5edbf9a-d27f-39fc-849a-eeeb1732c740 | -12.2254 | -50.7294 | 2026-09-28 16:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 95.1 |
| fa50ea3f-5ffb-3f75-aedd-14d6501094de | -12.1872 | -50.7339 | 2026-09-28 16:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 1ccdda61-5c67-3ce6-bf24-bbc71e720890 | -11.751 | -50.6351 | 2026-09-28 16:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 502aff0a-d022-3ea3-928f-1497997e9793 | -11.0956 | -51.3654 | 2026-09-28 16:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 109.1 |
| 84c84881-f764-324e-b0ee-04030968b471 | -10.2565 | -50.5185 | 2026-09-28 16:50:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 97.1 |
| baf43717-662e-396e-89b3-562089213d39 | -11.0764 | -51.3885 | 2026-09-28 16:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 93.4 |
| e9fbd6a3-6b65-3866-959e-4024034ce81b | -11.9777 | -50.7371 | 2026-09-28 16:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 109.5 |
| 0d7b607c-2428-3e1c-9b21-26bd76836c04 | -11.9612 | -50.568 | 2026-09-28 16:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 102.0 |
| 7c61c4ea-ead7-39fb-b9a5-1ffde787e9a4 | -11.5628 | -50.5069 | 2026-09-28 16:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 103.5 |
| 5b660832-165d-327a-9812-fcba0aa8576a | -11.8853 | -50.5554 | 2026-09-28 16:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 9903394a-3e24-3b95-925b-d74d373b5a00 | -12.2248 | -50.7722 | 2026-09-28 16:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 96.4 |
| c72f4107-ba63-3787-939b-d7a2255d1aeb | -10.9156 | -50.6845 | 2026-09-28 16:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 112.0 |
| 74e361e0-11fe-3f69-b5bc-ce3377e3eca2 | -11.5818 | -50.5047 | 2026-09-28 16:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 103.1 |
| ea3cb4d5-5bec-38fb-9dff-f8b02f8bb009 | -12.2639 | -50.7034 | 2026-09-28 16:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 72b81f52-f307-3166-975c-f279470abbe8 | -11.0767 | -51.3674 | 2026-09-28 16:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 99.6 |
| f67ff9db-398b-3c71-ab36-a285f1c7fe53 | -10.8967 | -50.6866 | 2026-09-28 16:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 137.8 |
| 27e116d3-7c9c-358e-b453-c81c5c737611 | -11.7138 | -50.5752 | 2026-09-28 16:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 113.9 |
| 9eb5d64e-d83f-3f38-9449-612d810726ff | -12.2251 | -50.7508 | 2026-09-28 16:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 104.9 |
| d7353a12-2c84-3117-aa65-77432012453c | -11.7329 | -50.573 | 2026-09-28 16:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 113.9 |
| f5e1ddab-01a9-38ed-9cb9-3138a41be993 | -12.2439 | -50.7699 | 2026-09-28 16:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 685cad8b-63a2-3ec6-ae2a-0d09adf4a872 | -1.3008 | -49.0613 | 2026-09-28 16:50:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 90.4 |
| 3f9dfcd0-bedc-3280-85f9-9cf10ccab05c | -11.8472 | -50.5598 | 2026-09-28 16:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 111.4 |
| 21694605-9845-352e-a7c2-982f89b7d495 | -1.3008 | -49.0826 | 2026-09-28 16:50:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 9741e894-1549-3aae-8550-b71d1fae2360 | -9.4813 | -46.3646 | 2026-09-28 17:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 110.0 |
| 424472d3-1a54-3e2e-8c62-aa5d6a163f6d | -11.058 | -51.3482 | 2026-09-28 17:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 10bf26a3-1017-316c-b219-c3529ac73991 | -12.1362 | -50.3328 | 2026-09-28 17:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 111.1 |
| dc10a9d6-763f-3cd7-8b79-ecbb745468be | -11.0956 | -51.3654 | 2026-09-28 17:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 110.5 |
| 96a54227-3870-3e84-a1d0-171d8517db08 | -12.1869 | -50.7553 | 2026-09-28 17:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 105.8 |
| 01eedae7-dcf4-3a1d-8ef8-aad6c62cdcc9 | -12.1737 | -50.3712 | 2026-09-28 17:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 96.6 |
| f6c7600e-2c36-381f-aa97-03ec7868918b | -11.0764 | -51.3885 | 2026-09-28 17:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 9fc306e1-24e4-3456-a6b7-984dd5392468 | -12.2254 | -50.7294 | 2026-09-28 17:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 95.2 |
| dd863ff6-68d4-3e37-a218-229d8917f831 | -11.9971 | -50.7135 | 2026-09-28 17:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 79629710-a13d-3230-ade9-19d0066c3618 | -12.289 | -50.3143 | 2026-09-28 17:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 94.7 |
| eec61dd7-c7f5-3ea3-8e53-defeb890a90b | -12.1547 | -50.3735 | 2026-09-28 17:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 132.9 |
| 5e6ae177-7eb0-3862-9e8a-bcf6d0960a05 | -11.8669 | -50.5147 | 2026-09-28 17:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 106.2 |
| 9555b05f-dcca-3c08-aad4-d52ea60ccb49 | -12.2442 | -50.7485 | 2026-09-28 17:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 98.0 |
| fc27546b-071e-3e9f-a7f7-801eeb8a01f5 | -11.8859 | -50.5125 | 2026-09-28 17:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 106.3 |
| f7b6b7e9-d4ef-36df-8984-f413f8861ac6 | -11.5628 | -50.5069 | 2026-09-28 17:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 107.4 |
| dcfb2f6e-fc58-3210-9027-220786f0dfb9 | -12.206 | -50.7531 | 2026-09-28 17:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 104.8 |
| 07945689-ca0a-33e6-9bc8-21108eea478b | -12.1553 | -50.3305 | 2026-09-28 17:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 58d73abc-0b13-3f98-8245-14053cee4605 | -9.9784 | -50.1412 | 2026-09-28 17:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 136.3 |
| f15e4838-1a76-3a8b-90d8-f3e1bddefb63 | -10.2565 | -50.5185 | 2026-09-28 17:00:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 92.3 |
| 5fed7d63-1644-3620-ab85-aaae52b7fa45 | -12.1744 | -50.3282 | 2026-09-28 17:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 89.4 |
| bb2301d7-52c3-3df7-a0ed-0bcf0dbabb00 | -11.9047 | -50.5317 | 2026-09-28 17:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 100.4 |
| d1e59c04-1f9d-31ff-a9e9-50c89cf7c9cb | -12.2251 | -50.7508 | 2026-09-28 17:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 108.6 |
| b850f022-0dfa-352b-b3b1-df9626ce6454 | -10.824 | -60.7246 | 2026-09-28 17:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 118.4 |
| 246d788e-7c16-3e19-b768-e8df11de593e | -20.45755 | -46.22521 | 2026-09-28 17:05:00 | NOAA-21 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 15.1 |
| ada16e70-941a-3025-b861-b8bb63cbb3c9 | -20.77845 | -51.29825 | 2026-09-28 17:05:00 | NOAA-21 | ANDRADINA | SÃO PAULO | Brasil | 3502101 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.7 |
| 74ff1970-ab0f-3b7d-aa4a-bf3c78676cb1 | -19.03831 | -42.16825 | 2026-09-28 17:05:00 | NOAA-21 | PERIQUITO | MINAS GERAIS | Brasil | 3149952 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.9 |
| e2ff25b9-128d-3088-92f6-8af9dfcf3f37 | -23.10325 | -50.91981 | 2026-09-28 17:05:00 | NOAA-21 | RANCHO ALEGRE | PARANÁ | Brasil | 4121307 | 41 | 33 | nan | nan | nan | Mata Atlântica | 13.6 |
| b215ab8c-4f4a-3fdc-834f-a8ed2d7ac378 | -20.99975 | -47.06504 | 2026-09-28 17:05:00 | NOAA-21 | SÃO SEBASTIÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3164704 | 31 | 33 | nan | nan | nan | Cerrado | 52.5 |
| 0b10d06c-8c2e-38fd-9cea-7284c81a93ee | -20.96687 | -44.17426 | 2026-09-28 17:05:00 | NOAA-21 | RESENDE COSTA | MINAS GERAIS | Brasil | 3154200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 14156be6-53f0-31d7-974c-004494b430b3 | -20.35648 | -46.38365 | 2026-09-28 17:05:00 | NOAA-21 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e82bc829-eef6-3bfa-8ef5-9f455446060c | -21.23695 | -43.94298 | 2026-09-28 17:05:00 | NOAA-21 | BARBACENA | MINAS GERAIS | Brasil | 3105608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.2 |
| dae95858-9fc3-3434-a1ab-ebf05e1eb80b | -21.65104 | -51.99547 | 2026-09-28 17:05:00 | NOAA-21 | PRESIDENTE EPITÁCIO | SÃO PAULO | Brasil | 3541307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| edd111a7-a79a-3e59-995a-0c56b4734abd | -20.23653 | -44.17532 | 2026-09-28 17:05:00 | NOAA-21 | BONFIM | MINAS GERAIS | Brasil | 3108107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 67d7fffa-4c7b-3ea9-a12d-162a48ce3ff1 | -21.32014 | -43.98571 | 2026-09-28 17:05:00 | NOAA-21 | BARBACENA | MINAS GERAIS | Brasil | 3105608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.7 |
| f5abba55-41e2-314c-8601-bbbff8df5dfc | -20.76241 | -51.30494 | 2026-09-28 17:05:00 | NOAA-21 | ANDRADINA | SÃO PAULO | Brasil | 3502101 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 14928a5f-d148-3311-b67c-36558ef7cf12 | -22.84808 | -49.36121 | 2026-09-28 17:05:00 | NOAA-21 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 17.5 |
| c00d3cd0-5f13-3dda-a902-2b44c0841cac | -21.60531 | -46.54978 | 2026-09-28 17:05:00 | NOAA-21 | CACONDE | SÃO PAULO | Brasil | 3508702 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| d00b5807-a881-3370-8a52-3eeaa1991cab | -23.13642 | -50.91374 | 2026-09-28 17:05:00 | NOAA-21 | RANCHO ALEGRE | PARANÁ | Brasil | 4121307 | 41 | 33 | nan | nan | nan | Mata Atlântica | 16.1 |
| f7907d88-9a80-3a44-8dc9-fb6c79b82fbf | -19.9741 | -43.42484 | 2026-09-28 17:05:00 | NOAA-21 | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| e6ef0720-1d5b-3fc7-b4c0-f36bb41ee444 | -20.95631 | -45.81361 | 2026-09-28 17:05:00 | NOAA-21 | ILICÍNEA | MINAS GERAIS | Brasil | 3130507 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e4de8b9e-9a90-3c2e-aabc-98860ce73a46 | -19.49783 | -45.90601 | 2026-09-28 17:05:00 | NOAA-21 | SANTA ROSA DA SERRA | MINAS GERAIS | Brasil | 3159704 | 31 | 33 | nan | nan | nan | Cerrado | 11.7 |
| aaed9bd4-e310-3320-856f-ba13b2bf1462 | -20.76574 | -51.30434 | 2026-09-28 17:05:00 | NOAA-21 | ANDRADINA | SÃO PAULO | Brasil | 3502101 | 35 | 33 | nan | nan | nan | Mata Atlântica | 35.5 |
| 4b9a2b31-2e48-3c50-972b-370afcf8181f | -21.73052 | -45.83574 | 2026-09-28 17:05:00 | NOAA-21 | CARVALHÓPOLIS | MINAS GERAIS | Brasil | 3114709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| c62ab93d-56e5-301f-89b7-fdcf1fcd198a | -23.13701 | -50.9175 | 2026-09-28 17:05:00 | NOAA-21 | RANCHO ALEGRE | PARANÁ | Brasil | 4121307 | 41 | 33 | nan | nan | nan | Mata Atlântica | 16.1 |
| 0c27a766-cbdf-35d4-994d-60c0a449d244 | -19.44926 | -41.94424 | 2026-09-28 17:05:00 | NOAA-21 | INHAPIM | MINAS GERAIS | Brasil | 3130903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| c1a589bb-a86e-3813-b0b7-fe4d99fe2b3f | -21.10332 | -46.26681 | 2026-09-28 17:05:00 | NOAA-21 | CONCEIÇÃO DA APARECIDA | MINAS GERAIS | Brasil | 3117108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| d8902f1b-080e-3c8b-9c9c-3857c2063df5 | -21.21806 | -46.70615 | 2026-09-28 17:05:00 | NOAA-21 | GUAXUPÉ | MINAS GERAIS | Brasil | 3128709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 03449354-94d3-39ac-a011-c25b09202b20 | -21.79263 | -43.81474 | 2026-09-28 17:05:00 | NOAA-21 | LIMA DUARTE | MINAS GERAIS | Brasil | 3138609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |


[Clique aqui para ver as próximas entradas](README127.md)

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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b75b410f-4df5-32d3-85b5-2560cf0753c4 | -12.9183 | -45.0517 | 2025-03-20 00:10:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 0b2541e0-bd76-3c5f-ade4-582a2c758ba3 | -12.899 | -45.0549 | 2025-03-20 00:10:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 84.5 |
| a1833e6c-f328-3a8c-b277-60530e824b90 | -12.9183 | -45.0517 | 2025-03-20 00:20:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 123.8 |
| 9f8ab8b7-4298-36b7-b5e0-37dfe556bbad | -12.9183 | -45.0517 | 2025-03-20 00:30:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 119.9 |
| f005d2fd-6101-376b-8d7f-67fac0de4fbe | -19.83624 | -40.11664 | 2025-03-20 00:37:00 | TERRA_M-M | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| bb8ae983-5d3a-3122-8d2a-3bcf297b2ed0 | -19.8305 | -40.10955 | 2025-03-20 00:37:00 | TERRA_M-M | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 36006d27-8395-31da-9151-dd621d9cd7c2 | -14.83268 | -46.54718 | 2025-03-20 00:39:00 | TERRA_M-M | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| ca872f16-f1f5-376e-a433-6b0a98cc3d43 | -12.58704 | -48.3279 | 2025-03-20 00:39:00 | TERRA_M-M | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 33bf692e-5acf-3a7c-b988-d35e7a3591bb | -12.90256 | -45.04819 | 2025-03-20 00:39:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 32.5 |
| 77983a71-a3f3-31ea-84be-f09cfd0da5eb | -12.91414 | -45.06534 | 2025-03-20 00:39:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 50.3 |
| 570c7514-9c09-3744-a539-22dbd2502d46 | -12.09308 | -45.63676 | 2025-03-20 00:39:00 | TERRA_M-M | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 59b63b60-7954-3ce1-8218-e5b2765b32f5 | -12.10196 | -45.63543 | 2025-03-20 00:39:00 | TERRA_M-M | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 4b8d1dc9-ac91-31ce-9e98-be75476ab85c | -12.10068 | -45.62636 | 2025-03-20 00:39:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| e2380704-9f93-3727-bb68-13c33ebae91a | -12.88637 | -44.87001 | 2025-03-20 00:39:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| b676c0bd-00ba-3eba-b67d-e464eda6cc5e | -18.43703 | -41.87817 | 2025-03-20 00:39:00 | TERRA_M-M | FREI INOCÊNCIO | MINAS GERAIS | Brasil | 3126901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 15f34b6d-6796-3448-9f2c-c11c1802cbd9 | -12.90124 | -45.03894 | 2025-03-20 00:39:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 22.8 |
| ba7e8ab9-4974-3b33-927f-caaa8b2ac70d | -12.91282 | -45.05609 | 2025-03-20 00:39:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 1bc9bc03-1e0b-34be-9e39-9ad3bcc57d73 | -12.18341 | -41.375 | 2025-03-20 00:39:00 | TERRA_M-M | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 8.1 |
| ad37c580-264e-3b93-9a6d-ded4b61c7e2f | -12.9102 | -45.03757 | 2025-03-20 00:39:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 5ce3c99c-8087-3025-949c-0acc47b9bb6e | -10.6512 | -44.39481 | 2025-03-20 00:39:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 295e8e42-739e-360c-adbe-a04f6d50c854 | -12.90519 | -45.06671 | 2025-03-20 00:39:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 0a4dfc43-d58e-3a2e-86a3-224506934d7c | -10.66054 | -44.39336 | 2025-03-20 00:39:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 554987e5-2e8f-3a26-ae2d-1264c2694905 | -10.47893 | -47.35133 | 2025-03-20 00:39:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| ca5db424-c0fb-3732-91ed-b742844a211d | -12.90387 | -45.05745 | 2025-03-20 00:39:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 27.8 |
| 3f05a70d-9252-311c-ab15-efa9621ab077 | -12.18312 | -41.36938 | 2025-03-20 00:39:00 | TERRA_M-M | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 11.6 |
| caa3655f-fc34-380c-b0ee-8461207ac274 | -10.35635 | -44.83627 | 2025-03-20 00:39:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 2b5d4088-60de-3de3-adee-186379c132f8 | -10.48926 | -47.35324 | 2025-03-20 00:39:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ee16f07a-fc26-3042-b7a1-84acff5ae7a6 | -11.57536 | -47.63147 | 2025-03-20 00:39:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 52310b5f-096f-3d02-9981-8983b3e3ff24 | -14.83394 | -46.55651 | 2025-03-20 00:39:00 | TERRA_M-M | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 93df7ea9-061b-3ed9-ad9b-904b0e33e7c8 | -16.08267 | -40.87811 | 2025-03-20 00:39:00 | TERRA_M-M | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| 476007d9-beb5-31e5-bb33-26213aadee9d | -12.91151 | -45.04683 | 2025-03-20 00:39:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 31bc0d11-3ef1-3120-a5d5-0af444501b0b | -12.0918 | -45.62769 | 2025-03-20 00:39:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| f6c9ac0f-1a08-3b5c-b730-733dde8d3ed7 | -16.08433 | -46.62247 | 2025-03-20 00:39:00 | TERRA_M-M | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 96a3d1ff-ec0a-3af6-b997-7593ea3a0573 | -12.9183 | -45.0517 | 2025-03-20 00:40:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 102.6 |
| f0fc6256-bd67-39ba-84f7-d78a00759e5d | -7.06493 | -44.38241 | 2025-03-20 00:41:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 16b89ca3-1e49-3903-9074-3c597c3724cb | -7.05516 | -44.3839 | 2025-03-20 00:41:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 1e47931c-f61e-367f-9f01-68bf63c150cf | -7.0633 | -44.37127 | 2025-03-20 00:41:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| eb77b7e6-bd59-3bb3-a8d7-c0ce013350af | -12.9183 | -45.0517 | 2025-03-20 00:50:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 6e8683cf-f6af-33c7-8c3f-6c9be65e7e10 | -12.9183 | -45.0517 | 2025-03-20 01:00:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 90.7 |
| e472260f-83b9-37dd-b989-073cac079fef | -12.9183 | -45.0517 | 2025-03-20 01:10:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 3bd042c8-cfdc-3173-ba78-581ac0568dea | -12.9183 | -45.0517 | 2025-03-20 01:20:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 39f3139c-937e-3717-ae99-854c35814007 | -12.9183 | -45.0517 | 2025-03-20 01:40:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 3a1da90f-19db-391a-bfda-2c4e37e4fa5f | -12.9183 | -45.0517 | 2025-03-20 01:50:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 5a6bb4fe-b1c3-3a91-9778-1d13be227603 | -12.9183 | -45.0517 | 2025-03-20 02:00:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 13798ffd-5cc4-3f91-a3e9-f89447fe5491 | -12.9183 | -45.0517 | 2025-03-20 02:10:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 71.1 |
| b0fed1e5-b064-306e-98da-5108fde74e62 | -12.9183 | -45.0517 | 2025-03-20 02:20:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 0637f15f-a9c8-3cbb-be67-1253e411eb00 | -6.5631 | -51.1126 | 2025-03-20 04:00:00 | GOES-16 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 6980266c-ed32-3de0-8439-d50fd3cf791a | -6.24181 | -44.82531 | 2025-03-20 04:02:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3a5bb114-f475-36af-90d2-e649e070406c | -10.47916 | -47.34769 | 2025-03-20 04:02:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4b832661-7328-30df-a84a-5b6ec157a5fc | -12.86074 | -38.36715 | 2025-03-20 04:02:00 | NPP-375D | SALVADOR | BAHIA | Brasil | 2927408 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 2a5f224a-6968-30a0-b52c-bfcc0206a49a | -11.77011 | -37.88954 | 2025-03-20 04:02:00 | NPP-375D | ESPLANADA | BAHIA | Brasil | 2910602 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d093e8e7-e625-3cac-961d-553743498753 | -7.05943 | -44.37433 | 2025-03-20 04:02:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 0b8c8672-7bc5-380b-bba5-a160fe5b70e9 | -8.7355 | -36.83014 | 2025-03-20 04:02:00 | NPP-375D | PEDRA | PERNAMBUCO | Brasil | 2610806 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 7b731b1f-620c-3d44-9188-58a288adf90c | -12.90748 | -45.05197 | 2025-03-20 04:02:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0778a8e0-d49d-3db7-a17f-08b74591c73e | -12.09176 | -45.62946 | 2025-03-20 04:02:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0a545cc5-e8db-38a4-87d1-f878ea0bf561 | -7.05995 | -44.37648 | 2025-03-20 04:02:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 019f5e70-7ef3-3fa0-bf21-ddf83a7cb949 | -11.21369 | -37.7319 | 2025-03-20 04:02:00 | NPP-375D | ITABAIANINHA | SERGIPE | Brasil | 2803005 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| f0f85e41-1aee-3100-b5a6-e7f3d87c6445 | -12.09952 | -45.63087 | 2025-03-20 04:02:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e705cbed-3c98-3645-85d9-c9c84ee2a481 | -12.91027 | -45.06388 | 2025-03-20 04:02:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1a488cfa-7296-39cd-845a-b753ecefc6d3 | -12.29485 | -43.50045 | 2025-03-20 04:02:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3b792d8a-ebe3-301e-a2dd-0b766cec0af1 | -7.06382 | -44.37713 | 2025-03-20 04:02:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| df1ddc68-70c7-35cf-af2e-c7e325a3a503 | -12.29833 | -43.50105 | 2025-03-20 04:02:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1c55ec1e-b338-3a99-9b94-54788920efa9 | -12.1495 | -40.2988 | 2025-03-20 04:02:00 | NPP-375D | MACAJUBA | BAHIA | Brasil | 2919603 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 68d5b415-1a20-3bac-bee0-8a8c91817559 | -6.8357 | -44.3223 | 2025-03-20 04:02:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ce33b33a-83f3-355d-8995-07f91a5178cd | -10.35807 | -44.84193 | 2025-03-20 04:02:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ef8d13da-a197-3818-9821-577e0d5bcf74 | -12.90824 | -45.04747 | 2025-03-20 04:02:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c7e6c9d2-dfc0-3c07-8d30-4980cb94755f | -7.05787 | -44.38389 | 2025-03-20 04:02:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| fc5ec608-f052-3772-8145-c936bb17c41c | -12.1742 | -44.05449 | 2025-03-20 04:02:00 | NPP-375D | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7d55dded-bad8-3951-98c9-83cbc77548f4 | -12.906 | -45.04456 | 2025-03-20 04:02:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4d2d9fe5-d0dc-374a-b9c5-b2b694115cce | -12.90229 | -45.04389 | 2025-03-20 04:02:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fa2b887a-1e1a-3620-a085-3406f054aa35 | -11.6403 | -37.78915 | 2025-03-20 04:02:00 | NPP-375D | RIO REAL | BAHIA | Brasil | 2927002 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 992bc8ee-4f80-3a2f-a0bf-199ba1191654 | -11.4595 | -39.94088 | 2025-03-20 04:02:00 | NPP-375D | SÃO JOSÉ DO JACUÍPE | BAHIA | Brasil | 2929370 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 1943c294-e213-3ba0-b30e-eb60777c4a50 | -10.87966 | -44.17352 | 2025-03-20 04:02:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f081dbb1-9900-3590-ad64-1979ddcf5383 | -12.09564 | -45.63016 | 2025-03-20 04:02:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| af498477-6045-31fe-abed-04afd19b0610 | -13.18768 | -39.69425 | 2025-03-20 04:02:00 | NPP-375D | UBAÍRA | BAHIA | Brasil | 2932101 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| e3064587-32c6-360e-b0d1-477da938d5f6 | -12.89858 | -45.04322 | 2025-03-20 04:02:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f5b16646-3c2c-3bb2-87f5-0f7741a21903 | -9.22501 | -37.77176 | 2025-03-20 04:02:00 | NPP-375D | INHAPI | ALAGOAS | Brasil | 2703304 | 27 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 3233d64b-97a8-3ecb-b81b-65a2c965369b | -12.29192 | -43.54016 | 2025-03-20 04:02:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| eec50fce-e4c7-3fc2-ac9f-e0ee0b618585 | -7.05832 | -44.38603 | 2025-03-20 04:02:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 87039e1a-a6f0-3f82-97bc-efbb423f89ec | -10.35888 | -44.83724 | 2025-03-20 04:02:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 77a23e30-12ae-30d0-b691-8599a890031b | -12.39819 | -38.7926 | 2025-03-20 04:02:00 | NPP-375D | AMÉLIA RODRIGUES | BAHIA | Brasil | 2901106 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a634bd81-2111-36e4-b531-f3559659d819 | -12.90892 | -45.04972 | 2025-03-20 04:02:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d7a65b2e-6bca-3c41-a015-9aca57a1f84e | -12.09262 | -45.62453 | 2025-03-20 04:02:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5d743336-36e0-375a-bdfb-62e4a0a4668c | -12.09866 | -45.63581 | 2025-03-20 04:02:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b4e34b85-b592-33e8-97e7-ce4e252a227a | -12.90521 | -45.04905 | 2025-03-20 04:02:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4c28f23f-6f62-3deb-9618-debd8264ce96 | -12.0978 | -45.64076 | 2025-03-20 04:02:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3d1bbf0c-3a1c-380c-84c3-bb78fbd29ab3 | -12.90453 | -45.04679 | 2025-03-20 04:02:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b4eb675e-589b-3452-9a85-dd68497e8433 | -12.90376 | -45.0513 | 2025-03-20 04:02:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fe2447d7-5359-3f4a-89e7-2d89bd1feb9f | -9.41605 | -40.51757 | 2025-03-20 04:02:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| e458665b-bb71-388b-99d3-effc90bda0d8 | -7.05865 | -44.3791 | 2025-03-20 04:02:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| e410bcf5-9ff7-3dd8-8968-d3aeae8481f6 | -12.14671 | -40.2947 | 2025-03-20 04:02:00 | NPP-375D | MACAJUBA | BAHIA | Brasil | 2919603 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 121cca48-6acc-37ee-a496-f05f25bbc4b8 | -12.28926 | -43.5387 | 2025-03-20 04:02:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 96bdcbe5-abc8-39b9-995e-1d4e67453880 | -7.06463 | -44.37239 | 2025-03-20 04:02:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| fcb4dc93-72cc-36dc-b0ac-1b4ef141d01e | -12.90158 | -45.04162 | 2025-03-20 04:02:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e0827e1f-74d4-3fcb-9d4a-348e0472958c | -7.06331 | -44.375 | 2025-03-20 04:02:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 38aab4db-2fd7-3576-950e-7d6874c2660d | -12.91263 | -45.05038 | 2025-03-20 04:02:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cc238029-4685-315d-93d7-26617ee73851 | -12.90971 | -45.04522 | 2025-03-20 04:02:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8f7c691d-d51f-3a9a-aeb4-421af8ef2855 | -12.09478 | -45.6351 | 2025-03-20 04:02:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 18b8cb45-8f7c-38b2-aaa9-53c481d191d2 | -10.48282 | -47.35293 | 2025-03-20 04:02:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 10aa7b99-b63d-3a8c-bb55-8cb142bcfdf9 | -12.9015 | -45.04839 | 2025-03-20 04:02:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README2.md)

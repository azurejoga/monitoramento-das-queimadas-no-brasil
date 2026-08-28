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

## Dados Diários - Página 183

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 108c6e2d-d189-3b33-95b5-8242f6ab4c39 | -11.7167 | -54.5244 | 2026-08-28 20:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 232.5 |
| 23e20eea-a668-3b9c-9f7d-89629cf81d9d | -6.7247 | -60.0189 | 2026-08-28 20:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 163.9 |
| 4776a489-8907-38b5-bbbf-0510daf788f3 | -5.2448 | -43.7225 | 2026-08-28 20:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 115.5 |
| 8c25936f-45c4-3cbb-b16b-295a42c77cd7 | -4.1935 | -54.5555 | 2026-08-28 20:40:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 89.5 |
| a8cea295-2aed-3858-b6d8-ad7295ace9d0 | -4.1934 | -54.5755 | 2026-08-28 20:40:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 208.0 |
| 02fbf78c-2b97-3c7c-a82f-c2a5467c1085 | -4.5694 | -44.0657 | 2026-08-28 20:40:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 356.0 |
| d42f7dac-5cd4-3a96-b2ab-fc8f4a441727 | -6.7699 | -55.6644 | 2026-08-28 20:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 254.4 |
| 59ae10ee-9b0a-3e91-8cb2-76da64b2e00c | -9.971 | -53.9214 | 2026-08-28 20:40:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 95.3 |
| 0f76c16e-3cc4-391e-860e-ad31718212aa | -14.8817 | -52.6293 | 2026-08-28 20:40:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 914e2083-6914-3723-b094-5b68118d4b4d | -14.1597 | -53.1219 | 2026-08-28 20:40:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 103.3 |
| b3e2ccbe-ba13-3747-8ccf-1cba3d0a64b4 | -5.8895 | -57.7513 | 2026-08-28 20:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 291.3 |
| 2f2a527c-33da-3160-a151-d3fc70e9c45f | -7.2807 | -49.969 | 2026-08-28 20:40:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 128.2 |
| 73aabbea-6fac-33ac-9e0c-22813f4bbcf1 | -6.7504 | -58.7268 | 2026-08-28 20:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 80.0 |
| c866b376-dc14-30b6-ae02-3924087468d6 | -9.8028 | -46.373 | 2026-08-28 20:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 208.1 |
| 18df3777-c901-3464-a313-805a6d587de4 | -5.9078 | -57.77 | 2026-08-28 20:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 73.4 |
| c8e9c566-cd26-3a3d-bb59-baf2d84923ef | -14.1978 | -48.7673 | 2026-08-28 20:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 3b7cf40b-7717-3761-a83d-ab000968af72 | -8.5366 | -55.2625 | 2026-08-28 20:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 108.1 |
| b6159b85-59ef-382d-9d93-39f243df9e14 | -14.3569 | -51.6995 | 2026-08-28 20:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 2a65ce6f-40e6-3ce7-b93e-57f923238a6b | -9.9102 | -60.4287 | 2026-08-28 20:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 177.8 |
| 0db04a1a-0f54-3522-81ac-45d807374edb | -6.7652 | -63.054 | 2026-08-28 20:40:00 | GOES-19 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 91.2 |
| 3d4b45ca-9787-3c58-bf5d-c6c90f692104 | -8.6012 | -70.2192 | 2026-08-28 20:40:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 137.6 |
| 2b81b71e-1338-311f-a4fc-7b5c35a55b4e | -9.0198 | -57.5574 | 2026-08-28 20:40:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 137.6 |
| b8813566-4ec7-37e5-b28a-7def68e05302 | -5.2634 | -43.7444 | 2026-08-28 20:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 67dc78c2-2c67-3a54-97ce-490024dcbcbd | -8.5968 | -54.7957 | 2026-08-28 20:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 98.9 |
| cbf6b409-ab7e-3235-adc2-03bbd9096f8d | -11.2106 | -51.2688 | 2026-08-28 20:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 582ffe39-24ea-3848-8db8-e3dde83c8cb6 | -8.8219 | -70.638 | 2026-08-28 20:40:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 35031e50-5fc4-36a7-9564-23366f7a615e | -6.0005 | -57.6689 | 2026-08-28 20:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| d9e25d29-742b-3afa-8466-91017f615598 | -6.9521 | -58.9506 | 2026-08-28 20:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 93.3 |
| 28fa863f-11a5-3b57-9680-9b2425402e57 | -9.9474 | -60.446 | 2026-08-28 20:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 116.0 |
| cb5e8d47-e847-3a92-b1bc-b09ab7ef7a5d | -14.9389 | -56.3011 | 2026-08-28 20:40:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 117.3 |
| f80c98f4-9f69-38f5-8b29-b356345df189 | -9.1523 | -49.9853 | 2026-08-28 20:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 92.8 |
| 757a2a9a-48bf-3c83-b576-4cf6a814734b | -8.0115 | -47.9943 | 2026-08-28 20:40:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 134.3 |
| 839c0eb6-eeca-36d8-9df9-7f4a026570cb | -8.0301 | -48.0145 | 2026-08-28 20:40:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 120.5 |
| a8fdae19-6a12-35d5-8b82-c3f29448b2ed | -4.9593 | -49.6239 | 2026-08-28 20:40:00 | GOES-19 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 58c69b03-96da-37bc-9835-a861e9ea190f | -7.529 | -61.3635 | 2026-08-28 20:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 135.8 |
| 9563b95b-420d-326f-a342-1e50fa50f4bb | -11.1726 | -51.2728 | 2026-08-28 20:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 94.7 |
| d860b0f2-e628-3075-a7e2-136358781a8c | -11.1916 | -51.2708 | 2026-08-28 20:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 209.7 |
| e3492e5f-53d5-3d61-8be7-e9ad0757bb4f | -5.8894 | -57.7708 | 2026-08-28 20:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 225.6 |
| 87f973b0-3515-387f-ab50-a5c7182c2c5e | -4.282 | -48.2007 | 2026-08-28 20:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| f7c787b3-8e29-38a7-8f83-719a99571ec4 | -6.7513 | -55.6853 | 2026-08-28 20:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 96.2 |
| 8d934467-5d2d-357a-b4f6-08742ccfe882 | -8.0303 | -47.9926 | 2026-08-28 20:40:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 05311c95-721f-3a06-ae6a-f83963ca0a89 | -9.8737 | -60.3149 | 2026-08-28 20:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 88.0 |
| 14e038a6-7074-35bd-9c67-36d834c4002a | -9.9708 | -53.9419 | 2026-08-28 20:40:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 103.4 |
| 0a06fd89-7338-3648-b8a5-c0c6f33c49a0 | -14.2027 | -52.8432 | 2026-08-28 20:40:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 104.6 |
| 85cd13d6-ccc0-3f94-98d4-ded17527b7ab | -8.5971 | -54.7553 | 2026-08-28 20:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 103.1 |
| 7bbc8de0-68fe-31e6-8df8-6b4795f1ad34 | -9.9288 | -60.4277 | 2026-08-28 20:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 485.3 |
| 3c922116-7a15-35d4-85e0-3d42741a415f | -14.1788 | -48.7481 | 2026-08-28 20:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 127.6 |
| 0761e0ca-1e4a-3f88-90ba-e273495f0539 | -14.6224 | -50.8901 | 2026-08-28 20:40:00 | GOES-19 | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 73.9 |
| cbcac866-1b2f-3046-b688-0d3a76023cb8 | -12.7797 | -44.2576 | 2026-08-28 20:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 118.1 |
| 1b4dea8d-16b2-3927-920f-7966e3960ff7 | -9.1424 | -61.026 | 2026-08-28 20:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 91.1 |
| 3e2e0e68-3b54-34f6-8e0f-93e71eddd19b | -9.9287 | -60.447 | 2026-08-28 20:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 205.1 |
| 3a734ca5-0b26-3e61-ade3-974d6a909f2e | -9.0012 | -57.5585 | 2026-08-28 20:40:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 09b25e4a-33eb-3781-ba1b-5cb5de627bfc | -12.3799 | -50.6038 | 2026-08-28 20:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 89.0 |
| b876231a-1605-396d-8afe-4c1491a61ba1 | -6.7514 | -55.6654 | 2026-08-28 20:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 117.7 |
| ebabc34a-dda3-3d14-bd2a-447e0cec74fa | -14.622 | -50.9117 | 2026-08-28 20:40:00 | GOES-19 | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 097cbb56-31bc-3392-93ab-a8c08ad45c9f | -14.4664 | -58.5091 | 2026-08-28 20:40:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 128.2 |
| 4be986b4-150e-3170-b809-1b5aa29f4905 | -2.7119 | -47.043 | 2026-08-28 20:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 88.5 |
| 1dfe487e-7996-35cf-864c-4572605b2aca | -6.3467 | -44.0782 | 2026-08-28 20:40:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 241.8 |
| 6aa68075-10e1-3d6e-85f7-c47202da9a15 | -5.9819 | -57.6892 | 2026-08-28 20:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 102.8 |
| b1f483e0-8de3-35bb-a186-7995a9c644bd | -5.2446 | -43.7457 | 2026-08-28 20:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 227.1 |
| 5ac4d2e2-a2c0-3743-85ab-cbd702b07951 | -5.4177 | -43.1986 | 2026-08-28 20:40:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 139.3 |
| 33b61b2f-2ac8-3fa9-83bd-712642f8f1ad | -14.9386 | -56.3216 | 2026-08-28 20:40:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 181.9 |
| ff7ece7a-1860-3a6b-b24e-d016088c5b64 | -5.2696 | -45.2756 | 2026-08-28 20:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 5b1f6529-29a5-33b9-873c-485f07ff5494 | -7.4919 | -61.403 | 2026-08-28 20:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 85.9 |
| 30e3566f-a33e-3fa8-a3b5-b3298d740895 | -4.5695 | -44.0427 | 2026-08-28 20:40:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 139.0 |
| 41639005-1866-3ac0-bd91-464a60877035 | -5.9079 | -57.7506 | 2026-08-28 20:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 139.1 |
| f3d927a2-2720-301b-942c-e780fc462d9b | -10.5711 | -59.6149 | 2026-08-28 20:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 98.7 |
| 1c19cb9d-e8f5-3fe1-9e70-603b7e6145c8 | -7.2993 | -49.9676 | 2026-08-28 20:40:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 93.5 |
| aaa765dd-7054-3d1d-827c-15e9bbe3a7a1 | -14.1982 | -48.7451 | 2026-08-28 20:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 124.1 |
| c77e71e0-da3a-3040-995a-f5569009cd50 | -3.6033 | -60.5474 | 2026-08-28 20:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 127.1 |
| 97d60ef4-2809-3012-bd2a-b7945dde1610 | -6.7698 | -55.6844 | 2026-08-28 20:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 140.4 |
| 19fcf3a6-ba4d-32e1-be99-1a0461c6ac97 | -8.5969 | -54.7755 | 2026-08-28 20:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 162.4 |
| 2e1012e6-4d05-3df4-a36d-9b10b0b1c5dd | -14.1835 | -52.8456 | 2026-08-28 20:40:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 75.6 |
| d944fcb1-f3a0-39a3-be44-f75b1bd536b0 | -8.0113 | -48.0161 | 2026-08-28 20:40:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 170.0 |
| 15b2a8a9-f3a9-3b4e-b328-4457508480f6 | -9.1238 | -61.0269 | 2026-08-28 20:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 79.1 |
| d14140ed-03a8-3e9c-bf72-3a3b81301aa4 | -6.9336 | -58.9514 | 2026-08-28 20:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 127.9 |
| 10ab3cdc-7ed3-31eb-840f-82ef9ba99e11 | -10.7596 | -54.0384 | 2026-08-28 20:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 88.4 |
| f75ccdf4-faa3-3262-8c1e-91ef5ce8d943 | -5.982 | -57.6697 | 2026-08-28 20:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 0e417a54-f457-3abe-a55e-25b12c2abb33 | -5.3992 | -43.1766 | 2026-08-28 20:40:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 101.5 |
| 36c9525f-092d-38b8-b45c-52f2854e51e6 | -2.7304 | -47.0424 | 2026-08-28 20:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 79.5 |
| edfc7c63-0cb3-30c8-a139-04bbbd046a84 | -14.4057 | -50.0537 | 2026-08-28 20:40:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 102.0 |
| a4cc5a45-f176-358a-b751-baf016146536 | -12.7603 | -44.2608 | 2026-08-28 20:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 141.7 |
| 9e5c6973-72fa-37a1-bb2e-cd6cba8809e2 | -5.1414 | -44.967 | 2026-08-28 20:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 100.5 |
| 3b1031ac-5826-3ec3-88bb-b2a759a3e08b | -8.6013 | -70.2009 | 2026-08-28 20:40:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 31f21dd0-516c-3cae-8c15-89b10251c4ea | -6.949 | -59.4719 | 2026-08-28 20:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 87.2 |
| 0d66ba1c-b068-3d45-af01-cbe49f9eb45e | -6.1656 | -57.7988 | 2026-08-28 20:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 97.4 |
| a06b620e-a9dc-3015-aed5-f78a3d17c784 | -6.0391 | -44.9042 | 2026-08-28 20:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 9feec196-84df-3fd2-a83c-dbc63b596463 | -9.8739 | -60.2955 | 2026-08-28 20:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 201.8 |
| 0979b8d3-4d8c-3e02-9e0e-c916e295a1d2 | -3.913 | -60.9395 | 2026-08-28 20:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 84.7 |
| 5eaeaf6c-c708-3a29-b432-ea319eda4a74 | -9.929 | -60.4084 | 2026-08-28 20:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 98.0 |
| f0a0ca47-bb92-398b-a207-f511084f5b93 | -6.0004 | -57.6884 | 2026-08-28 20:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 100.8 |
| 6b1a6a44-45a5-31d0-93a8-e928e85e6315 | -8.0301 | -48.0145 | 2026-08-28 20:50:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 147.5 |
| 93608062-edf8-3c24-88ce-714a18722761 | -11.2106 | -51.2688 | 2026-08-28 20:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 142.5 |
| 8bb478f4-81a1-3eae-a489-c5b80ec9f2b5 | -6.3465 | -44.1013 | 2026-08-28 20:50:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 163.3 |
| a494bcaf-32cd-3681-84b1-98633b435299 | -14.1978 | -48.7673 | 2026-08-28 20:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 7d244a4a-a731-31fb-aadf-4861250c2051 | -6.1656 | -57.7988 | 2026-08-28 20:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 102.6 |
| 22b5245b-30f2-321a-84dc-8635a24bd65c | -11.2103 | -51.2899 | 2026-08-28 20:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 196.6 |
| 31f6f649-b3dc-34b0-affb-870ff3d48ab4 | -6.1657 | -57.7793 | 2026-08-28 20:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 117.2 |
| 6debe97d-7501-32e7-8272-541910fa29f8 | -5.4179 | -43.1752 | 2026-08-28 20:50:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 121.9 |
| a3a3f5cb-1f33-39d8-bbb2-e5d652b2296f | -9.5375 | -66.782 | 2026-08-28 20:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 89.2 |


[Clique aqui para ver as próximas entradas](README184.md)

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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 324f7340-3b8b-360d-9e0c-1602eb10b9ed | -7.05761 | -46.22507 | 2026-09-18 04:19:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 141b5772-06d4-3cb6-b91f-eddd3bf00a98 | -7.67495 | -46.10629 | 2026-09-18 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b9079c76-126c-3181-af13-3c53ddf272dc | -4.48216 | -54.97378 | 2026-09-18 04:19:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cb604ce1-16da-3da1-b7b9-6b5bf27f1424 | -2.35487 | -55.23379 | 2026-09-18 04:19:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dbf95fb7-f318-384b-8f97-b89713926848 | -4.4089 | -42.31466 | 2026-09-18 04:19:00 | NOAA-21 | CABECEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202059 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| ae734412-8e9e-3995-ac98-c3b3e3eebedd | -5.63407 | -44.80573 | 2026-09-18 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| eb8710a8-9d07-3ccc-9f41-8a9696990231 | -5.6313 | -44.80178 | 2026-09-18 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 20bb9bec-4209-3738-9a2e-343719e00c46 | -7.18218 | -44.54033 | 2026-09-18 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 15b820bb-fbe5-3723-b70d-2b13fcd3f016 | -2.79148 | -42.47716 | 2026-09-18 04:19:00 | NOAA-21 | PAULINO NEVES | MARANHÃO | Brasil | 2108058 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c31158cb-ca2a-37ef-b653-3284ac1c13b3 | -7.52569 | -44.9352 | 2026-09-18 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 669d5a32-806c-3cc0-9f58-b9e0da9777f0 | -7.64287 | -44.81576 | 2026-09-18 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c06b7e75-48d2-3082-989f-b40c23895f22 | -6.6687 | -43.63697 | 2026-09-18 04:19:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 533d2212-5a1b-3ba5-998b-5c2809756e73 | -4.51194 | -54.97496 | 2026-09-18 04:19:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b6fdea9a-c862-3b8f-8957-d2c107b83daf | -6.29445 | -41.78099 | 2026-09-18 04:19:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 64231835-68a2-3684-8ed6-1667c44f6dfa | -5.65379 | -43.38704 | 2026-09-18 04:19:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| c24d0894-bdaa-3150-b746-62b56b6049ac | -5.64121 | -44.80331 | 2026-09-18 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f2b15441-e68f-3fd9-a8ac-b0fe67e7af0f | -4.57756 | -42.95466 | 2026-09-18 04:19:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 4fd2349d-8ef4-392f-9f69-8f4be1855f6d | -3.96092 | -49.44017 | 2026-09-18 04:19:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ec767a96-0eb9-3f07-8c98-2a886fba672f | -4.58768 | -42.95619 | 2026-09-18 04:19:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| e734a119-349b-3088-b23c-6663336ba576 | -7.57622 | -46.34466 | 2026-09-18 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ebd17593-bb10-31c2-8259-50d43ae51c10 | -6.51534 | -49.89099 | 2026-09-18 04:19:00 | NOAA-21 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 470aba43-4f31-363e-aff2-80c8fdd19812 | -3.21867 | -53.95085 | 2026-09-18 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 594644c9-5e98-3f1d-ad8f-791fb61789f9 | -3.36266 | -50.45526 | 2026-09-18 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 73d65fbe-186e-3929-b16f-e521c2723035 | -5.25873 | -47.93376 | 2026-09-18 04:19:00 | NOAA-21 | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0f55583f-061c-3cf0-8331-dd042826c436 | -6.95324 | -42.55048 | 2026-09-18 04:19:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| bf2df8cf-1488-3230-82d1-208daef89cb3 | -5.61788 | -40.86646 | 2026-09-18 04:19:00 | NOAA-21 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 5f32d089-cf3a-3e2d-aa91-81e1400a7d95 | -6.93821 | -43.11322 | 2026-09-18 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cbb2bfd3-7eb3-3216-a8d9-715762cf3507 | -6.6664 | -50.90026 | 2026-09-18 04:19:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 494fcbd8-9f84-3835-bd4a-ab7693c285ce | -4.42677 | -46.29691 | 2026-09-18 04:19:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8424f5a8-d187-3b6d-970e-cb8aea7b7cf6 | -3.06724 | -49.52138 | 2026-09-18 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2a663c07-868e-38ab-b8d5-9e0cb3a7a68f | -7.00089 | -42.16218 | 2026-09-18 04:19:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 2c861992-3b87-3dc7-86ce-60093378e7c2 | -5.50229 | -45.51605 | 2026-09-18 04:19:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0a02721d-d4a4-3951-9dbc-6e6a46c9234b | -2.95916 | -50.32646 | 2026-09-18 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0d767672-5c74-3e7b-a4da-22bbba2e74c5 | -7.6591 | -45.8412 | 2026-09-18 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 86545c3b-2b02-358f-bbd6-7e11fcb188e8 | -7.34852 | -44.63078 | 2026-09-18 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 64f7b3b5-ae68-3ac7-9b48-4340e17e80c6 | -7.00357 | -43.87046 | 2026-09-18 04:19:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 548de15d-145d-3bf3-ab3b-911e4c02308f | -2.2721 | -48.74693 | 2026-09-18 04:19:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2b54cec4-951c-3ddf-bbd6-f462e2e42c9e | -5.42814 | -43.43945 | 2026-09-18 04:19:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| eae23f36-8510-3c6c-977a-050a2e9a1d19 | -4.43889 | -55.52159 | 2026-09-18 04:19:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e36b9cd8-38df-3a52-8d42-1b59a15797e7 | -6.27872 | -41.66425 | 2026-09-18 04:19:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| beadc86d-5884-31e3-9ce4-d0619b1174ee | -2.29319 | -47.8833 | 2026-09-18 04:19:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 451af729-fae2-3dd6-aa63-90ba32dde74a | -7.02364 | -43.62907 | 2026-09-18 04:19:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 9bdcb407-76ae-3d0f-9f6f-60c18ee6d8cc | -7.19704 | -44.53196 | 2026-09-18 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8901c7af-60a3-3438-bd83-0d88351c581f | -7.00127 | -43.64028 | 2026-09-18 04:19:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 95e34090-6c1e-378f-becb-d9aa3a05e50d | -4.58149 | -42.95156 | 2026-09-18 04:19:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 656a0100-b0a6-311f-a9dd-deed34630aa9 | -5.62371 | -40.869 | 2026-09-18 04:19:00 | NOAA-21 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 2af45373-e09f-315e-8a65-dda5551c8c1c | -4.48724 | -54.97911 | 2026-09-18 04:19:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5c98b382-5bdd-38e8-8c2d-8ade7df132f6 | -7.29152 | -38.95905 | 2026-09-18 04:19:00 | NOAA-21 | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| e58e97ee-5657-3751-bed0-5efbd2ea0f71 | -4.43612 | -55.52758 | 2026-09-18 04:19:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f1e11d48-bb3a-310e-aa7f-09f0b353ee07 | -7.93847 | -44.83707 | 2026-09-18 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9ae9e790-168b-3d1f-abf3-4ee68181134d | -7.86135 | -44.8321 | 2026-09-18 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e82accdd-51d0-305c-b8a5-923424ce5251 | -5.07551 | -42.74764 | 2026-09-18 04:19:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 187c1734-fa84-3078-93d5-2781fb02c946 | -3.07062 | -49.51781 | 2026-09-18 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b855e7dd-1fa3-3037-ac0e-de826a86e3e2 | -3.37786 | -50.44479 | 2026-09-18 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 5b775ac8-97d0-3cfd-a180-4079873bcf67 | -5.88992 | -49.77932 | 2026-09-18 04:19:00 | NOAA-21 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fe853d7d-97f1-3962-b2b6-6e8537c9017e | -2.82399 | -49.23875 | 2026-09-18 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 99d03fc7-26fe-3c8f-8113-31e7be4d50ba | -5.14037 | -47.60323 | 2026-09-18 04:19:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1ea32ad5-1f2b-374c-8905-8872b9df356b | -7.09397 | -43.58794 | 2026-09-18 04:19:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 30ce8566-7adc-31dc-9f17-be4c783e2b20 | -7.44941 | -44.57183 | 2026-09-18 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9170820d-47fd-39c4-b617-fe7069b0b8d6 | -2.82343 | -50.46411 | 2026-09-18 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b83ba0c0-c3fc-35a6-af0f-90064168ad4c | -4.55733 | -42.95155 | 2026-09-18 04:19:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5bc0ea30-6225-3d2b-8e2b-d8fd11f68a0f | -5.9135 | -53.55553 | 2026-09-18 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ae294cb1-86b8-32b3-820f-20b662048148 | -6.44812 | -44.95237 | 2026-09-18 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 82e798cf-2348-3886-b904-89c2678ac55f | -5.76652 | -45.80262 | 2026-09-18 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7893f365-4dda-3c48-b360-2044187e2a0e | -7.07922 | -47.48104 | 2026-09-18 04:19:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c94421e1-1975-314b-8d04-45c0866e501a | -3.70293 | -54.17221 | 2026-09-18 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e4ac9640-c965-3777-aee4-2a1985f5107d | -3.91913 | -55.7486 | 2026-09-18 04:19:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 878230b3-4fac-3ca0-ab94-b37590831835 | -7.80997 | -44.89854 | 2026-09-18 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ab46b617-821b-358a-9b18-d46b517e42ed | -6.77614 | -46.4749 | 2026-09-18 04:19:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 95df0ef6-76a7-33b1-86a3-4664add65853 | -7.63956 | -44.81525 | 2026-09-18 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3bcb2d16-6c27-35bb-8ead-2ce6fff14282 | -7.18164 | -44.54381 | 2026-09-18 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0b15f561-ef8d-3c01-b690-b3d76d3a77cd | -7.00411 | -43.86692 | 2026-09-18 04:19:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 170636ad-316e-3fc2-a894-740f2e55f5d3 | -2.64295 | -54.69427 | 2026-09-18 04:19:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| fb4f7779-c6f9-3027-bb95-a0710c10b980 | -5.87546 | -44.96058 | 2026-09-18 04:19:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0dc0ebcb-f131-366d-baa2-7d69b2445207 | -2.89799 | -54.17213 | 2026-09-18 04:19:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 23c280c9-1732-3994-88f8-03053efd0494 | -5.184 | -49.27569 | 2026-09-18 04:19:00 | NOAA-21 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 507db4e4-f01f-3097-a76c-b782ba13dc0c | -6.39931 | -42.99078 | 2026-09-18 04:19:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| feac7acd-6627-34ef-af34-69a337e04e56 | -6.11886 | -44.02891 | 2026-09-18 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 64ff040b-af9c-39b0-9090-d147653e2b7a | -6.46098 | -46.01431 | 2026-09-18 04:19:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e8a52a8f-44b5-3b7d-ad96-dec6432811e9 | -5.75259 | -45.09335 | 2026-09-18 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| a0c8966f-e2cd-3304-9e0e-d93343c46fb7 | -5.41311 | -42.94458 | 2026-09-18 04:19:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 2.3 |
| af6940f3-4299-3b97-8ea4-9465a193e1dd | -3.36125 | -50.46373 | 2026-09-18 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| da4ca8b4-3f4d-375f-a553-75e7cf7aa2a7 | -1.17964 | -54.17275 | 2026-09-18 04:19:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2e6b03cc-d40a-3870-a4f6-689416401a75 | -6.59077 | -45.8828 | 2026-09-18 04:19:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 21009764-ca6c-3441-b807-70de3ed2edd8 | -2.81485 | -50.46418 | 2026-09-18 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4df0fafe-8c2a-36ef-9af0-66ac2d61028d | -6.61172 | -44.20546 | 2026-09-18 04:19:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 6ad88bce-1122-3e0f-882c-b566cabad313 | -3.76189 | -49.68826 | 2026-09-18 04:19:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8ff61806-07ea-3dd9-95d3-f144b2ec9f73 | -5.14461 | -47.59968 | 2026-09-18 04:19:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ff0652af-1627-372d-b8cc-c3f2980f46da | -4.57309 | -42.96133 | 2026-09-18 04:19:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e1b359d6-3e76-33f1-8ca5-91e3b029679c | -4.50614 | -54.97385 | 2026-09-18 04:19:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| afcad783-62e8-3132-b603-a1d868094513 | -5.1567 | -45.24714 | 2026-09-18 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ed278ee9-92fe-3f06-a257-264cd9b28e63 | -6.77419 | -42.7828 | 2026-09-18 04:19:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6db28055-2913-3ccb-ac7d-4ac151427707 | -6.66309 | -43.62877 | 2026-09-18 04:19:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 88957f96-db7f-3568-bdbf-81d75124af7c | -6.11621 | -47.17674 | 2026-09-18 04:19:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c4e98c29-54b1-39fd-97e1-e8b1c58d1565 | -6.65581 | -51.48932 | 2026-09-18 04:19:00 | NOAA-21 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d86a8046-53be-3a35-b0b7-7214d51eba78 | -2.55208 | -48.93074 | 2026-09-18 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3ad9dd9a-f391-36af-b4b2-2bac1ca14534 | -6.7441 | -44.09689 | 2026-09-18 04:19:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 738245cc-81e2-3dc9-8244-3ad301b33764 | -7.50526 | -44.9143 | 2026-09-18 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1a3aaeca-c9fb-3a23-ab87-271e02095635 | -6.74077 | -44.09639 | 2026-09-18 04:19:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4191b53d-17a0-35c2-90b6-a2279bc5d9a9 | -4.48141 | -54.97811 | 2026-09-18 04:19:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README35.md)

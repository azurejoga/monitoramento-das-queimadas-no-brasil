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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4a91b79f-dd19-3edd-8fd2-7efe80242b76 | -9.41666 | -51.65059 | 2026-08-25 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 81cdcd63-fe88-3eb8-8929-38f34954aebd | -8.59999 | -47.44775 | 2026-08-25 04:25:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c5d5362e-7e60-3010-8971-69763de6c547 | -7.43773 | -43.12191 | 2026-08-25 04:25:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 8b092b0f-72f0-3cc3-bceb-31f011035c17 | -6.4069 | -51.71279 | 2026-08-25 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 2189cdeb-ed2e-3e62-a8ff-f79b00aac531 | -6.0965 | -53.4106 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b6c5f46e-bf50-352b-aedb-56f78f1c0d28 | -6.12025 | -57.82011 | 2026-08-25 04:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| ef9d6aeb-d33a-3f9d-b7fe-e13bfcfb0871 | -7.70278 | -38.15914 | 2026-08-25 04:25:00 | NOAA-20 | MANAÍRA | PARAÍBA | Brasil | 2509008 | 25 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c18e0a8e-52ce-3b13-8aba-a4a8b562da66 | -8.57311 | -54.85563 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 890686c9-f66c-3b8b-a1c6-bc111fd05b5d | -11.14012 | -44.48069 | 2026-08-25 04:25:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 32.8 |
| 399df46a-9a2b-3a40-ad75-8917fde66e5a | -8.81192 | -46.60219 | 2026-08-25 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 07c4396e-2969-3443-8fdc-571f415bada4 | -5.61295 | -47.00573 | 2026-08-25 04:25:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f9cb9ae3-ca08-3063-b2ba-d8f8f7320295 | -6.25893 | -55.41379 | 2026-08-25 04:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ebbdea3a-8067-359a-9741-c8123300201a | -9.44604 | -51.58365 | 2026-08-25 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4e8f1ddc-5b9f-3885-825d-f778900bd61d | -6.96302 | -59.07817 | 2026-08-25 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b6f4deef-f60d-32b4-837f-ae6411e8cc49 | -10.71047 | -47.75891 | 2026-08-25 04:25:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9a7f0134-e4d1-3893-9501-99380759bb4b | -8.08785 | -47.51412 | 2026-08-25 04:25:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7e9d197a-08ca-39a3-9eb9-941a4283171d | -8.15339 | -46.70201 | 2026-08-25 04:25:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 527ee652-f9c4-3786-855d-e2d94915a326 | -7.31994 | -46.14318 | 2026-08-25 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7a5a114a-c9da-3dda-86c5-651f12023caa | -6.43519 | -54.96707 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 53ee57b3-c3f3-3be6-8acf-f6b0c425547d | -6.12477 | -57.83334 | 2026-08-25 04:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b063b7b1-b85b-342e-abe3-c1bb4b19d442 | -8.10195 | -47.49288 | 2026-08-25 04:25:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9eba9197-480e-3785-9b87-fd08a326ef7e | -9.56826 | -49.22884 | 2026-08-25 04:25:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d2a75c06-f470-3fa4-bfb0-5dfdfd2d590f | -6.44013 | -54.97198 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 87a01e35-2651-3926-9d2c-a19e6f082d4d | -5.78636 | -57.6166 | 2026-08-25 04:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 6ab7a227-bb92-362d-b494-7296355e71c8 | -6.808 | -42.66914 | 2026-08-25 04:25:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 471b3c54-ebed-3b21-ae41-418c079add2a | -6.6266 | -58.50108 | 2026-08-25 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 64a8ef81-9c4e-3c5d-8592-d7eedb423707 | -10.03743 | -46.42282 | 2026-08-25 04:25:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 03d0921d-88a9-3fac-b733-a1e167363c20 | -7.26315 | -45.37005 | 2026-08-25 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 08fdea0e-be5d-3d38-813d-1cbae9ed32d3 | -6.93696 | -52.78119 | 2026-08-25 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 62d7c6ec-6a17-31d1-a022-a12e4dad921e | -6.63312 | -58.49697 | 2026-08-25 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 12.2 |
| c05cf5f3-4566-3ef8-90ad-3ee12637eb82 | -6.3563 | -54.77405 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 740bf89f-6e43-34ee-815e-9c7959484203 | -8.57032 | -47.43498 | 2026-08-25 04:25:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 597498e9-b976-3f37-934d-d0ea1a70507c | -8.08156 | -44.63928 | 2026-08-25 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3ad1a9df-0941-3cf5-8597-543dd6e7b9a6 | -7.29183 | -45.36041 | 2026-08-25 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 22.2 |
| c9f26b9a-260e-3530-a4f3-f24aa623215d | -6.31646 | -45.70422 | 2026-08-25 04:25:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 934995ca-bdb2-3533-a53a-5430b1f457d8 | -10.02519 | -46.43527 | 2026-08-25 04:25:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ea0fbc69-9905-3b39-bf65-d312ef37f1b3 | -6.95447 | -59.08401 | 2026-08-25 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 54bf9a0e-bfd0-3da1-907a-47a503685dc6 | -8.76487 | -45.79646 | 2026-08-25 04:25:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a0d5e589-03a8-31da-ba6a-bcabcb141dc3 | -8.07051 | -44.64469 | 2026-08-25 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9ec6288d-51f2-3ab6-a6e3-72632b177735 | -6.9696 | -42.09075 | 2026-08-25 04:25:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1a377506-b1f6-344e-9e10-62032d0b12aa | -7.25393 | -45.85418 | 2026-08-25 04:25:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 15fd0467-88bb-3ab3-9d85-a6b9295ca85d | -6.75959 | -45.24699 | 2026-08-25 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| afc01046-8141-3403-9b51-388db9463f65 | -8.08543 | -44.6363 | 2026-08-25 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a7871bbb-8a15-309e-a90b-4b37f950bedc | -9.60846 | -47.75793 | 2026-08-25 04:25:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ad380706-c3b7-3aab-8143-0749b99e5ec5 | -7.44118 | -43.09944 | 2026-08-25 04:25:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 12add1d9-fa50-35ee-85ac-da70547d141f | -6.96899 | -42.09478 | 2026-08-25 04:25:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 450d5616-ae9a-3fde-b9f3-561b7d58dd2d | -7.30138 | -43.00524 | 2026-08-25 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 188a8b1b-ccee-3021-ba54-0108d3db5157 | -8.57103 | -54.85641 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 09b3d434-c184-34d0-8ea2-fa0ce4ca83b0 | -8.57777 | -54.84999 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 4586501a-32f6-3c6e-a892-b86447648488 | -7.43716 | -43.12564 | 2026-08-25 04:25:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 88f81b7c-642d-3f6d-8e92-fef9eaf526a3 | -6.7025 | -56.34582 | 2026-08-25 04:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 49eade93-9ace-35f9-a75b-b510632f51d3 | -7.49481 | -55.36329 | 2026-08-25 04:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3ab8fa35-7f72-3638-81ad-a45643e820fc | -9.57035 | -49.23149 | 2026-08-25 04:25:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2faf8864-d9cc-3319-b12c-7704204ccb34 | -8.60225 | -54.74443 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f3210ba3-3abc-3614-93dc-31cda389d332 | -7.25004 | -45.85714 | 2026-08-25 04:25:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 61b1cb8a-1840-366b-9796-c13f8f2cf955 | -6.96162 | -59.0854 | 2026-08-25 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e4c3b0b5-1da4-39ef-91dc-f8113c68b565 | -8.07714 | -44.64575 | 2026-08-25 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 55d1830c-882a-398f-81c4-b43cd45bd1a2 | -6.63358 | -58.50233 | 2026-08-25 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 15091a81-a9de-3568-9c10-a1831510cfa6 | -7.30997 | -42.97184 | 2026-08-25 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 306a49c4-8550-32e5-99b9-58ca7d041eab | -6.94392 | -42.68808 | 2026-08-25 04:25:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| d150e006-39cc-3b86-a10b-664475869f02 | -6.63183 | -58.50373 | 2026-08-25 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 817201c6-9f98-3b23-ace4-3770b2dcd95d | -7.44002 | -43.10696 | 2026-08-25 04:25:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 0235506f-7c65-3348-a75b-7ceb30d1df5e | -6.82891 | -52.5011 | 2026-08-25 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 18c9fe9c-11e5-3365-940a-aa347c45997a | -7.43373 | -43.10214 | 2026-08-25 04:25:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 5086e0c2-dada-316d-a477-b3cc363fb6fa | -7.38205 | -55.18674 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4f39346d-b601-3486-bc64-f21325b8631a | -5.51725 | -46.62421 | 2026-08-25 04:25:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e97140a6-6e6d-3e3a-a1c0-d727e13e55bc | -7.15448 | -44.51046 | 2026-08-25 04:25:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6ced914a-99d5-38bb-ae88-f49084ef1821 | -8.60036 | -50.02023 | 2026-08-25 04:25:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| aefad13b-390e-364c-b95c-0745b82842a8 | -7.49392 | -44.46774 | 2026-08-25 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f9127447-1a75-327e-8c96-a9e9c5688148 | -9.93266 | -40.49683 | 2026-08-25 04:25:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| bf111913-5cff-33ed-8dbb-c4fd8c76de50 | -6.83239 | -52.50614 | 2026-08-25 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 1be22872-fe96-3895-8121-9d34255e1f9a | -5.95722 | -53.59106 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6a538b88-62c4-370b-bd90-657aeea0e8b7 | -6.12811 | -57.85297 | 2026-08-25 04:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b0beaccd-18ff-34ab-87f4-699813889d83 | -7.42916 | -43.08604 | 2026-08-25 04:25:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 4d804857-3420-3209-b50a-6c6602a4e5a0 | -5.98421 | -43.74644 | 2026-08-25 04:25:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d867eeaf-a192-3429-966c-4ab9cc8b41b3 | -7.27689 | -44.07378 | 2026-08-25 04:25:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 32c2a5f6-a9dc-367d-be7f-438d684ac779 | -8.21281 | -54.98722 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 74bbcb8a-9513-3f36-b937-c730096618da | -8.56802 | -55.28003 | 2026-08-25 04:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f911d1d8-996d-3f92-8d69-b0c44773dc04 | -8.80522 | -46.6011 | 2026-08-25 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1dd7ca79-b4ce-37a0-9000-1be580679a26 | -8.1001 | -47.50433 | 2026-08-25 04:25:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 11b62085-df5d-35e5-b2cc-dd9007987817 | -8.92558 | -45.74759 | 2026-08-25 04:25:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e55f80e3-39ab-38b3-ae24-b3dc3aa82287 | -7.1526 | -42.74255 | 2026-08-25 04:25:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 2333aa21-a92f-37c4-b64c-80f94c02e934 | -7.43087 | -43.12085 | 2026-08-25 04:25:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 3e41ee75-6075-3f5a-a2cf-a183473f6347 | -9.599 | -45.3777 | 2026-08-25 04:25:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d4b9716d-e412-334c-9300-671d053e5dd1 | -6.14157 | -57.7058 | 2026-08-25 04:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| ee745b08-0020-3485-8f94-c0ed17a29a23 | -7.34909 | -55.66212 | 2026-08-25 04:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5ed754f0-eacc-35e5-820a-84c52524eeaa | -6.25088 | -55.4251 | 2026-08-25 04:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1be0498e-e3d6-3255-9771-7fafe665f52e | -2.80912 | -48.67004 | 2026-08-25 04:25:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 3a012ddb-7d8e-3cc2-841d-946b40c0028f | -6.4306 | -52.75688 | 2026-08-25 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8631fc41-4079-3049-a145-43d32dcda653 | -8.21942 | -54.98199 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4a74a9f6-3673-38a7-abbe-f26f82a5a188 | -6.17613 | -57.70645 | 2026-08-25 04:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| aa08a4e4-50b0-3efb-83fb-e84c61961f48 | -8.09725 | -47.49995 | 2026-08-25 04:25:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5c36d234-be1e-3b77-b1f8-f6bc0f2be546 | -7.25984 | -45.36953 | 2026-08-25 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 118eaded-7925-3045-bc0e-eac530b80da3 | -6.20589 | -53.49321 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d069afd1-c72d-37a4-8bc8-f7c802063e99 | -6.83744 | -52.50823 | 2026-08-25 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 293ab9c2-7697-30c5-88da-d1fcd100c785 | -7.88385 | -46.33133 | 2026-08-25 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c776b97d-fd7e-3bbc-ac45-8ce341b613bc | -9.96003 | -48.32454 | 2026-08-25 04:25:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4ecebf8e-1bd9-38c9-aa22-d448941c51c6 | -5.77409 | -46.11863 | 2026-08-25 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9d43fa61-e631-329d-9889-6a9f0cdce97f | -6.17102 | -53.4805 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4b40c971-52fa-3bdb-826e-d4144617df2b | -8.59975 | -54.74302 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |


[Clique aqui para ver as próximas entradas](README33.md)

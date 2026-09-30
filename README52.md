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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ea5c7150-5e19-3e39-983d-4bd916383927 | -6.04834 | -53.29179 | 2026-09-30 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 18e6cacb-3830-34a9-85a1-13fc6beb0523 | -6.13808 | -53.06447 | 2026-09-30 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 04627b6e-ea6b-39cd-a79f-c0081c98c507 | -11.37898 | -43.37624 | 2026-09-30 04:53:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 920f41c1-a579-37e5-9eec-bf50551dd156 | -10.70824 | -47.8313 | 2026-09-30 04:53:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0729e23d-67bd-3df6-a03e-3ee33821f963 | -5.74656 | -45.17154 | 2026-09-30 04:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e6107f77-86e1-364b-9a86-f31b39575073 | -17.90768 | -45.05445 | 2026-09-30 04:53:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 3a5998ff-9cd7-38f2-bb14-a59b32842cae | -5.09432 | -46.04244 | 2026-09-30 04:53:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 722be3ed-ae16-3afd-ace6-b420a18bc4c1 | -7.47251 | -45.79253 | 2026-09-30 04:53:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2941a51a-9475-3373-bfad-527732d6d3e5 | -5.75143 | -45.16819 | 2026-09-30 04:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fe1600d5-96c8-3351-9d56-ec66bfcdd2cf | -10.05032 | -53.12076 | 2026-09-30 04:53:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ba877b1b-fe9b-3dab-a0a2-b9b90c538d2b | -7.06818 | -46.57173 | 2026-09-30 04:53:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fc493354-3f1e-3183-b27b-8373fef954f0 | -5.75024 | -45.17611 | 2026-09-30 04:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f2ee54c8-c1c5-310e-8057-fe1447a1459b | -11.17037 | -44.78848 | 2026-09-30 04:53:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c1af9fb2-ee9f-39c7-8ef8-e2321f538322 | -11.39293 | -47.42749 | 2026-09-30 04:53:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a0bf29a7-7fff-3623-a847-76474c3c6c95 | -6.12431 | -57.79136 | 2026-09-30 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1f6c21c0-16ab-3db8-b853-bfea64290945 | -5.72521 | -43.5101 | 2026-09-30 04:53:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 63a4f164-92a0-3299-8450-01ddd7b4b408 | -6.06857 | -47.27654 | 2026-09-30 04:53:00 | NOAA-20 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 13d24cf4-1496-3c63-a40d-56c563ef786a | -4.12616 | -46.87326 | 2026-09-30 04:53:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 79898c11-a287-3d80-bdda-ab6d205b7438 | -3.01086 | -54.22155 | 2026-09-30 04:53:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dd8feb92-cf1f-35f5-a47c-4bc70be649a3 | -5.98421 | -53.55225 | 2026-09-30 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 33ac30a9-fc09-3deb-b593-70472f01fb74 | -2.99267 | -54.9108 | 2026-09-30 04:53:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1cd7902a-6746-30e1-88aa-34295715dd7a | -3.01245 | -54.2355 | 2026-09-30 04:53:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6389028d-bd30-3b52-8274-cfd595d1e588 | -3.97141 | -48.00485 | 2026-09-30 04:53:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 342ca152-f0e1-3014-b3ce-76d1292b63dc | -4.81925 | -45.63934 | 2026-09-30 04:53:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2a54c57e-71ee-38b1-a823-0a17fdd83fe3 | -10.75013 | -50.50311 | 2026-09-30 04:53:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 037eb7c8-87cc-3b24-a4b6-715ce54df441 | -9.103 | -47.16806 | 2026-09-30 04:53:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| af86294d-c5a6-31f0-9a9a-e31dbcd849b6 | -4.35063 | -48.96979 | 2026-09-30 04:53:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 55c1d34d-a368-3906-9fc1-5e264cac56ce | -17.57694 | -43.70755 | 2026-09-30 04:53:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a16cd847-d824-35ed-8db5-0534c47c0036 | -3.56266 | -53.26444 | 2026-09-30 04:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ecf1a62d-d91d-3310-89b0-6ba0a09e30d2 | -11.63656 | -43.53336 | 2026-09-30 04:53:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c2bbdd96-9705-3878-9cbc-692f34c01ecb | -5.98326 | -53.54929 | 2026-09-30 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bc2fe556-5006-30cc-8e2b-eb072c8ebbd6 | -3.95553 | -49.05194 | 2026-09-30 04:53:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ae4f7eb5-3e1d-3e72-a85f-eb64604105bf | -16.35409 | -42.58813 | 2026-09-30 04:53:00 | NOAA-20 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 06f794e0-0ff8-33d0-8771-77eb44e5da6c | -8.19512 | -55.09198 | 2026-09-30 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5d507303-6cc8-3d31-ae79-36ba55c555b5 | -3.37355 | -50.95122 | 2026-09-30 04:53:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ca92bb0e-f2e2-3ede-acbd-b89338d91812 | -6.12508 | -57.78681 | 2026-09-30 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 52461673-aa39-3379-93a5-2c587730ed5c | -8.26917 | -54.75578 | 2026-09-30 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 07fa8054-ebc7-37b6-9bd5-45268221a402 | -9.0687 | -49.86875 | 2026-09-30 04:53:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b497deba-2954-399d-b18c-16813efbe829 | -4.2859 | -48.61781 | 2026-09-30 04:53:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e58e8456-3e6a-3be4-8e97-57da07b0486f | -7.50284 | -45.82359 | 2026-09-30 04:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e76ad8bf-fdd3-38a9-83ec-8cb6c7eaf7d4 | -14.50359 | -48.30468 | 2026-09-30 04:53:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7c6c9379-69b1-3962-ab63-e85316d1223f | -10.71204 | -44.42026 | 2026-09-30 04:53:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 49aca748-1268-3be3-8079-52001067da7a | -3.37245 | -50.95812 | 2026-09-30 04:53:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 910d157c-f880-39c7-bf80-9cc6c8ec6f4b | -5.36243 | -47.91457 | 2026-09-30 04:53:00 | NOAA-20 | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a1ca9e64-a008-35e8-bd06-492caabcbda6 | -10.51653 | -45.37347 | 2026-09-30 04:53:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 24873cd8-f9b6-31c4-9981-40d9905fe678 | -6.33986 | -55.33062 | 2026-09-30 04:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 10bef7a5-362b-3bf1-8ed9-13c70e2a303b | -11.16702 | -44.77739 | 2026-09-30 04:53:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 38bbc701-98ce-3357-88be-bfb63890cf03 | -7.5085 | -55.02599 | 2026-09-30 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b414665d-8ab3-37be-9eb7-fe063e632d3a | -15.97591 | -48.1373 | 2026-09-30 04:53:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1cfafd83-2937-3d63-957e-7ac3dee78708 | -7.5019 | -55.04277 | 2026-09-30 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2dfd9dca-8696-3ac2-98a4-d83be1caa5b7 | -7.38719 | -47.01784 | 2026-09-30 04:53:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c2299159-3fd6-3571-8068-111530734598 | -4.80642 | -45.64133 | 2026-09-30 04:53:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3d268565-2f78-31bb-af50-1304a127fa09 | -6.13585 | -53.05648 | 2026-09-30 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a7bec6a9-f4a7-35a0-b4d6-89aff78f2065 | -8.38986 | -45.44712 | 2026-09-30 04:53:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a4ce101e-d63f-37ec-9a9f-faa5b751c68e | -5.03197 | -43.57463 | 2026-09-30 04:53:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 14d9b36c-2491-3acd-82b2-4007a951062b | -10.83226 | -48.70313 | 2026-09-30 04:53:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5b663933-8aa8-3a0f-9a0a-19dc1cb4d334 | -4.02302 | -54.2091 | 2026-09-30 04:53:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9db24df6-56d2-3640-a79d-413b3a941f17 | -11.37494 | -43.36572 | 2026-09-30 04:53:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e63cf5c2-a6fb-391b-99ad-1eaa527af1f1 | -7.82803 | -45.81021 | 2026-09-30 04:53:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a12225f1-c389-3d9d-adf0-4be837358ee2 | -9.76216 | -54.29063 | 2026-09-30 04:53:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f2e6cfbb-56e4-365f-9c33-38e255dcfd65 | -11.19341 | -44.84114 | 2026-09-30 04:53:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 09ef7b3e-3372-3810-8334-9f798a93aea9 | -5.87185 | -50.16471 | 2026-09-30 04:53:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 306dadcd-46a4-3733-89e5-3cd9202a6f34 | -18.09987 | -44.40927 | 2026-09-30 04:53:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eaf4e370-6643-39fc-8bc6-a6f90fccdec8 | -3.9561 | -49.04833 | 2026-09-30 04:53:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1fc02cdf-ecfc-3deb-a995-fe59f52590d1 | -3.1543 | -54.07566 | 2026-09-30 04:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8d76ca72-8820-39b0-872a-59570d371900 | -4.32264 | -48.63123 | 2026-09-30 04:53:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4414f1df-91f0-3c40-b54e-92d380ebd787 | -15.25476 | -44.81871 | 2026-09-30 04:53:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0f9eb2f7-7690-393b-955f-9c598480f92b | -3.3785 | -50.94138 | 2026-09-30 04:53:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 665fe333-e89c-320b-9d81-77e990ff40f4 | -15.83423 | -42.55808 | 2026-09-30 04:53:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| df2231c7-baf3-3e3d-8a9c-b4fe5d9ecce5 | -7.0774 | -41.75828 | 2026-09-30 04:53:00 | NOAA-20 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 62cdaa6b-0981-393a-9848-e5a6c70967db | -10.19703 | -49.97551 | 2026-09-30 04:53:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a75715b4-c0f6-3a23-a723-1ce57a4ba208 | -12.8989 | -61.71583 | 2026-09-30 04:53:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9e986acb-70bc-3087-9c51-97b307e94b9d | -8.59257 | -50.4157 | 2026-09-30 04:53:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 74c21e8d-f934-3285-a583-495112279b92 | -8.25241 | -45.43621 | 2026-09-30 04:53:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6cc80a24-1b33-3008-a45c-bbea18fb211f | -8.33356 | -44.16359 | 2026-09-30 04:53:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 35ec2b62-b727-3be9-94e7-8a00acad0323 | -9.06752 | -51.5271 | 2026-09-30 04:53:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b894a3a8-0bfd-3a0e-b15e-d9928604de55 | -10.41173 | -53.77415 | 2026-09-30 04:53:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c2cfe132-b196-3c37-9d80-29cc9e3d3d58 | -4.45416 | -47.92453 | 2026-09-30 04:53:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ae3f9598-9307-34d0-b4eb-bb659c2f45fe | -5.33428 | -46.19683 | 2026-09-30 04:53:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 061c5771-c2f0-3ccb-af01-fe228765cfda | -11.16958 | -44.83009 | 2026-09-30 04:53:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| ce5ed685-60c6-3771-9fbd-823a09b4307a | -3.56478 | -50.25814 | 2026-09-30 04:53:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 73b5ea20-62ed-3171-84f1-1c6c4bb96fc9 | -2.98067 | -54.14839 | 2026-09-30 04:53:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 61cd4d1b-032a-3513-98d8-b8ef49155a13 | -3.4309 | -50.43785 | 2026-09-30 04:53:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 13ca0a73-1879-3f2d-b2c7-ea1c23d3399a | -6.33077 | -51.15541 | 2026-09-30 04:53:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2d412794-124b-3e67-957d-123955274964 | -7.55638 | -55.03374 | 2026-09-30 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3004cffa-d78b-3ff7-9ab0-fd22977f7517 | -9.15415 | -45.60038 | 2026-09-30 04:53:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fb579aec-096d-341d-af0f-bec62ceafd63 | -10.55104 | -50.86989 | 2026-09-30 04:53:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e4822aaf-5617-3f45-b2ea-6e91d95ac453 | -9.806 | -44.83504 | 2026-09-30 04:53:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7d395235-9835-3d28-80a2-7d6246340dbd | -15.12611 | -43.62598 | 2026-09-30 04:53:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4ea71ab5-9079-30bc-9c3e-0c6ff628810e | -6.66893 | -59.92753 | 2026-09-30 04:53:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ba5adfd7-2ee7-37d6-9e1e-b43231c52208 | -8.20955 | -45.4567 | 2026-09-30 04:53:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8cb0d82b-5a82-355e-9417-06a762fddfc9 | -15.20082 | -46.12962 | 2026-09-30 04:53:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c85c67d0-5c7a-3fcc-bfa1-a672981bdc76 | -3.00944 | -54.23043 | 2026-09-30 04:53:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4e29cedb-b1d9-30d2-918b-cd8f1404fd13 | -5.09675 | -49.05933 | 2026-09-30 04:53:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a5810a57-fc23-33ab-8a84-176e385f5f0d | -3.91141 | -49.37585 | 2026-09-30 04:53:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e5a0eba4-0cf8-39cb-af21-595ade627987 | -3.1589 | -54.09427 | 2026-09-30 04:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e959bc42-23e6-38ad-ae67-2a8bf6ce5c5f | -8.94179 | -49.78463 | 2026-09-30 04:53:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 85148308-491f-3ab9-9205-f3018e1ddb04 | -10.8329 | -48.6988 | 2026-09-30 04:53:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e4d875ff-6470-30e3-9d41-54b4d2a45c86 | -15.19844 | -46.14794 | 2026-09-30 04:53:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ea682ec4-ea77-333d-9c77-77bb13f790d9 | -3.9637 | -48.1243 | 2026-09-30 04:53:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README53.md)

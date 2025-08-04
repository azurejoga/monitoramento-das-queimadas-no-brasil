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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eed54674-e759-3f60-843d-eab4f7b45347 | -17.3667 | -46.08397 | 2025-08-04 00:45:00 | TERRA_M-M | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 24.4 |
| a061e221-dc92-3d01-accc-c48ab39fdd7a | -17.61514 | -46.71398 | 2025-08-04 00:45:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 50768880-e8ff-3e91-b8b1-d8fd5af269d9 | -15.70786 | -48.99733 | 2025-08-04 00:45:00 | TERRA_M-M | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 5c529123-847f-326f-96a2-9eebbd3724c0 | -14.84841 | -48.40167 | 2025-08-04 00:45:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 7740c1d9-bbe5-34d2-848f-d2cc7c3e74d6 | -17.61353 | -46.70324 | 2025-08-04 00:45:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 10.6 |
| ca0f6c19-bb95-38f3-8ae7-f3e9e5d40a9f | -17.36845 | -46.09514 | 2025-08-04 00:45:00 | TERRA_M-M | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 9.9 |
| f827810b-486f-35b3-86c3-6665f17ba787 | -16.13607 | -46.88375 | 2025-08-04 00:45:00 | TERRA_M-M | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 9eb8554a-d698-3d6a-afa4-2377afedc64e | -13.68377 | -41.3779 | 2025-08-04 00:45:00 | TERRA_M-M | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 49.8 |
| 4102a84e-f155-3975-b3c0-5c2359761456 | -18.06328 | -51.30962 | 2025-08-04 00:45:00 | TERRA_M-M | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 310c0cd9-89bf-345b-9a3d-4f702843f3f8 | -13.68126 | -41.37148 | 2025-08-04 00:45:00 | TERRA_M-M | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 37.5 |
| cd9760bc-f8dd-3443-a3a1-41ad02d649e7 | -17.3727 | -46.075802 | 2025-08-04 00:47:00 | METOP-C | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 66c545fc-5bf9-3e25-899a-730835d1dcb7 | -8.0134 | -43.157101 | 2025-08-04 00:47:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 96019cdc-6f73-398f-9e4e-2d8cb491d7a3 | -8.7505 | -46.416901 | 2025-08-04 00:47:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 93198d52-5852-3f98-81be-63ea06fb0003 | -7.5596 | -44.893101 | 2025-08-04 00:47:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b1ab2074-2ad2-3703-b96d-c05603c0ef1c | -8.0038 | -43.202 | 2025-08-04 00:47:00 | METOP-C | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 538a3005-f098-348b-9188-187a81f85eee | -8.1362 | -49.5877 | 2025-08-04 00:47:00 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9fa61209-7e86-3a0d-adc7-b7f60d72003a | -4.7476 | -44.434399 | 2025-08-04 00:47:00 | METOP-C | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| df5f8f0c-44aa-347f-a322-112357ed34ba | -6.6155 | -59.952702 | 2025-08-04 00:47:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f7594e3f-522d-336d-b20f-7bfbf7cc208f | -4.1347 | -47.639198 | 2025-08-04 00:47:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4ebea853-5772-304d-873d-3d341db69778 | -10.5741 | -45.268902 | 2025-08-04 00:47:00 | METOP-C | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 13aa9532-dbd6-3745-8cd1-6654aa1ff74a | -6.6108 | -59.930302 | 2025-08-04 00:47:00 | METOP-C | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 76b47380-7cd2-3be7-bbf0-2994e4ff780f | -15.7008 | -48.997501 | 2025-08-04 00:47:00 | METOP-C | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 01f7f8de-6ba5-347f-8268-fd43396a1608 | -18.065701 | -51.305 | 2025-08-04 00:47:00 | METOP-C | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 426728ac-580e-36c5-b3b3-ab13130aa466 | -21.258699 | -43.9813 | 2025-08-04 00:47:00 | METOP-C | BARBACENA | MINAS GERAIS | Brasil | 3105608 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 019f28d5-759f-37dd-93ea-4f43ea2e4fd3 | -19.9809 | -45.690899 | 2025-08-04 00:47:00 | METOP-C | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 82138650-2e84-38da-9f08-99c3d66e7f7e | -6.6205 | -59.928299 | 2025-08-04 00:47:00 | METOP-C | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 12b820c6-8701-334d-9bc5-d953a945bff1 | -10.2494 | -50.178902 | 2025-08-04 00:47:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cb55ce67-c1b2-3618-9993-b2f99bdd850f | -8.7465 | -46.4002 | 2025-08-04 00:47:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e0319a98-544b-3d58-b36d-1887a9025082 | -7.0133 | -59.824501 | 2025-08-04 00:47:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 01c9e07f-bc08-3ac9-b754-f820bdc355c5 | -19.530399 | -46.8946 | 2025-08-04 00:47:00 | METOP-C | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| d8cda693-d95b-3a3e-bca4-0fee49ca9657 | -8.0167 | -43.170502 | 2025-08-04 00:47:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 27cfbb7e-41c1-37a7-9543-d0353346b032 | -8.0618 | -43.102402 | 2025-08-04 00:47:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e1657000-5d1f-3564-bed4-31047ce27f9c | -8.0068 | -43.130299 | 2025-08-04 00:47:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ccfaf8e6-9706-3246-b1a3-f8ba9806c41c | -22.568501 | -42.1478 | 2025-08-04 00:47:00 | METOP-C | CABO FRIO | RIO DE JANEIRO | Brasil | 3300704 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7af0b02d-26b9-360e-909c-315c75d903ca | -11.763 | -44.967701 | 2025-08-04 00:47:00 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 529b1256-a4df-3fce-b7e5-e000c8174f6c | -4.1268 | -47.649601 | 2025-08-04 00:47:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2d9fd78a-4a3c-3cb8-aa07-044c8d4b3253 | -6.1463 | -57.897999 | 2025-08-04 00:47:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3e685f88-dd51-3960-bf19-b590ce594a91 | -7.7824 | -45.217999 | 2025-08-04 00:47:00 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f322bdd5-0192-3c01-84b9-713d0dddc59c | -8.0037 | -43.1595 | 2025-08-04 00:47:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 5158d37c-7c10-3015-a4b5-a3f0cdaae60f | -13.6897 | -41.359901 | 2025-08-04 00:47:00 | METOP-C | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 495a3afc-edbb-3f07-95ca-b2200602d564 | -18.0676 | -51.314201 | 2025-08-04 00:47:00 | METOP-C | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 4d0499f4-fe8e-3316-8c39-65488123ef35 | -22.578199 | -42.1451 | 2025-08-04 00:47:00 | METOP-C | CABO FRIO | RIO DE JANEIRO | Brasil | 3300704 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 517a72e1-0ce6-3e26-9d72-b12b09c132e7 | -12.15 | -43.379501 | 2025-08-04 00:47:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f2b6c502-6d16-3cee-af24-646ed6b3b6e1 | -17.374399 | -46.083199 | 2025-08-04 00:47:00 | METOP-C | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 77794969-070f-3e9b-8334-544642beae13 | -5.8817 | -50.1478 | 2025-08-04 00:47:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7e8b11a7-ec61-3921-8c5c-3cfadaf3e798 | -7.4515 | -48.942799 | 2025-08-04 00:47:00 | METOP-C | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 4c8920f0-9495-3bac-a75f-094c40c7e320 | -6.6522 | -59.0737 | 2025-08-04 00:47:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2b50073f-ee9c-3809-8a81-a2ec63bfbbe1 | -6.6466 | -59.0952 | 2025-08-04 00:47:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ac355fa8-10ad-3a62-a952-c676ccd4e3b4 | -4.1366 | -47.6474 | 2025-08-04 00:47:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d009fc9d-acef-32d6-bb91-017fe0676b30 | -8.0457 | -43.120701 | 2025-08-04 00:47:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 9fa308eb-3cda-36c7-a9ea-71b053249600 | -13.6957 | -41.342899 | 2025-08-04 00:47:00 | METOP-C | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 8348b0a2-58a2-333b-bcd1-5d09ed9b98ea | -9.3986 | -45.495701 | 2025-08-04 00:47:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 4affdd0e-bc16-3a8b-8666-3598b85fbc31 | -8.0391 | -43.0937 | 2025-08-04 00:47:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 7ad9509e-6953-3847-9556-ba2b3b589374 | -16.105 | -48.497101 | 2025-08-04 00:47:00 | METOP-C | ALEXÂNIA | GOIÁS | Brasil | 5200308 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 7b01ba65-0801-392d-99de-b349a6e509c4 | -16.439699 | -43.723 | 2025-08-04 00:47:00 | METOP-C | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 44b8e852-38a4-3f89-887f-52a5bc6bfdd1 | -19.982599 | -45.698299 | 2025-08-04 00:47:00 | METOP-C | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 0f4226cc-5dc5-3134-8b82-54cc4c816c39 | -9.4008 | -45.504902 | 2025-08-04 00:47:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 82869e94-aae5-3d7b-baa9-2b683678df6d | -18.063801 | -51.295799 | 2025-08-04 00:47:00 | METOP-C | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 8c7f3e4a-795d-3e8e-a7bb-3462a67c1abb | -6.6424 | -59.075699 | 2025-08-04 00:47:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b7c03b59-2f69-35bc-88c3-a44606264f5a | -4.1249 | -47.641399 | 2025-08-04 00:47:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4472c03f-25b1-3712-b9a4-7e8eea5163aa | -10.2541 | -50.200001 | 2025-08-04 00:47:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 070fe01c-ae69-3a8d-b48c-97515efafee6 | -8.0003 | -43.146099 | 2025-08-04 00:47:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 26c93fc9-43d3-36d2-b10d-42ee4c013455 | -8.0069 | -43.172901 | 2025-08-04 00:47:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 4f3a1be4-4441-34ea-9752-d7950d7fd2e9 | -8.3871 | -46.933201 | 2025-08-04 00:47:00 | METOP-C | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4e07841c-56b9-3d80-a490-5c609758ec8f | -8.0101 | -43.1437 | 2025-08-04 00:47:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 878a9ad6-2772-34f4-a519-cacd975da6a3 | -4.1287 | -47.6577 | 2025-08-04 00:47:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4c3559fc-5031-3d8d-9809-9a3def79a30b | -4.1385 | -47.655499 | 2025-08-04 00:47:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7fb6c588-9433-3b74-be0c-1fbd3171020d | -5.2972 | -44.879002 | 2025-08-04 00:47:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0eeb1583-7fe1-3865-a582-2283e3b6adbd | -8.0005 | -43.188702 | 2025-08-04 00:47:00 | METOP-C | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ccc9e935-5393-3037-97b7-9f0a1f9a49ce | -19.532 | -46.901901 | 2025-08-04 00:47:00 | METOP-C | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 4e87bc75-1d01-37ac-83dd-72f3290ac50b | -7.0086 | -59.802299 | 2025-08-04 00:47:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 14eeb608-545d-3edb-b23d-5b09f505c3cb | -6.1497 | -57.913799 | 2025-08-04 00:47:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 526c48f6-0b97-3e40-aa8d-70f4fa04a92f | -6.1561 | -57.895901 | 2025-08-04 00:47:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d6bb4ec2-2b48-3a6f-a0ef-51aa64ab8ffa | -8.7485 | -46.408501 | 2025-08-04 00:47:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 028dce58-0e08-3e06-baed-3e3162120611 | -8.0104 | -43.2285 | 2025-08-04 00:47:00 | METOP-C | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 603d8e82-5902-3bc3-9c85-ee253c080d75 | -22.583 | -42.164398 | 2025-08-04 00:47:00 | METOP-C | CABO FRIO | RIO DE JANEIRO | Brasil | 3300704 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a918444e-c645-3948-b02d-0bfd9dd50004 | -8.0585 | -43.088902 | 2025-08-04 00:47:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 5c77d38d-b9fc-369a-aa63-b4f93e7d59ee | -21.1682 | -49.064999 | 2025-08-04 00:47:00 | METOP-C | ELISIÁRIO | SÃO PAULO | Brasil | 3514924 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d5a32067-e1cf-3385-9d5a-b2e3747a1463 | -21.1551 | -49.051102 | 2025-08-04 00:47:00 | METOP-C | ELISIÁRIO | SÃO PAULO | Brasil | 3514924 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0e06d15d-d291-3d41-a973-cee7aa96e2b8 | -22.5709 | -42.157501 | 2025-08-04 00:47:00 | METOP-C | CABO FRIO | RIO DE JANEIRO | Brasil | 3300704 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7b2efb2a-0817-3899-bd2d-2e14fe03fed4 | -7.6577 | -49.840599 | 2025-08-04 00:47:00 | METOP-C | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 93a463be-f4bd-3272-8550-547de02879b0 | -7.7848 | -45.228001 | 2025-08-04 00:47:00 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 27a32765-5789-312c-a399-bd9255b6599c | -13.6994 | -41.3573 | 2025-08-04 00:47:00 | METOP-C | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 223ba353-446f-3050-a10d-d5e7b777c8e4 | -22.580601 | -42.154701 | 2025-08-04 00:47:00 | METOP-C | CABO FRIO | RIO DE JANEIRO | Brasil | 3300704 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9c2ed99d-9e6f-32ee-9ccf-1e1652653e58 | -20.7306 | -47.291801 | 2025-08-04 00:47:00 | METOP-C | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 23e57c55-1422-36a5-9719-6dce13869eff | -8.02 | -43.183899 | 2025-08-04 00:47:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 8c16bf52-1c8a-31ab-b714-88f5136fffd6 | -4.7505 | -44.4468 | 2025-08-04 00:47:00 | METOP-C | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 12a35485-2c5c-358f-91bb-b65692040b66 | -10.3384 | -50.0704 | 2025-08-04 00:47:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6f739be5-04f2-31aa-abe9-5539707ff082 | -7.4408 | -49.658798 | 2025-08-04 00:47:00 | METOP-C | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 82827b0d-80fb-3ab0-98cc-565be5171b09 | -12.1598 | -43.377102 | 2025-08-04 00:47:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ea40f4e4-662d-36fb-a0fc-398e1e055e08 | -8.0165 | -43.127899 | 2025-08-04 00:47:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 606534c3-b772-3fa1-af86-13ebeb567c91 | -10.251 | -50.185902 | 2025-08-04 00:47:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ea298312-0ef0-3174-afcf-6306e58a2eac | -8.0071 | -43.215302 | 2025-08-04 00:47:00 | METOP-C | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| da1b80e7-ccc5-3b9e-bf61-36a3ae68e267 | -16.437401 | -43.713501 | 2025-08-04 00:47:00 | METOP-C | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 93b9a618-9e7c-32e6-8b56-7f42344da5bf | -8.0521 | -43.104801 | 2025-08-04 00:47:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 31b3da44-c6b7-392e-85d0-82fb7ec4d0f6 | -15.7106 | -48.995201 | 2025-08-04 00:47:00 | METOP-C | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 6b202e2c-d245-3221-915b-b68e52259186 | -8.0297 | -43.181499 | 2025-08-04 00:47:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 0300036e-4900-3586-b090-43992a81b494 | -7.4423 | -49.6656 | 2025-08-04 00:47:00 | METOP-C | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3f416812-00e7-3f28-85d5-420f331a40b1 | -21.256701 | -43.973 | 2025-08-04 00:47:00 | METOP-C | BARBACENA | MINAS GERAIS | Brasil | 3105608 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 6fe21647-8d0b-3edb-bd6d-a8d73e2291c2 | -9.4106 | -45.502499 | 2025-08-04 00:47:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README3.md)

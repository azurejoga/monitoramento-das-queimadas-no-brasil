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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c6e13c36-6ac0-3336-b0d3-cfad420caf4c | -4.28064 | -48.24755 | 2026-08-03 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| dd703887-63d9-3510-a14f-56268f4aa230 | -3.67191 | -49.47028 | 2026-08-03 04:38:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5ad747c7-67b4-3202-bfff-025e4e20c02f | -6.5512 | -55.1612 | 2026-08-03 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 51bfd16c-0b3b-3c53-b4a6-512e02ce84ee | -9.4856 | -48.20579 | 2026-08-03 04:38:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a42b8897-a517-31ae-84d8-3c88b35a6e29 | -7.31969 | -42.99372 | 2026-08-03 04:38:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 3bc91573-c2c0-398c-9d1f-b0b36d7c9647 | -7.55706 | -45.03938 | 2026-08-03 04:38:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 81c03dd3-283b-3033-b42a-b193270b876b | -3.98306 | -48.42908 | 2026-08-03 04:38:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d3075f2b-c09c-3a44-bfd4-4143a4248a0b | -4.27233 | -48.19286 | 2026-08-03 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 54941077-0113-3eae-a9a9-f30e8bd9eed2 | -7.15514 | -44.04321 | 2026-08-03 04:38:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f86d0c40-5b6c-3f21-8b9a-2a23652c4b26 | -6.85467 | -44.78813 | 2026-08-03 04:38:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9a96db4c-1f51-3119-bd15-75cfc75b36b4 | -3.97013 | -48.12669 | 2026-08-03 04:38:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bbeea03e-41ca-342c-a258-fe514c0db86d | -3.97917 | -48.43205 | 2026-08-03 04:38:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a8b22cb7-f893-3343-873b-bf059b6364f5 | -5.73749 | -43.27559 | 2026-08-03 04:38:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 74856015-6069-357c-98cc-703c8b838a69 | -5.73357 | -43.27501 | 2026-08-03 04:38:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e0feb873-e7a4-3537-8600-7e329b0801fd | -6.06348 | -45.05056 | 2026-08-03 04:38:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1901034f-e1c3-3a90-943e-3b01377b8d78 | -7.5562 | -45.09475 | 2026-08-03 04:38:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 879800ae-e1af-39b7-8cc6-3fb81323bc7d | -6.84714 | -42.90351 | 2026-08-03 04:38:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e23b4a54-6c0b-3f2f-b0da-525739e068f9 | -8.35005 | -45.98802 | 2026-08-03 04:38:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8e9efb0b-6378-3e2f-aa95-355d1b77385f | -5.97228 | -45.00843 | 2026-08-03 04:38:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 676b3657-63f0-3e4e-883d-1d39466d412a | -6.9082 | -43.73042 | 2026-08-03 04:38:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 17466970-aaaa-3140-9473-4b8674c9fe4e | -10.54413 | -42.54336 | 2026-08-03 04:38:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 0474a669-eb6e-3900-b37d-44f51c486f6c | -6.54511 | -55.16295 | 2026-08-03 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 82099946-79d5-3f51-901d-27f65f198ade | -6.72485 | -50.94256 | 2026-08-03 04:38:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f399fda2-d047-341c-a5dc-16ee0dcf8003 | -7.34401 | -46.6081 | 2026-08-03 04:38:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 70991371-af60-379f-964b-e00756fea840 | -6.55581 | -55.16201 | 2026-08-03 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ee20877d-7274-3610-873d-ef043124f5a2 | -4.46202 | -47.9176 | 2026-08-03 04:38:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 3c06d6d2-3b23-3bf1-b9d1-5d640a5b45b4 | -4.82045 | -46.81005 | 2026-08-03 04:38:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f25e357b-9b5b-3498-b9d5-db9f6a617c96 | -5.73328 | -43.27806 | 2026-08-03 04:38:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a8e2f3b0-21ab-39cb-80c0-d77f544d6a83 | -7.55035 | -45.05956 | 2026-08-03 04:38:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4cbdb9f7-3a7e-3401-8e33-7ab4f38b6ed1 | -7.83204 | -44.45643 | 2026-08-03 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b5321f36-f5d6-34ef-981f-b894ef1a2639 | -6.85701 | -44.79736 | 2026-08-03 04:38:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0d9d4ba7-b40c-3a6f-891c-8d5f97f070f5 | -8.33957 | -45.98637 | 2026-08-03 04:38:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 31c5add5-2b54-3260-a459-09dbba4fafd0 | -5.73404 | -43.27314 | 2026-08-03 04:38:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b9797833-367c-3aa1-8a8a-53cef29327f8 | -3.97973 | -48.42854 | 2026-08-03 04:38:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e78b3dc4-6bc8-3e98-9706-7b702adde777 | -5.20594 | -46.0744 | 2026-08-03 04:38:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1eeb8dfc-24e7-3714-827f-541e025a496b | -7.15132 | -44.04266 | 2026-08-03 04:38:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b30e9a05-63d3-3e8d-b33a-cb728329266f | -7.35406 | -43.8554 | 2026-08-03 04:38:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 93d2fa7d-9ce2-3a29-80ef-f2d6181eddb5 | -7.38415 | -45.06773 | 2026-08-03 04:38:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5f90a587-6c69-3ec1-8882-c0b1ce3e4a69 | -7.38776 | -45.06831 | 2026-08-03 04:38:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9e588450-ef1b-3bac-ad66-caf7cbf830de | -8.55218 | -47.74568 | 2026-08-03 04:38:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4aa7e4f5-8eeb-348a-96e0-2ad70a7644c1 | -5.93113 | -46.04889 | 2026-08-03 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b97e9618-262d-307f-8c1e-9a97314d7f8f | -10.58015 | -46.78371 | 2026-08-03 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b57230eb-d969-3511-a02e-36c1d24cf643 | -5.62354 | -47.10336 | 2026-08-03 04:38:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 3f1f76b7-eedb-3fad-96e0-f7f12966ef74 | -5.97647 | -45.00492 | 2026-08-03 04:38:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5adeb844-bf77-30c7-870f-f22423aa4019 | -3.96737 | -48.12271 | 2026-08-03 04:38:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d6e3bb31-25d0-3d8d-a154-a679d8e97c36 | -4.59893 | -47.29047 | 2026-08-03 04:38:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0683b302-e896-34fb-abb6-a832883e2904 | -10.56921 | -46.7859 | 2026-08-03 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0ff21dfd-c9e9-3769-a003-2fd9ccb4e270 | -8.23544 | -46.25032 | 2026-08-03 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2881dc8b-c809-39b6-8626-9790643a313b | -6.8583 | -44.78875 | 2026-08-03 04:38:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| af0dd6a4-5aa9-31a7-8f72-67a86811a129 | -7.20915 | -45.76966 | 2026-08-03 04:38:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9612a4c7-b403-3729-a5c0-9ad1a6bcaaf4 | -7.34739 | -46.60863 | 2026-08-03 04:38:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 265cc48d-31a8-31b9-98f2-6907e7086b17 | -7.23127 | -43.52044 | 2026-08-03 04:38:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 11c91a81-20ff-3480-b03c-939d2acc367a | -7.5643 | -45.04051 | 2026-08-03 04:38:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 561df593-9930-3e0c-8053-23312f5cac76 | -10.5836 | -46.78425 | 2026-08-03 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 27fb362a-7340-3542-9f05-4b29681c751e | -6.56527 | -55.15653 | 2026-08-03 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 24ad74de-7616-3852-8942-202a30be22f9 | -6.55981 | -55.16052 | 2026-08-03 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c7260ef0-557e-359b-b971-ecb094cf728c | -6.54618 | -41.8382 | 2026-08-03 04:38:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6f200223-82ef-38dd-976e-bf1ae015b307 | -6.55602 | -55.15503 | 2026-08-03 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0a714be1-2784-3f3e-9f5c-be0ac83e9ee3 | -6.55434 | -55.16462 | 2026-08-03 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ac3e4475-f056-3429-9ea9-48f3c13ba76a | -9.63928 | -49.6751 | 2026-08-03 04:38:00 | NOAA-20 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 456f958c-3f0e-3159-b91d-631123f8085e | -6.56359 | -55.16615 | 2026-08-03 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0aba4a17-5249-3e78-bf25-61fbd9297331 | -8.34017 | -45.98248 | 2026-08-03 04:38:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dbcb76fd-6f5e-38f9-b665-5317629d95d8 | -6.85402 | -44.79244 | 2026-08-03 04:38:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5b7f5d90-7a4d-3088-b06e-f8f210b6f0a1 | -6.56065 | -55.15576 | 2026-08-03 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a90533ed-5d55-34eb-9952-790f6ad0d8f0 | -6.90433 | -43.72983 | 2026-08-03 04:38:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0f7e6b4a-8778-3ffe-b414-8544e61887d0 | -2.95593 | -50.34755 | 2026-08-03 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ffda1ac9-1e03-3fc3-9ee2-e5c9ecaf55c0 | -8.96957 | -45.18468 | 2026-08-03 04:38:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 72abf6c9-0539-3b6e-b133-87e3a4da7169 | -1.6591 | -54.4543 | 2026-08-03 04:40:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 4ee341dd-fdb2-32ae-b6d3-177e59f9ebf1 | -1.6408 | -54.4545 | 2026-08-03 04:40:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 0c5f3143-1a86-3b89-b77a-32f4c220619c | -11.2353 | -54.85246 | 2026-08-03 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 31ae9dbd-0cdb-39f9-b269-2b6bf0cfe74c | -12.24739 | -51.55542 | 2026-08-03 04:40:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9091826b-302a-30d9-a9e7-4d4b076fcf1d | -17.96317 | -51.61316 | 2026-08-03 04:40:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d2ad4c0f-97a6-3820-a750-30b8af49930f | -18.54062 | -45.1217 | 2026-08-03 04:40:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b65e7e2e-d8c5-3de5-bfba-7690a13b9204 | -10.62562 | -49.98911 | 2026-08-03 04:40:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b874b41e-674d-30a0-bc17-ce21fba1ca87 | -14.4089 | -53.27801 | 2026-08-03 04:40:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 83a4bccf-de2c-3e15-a52a-e917e38c2c47 | -11.26651 | -54.84655 | 2026-08-03 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5134bd24-fe6e-3249-a570-af29b1fbc8e5 | -12.33727 | -45.7106 | 2026-08-03 04:40:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 846436a2-71a5-3aeb-a1a7-dddaf4d654d7 | -11.26351 | -54.84398 | 2026-08-03 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| da2c55e8-f0b4-32ad-88b6-89046c7404e4 | -17.87151 | -40.05663 | 2026-08-03 04:40:00 | NOAA-20 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.1 |
| 3da34a42-c79e-30a5-91f0-d1a7f19f2a30 | -11.91773 | -55.90144 | 2026-08-03 04:40:00 | NOAA-20 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6b5d45d5-86c4-316a-a457-e496d2b10580 | -11.23324 | -54.86415 | 2026-08-03 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 844ddd3f-589a-3a22-9e28-a5d4a7e11c1d | -10.63677 | -49.98364 | 2026-08-03 04:40:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f439cae7-55f6-374e-93fb-640af6e4e554 | -12.26838 | -51.55029 | 2026-08-03 04:40:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 946c97ba-5fe7-367f-946e-3e61293fe43e | -11.27203 | -54.83957 | 2026-08-03 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1fc3892a-a609-3ce6-a3b6-c091af0e4e8f | -11.25673 | -54.82852 | 2026-08-03 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 95fa3b96-5c92-3d04-a454-b4df84de1eb3 | -12.33664 | -45.71503 | 2026-08-03 04:40:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cfb31e35-0ac4-36f9-b6b7-676f3db384ca | -14.10438 | -46.52225 | 2026-08-03 04:40:00 | NOAA-20 | IACIARA | GOIÁS | Brasil | 5209903 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 88938e25-135a-3ddf-8b53-d2452d7e869e | -11.82952 | -49.603 | 2026-08-03 04:40:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7f2b54c2-ff27-3639-bca9-a92e7a82dd03 | -11.23255 | -54.86811 | 2026-08-03 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d78463a8-0ef0-313e-b64b-61cdd5b9f2d3 | -15.23842 | -52.91092 | 2026-08-03 04:40:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5f528f7d-5317-3450-a2f7-c582735e7022 | -11.22764 | -54.84696 | 2026-08-03 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a66d5141-faa3-3244-83d1-d2feac9182b6 | -17.96253 | -47.13125 | 2026-08-03 04:40:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| cd1cf893-882c-39c4-99a8-17dd18a0044c | -16.33371 | -43.33366 | 2026-08-03 04:40:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d5433471-a838-3d00-9683-f8ac77257734 | -11.24975 | -54.81924 | 2026-08-03 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8c2cf1af-7e74-3c02-8bde-f1daf8d20fc0 | -11.13673 | -50.40493 | 2026-08-03 04:40:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6343430b-938b-3f6b-b975-91224fa35397 | -17.96621 | -47.13173 | 2026-08-03 04:40:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 5ff925fe-0aca-3ada-8f27-3ca69488aa1b | -15.23135 | -52.90961 | 2026-08-03 04:40:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 78b42e91-08ed-38bb-b8f6-d3d9541cf7ff | -16.22262 | -45.49274 | 2026-08-03 04:40:00 | NOAA-20 | URUCUIA | MINAS GERAIS | Brasil | 3170529 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c8b06fdb-0b5c-321b-bd9c-0af95ce224d8 | -12.26118 | -51.55778 | 2026-08-03 04:40:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f8c16cdc-5a63-3cf6-be55-2bd3570a0af8 | -12.26181 | -51.55392 | 2026-08-03 04:40:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README7.md)

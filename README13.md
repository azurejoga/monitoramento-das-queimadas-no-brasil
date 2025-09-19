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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 634459e5-6fb3-3e6d-9481-67d10c6b0e6b | -4.7806 | -42.75286 | 2025-09-19 03:53:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 99e4f325-bbb5-351e-bea1-00b813070a48 | -7.93222 | -43.87902 | 2025-09-19 03:53:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| baecd86f-ee0d-39db-a290-9488e008dedc | -6.96363 | -44.47365 | 2025-09-19 03:53:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 28571540-5b6d-347c-94a8-14db6e5e3f4b | -7.24293 | -39.17739 | 2025-09-19 03:53:00 | NOAA-20 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |
| e4988965-eb28-3f39-8b4c-ce03e1f0d253 | -5.71061 | -49.10272 | 2025-09-19 03:53:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 30830ba0-93ad-3e07-a989-e7998f876398 | -5.79563 | -45.35988 | 2025-09-19 03:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8abf34e2-0a60-38e0-afbf-0073557339b6 | -7.44499 | -42.64376 | 2025-09-19 03:53:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 5c222324-1298-32fc-8179-9efe35d75de0 | -7.50101 | -44.39941 | 2025-09-19 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 573e1591-1409-3a73-9b57-0a9b55004f45 | -4.99867 | -43.18032 | 2025-09-19 03:53:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 87a65879-6c95-39af-b531-5c2395dd722d | -5.79786 | -43.90348 | 2025-09-19 03:53:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 12dd868a-902c-3284-b2bc-d6b8a3b4499e | -9.14655 | -44.8485 | 2025-09-19 03:53:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cc55311c-eea1-3f65-98a0-a45069515f5b | -6.26076 | -43.9116 | 2025-09-19 03:53:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 266e204f-7857-371e-bd73-dce18a33a0bc | -5.12566 | -47.82829 | 2025-09-19 03:53:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 1e306c9a-27d4-309e-9f48-d71af1da05dd | -8.14834 | -46.77782 | 2025-09-19 03:53:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a12ff91b-6480-3e6e-9688-bcf384a6430c | -10.0992 | -40.92853 | 2025-09-19 03:53:00 | NOAA-20 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 6b615dfe-c888-39ce-937a-6838fae6dddc | -7.54653 | -45.50032 | 2025-09-19 03:53:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e660f338-f27e-36d6-91c1-7efa45c0c60a | -7.28544 | -43.92868 | 2025-09-19 03:53:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9b9903a2-ff67-34f4-a82b-7ada54822f0b | -3.68863 | -49.02028 | 2025-09-19 03:53:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b5db518f-1ef8-3450-8412-77968c7d6f5b | -7.65415 | -45.13256 | 2025-09-19 03:53:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a827ce1f-6898-365f-9b6f-d93f2edb1989 | -6.58939 | -45.5831 | 2025-09-19 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8bca276a-15e4-3253-ac8d-0b68179a62bb | -7.56883 | -45.47988 | 2025-09-19 03:53:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3a42d69b-d6db-33aa-bdcb-5c118f29ffca | -5.79182 | -45.35421 | 2025-09-19 03:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f4ef8a86-55a8-3322-b31b-473ec8fa8d65 | -5.45475 | -46.69867 | 2025-09-19 03:53:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1006842a-5971-35a6-9a28-54edfda42c76 | -7.04364 | -46.41117 | 2025-09-19 03:53:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b85889a9-c886-32d0-b866-8181d8522132 | -4.77746 | -42.74706 | 2025-09-19 03:53:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 59756723-d2bc-312f-b541-68f965aca974 | -7.57516 | -44.78081 | 2025-09-19 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ed0bc90d-4ea4-343e-8bef-218ce368387b | -7.44433 | -42.62455 | 2025-09-19 03:53:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c3cd8d85-551a-310d-b230-af2ee93add47 | -6.48265 | -39.68736 | 2025-09-19 03:53:00 | NOAA-20 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5400aa52-5272-3ab6-b197-5a0f1bce913d | -5.96236 | -47.09635 | 2025-09-19 03:53:00 | NOAA-20 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9d699e29-d87c-31ed-8c02-933ce854e586 | -5.21125 | -45.17616 | 2025-09-19 03:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 65db7c6d-4c71-376b-9236-d8b997e29da7 | -7.35522 | -38.9631 | 2025-09-19 03:53:00 | NOAA-20 | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 86717545-027a-3a30-a3f1-bfb1a3b78761 | -5.63084 | -45.9464 | 2025-09-19 03:53:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3a8f529b-a7a7-3896-a3ab-84d86af146e5 | -8.15221 | -46.78457 | 2025-09-19 03:53:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f42ac271-3b0d-37a4-b6e1-b39a52288e68 | -5.45686 | -46.68658 | 2025-09-19 03:53:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 18433f02-7eac-3960-99ae-7ba690b0a9a9 | -7.57338 | -45.48069 | 2025-09-19 03:53:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 15b149c1-d9c9-3fde-8aeb-c9366dd687c0 | -7.36444 | -44.5886 | 2025-09-19 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e695b9f8-17cf-34f2-a4b6-2b64229bc6a0 | -6.61603 | -45.62312 | 2025-09-19 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8a3c32ab-4ea0-30df-b1e4-b37918bafe51 | -5.91303 | -40.91777 | 2025-09-19 03:53:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 0bd1faf5-d217-3757-8b44-3a160bc1dd6c | -4.62369 | -47.01853 | 2025-09-19 03:53:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 977a66bb-b73b-3af3-8d22-07daf91d424a | -5.77686 | -45.97627 | 2025-09-19 03:53:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2897179e-cda3-3bde-9316-a02b509cf7d4 | -8.01918 | -44.79811 | 2025-09-19 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ee626ed5-d3aa-3ea4-9fc6-a00c086ff802 | -7.78251 | -43.8506 | 2025-09-19 03:53:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a444e056-886c-3792-9083-a7842429837e | -8.48564 | -44.73429 | 2025-09-19 03:53:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e56d192c-65e9-3154-b0a9-3bb05f2611b7 | -7.04269 | -46.41659 | 2025-09-19 03:53:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 368cda67-9646-3774-ba1f-6ab9c501bb9c | -5.6357 | -45.94728 | 2025-09-19 03:53:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1650c301-23a3-32a8-b7a7-13370833dd07 | -5.80329 | -45.71306 | 2025-09-19 03:53:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aef9ce76-10bf-31d8-8737-40c7eeea3749 | -6.95156 | -42.4396 | 2025-09-19 03:53:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 2505cbe5-14b6-3fd9-8aa7-69481ae9e9e1 | -5.91937 | -45.07943 | 2025-09-19 03:53:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 9b6ec6c1-8a18-3062-81ff-9f8ed5423130 | -7.04174 | -46.42201 | 2025-09-19 03:53:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e6fd4e5a-3d66-3bf0-87f1-88717ef9656b | -8.63496 | -45.71389 | 2025-09-19 03:53:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 848923ef-f4f1-3356-92c8-add29d5fe1e7 | -4.78226 | -42.74261 | 2025-09-19 03:53:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e827ac59-5946-361d-bb3f-518be9189389 | -9.14007 | -44.86047 | 2025-09-19 03:53:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 99d6ec14-28e0-3289-b5d6-cbbf36abdc17 | -7.2959 | -44.12873 | 2025-09-19 03:53:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0d053bc9-882a-3a84-b3ee-3d072ec0c723 | -7.92634 | -43.88898 | 2025-09-19 03:53:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 26719621-6d71-398a-ba91-778614db04f8 | -8.74919 | -44.2308 | 2025-09-19 03:53:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dd855781-84da-341e-92e2-e93631aeb6b1 | -7.24755 | -40.27724 | 2025-09-19 03:53:00 | NOAA-20 | SALITRE | CEARÁ | Brasil | 2311959 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 58d9d272-e58e-3bd4-ab44-7f77b04d4cb5 | -7.83856 | -45.6352 | 2025-09-19 03:53:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2d9950fb-a91d-365d-87e1-d9d48431ac33 | -4.7033 | -41.96087 | 2025-09-19 03:53:00 | NOAA-20 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9b8f993b-e231-3f91-9e58-af847d541304 | -9.18252 | -45.31152 | 2025-09-19 03:53:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2a1d941e-f928-3a7f-b544-934d1f30f94e | -5.7559 | -43.39516 | 2025-09-19 03:53:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7527e0f2-f82d-3c56-9dd3-cde6931056d3 | -8.68251 | -40.98612 | 2025-09-19 03:53:00 | NOAA-20 | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| a5bf89ad-3b1d-3456-9090-f4d296a417df | -8.95101 | -44.19711 | 2025-09-19 03:53:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9389a23a-3f3f-3991-a9d9-408f6b550edd | -7.57153 | -44.49233 | 2025-09-19 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f9a23e47-d8c3-3906-9ea2-c2efff79e0ef | -9.34074 | -44.52995 | 2025-09-19 03:53:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 243ab361-ec0a-32a0-b95a-4c568d2fe606 | -3.27726 | -49.14814 | 2025-09-19 03:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cf6769b7-c523-305a-bfb2-233709d2824f | -7.55645 | -45.49731 | 2025-09-19 03:53:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 84f5a0e9-99b2-3caa-9175-ab1934ecf8ae | -10.37016 | -42.46228 | 2025-09-19 03:53:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 4ffe5c02-0daa-3464-9a81-a720991970c3 | -7.34182 | -39.70935 | 2025-09-19 03:53:00 | NOAA-20 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| f706d2f4-ecb5-394a-af07-aca526e72698 | -6.97818 | -44.49223 | 2025-09-19 03:53:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 9227ab40-aff9-325c-bd69-976f7f25c01e | -7.56634 | -45.49439 | 2025-09-19 03:53:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 336c624e-09d0-3ab3-8485-a0ce74114563 | -5.44878 | -44.83088 | 2025-09-19 03:53:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 700b9171-82fe-350b-9bae-bb749841ec54 | -6.9046 | -44.76797 | 2025-09-19 03:53:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 2b1c04ee-55c4-3420-a5e0-8df29eda9764 | -5.66965 | -45.35086 | 2025-09-19 03:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e56b782b-b404-3e68-be58-94d7b6de11c0 | -7.92571 | -43.89276 | 2025-09-19 03:53:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f5093a46-d625-32c4-af95-df4ca012182c | -6.58704 | -45.58119 | 2025-09-19 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 67af0930-636e-3e6e-a7d6-d2adee1a6f04 | -7.55571 | -44.7899 | 2025-09-19 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 84c6123d-40b9-3208-af3b-d4b0c683b054 | -8.68906 | -46.45394 | 2025-09-19 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0fcad681-7052-30e3-a294-c72c1362de99 | -5.43583 | -46.68605 | 2025-09-19 03:53:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c4f2cfb6-a75c-388a-ad9e-b90fd69b8152 | -5.79943 | -45.36568 | 2025-09-19 03:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b3f3b9c9-9cca-3f1f-b1aa-38615bc6bbed | -8.37671 | -44.67877 | 2025-09-19 03:53:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1b94c0b3-0f07-3323-a494-629bd84e543f | -8.13491 | -43.62468 | 2025-09-19 03:53:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c0e0a943-37ff-3a46-af8c-11bbd55c7894 | -7.92756 | -43.88181 | 2025-09-19 03:53:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8ffb6149-c75f-3bc1-a009-b1a7622d78ff | -6.11398 | -46.33977 | 2025-09-19 03:53:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a7e4f9bb-0e92-3d67-877a-7f30d9b74a9e | -5.77368 | -43.71088 | 2025-09-19 03:53:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 63d0cbba-c433-3a66-b36a-e42ddc8acfed | -6.00806 | -44.33022 | 2025-09-19 03:53:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e3ee95c0-4487-3f3a-ad08-3c95cd6cd782 | -5.462 | -46.6874 | 2025-09-19 03:53:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 254ed4e3-93a5-3316-a059-d2ee5ff6431f | -4.53625 | -43.98175 | 2025-09-19 03:53:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 616731dc-e8da-3490-8dcd-41d92468dc8b | -9.72887 | -45.92742 | 2025-09-19 03:53:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 16bf2dd1-8ac9-3dd8-9c3f-aca3745c11a7 | -6.18539 | -41.2244 | 2025-09-19 03:53:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| d0d8f074-1e9c-3b69-afdc-8e8ceb658b34 | -8.13544 | -46.78501 | 2025-09-19 03:53:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a1ba5bce-5140-3c55-80ad-f848e036441c | -7.35578 | -44.58743 | 2025-09-19 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4d6c3bbd-2c69-33de-9eca-9833d1503ff5 | -5.7571 | -43.38787 | 2025-09-19 03:53:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cd8451e0-db9b-32e5-8a79-de8d25de966b | -8.13463 | -46.76928 | 2025-09-19 03:53:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ebdcd0bb-e041-3845-9e29-980efb8cbb4f | -4.27252 | -45.26709 | 2025-09-19 03:53:00 | NOAA-20 | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1fefae0c-4f4a-3a95-b41f-e307b602f360 | -5.6705 | -45.34595 | 2025-09-19 03:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bb0c8e2e-947b-3af0-8bdd-4898a0c815e5 | -5.82632 | -46.28158 | 2025-09-19 03:53:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 51e4f6c0-90a5-3e93-a252-6601da0953ec | -6.9037 | -44.79979 | 2025-09-19 03:53:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a4be22bf-28f3-3a2b-9ca7-62ab95bb549c | -7.48637 | -36.69314 | 2025-09-19 03:53:00 | NOAA-20 | SERRA BRANCA | PARAÍBA | Brasil | 2515500 | 25 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 78692709-bad5-3ca0-bb57-6702c7bf3e08 | -8.14733 | -46.78343 | 2025-09-19 03:53:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2cd74a75-b9d1-30e1-80ca-11ac7c83b411 | -4.68841 | -43.2428 | 2025-09-19 03:53:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README14.md)

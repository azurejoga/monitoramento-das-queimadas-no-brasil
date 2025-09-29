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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c65d71ab-230b-3289-92f3-e5312ef5ccec | -3.09657 | -47.00847 | 2025-09-29 04:06:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 22391e2f-9ae5-3fdc-b0da-017555f896c1 | -8.24717 | -45.48819 | 2025-09-29 04:06:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5cc816ae-e4d1-3253-85ab-52fd9bab320e | -6.17737 | -43.46806 | 2025-09-29 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 460e2ec1-40dd-34e5-8aa3-92fcece3ef55 | -5.65003 | -46.25584 | 2025-09-29 04:06:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 940033c5-fcef-3cc3-b98a-4fb90f410ca2 | -4.15455 | -40.00419 | 2025-09-29 04:06:00 | NOAA-20 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| cee2ac1b-1875-3b53-86d9-922c1bbe8159 | -5.02464 | -42.54127 | 2025-09-29 04:06:00 | NOAA-20 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e79a5968-73da-312f-9a0a-0b6695ddb4d9 | -8.30006 | -45.43554 | 2025-09-29 04:06:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 389b4d30-b13e-32f2-b8f0-b27ead70963c | -3.6025 | -41.37586 | 2025-09-29 04:06:00 | NOAA-20 | COCAL DOS ALVES | PIAUÍ | Brasil | 2202729 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b02e66a0-1eba-398f-b195-035efe2f6e75 | -5.76743 | -42.82849 | 2025-09-29 04:06:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 89035679-4141-366e-a33a-f0597c8cb2a0 | -6.28049 | -42.48065 | 2025-09-29 04:06:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| d7bba9b8-d00b-3580-b70f-55533bad3a44 | -7.82825 | -45.14177 | 2025-09-29 04:06:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 593871f9-eeee-35c3-8fde-83d8c2e3cb48 | -5.28346 | -43.15936 | 2025-09-29 04:06:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a0b2b399-82bf-30b4-99d2-4eb94ec592ad | -5.18882 | -43.76049 | 2025-09-29 04:06:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 338ba6e2-60bb-3b27-ba2e-c2f21c27d376 | -7.80721 | -46.9052 | 2025-09-29 04:06:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f91ec98b-6678-3780-987a-f577c127fd7f | -6.46969 | -42.91438 | 2025-09-29 04:06:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| bf3abd18-3b09-358f-83bf-bdce1c114f02 | -6.25551 | -43.63544 | 2025-09-29 04:06:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 8c38b4ca-9752-34e4-ba82-9ed865ee80eb | -5.75322 | -42.85244 | 2025-09-29 04:06:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| c443caa6-a7b9-398a-9c87-45e6bbbdbe5e | -4.74199 | -43.27575 | 2025-09-29 04:06:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 57c85928-4c2b-3ec0-9ce7-6e00eb8ea9d4 | -4.7541 | -38.47897 | 2025-09-29 04:06:00 | NOAA-20 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 44d12310-1d86-3aae-8805-6bb73f3a08e5 | -6.17333 | -43.47127 | 2025-09-29 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| e9de958e-2c17-3fc7-8e04-379c4cc22fd2 | -6.05997 | -42.47825 | 2025-09-29 04:06:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 636ef808-7bb4-363b-b9b4-ec6b864191c1 | -7.86698 | -41.06317 | 2025-09-29 04:06:00 | NOAA-20 | JACOBINA DO PIAUÍ | PIAUÍ | Brasil | 2205151 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 545ddffc-9d64-30e0-9fc7-3a146aa85402 | -7.03288 | -44.78271 | 2025-09-29 04:06:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7a54d4c0-29aa-38cc-9efb-2ba98a0f4ddb | -8.26606 | -45.47948 | 2025-09-29 04:06:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8cefaf2c-53b3-3318-95f2-e734e0dec365 | -3.05039 | -49.59821 | 2025-09-29 04:06:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9450e045-54d8-39b3-84ca-cd900f7514d9 | -4.26285 | -48.55389 | 2025-09-29 04:06:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b9207bbe-8870-37ae-84a7-421c3856496d | -5.90015 | -42.50434 | 2025-09-29 04:06:00 | NOAA-20 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d5eb06e6-7e63-31b7-b632-fc83dd946a44 | -7.21951 | -44.78932 | 2025-09-29 04:06:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 11201564-3771-3053-9f57-e6a5fea089b5 | -3.83192 | -40.3311 | 2025-09-29 04:06:00 | NOAA-20 | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c9796803-97c8-3e4c-9438-a62a96629ecb | -7.58345 | -44.80641 | 2025-09-29 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 8fdeab89-678d-3f7d-b905-f8fb1181d612 | -8.26676 | -45.49772 | 2025-09-29 04:06:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c3687c09-5007-3456-879f-37ace0ae3ac7 | -6.10966 | -41.82615 | 2025-09-29 04:06:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 021acf05-ab49-3bd3-83d1-548bbf1bef17 | -5.4725 | -42.87875 | 2025-09-29 04:06:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e53503cd-27d4-320c-a3fc-9d021fee2d10 | -7.01842 | -44.78025 | 2025-09-29 04:06:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 99ff8e5e-8699-3a8e-8e5c-a5879f4232e4 | -7.86421 | -41.05915 | 2025-09-29 04:06:00 | NOAA-20 | JACOBINA DO PIAUÍ | PIAUÍ | Brasil | 2205151 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 277ad0ea-08b9-3f6c-a53d-5115b9a62bac | -8.67168 | -43.98274 | 2025-09-29 04:06:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 61549885-266d-3698-bdfa-ac252961305e | -5.69176 | -42.62098 | 2025-09-29 04:06:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 90ed8696-29b1-39da-8119-5359c6acb4c9 | -5.8887 | -43.30022 | 2025-09-29 04:06:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c9e2390f-7bf0-3913-8d77-ced8f4ef1ba6 | -5.24396 | -45.35565 | 2025-09-29 04:06:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| de635f4e-0cf7-3f7c-8dd2-5104c6128690 | -4.39472 | -47.28683 | 2025-09-29 04:06:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0f0ceab0-a0cb-32b1-8c4c-5cf7b2c05768 | -6.05668 | -42.456 | 2025-09-29 04:06:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 21088166-9c32-3937-b923-edcea10059ca | -7.43971 | -43.03161 | 2025-09-29 04:06:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 72262669-8157-3165-b385-ec81b185cd5b | -2.58002 | -48.41012 | 2025-09-29 04:06:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 35.8 |
| 61265b0b-3de6-3fb7-83bd-c2cb56b73a44 | -4.40363 | -44.08709 | 2025-09-29 04:06:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 284d66d7-cc81-30fd-9a76-28aa3a07089c | -4.5072 | -40.7237 | 2025-09-29 04:06:00 | NOAA-20 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| cddf8f2d-7b3a-3b1a-88cc-667522f496d6 | -5.29315 | -43.1647 | 2025-09-29 04:06:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| af5b2412-6f33-3884-a066-8b0d3ee46037 | -6.08344 | -42.46026 | 2025-09-29 04:06:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| eaffe7f8-c733-32e9-be3c-d770b1e3ba27 | -5.48509 | -46.97032 | 2025-09-29 04:06:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9e62fc95-05e6-3197-905d-35907e3b4f8d | -6.83032 | -44.82892 | 2025-09-29 04:06:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| e69a0d55-2b7d-3870-b179-c8c5f433bacd | -5.71775 | -42.83549 | 2025-09-29 04:06:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 11355f3c-604b-37e6-b7de-22e322127a42 | -5.78535 | -42.65034 | 2025-09-29 04:06:00 | NOAA-20 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 1355093b-f019-34d7-983f-c60d3c966cad | -5.74212 | -42.66168 | 2025-09-29 04:06:00 | NOAA-20 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ed711608-4565-3fc8-a343-8b865938e17b | -2.22292 | -48.36895 | 2025-09-29 04:06:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 861ad295-4675-3041-9e79-6411c8225e5c | -7.81201 | -46.99849 | 2025-09-29 04:06:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1c654a41-0b8b-3ad7-a233-fd21933893ca | -5.24685 | -45.35346 | 2025-09-29 04:06:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 58a11d2b-54e7-38f9-a08f-856cd94012f3 | -7.21507 | -44.77145 | 2025-09-29 04:06:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6e81e3cf-7f92-3328-ada7-edfb8bc76f3a | -7.89613 | -44.57744 | 2025-09-29 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6b4e5e93-6d15-370e-b775-6df3a9deac06 | -4.74808 | -42.69455 | 2025-09-29 04:06:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1048ff15-4e3e-31f9-9b9d-2e6f5a8f0e4f | -3.22801 | -40.02433 | 2025-09-29 04:06:00 | NOAA-20 | MORRINHOS | CEARÁ | Brasil | 2308906 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e9786c1f-268a-3fb1-b6f3-c62eb4283974 | -5.78322 | -42.84612 | 2025-09-29 04:06:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 24ae9575-a110-3e51-bae5-debe5a909ea0 | -3.50079 | -52.47034 | 2025-09-29 04:06:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8e572497-9bef-39df-8582-1f65947d3885 | -6.27486 | -42.49436 | 2025-09-29 04:06:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 1db78347-71cf-3fe5-ab46-6b1feea95a55 | -5.68669 | -42.63116 | 2025-09-29 04:06:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3eb75c7c-6d2d-346b-a4e2-b20ce331a115 | -5.73583 | -42.83093 | 2025-09-29 04:06:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 79febcb7-5a4c-308e-bb41-964cfdbd694f | -6.46033 | -44.00808 | 2025-09-29 04:06:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 9e95dc85-b105-37dd-85d2-beafa4943888 | -7.79931 | -48.3148 | 2025-09-29 04:06:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b19e47d4-8d48-3568-9ec3-5c676cdab8bd | -5.73525 | -42.83453 | 2025-09-29 04:06:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 7dd09cc1-197b-3e76-b1b3-bd9a157aae72 | -4.14465 | -40.00615 | 2025-09-29 04:06:00 | NOAA-20 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4a0c2d95-d17d-3b81-a30e-1661b1541a4e | -8.2516 | -45.48438 | 2025-09-29 04:06:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4cbadf42-b610-3ca1-af5c-fd2d81a14d3c | -5.74639 | -42.54889 | 2025-09-29 04:06:00 | NOAA-20 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| e0b68808-50cb-3e58-87d2-8f706b581fe0 | -5.5092 | -42.2068 | 2025-09-29 04:06:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e36cfac4-474b-35f2-8092-b0666f937476 | -3.30143 | -48.71007 | 2025-09-29 04:06:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| edec9d75-7f63-3655-b210-07297f751d7a | -6.05719 | -42.47419 | 2025-09-29 04:06:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5731b89a-4c2d-383d-b2c7-d4dbeec0046d | -5.42447 | -42.26563 | 2025-09-29 04:06:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9b4bacbb-979a-3ddf-8d93-388a88fe72dc | -5.97401 | -44.23678 | 2025-09-29 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9a98b0ec-53b5-3758-9df8-5541776a7fdb | -6.82964 | -44.83311 | 2025-09-29 04:06:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 16fa0244-f047-34f8-886c-d366a0577e55 | -7.25073 | -43.00493 | 2025-09-29 04:06:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| f1a3fb0f-855f-39b8-8a0d-61fed12390b1 | -5.9496 | -46.40969 | 2025-09-29 04:06:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e1fbec5a-5e68-3447-8962-5758c730648b | -7.72969 | -46.99265 | 2025-09-29 04:06:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2d073702-e62d-3710-8e68-ed3bf2a66c36 | -7.17855 | -41.7052 | 2025-09-29 04:06:00 | NOAA-20 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a6dcfb9b-e423-3245-a133-d957a56e52e3 | -6.4999 | -44.11943 | 2025-09-29 04:06:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 73ddbf36-a899-30b6-bc14-506861b119d0 | -7.22451 | -44.78155 | 2025-09-29 04:06:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 31.9 |
| c55da4fe-ca31-3b31-a286-b2eea68c3202 | -6.98257 | -44.40334 | 2025-09-29 04:06:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9c167b5c-101b-309a-853f-c61b555b8a50 | -6.82669 | -44.82827 | 2025-09-29 04:06:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 4b9c0ca6-dcd1-35b4-9b08-6ffa30cc2006 | -3.61089 | -42.76595 | 2025-09-29 04:06:00 | NOAA-20 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 077ae73f-5dd3-343e-a149-feab81dc0236 | -6.58066 | -43.42366 | 2025-09-29 04:06:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 2.7 |
| a24eda4d-26af-3398-9029-e1cb2544dfea | -8.62765 | -44.01442 | 2025-09-29 04:06:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3ae263e8-eeba-3c52-8777-c2e4fb417967 | -6.21956 | -44.21559 | 2025-09-29 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 12f22591-20ef-359f-a69d-14eab3fe9a88 | -7.28958 | -44.61018 | 2025-09-29 04:06:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ab3fe1a1-fbc1-3748-96a0-a8b37d2d2569 | -5.15526 | -46.41898 | 2025-09-29 04:06:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c9502118-dfb1-32a5-90a6-4f7d37b4be14 | -6.19131 | -44.29829 | 2025-09-29 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| b3b19591-15ab-39a8-8cc3-f0729029b4d7 | -5.76685 | -42.83213 | 2025-09-29 04:06:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 467e235d-d900-3e5e-86a6-639612cb6162 | -4.56822 | -37.8558 | 2025-09-29 04:06:00 | NOAA-20 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a9a9200a-67f7-34f0-a5a1-5fe92d83a785 | -6.20102 | -42.84546 | 2025-09-29 04:06:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 90044d9d-75d2-3500-8281-b680043c4828 | -4.76668 | -46.59777 | 2025-09-29 04:06:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 536a7cfc-b141-34c8-9529-3540a29fbbc6 | -5.50574 | -44.01593 | 2025-09-29 04:06:00 | NOAA-20 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 85ba3071-7e0e-3c14-acdf-fbedf5b97fe5 | -4.70806 | -41.98585 | 2025-09-29 04:06:00 | NOAA-20 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 39b6c60b-f8eb-33a0-a9f9-17d8e534929b | -7.38375 | -47.03627 | 2025-09-29 04:06:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4cc4779f-b24a-300e-9437-a49d6f440246 | -6.0611 | -42.47118 | 2025-09-29 04:06:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c0b2a343-5e03-394b-8bed-9edbc1604712 | -8.05929 | -44.11868 | 2025-09-29 04:06:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README31.md)

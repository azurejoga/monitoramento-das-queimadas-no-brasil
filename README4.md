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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bd402078-bbfe-3555-a706-0c6484047d24 | -21.60476 | -48.77041 | 2025-05-06 03:57:00 | NOAA-21 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0f308bad-5519-30a4-b27e-1b600b9229d2 | -22.85769 | -42.98119 | 2025-05-06 03:57:00 | NOAA-21 | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 1897b5a6-bb7e-3609-a1ae-660797828f91 | -22.67438 | -43.47954 | 2025-05-06 03:57:00 | NOAA-21 | NOVA IGUAÇU | RIO DE JANEIRO | Brasil | 3303500 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 0d71433a-5236-3638-b223-54c5bc39a852 | -17.09622 | -43.80415 | 2025-05-06 03:57:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f775889a-6027-37e3-b739-7db13878381e | -17.77671 | -42.80899 | 2025-05-06 03:57:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f2508065-e447-3dd4-8ac8-d141f9653bf0 | -23.40697 | -46.55728 | 2025-05-06 03:57:00 | NOAA-21 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 6ab3c22a-7720-3be7-a8db-28fc05c55800 | -21.36815 | -48.63053 | 2025-05-06 03:57:00 | NOAA-21 | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 8484325d-2c1b-34ba-876d-ef57c433916a | -21.8235 | -53.61699 | 2025-05-06 03:57:00 | NOAA-21 | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d31c5010-8064-38c1-926d-0aa4a5b3f409 | -22.91972 | -45.41338 | 2025-05-06 03:57:00 | NOAA-21 | PINDAMONHANGABA | SÃO PAULO | Brasil | 3538006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 44e5a937-b1c1-36fe-b16e-a54a397b686a | -16.68222 | -43.88617 | 2025-05-06 03:57:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d0b42469-eaa1-30cc-8bbc-37f664bdbd7e | -19.53185 | -43.92015 | 2025-05-06 03:57:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| a40a08d5-b796-32e1-9acd-b70fef147723 | -19.84123 | -45.01967 | 2025-05-06 03:57:00 | NOAA-21 | NOVA SERRANA | MINAS GERAIS | Brasil | 3145208 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 438c6b58-711c-31a8-98c9-5664ea63b493 | -22.34278 | -41.78296 | 2025-05-06 03:57:00 | NOAA-21 | MACAÉ | RIO DE JANEIRO | Brasil | 3302403 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| b5ddab05-684d-3ce9-bcbc-560487de2414 | -19.84167 | -44.61145 | 2025-05-06 03:57:00 | NOAA-21 | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 42fece91-3b19-34cd-bac4-53b487b77fb0 | -20.05855 | -49.37179 | 2025-05-06 03:57:00 | NOAA-21 | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 5dec434f-7d10-35f5-a351-aa79083d0ab2 | -21.03361 | -48.98745 | 2025-05-06 03:57:00 | NOAA-21 | CATIGUÁ | SÃO PAULO | Brasil | 3511201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 9b189937-7b0b-322c-bc73-874c42c9cfe0 | -18.79954 | -39.76967 | 2025-05-06 03:57:00 | NOAA-21 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 390c95b4-6669-3ecd-bb1c-007929db4f11 | -6.7053 | -42.1234 | 2025-05-06 04:00:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 68.2 |
| 50305d60-9bed-3234-bec0-827de77ae3cc | -23.60197 | -49.00478 | 2025-05-06 04:00:00 | NOAA-21 | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6ca30728-69f7-39fe-9cf7-b5d9b96e2175 | -23.0481 | -49.89586 | 2025-05-06 04:00:00 | NOAA-21 | OURINHOS | SÃO PAULO | Brasil | 3534708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| c77758b6-e0dd-3b3d-84cb-b61fe9d99ed3 | -23.60872 | -49.01575 | 2025-05-06 04:00:00 | NOAA-21 | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 495592b6-833b-3a77-a2f7-07986b58d037 | -23.60105 | -49.00933 | 2025-05-06 04:00:00 | NOAA-21 | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 35.1 |
| ad6ae8db-b6df-3146-9fb0-ee1b42e1cea0 | -21.7276 | -56.11104 | 2025-05-06 04:00:00 | NOAA-21 | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 8e2e8e75-38d3-383a-912f-8891c93118ca | -21.72082 | -56.10949 | 2025-05-06 04:00:00 | NOAA-21 | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 40445c15-0525-37dd-9b75-f2876b65c2af | -23.04087 | -50.44076 | 2025-05-06 04:00:00 | NOAA-21 | ITAMBARACÁ | PARANÁ | Brasil | 4111001 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| eb1dc370-68b9-3440-8338-663505084ac0 | -23.60013 | -49.01386 | 2025-05-06 04:00:00 | NOAA-21 | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 35.1 |
| 2d9d84fe-97f5-3268-b7d1-2735bdc2eac3 | -23.98375 | -48.91697 | 2025-05-06 04:00:00 | NOAA-21 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1c99646b-534f-3ce6-8fd5-6b795b02a227 | -23.03996 | -50.44326 | 2025-05-06 04:00:00 | NOAA-21 | BANDEIRANTES | PARANÁ | Brasil | 4102406 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 408ff599-0b67-30ad-9dff-e9e1e5be361c | -23.04687 | -49.8978 | 2025-05-06 04:00:00 | NOAA-21 | OURINHOS | SÃO PAULO | Brasil | 3534708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| caae2307-3a2d-3920-a9fd-7417e1e6ade4 | -23.60287 | -49.00029 | 2025-05-06 04:00:00 | NOAA-21 | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1a5bfb80-8e7c-34d3-9ecf-95e56d7c80f8 | -23.23766 | -51.28598 | 2025-05-06 04:00:00 | NOAA-21 | CAMBÉ | PARANÁ | Brasil | 4103701 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 881ee25e-9b6d-3a76-a15b-8e517ba4b396 | -21.72684 | -56.10726 | 2025-05-06 04:00:00 | NOAA-21 | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 6df1a2e4-6729-315f-a0a3-2b64b3a0ad36 | -23.55956 | -47.85412 | 2025-05-06 04:00:00 | NOAA-21 | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 932a9743-fec4-32d6-b1f4-86eacbee9558 | -21.72523 | -56.11377 | 2025-05-06 04:00:00 | NOAA-21 | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 2785eb49-3911-3434-be17-4543d6e3c784 | -23.60534 | -49.01029 | 2025-05-06 04:00:00 | NOAA-21 | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cc222194-7a2f-363c-996d-af4b7da69072 | -29.77807 | -51.17406 | 2025-05-06 04:02:00 | NOAA-21 | SÃO LEOPOLDO | RIO GRANDE DO SUL | Brasil | 4318705 | 43 | 33 | nan | nan | nan | Pampa | 0.6 |
| 149e07fd-2684-3a5e-98e9-fa4e1d480492 | -6.19435 | -48.04442 | 2025-05-06 04:19:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2065aa77-6969-3f43-8fbc-a595a9cdf9bb | -6.96643 | -42.79579 | 2025-05-06 04:19:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 6b363016-006d-3e90-8d54-21a6dc1078cb | -6.8432 | -42.80406 | 2025-05-06 04:19:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 46b22fcd-b1f8-32b6-b8bc-d7e9585347de | -6.70341 | -42.13401 | 2025-05-06 04:19:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 9ab51e58-232f-3fa6-a1ba-12df913aa4ac | -5.16296 | -45.10725 | 2025-05-06 04:19:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 695947b3-06a4-3a9e-911a-4c2b52b5719c | -6.94915 | -42.79314 | 2025-05-06 04:19:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 5fb1eca3-c875-33d0-bdcb-e97921363226 | -6.69694 | -42.12897 | 2025-05-06 04:19:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 34416c62-34fd-3db9-a794-558ded035d79 | -6.96471 | -42.80714 | 2025-05-06 04:19:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 926e0ba5-c574-3a53-aa2a-20bccd5357d1 | -5.16352 | -45.10376 | 2025-05-06 04:19:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 220d09c9-078c-358e-aa02-0f8fa54036a1 | -6.96125 | -42.80659 | 2025-05-06 04:19:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f0020747-c952-3ab5-a451-64c4100d1939 | -6.69926 | -42.13744 | 2025-05-06 04:19:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 14.4 |
| 849153e9-78ee-322f-903f-3e8376432428 | -6.95376 | -42.78608 | 2025-05-06 04:19:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 916bec32-d1c8-361e-9e79-5e3e0ff9ce5c | -6.96989 | -42.79633 | 2025-05-06 04:19:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 1ec1c0d1-d385-37b2-a3ce-034d9cc5fdac | -6.94973 | -42.78935 | 2025-05-06 04:19:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 32603472-e023-30c8-9426-ec601127dc2d | -6.69987 | -42.13348 | 2025-05-06 04:19:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 14.4 |
| eb554d01-4202-3bba-b362-0882dcff1b82 | -6.96183 | -42.80282 | 2025-05-06 04:19:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f655c3ca-ab09-3bc4-96e6-5becea84213e | -6.97047 | -42.79254 | 2025-05-06 04:19:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6197b713-8f8a-316f-9940-300b9fa23488 | -6.70048 | -42.1295 | 2025-05-06 04:19:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 67db000e-c8ba-308d-94c1-36f202fdb76d | -6.96528 | -42.80336 | 2025-05-06 04:19:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c86a911a-4572-3ed3-85af-990daccd8f01 | -4.12396 | -46.67854 | 2025-05-06 04:19:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0bb1e32c-58b7-3254-bafd-196d0db63f28 | -6.95664 | -42.79039 | 2025-05-06 04:19:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| e546f687-7de5-3108-a094-4865e90765d6 | -6.69633 | -42.13294 | 2025-05-06 04:19:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 14.4 |
| 2dd2cc6a-4cfd-31b5-9999-5202f63d5752 | -6.96931 | -42.80012 | 2025-05-06 04:19:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 9347ad47-dc3d-301d-b725-37f5c89b40b8 | -6.96413 | -42.81091 | 2025-05-06 04:19:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f9adb6fb-8417-3180-a749-f0d6eb150f25 | -5.16018 | -45.10324 | 2025-05-06 04:19:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ab8269f2-5cd2-3c7f-aa1f-af065cd5f311 | -5.15963 | -45.10673 | 2025-05-06 04:19:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2ccf06bd-a53c-3691-9345-2d071f3e346d | -6.95318 | -42.78986 | 2025-05-06 04:19:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 44779ab2-1157-3bc5-bfdd-7a521c101018 | -6.96586 | -42.79958 | 2025-05-06 04:19:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 09eea959-151d-36c3-a037-f9dd380b03c8 | -4.12458 | -46.67466 | 2025-05-06 04:19:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 61a0fd5f-5580-35e1-aa36-739608228855 | -4.12044 | -46.67797 | 2025-05-06 04:19:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bafe2353-c16f-3e47-a1a0-55b9fd59fb85 | -6.84665 | -42.80459 | 2025-05-06 04:19:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 47309de5-f297-32c2-a5e0-2f4c6abdcd17 | -6.96873 | -42.80391 | 2025-05-06 04:19:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| bc3d70cd-8e05-3567-8eca-8766b78c6611 | -2.6363 | -47.96286 | 2025-05-06 04:19:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 208290f3-a256-3506-a2ce-d32c2b4875ee | -2.63555 | -47.96756 | 2025-05-06 04:19:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1279570f-8830-376b-a7a0-aeb009ff57d1 | -6.95722 | -42.78661 | 2025-05-06 04:19:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 634f8d8e-10e7-34df-a8cc-9dde214ffb82 | -6.69279 | -42.13241 | 2025-05-06 04:19:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5c401fe2-1bd9-357a-8004-8424cc377ea3 | -6.95261 | -42.79364 | 2025-05-06 04:19:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| acbc1463-1969-34e8-8d92-24f598c4ed95 | -6.22818 | -36.52563 | 2025-05-06 04:19:00 | NPP-375D | CURRAIS NOVOS | RIO GRANDE DO NORTE | Brasil | 2403103 | 24 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 89dc7f17-a882-385f-b0bc-4a7526190472 | -8.30532 | -48.05303 | 2025-05-06 04:21:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 558bd806-e843-3d90-b432-30b08d8f12bd | -13.6695 | -47.84479 | 2025-05-06 04:21:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 95191f09-25ce-3a26-ae87-6cd53dcb4a5a | -14.23117 | -45.47291 | 2025-05-06 04:21:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cdc75afb-1cae-3a0a-a702-04ff8ab60ebd | -14.22276 | -45.46036 | 2025-05-06 04:21:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9b535a4e-67a3-38b9-a803-987ca4b1e501 | -8.31025 | -48.04544 | 2025-05-06 04:21:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ed5c3f11-f7b2-3ba2-b692-6e4a31a78f07 | -14.22612 | -45.46091 | 2025-05-06 04:21:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 48352612-2ba1-3254-a7c2-134488029a14 | -6.71793 | -47.59647 | 2025-05-06 04:21:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e77fbf14-2994-36c4-987e-f62208daf289 | -7.55886 | -45.84114 | 2025-05-06 04:21:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 98e9f602-2552-35c3-a4a1-a6ff62be045d | -7.55273 | -45.83656 | 2025-05-06 04:21:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2237d816-4634-3e26-89af-bab88d7c37c0 | -14.21718 | -45.47438 | 2025-05-06 04:21:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b396388d-15a4-31c2-bff8-0e4fe456973b | -14.2362 | -45.46252 | 2025-05-06 04:21:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 71282194-8e3e-3d85-ab10-d0473fa75cf0 | -14.21548 | -45.46292 | 2025-05-06 04:21:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e656752a-52f9-3869-839a-ecf797f5e53d | -8.30958 | -48.04953 | 2025-05-06 04:21:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 40216ace-0e67-3f12-bc2d-d5d015d00830 | -10.98946 | -44.43877 | 2025-05-06 04:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5d143e83-56cc-39cc-8f5c-d158d18a9811 | -14.21493 | -45.46656 | 2025-05-06 04:21:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cdadb4a4-9caa-3a6d-bcf5-4813f499c1fa | -7.70959 | -45.66282 | 2025-05-06 04:21:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f2ba9e47-2b12-3037-9dea-a40522d0548a | -14.21101 | -45.46965 | 2025-05-06 04:21:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3470daaa-328d-3ce6-a17e-49ea9a091b54 | -12.17322 | -54.23845 | 2025-05-06 04:21:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d03088f7-3223-305a-9e1f-bfbf276bc5b8 | -14.23284 | -45.46198 | 2025-05-06 04:21:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| adc1d47c-232f-37db-b4ba-ee2bc52b4521 | -11.19162 | -44.50756 | 2025-05-06 04:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f9a90eae-7849-3389-890c-bac5678a4da6 | -13.06595 | -47.58215 | 2025-05-06 04:21:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b021e500-08e9-3814-92e5-fa49a55b22b2 | -6.78649 | -47.59389 | 2025-05-06 04:21:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 63223291-4de7-3a4e-8d1c-6e34955eb581 | -8.07344 | -43.12996 | 2025-05-06 04:21:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 15.3 |
| 78ddebdd-1dc5-356f-ab8f-a79d5e4766bf | -14.2071 | -45.47275 | 2025-05-06 04:21:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e6914e71-f806-3a53-bfc3-6d596e567cad | -14.21212 | -45.46238 | 2025-05-06 04:21:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 05557395-9879-34e4-ac65-deb11cb9609b | -11.00123 | -44.33972 | 2025-05-06 04:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README5.md)

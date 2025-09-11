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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e820c914-6ef0-31c9-a061-0cfe5825896f | -7.38735 | -47.36748 | 2025-09-11 04:21:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 634b26f1-6407-3820-bbf5-c3911aedc75b | -7.39093 | -50.89297 | 2025-09-11 04:21:00 | NPP-375D | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3462b104-a362-3e2a-a9e7-56ac1f4c9021 | -5.84266 | -43.86454 | 2025-09-11 04:21:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e0cf3b2f-9b8b-3ada-8f63-3e42aba0805e | -5.84185 | -46.15452 | 2025-09-11 04:21:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9daf3f35-7237-3fbe-b545-d0e0cb158aa3 | -3.66577 | -43.08823 | 2025-09-11 04:21:00 | NPP-375D | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7967fa75-a230-3d96-b907-a90a5cc910c5 | -7.29156 | -45.18504 | 2025-09-11 04:21:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b1255f4d-8b0d-31f8-ac6a-0585e8ce9428 | -4.71429 | -44.94697 | 2025-09-11 04:21:00 | NPP-375D | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 09c46616-1842-3552-9b17-6206498c4d7f | -8.52433 | -45.68958 | 2025-09-11 04:21:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6f8d28ae-e13f-3df0-9c89-e1ccdb115db1 | -6.39732 | -43.50565 | 2025-09-11 04:21:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0871f68a-249a-3454-88f6-e0b75d9c0299 | -5.36122 | -45.22208 | 2025-09-11 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5fb6b0bd-7b5f-34a6-bcdf-64b987209100 | -6.65992 | -44.54551 | 2025-09-11 04:21:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5d554c67-6088-3d5f-8a8b-d0a1c8fd1d1b | -8.96776 | -46.06878 | 2025-09-11 04:21:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ffda360f-8cd3-32a4-ac16-52a0ce39182d | -6.84696 | -47.88797 | 2025-09-11 04:21:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bca1cc5b-6d4e-3686-8159-2104a98ca59c | -8.03298 | -48.66148 | 2025-09-11 04:21:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 83f20a60-cf2b-3c86-8739-f9e39bc7dd9e | -6.30285 | -44.92273 | 2025-09-11 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 08272f54-610f-378f-b751-813355e56b31 | -5.55762 | -43.0472 | 2025-09-11 04:21:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| da13ec97-e8e6-3d67-af1b-5667bbbde107 | -5.85866 | -47.05513 | 2025-09-11 04:21:00 | NPP-375D | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 05a2ed22-57ae-38aa-aaac-52208d7dbeb4 | -5.53049 | -44.34697 | 2025-09-11 04:21:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 975ffaa5-9625-3bfc-a167-4c2b58bf9e7a | -7.89943 | -46.25559 | 2025-09-11 04:21:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 33dfaf44-8d8f-31dd-9e4d-bd1eb966899b | -5.66646 | -43.89105 | 2025-09-11 04:21:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 467782ac-c42c-3f52-822f-20cf6a6a056b | -1.86371 | -47.98767 | 2025-09-11 04:21:00 | NPP-375D | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 524058e7-e5d7-36e3-8f00-7e4fc25002d4 | -6.76028 | -39.26225 | 2025-09-11 04:21:00 | NPP-375D | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 3af058d6-a9b4-3e7e-8221-68f41ac82bee | -6.57116 | -44.80555 | 2025-09-11 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6a2a131f-a3b6-3010-aa89-ff3f63e10640 | -8.46355 | -47.27846 | 2025-09-11 04:21:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 236fe7d4-abb2-346e-a670-2d65448c86a4 | -8.46292 | -47.28228 | 2025-09-11 04:21:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7f7db5be-13dd-38a7-85f5-c419840620d3 | -8.2365 | -47.86709 | 2025-09-11 04:21:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e53fc5ec-ea40-3f66-9d75-8d1b555bc70f | -5.24858 | -45.9726 | 2025-09-11 04:21:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c7f830ce-019c-355a-93e1-e06af7d60085 | -6.73566 | -43.39257 | 2025-09-11 04:21:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 3b4b7da2-69b0-3ec3-905d-2ee9cd463861 | -7.70445 | -44.75782 | 2025-09-11 04:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c84631dd-a810-3d0d-bd80-06ab3d5ec039 | -5.40125 | -45.9365 | 2025-09-11 04:21:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4d68500d-9bd9-32c4-ba13-6be98978c18c | -7.18388 | -44.96818 | 2025-09-11 04:21:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e56fbd41-e3d1-39ff-acb2-bf29c10623e7 | -7.14753 | -46.04363 | 2025-09-11 04:21:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 53914529-3d1f-36d0-91a1-108c74497cec | -8.16748 | -46.08571 | 2025-09-11 04:21:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 93e3809c-6b27-396b-a3a3-37622c057174 | -5.5659 | -42.92626 | 2025-09-11 04:21:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| c77e8a81-0536-3b41-ae46-48cdc8db74e3 | -5.78685 | -45.40085 | 2025-09-11 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d1ccb470-c5a0-3ad1-adb2-bb9f9c8c623a | -8.4372 | -49.11413 | 2025-09-11 04:21:00 | NPP-375D | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| af10421b-4b53-3a0f-821d-150caa5646fc | -8.52099 | -45.68904 | 2025-09-11 04:21:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bcae4a21-bf89-3fa5-ba9b-1fec26dbfe05 | -5.28305 | -44.19759 | 2025-09-11 04:21:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 63ed763e-0734-39ce-b236-9b571ceb7227 | -6.1439 | -45.47084 | 2025-09-11 04:21:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 383045d9-f071-3424-99f2-0e39a47a0598 | -6.9078 | -47.90552 | 2025-09-11 04:21:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fd0c0d67-b2bd-3f8c-8440-bb7c69340fdf | -5.54757 | -43.80465 | 2025-09-11 04:21:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c851603f-89e3-3640-af9e-2d4381eb012a | -3.24006 | -50.80219 | 2025-09-11 04:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3fb4af20-2dff-3e7e-b581-58d008cea508 | -5.66339 | -45.32342 | 2025-09-11 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 64127766-ebb7-3b9e-8a78-9254aaeb006b | -8.02245 | -49.04673 | 2025-09-11 04:21:00 | NPP-375D | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 3.3 |
| dd89ddd1-3741-311b-b413-d89b22d96606 | -4.45791 | -55.05156 | 2025-09-11 04:21:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fd7b380d-480b-3158-a900-b2df98f7ba3c | -7.048 | -44.69662 | 2025-09-11 04:21:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 13f8301a-2340-3864-8e3e-ce838c053e2a | -6.41332 | -44.49963 | 2025-09-11 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 10722b90-ab17-3ce9-8f03-ec979b8c1028 | -8.76042 | -47.11209 | 2025-09-11 04:21:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 45c436e9-cb9d-3582-8da1-1d68d6215a06 | -9.0675 | -45.70177 | 2025-09-11 04:21:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5394216d-2c1b-372e-b86b-2ef47e3bc993 | -4.90185 | -45.67664 | 2025-09-11 04:21:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3b11d88c-ded6-38da-a723-4f49e231967d | -6.70573 | -47.76897 | 2025-09-11 04:21:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| da7548b5-b488-3c0c-b0f8-e49c74bcc6e5 | -5.45329 | -44.00015 | 2025-09-11 04:21:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c491ade5-c196-340f-9ed0-5b038e31ea78 | -6.28559 | -42.20163 | 2025-09-11 04:21:00 | NPP-375D | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b3bee4d1-2a0e-324b-adca-e242400d905f | -7.22653 | -43.98346 | 2025-09-11 04:21:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a698b399-b014-3f79-9bbe-34abbe675743 | -7.19941 | -44.97778 | 2025-09-11 04:21:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e319a946-2942-30b7-a954-99255242db86 | -5.56045 | -43.05132 | 2025-09-11 04:21:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c7245316-2454-35d0-803b-6d9c78f2e58c | -5.12887 | -43.08898 | 2025-09-11 04:21:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c4f42559-f421-30aa-9c09-665ba6c42dab | -5.86126 | -44.22438 | 2025-09-11 04:21:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 15f5bcbd-ea64-3e8e-8ba7-5a16e3753182 | -8.47556 | -47.29214 | 2025-09-11 04:21:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 16f4d0c1-d0fb-3bf9-8051-d17efcc59313 | -8.73634 | -47.10818 | 2025-09-11 04:21:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4575cfcb-db7e-3f41-85af-db491dcc571b | -2.81049 | -49.20638 | 2025-09-11 04:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a630843f-d15c-353b-a4f1-05896cf188ae | -6.29876 | -42.21445 | 2025-09-11 04:21:00 | NPP-375D | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| f5f8dc0b-68b0-3b9d-b172-4a47049600f5 | -7.32369 | -44.38379 | 2025-09-11 04:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4969e5e0-8a02-33ee-954a-9d65d5eaa551 | -6.35938 | -43.05347 | 2025-09-11 04:21:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 897c8ef6-d64d-3f07-8220-a53bd2bd2001 | -6.49487 | -45.2644 | 2025-09-11 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bfca481e-6bcc-3e7a-ab42-4512fc544104 | -7.31033 | -44.36016 | 2025-09-11 04:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 723f4a0a-5d67-3456-8d81-58a87fde06b3 | -5.86455 | -44.20351 | 2025-09-11 04:21:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9a241591-f3b4-31e4-845c-2e4c8cd13de8 | -5.73408 | -45.60285 | 2025-09-11 04:21:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 797e36c1-5283-375c-ad6a-8448556149cb | -6.47344 | -44.11694 | 2025-09-11 04:21:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3d41889c-0208-3cd7-a59b-6d61ef0765cc | -4.19832 | -55.13529 | 2025-09-11 04:21:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d9e18259-6990-3b42-8366-82ee0ec7817b | -6.246 | -43.49331 | 2025-09-11 04:21:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| af45afc9-21c1-38e2-bdb3-1c7abe70a1ca | -7.67431 | -50.27706 | 2025-09-11 04:21:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2d689235-f3ce-392f-a6ae-e5e4de80d38a | -6.31435 | -43.40885 | 2025-09-11 04:21:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f800ef46-dbad-375f-8bb1-434531f7fe08 | -8.20411 | -47.13972 | 2025-09-11 04:21:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9b22d03c-9957-347e-8246-bca5e55e93fb | -5.35934 | -43.40435 | 2025-09-11 04:21:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7caf0b99-59f4-3698-a5f0-d9e2717b40fd | -6.31324 | -45.65753 | 2025-09-11 04:21:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6b5054ab-4222-366a-b50b-c87e1a7fb823 | -8.16521 | -46.0999 | 2025-09-11 04:21:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8e87efaf-0ec8-32c4-8d13-69a5cb0c9fa5 | -8.01517 | -48.65378 | 2025-09-11 04:21:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 72ac3602-1bc4-35ec-b819-2bd943b20ba5 | -5.10072 | -46.0687 | 2025-09-11 04:21:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 48f4597d-f7cf-3421-a379-fbb50c326046 | -5.6823 | -45.46378 | 2025-09-11 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7266c2e2-5877-32e2-896c-eef5d44832d5 | -6.36709 | -45.15833 | 2025-09-11 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 49124262-2b58-309a-8fce-5168c95717ef | -3.07921 | -48.82021 | 2025-09-11 04:21:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3527fcef-1ead-3155-bc96-e7cd62c9059a | -5.92009 | -45.81804 | 2025-09-11 04:21:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 27101598-8712-36b5-8873-291467c8b3bc | -8.42607 | -47.26824 | 2025-09-11 04:21:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a20a9a87-a34c-3d20-bb49-759dc6f99eb8 | -7.92468 | -44.86438 | 2025-09-11 04:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 41ff6db8-b411-3935-814a-74119047e132 | -6.39621 | -43.51278 | 2025-09-11 04:21:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 89350557-bca5-3c25-b593-3ec71db8dbad | -7.3836 | -50.88412 | 2025-09-11 04:21:00 | NPP-375D | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8e8e7960-3d09-3cdb-8d49-1fe5be9d548e | -5.90449 | -45.76421 | 2025-09-11 04:21:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 14add1fd-709e-3a45-9fb0-b7057bfe8776 | -6.27612 | -43.38823 | 2025-09-11 04:21:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 288cb392-04fa-3c6b-a884-539ecc2d937b | -5.56191 | -42.90701 | 2025-09-11 04:21:00 | NPP-375D | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| e89f621b-8627-3343-aff9-f2c799d0c3d2 | -5.42148 | -45.8543 | 2025-09-11 04:21:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fdcab0e8-5e6f-3993-a4c2-817f48b8eb84 | -6.85901 | -47.85995 | 2025-09-11 04:21:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d0e9cbd4-486d-3104-ab9c-8a77d64bda7a | -7.18831 | -44.96175 | 2025-09-11 04:21:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cea37ace-6225-3ef0-9755-2899b7e34ac6 | -7.83483 | -47.25812 | 2025-09-11 04:21:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1f6f4c39-ca47-3d7b-9d2f-3ca25e32410d | -5.3824 | -46.13952 | 2025-09-11 04:21:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 577563a6-ba33-37f4-805b-379131fa74ed | -6.64265 | -44.07508 | 2025-09-11 04:21:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eef35df2-962d-35dd-905e-df19890bff8a | -5.2836 | -44.19413 | 2025-09-11 04:21:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 99be901e-b134-3cf9-9cb4-bd5303f4f5d7 | -7.86243 | -45.50857 | 2025-09-11 04:21:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 488af6f3-73bb-36a3-9451-6d508fb5f2b5 | -4.58384 | -45.6114 | 2025-09-11 04:21:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2a93972e-4fd1-3818-977e-1c0f4a01b2ce | -8.42133 | -47.27535 | 2025-09-11 04:21:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README54.md)

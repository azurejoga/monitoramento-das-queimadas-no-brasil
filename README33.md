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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6e4fccf3-ba57-3ced-ac90-d97faceef9e9 | -7.1389 | -42.1051 | 2026-09-09 14:50:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 183.2 |
| f21fb533-368f-3353-9080-19c233de0b66 | -9.7321 | -43.4639 | 2026-09-09 15:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 133.0 |
| 035f3093-f3e1-3645-bccb-d31b6e4a2de3 | -13.2917 | -61.109 | 2026-09-09 15:00:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 7156f6c2-91c8-3452-b180-c27332fd3b2c | -10.2372 | -45.2087 | 2026-09-09 15:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 2f813486-0257-3412-a1b2-f8b6fecc941c | -9.7702 | -43.4589 | 2026-09-09 15:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 150.1 |
| 184f8edf-07fa-3a04-98f4-4918a186c164 | -8.7253 | -62.4177 | 2026-09-09 15:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 64.8 |
| decd3caf-2b43-3207-a467-84bbcc314afc | -10.8047 | -60.7837 | 2026-09-09 15:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 52.1 |
| a44bd0c3-867a-306c-b83a-7e9892d8c217 | -8.6198 | -47.3672 | 2026-09-09 15:00:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 86b5b9c5-7239-31fd-bc1b-83b72191728f | -9.7138 | -43.4192 | 2026-09-09 15:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 320.4 |
| 83855182-b0ec-3a81-8575-8a295ad8f31a | -10.2559 | -45.2292 | 2026-09-09 15:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 111.2 |
| 08c0fe0c-f412-3d10-8497-2fcf2d1b6671 | -3.0254 | -57.8738 | 2026-09-09 15:00:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 73.0 |
| cbb4bb7d-fe22-3376-b6f2-4691dfe53b89 | -6.852 | -46.0141 | 2026-09-09 15:00:00 | GOES-19 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 76.9 |
| c108a480-bffb-3fe5-910f-66084cec3d31 | -9.7134 | -43.4428 | 2026-09-09 15:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 163.7 |
| d6bc0ddc-8b46-3d21-80a0-99c8d55fb15d | -13.2725 | -61.1299 | 2026-09-09 15:00:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 57.2 |
| cfbb3428-2fc6-30bd-b117-a0006d11c5dd | -13.3298 | -61.1064 | 2026-09-09 15:00:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 58984457-affb-3913-a5f1-32ff3ac7405c | -10.2559 | -45.2292 | 2026-09-09 15:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 120.1 |
| ffb9e617-9d39-34d2-851f-7ba492a3f4a3 | -9.7134 | -43.4428 | 2026-09-09 15:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 167.9 |
| f1942603-e729-346f-9935-194ac3feca8d | -9.7702 | -43.4589 | 2026-09-09 15:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 182.8 |
| 38f3f9ab-738e-396b-9319-2e2a8962420c | -10.2372 | -45.2087 | 2026-09-09 15:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 96.8 |
| d81ffa4c-c330-3abb-988e-248f80be49a1 | -7.5383 | -45.0047 | 2026-09-09 15:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 109.1 |
| e57410f4-1346-3c68-a39b-a299b1837a32 | -8.7253 | -62.4177 | 2026-09-09 15:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 8fd9e620-3a06-3ead-a002-a7d3dfc07f55 | -9.7698 | -43.4825 | 2026-09-09 15:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 152.8 |
| c586280b-94d6-39aa-807f-254158f14ec7 | -9.7131 | -43.4664 | 2026-09-09 15:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 156.0 |
| eac64d9b-44c2-361f-a58a-a6ffd80ed33d | -6.7123 | -58.9412 | 2026-09-09 15:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.0 |
| d74f50b3-1151-34ad-87e3-63198153505a | -8.7254 | -62.3987 | 2026-09-09 15:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 47.8 |
| f3d5b214-ca59-3006-bb45-29dd74167b7e | -8.6198 | -47.3672 | 2026-09-09 15:10:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 5822a2af-69c2-3e6d-994f-763f51bcd1e7 | -2.4653 | -54.9001 | 2026-09-09 15:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 6c0008ce-87cf-3eb6-8a96-2c9897476744 | -9.7138 | -43.4192 | 2026-09-09 15:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 235.4 |
| 7e75d7f9-b4f0-3a57-998e-1cb41cc83d52 | -9.7845 | -59.7974 | 2026-09-09 15:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 0beb15fe-fd8a-38c7-8845-8629520f1cdf | -9.371 | -66.6752 | 2026-09-09 15:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 68.0 |
| cb331e23-8484-3ab0-a810-edd83e1e81a1 | -10.7578 | -45.9624 | 2026-09-09 15:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 106.8 |
| 8e75cde2-9e6f-3fd7-b03d-7ac18c5902db | -10.701 | -45.9471 | 2026-09-09 15:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 188.6 |
| e8774bef-d573-3f8b-829e-9b8d26ce9c60 | -3.0254 | -57.8738 | 2026-09-09 15:20:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 64.7 |
| eb48b81f-839b-3402-b34d-62208ab2be70 | -10.2559 | -45.2292 | 2026-09-09 15:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 154.8 |
| 2215db83-2398-3e5f-8580-d4bbf8933d43 | -8.7066 | -62.4374 | 2026-09-09 15:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 60.4 |
| c6faf143-f409-31f3-a4d9-0ced521f36ef | -9.7131 | -43.4664 | 2026-09-09 15:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 182.5 |
| 9f5e775c-11cb-306a-a9fa-24664ce16ef4 | -10.2372 | -45.2087 | 2026-09-09 15:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 182.4 |
| 882e5e55-da21-3253-b024-a916c664c5e7 | -10.6819 | -45.9496 | 2026-09-09 15:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 74.2 |
| b4851b76-5d4b-3233-b73c-29c0bfc04eb1 | -3.2546 | -50.0747 | 2026-09-09 15:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 73.6 |
| fc518435-0bf4-3918-9f70-24777a09550b | -9.7698 | -43.4825 | 2026-09-09 15:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 199.2 |
| fb8bedbd-a577-3607-891d-7a550a7572aa | -8.7439 | -62.3979 | 2026-09-09 15:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 49.3 |
| cd0c0e7b-a11e-3b42-b4b3-0b55497dd2b7 | -8.3904 | -62.6774 | 2026-09-09 15:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 47.5 |
| bd693916-6aa6-3ad6-917a-9724c0bced48 | -9.7138 | -43.4192 | 2026-09-09 15:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 244.7 |
| b0d6510b-9724-30e1-ab4d-c4b81ccbeb2c | -8.7254 | -62.3987 | 2026-09-09 15:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 10feaa6e-6444-3224-8692-dff6e7940712 | -2.4653 | -54.9001 | 2026-09-09 15:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| d33a75b8-4713-3ec7-81fb-fd1ef7425fb9 | -10.7391 | -45.9422 | 2026-09-09 15:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 138.8 |
| a7fa98e3-1d2e-3e79-b9b5-2adcdbf007ce | -9.7134 | -43.4428 | 2026-09-09 15:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 229.6 |
| ebe9a5a0-8b8d-3258-89b6-55be25707e6f | -9.7332 | -43.3932 | 2026-09-09 15:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 131.0 |
| 25d71c8c-977b-30f0-8903-1f2abe76d2b5 | -8.7253 | -62.4177 | 2026-09-09 15:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 11dedaaf-7c73-3114-a078-407dd69b9bcb | -9.17695 | -37.2225 | 2026-09-09 15:22:00 | NPP-375 | ITAÍBA | PERNAMBUCO | Brasil | 2607505 | 26 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 5165ba99-083b-3797-bc5b-8627f06a6ac4 | -6.74473 | -37.53878 | 2026-09-09 15:22:00 | NPP-375 | SÃO JOSÉ DE ESPINHARAS | PARAÍBA | Brasil | 2514404 | 25 | 33 | nan | nan | nan | Caatinga | 11.3 |
| fbc3acd6-8160-374e-bb89-0ce8d47ee23a | -6.74754 | -37.53759 | 2026-09-09 15:22:00 | NPP-375 | SÃO JOSÉ DE ESPINHARAS | PARAÍBA | Brasil | 2514404 | 25 | 33 | nan | nan | nan | Caatinga | 9.7 |
| edb66967-be56-3cb6-b4c6-828c2c5da654 | -5.10686 | -37.36478 | 2026-09-09 15:22:00 | NPP-375 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 40731a8a-2970-3ba0-ae7f-708a4d244d61 | -9.01567 | -37.45417 | 2026-09-09 15:22:00 | NPP-375 | CANAPI | ALAGOAS | Brasil | 2701605 | 27 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 4206590a-832d-369e-9b53-88118b9a8f9a | -6.89913 | -38.58661 | 2026-09-09 15:22:00 | NPP-375 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 54.7 |
| c310612a-885a-32c0-bfc8-bdd1438c5592 | -6.896 | -38.59208 | 2026-09-09 15:22:00 | NPP-375 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 92.5 |
| 8a3f0661-98ae-3878-909a-46e133ec88b5 | -6.4734 | -38.42698 | 2026-09-09 15:22:00 | NPP-375 | UIRAÚNA | PARAÍBA | Brasil | 2516904 | 25 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 1ace508e-df6b-3405-bd99-625e75507c41 | -6.89997 | -38.59327 | 2026-09-09 15:22:00 | NPP-375 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 34.6 |
| ab67f43c-c2bf-3d24-ad83-48ada8e0da55 | -8.82438 | -37.06461 | 2026-09-09 15:22:00 | NPP-375 | BUÍQUE | PERNAMBUCO | Brasil | 2602803 | 26 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 3b89d6bc-0e33-3e2e-9391-d87e41804755 | -6.89293 | -38.59433 | 2026-09-09 15:22:00 | NPP-375 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 34.6 |
| 2e550931-7f37-386a-b02b-338f4e52ddd6 | -6.46791 | -38.42711 | 2026-09-09 15:22:00 | NPP-375 | UIRAÚNA | PARAÍBA | Brasil | 2516904 | 25 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 6e755599-6a46-3823-b230-16f90bc28290 | -6.46648 | -38.42813 | 2026-09-09 15:22:00 | NPP-375 | UIRAÚNA | PARAÍBA | Brasil | 2516904 | 25 | 33 | nan | nan | nan | Caatinga | 5.4 |
| e66bb4a7-4a42-3e7d-ba65-9672ae8dc933 | -9.7134 | -43.4428 | 2026-09-09 15:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 151.4 |
| 9ee2dfb5-6346-379a-8039-7d6fabc1dd93 | -9.7138 | -43.4192 | 2026-09-09 15:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 233.0 |
| fd49a5a4-4b9b-39bc-a46c-4e2011a31be7 | -9.3711 | -66.6566 | 2026-09-09 15:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 49.8 |
| ace1f507-a693-31ea-a045-5e7a6d1d9ea0 | -10.7006 | -45.9698 | 2026-09-09 15:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 293.2 |
| d12bad87-f794-3656-9dd8-ca12ab029402 | -3.0254 | -57.8738 | 2026-09-09 15:30:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 107.6 |
| 509143d0-435b-3263-b19b-1bc7940115d9 | -8.7253 | -62.4177 | 2026-09-09 15:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 86.9 |
| 91d832ec-46d2-331d-89ab-41e88d44f944 | -10.6819 | -45.9496 | 2026-09-09 15:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 97.0 |
| ee4a3ef5-878b-312e-ae6c-7fb87f738b52 | -10.2563 | -45.2062 | 2026-09-09 15:30:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 115.4 |
| d8ad7ccc-938b-3c48-b5b3-207120512611 | -9.371 | -66.6752 | 2026-09-09 15:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 9a09c6f3-7038-30e7-8eef-92f4252be067 | -10.7391 | -45.9422 | 2026-09-09 15:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 149.2 |
| f74dab58-f237-3dd9-96d1-e42e8868a1f5 | -10.6816 | -45.9723 | 2026-09-09 15:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 196.4 |
| ea062d29-6e9c-31e3-9b20-ab806d00ae95 | -6.7123 | -58.9412 | 2026-09-09 15:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 25a114f5-64b7-3161-a60d-503d1f70cebf | -6.7861 | -58.9382 | 2026-09-09 15:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.7 |
| eb1121bb-0689-3d0c-af30-1242122fe0ce | -10.2559 | -45.2292 | 2026-09-09 15:30:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 214.8 |
| ee0adaa4-f3a1-3779-9648-b2746c6bfb69 | -10.701 | -45.9471 | 2026-09-09 15:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 166.6 |
| a9095671-f4f1-3f24-9acc-1d5c5e035d33 | -10.2372 | -45.2087 | 2026-09-09 15:30:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 145.4 |
| 7c117c85-ddc0-36cc-b86d-d266ccc4f677 | -6.6357 | -59.4459 | 2026-09-09 15:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 91.2 |
| c2791214-46a1-36fe-9990-f6c02a60ebfb | -8.6198 | -47.3672 | 2026-09-09 15:30:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 73.6 |
| bb563da3-9ae0-37b6-a81f-2e2609f654da | -9.2177 | -60.8881 | 2026-09-09 15:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 91.3 |
| d9d43f30-2669-3e2e-b737-656e137f1a51 | -9.3711 | -66.6566 | 2026-09-09 15:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 87.6 |
| ef479ca6-aa13-337e-8165-ede9965179e5 | -6.5302 | -58.5227 | 2026-09-09 15:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 966528db-f8bb-359c-95d0-e64285b600b7 | -6.9701 | -59.0272 | 2026-09-09 15:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 83.4 |
| 2abb1e7c-bf91-348e-9a76-e50a1eb91291 | -8.7253 | -62.4177 | 2026-09-09 15:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 92.6 |
| 1d3ef87d-cc31-3afd-9e68-baa05a7c36a5 | -6.7861 | -58.9382 | 2026-09-09 15:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 84.0 |
| ffe25123-d0d9-3b91-b4bf-36c1742d3984 | -10.7391 | -45.9422 | 2026-09-09 15:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 156.8 |
| 2a8cb68b-8f14-3cd1-99be-f937d83d8424 | -8.3904 | -62.6774 | 2026-09-09 15:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 38df996a-b7ca-374f-bcd9-caf73de4736c | -10.2372 | -45.2087 | 2026-09-09 15:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 102.1 |
| 5246a0d4-4895-38d9-a83a-65d9cc3d10d5 | -9.371 | -66.6752 | 2026-09-09 15:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 133.7 |
| 701118e6-81c6-3c8a-938d-ecbf66990049 | -10.2559 | -45.2292 | 2026-09-09 15:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 150.4 |
| 9d6d954f-0680-3ca2-b35d-58a49a9bc217 | -10.701 | -45.9471 | 2026-09-09 15:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 138.6 |
| 5c9ff77b-2106-3356-83a7-8b8ae013f10e | -3.0254 | -57.8738 | 2026-09-09 15:40:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 8d841307-765a-3eb0-b3e6-7c37b626581b | -2.0585 | -56.4284 | 2026-09-09 15:40:00 | GOES-19 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| c3273824-5b73-3f06-a870-71c961c0dbd0 | -1.4935 | -54.8354 | 2026-09-09 15:50:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| ee5ee19f-70be-343a-b7b0-dd10dafdd2df | -10.7387 | -45.9649 | 2026-09-09 15:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 222.2 |
| 3cd12bfb-3fa3-39fb-a2c7-ec50f8869eab | -10.6816 | -45.9723 | 2026-09-09 15:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 186.4 |
| 792fd6af-e43f-3607-9979-4b8dc7cf1788 | -10.7391 | -45.9422 | 2026-09-09 15:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 527.6 |
| 028dd95a-adaa-3b99-929f-9d851ca806e9 | -9.3711 | -66.6566 | 2026-09-09 15:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 99.3 |
| 96a6e125-4ef0-3869-ba7e-677e46d7f7bb | -6.7676 | -58.939 | 2026-09-09 15:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 74.7 |


[Clique aqui para ver as próximas entradas](README34.md)

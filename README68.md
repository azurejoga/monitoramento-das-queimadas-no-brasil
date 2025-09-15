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

## Dados Diários - Página 68

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3ea65f0b-1a26-314f-8fa8-62a67db275c0 | -7.8942 | -43.5857 | 2025-09-15 11:30:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 221.4 |
| 0e933504-f64b-3c1d-85e0-53672263e4e5 | -7.8753 | -43.5876 | 2025-09-15 11:30:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 352.3 |
| 06bafddc-c7e5-31fd-a668-120086fe9e42 | -10.075 | -47.1908 | 2025-09-15 11:30:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 5f26faec-73fa-3209-a7a3-dcd03d1b4630 | -8.9793 | -45.7665 | 2025-09-15 11:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 818e7bd3-6e0d-3522-ab94-1da1fd4aa1d2 | -12.6533 | -47.9507 | 2025-09-15 11:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 115.5 |
| 0cda516f-b1ba-3e47-bbbc-586172f10a30 | -9.9385 | -50.3158 | 2025-09-15 11:30:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 84.9 |
| 61a01bbe-06ac-3b9d-91fa-44b49c7ec41c | -6.6885 | -45.5103 | 2025-09-15 11:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 9a856018-2cc1-31a9-afcd-f8953d17e9da | -12.6533 | -47.9507 | 2025-09-15 11:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 260.3 |
| 3f4ebe90-9e86-3c53-b6b4-8fe444eef717 | -12.6537 | -47.9285 | 2025-09-15 11:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 135.6 |
| 46bcf749-65b3-3ecf-8803-0f6d7b524da4 | -7.8945 | -43.5623 | 2025-09-15 11:40:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 408.5 |
| 126b8d42-883c-3238-9e0c-09f16cc95416 | -7.8753 | -43.5876 | 2025-09-15 11:40:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 336.2 |
| cfc0fffd-dad7-39f5-9422-de693b167c84 | -12.6341 | -47.9534 | 2025-09-15 11:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 97e67934-a742-3ec2-b6f1-8413e47e1ca8 | -7.8942 | -43.5857 | 2025-09-15 11:40:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 159.9 |
| 645056ee-a324-373f-baeb-5f8f285a049c | -6.9798 | -44.5529 | 2025-09-15 11:40:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 122.7 |
| b4f5df80-481d-33a5-9d4c-35813f2dfbae | -7.8756 | -43.5643 | 2025-09-15 11:40:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 900.9 |
| 41622a84-731e-3916-8016-ab8107e1fede | -6.98 | -44.5299 | 2025-09-15 11:40:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 88ff90a8-a3bd-3f17-b546-3b03415a6372 | -6.6885 | -45.5103 | 2025-09-15 11:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 147.3 |
| f01803c4-d60f-319f-8ffd-fbcb09002b25 | -9.2235 | -44.5052 | 2025-09-15 11:50:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 129.6 |
| 2bb6f13f-6a8b-3af6-b30d-ac4daff81646 | -8.651 | -46.3637 | 2025-09-15 11:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 172.0 |
| c4d33af4-c2a3-309a-93e3-d55a36e583a0 | -10.075 | -47.1908 | 2025-09-15 11:50:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 104.3 |
| d67288f4-158d-30ee-82f9-8e7bdfcc8a86 | -7.8756 | -43.5643 | 2025-09-15 11:50:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 711.8 |
| 70a9793c-a783-3438-b783-23cf62740384 | -8.6507 | -46.3862 | 2025-09-15 11:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 131.6 |
| 8a795f74-a785-39e4-9391-9c7beedb3ecb | -6.9798 | -44.5529 | 2025-09-15 11:50:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 99.0 |
| 9aa554b8-433c-308e-906b-ae0e35380698 | -8.9784 | -45.8344 | 2025-09-15 11:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 93.7 |
| abf8191b-3c4e-3b9d-8738-c796c3957dce | -12.6533 | -47.9507 | 2025-09-15 11:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 105.0 |
| 2868a0d0-7999-3691-9073-fcda7b16113f | -7.8753 | -43.5876 | 2025-09-15 11:50:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 365.5 |
| 610a0d96-ec7a-3a56-b96d-92f246a48564 | -7.8942 | -43.5857 | 2025-09-15 11:50:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 188.7 |
| be570a1c-0b7f-376e-bd4e-8450077900cd | -7.8945 | -43.5623 | 2025-09-15 11:50:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 367.7 |
| 6742bfd9-897f-34d6-a4f9-e3222d77ede6 | -6.1693 | -41.1872 | 2025-09-15 11:50:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 93.2 |
| 9a53ca2c-9ef5-3610-aed7-0a239381d6c8 | -6.98 | -44.5299 | 2025-09-15 11:50:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 92.7 |
| b1d6904d-fa30-33c1-9e3c-776d9049074f | -12.7879 | -47.9318 | 2025-09-15 12:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 114.1 |
| 1e5c909b-96a8-3fb3-b059-bcd2638eb64f | -9.5531 | -48.0428 | 2025-09-15 12:00:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 129.0 |
| 4c5a9c37-7353-3f4f-8d26-efc7aaed6e02 | -8.651 | -46.3637 | 2025-09-15 12:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 77.8 |
| d577a5e1-1193-383a-995b-a58c08914f8e | -7.8942 | -43.5857 | 2025-09-15 12:00:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 173.8 |
| f3512756-c7b6-361a-b61d-ae6158fe400e | -12.5975 | -45.7251 | 2025-09-15 12:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 158.8 |
| d7f0fe5e-89ab-3306-be20-23cd2e5e4e29 | -8.9568 | -46.0398 | 2025-09-15 12:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 85.4 |
| cf0720ab-83a8-32a3-87df-0af2d924ebad | -6.1693 | -41.1872 | 2025-09-15 12:00:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 110.1 |
| 0ab30240-5683-3c13-9fc4-bece8e3b251d | -8.9787 | -45.8118 | 2025-09-15 12:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 70.7 |
| b45e5add-ec50-3f9d-aacd-f92b973ef9a9 | -7.8756 | -43.5643 | 2025-09-15 12:00:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 362.7 |
| cf374a00-21d0-3c12-b949-447aa5bb648a | -8.6136 | -46.3452 | 2025-09-15 12:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 12162ae5-cb14-3e71-9dda-e8b9c20872bd | -10.9137 | -48.1759 | 2025-09-15 12:00:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 59fce2c8-0eca-3098-9e6f-879f34994574 | -7.8753 | -43.5876 | 2025-09-15 12:00:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 208.5 |
| 17c511e9-07f1-34c2-9316-a5e3a45611ea | -6.9798 | -44.5529 | 2025-09-15 12:00:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 124.4 |
| b596a32c-3ff1-38b9-bf4f-1d8b99fea8ce | -7.8945 | -43.5623 | 2025-09-15 12:00:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 199.0 |
| cea23722-0be1-32c5-9e53-791758034caa | -8.9734 | -46.218 | 2025-09-15 12:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 8fdc792a-4c47-3cb6-b739-f6e5fd37b830 | -8.9784 | -45.8344 | 2025-09-15 12:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 105.9 |
| 95f607c4-de4d-3da0-a387-ae4037fd33ed | -12.6533 | -47.9507 | 2025-09-15 12:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 95.1 |
| bab54d59-651b-3e0c-89f9-a94b4c4d352e | -6.169 | -41.2114 | 2025-09-15 12:00:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 86.0 |
| 65c45b4a-cdf5-385b-a7cc-14309fc6acd1 | -6.98 | -44.5299 | 2025-09-15 12:00:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 88.8 |
| bd1db648-3e3d-3bc3-9d4e-da4e5a1af820 | -7.8942 | -43.5857 | 2025-09-15 12:10:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 258.4 |
| 3812796f-d1c7-3cef-8ee3-3de184e8ca52 | -12.6537 | -47.9285 | 2025-09-15 12:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 117.5 |
| f429436c-833c-3c04-8661-41f9d625737a | -10.9137 | -48.1759 | 2025-09-15 12:10:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 146.0 |
| 67b446d3-8637-3beb-b59e-d422d23ffdac | -8.9412 | -45.7933 | 2025-09-15 12:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 225a5da9-9bcf-3417-bd82-3719dcfb25e4 | -16.673 | -49.7615 | 2025-09-15 12:10:00 | GOES-19 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 79.6 |
| d3c05043-2220-3309-92d1-ea851d941241 | -8.9784 | -45.8344 | 2025-09-15 12:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 80.0 |
| e9157cea-6975-3fc1-bd62-987b052a59eb | -12.8404 | -47.1417 | 2025-09-15 12:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 76.9 |
| ba7d6a37-c6ab-390e-a9bb-38ae7b294525 | -8.9568 | -46.0398 | 2025-09-15 12:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 72.4 |
| e01c3dc2-0c0f-33f4-998f-d442bc8dec0f | -8.5944 | -46.3695 | 2025-09-15 12:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 35525c59-a977-30b7-bef5-5a7893310ccb | -16.6725 | -49.7838 | 2025-09-15 12:10:00 | GOES-19 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 74.5 |
| e80e96bd-85da-3574-9ca5-6df3a35ea641 | -6.1693 | -41.1872 | 2025-09-15 12:10:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 102.3 |
| d30356fc-2efe-32c6-8aef-a2464956838d | -6.98 | -44.5299 | 2025-09-15 12:10:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 030b2b3d-2633-3128-8f4d-cadb2290d29e | -6.961 | -44.5546 | 2025-09-15 12:10:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 81.4 |
| c45cc42d-1fdc-3ceb-bf7d-fdca2192c360 | -8.5947 | -46.3471 | 2025-09-15 12:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 8297606f-72b6-345d-b9fa-35f7ac243b84 | -12.6533 | -47.9507 | 2025-09-15 12:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 173.8 |
| f8a3077a-eeda-3a65-b7f0-7527c18f717d | -12.6341 | -47.9534 | 2025-09-15 12:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 373d405c-40a5-35ac-9d01-b4853563f1c3 | -8.9545 | -46.22 | 2025-09-15 12:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 7438c51a-13ad-3098-b411-3bbcb4d082cc | -8.9601 | -45.7912 | 2025-09-15 12:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 1298e581-fcd8-3f0a-96a6-7e2e249a34ef | -7.8756 | -43.5643 | 2025-09-15 12:10:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 194.3 |
| f1124ea1-4941-3dc7-b859-746678e1eef2 | -10.0754 | -47.1686 | 2025-09-15 12:10:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 0880c195-5eae-345e-b20d-bbc53de63600 | -8.9734 | -46.218 | 2025-09-15 12:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 64.2 |
| fd615887-da15-3d2e-b193-0ce98639c71e | -7.8753 | -43.5876 | 2025-09-15 12:10:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 143.8 |
| 9eaf2d37-9960-363d-888a-9e951ddd7fd6 | -10.935 | -45.5978 | 2025-09-15 12:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 69.7 |
| ea8f7656-59b6-3147-a506-b075107271a3 | -7.8945 | -43.5623 | 2025-09-15 12:10:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 178.6 |
| 42e7cf05-8e95-3eaf-9100-f2b0742b2ec4 | -8.651 | -46.3637 | 2025-09-15 12:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 5b2f245a-e8bc-32a2-adfb-9800e87686d1 | -6.9798 | -44.5529 | 2025-09-15 12:10:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 1b7b1ef4-1369-3b09-bc0b-62b3c8da65d0 | -12.7879 | -47.9318 | 2025-09-15 12:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 74.6 |
| f4bc61c4-fd73-3621-b5e2-73a7bd1b291e | -6.169 | -41.2114 | 2025-09-15 12:10:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 81.9 |
| 73f651d0-23af-3135-8168-ecc8ef564472 | -10.075 | -47.1908 | 2025-09-15 12:10:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 85.4 |
| fc876a40-e9c0-34e7-b3ad-a3527d7ad4d9 | -7.8942 | -43.5857 | 2025-09-15 12:20:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 160.8 |
| 8a22a516-e47b-3814-9efd-46b123e240f5 | -10.9137 | -48.1759 | 2025-09-15 12:20:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 117.7 |
| c57aaa05-2039-3808-84dd-9dbb083b22ca | -8.9545 | -46.22 | 2025-09-15 12:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 229.9 |
| 8309ff2e-2db1-3277-852b-934fc9371049 | -6.9798 | -44.5529 | 2025-09-15 12:20:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 113.4 |
| b1ca518d-2a31-3351-b287-f7bafb6ee9d0 | -12.7879 | -47.9318 | 2025-09-15 12:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 91.0 |
| d8a4d71d-edc5-363c-8722-368b1cfcd359 | -8.651 | -46.3637 | 2025-09-15 12:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 86.1 |
| d2cc7562-365e-3e50-9d3e-4df17027e647 | -12.6533 | -47.9507 | 2025-09-15 12:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 137.7 |
| 7f66f1a3-3a96-3880-8039-20d6716841f2 | -10.8947 | -48.1782 | 2025-09-15 12:20:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 61.7 |
| a33fd8ad-ccc6-3b5e-b521-eeded83b8231 | -6.1881 | -41.1855 | 2025-09-15 12:20:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 75.0 |
| 42628005-be88-3e37-9050-62af281d7f80 | -6.98 | -44.5299 | 2025-09-15 12:20:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 83.7 |
| b5edfc9e-f129-36f7-bfb3-c320c6c0e6b6 | -8.9734 | -46.218 | 2025-09-15 12:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 315.1 |
| 542a7b61-a3d4-3aff-8072-46a01662512f | -6.169 | -41.2114 | 2025-09-15 12:20:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 104.6 |
| e79f61d6-29cc-3a52-98b3-2d5af6c1f5b6 | -6.1693 | -41.1872 | 2025-09-15 12:20:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 129.3 |
| 2b4a054e-930b-3bb9-8164-305c4c67b834 | -10.8944 | -48.2002 | 2025-09-15 12:20:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 90.2 |
| de99579c-ac9f-34aa-aef9-ae653ae09771 | -7.8945 | -43.5623 | 2025-09-15 12:20:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 119.8 |
| 7b448342-84d6-3f13-8b6b-f100e3a0c003 | -7.8753 | -43.5876 | 2025-09-15 12:20:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 142.2 |
| 03bea830-83aa-34a8-8229-6de0e17594d0 | -8.9737 | -46.1955 | 2025-09-15 12:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 9fddfbdc-7a0f-3cad-9348-42161936c808 | -12.6537 | -47.9285 | 2025-09-15 12:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 90.2 |
| b4e3e032-1ec5-393f-8e51-e0a2573f0962 | -20.9096 | -46.4681 | 2025-09-15 12:20:00 | GOES-19 | ALPINÓPOLIS | MINAS GERAIS | Brasil | 3101904 | 31 | 33 | nan | nan | nan | Mata Atlântica | 116.2 |
| 899238fc-df3b-337f-8935-5e1a36980479 | -8.8981 | -46.2035 | 2025-09-15 12:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 6f0cbc67-cba3-3941-8600-a7261d1b606a | -7.8756 | -43.5643 | 2025-09-15 12:20:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 157.4 |
| 7a1da74f-ee4d-3831-894f-c8ff0993a530 | -12.8404 | -47.1417 | 2025-09-15 12:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 82.2 |


[Clique aqui para ver as próximas entradas](README69.md)

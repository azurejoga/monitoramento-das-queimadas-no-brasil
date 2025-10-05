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

## Dados Diários - Página 160

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 781fe45f-41ff-38af-ba58-8ba4145d039b | -8.5581 | -46.2611 | 2025-10-05 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 105.7 |
| ff04c3c1-f7ba-3be1-a488-ffcedc8151a8 | -17.9605 | -57.5904 | 2025-10-05 13:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 120.9 |
| ee39b31f-ba0b-3998-8e1a-649816134f15 | -15.1352 | -45.7337 | 2025-10-05 13:40:00 | GOES-19 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 154.9 |
| eaf49814-9b5b-3174-86fc-bc68d48df8cc | -6.7052 | -43.8859 | 2025-10-05 13:40:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 71.1 |
| aa5fffb9-6fa9-3799-a826-bb0eeeba1252 | -14.7517 | -54.6565 | 2025-10-05 13:40:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 3c22f983-e2df-3f4c-a1aa-9aeb8bfdf322 | -7.5078 | -41.2719 | 2025-10-05 13:40:00 | GOES-19 | JAICÓS | PIAUÍ | Brasil | 2205201 | 22 | 33 | nan | nan | nan | Caatinga | 143.7 |
| 663fc74f-4877-3795-b581-1076e70350d8 | -13.7284 | -51.2908 | 2025-10-05 13:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 142.5 |
| 00ff8fce-b8a9-35b2-a40f-a631fe5e565f | -7.5267 | -41.2699 | 2025-10-05 13:40:00 | GOES-19 | JAICÓS | PIAUÍ | Brasil | 2205201 | 22 | 33 | nan | nan | nan | Caatinga | 119.0 |
| 4e397900-4ebb-3bf1-bb1e-ebd839f4f364 | -6.6546 | -41.601 | 2025-10-05 13:50:00 | GOES-19 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 130.2 |
| 16984cf6-45c6-366d-b80e-e8ad52e2bd71 | -7.7885 | -44.5228 | 2025-10-05 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 91.1 |
| e30217a1-d5da-3582-90ec-2a50f5627505 | -11.8225 | -45.0827 | 2025-10-05 13:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 207.5 |
| 79c95e9e-f491-3228-a15a-488fb348d9a8 | -7.4276 | -46.5239 | 2025-10-05 13:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 80.7 |
| c63dcc9e-8572-31a6-aea8-d3e8b10f6dc2 | -12.4673 | -45.4925 | 2025-10-05 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 113.8 |
| 6f9f708c-67c5-3d1f-8fe6-b45bb78f5e09 | -7.6993 | -42.5708 | 2025-10-05 13:50:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 93.9 |
| b8a9492a-ee44-3f53-8232-483274aace37 | -17.9404 | -57.6134 | 2025-10-05 13:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 49.1 |
| 02dbc939-237d-3823-98f2-5e8d3899fbc2 | -11.0975 | -49.8729 | 2025-10-05 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 75.1 |
| e6c672f1-ec8d-3068-ae8f-8ff407acd91f | -7.2416 | -42.9957 | 2025-10-05 13:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 106.6 |
| 0d3762ef-3aa7-3e8a-acb0-0cac402d590c | -15.9084 | -48.8254 | 2025-10-05 13:50:00 | GOES-19 | CORUMBÁ DE GOIÁS | GOIÁS | Brasil | 5205802 | 52 | 33 | nan | nan | nan | Cerrado | 109.3 |
| 7b865a56-6a11-3346-bc8d-d6d01d0df005 | -11.8221 | -45.1059 | 2025-10-05 13:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 84.8 |
| a38c2574-259b-3add-aa0f-01afd2b368ff | -7.6622 | -47.367 | 2025-10-05 13:50:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 55.3 |
| fb386336-39cf-3adb-b1cf-42155ad2f60f | -14.9357 | -46.8278 | 2025-10-05 13:50:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 94.0 |
| f14d8c76-b438-351d-8726-76878735ed38 | -11.7912 | -48.0448 | 2025-10-05 13:50:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 105.6 |
| 20e2648b-d95a-3d7a-b09c-0d20d77457f9 | -11.5264 | -46.742 | 2025-10-05 13:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 142.3 |
| de2d414b-bb74-374e-92d0-d5310c29ca51 | -9.6287 | -46.6394 | 2025-10-05 13:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 109.5 |
| cdef721c-f5bb-3a90-92a0-a76e8ca3fddd | -6.6976 | -42.8354 | 2025-10-05 13:50:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 87.0 |
| 044a0356-878c-3463-bb8b-9cf3263b186e | -8.1699 | -44.1608 | 2025-10-05 13:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 117.8 |
| 89adb1f8-9f8b-35b9-b070-5bd1791efbf8 | -7.699 | -42.5946 | 2025-10-05 13:50:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 83.0 |
| 84cbf2c4-23ab-3b0d-8d4f-90ed8028bd1a | -9.283 | -45.6649 | 2025-10-05 13:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 52.9 |
| 036a48a7-72d5-31f6-ab4b-b1287e566d86 | -11.0316 | -46.6946 | 2025-10-05 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 110.1 |
| 6e6a9762-43e9-3c56-86c4-c2fa771b7b06 | -10.0692 | -50.4094 | 2025-10-05 13:50:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 187.9 |
| 81c09612-2083-3fe7-a097-54cd8f4cf797 | -15.6019 | -52.4888 | 2025-10-05 13:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 117.7 |
| 048d43b9-562e-3801-8e3b-1009e834ce2c | -16.0561 | -45.7438 | 2025-10-05 13:50:00 | GOES-19 | URUCUIA | MINAS GERAIS | Brasil | 3170529 | 31 | 33 | nan | nan | nan | Cerrado | 131.3 |
| ca1681f9-9d07-3f8b-9a4b-a9a18f553963 | -10.4557 | -48.3827 | 2025-10-05 13:50:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 5365b6dd-057d-37c5-9ece-ef9388319cdb | -7.7746 | -42.5865 | 2025-10-05 13:50:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 108.1 |
| 6c592c44-a6ff-3f0d-a61e-251f1a3b4c63 | -10.3907 | -50.3557 | 2025-10-05 13:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 123.0 |
| 388d9284-0166-334e-8866-349f09128f86 | -12.3993 | -45.0183 | 2025-10-05 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 111.0 |
| f4e70adb-0608-3d1f-8183-aae6c2440a9f | -10.069 | -50.4307 | 2025-10-05 13:50:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 123.6 |
| c4d76598-f41d-37a1-a13c-29069f956636 | -11.823 | -45.0596 | 2025-10-05 13:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 201.1 |
| c4566464-06f2-3d68-b546-866d62c07dc3 | -8.5953 | -46.3022 | 2025-10-05 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 100.5 |
| 7eb0b2d1-e470-3006-ab70-4af393b2b442 | -6.9858 | -42.3109 | 2025-10-05 13:50:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 77.3 |
| 596de131-5c74-3aa4-b62c-5b0a4cc41109 | -10.8093 | -48.8229 | 2025-10-05 13:50:00 | GOES-19 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 96.3 |
| e73804ce-045a-3264-a6fe-786fb65959c0 | -7.646 | -45.4489 | 2025-10-05 13:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 56.3 |
| fc4fea73-0373-3e02-9d4b-3a36f0eef8dd | -11.7908 | -48.0669 | 2025-10-05 13:50:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 67.9 |
| efd806a0-b5f4-3c27-8ec1-d14d59b9dc71 | -7.0372 | -42.7563 | 2025-10-05 13:50:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 84.0 |
| a524385b-49d9-396c-8f56-2b5998c6a6e8 | -7.7938 | -42.5607 | 2025-10-05 13:50:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 158.9 |
| 1f988f5e-d81f-33a8-89aa-09c3a344b6a1 | -9.2439 | -51.8133 | 2025-10-05 13:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 78.7 |
| e2fc26c6-bd00-3edf-ae23-6529bd557464 | -8.5596 | -47.6813 | 2025-10-05 13:50:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 52.1 |
| 9c7cec00-809d-3578-ad61-44dca4c17aed | -9.2973 | -46.0026 | 2025-10-05 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 95.6 |
| a4e7d634-67f5-3aa4-b092-505f99d20ab2 | -8.5581 | -46.2611 | 2025-10-05 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 132.9 |
| 2f01cc63-127b-3cf0-9fcc-df976e501d34 | -10.1943 | -45.5339 | 2025-10-05 13:50:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 152.2 |
| 78914b05-fdf4-34cb-8f8f-3877d97f9a1f | -6.812 | -39.3987 | 2025-10-05 13:50:00 | GOES-19 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 167.7 |
| def0f0f0-5ab0-3438-b5da-d95306af838f | -8.1891 | -44.1357 | 2025-10-05 13:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 135.1 |
| 5fc8c754-624d-38a8-bb1c-41c7f58f18df | -11.8422 | -45.0567 | 2025-10-05 13:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 137.0 |
| a4afd067-14c1-3029-850d-bea083ee33a0 | -12.3911 | -51.1153 | 2025-10-05 13:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 61f54222-973a-3eb8-b27b-27bac5af72eb | -7.8127 | -42.5587 | 2025-10-05 13:50:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 95.2 |
| 33ec872c-db99-328a-97f8-48dbad143be1 | -10.4463 | -50.4353 | 2025-10-05 13:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 143.5 |
| 3453c82b-f0f4-38c1-913d-08a91810aef5 | -15.582 | -52.5129 | 2025-10-05 13:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 213.5 |
| d93f651b-8a9a-3eca-b87a-53074b25cec8 | -11.8033 | -45.0856 | 2025-10-05 13:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 203.6 |
| c8c504f6-8a0a-39f9-8f68-b02a380f8211 | -18.2565 | -53.3544 | 2025-10-05 13:50:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 5e9d62c2-06f9-303a-8acf-8adfab295a27 | -9.9313 | -50.8898 | 2025-10-05 13:50:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 101.6 |
| 6f04aac0-35a9-3d23-9f73-3647430ca6f8 | -8.5578 | -46.2836 | 2025-10-05 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 0481c6fc-a827-39ff-8896-8f96603bb149 | -6.3982 | -42.6972 | 2025-10-05 13:50:00 | GOES-19 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 113.7 |
| 33e01d73-afb2-34d7-85bd-23853c7f154a | -6.4179 | -44.4633 | 2025-10-05 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 58b3deb0-dae0-3f91-830b-9a0ff17bb1bd | -10.1576 | -45.4473 | 2025-10-05 13:50:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 126.6 |
| 554dc9d1-8909-34b1-82b8-f861d9987c9e | -10.0501 | -50.4326 | 2025-10-05 13:50:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 84.9 |
| 07dc06f2-eeaa-30b7-bf56-f29b2ec07c83 | -10.9497 | -47.0634 | 2025-10-05 13:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 107.8 |
| b1e7807a-1632-33c3-ac0b-f5d6f0fd9290 | -10.158 | -45.4244 | 2025-10-05 13:50:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 138.8 |
| 7906a7ec-bb69-39ee-84f6-b9e7d4f0c2a7 | -21.6882 | -50.0788 | 2025-10-05 13:50:00 | GOES-19 | PROMISSÃO | SÃO PAULO | Brasil | 3541604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 110.5 |
| 2799a6e7-f3d7-38e4-9000-1762e5b83e60 | -13.7473 | -51.3097 | 2025-10-05 13:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 250.2 |
| 33f018e7-4355-3923-a838-cced8488d443 | -7.6463 | -45.4262 | 2025-10-05 13:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 69.9 |
| f9884f64-4388-3fd1-b6b7-b6dc9c93d1d9 | -12.3914 | -51.094 | 2025-10-05 13:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 107.0 |
| 1e69bbed-56f5-3f29-bcb8-8bfb96abf722 | -7.0367 | -42.8036 | 2025-10-05 13:50:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 269.5 |
| ec129ced-34d8-3235-9b96-5ed55cfef6ab | -17.9605 | -57.5904 | 2025-10-05 13:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 122.0 |
| fc0f7db8-3ff2-3941-95be-54397a629ee7 | -8.5407 | -47.6831 | 2025-10-05 13:50:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 1c5042fb-ab6a-33e8-96b6-7e2313db1518 | -7.4669 | -43.0674 | 2025-10-05 13:50:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 102.5 |
| 98a8642d-35a5-3563-8dc4-cde67fcbfa25 | -17.921 | -57.5952 | 2025-10-05 13:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 48.3 |
| 33128980-4c61-3c50-9155-90b4357dc84a | -6.4161 | -44.6466 | 2025-10-05 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 753191a1-8ba2-3ef3-b654-e290dee0882e | -14.7517 | -54.6565 | 2025-10-05 13:50:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 113.3 |
| 8fb8a87a-52ae-32f3-ab00-eb283f308a40 | -7.0369 | -42.78 | 2025-10-05 13:50:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 306.2 |
| c77087b1-99dc-3e11-85ba-6f9935850094 | -17.986 | -51.144 | 2025-10-05 13:50:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 122.5 |
| 77c28235-261c-3def-87d7-55d905736cd6 | -7.4464 | -46.5223 | 2025-10-05 13:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 74a67545-c24b-34ae-9a51-b48aae45bebc | -16.0212 | -50.9425 | 2025-10-05 13:50:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 88.6 |
| de2c724b-5c98-3a71-9607-ad1985513a97 | -13.728 | -51.3122 | 2025-10-05 13:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 253.1 |
| be098c21-2507-3e13-808f-10bf42268474 | -9.9021 | -50.2128 | 2025-10-05 13:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 72.9 |
| fce54be7-e86d-3f44-b863-5a5f468fb4dc | -7.5267 | -41.2699 | 2025-10-05 13:50:00 | GOES-19 | JAICÓS | PIAUÍ | Brasil | 2205201 | 22 | 33 | nan | nan | nan | Caatinga | 107.2 |
| 6e8a0a6a-5f05-3897-99a9-b1de05fa4375 | -9.3276 | -54.5215 | 2025-10-05 13:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 92.5 |
| c919facc-8aee-37e6-964e-8df6df335428 | -9.9207 | -50.2323 | 2025-10-05 13:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 84efbd42-4718-3a12-8368-abce93b39fc7 | -7.2419 | -42.9722 | 2025-10-05 13:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 96.7 |
| 56aaef16-f0a1-37e5-8ce8-6580525f3c6d | -11.0978 | -49.8513 | 2025-10-05 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 90.1 |
| ca3b8296-f422-3833-9de0-d27585593c38 | -17.8417 | -57.6254 | 2025-10-05 13:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 47.0 |
| 5ea0c52a-dd54-3ac7-bd33-a14cf3097a02 | -9.5794 | -46.106 | 2025-10-05 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 189.9 |
| 217f0e70-fb20-3abb-855d-80188aac452b | -17.9612 | -57.5492 | 2025-10-05 13:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 48.8 |
| ab50bd06-e5c1-35e8-9725-92cf1ccce216 | -15.6015 | -52.5102 | 2025-10-05 13:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 219.8 |
| a96cdee8-3e2d-3f02-9263-28d3cb66e68e | -9.9556 | -43.7632 | 2025-10-05 13:50:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 128.3 |
| b57dbf91-f1bf-37d8-940e-4e1e17f1be9e | -18.2569 | -53.3329 | 2025-10-05 13:50:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 94351bc6-dcdd-33cf-8679-e69eed7b1843 | -11.8038 | -45.0624 | 2025-10-05 13:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 179.8 |
| e2e5628f-8af2-3bd4-b807-1160089d40b5 | -10.93 | -47.1106 | 2025-10-05 13:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 124.9 |
| 3afd1caf-dc85-396c-9518-c0534f86520e | -14.7514 | -54.6772 | 2025-10-05 13:50:00 | GOES-19 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 829d6a42-424f-3eb3-ab59-da59acb572f7 | -9.9212 | -50.1895 | 2025-10-05 13:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 5b96dae1-47b4-3f35-ae0e-291a7721f93f | -7.7932 | -42.6082 | 2025-10-05 13:50:00 | GOES-19 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 152.4 |


[Clique aqui para ver as próximas entradas](README161.md)

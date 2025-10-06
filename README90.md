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

## Dados Diários - Página 90

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e0375791-ccf8-3a16-b66b-6903c95fec21 | -8.519 | -46.3771 | 2025-10-06 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 90fc27bd-acbd-3b96-923c-dd3adc268bc7 | -9.6801 | -48.4232 | 2025-10-06 13:40:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 09c9793b-36e5-382e-9dfd-efd434a3802f | -8.0866 | -44.791 | 2025-10-06 13:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 130.2 |
| d6cca868-b411-3b1a-a2f8-0e48261031f8 | -15.3541 | -47.3235 | 2025-10-06 13:40:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 74.8 |
| bd330581-9e72-357d-b549-81bfc132876c | -8.5004 | -46.3566 | 2025-10-06 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 213.5 |
| 4d101eba-0045-3388-94b8-49a71a2b767c | -7.2577 | -44.8938 | 2025-10-06 13:40:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 6c1c89f4-4139-345d-8dab-7c861e34b7de | -8.88 | -47.6282 | 2025-10-06 13:40:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 53.2 |
| 3c49d37e-c849-3616-9e68-ca8486b63889 | -12.4468 | -45.5646 | 2025-10-06 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 62.4 |
| c227f933-ea51-3091-a894-2c7367ddc625 | -12.5541 | -48.1419 | 2025-10-06 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 54773995-5deb-3a44-844e-abf8161941cf | -14.8637 | -51.4589 | 2025-10-06 13:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 145.0 |
| 48851269-962f-3065-8617-f0e091ecca2b | -17.8417 | -57.6254 | 2025-10-06 13:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 122.1 |
| 38938cda-09f4-33b5-8954-d982105ec6ea | -8.6141 | -46.3003 | 2025-10-06 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 152.0 |
| 131af798-0bfc-324a-9f31-5f492eca64d9 | -7.0178 | -42.8054 | 2025-10-06 13:40:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 99.4 |
| 8a944226-b617-36d4-bb09-9fe79f6125ee | -6.9987 | -42.8308 | 2025-10-06 13:40:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 270.8 |
| 6764d52b-0b8c-3ab9-ab49-b8ecf3ad3f1a | -8.633 | -46.2984 | 2025-10-06 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 144.0 |
| 35e61dde-1426-36fb-b617-46ef81ce6554 | -7.7885 | -44.5228 | 2025-10-06 13:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 2480e4c0-3f10-3992-8a01-cb0777ee8313 | -7.2389 | -44.8955 | 2025-10-06 13:40:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 09db5f2f-db7b-38d3-99c7-500f98d0aa97 | -14.6325 | -52.5137 | 2025-10-06 13:40:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 88443e48-a115-3a98-8334-5b2c24e72605 | -11.0104 | -50.6744 | 2025-10-06 13:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 197.6 |
| 550e3df7-7290-33f1-b1ab-ebccf8048417 | -9.959 | -48.7425 | 2025-10-06 13:40:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 54.3 |
| ade475d7-03ba-3e57-935e-52d95a1bfc76 | -16.0038 | -50.8365 | 2025-10-06 13:40:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 49.9 |
| dc7f4758-8d9f-3426-a1e9-bd737d80d2b5 | -8.5193 | -46.3547 | 2025-10-06 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 173.2 |
| c1217dd8-7e53-3ea9-95ca-9289facf21d0 | -10.1383 | -45.4725 | 2025-10-06 13:40:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 66.6 |
| f66a61da-fcb6-3b7b-bf9e-5302c066f53d | -15.5704 | -47.2625 | 2025-10-06 13:40:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 39996dcb-c74e-3bbe-8645-0747e4fd17da | -12.9841 | -51.0648 | 2025-10-06 13:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 138.7 |
| 01e8d9ad-3efc-37c9-8b46-3ffe6d2fc202 | -7.7203 | -42.4023 | 2025-10-06 13:40:00 | GOES-19 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 115.4 |
| 0ed359d2-8243-322d-a5e5-f67cd0e3c422 | -16.0083 | -56.0155 | 2025-10-06 13:40:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 128.0 |
| 6bfacaa4-f522-3ed5-afe5-ed3f40be68ae | -12.5929 | -48.1144 | 2025-10-06 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 68.1 |
| b781a8b5-d8de-3b23-9139-4e07585c4a35 | -15.6616 | -47.5642 | 2025-10-06 13:40:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 136.2 |
| 14415a98-4655-3a6c-b856-de1db3b5544b | -9.6804 | -48.4014 | 2025-10-06 13:40:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 04777548-00ad-36fa-a908-dffb422e9373 | -7.2392 | -44.8727 | 2025-10-06 13:40:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 309d61e5-c697-3e4c-b691-cea777f0e495 | -7.2094 | -45.8942 | 2025-10-06 13:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 63.6 |
| cfd36ec5-55c0-323e-a7ec-460a7c723cf0 | -8.8794 | -47.6722 | 2025-10-06 13:40:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 99.1 |
| c7f44c90-6177-3c05-8003-26b95a0d8ad6 | -14.5442 | -46.9405 | 2025-10-06 13:40:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 22a8379f-130b-31b3-a204-3e36280b6586 | -14.2754 | -45.8647 | 2025-10-06 13:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 153.3 |
| fab3d231-5dd5-37ee-8c89-ef9a406ad9eb | -7.6993 | -42.5708 | 2025-10-06 13:40:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 76.2 |
| e1688b2c-f435-350e-8189-3ed595c466b3 | -10.6378 | -46.3396 | 2025-10-06 13:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 84.9 |
| a39cbeeb-ccc1-3908-a73c-f95375d65481 | -7.7014 | -42.4043 | 2025-10-06 13:40:00 | GOES-19 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 135.4 |
| 28a703c1-7e6b-31db-afd7-2be95eee9267 | -7.4669 | -43.0674 | 2025-10-06 13:40:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 81.5 |
| 878342be-731c-3b4b-bfed-75356f82f444 | -11.655 | -47.039 | 2025-10-06 13:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 89ec182e-749b-3ace-a917-e1c6493a1873 | -15.5896 | -47.2819 | 2025-10-06 13:40:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 815ec24b-befc-37ab-8441-3bf2bd1734a3 | -14.8828 | -51.4777 | 2025-10-06 13:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 118.1 |
| 96bcb44a-5ffb-320c-8294-eac1653f95a9 | -17.842 | -57.6048 | 2025-10-06 13:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 119.5 |
| 2239693f-8026-3e93-a342-56b6a5b09174 | -15.2351 | -49.2914 | 2025-10-06 13:40:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 514da14b-9e92-345c-b56b-3de5e544a8b4 | -11.0101 | -50.6958 | 2025-10-06 13:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 121.6 |
| f0e42d41-ce75-303c-99ef-7c1f8643bf31 | -13.2779 | -48.4607 | 2025-10-06 13:40:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 596f03a2-2b04-39cc-bbce-ac57e1a6b859 | -14.6897 | -48.3797 | 2025-10-06 13:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 115.7 |
| 7a707ec6-074b-3c22-931b-105adc3b4926 | -7.0369 | -42.78 | 2025-10-06 13:40:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 85.9 |
| 6760194b-fd3c-3f01-b87e-76f8fafeb119 | -10.6184 | -46.3646 | 2025-10-06 13:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 131.8 |
| cfb031d4-63a6-3b15-94e9-b18e28556336 | -10.391 | -50.3344 | 2025-10-06 13:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 151.1 |
| 313e8e62-4865-3550-9e19-40940d0776de | -10.0028 | -48.3015 | 2025-10-06 13:40:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 0fd9e6c0-a5f4-30db-8764-1f00852ad290 | -7.0175 | -42.829 | 2025-10-06 13:40:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 107.9 |
| 023830ad-0c37-3416-b2f2-bc536baafd03 | -14.6893 | -48.4021 | 2025-10-06 13:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 51.6 |
| 1b73f58d-b927-33e6-90f0-8345f9224e11 | -18.2869 | -45.4109 | 2025-10-06 13:40:00 | GOES-19 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 18c9be18-d9fb-35f5-ac88-a8bfb8229536 | -14.5438 | -46.9633 | 2025-10-06 13:40:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 133.2 |
| f992ca92-b502-3f3a-837d-4971f6c5ba87 | -12.184 | -50.9478 | 2025-10-06 13:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 0f1f15df-12cf-3369-a837-aaa498b27d7b | -18.018 | -44.9965 | 2025-10-06 13:40:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 75.7 |
| d1824ba8-0b88-3bc5-aa18-e4eaf56669f9 | -13.2515 | -47.7979 | 2025-10-06 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 81.7 |
| e2836987-9024-3c8e-9929-df4291d7f7e3 | -7.6801 | -42.5966 | 2025-10-06 13:40:00 | GOES-19 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 101.6 |
| 4e300d93-79a5-35dc-91a2-d81dcdc64c0c | -8.1879 | -44.2283 | 2025-10-06 13:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 178.4 |
| 2bbb2fc2-aad7-33e7-bd10-4723de83946d | -10.1576 | -45.4473 | 2025-10-06 13:40:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 4e40e2cc-52db-308f-acd4-e7aab6c83db6 | -12.4853 | -45.5587 | 2025-10-06 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 52c9e129-f392-3cb4-a149-1634c404ca4e | -8.5196 | -46.3323 | 2025-10-06 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 115.0 |
| 35646eb7-2387-3e73-8d44-1dde78398e8f | -7.4672 | -43.0438 | 2025-10-06 13:40:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 68.5 |
| a5e35f71-f23d-390b-acaa-b815df1c5473 | -9.9215 | -50.1682 | 2025-10-06 13:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 80ec4401-82c4-3e39-ab65-0454aa911126 | -8.8991 | -47.6042 | 2025-10-06 13:40:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 72214191-0505-3d03-b511-2b56004d160a | -18.2862 | -45.4348 | 2025-10-06 13:40:00 | GOES-19 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 60.5 |
| edc23218-ce8e-385d-8702-d46fc17048e2 | -11.1185 | -47.2207 | 2025-10-06 13:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 9a1fcf36-69ae-3a0f-9307-c41522ca2308 | -13.3237 | -48.0547 | 2025-10-06 13:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 9a977f4f-d96b-3ad3-98bc-5dc10057012d | -13.2708 | -47.7951 | 2025-10-06 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 53.7 |
| b00665d5-6334-36c0-81dc-fc9b77213e09 | -15.2156 | -49.2945 | 2025-10-06 13:40:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 4486d182-554f-36e0-b3c0-f80e767c48e2 | -14.2759 | -45.8416 | 2025-10-06 13:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 157.2 |
| 44854efc-16b2-36b2-9583-52b24f3d4381 | -10.1766 | -45.4449 | 2025-10-06 13:40:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 116.9 |
| fa611839-6a27-335e-95bb-e16daf86bbe2 | -7.0183 | -42.7582 | 2025-10-06 13:40:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 80.4 |
| 7d332c49-7c95-3735-bb10-b08a74901739 | -12.4464 | -45.5876 | 2025-10-06 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 9648a5d0-15ef-36dc-9839-56447f768148 | -7.4276 | -46.5239 | 2025-10-06 13:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 5d5b02ff-f401-3ad3-a37a-3b75a454b5f6 | -16.0086 | -55.9949 | 2025-10-06 13:40:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 64.8 |
| 50e9bac2-9dab-3a92-bb8f-a87948570310 | -19.5986 | -44.639 | 2025-10-06 13:40:00 | GOES-19 | PEQUI | MINAS GERAIS | Brasil | 3149606 | 31 | 33 | nan | nan | nan | Cerrado | 105.9 |
| ee6bf245-6d0c-363a-8236-f2a56fc816df | -8.5387 | -46.3079 | 2025-10-06 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 105.3 |
| c2a54af7-dea5-3b6f-843a-9fbf18d6d769 | -8.6327 | -46.3208 | 2025-10-06 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 048a3328-8960-3b91-9d8e-37a0b1eaaa01 | -14.55 | -46.6662 | 2025-10-06 13:40:00 | GOES-19 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 4b7839da-db5f-3351-9b54-c1e6e489b9b8 | -12.1458 | -50.9523 | 2025-10-06 13:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 120.1 |
| 69a547e6-c2f2-3750-b0ab-9a7d100c5e18 | -9.9779 | -48.7405 | 2025-10-06 13:40:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 55.7 |
| 13bf5612-0b4a-3f14-b087-c2a39aedd5f5 | -11.6849 | -45.2872 | 2025-10-06 13:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 09c8c72c-82d8-3c5e-9fa8-6de6335f282c | -14.5433 | -46.9861 | 2025-10-06 13:40:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 183.7 |
| e208c5f8-5729-3134-81c5-122a195f8b6c | -19.49 | -44.8839 | 2025-10-06 13:40:00 | GOES-19 | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 0a2d2504-3160-3157-ba52-bac868a30a13 | -10.9851 | -51.1443 | 2025-10-06 13:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 123.7 |
| e2ede527-af90-39a1-99f5-a2839598db1b | -11.8029 | -45.1087 | 2025-10-06 13:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 80.9 |
| ca717e02-8b8a-3637-bb1b-af66a31a8ed4 | -8.6139 | -46.3227 | 2025-10-06 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 137.3 |
| f372c64b-020d-3754-be0c-fa5e08c9b46f | -8.0678 | -44.7929 | 2025-10-06 13:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 60.3 |
| c192fe7a-23ab-3984-9c9e-03903c013235 | -11.9171 | -46.2362 | 2025-10-06 13:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 42c49b07-734d-376e-8849-074aa4ce378e | -10.4054 | -45.3931 | 2025-10-06 13:50:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 76.8 |
| fee33558-82d8-3df0-88a4-894950312c6c | -12.4468 | -45.5646 | 2025-10-06 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 100.3 |
| e07846ae-0aa6-367a-bc8e-6b37ce1dd26b | -13.304 | -48.0798 | 2025-10-06 13:50:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 73.1 |
| ac517503-7576-3849-8610-e0b3e0c56cb6 | -6.9987 | -42.8308 | 2025-10-06 13:50:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 180.5 |
| 18e609de-75ba-3e84-84da-d9e23749220a | -14.2759 | -45.8416 | 2025-10-06 13:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 231.4 |
| a37bde19-c56a-35d5-997f-5a9cb77fa926 | -7.6804 | -42.5728 | 2025-10-06 13:50:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 89.7 |
| 8faec081-e314-32f8-b03d-67d19bd183f4 | -10.391 | -50.3344 | 2025-10-06 13:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 177.9 |
| 25f7687f-6684-3499-9e5e-e4b0c11beee6 | -10.4099 | -50.3324 | 2025-10-06 13:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 137.1 |
| 4bd788f6-caed-31b2-8b43-083d7dd94229 | -18.2869 | -45.4109 | 2025-10-06 13:50:00 | GOES-19 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 81.4 |


[Clique aqui para ver as próximas entradas](README91.md)

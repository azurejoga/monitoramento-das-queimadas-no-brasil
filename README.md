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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 03707e90-d7ef-37a9-8bcc-0c18fb3f2ad2 | -12.1841 | -47.3922 | 2026-10-01 00:00:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 909d95e0-0742-338c-9eef-086440bc787d | -2.974 | -51.0247 | 2026-10-01 00:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 9757bc46-c326-38cd-92af-fa6898bbed68 | -12.8746 | -44.3357 | 2026-10-01 00:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 78.3 |
| c9fe2da8-ebcc-3ed1-9004-95ce0dc72f2d | -14.4225 | -51.2624 | 2026-10-01 00:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 8dcf2276-eb86-35a7-b205-7cacb00bca1f | 1.6933 | -55.9026 | 2026-10-01 00:00:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 17a5eb37-4e9a-3bc8-b451-2a0e1df7148a | -5.7376 | -45.1533 | 2026-10-01 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 76f14f9c-628d-3664-a67f-e9236cae0648 | -9.0231 | -65.7169 | 2026-10-01 00:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 483800d1-896f-3f28-aea8-9e01741f65d9 | -7.1269 | -43.1479 | 2026-10-01 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 40.6 |
| 372bb3f2-f30b-3f44-ad18-2e6cc47a36de | -3.295 | -53.8597 | 2026-10-01 00:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 157.2 |
| 7dcbb4d9-1a56-3579-bcca-d633c2a285f4 | -3.5808 | -51.4832 | 2026-10-01 00:00:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 376.3 |
| cb460388-ff09-3e61-b7df-1dd98deb2c24 | -9.0046 | -65.6988 | 2026-10-01 00:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 95.6 |
| fd786ea0-6da9-3f8f-9eca-4fabc9902a27 | -3.263 | -52.5827 | 2026-10-01 00:00:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 72b7e3f8-7451-33d6-8c45-9f2c70aaa70f | -9.6572 | -65.022 | 2026-10-01 00:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 72.1 |
| fd847234-e4cb-381d-b454-b398e95d4c16 | -18.9806 | -53.0217 | 2026-10-01 00:00:00 | GOES-19 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 7d052976-90de-3575-b7fc-c52d7b1644c6 | -10.5316 | -57.7747 | 2026-10-01 00:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 63c47e5e-7645-34c2-8eda-f09131343f9f | -2.908 | -54.151 | 2026-10-01 00:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| f33072b5-86d8-36d8-b9d1-79c1ab16e8d7 | -6.895 | -43.7066 | 2026-10-01 00:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 34.7 |
| ddf5ddc7-e1d3-3b02-a61b-330a1f23f5e9 | -4.0477 | -54.2394 | 2026-10-01 00:00:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 23992e13-07eb-3a45-a62b-c38c1944d847 | -14.4418 | -51.2597 | 2026-10-01 00:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 8f032392-b396-328a-aa12-b0b50a4b3bd5 | -6.7401 | -44.1371 | 2026-10-01 00:00:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 7eb6ca15-dac3-3cff-9bfa-aa8af1fe1882 | -6.0179 | -49.5648 | 2026-10-01 00:00:00 | GOES-19 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 95.7 |
| 3ffd4ee4-2ea3-35b8-8172-0f2aec55213f | -10.4629 | -59.1343 | 2026-10-01 00:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 42.4 |
| 60d50578-665f-3fa3-ae7b-2925850a3344 | -3.1841 | -60.0797 | 2026-10-01 00:00:00 | GOES-19 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 51.7 |
| dfeede3a-5447-33f9-8ce1-1294a4534922 | -6.0181 | -49.5435 | 2026-10-01 00:00:00 | GOES-19 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| f64876bb-3169-3ef8-be19-29f5f9879de0 | -13.6668 | -53.9522 | 2026-10-01 00:00:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 72.7 |
| f60502dd-6e04-372f-86db-e4bbae5c50bb | -5.7561 | -45.1747 | 2026-10-01 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 66.5 |
| d680ea4a-cebb-36ca-83f4-86ad5d66f404 | -8.5738 | -66.994 | 2026-10-01 00:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 36b831ab-99b3-3ccd-bfcd-e30955f3ef9b | -7.8486 | -45.8138 | 2026-10-01 00:00:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 61.1 |
| d1f37086-b19b-3206-8c4b-4eabdc94ed68 | -10.5692 | -57.7721 | 2026-10-01 00:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 02750046-b842-3515-994c-7c6dd361fc84 | -9.1407 | -64.4024 | 2026-10-01 00:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 96.2 |
| 79516eeb-5260-3a5a-b7fe-7d10f8ae6616 | -8.5554 | -66.9945 | 2026-10-01 00:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 69.0 |
| fb279cef-ff17-3293-9ecd-d73ce1029b4a | -9.1222 | -64.3843 | 2026-10-01 00:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 131.1 |
| c74f32df-01e0-3cb3-9a3b-d1deb3a35f3d | -5.7563 | -45.152 | 2026-10-01 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 147.4 |
| cf5411b9-41e1-3f76-a55f-5a0375c4b1ff | -3.106 | -50.2896 | 2026-10-01 00:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 170.5 |
| 3b48fb07-f818-3ac0-bd18-e66653edb695 | -9.0045 | -65.7174 | 2026-10-01 00:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 98.4 |
| a7211b35-c1d8-3c7e-95ea-33b71d936281 | -5.9993 | -49.566 | 2026-10-01 00:00:00 | GOES-19 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 12260ee2-d29a-320e-8754-3efc607410ac | -3.5809 | -51.4625 | 2026-10-01 00:00:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 113.4 |
| b2064ea9-ad24-363e-a596-6bfeace86786 | -3.1245 | -50.268 | 2026-10-01 00:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 8b9dfb1d-6c70-3412-a2e1-e781ada81e31 | -3.8043 | -51.0396 | 2026-10-01 00:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 4d8ae443-fbeb-36d5-9f47-857f01a1445f | -7.4977 | -54.9854 | 2026-10-01 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 01525d75-519d-3b6b-9c62-e2399e86a258 | -5.7357 | -43.2682 | 2026-10-01 00:00:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 91.8 |
| cc49787a-52a9-3837-8e52-610f8f91a54f | -9.1408 | -64.3836 | 2026-10-01 00:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 114.2 |
| ea06eeb9-9255-39b8-9fb5-bf1e9973764e | -5.7355 | -43.2916 | 2026-10-01 00:00:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 106.3 |
| fe29a5db-28d4-3934-ac03-e132be2b2507 | -9.1221 | -64.4031 | 2026-10-01 00:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 002e0599-4ef4-3f4e-8e91-c76349f014db | -3.2602 | -48.7796 | 2026-10-01 00:00:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| a1d67afc-73d0-3f9c-9ed8-4e0f3c9ae6be | -4.9514 | -45.4084 | 2026-10-01 00:00:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 0d33df53-9524-3608-85d4-9d69b199ef54 | -3.0192 | -53.887 | 2026-10-01 00:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| d6473254-9e24-3dfc-8089-2f07280a2590 | -5.7544 | -43.2668 | 2026-10-01 00:00:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 57.6 |
| bec21996-0dc6-34b1-b178-ecce831563c2 | -3.1756 | -51.351 | 2026-10-01 00:00:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| eb469b97-770c-3732-8db0-66f9700a4791 | -3.5624 | -51.4631 | 2026-10-01 00:00:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 90.2 |
| a792a086-d61e-397f-b83a-a808fe7a0388 | -13.6479 | -53.9336 | 2026-10-01 00:00:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 102.9 |
| e58ef35b-67da-3459-b5e1-95df083275f5 | -3.1061 | -50.2686 | 2026-10-01 00:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 120.9 |
| d28c73ea-b445-3e50-b38e-81946cb1327d | -3.1245 | -50.289 | 2026-10-01 00:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 108.3 |
| 59dec10d-0f5c-321c-a770-a73efc5b1bf4 | -12.8552 | -44.3389 | 2026-10-01 00:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 113b3105-e7d7-3fa4-85af-0554e8e6a6bb | -3.1572 | -51.3515 | 2026-10-01 00:00:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| f416939e-8773-3f50-a983-c1056e8dce01 | -3.1842 | -60.0607 | 2026-10-01 00:00:00 | GOES-19 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 62.3 |
| bc646e83-5631-3c08-a021-bd8dd058b5be | -10.5504 | -57.7734 | 2026-10-01 00:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 673a5371-b856-3757-82c8-a216c347b563 | -2.9081 | -54.1309 | 2026-10-01 00:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| cf52dbef-0d4e-3168-9746-cde966723986 | -3.5623 | -51.4838 | 2026-10-01 00:00:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 299.6 |
| d9b7befa-b8ff-3e96-9c0f-75b748fa1493 | -13.6671 | -53.9314 | 2026-10-01 00:00:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 108.9 |
| a1ea7258-a1e2-3681-82ab-2f805ed9e2bf | -6.2797 | -43.2711 | 2026-10-01 00:00:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 67.0 |
| deb6138a-d852-3d31-986e-aa6be532b313 | -3.2766 | -53.8602 | 2026-10-01 00:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 120acfbe-0f3e-3c56-8373-62ba682afe67 | -14.4414 | -51.2812 | 2026-10-01 00:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 6704fc95-a1df-3de4-b111-e775106b66f8 | -5.7542 | -43.2901 | 2026-10-01 00:00:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 61.5 |
| ea79fa16-9df4-3732-97a0-0f181e02b1f3 | -12.1841 | -47.3922 | 2026-10-01 00:10:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 46887a42-2a18-3c8b-88d0-3c7fed5cebc6 | -9.0045 | -65.7174 | 2026-10-01 00:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 59184e13-96f5-3e09-b065-752c807f4045 | -3.1756 | -51.351 | 2026-10-01 00:10:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| a842755c-77b1-333c-80f2-d75ceec979fb | -3.2951 | -53.8395 | 2026-10-01 00:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| e26b1bdf-129c-3c11-9876-c3c76b84433a | -5.7563 | -45.152 | 2026-10-01 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 125.7 |
| 23526d44-0f87-389b-8c73-08bacc5ac719 | -3.0876 | -50.2691 | 2026-10-01 00:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 9031e626-7687-3cc8-ae1b-718ccda1d463 | -6.7401 | -44.1371 | 2026-10-01 00:10:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 91ec1e67-149e-3bc2-9a41-ea6874b5836d | -3.295 | -53.8597 | 2026-10-01 00:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 181.9 |
| 59a3c576-51d1-3716-9945-146efbcc82ee | -2.9081 | -54.1309 | 2026-10-01 00:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| bfefd69a-7fdf-3a50-acd3-afe1591ee28e | -5.7357 | -43.2682 | 2026-10-01 00:10:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 6fb98ea0-2ea7-354b-b4a3-ead6cde2a05f | -14.4418 | -51.2597 | 2026-10-01 00:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 112.2 |
| fe278e2c-4f95-3208-b2a3-f431de4ceefa | -6.895 | -43.7066 | 2026-10-01 00:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 34.8 |
| 8433cbc3-d334-35d6-8818-c37be6e2d805 | -6.914 | -43.6816 | 2026-10-01 00:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 28.8 |
| ce0b3d87-a689-3d79-a5a5-8b02fe2c5476 | -3.2766 | -53.8602 | 2026-10-01 00:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 583dc33b-29b6-336e-9640-e56a13ae755e | -14.4414 | -51.2812 | 2026-10-01 00:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 846aa836-0696-3994-b7ed-09980b8f5d1a | -6.8952 | -43.6833 | 2026-10-01 00:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 35.3 |
| d97c21ea-0b3e-367d-82e3-d979238e2375 | -14.4225 | -51.2624 | 2026-10-01 00:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 79.6 |
| f0d6e014-9ece-32e3-a07c-473c2feb426e | -7.1455 | -43.1696 | 2026-10-01 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 49.1 |
| 2bf5587d-3490-3b76-92fe-66334b1bee3e | -3.1061 | -50.2686 | 2026-10-01 00:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 93.8 |
| e912807b-bffe-3651-8533-ac1ef2e6dfe2 | -9.0046 | -65.6988 | 2026-10-01 00:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 57.6 |
| e089a55a-007a-3bed-8f03-f2a04a221c13 | -3.1841 | -60.0797 | 2026-10-01 00:10:00 | GOES-19 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 7e5a221e-95e3-3e07-896a-fa962f9b3d3d | -3.5808 | -51.4832 | 2026-10-01 00:10:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 307.1 |
| 2a23b3c9-dc7b-3a99-a9d1-53efff300b5f | -7.1266 | -43.1714 | 2026-10-01 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 281.7 |
| 6c783c64-8fdd-3bd6-a59e-9d2f4b39073f | -6.9317 | -59.2798 | 2026-10-01 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 3d3a08d1-8309-3270-8961-b4caf986bf5f | -12.8746 | -44.3357 | 2026-10-01 00:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 416211d1-d810-3d45-aab8-6103557250fb | -12.8552 | -44.3389 | 2026-10-01 00:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 74.8 |
| e793009f-062b-3abd-9699-11b0087fb338 | -7.1457 | -43.1461 | 2026-10-01 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 67.7 |
| 794805fa-35d0-388a-b9ef-8ff3017588fc | -3.5623 | -51.4838 | 2026-10-01 00:10:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 318.5 |
| d0450c67-c8ee-33b0-8f88-bacfefc488c7 | -7.108 | -43.1497 | 2026-10-01 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 366.5 |
| 3db4916b-91f3-39d9-984f-412c18a21698 | -6.0179 | -49.5648 | 2026-10-01 00:10:00 | GOES-19 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 84.3 |
| 868ab697-bed2-3795-b0df-142ebcda25c8 | -13.6668 | -53.9522 | 2026-10-01 00:10:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 732bdab7-ca99-3a3d-a741-9b277066be31 | -6.2609 | -43.2727 | 2026-10-01 00:10:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 49.1 |
| e3c9e0b0-a73a-34b5-a040-a2e4dabb1f0c | -3.1572 | -51.3515 | 2026-10-01 00:10:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 95.2 |
| 01411c11-87b7-3d5e-a866-91d6d75f251d | -8.5554 | -66.9945 | 2026-10-01 00:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 25f3a6a0-6aaa-3f56-9dcb-a8bd01ea6536 | -9.1408 | -64.3836 | 2026-10-01 00:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 82.5 |
| a07fbbd5-b438-3d8b-bb73-fe6cca89ac1d | -13.6671 | -53.9314 | 2026-10-01 00:10:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 99.5 |


[Clique aqui para ver as próximas entradas](README2.md)

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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| af14ecda-5ce5-333c-b471-b6415dbe425b | -3.8566 | -55.9967 | 2026-10-07 02:00:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 73.7 |
| c7092ead-6e26-3643-8c58-bfa9c1d46ee2 | -3.1787 | -50.5597 | 2026-10-07 02:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 106.7 |
| 84283375-bf4b-3458-be43-8e5e0d202704 | -4.8397 | -42.911 | 2026-10-07 02:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 124.9 |
| 32f549f9-4c9d-3181-9539-d7bc3453c9bf | -3.4762 | -50.0883 | 2026-10-07 02:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 83.0 |
| b6bdfa31-6ecb-3073-ba20-93f562b08ee5 | -8.7228 | -45.1812 | 2026-10-07 02:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 226.1 |
| d581c65a-506c-3d84-9b14-135a770bea0c | -2.7796 | -54.0937 | 2026-10-07 02:00:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 171.2 |
| a61ea70a-e38c-3a3e-8c70-f2b45dc8ceeb | -3.1787 | -50.5807 | 2026-10-07 02:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| a893ee35-5357-33c5-a1a6-840c897e2bbe | -3.5061 | -51.6924 | 2026-10-07 02:00:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 220d1445-6a1f-38b6-a8f8-438d0a15d2f2 | -11.014 | -45.4272 | 2026-10-07 02:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 12347254-586c-371e-b616-6a3799b649db | -3.1114 | -53.7839 | 2026-10-07 02:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 85.2 |
| d420f51b-a93b-37b2-8150-80e60063de42 | -2.7797 | -54.0736 | 2026-10-07 02:00:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| ce404a93-2b98-3eb6-859f-19308e6a6b70 | -11.7143 | -43.652 | 2026-10-07 02:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 520e641b-97bd-3e05-a7d6-d6304bad8d76 | -3.4577 | -50.089 | 2026-10-07 02:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 12d38a2b-8388-372d-8cf3-d4472b02cff1 | -3.5127 | -54.6362 | 2026-10-07 02:00:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 003097fd-a7d8-3496-b518-3fe321a1c149 | -3.5515 | -59.4807 | 2026-10-07 02:00:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 23d78a25-a61e-3a8b-9445-d9967dfa368c | -14.2531 | -41.6256 | 2026-10-07 02:00:00 | GOES-19 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 182.8 |
| 802a82a2-9923-3fe3-aae5-637baf2824ea | -3.531 | -54.6757 | 2026-10-07 02:00:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 7664c4a3-c52e-3858-a6c0-97f205c6f6cf | -8.7036 | -45.2061 | 2026-10-07 02:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 287.7 |
| 8e95e243-fd67-33eb-b600-4eb3af6653cd | -3.5311 | -54.6357 | 2026-10-07 02:00:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 5ab2bf24-4333-3e4e-8e65-1a9e2480704a | -2.9264 | -54.1505 | 2026-10-07 02:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| fd26a6e0-1b54-3d3c-8530-fdf848f2ad5a | -8.7033 | -45.2289 | 2026-10-07 02:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 71eeba82-3856-3d8e-8cb1-2507355c028b | -3.0001 | -54.1086 | 2026-10-07 02:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 2391dc0e-b363-3fb6-abaa-ff050d45054e | -2.7613 | -54.0941 | 2026-10-07 02:00:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 235.7 |
| dfab8aaa-8a42-318d-a357-e3fda15a713c | -1.801 | -57.1161 | 2026-10-07 02:10:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 7acd56c6-347f-3720-8b02-d85f45a873e7 | -3.6762 | -60.6219 | 2026-10-07 02:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 62.4 |
| eff19d43-e3f1-3a78-9f25-fa60bfe45a27 | -2.7612 | -54.1142 | 2026-10-07 02:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 99.0 |
| 8a87e5f6-79b9-3605-9bd8-e33be6e9d440 | -2.9448 | -54.1501 | 2026-10-07 02:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| aefe77a6-621e-3744-ad75-3a5fd65a0a6e | -11.1051 | -45.689 | 2026-10-07 02:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 111.2 |
| 9d9d60ba-c081-3c7a-a00c-c591f8615c1e | -3.6205 | -55.2907 | 2026-10-07 02:10:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 1e3e17c2-c847-3a75-a4c0-6bae35655e19 | -5.7189 | -45.1547 | 2026-10-07 02:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 8c1e34c9-798c-39df-b502-28851ed52f08 | -3.0375 | -53.9066 | 2026-10-07 02:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| acc84697-0e56-3610-8deb-ab5cef3cab27 | -11.7335 | -43.649 | 2026-10-07 02:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 166.1 |
| 403dc0a9-e041-3c6d-b59d-49d7858bbf45 | -3.0184 | -54.1282 | 2026-10-07 02:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 81bbb400-6942-390c-9fef-2f96c6cab293 | -9.4621 | -67.0817 | 2026-10-07 02:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 39.2 |
| 9bc7e05a-c36e-3ca9-a6d3-72b41a2b5e21 | -11.0137 | -45.4501 | 2026-10-07 02:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 130.6 |
| b0b75d1b-7d97-3217-ab24-6584168fc718 | -2.9264 | -54.1505 | 2026-10-07 02:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 70b3a6ed-346e-3870-a325-9c157a923dd9 | -2.7797 | -54.0736 | 2026-10-07 02:10:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| d81358fe-7779-3ccf-a8ce-b42523f84ead | -8.7225 | -45.204 | 2026-10-07 02:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 287.0 |
| 1bcb1b2c-4643-347e-970b-77b9675a217b | -10.9949 | -45.4298 | 2026-10-07 02:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 145.5 |
| 791b0151-bc3d-3871-bd65-297c8d5b52ff | -3.1114 | -53.7839 | 2026-10-07 02:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| f29bacb2-1df6-3443-a99d-2875026511b2 | -2.7613 | -54.074 | 2026-10-07 02:10:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 83.8 |
| aabf3cbb-55e1-3d78-8ea2-81db99f97f0f | -11.1238 | -45.7093 | 2026-10-07 02:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 63c1bf2b-6404-3d52-b050-b853dbaac49e | -3.6206 | -55.2708 | 2026-10-07 02:10:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 1fd95d3b-6db2-37b8-a44c-61a3e93c891c | -3.1115 | -53.7637 | 2026-10-07 02:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 82.4 |
| b465c602-f1eb-3e00-8082-cfeca4ed6f77 | -2.7613 | -54.0941 | 2026-10-07 02:10:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 212.7 |
| 5fe86a5b-577e-327b-8b3a-2e85d50ecc85 | -3.658 | -60.6222 | 2026-10-07 02:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 124.7 |
| cd9b6135-537a-35d6-a2f1-b02bc7727115 | -3.4762 | -50.0883 | 2026-10-07 02:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 3dd0b963-9f9c-37a8-8a9b-52c04b75e8fd | -11.1047 | -45.7119 | 2026-10-07 02:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 198.8 |
| 67ddb893-3b14-3776-a133-5e2d26dc60e3 | -11.7143 | -43.652 | 2026-10-07 02:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 78.1 |
| d2b24a91-bdd3-3671-8372-629364a5b79f | -3.0 | -54.1287 | 2026-10-07 02:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 83.0 |
| dd94aee7-0fc5-365f-bee4-e5b0d5e18761 | -3.1787 | -50.5597 | 2026-10-07 02:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 103.9 |
| 9bec854b-451c-3ec7-904d-06abd358988f | -2.7796 | -54.1138 | 2026-10-07 02:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 112.2 |
| 8571e26a-1dc1-3e8d-a307-691f80d5908c | -2.7796 | -54.0937 | 2026-10-07 02:10:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 168.4 |
| 35d02eeb-5ba1-3329-8f93-87d73e57723e | -3.0374 | -53.9268 | 2026-10-07 02:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 73.7 |
| e6229520-9bd5-3349-8f81-7bdf93cf0f5f | -11.7331 | -43.6727 | 2026-10-07 02:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 68.7 |
| b36eee56-0841-308e-b183-8bda4624cdad | -8.7228 | -45.1812 | 2026-10-07 02:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 226.0 |
| cec72d5a-307f-3caf-9592-0f95950b6793 | -7.4129 | -44.4673 | 2026-10-07 02:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 61.9 |
| c4a7a517-abc3-3045-ab46-ade3815b7085 | -3.8566 | -55.9967 | 2026-10-07 02:10:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| c6026741-71a3-3b5b-93d5-584aec08e4ed | -3.2728 | -50.1372 | 2026-10-07 02:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 98595443-0752-3b25-be13-12aa15119ae7 | -3.8567 | -55.9769 | 2026-10-07 02:10:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 225b72da-6f75-30f0-b127-2036a98b443a | -14.2531 | -41.6256 | 2026-10-07 02:10:00 | GOES-19 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 108.1 |
| 7abff1cd-7ade-3fe8-95a1-9934ace32151 | -8.7033 | -45.2289 | 2026-10-07 02:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 06db6077-62ff-355a-ba71-88c8f391484f | -3.5515 | -59.4807 | 2026-10-07 02:10:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 9ce82158-9cc9-3909-b866-97f89b310bc1 | -8.7039 | -45.1832 | 2026-10-07 02:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 142.4 |
| 25f7cdcd-d24c-39d0-85be-dad47cf4e047 | -3.6579 | -60.6412 | 2026-10-07 02:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 100.0 |
| a08aac4f-a1a9-3c71-8138-1e5feb58d228 | -8.7036 | -45.2061 | 2026-10-07 02:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 271.5 |
| bd280a86-8a3c-3f8d-bc2c-bae95247237d | -11.014 | -45.4272 | 2026-10-07 02:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 117.9 |
| 2b7c01e5-715f-3aa4-9f0e-1ce925dc3227 | -8.2865 | -50.2731 | 2026-10-07 02:10:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 152.6 |
| f320cd0b-19f7-3c93-aaeb-b0af2bd15aac | -10.9946 | -45.4527 | 2026-10-07 02:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 67.0 |
| b8562f81-f901-30c1-8018-fb267118fcb8 | -3.1787 | -50.5807 | 2026-10-07 02:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 13318b8e-1d9c-3406-8d21-755a3cc98018 | -11.2333 | -44.8678 | 2026-10-07 02:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 70.6 |
| cfc44892-a5ab-39ef-87ba-18dfa45922ec | -8.7 | -45.19 | 2026-10-07 02:15:00 | MSG-03 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e87c733e-35e7-3d81-b08e-38fa967223aa | -3.29 | -54.07 | 2026-10-07 02:15:00 | MSG-03 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 11f3ad34-7346-3b2c-9dad-b3f6e926a195 | -3.29 | -54.01 | 2026-10-07 02:15:00 | MSG-03 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1ea6d106-83c5-328f-8995-1641338a2acd | -8.7 | -45.24 | 2026-10-07 02:15:00 | MSG-03 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 8d33823a-83ee-3444-9906-b94b609fb2ef | -11.1051 | -45.689 | 2026-10-07 02:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 119.4 |
| 2cd07883-159c-3369-be67-166dbdfad331 | -3.1115 | -53.7637 | 2026-10-07 02:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 13ba9c81-a2da-3a6f-8fa9-0deb501f0f99 | -5.7189 | -45.1547 | 2026-10-07 02:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 1e9caf97-bcaa-368b-aabb-06f66836728d | -3.0374 | -53.9268 | 2026-10-07 02:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| fccd470f-d07a-3940-b265-760c8c796a40 | -2.7796 | -54.1138 | 2026-10-07 02:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 105.6 |
| b37d70eb-4308-3272-83cd-ddb2437a8d3c | -9.4621 | -67.0817 | 2026-10-07 02:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 1c2a806e-4bec-3590-bf58-a4e283c3c088 | -3.6206 | -55.2708 | 2026-10-07 02:20:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| daec2605-e100-3548-886f-1582029642ae | -3.0 | -54.1287 | 2026-10-07 02:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 83.2 |
| fa8c4db7-4b04-3d74-90c6-1f72aafe8b2c | -11.0137 | -45.4501 | 2026-10-07 02:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 162.5 |
| c71ef9d3-3a3a-3201-a02b-a8f90c50bd21 | -3.658 | -60.6222 | 2026-10-07 02:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 114.9 |
| 8f8c52f7-bfba-3fef-aa33-7613d9c1d1d3 | -11.7331 | -43.6727 | 2026-10-07 02:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 5a2dcf1c-4012-3c21-9368-d206daaaf5b1 | -5.7187 | -45.1773 | 2026-10-07 02:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 2e92e118-a9cb-3151-9a5f-555bd4c02333 | -3.5515 | -59.4807 | 2026-10-07 02:20:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 5e9ddeef-d79e-3214-8cda-177d1ba14928 | -2.7796 | -54.0937 | 2026-10-07 02:20:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 156.4 |
| b1e96a87-17ba-3920-915f-783ab39ebfd0 | -3.6762 | -60.6219 | 2026-10-07 02:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 4181395e-39b2-3c8a-9612-13965067c058 | -3.8567 | -55.9769 | 2026-10-07 02:20:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| b8c8a574-008e-3372-9c11-0355fdb81f65 | -3.0184 | -54.1282 | 2026-10-07 02:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| a576d374-e856-3a99-b4f9-9b4fe0d02c94 | -2.7612 | -54.1142 | 2026-10-07 02:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 149.6 |
| 66167dca-bd00-355b-91c1-bae56a7ef0c8 | -2.7613 | -54.0941 | 2026-10-07 02:20:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 239.1 |
| 935d8e4c-e145-38ec-83d2-14a6f8b35fd7 | -2.7797 | -54.0736 | 2026-10-07 02:20:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 1138c1da-7bd7-3001-928f-1fb05639d544 | -10.9946 | -45.4527 | 2026-10-07 02:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 106.8 |
| 6410f45d-8b6f-3e4a-a155-fa81c633b8d0 | -11.7335 | -43.649 | 2026-10-07 02:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 161.4 |
| 00ea090d-40ca-3351-92bf-ca3c24fcf5eb | -8.7225 | -45.204 | 2026-10-07 02:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 241.4 |
| 2b47999f-1aeb-3f8c-a9cf-0e36d1c7ea40 | -3.8566 | -55.9967 | 2026-10-07 02:20:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 249a3a70-c48f-3f95-8236-760cfc1c8727 | -14.2531 | -41.6256 | 2026-10-07 02:20:00 | GOES-19 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 69.0 |


[Clique aqui para ver as próximas entradas](README28.md)

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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 11f7396b-53f7-360c-b04f-66905973a995 | -5.14599 | -55.93284 | 2026-09-16 00:24:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 88.4 |
| 6a0de6f9-52de-39ae-94e5-c8817c204a6d | -3.42899 | -58.22288 | 2026-09-16 00:24:00 | TERRA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 87f41cfe-4dc8-3aac-8866-ed22027606a7 | -2.90759 | -50.43536 | 2026-09-16 00:24:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| cda9504f-2598-3963-9767-5a8f00f81f02 | -2.89375 | -50.4213 | 2026-09-16 00:24:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| d040e539-83d0-3098-b8c6-f78bb9bd4954 | -2.45926 | -54.77133 | 2026-09-16 00:24:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| afdb49fa-7595-393e-91af-81821fcbf1f6 | -2.72942 | -54.9876 | 2026-09-16 00:24:00 | TERRA_M-M | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 8a6fea71-b202-3052-8236-cdbd611eec59 | -4.53531 | -54.97156 | 2026-09-16 00:24:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| fe4b0b0c-b731-3d80-8db8-ef87e46f04e9 | -2.70423 | -57.62869 | 2026-09-16 00:24:00 | TERRA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 24.6 |
| 7c46b37d-2caf-3da7-8daa-d57cacc1f2b4 | -3.16871 | -58.65046 | 2026-09-16 00:24:00 | TERRA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 622f0940-cf09-3581-9dc5-bf806c6329b3 | -2.90528 | -54.86032 | 2026-09-16 00:24:00 | TERRA_M-M | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 107fb20d-2eea-3db5-adbd-a35c78af95f8 | -5.11939 | -55.93661 | 2026-09-16 00:24:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 31152956-dde8-3c59-8296-6b939c947b54 | -3.42077 | -58.23489 | 2026-09-16 00:24:00 | TERRA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 179c0d6c-9868-3202-bacc-832377c3a892 | -1.2274 | -54.12445 | 2026-09-16 00:24:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| a4713461-fa50-3168-961f-7a2ff61df115 | -3.01542 | -51.33886 | 2026-09-16 00:24:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 1d15a068-8308-33e9-bc4b-aba019f9b839 | -1.7445 | -55.2645 | 2026-09-16 00:24:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| faeb1e3b-c358-345f-a0d6-97ecc533fd99 | -2.87882 | -51.74225 | 2026-09-16 00:24:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 42abadda-7f49-382c-bbf1-3682cd968692 | -3.17052 | -61.10725 | 2026-09-16 00:24:00 | TERRA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 22.8 |
| ca3de5d4-4a2e-34ae-9de0-841c37858fe1 | -3.42756 | -58.21222 | 2026-09-16 00:24:00 | TERRA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 2e973f69-3f66-334e-88b2-a5f2af11664e | -3.11859 | -57.68753 | 2026-09-16 00:24:00 | TERRA_M-M | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 21.3 |
| 3b705ba4-6fa0-3c33-b932-34aaef6b9406 | -5.13713 | -55.9341 | 2026-09-16 00:24:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| f5d45bae-5ac1-3e18-aa89-05d4255f3d2f | -3.75643 | -51.14112 | 2026-09-16 00:24:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| fdb9743f-3656-37ae-ad4f-2da365d476ad | -4.51369 | -54.96268 | 2026-09-16 00:24:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 6c64f41f-6373-31c7-b672-a2545c04ddef | -1.0195 | -53.74701 | 2026-09-16 00:24:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |
| abb55af7-466b-3e2d-b935-b9203efdda1b | -3.58377 | -58.5409 | 2026-09-16 00:24:00 | TERRA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 64f19d35-0945-33cb-a493-001cc527f688 | -1.64142 | -55.18608 | 2026-09-16 00:24:00 | TERRA_M-M | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 122a131d-848f-398d-acfe-5fdacfd64be9 | -3.10927 | -57.68882 | 2026-09-16 00:24:00 | TERRA_M-M | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 36.8 |
| 014723da-ef1b-37c8-bf63-02b000bcb0e5 | -1.61036 | -55.56403 | 2026-09-16 00:24:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 5122d22c-c909-3e22-98bf-9df1d07019e1 | -2.57458 | -56.00173 | 2026-09-16 00:24:00 | TERRA_M-M | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 3c7b5e9d-b344-3673-bcc2-43f242ea9810 | -4.29712 | -56.26691 | 2026-09-16 00:24:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| af459c59-73ab-369f-b9eb-9b2c1bd6d2a5 | -4.08931 | -51.12344 | 2026-09-16 00:24:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| e7998199-7742-361d-b5eb-b7ee9c6614a6 | -3.14452 | -51.11285 | 2026-09-16 00:24:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 65310e89-01b4-397b-a8a8-b58123ff2734 | -5.1206 | -55.94553 | 2026-09-16 00:24:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 0a36f535-1aea-39e6-b5b5-bf793ba64004 | -3.26536 | -54.52384 | 2026-09-16 00:24:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 91b565da-cc30-3bc3-b3a8-95a79edbb3fd | -1.62036 | -55.57157 | 2026-09-16 00:24:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 1900ce1d-e190-337d-b61a-3b46634d483a | -3.15728 | -58.64057 | 2026-09-16 00:24:00 | TERRA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 80501b10-6ec5-3fca-9824-004ac728e680 | -2.99318 | -54.16218 | 2026-09-16 00:24:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a1b8877b-9d82-341d-ab19-e3ea18822ac9 | -2.34688 | -56.0966 | 2026-09-16 00:24:00 | TERRA_M-M | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| fc9a916a-794f-3095-9618-aeef83c00ab8 | -3.10665 | -51.82462 | 2026-09-16 00:24:00 | TERRA_M-M | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 6325494b-d442-38c4-a70b-9029540efe9b | -4.83795 | -55.76775 | 2026-09-16 00:24:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b7551ad2-2583-3ac1-8a24-948549d45ef1 | -1.79712 | -47.83755 | 2026-09-16 00:24:00 | TERRA_M-M | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 99273ccc-6b9b-3764-82ef-b3b59b04d414 | -3.4797 | -54.67329 | 2026-09-16 00:24:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| ab54df72-3038-32bd-9a1d-01e4552033fb | -2.62837 | -54.19063 | 2026-09-16 00:24:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 303f23b3-3718-3133-9940-c40973f87c5c | -3.17247 | -53.92467 | 2026-09-16 00:24:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 8709e31e-bb2c-3f6e-93cc-9dd1677cf980 | -1.28901 | -55.71357 | 2026-09-16 00:24:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 65068e58-4fbc-3679-a732-06840075f52a | -9.1123 | -45.7067 | 2026-09-16 00:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 51.0 |
| 244d75a5-f375-31d9-99c9-7c9dec071135 | -9.4102 | -62.7113 | 2026-09-16 00:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 2c383ae8-9013-3563-81b7-948ba4b3f3a9 | -9.0931 | -45.7314 | 2026-09-16 00:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 110.3 |
| 57e34258-fc0b-3be2-866a-580da3ccbb9c | -3.3806 | -50.8458 | 2026-09-16 00:30:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| fba63230-dd2a-3c9b-9c42-e9edae46f378 | -8.3319 | -51.3022 | 2026-09-16 00:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 22.1 |
| ea05bbeb-4365-3733-a89a-4b68873e7367 | -18.2257 | -41.2559 | 2026-09-16 00:30:00 | GOES-19 | ATALÉIA | MINAS GERAIS | Brasil | 3104700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 98.9 |
| 5e78d916-4127-370e-a239-cfe3d376376f | -11.5033 | -45.8396 | 2026-09-16 00:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 6e6a9dce-3f07-3e1d-8fc1-6957da58eff2 | -7.6327 | -67.1644 | 2026-09-16 00:30:00 | GOES-19 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 41.9 |
| baf8c1cc-f325-3197-a473-c9b0e1211ef5 | -3.1174 | -57.6779 | 2026-09-16 00:30:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 883b3dc9-69b1-3617-a0ee-38cff141e715 | -4.2951 | -49.1234 | 2026-09-16 00:30:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 8f60e1dc-32e9-3ead-9484-3eabfeaad43d | -11.9906 | -52.4695 | 2026-09-16 00:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 64ef8c33-8d51-3b5e-878f-22218888cff2 | -5.144 | -55.9345 | 2026-09-16 00:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 0cf44c9c-51aa-3cb1-8de2-549970cbe111 | -10.7015 | -54.1663 | 2026-09-16 00:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 60.2 |
| c875c168-5999-38ba-ab60-0ddcd9c41bd9 | -5.7754 | -45.1053 | 2026-09-16 00:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 57.2 |
| f76867fd-9a24-3dba-ab9d-c44385d296bb | -2.1052 | -52.037 | 2026-09-16 00:30:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 87e11df4-9ad1-3cd4-bf0a-938dd84ef574 | -12.6051 | -50.8548 | 2026-09-16 00:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 110.1 |
| 4b04fe69-8835-317f-9ed6-5556dd5e37ab | -9.7136 | -64.9074 | 2026-09-16 00:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 734c6b06-11d4-310d-ae24-245f9964edce | -9.7322 | -64.9067 | 2026-09-16 00:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 47.9 |
| a84042d7-c49c-36bc-8060-7241dc587b44 | -5.1217 | -47.5928 | 2026-09-16 00:30:00 | GOES-19 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 54.7 |
| cf977199-2e08-355a-a38a-f0589765a6a6 | -5.7756 | -45.0826 | 2026-09-16 00:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 68.6 |
| d9f3225d-8e4b-3d79-b522-e2ed631bb50f | -7.651 | -67.1824 | 2026-09-16 00:30:00 | GOES-19 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 12200169-9b78-35c6-80d6-fc0cd3185381 | -12.6245 | -50.8311 | 2026-09-16 00:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 95.7 |
| f2e66b5c-90aa-3212-a5b0-41dd9fa06015 | -10.8301 | -46.2022 | 2026-09-16 00:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 39.0 |
| c0f7faea-916d-3bc2-9500-f28aae23e085 | -1.2907 | -55.7098 | 2026-09-16 00:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 8c713e0e-7193-340a-9b52-12660e8c10ac | -7.6511 | -67.164 | 2026-09-16 00:30:00 | GOES-19 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 113.7 |
| 25be13e2-036a-3ec1-ab64-6a5ae2d28cbc | -11.5029 | -45.8624 | 2026-09-16 00:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 47.1 |
| 4538e2d7-3bd6-3375-b4be-e678af60028c | -8.8399 | -44.894 | 2026-09-16 00:30:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 50.9 |
| adf9e9db-4cea-3ab2-923a-bdd1574cb9c0 | -9.112 | -45.7294 | 2026-09-16 00:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 182.4 |
| 088a645d-7937-3871-bcdf-5e352c399edf | -5.1215 | -47.6146 | 2026-09-16 00:30:00 | GOES-19 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 126.6 |
| 52330789-4699-34e5-a644-4e3cff6d8629 | -18.2265 | -41.2303 | 2026-09-16 00:30:00 | GOES-19 | ATALÉIA | MINAS GERAIS | Brasil | 3104700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 90.8 |
| 36a0c679-3754-3d2b-80b6-af0f2f90485b | -16.2596 | -39.4398 | 2026-09-16 00:30:00 | GOES-19 | EUNÁPOLIS | BAHIA | Brasil | 2910727 | 29 | 33 | nan | nan | nan | Mata Atlântica | 80.4 |
| 8250c43a-011f-31ba-abea-bb75dfe91e98 | -9.3892 | -60.3215 | 2026-09-16 00:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 01ab35e2-50b0-3dd5-9aea-269f66770acd | -10.4695 | -44.9491 | 2026-09-16 00:30:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 70696816-b515-3e19-9a31-f3c9ec3861bb | -3.1634 | -61.1048 | 2026-09-16 00:30:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 42.6 |
| 0c5d4377-987e-35ef-8b1d-ba690c573773 | -12.6242 | -50.8525 | 2026-09-16 00:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 112.8 |
| 2d4d60ff-6c6d-312d-a77d-a9cae4ba82d3 | -2.1051 | -52.0575 | 2026-09-16 00:30:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 9750f392-6899-3cda-8308-71f93d6d4c44 | -12.6054 | -50.8334 | 2026-09-16 00:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 145.9 |
| b51309e3-90c9-38ec-9fac-52b06620005c | -12.3277 | -47.9513 | 2026-09-16 00:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 81.9 |
| ddac41d0-8afe-3d0c-bbb4-ee7d9847edfc | -9.3893 | -60.3022 | 2026-09-16 00:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 128.8 |
| bc06cc81-5f9b-3e1c-bdba-22771dd98d64 | -3.1816 | -61.1045 | 2026-09-16 00:30:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 690e0ff3-7473-3192-90c4-237d3e4a0433 | -3.1265 | -61.2566 | 2026-09-16 00:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 41.5 |
| 11c0583a-756c-39da-ae62-5c8232bf2e93 | -12.7709 | -51.2403 | 2026-09-16 00:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 23c56047-3e93-352a-bd6a-e6ce0b6b76b5 | -10.7015 | -54.1663 | 2026-09-16 00:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 428f06f8-ed31-3bcc-99fb-213a302d891f | -12.6245 | -50.8311 | 2026-09-16 00:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 46.6 |
| de443eee-f0be-32f4-a6fd-33d2a2a47834 | -5.144 | -55.9345 | 2026-09-16 00:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 92.5 |
| b103492b-a3e2-3b6c-9134-d1dc9cc30f81 | -4.2951 | -49.1234 | 2026-09-16 00:40:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 80.9 |
| b783f3b8-e750-338f-ba8f-af69c38f7440 | -9.3892 | -60.3215 | 2026-09-16 00:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 8654faff-7a81-3c5c-a1c5-0483a51b4a2f | -11.5033 | -45.8396 | 2026-09-16 00:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 6dc84895-6766-3096-a585-ee794109bdc2 | -7.6511 | -67.164 | 2026-09-16 00:40:00 | GOES-19 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 117.0 |
| 7a16678a-24a9-3917-8db8-e2af60cc96aa | -9.7322 | -64.9067 | 2026-09-16 00:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 46.9 |
| fe8b6e31-673e-32b2-9ed4-fcecd80ee08e | -9.5152 | -40.331 | 2026-09-16 00:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 103.4 |
| b45de6a3-fb80-3a5a-ba75-ae294076b5ef | -3.1816 | -61.1235 | 2026-09-16 00:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 4ea690f8-8ec5-3c8c-a813-aaecae224d37 | -3.1816 | -61.1045 | 2026-09-16 00:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 8232940f-91fb-3e1a-addc-d4519229d604 | -18.2257 | -41.2559 | 2026-09-16 00:40:00 | GOES-19 | ATALÉIA | MINAS GERAIS | Brasil | 3104700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 124.7 |
| 1a9b663a-e425-3e07-898d-75bb69880942 | -7.6327 | -67.1644 | 2026-09-16 00:40:00 | GOES-19 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 43.2 |
| 339180d1-fa69-349f-a949-b95f8f032bef | -5.1029 | -47.6157 | 2026-09-16 00:40:00 | GOES-19 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 54.5 |


[Clique aqui para ver as próximas entradas](README7.md)

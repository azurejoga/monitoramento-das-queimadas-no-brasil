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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d4b8b6cb-8ef4-307c-8c8a-b07d26a43f38 | -14.9725 | -49.7945 | 2026-10-01 00:30:00 | GOES-19 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 852e5200-0093-3ca5-b6ba-2d33ca6fbe6e | -2.974 | -51.0247 | 2026-10-01 00:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 259fe835-e33c-3735-b0c0-1079eb6637f2 | -13.6476 | -53.9544 | 2026-10-01 00:30:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 7c3c6246-b443-3aac-af89-aeeba8323fbf | -13.6668 | -53.9522 | 2026-10-01 00:30:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 1ddacf73-36d2-3a49-bd9c-efbf6258eb7b | -9.1221 | -64.4031 | 2026-10-01 00:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 99.4 |
| 86fc0746-ff83-34b5-98b3-bfa8fa0914b1 | -14.1547 | -51.1271 | 2026-10-01 00:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 52.2 |
| ccb874cc-ea78-3865-9283-48ac122eefe4 | -11.2903 | -50.9846 | 2026-10-01 00:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 44.2 |
| 0e20b2f4-4255-3829-aba8-6879091160b1 | -3.0192 | -53.887 | 2026-10-01 00:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| e5096019-1c2e-378a-9de8-1de53253172d | -9.0046 | -65.6988 | 2026-10-01 00:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 234.8 |
| f191c355-7921-35d8-87bc-812343d8ae1a | -6.7401 | -44.1371 | 2026-10-01 00:30:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 0f516259-fa53-3e89-b88c-385bc3099f93 | -9.1407 | -64.4024 | 2026-10-01 00:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 17d3513b-ca98-3ae6-8993-5231cb2bf37b | -13.0581 | -51.2264 | 2026-10-01 00:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 341a5692-2c4a-34ef-b136-e27d64d60d63 | -9.1222 | -64.3843 | 2026-10-01 00:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 139.9 |
| b7975ef8-52fd-3f06-bca9-ed1403ce7a25 | -10.785 | -50.5493 | 2026-10-01 00:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 1140ee80-2ac8-39bc-9b64-670169ded2df | -2.908 | -54.151 | 2026-10-01 00:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| b4c2d07a-cb32-3248-a0b6-846d4a43d71e | -11.81 | -50.4999 | 2026-10-01 00:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 25.6 |
| 49a0d15f-57c4-31ae-a33b-3a46a370d2d8 | -3.1245 | -50.268 | 2026-10-01 00:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 41f5e32b-b229-3fc5-82db-a477661b6854 | -3.106 | -50.2896 | 2026-10-01 00:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 160.3 |
| 5995f7d6-bd92-3421-aa80-d5067d0eea1d | 3.2741 | -60.6294 | 2026-10-01 00:30:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 877e44a8-fd9f-3b53-a2a5-6fe813408354 | -5.7357 | -43.2682 | 2026-10-01 00:30:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 90e9df12-5ceb-31c7-8767-9457596d40a0 | -8.5554 | -66.9945 | 2026-10-01 00:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 75.0 |
| cdcfcc71-9113-3679-99e8-196e50c26f25 | -10.7661 | -50.5513 | 2026-10-01 00:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 101.9 |
| 7ed2d4e7-269f-32b1-9e6f-1f7990b09796 | -3.295 | -53.8597 | 2026-10-01 00:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 135.6 |
| c01d50a2-790b-3e05-a17f-bcbfe10976ac | -9.0045 | -65.7174 | 2026-10-01 00:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 133.0 |
| 2ee72e68-be80-3faf-8a3d-01930c68b8f8 | -13.0769 | -51.2454 | 2026-10-01 00:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 47790388-dd50-31d2-aaf0-27074de6e570 | -5.7561 | -45.1747 | 2026-10-01 00:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 78cdc4a2-a7d7-3439-a023-9d3947f50bdd | -14.174 | -51.1245 | 2026-10-01 00:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 51.0 |
| 64bcdc16-ae6a-3f6d-9a90-348fc864b7a3 | -3.5808 | -51.4832 | 2026-10-01 00:30:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 221.2 |
| bd023058-7099-3c23-b27b-bd526016e288 | -5.7544 | -43.2668 | 2026-10-01 00:30:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 52.5 |
| c014fe26-b14b-3b55-8338-8b381f40686d | -3.1756 | -51.351 | 2026-10-01 00:30:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 6275078e-d129-3c25-ba83-4a490ddd517c | -9.1408 | -64.3836 | 2026-10-01 00:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 34bf8cf6-0f94-3c7d-ae98-5ad110b90674 | -5.7376 | -45.1533 | 2026-10-01 00:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 563036ae-e60f-3690-9a1c-cd1135239e7b | -5.7563 | -45.152 | 2026-10-01 00:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 122.4 |
| fd517ba4-2d0f-3700-90fa-f37061e92079 | -10.7664 | -50.5299 | 2026-10-01 00:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 99.7 |
| c4da1685-18d9-30c7-b641-46031cc74700 | -14.9915 | -49.8135 | 2026-10-01 00:30:00 | GOES-19 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 058844e8-eb3f-39e0-b19c-11d55666a1c5 | -3.2766 | -53.8602 | 2026-10-01 00:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 40f106df-2679-38cb-9fa1-7c50295efd42 | -13.0779 | -51.1813 | 2026-10-01 00:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 47.6 |
| 4001b2f7-7f1f-304e-96fb-488707d623b8 | -3.5809 | -51.4625 | 2026-10-01 00:30:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 103.8 |
| 15a2523c-b473-3a3c-a6e6-e6f211ef63bd | -5.7542 | -43.2901 | 2026-10-01 00:30:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 50.1 |
| 949b6d98-ac12-313b-b736-b8b38786a1e3 | -12.1841 | -47.3922 | 2026-10-01 00:30:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 61.9 |
| a7751840-0c9c-38f5-92d1-819b9e07b450 | -14.4418 | -51.2597 | 2026-10-01 00:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 87.5 |
| c11a608f-1b29-3379-a148-56bbbabd7f00 | -12.8746 | -44.3357 | 2026-10-01 00:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 56.2 |
| db67439d-8f4d-32da-b51f-d83d3ed545fc | -14.4225 | -51.2624 | 2026-10-01 00:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 4d721777-67c2-3397-9683-0c2bf67409b7 | -13.6476 | -53.9544 | 2026-10-01 00:40:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 59.1 |
| aa8d1335-c089-3fb3-856a-d148394ab7c0 | -13.6668 | -53.9522 | 2026-10-01 00:40:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 7f5f8090-c75b-34b6-aee5-14d373b8fef0 | -9.0047 | -65.6801 | 2026-10-01 00:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 59190aa4-b189-319d-bf64-b885c93d9375 | -3.1061 | -50.2686 | 2026-10-01 00:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 74.3 |
| bd2e3c53-663e-3f7c-998e-5b0eb8d0a5df | -4.1667 | -48.894 | 2026-10-01 00:40:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 112.2 |
| d96deac2-318b-3e01-b7e0-588c72f1b59d | -14.4414 | -51.2812 | 2026-10-01 00:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 100.5 |
| 8150240b-0415-3133-86e7-a7051a2e9f6d | -12.8552 | -44.3389 | 2026-10-01 00:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 8c78be7b-2cb9-3eb9-a4c5-77c44bc8983c | -10.4791 | -46.7862 | 2026-10-01 00:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 86c9dbed-6984-3618-9f41-b60bd637425d | -5.7376 | -45.1533 | 2026-10-01 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 69.8 |
| f3da06e4-5327-3b7e-bc05-42e15e2df7ad | -9.1221 | -64.4031 | 2026-10-01 00:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 85.1 |
| 5d459872-c8ec-3978-8b7f-305a77afb4d2 | -8.9861 | -65.6993 | 2026-10-01 00:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 143.6 |
| 00b9f880-091d-375b-9036-38746c01294e | -8.5738 | -67.0125 | 2026-10-01 00:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 1ba8733d-3b1a-3707-97e4-b5c5fe7cd95d | -9.1222 | -64.3843 | 2026-10-01 00:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 125.9 |
| 912fa6b4-d837-3ab2-bbbd-2567adb1c692 | -14.4225 | -51.2624 | 2026-10-01 00:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 228.1 |
| ebae7bdb-8c67-3bac-98a7-3b525ca53d90 | -13.6479 | -53.9336 | 2026-10-01 00:40:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 124.1 |
| dd050579-8dc4-36b7-a907-f46fae3e0c59 | -7.1266 | -43.1714 | 2026-10-01 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 35.5 |
| 77a77c20-3266-30e1-a119-fa5eada41ee7 | -2.908 | -54.151 | 2026-10-01 00:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| e1eace45-2104-32a7-aec4-2d16b02cab6d | -3.295 | -53.8597 | 2026-10-01 00:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 135.1 |
| 733f1db8-06a2-3180-ab88-c26f75a29102 | -9.0045 | -65.7174 | 2026-10-01 00:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 150.5 |
| 570ea851-0fdb-358a-b034-e06e9b7a271e | -5.7357 | -43.2682 | 2026-10-01 00:40:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 103.2 |
| 68b0c1a8-5036-3f11-b003-71fc563465a3 | -8.986 | -65.718 | 2026-10-01 00:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 9a5650a3-b7b7-33af-9c0f-3af4c4045316 | -13.0772 | -51.224 | 2026-10-01 00:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 129.9 |
| 0ece118e-ef38-30b1-8ab3-4a7b23730b7c | -6.9317 | -59.2798 | 2026-10-01 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.8 |
| ac9c892c-89e7-306f-9f05-af1871922b7f | -13.0581 | -51.2264 | 2026-10-01 00:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 7f849498-47f6-3068-a780-bf691c944be3 | -5.7563 | -45.152 | 2026-10-01 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 132.5 |
| ba2ff3ea-7ca3-37df-8b38-83a49e20fb00 | -3.1572 | -51.3515 | 2026-10-01 00:40:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 980f31fc-caf9-3e3a-b211-201b1fd13f39 | -13.0779 | -51.1813 | 2026-10-01 00:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 66.9 |
| bee68669-0ba2-3889-ae29-93aa30b1b6a0 | -7.4223 | -64.3464 | 2026-10-01 00:40:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 56.6 |
| ce6799ab-ef42-3130-ad5f-ede07a8f0eb2 | -5.7542 | -43.2901 | 2026-10-01 00:40:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 0fe888ed-8c85-3f2d-a58f-527211eb1d31 | -5.7561 | -45.1747 | 2026-10-01 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 67.0 |
| cd108f02-8454-3df6-bb69-6a387c94dd04 | -12.1841 | -47.3922 | 2026-10-01 00:40:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 63.7 |
| a7c441d5-0591-3afa-bc94-90b765b22842 | -9.0046 | -65.6988 | 2026-10-01 00:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 224.4 |
| 63f4f45d-5295-3417-a4a1-0ba5799165c1 | -8.9862 | -65.6807 | 2026-10-01 00:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 76eb317f-7e78-3619-bbd1-7c399eb7c716 | -8.5738 | -66.994 | 2026-10-01 00:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 76.9 |
| e23b3fc5-4b8e-355e-b589-b171d8d67896 | -14.4228 | -51.2409 | 2026-10-01 00:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 96.4 |
| db005c91-1419-314e-a79c-b65a9b3f91d8 | -13.0769 | -51.2454 | 2026-10-01 00:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 4ca0f2cf-9efb-39d7-915b-9aad4f7b3bcf | -5.7544 | -43.2668 | 2026-10-01 00:40:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 38.2 |
| bead3e09-67d8-3659-8272-af3bfc5e4831 | -3.2951 | -53.8395 | 2026-10-01 00:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 6897b09a-2020-3c0a-b129-34a2b343e29f | -3.1245 | -50.289 | 2026-10-01 00:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 111.3 |
| 52cc1b83-24fa-389b-8e5f-b298bf5fefdd | -5.7355 | -43.2916 | 2026-10-01 00:40:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 151.6 |
| b65c70fb-7b39-3214-b8c5-ddfdb0f56853 | -3.106 | -50.2896 | 2026-10-01 00:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 117.8 |
| 9333f3d7-9962-3ac2-9cab-c014bc365fc2 | -8.5554 | -66.9945 | 2026-10-01 00:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 84.5 |
| a4845402-1b25-3a46-932c-519aca14c783 | -3.5624 | -51.4631 | 2026-10-01 00:40:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 8cf6245c-af32-3f3a-b6d9-3a00ef6c5693 | -13.0776 | -51.2027 | 2026-10-01 00:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 122.7 |
| e8531e2d-0e8e-3e53-96c9-c02cc36ff394 | -14.4418 | -51.2597 | 2026-10-01 00:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 217.4 |
| 4ae49c6a-c9ab-31cf-b3f3-6c42580e2ea6 | -13.0584 | -51.205 | 2026-10-01 00:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 6435b44a-fac1-307c-b998-da556d6d9963 | -5.9993 | -49.566 | 2026-10-01 00:40:00 | GOES-19 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 11e1979c-5b6d-3a43-950f-b0febe10f950 | -3.1245 | -50.268 | 2026-10-01 00:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 93.9 |
| b59012ac-01a1-3f53-8ef6-33797fa39d54 | -3.1842 | -60.0607 | 2026-10-01 00:40:00 | GOES-19 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 44.1 |
| 6e993c88-af88-39c4-bfbe-14b7bbfb93da | -6.0179 | -49.5648 | 2026-10-01 00:40:00 | GOES-19 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 84.1 |
| a1b527e1-27e5-3a13-a1de-a9032759516c | -10.7664 | -50.5299 | 2026-10-01 00:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 55.2 |
| 2afc4a1e-b884-3113-bc72-33c945666a93 | -3.5808 | -51.4832 | 2026-10-01 00:40:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 108.1 |
| 689a3217-073e-3cee-9b36-9385e8d09336 | -13.6671 | -53.9314 | 2026-10-01 00:40:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 107.8 |
| ff70e81c-7746-3e50-84c8-2084513bf0bf | -3.5623 | -51.4838 | 2026-10-01 00:40:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 156.7 |
| 874ed4a1-7762-3b7c-b6c0-324a1adbb338 | -4.1482 | -48.8948 | 2026-10-01 00:40:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 89.2 |
| 97f6f82b-94ff-37ab-98df-a99fb43e6eba | -7.1269 | -43.1479 | 2026-10-01 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 98.0 |
| 585c36a1-33f0-3bf1-9070-0d1c20ac879a | -5.9993 | -49.566 | 2026-10-01 00:50:00 | GOES-19 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |


[Clique aqui para ver as próximas entradas](README11.md)

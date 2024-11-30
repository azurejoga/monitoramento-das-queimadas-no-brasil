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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2f3aa17c-a3e0-395e-a48b-6dbd8ce3c237 | -2.63742 | -51.75441 | 2024-11-30 01:32:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 33.9 |
| 333d96f0-b2ea-32ba-a504-96fbbfc2c86c | -1.64393 | -53.87122 | 2024-11-30 01:32:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 9f26f66a-aa12-3a6b-a6b0-a87b6f09de87 | -1.19834 | -51.753 | 2024-11-30 01:32:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 18.2 |
| bd044dcd-7d56-3ef9-a067-0673bc7a8b4f | -2.90192 | -54.76918 | 2024-11-30 01:32:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 30.7 |
| f9a95b6e-8232-3257-be53-614ddaac8892 | -3.09319 | -53.72828 | 2024-11-30 01:32:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 7fd3b174-4ffc-3ebd-9c82-df6c1cfffd6c | -3.29209 | -53.83376 | 2024-11-30 01:32:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 763c5158-56e0-3ab4-9c8f-636244527a14 | 1.10325 | -59.58793 | 2024-11-30 01:32:00 | TERRA_M-M | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ac989d2f-916f-3f33-8140-2f22280fd9e8 | -1.30323 | -55.73857 | 2024-11-30 01:32:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| ad309601-8a4b-348f-818c-e45314de72a8 | -3.252 | -53.8685 | 2024-11-30 01:32:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 26.2 |
| 89f55d83-7f2d-38b5-9dcf-2711f2cf3970 | -2.01145 | -50.75803 | 2024-11-30 01:32:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 40.3 |
| 802155d8-0375-3f21-aa96-5ee8ae594a2f | -1.7189 | -52.63198 | 2024-11-30 01:32:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 52a9b3b2-59c2-323a-ab4b-3100b43561ba | -2.89554 | -54.77661 | 2024-11-30 01:32:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 056093d7-d5ae-334f-a1fb-262449ff0a56 | -2.58783 | -53.97104 | 2024-11-30 01:32:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 5f667f27-a94c-3d06-a616-01820a70028b | -1.70705 | -52.45942 | 2024-11-30 01:32:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 8b34f0bf-7fb7-38f9-a9c8-9b222e45380d | -1.36474 | -54.65583 | 2024-11-30 01:32:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| eac32974-af7d-3ec3-b0a9-f8c845b1d244 | -2.98162 | -53.27927 | 2024-11-30 01:32:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 252ab3bd-0924-3d6b-aa05-9a0dea2c1f96 | -2.98036 | -53.89719 | 2024-11-30 01:32:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 04a662da-1c9f-31c7-9f57-d6b32e1a5885 | -3.4407 | -59.27957 | 2024-11-30 01:32:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| d7ce3deb-b855-37a8-8e20-e44ab53a9d96 | -3.21481 | -54.0912 | 2024-11-30 01:32:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| ba75e386-fd6b-3fe5-ace4-b422765e98e0 | -1.0809 | -53.63745 | 2024-11-30 01:32:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 26.7 |
| 3a65a0c3-0867-3875-8701-cdc91a05b705 | -1.60445 | -52.2943 | 2024-11-30 01:32:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 813d3068-c185-37bb-904e-a6561ed23951 | 1.27767 | -55.91893 | 2024-11-30 01:32:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| fc018812-643a-313f-b68d-69a6b24d678a | -3.30315 | -53.83214 | 2024-11-30 01:32:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 85ac36ff-d4eb-38bd-8b90-869a8e0a2e1f | -3.47135 | -53.88086 | 2024-11-30 01:32:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 977d6600-4f8f-361a-9cab-993c9c0abefc | -2.86727 | -53.99796 | 2024-11-30 01:32:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| f8a02eae-17da-308c-9326-93d9ca79e8d9 | 1.98999 | -60.56227 | 2024-11-30 01:34:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f05a0eae-6c3e-3a23-8778-38cc6ad890ab | -4.8523 | -41.317 | 2024-11-30 01:40:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 116.6 |
| 893c8b2f-729d-3047-b8ff-9233403499f0 | -3.9699 | -41.5176 | 2024-11-30 01:40:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 118.1 |
| e5fc31ec-255f-3ca6-b873-dff722df9f4a | -3.4792 | -53.7941 | 2024-11-30 01:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 60159742-1a07-334f-9666-23d09882089d | -1.0022 | -51.7235 | 2024-11-30 01:40:00 | GOES-16 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 52.8 |
| ca95e632-3864-3eb7-9d16-bab61e0b7f71 | -3.6758 | -47.1176 | 2024-11-30 01:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 186.2 |
| b0aa81d0-28c3-35f0-8e4e-0fa2651edf0e | -4.8899 | -41.3143 | 2024-11-30 01:40:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 257.5 |
| 40397d18-6858-3bb6-8595-2209a119876e | -6.0674 | -48.0569 | 2024-11-30 01:40:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 3781d3c1-76cc-3c68-9c8d-f92e1506f345 | -17.6654 | -57.5645 | 2024-11-30 01:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 86.0 |
| 4b184fc6-e0ab-342f-ad01-75c1696cab23 | -3.4791 | -53.8142 | 2024-11-30 01:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 109.5 |
| 4d2048b1-69b0-334e-97a4-7d868ead01aa | -1.6938 | -46.7833 | 2024-11-30 01:40:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 118.8 |
| 2b85cac0-153e-341a-ab93-c6a3b97898c1 | -6.9156 | -43.5418 | 2024-11-30 01:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 418.0 |
| 54e7ecc6-f82f-3132-a7d7-7adbbcc800b6 | -4.8525 | -41.2928 | 2024-11-30 01:40:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 99.4 |
| 108b608a-0964-30c2-87df-61c909dea52f | -3.6757 | -47.1395 | 2024-11-30 01:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 186.0 |
| 1babdd59-66ed-3659-82bb-d538d3ce035a | -6.9153 | -43.5652 | 2024-11-30 01:40:00 | GOES-16 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 181.5 |
| 508b37a2-4b82-3da6-bfd9-3ecbd791a61a | -4.8711 | -41.3157 | 2024-11-30 01:40:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 482.0 |
| bb774f1e-2f0a-3576-b056-3ec5a9c846fa | -1.2556 | -54.5589 | 2024-11-30 01:40:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 50.0 |
| e92ec615-0d4b-3ec6-ace0-6f95c779e780 | -4.6238 | -46.9849 | 2024-11-30 01:40:00 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 120.3 |
| 09527679-2bc5-34ea-aa12-62c3818c9630 | -3.2591 | -53.6186 | 2024-11-30 01:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| e5479fda-1113-361d-912b-3d85caa28b2d | -17.6651 | -57.585 | 2024-11-30 01:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 82.0 |
| e07fa441-6860-30d2-af91-c2cd9cd24919 | -7.4991 | -34.8741 | 2024-11-30 01:40:00 | GOES-16 | CAAPORÃ | PARAÍBA | Brasil | 2503001 | 25 | 33 | nan | nan | nan | Mata Atlântica | 120.9 |
| 9a2dba28-aca6-3380-83c8-24fda20771cc | -1.6777 | -45.7868 | 2024-11-30 01:40:00 | GOES-16 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 4d078272-ba80-32a6-901a-0175b8a1c1d1 | -3.9886 | -41.5165 | 2024-11-30 01:40:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 97.3 |
| 84072867-aef3-3a64-abd5-0f70299abe27 | -6.8965 | -43.5669 | 2024-11-30 01:40:00 | GOES-16 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 61.8 |
| d0c26a9d-dec6-3c63-b2e8-f65b96db31bc | -4.8713 | -41.2915 | 2024-11-30 01:40:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 871.4 |
| a63d3980-5ab4-37ba-a0a9-1a130d596151 | -4.6052 | -46.9859 | 2024-11-30 01:40:00 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 5fa9c922-05cc-3d44-902b-a5688ff0e09b | -3.4975 | -53.8137 | 2024-11-30 01:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 92.4 |
| 5daa300a-929f-37c7-acd0-edebe5aa2cc0 | -7.4987 | -34.9017 | 2024-11-30 01:40:00 | GOES-16 | CAAPORÃ | PARAÍBA | Brasil | 2503001 | 25 | 33 | nan | nan | nan | Mata Atlântica | 107.5 |
| 264d0e89-855b-3791-af1a-492f10da07af | -4.6051 | -47.0079 | 2024-11-30 01:40:00 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 123.2 |
| 93697ae7-694c-344a-9087-c145a4e31cce | -3.6943 | -47.1168 | 2024-11-30 01:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 22f66f67-251c-34b7-aa07-7473ffc6d7eb | -6.0676 | -48.0352 | 2024-11-30 01:40:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 4fbc45df-7003-399d-93c8-1c8da82c1455 | -3.2406 | -53.6393 | 2024-11-30 01:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 77.1 |
| c2a4e3ad-50ff-3a15-a248-90230359c712 | -4.8903 | -41.266 | 2024-11-30 01:40:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 83.9 |
| 8a0537f3-65c6-39ab-991a-1c576394d5d6 | -4.8901 | -41.2902 | 2024-11-30 01:40:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 486.7 |
| 094ca611-f0b0-34fb-8ee5-9ad99c7c130f | -4.8715 | -41.2674 | 2024-11-30 01:40:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 177.1 |
| c5913f4f-42c8-39e3-b16c-546835bce459 | -2.0347 | -50.7765 | 2024-11-30 01:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| a5cfd3b0-86ee-3e98-849c-c259ff0a30b7 | -6.4474 | -35.0386 | 2024-11-30 01:40:00 | GOES-16 | BAÍA FORMOSA | RIO GRANDE DO NORTE | Brasil | 2401404 | 24 | 33 | nan | nan | nan | Mata Atlântica | 55.1 |
| 449946be-a381-3f35-bbd9-87afdbd7d685 | -6.9344 | -43.5401 | 2024-11-30 01:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 90.6 |
| d93bef7d-fcd9-3fa9-98e9-2818bfe208f8 | -2.0163 | -50.7768 | 2024-11-30 01:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 0af84f3b-9ac4-3a2f-b5a5-860e43fab7ca | -3.6942 | -47.1387 | 2024-11-30 01:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| fe067839-a311-39b3-aad7-8d0466837a0d | -3.259 | -53.6388 | 2024-11-30 01:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 137.8 |
| 21e2dbc5-862e-38ec-8391-0be61eb9dbfc | -4.6237 | -47.0069 | 2024-11-30 01:40:00 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 215.2 |
| 68147db5-b14a-3c13-ba75-cd7009d0fdf9 | -1.2739 | -54.5587 | 2024-11-30 01:40:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 23732b53-c7fb-3a29-b96d-083fb8375bfd | -6.8967 | -43.5436 | 2024-11-30 01:40:00 | GOES-16 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 133.0 |
| 02717e7a-552b-31f5-b393-13bb37c94b94 | -3.4976 | -53.7935 | 2024-11-30 01:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 22adc87e-41f7-3fd4-9d4e-ec3cab99115c | -1.6419 | -53.8731 | 2024-11-30 01:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 87209b1a-479b-3f3d-92df-829ca461b331 | -6.086 | -48.0557 | 2024-11-30 01:40:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 111.0 |
| 306820b6-ba70-3ace-82c8-6b5633bfd2ef | -1.3271 | -55.8475 | 2024-11-30 01:40:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 25186f9a-1ef1-3e8a-96e4-7e69251fe821 | -6.0862 | -48.0339 | 2024-11-30 01:40:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 145.4 |
| d53b1d9a-5555-3807-a990-40c788a9495a | -2.0163 | -50.7768 | 2024-11-30 01:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 99.9 |
| e3097e81-4cb6-3484-a718-a15dab953515 | -1.0733 | -53.6378 | 2024-11-30 01:50:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 48.7 |
| d48b7f3c-c46f-3813-a379-3bba1c59e63d | -6.0862 | -48.0339 | 2024-11-30 01:50:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 105.7 |
| b479d2b4-bbce-3063-b3ab-c424b31e6093 | -6.9153 | -43.5652 | 2024-11-30 01:50:00 | GOES-16 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 163.2 |
| 3c3b6db0-03f5-3419-905a-fdf6ea780903 | -1.0022 | -51.7235 | 2024-11-30 01:50:00 | GOES-16 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 60.9 |
| bf9729f9-7a1d-3c88-ac3b-6fd6ea92b87c | -3.2406 | -53.6393 | 2024-11-30 01:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 7560b61f-3fb5-357b-8180-638889f3306d | -4.8903 | -41.266 | 2024-11-30 01:50:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 91.8 |
| cf74d2da-d3fd-3d44-9d55-d006279d1b47 | -4.8899 | -41.3143 | 2024-11-30 01:50:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 255.5 |
| 761446f6-c1ea-34b3-8b15-f152d92343a9 | -3.4791 | -53.8142 | 2024-11-30 01:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 86.6 |
| 75ea78f4-10af-38c3-8c61-2610fefcde16 | -4.6051 | -47.0079 | 2024-11-30 01:50:00 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 66.1 |
| abb8ca8d-868c-3bde-bc81-497694295458 | -3.1481 | -53.8233 | 2024-11-30 01:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 2a680281-a633-3e8a-a595-0afef5324fb1 | -6.0674 | -48.0569 | 2024-11-30 01:50:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 4dfb3681-f77e-352d-a3d0-faf7bbd5d078 | -1.6938 | -46.7833 | 2024-11-30 01:50:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 137.5 |
| 80944364-1115-35ee-9673-a9312d163379 | -6.9344 | -43.5401 | 2024-11-30 01:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 119.1 |
| 488b6f44-7c50-32c8-9ab8-38a5f29be225 | -4.8525 | -41.2928 | 2024-11-30 01:50:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 113.1 |
| 4b6b668f-956c-312a-a156-3b94c878b362 | -4.6238 | -46.9849 | 2024-11-30 01:50:00 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 3b7848df-4c55-3b8c-ac76-524e0ba49df2 | -4.8713 | -41.2915 | 2024-11-30 01:50:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 724.3 |
| 485fff83-7b5a-3066-b9ff-45e5cf71f945 | -4.8711 | -41.3157 | 2024-11-30 01:50:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 444.9 |
| 77d1166b-3aa4-323f-a1a3-ea86df381dc3 | -6.9341 | -43.5634 | 2024-11-30 01:50:00 | GOES-16 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 3b2f7420-be8c-3944-9585-d807c545cb9a | -3.9699 | -41.5176 | 2024-11-30 01:50:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 94.2 |
| 62b6eedc-020e-3334-aa06-60976d557cbe | -6.8967 | -43.5436 | 2024-11-30 01:50:00 | GOES-16 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 140.3 |
| 719f5538-33eb-3bac-bfe6-bf163caa122b | -4.8523 | -41.317 | 2024-11-30 01:50:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 107.3 |
| 2db42f66-002a-3b69-93b7-f7f09a0fd077 | -3.2591 | -53.6186 | 2024-11-30 01:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 3868bc55-42b3-3cda-aca5-bbfc4b2272e8 | -3.259 | -53.6388 | 2024-11-30 01:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 172.4 |
| e7185be5-cfc7-3b3b-8a6a-01e8496bae25 | -4.6237 | -47.0069 | 2024-11-30 01:50:00 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 97.1 |
| 8eeeec71-c031-3212-8ced-9abebd823cb3 | -1.2556 | -54.5589 | 2024-11-30 01:50:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |


[Clique aqui para ver as próximas entradas](README10.md)

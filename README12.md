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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7c7cf51a-1092-3543-95a9-85457cd7a215 | -17.05511 | -56.74717 | 2024-09-29 01:05:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 30.1 |
| 8959792f-1ab2-3408-8d8b-439ccf660d0a | -17.05412 | -56.75249 | 2024-09-29 01:05:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 20.9 |
| ca3c2933-cccf-341a-b8ef-38beae4bc028 | -17.05244 | -56.71944 | 2024-09-29 01:05:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 22.1 |
| c3cf7ea9-f231-3497-9d07-535d9321cf72 | -17.05126 | -56.72478 | 2024-09-29 01:05:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 35.2 |
| 39715350-1276-3f74-801c-388be8388efb | -16.99361 | -56.17358 | 2024-09-29 01:05:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 31.0 |
| e5f40401-9cec-359a-9d38-f9d9eb61b97f | -16.99097 | -56.14867 | 2024-09-29 01:05:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 26.4 |
| 12b41e1c-a15d-3537-838b-82f3194de9b0 | -16.9339 | -57.93093 | 2024-09-29 01:05:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 64.6 |
| 328eb24d-a8e8-38c0-ba85-f0b0bd0316cc | -16.92664 | -57.92479 | 2024-09-29 01:05:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 99.0 |
| 087c2bf8-3b14-3eb6-9f09-5e8b4cba991a | -16.91788 | -57.93254 | 2024-09-29 01:05:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 97.0 |
| 5daa182c-c05e-3fa0-9a2a-324c8d35799a | -16.90523 | -57.96831 | 2024-09-29 01:05:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 48.5 |
| cf9d7fb9-53e8-3ca5-bd13-c39546092177 | -16.64439 | -55.23326 | 2024-09-29 01:05:00 | TERRA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 28.9 |
| 11f79382-a309-3249-9eb2-bc1712ee26ae | -16.6435 | -55.21878 | 2024-09-29 01:05:00 | TERRA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 41.7 |
| a394d14e-4350-3678-85b7-ebf19962bf73 | -16.64219 | -55.21246 | 2024-09-29 01:05:00 | TERRA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 25.9 |
| fcafafd1-737c-3dcf-b983-64c2b9f3fdb5 | -16.4824 | -57.37773 | 2024-09-29 01:05:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 18.9 |
| 00e0ba3b-cd6c-3a2d-836a-ed8d1f8ddb1b | -16.43723 | -53.95079 | 2024-09-29 01:05:00 | TERRA_M-M | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 4a75bbcc-0747-3ca9-abae-437be383f298 | -16.42558 | -53.95224 | 2024-09-29 01:05:00 | TERRA_M-M | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 10.2 |
| bcf580d1-9be9-3ee2-aab6-436c4f7e0114 | -15.93874 | -57.20608 | 2024-09-29 01:05:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 16.8 |
| bf705d10-12d7-3065-a190-96835ec338aa | -15.92365 | -57.2065 | 2024-09-29 01:05:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 18.1 |
| ad48a6b4-4df5-36ae-8d64-719493b9e331 | -15.92296 | -57.20025 | 2024-09-29 01:05:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 25.1 |
| b00a8835-3988-367a-bd7d-ba078778460d | -15.92083 | -57.17951 | 2024-09-29 01:05:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 944a9dd8-af32-3041-a200-2ee434568555 | -15.81975 | -57.36961 | 2024-09-29 01:05:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 34.1 |
| 900e8e45-1830-3b63-9ae9-f21c826cacd9 | -15.78271 | -54.19553 | 2024-09-29 01:05:00 | TERRA_M-M | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 53.1 |
| 17e91a76-0248-307e-ac49-e038cdbe068c | -15.78071 | -54.17871 | 2024-09-29 01:05:00 | TERRA_M-M | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 425e6215-333a-3f83-8499-55fdcad9bab3 | -15.62105 | -57.4984 | 2024-09-29 01:05:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 84e21cf8-cbec-35a9-a865-83c46df4c41f | -15.62024 | -57.47478 | 2024-09-29 01:05:00 | TERRA_M-M | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 5a74839c-f37a-3127-b0ab-e99457412d5b | -15.61806 | -57.46849 | 2024-09-29 01:05:00 | TERRA_M-M | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 5ff58dba-673d-359a-8050-001b81137d3a | -15.60505 | -57.47645 | 2024-09-29 01:05:00 | TERRA_M-M | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 37.9 |
| 90e695ae-9bcb-32d3-a8f8-af898129d97d | -15.60287 | -57.47022 | 2024-09-29 01:05:00 | TERRA_M-M | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 43.4 |
| 7f0ec33c-b514-3f8b-88df-7d57d6d9c588 | -15.59293 | -57.50756 | 2024-09-29 01:05:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 29.1 |
| af9febf6-6f03-3759-8a7d-dea8e285a026 | -15.59056 | -57.50145 | 2024-09-29 01:05:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 29.6 |
| 92a17d49-5b96-3f12-b336-476715ef9a53 | -13.70209 | -50.93896 | 2024-09-29 01:05:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 90f3cb02-b00a-3117-9225-10d315ac2b63 | -13.2505 | -51.28568 | 2024-09-29 01:05:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 95e750ec-8d86-3aa7-adcc-41d7f851c385 | -13.24119 | -51.28699 | 2024-09-29 01:05:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 27.2 |
| e75f828b-eb99-382e-9957-aa87ee29de99 | -13.23989 | -51.27694 | 2024-09-29 01:05:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 85aa4287-c771-3ad7-ae0d-3ce8ec7d41d0 | -13.23416 | -51.28418 | 2024-09-29 01:05:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 36.2 |
| 541804fe-c4ce-3915-9342-c99e49c8a8f2 | -13.19828 | -51.22808 | 2024-09-29 01:05:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 17.1 |
| fbc66815-e8f8-36b1-95d0-042ce26f12f0 | -13.17123 | -48.55106 | 2024-09-29 01:05:00 | TERRA_M-M | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| bf32ad48-b461-33b7-9ce2-0365faad40ca | -13.03334 | -48.62153 | 2024-09-29 01:05:00 | TERRA_M-M | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 3afe8e73-35c7-3232-9876-d71405bfe202 | -13.03206 | -48.61253 | 2024-09-29 01:05:00 | TERRA_M-M | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 6ffd09f8-3358-3e4f-ba7c-68278f8f207a | -13.03075 | -48.60329 | 2024-09-29 01:05:00 | TERRA_M-M | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 2814b768-c16d-3b6d-869e-a52461053433 | -13.02444 | -48.62287 | 2024-09-29 01:05:00 | TERRA_M-M | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 2638a22e-ece2-34d9-9427-1c59a6ba3e6e | -12.88105 | -51.19961 | 2024-09-29 01:05:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| b80d467c-0de9-3590-9816-79090373fc65 | -12.86534 | -51.15167 | 2024-09-29 01:05:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 019094fb-4c6a-323a-8131-9fa66b818d4c | -10.53991 | -51.0928 | 2024-09-29 01:07:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 05efcc15-60dc-3714-b838-f9d933ee70ba | -10.49208 | -51.14707 | 2024-09-29 01:07:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 7050bf9f-87ec-34a1-b78a-f78d81e48f09 | -10.49083 | -51.13779 | 2024-09-29 01:07:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| b2815da2-30ff-3910-915e-db16d1a63ffa | -10.45461 | -50.80378 | 2024-09-29 01:07:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 891c48b3-a9b2-3ef4-86cf-6034790ac77c | -10.45336 | -50.79463 | 2024-09-29 01:07:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 7e6d380f-b4cc-3086-b3f3-7c0dd22a27fe | -10.13354 | -50.00745 | 2024-09-29 01:07:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ac1ae6e8-1091-3086-980f-f82853c902b3 | -10.10472 | -50.00875 | 2024-09-29 01:07:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 24.6 |
| 806e8d40-56e1-3f9d-9183-37b40810dbdf | -9.28908 | -43.49889 | 2024-09-29 01:07:00 | TERRA_M-M | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 40.2 |
| 4f74b797-bf90-3afc-bec2-fb5ea36cb9e5 | -8.91389 | -45.66942 | 2024-09-29 01:07:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 52.2 |
| 34f297b5-d2cf-3838-bcfb-1ea043b84961 | -8.91173 | -45.65505 | 2024-09-29 01:07:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 10.4 |
| b4869f7f-12ee-3923-9f67-265b1953b604 | -8.76917 | -45.17724 | 2024-09-29 01:07:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 5bd5a548-2ac2-3daa-97ee-597cd8bca4fd | -8.7149 | -44.01807 | 2024-09-29 01:07:00 | TERRA_M-M | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 15.9 |
| e877aea8-e1dd-3f43-b42d-76976f002b70 | -8.55595 | -45.50627 | 2024-09-29 01:07:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| f64f092b-9e07-34ed-b76b-265230721795 | -8.55365 | -45.4915 | 2024-09-29 01:07:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 7415bd46-7fa9-309c-bd0f-5bbc8efae54f | -8.51191 | -44.71672 | 2024-09-29 01:07:00 | TERRA_M-M | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 8d800070-142d-3e06-90fb-e57f3a3a97e0 | -7.86346 | -44.61416 | 2024-09-29 01:07:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 28.9 |
| 5f4893e6-a6ed-31bc-8d9a-b45783b5b4fb | -7.86062 | -44.59615 | 2024-09-29 01:07:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 42.4 |
| 1d3afab4-bbde-34d6-8a4f-326783e61d49 | -7.85717 | -44.60351 | 2024-09-29 01:07:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 46.5 |
| 1728677b-50ee-3d6e-9c7f-f1c4e6c3cc86 | -7.84846 | -44.59824 | 2024-09-29 01:07:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 4f053cb8-c7d7-3c02-873c-222cb8bd9835 | -7.84562 | -44.58038 | 2024-09-29 01:07:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 51.9 |
| 1c9cc1c1-0e1c-3b12-92db-084c022b2d86 | -7.84228 | -44.58757 | 2024-09-29 01:07:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 193.0 |
| 038a02ba-6468-3beb-9ea3-d380e6c2eabb | -7.83957 | -44.56967 | 2024-09-29 01:07:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 21.5 |
| db8d03bb-696d-363e-be5d-b226ceea15cd | -7.83885 | -45.48489 | 2024-09-29 01:07:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 40.5 |
| b2d25946-14b6-342e-a522-de26a196e9c2 | -7.83651 | -45.46964 | 2024-09-29 01:07:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 48.8 |
| 8765ab9d-61d4-3022-b168-9fd3389a728f | -7.83629 | -44.60022 | 2024-09-29 01:07:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 40feb886-bb59-36ab-b2af-0e7104b65e52 | -7.83341 | -44.58223 | 2024-09-29 01:07:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 246.5 |
| 8d6eaee5-5ad8-374d-b335-b7435ba2f9ef | -7.83007 | -44.58943 | 2024-09-29 01:07:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 0f8636a3-da10-35d2-85f8-b3c7e544065b | -7.82731 | -44.57134 | 2024-09-29 01:07:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 42.6 |
| 21f7f37d-ed37-360c-bf9a-2cd32d544ed3 | -7.59554 | -45.09984 | 2024-09-29 01:07:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 4d5c12fa-f651-3ecd-bd25-4ec75f4d9b5a | -7.59296 | -45.08308 | 2024-09-29 01:07:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 207.4 |
| 204ee97a-f289-3e05-bb60-48f34fc53941 | -7.59042 | -45.06655 | 2024-09-29 01:07:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 5e3dcc4b-71c4-3d85-9625-d6ea2341c3c6 | -7.58124 | -45.08527 | 2024-09-29 01:07:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 79df7c88-b1f7-33e5-ac5d-fa000d8ef791 | -7.57869 | -45.06878 | 2024-09-29 01:07:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 9d384352-8be2-3b39-acc7-6b2905eed676 | -7.57356 | -45.03571 | 2024-09-29 01:07:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 6e3e776b-865d-3f55-a894-343e5292ce54 | -5.01065 | -43.829 | 2024-09-29 01:07:00 | TERRA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 8fe43cb0-73b7-3b79-9b9a-d0c84f225bc9 | -5.00713 | -43.80606 | 2024-09-29 01:07:00 | TERRA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 148.3 |
| 969afd0a-843c-3670-97bf-ef7dc2108706 | -4.99696 | -43.83098 | 2024-09-29 01:07:00 | TERRA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 38.8 |
| 5db13648-0348-37a4-b475-17bb1d2aa8f1 | -4.99342 | -43.80815 | 2024-09-29 01:07:00 | TERRA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 21.2 |
| b758611c-b36e-3d9d-80ef-b937bd1a87bf | -4.14171 | -43.7309 | 2024-09-29 01:07:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 29.5 |
| 3279631b-21f7-320e-a432-08b5fe0b6486 | -3.96112 | -41.51624 | 2024-09-29 01:07:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 91.9 |
| 58975d61-8e65-3209-8be7-705a7cbb897b | -3.95626 | -41.52216 | 2024-09-29 01:07:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 185.3 |
| b8c1b84c-13d0-39f4-8ede-89d0d257a90c | -3.95533 | -41.47998 | 2024-09-29 01:07:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 62.5 |
| cb61b2a2-4c2a-303e-9076-c6e873de2180 | -3.95071 | -41.48588 | 2024-09-29 01:07:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 95.7 |
| 6de1d502-bb21-3d3c-b851-38eb0413ae59 | -3.94444 | -41.51859 | 2024-09-29 01:07:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 157.1 |
| ae99bfed-fe9c-38ca-9fb5-6e51de836bb6 | -3.80219 | -41.59695 | 2024-09-29 01:07:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 49.4 |
| 5784fcc2-1130-343a-8502-7876852da880 | -3.79088 | -41.59365 | 2024-09-29 01:07:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 39.2 |
| 4ad1fa10-7482-3a99-af1e-034d97137af0 | -9.89027 | -47.41394 | 2024-09-29 01:07:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 17.5 |
| df314e10-bf6c-36c7-8c36-86fea5362e74 | -9.88069 | -47.41545 | 2024-09-29 01:07:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| c95d07dd-fd3a-35a7-9c4e-42f02edf9e46 | -9.77444 | -50.07482 | 2024-09-29 01:07:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4e7f7b49-642d-3054-b893-9cbbe32dcebe | -9.74584 | -50.67587 | 2024-09-29 01:07:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8b0d0cc3-055a-3a59-aa69-5070894c62d0 | -9.74459 | -50.66685 | 2024-09-29 01:07:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7339a938-816f-3684-985a-9137964fbb53 | -9.74089 | -50.43243 | 2024-09-29 01:07:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| b5a8e830-0f1f-361d-bf40-1df796a70783 | -9.73965 | -50.42348 | 2024-09-29 01:07:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f274290a-6c31-3a06-b803-c1ba2eb36f2f | -9.60063 | -50.08494 | 2024-09-29 01:07:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 5d20f8a0-3523-343c-8030-737d07bc73f6 | -9.59938 | -50.07602 | 2024-09-29 01:07:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 55c443b0-c1f4-313b-bdcd-c85473b82928 | -9.57911 | -50.20358 | 2024-09-29 01:07:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 22.9 |
| 088210ee-ca11-35e8-a6ba-50be524f1ecb | -9.57786 | -50.19466 | 2024-09-29 01:07:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 28.5 |


[Clique aqui para ver as próximas entradas](README13.md)

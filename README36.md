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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8d04c7a5-2f4f-37c4-8884-d389aff8fd83 | -18.214 | -56.6289 | 2024-10-14 04:06:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 62.6 |
| f37a8d5b-501e-3783-ac4c-49916ba20250 | -18.2144 | -56.6081 | 2024-10-14 04:06:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 174.3 |
| 86fe786d-6193-3c4a-99a4-8ddada4b95c8 | -18.2147 | -56.5873 | 2024-10-14 04:06:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 90.0 |
| 038e0c76-bf3a-3360-bc72-6bea9c6379af | -18.2338 | -56.6263 | 2024-10-14 04:06:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 89.2 |
| 082c1309-9037-39da-96e9-0e67f36f8f3d | -18.2342 | -56.6055 | 2024-10-14 04:06:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 295.9 |
| 4d292108-b2df-38e7-b4c2-446929271875 | -18.2346 | -56.5847 | 2024-10-14 04:06:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 125.2 |
| a0feb290-e051-3fdb-a113-a3b0c34e6879 | -2.6118 | -49.0985 | 2024-10-14 04:15:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 37.5 |
| 5182d780-1f75-3307-b08a-b347dd513211 | -2.6119 | -49.0772 | 2024-10-14 04:15:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 28.4 |
| b8d7e977-8745-318b-937f-ddeb9c4c378a | -3.1792 | -50.4551 | 2024-10-14 04:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 20.9 |
| 6a60fb32-4b87-3128-98ac-9e6a4e376b78 | -3.2889 | -42.8561 | 2024-10-14 04:15:25 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 53.9 |
| a47a5d87-467c-3262-b92e-4c35104a8373 | -3.289 | -42.8327 | 2024-10-14 04:15:25 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 75.2 |
| fcc77d86-80fc-3bd2-9842-47ca0d493ae5 | -3.3076 | -42.8553 | 2024-10-14 04:15:25 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 46b42007-35ef-3ade-80d5-8974890d833c | -3.3077 | -42.8318 | 2024-10-14 04:15:25 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 133.1 |
| 55fe9e3d-d953-31f4-a5bd-eb3662ada214 | -4.1148 | -48.2515 | 2024-10-14 04:15:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 07d04895-5ef0-30ba-8442-f177a246edc7 | -4.1149 | -48.2299 | 2024-10-14 04:15:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 83.4 |
| fdf31616-3e2f-3a28-84f4-75193319e066 | -4.3565 | -55.1291 | 2024-10-14 04:15:31 | GOES-16 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 25.7 |
| af1cf653-57a8-3759-b23d-50b670e24145 | -7.9418 | -63.6365 | 2024-10-14 04:15:52 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 46.2 |
| f1d4cfbc-8a3d-3189-81fd-af90602808d1 | -10.0619 | -44.2624 | 2024-10-14 04:16:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 267.3 |
| 29ff29a5-fc38-3fe8-81e7-3896f87a1f56 | -10.0622 | -44.2391 | 2024-10-14 04:16:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 158.1 |
| c0bfd04f-f374-352e-98aa-620da3696fe9 | -10.0809 | -44.2599 | 2024-10-14 04:16:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 356.1 |
| 8adcb20a-87f2-3e18-9f88-ae05d8c38b98 | -10.0813 | -44.2366 | 2024-10-14 04:16:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 211.2 |
| 78f6967c-59d7-3e8a-821a-8c5618b4b360 | -12.3804 | -53.1376 | 2024-10-14 04:16:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 27b7a9e6-dd4d-3dac-92e1-f1368b91f6a1 | -12.3807 | -53.1167 | 2024-10-14 04:16:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 93.2 |
| 1ae67e9f-6bd9-30fa-8bdf-9f9f32398037 | -12.3994 | -53.1355 | 2024-10-14 04:16:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 5a89b97b-cd47-3ac5-b0ef-f59a09625593 | -12.3997 | -53.1147 | 2024-10-14 04:16:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 999059db-cad6-325c-9329-746a4953aea6 | -17.02 | -57.4153 | 2024-10-14 04:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 74.9 |
| e3256016-e5fa-3664-9008-cdbe14106dfa | -17.0197 | -57.4358 | 2024-10-14 04:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 76.5 |
| 37f7840f-e353-3786-b8f3-03d9b2aa40a9 | -17.0001 | -57.4381 | 2024-10-14 04:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 52.0 |
| 246cc4a1-b98e-3df0-9d64-95d227087aef | -17.0004 | -57.4176 | 2024-10-14 04:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 76.7 |
| 9f85d420-33fa-3b96-8ca0-7f24ccc1c578 | -17.196 | -57.4357 | 2024-10-14 04:16:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 58.6 |
| 72db3fd1-d10d-3205-a58e-d009a62aae3e | -17.1957 | -57.4562 | 2024-10-14 04:16:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 61.7 |
| 7e49c15b-7a78-33d7-8259-e3d54d4b5aa9 | -17.6876 | -56.2409 | 2024-10-14 04:16:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 56.7 |
| 2f3db791-0830-315e-b304-938fdd17bf45 | -18.1905 | -56.8394 | 2024-10-14 04:16:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 50.6 |
| 4128dd58-5a6e-38a1-b644-f21cb8272933 | -18.2346 | -56.5847 | 2024-10-14 04:16:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 97.4 |
| 9b7e359d-956c-3c37-9788-e3a78a9f3f6c | -18.2342 | -56.6055 | 2024-10-14 04:16:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 203.4 |
| 951646dd-e71f-3e25-b095-da30551b0d4b | -18.2338 | -56.6263 | 2024-10-14 04:16:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 72.6 |
| 5f103989-fd4b-3886-8e0e-e68c273e36e8 | -18.2147 | -56.5873 | 2024-10-14 04:16:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 77.3 |
| 013c532f-865d-389c-b5b1-469878ab071a | -18.2144 | -56.6081 | 2024-10-14 04:16:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 116.1 |
| 1dc06c51-12e6-36fb-8152-1f11d5479d8a | -18.214 | -56.6289 | 2024-10-14 04:16:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 50.6 |
| b77dd2c3-2a81-3b45-a8c1-1b03ab0a8d08 | 3.34754 | -51.30573 | 2024-10-14 04:17:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7b1e723d-4b6d-3a6a-b48d-69f643e05873 | 3.48875 | -51.49785 | 2024-10-14 04:17:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cfbd93bb-5022-3600-b9e5-1f415cfadac6 | 3.36907 | -51.34172 | 2024-10-14 04:17:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5f75d496-4869-32a7-96ee-a87a7dcfaf42 | 3.35374 | -51.31139 | 2024-10-14 04:17:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1b8f142d-44cf-3343-a4a6-4718adbda4f6 | 3.34929 | -51.3129 | 2024-10-14 04:17:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e1366312-b806-308b-a630-fcd6c2deeed0 | 3.34883 | -51.30969 | 2024-10-14 04:17:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6e9c78cf-ad14-3882-9348-4911fed8d577 | 3.34851 | -51.31212 | 2024-10-14 04:17:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 810c0baa-2f42-3b09-a6c3-9cc78586659f | 3.34837 | -51.30648 | 2024-10-14 04:17:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3403e2c2-64fb-3ca7-85b8-0bcc981a4068 | 3.34803 | -51.30893 | 2024-10-14 04:17:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 292f9be8-de40-39c7-9656-03d9dcb266c0 | -8.04567 | -44.81796 | 2024-10-14 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9d842bf4-976e-3536-9a3b-f8ce983a8233 | -8.04183 | -44.82092 | 2024-10-14 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c9b9204e-5b8b-3fbc-8f63-1050d5f83b90 | -8.04129 | -44.82438 | 2024-10-14 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4ad11d82-d99d-31ff-92b2-b0907959d9b0 | -8.03745 | -44.82732 | 2024-10-14 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| aa086907-0925-3466-9aa9-d7b4e1820252 | -7.96005 | -44.49496 | 2024-10-14 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b29abac9-e5fe-3346-85cf-23ade6e1769d | -7.95674 | -44.49446 | 2024-10-14 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 22145f21-2dc9-3219-b86a-879514e1a656 | -7.9485 | -44.50382 | 2024-10-14 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ba5b09b3-d6c2-3c0f-9681-3db4c94d0b26 | -7.79011 | -45.20929 | 2024-10-14 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2bfcb9d8-ca48-303b-9bf7-6f633c7528de | -7.76535 | -44.5427 | 2024-10-14 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0c798dba-02e5-3452-876a-54989b140942 | -7.76204 | -44.54218 | 2024-10-14 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 65112f0b-0137-3fba-ab35-0f99308982ab | -7.76151 | -44.54564 | 2024-10-14 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 86d4a11e-19ee-3763-8922-7dc5a9afd624 | -7.64917 | -44.67642 | 2024-10-14 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 35b41ab6-7e47-3559-a2bf-33f2dddb6081 | -7.64863 | -44.67988 | 2024-10-14 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6021983a-8860-3d8b-bd36-2579b0fd8828 | -7.64587 | -44.6759 | 2024-10-14 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4ef488a7-9d67-39de-8927-4026ad529dda | -7.64203 | -44.67884 | 2024-10-14 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 889799d2-82e9-310b-93ae-9c7aba94c8ac | -7.64149 | -44.6823 | 2024-10-14 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ac6419d0-bbd1-3d0c-ae90-ca4db3a721cc | -7.62169 | -44.6792 | 2024-10-14 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 51104af7-7459-3756-bf58-0a90d8c1d5f9 | -7.62125 | -44.06979 | 2024-10-14 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3815896b-2167-3f5f-86f4-22bc12d3966f | -7.62071 | -44.0733 | 2024-10-14 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ce157a7b-671b-34b6-98cd-659c818bb7a1 | -8.12777 | -43.67542 | 2024-10-14 04:19:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a73dacad-b08d-32c9-94af-20b3c6d8bf39 | -6.41909 | -43.22222 | 2024-10-14 04:19:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f32c61ff-b2c4-301b-a8bb-6c94cb14befe | -6.41738 | -43.21088 | 2024-10-14 04:19:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4ff56aac-4a1f-323b-8235-e5a2cb9d2d6a | -6.41628 | -43.2181 | 2024-10-14 04:19:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f82b7daf-ff84-3268-8b95-1030c6049c88 | -6.41402 | -43.21038 | 2024-10-14 04:19:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ba473fc8-ae90-3afe-93dc-500de341257c | -6.23604 | -43.48275 | 2024-10-14 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| faf9ea38-4391-3798-b3a4-f922267b50a6 | -6.21914 | -43.39686 | 2024-10-14 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d0bda149-beae-36da-b3c3-e9df5fe9d3a6 | -6.22835 | -43.51066 | 2024-10-14 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 76ebdf9c-69c8-35e0-9ded-6e3a4fc9e77e | -6.22672 | -43.52121 | 2024-10-14 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7a8d2ad2-8676-3959-9006-f292b5098d84 | -6.21762 | -43.51652 | 2024-10-14 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1fc94fa1-db46-34b6-a1fe-694489a545b6 | -3.70975 | -42.9291 | 2024-10-14 04:19:00 | NOAA-21 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 764673bc-7357-31da-ad95-998c62a7feaa | -3.93395 | -43.15106 | 2024-10-14 04:19:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6ead6ccf-5c25-32f9-bdc8-4f862a5426df | -3.93117 | -43.14705 | 2024-10-14 04:19:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f081d987-bebf-3ca8-9b39-4459e48892a3 | -3.93062 | -43.15055 | 2024-10-14 04:19:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 118a8ee2-51fb-36c0-80ad-6d51e890e018 | -3.92839 | -43.14304 | 2024-10-14 04:19:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| bac043f9-ba9a-31a5-a020-978c016d8a43 | -3.92784 | -43.14654 | 2024-10-14 04:19:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b6fd8ed2-0d0b-354e-a5a3-1eeceff701b8 | -3.92451 | -43.14602 | 2024-10-14 04:19:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| dc63542b-1f5b-3cb7-becc-5ce62dbb971e | -3.92119 | -43.1455 | 2024-10-14 04:19:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 83410d49-bd32-3ba0-941f-f17a9d28a008 | -7.47253 | -44.08615 | 2024-10-14 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 64e77ef7-0b8e-3c6f-b97e-33249fd3b2c8 | -7.47145 | -44.09315 | 2024-10-14 04:19:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 826e232f-2923-3654-a52f-699ff6778ab4 | -7.34833 | -44.33772 | 2024-10-14 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dacc8471-c154-35de-a97d-a70ed4244bfa | -7.34725 | -44.34465 | 2024-10-14 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 28d54a19-24b8-323f-a237-a918dc83e44d | -7.34388 | -44.32279 | 2024-10-14 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5e1b735b-bdaf-37ae-b05b-7d7630c1266a | -7.34333 | -44.32627 | 2024-10-14 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6f8ee14b-91aa-33b1-a168-cd575a8635ce | -7.34057 | -44.32227 | 2024-10-14 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| faf5f735-3d9c-3179-a899-a7096b7becd5 | -7.33767 | -44.27546 | 2024-10-14 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6c338487-f342-3fc9-b8ad-1d3e6f47609a | -6.90739 | -43.49515 | 2024-10-14 04:19:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f094179c-bb8f-3d07-958d-beeb8f601770 | -6.90684 | -43.49872 | 2024-10-14 04:19:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a3299dcc-e65f-32e3-b8e3-7b9eb1519281 | -6.90404 | -43.49463 | 2024-10-14 04:19:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e7f65a06-c05c-3a59-a881-6811f68bbbd9 | -6.90349 | -43.49821 | 2024-10-14 04:19:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 42be444a-8a3c-3352-a4ff-876d7ef0bcf9 | -6.90294 | -43.50177 | 2024-10-14 04:19:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3e9c5fed-1958-33e1-a88e-2d3fd98e2b9f | -7.24006 | -44.35616 | 2024-10-14 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4fe362ac-2e54-3ade-b30e-cf4cd6f41f52 | -7.14821 | -43.87362 | 2024-10-14 04:19:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README37.md)

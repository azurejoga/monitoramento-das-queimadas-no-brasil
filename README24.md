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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 844e2dbd-488d-3813-9ab4-7e17672cce26 | -12.8202 | -50.5495 | 2024-10-05 01:36:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 95424f94-bc81-300c-8246-abde1a816a18 | -15.5791 | -57.4532 | 2024-10-05 01:36:34 | GOES-16 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 97.9 |
| cc784876-3b28-32c9-8223-fba2c5d03067 | -15.7151 | -57.4184 | 2024-10-05 01:36:35 | GOES-16 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 7eb61a22-ace0-3b04-9374-706a9c45381a | -16.0938 | -50.2543 | 2024-10-05 01:36:36 | GOES-16 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 91.1 |
| b9780c90-03e6-34d1-a0d2-767f7ee160d9 | -16.0942 | -50.2323 | 2024-10-05 01:36:36 | GOES-16 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 152.3 |
| 08910398-fbc5-3c9c-8251-b0ef037b3f79 | -16.1134 | -50.2511 | 2024-10-05 01:36:36 | GOES-16 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 53.4 |
| c669f79c-47e1-3043-8ea3-dfee5733cb2f | -16.1138 | -50.2291 | 2024-10-05 01:36:36 | GOES-16 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 67.6 |
| e1cbe0b3-e844-3f2b-a6ad-d848e61f9e71 | -16.4155 | -57.3619 | 2024-10-05 01:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 91.3 |
| 31bef7c8-0fd1-3574-9767-58e28aee4391 | -16.554 | -57.2237 | 2024-10-05 01:36:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 231.7 |
| ca0c8edf-4045-3042-a885-0b70b1abe891 | -16.5544 | -57.2032 | 2024-10-05 01:36:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 133.1 |
| af2d65e3-b6a6-3c11-8db2-5e2d841cc5da | -16.5547 | -57.1828 | 2024-10-05 01:36:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 102.6 |
| 6262bd03-4168-38f5-8c15-503cacc348da | -16.555 | -57.1623 | 2024-10-05 01:36:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 100.8 |
| 7dea78e2-d76c-319d-9ef1-c121d9ba2284 | -16.5742 | -57.1805 | 2024-10-05 01:36:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 328.7 |
| 9702577d-db2b-38f9-8e57-15873f73c532 | -16.5745 | -57.16 | 2024-10-05 01:36:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 327.3 |
| 774a6fd0-0424-3a20-b019-e4a00a3c4c46 | -16.7647 | -57.4856 | 2024-10-05 01:36:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 156.5 |
| 03afbca9-8312-3ae5-9fc8-f2412eba67a8 | -16.6402 | -55.5243 | 2024-10-05 01:36:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 78.5 |
| 1a0934ab-015a-3258-9723-8cc99c3bb216 | -16.6594 | -55.5427 | 2024-10-05 01:36:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 86.5 |
| 4dc35f77-9ce6-303a-a5a7-577c7af104b0 | -16.6598 | -55.5219 | 2024-10-05 01:36:40 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 84.4 |
| dcba57c4-0698-38fc-b637-fec07beb3273 | -16.6871 | -57.4536 | 2024-10-05 01:36:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 99.8 |
| c99029e7-ee61-339d-8712-8b0de0477bee | -16.7843 | -57.4834 | 2024-10-05 01:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 114.5 |
| 6cbb8558-e981-370e-852f-6bba4de86de7 | -17.0888 | -56.7915 | 2024-10-05 01:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 97.1 |
| 9c2ac169-f608-3974-b4ec-c929cb977403 | -17.0892 | -56.7709 | 2024-10-05 01:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 107.1 |
| 00126d60-7a1f-3d89-bdec-dd2aa81cb06a | -17.1085 | -56.7892 | 2024-10-05 01:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 90.1 |
| 43e038c7-e568-3102-8b16-66eaed8c4089 | -17.1178 | -57.4244 | 2024-10-05 01:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 143.8 |
| 13f5ef4a-aadc-387f-be2a-4a49f69c67f7 | -17.1182 | -57.4039 | 2024-10-05 01:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 197.0 |
| 15c0b08d-0a83-310e-992c-2dffe55c30bd | -17.1185 | -57.3834 | 2024-10-05 01:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 97.0 |
| cb797ce2-6f6b-3fdc-b728-9f93ec07082c | -17.1375 | -57.4221 | 2024-10-05 01:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 168.3 |
| 491bdfb6-4a17-3549-a343-2f5382fd05c9 | -17.1378 | -57.4016 | 2024-10-05 01:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 219.9 |
| e1fa6a89-0af8-317d-96bf-a3a74fc0e767 | -17.1381 | -57.381 | 2024-10-05 01:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 94.4 |
| 324d3732-d210-3762-a982-752f03a01544 | -18.8809 | -43.6032 | 2024-10-05 01:36:50 | GOES-16 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 94.8 |
| 369436b6-e9af-3773-b83b-ee0224e88f7f | -18.8816 | -43.5785 | 2024-10-05 01:36:50 | GOES-16 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 76.5 |
| 347d9a79-293e-3589-a3b3-897b5bad369a | -18.6582 | -57.2967 | 2024-10-05 01:36:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 76.3 |
| 78dab858-90ec-350e-8b72-6f1268c3ba3d | -18.6586 | -57.2759 | 2024-10-05 01:36:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 107.3 |
| 28c10de6-2ef4-37fc-b834-dc97b70d2abe | -18.6782 | -57.2941 | 2024-10-05 01:36:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 99.5 |
| 41d7a103-725e-384a-bf5a-4c85785a3491 | -18.6785 | -57.2734 | 2024-10-05 01:36:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 143.3 |
| f24fd839-6c62-3861-ae3d-6583ab44d039 | -1.0626 | -47.9269 | 2024-10-05 01:45:12 | GOES-16 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 17417cb5-a75f-3b97-b157-cb5269d60122 | -2.8829 | -50.7147 | 2024-10-05 01:45:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| d1ee9faa-8693-311f-b6fe-4602ebd4ed28 | -2.9014 | -50.7142 | 2024-10-05 01:45:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 83.4 |
| a5c2cd6f-98dd-3939-a0b7-667cc4c22219 | -3.1432 | -50.2254 | 2024-10-05 01:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 42.9 |
| b4a0ad4e-28bc-337b-b928-3a28774ca581 | -3.2349 | -50.3695 | 2024-10-05 01:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| ccac3604-c010-3359-973f-fef4dd1acd7f | -3.2899 | -50.4516 | 2024-10-05 01:45:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 9152cd8c-af81-3af6-af89-0a90ee433b0a | -3.3083 | -50.4719 | 2024-10-05 01:45:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 78.4 |
| eaedb430-85ef-3c96-ba8f-f7580d107f1d | -3.3084 | -50.451 | 2024-10-05 01:45:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 88.7 |
| 72cc7f28-7bb7-30f2-b019-58753e1d053b | -3.3269 | -50.4504 | 2024-10-05 01:45:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 0a4397f3-0397-3079-b3ea-06f3f36b7600 | -3.618 | -47.5352 | 2024-10-05 01:45:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 3c87ded3-dfc9-3c64-a3b9-f97e6f24ab7b | -3.6181 | -47.5134 | 2024-10-05 01:45:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 88.6 |
| ace5febb-9060-3897-9452-6c1507bb682a | -4.0148 | -43.2408 | 2024-10-05 01:45:29 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 4737b2bd-0705-3a85-8c27-9ad90bcb490b | -4.9451 | -43.7888 | 2024-10-05 01:45:34 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 61.4 |
| f7c08eab-2bd2-3bcd-8de6-761d46ececf4 | -4.9452 | -43.7657 | 2024-10-05 01:45:34 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 2960ff9d-a680-3796-82c1-91c1685a7683 | -5.8214 | -44.1426 | 2024-10-05 01:45:39 | GOES-16 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 10f35b0d-9c6f-38b6-b797-efbdc8eff966 | -5.8216 | -44.1196 | 2024-10-05 01:45:39 | GOES-16 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 127.7 |
| 038eac3e-bd47-3204-b255-df214eb786a4 | -5.897 | -53.4365 | 2024-10-05 01:45:40 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 47.1 |
| ce62c101-b9dd-3bc4-a228-72d6911dd874 | -7.7364 | -49.2082 | 2024-10-05 01:45:50 | GOES-16 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 678eba82-8215-3f10-bada-110dab86dcb0 | -7.7549 | -49.2282 | 2024-10-05 01:45:50 | GOES-16 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 93cb6b51-f1cf-3a2c-b086-7980452ed821 | -7.7551 | -49.2067 | 2024-10-05 01:45:50 | GOES-16 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 20ebe002-f17f-3ea8-abd2-42d63a6ce873 | -8.7655 | -44.8106 | 2024-10-05 01:45:55 | GOES-16 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 39.1 |
| 35ce3231-4fde-3eeb-8bbe-3c89f90118f7 | -8.7769 | -49.9763 | 2024-10-05 01:45:56 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 44.1 |
| d50dd639-19ec-3b15-9c5b-80424562f8b7 | -8.7772 | -49.955 | 2024-10-05 01:45:56 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 7d5d4c33-16e1-37df-94b6-6bca4be99492 | -8.7957 | -49.9747 | 2024-10-05 01:45:56 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| c181ee9e-ca1a-3e5b-aeb4-27b2a02d6130 | -8.7959 | -49.9533 | 2024-10-05 01:45:56 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| deac5cee-4d58-3ac1-a746-49073060162b | -9.2839 | -65.4283 | 2024-10-05 01:45:59 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 46.5 |
| f17b4655-2309-3ce7-9036-aa0bb1a24e87 | -9.284 | -65.4096 | 2024-10-05 01:45:59 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 48.0 |
| d98147b8-3ac0-32a1-a5be-7f20ec99b244 | -10.4424 | -50.7336 | 2024-10-05 01:46:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 45.1 |
| f2c29535-45b4-3bc4-aa7b-36287dcdbf55 | -11.0966 | -54.2336 | 2024-10-05 01:46:09 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 81089423-bacb-3031-a4c5-8e56a7d734f2 | -11.1155 | -54.2319 | 2024-10-05 01:46:09 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 83.6 |
| baa7a12c-178c-31fb-a470-9a4a58e7419d | -11.1158 | -54.2114 | 2024-10-05 01:46:09 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 80deec60-d654-3c1a-aef1-c7595c521637 | -11.6995 | -47.8131 | 2024-10-05 01:46:12 | GOES-16 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 52.0 |
| 8b997486-43e7-336e-993c-e92bd75cd429 | -11.7187 | -47.8107 | 2024-10-05 01:46:12 | GOES-16 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 41.6 |
| 4e5e821b-72b4-38f2-a7c9-4e725fe24f26 | -13.1543 | -51.1931 | 2024-10-05 01:46:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 838323e5-952d-3baa-afdd-95c1c7e6889e | -15.5597 | -57.4553 | 2024-10-05 01:46:34 | GOES-16 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 105.9 |
| b3bd7088-ddca-3814-b311-5984bb17a7de | -15.5791 | -57.4532 | 2024-10-05 01:46:34 | GOES-16 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 110.8 |
| 1f48d3f2-6b05-3460-af5c-0f108a65a70a | -15.7151 | -57.4184 | 2024-10-05 01:46:35 | GOES-16 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 82.6 |
| ccec0de1-4a05-39a8-b35d-304595a5d44e | -16.5544 | -57.2032 | 2024-10-05 01:46:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 107.4 |
| e8d3caea-8b12-35a6-8ef9-ffb06a9d0e17 | -16.4155 | -57.3619 | 2024-10-05 01:46:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 85.3 |
| c7cc0f88-753d-38f7-9797-62d0113cb015 | -16.554 | -57.2237 | 2024-10-05 01:46:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 215.7 |
| bc547186-6a5e-3ada-b8ac-642d2cdcef23 | -16.5547 | -57.1828 | 2024-10-05 01:46:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 111.7 |
| 1bfbcf95-866c-31ab-b5bb-05363bdee176 | -16.555 | -57.1623 | 2024-10-05 01:46:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 101.5 |
| c88b74e6-7e77-36f6-ac33-0a382ab2f1e1 | -16.5742 | -57.1805 | 2024-10-05 01:46:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 355.6 |
| ee95e354-baa7-306e-8cef-a2e8efcb0c3b | -16.5745 | -57.16 | 2024-10-05 01:46:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 316.7 |
| 173c875f-c66d-31ee-8e0e-af528df4f2cc | -16.6402 | -55.5243 | 2024-10-05 01:46:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 80.1 |
| 81bf8f14-a834-386a-ac25-937c7917f929 | -16.6598 | -55.5219 | 2024-10-05 01:46:40 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 80.0 |
| 8371d6fa-8a3e-3334-bcf1-4259c93b92fe | -16.6871 | -57.4536 | 2024-10-05 01:46:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 101.8 |
| 56b3e335-977f-3668-9d80-7cf98ad961fc | -16.7647 | -57.4856 | 2024-10-05 01:46:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 153.6 |
| 3a33dd56-35e4-36d8-b0c6-fb8f2e371a20 | -16.7843 | -57.4834 | 2024-10-05 01:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 106.2 |
| bbc35e6d-ebe7-36ae-9647-00dc703c97db | -17.1381 | -57.381 | 2024-10-05 01:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 91.6 |
| 180311ba-cfa0-3785-bb01-2428275d2c20 | -17.0888 | -56.7915 | 2024-10-05 01:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 101.7 |
| 2fe038da-3d3a-3b33-98c5-0f0d798226a5 | -17.0892 | -56.7709 | 2024-10-05 01:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 124.4 |
| 0a3e0415-a1fd-323e-bb01-20a03feda484 | -17.1178 | -57.4244 | 2024-10-05 01:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 177.3 |
| 26387819-c182-336c-9278-826c634f4f17 | -17.1182 | -57.4039 | 2024-10-05 01:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 223.3 |
| 2580330d-e81c-3d00-9f56-603c34f7f194 | -17.1185 | -57.3834 | 2024-10-05 01:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 101.6 |
| dc779134-837a-328b-b4a6-abfbf00c4c23 | -17.1375 | -57.4221 | 2024-10-05 01:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 163.8 |
| b663267e-ab25-3920-a747-287870214f18 | -17.1378 | -57.4016 | 2024-10-05 01:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 198.8 |
| 2ea53804-d6f9-3337-8f2e-04886734883b | -18.8606 | -43.6084 | 2024-10-05 01:46:50 | GOES-16 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 71.0 |
| 9f92365a-bf3f-33ed-93e6-52819c767b11 | -18.8809 | -43.6032 | 2024-10-05 01:46:50 | GOES-16 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 110.1 |
| bd128cc4-1ffd-30aa-bc48-43af631141b7 | -18.8816 | -43.5785 | 2024-10-05 01:46:50 | GOES-16 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 95.3 |
| e1ddfdf3-93d0-3ce6-85c8-faa7249d6bbe | -18.6582 | -57.2967 | 2024-10-05 01:46:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 108.7 |
| e50221f8-1809-3fe5-9fb3-3ffeeb391917 | -18.6586 | -57.2759 | 2024-10-05 01:46:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 143.9 |
| 52faa41d-4f2e-3385-b6ce-f4602d59ce49 | -18.6782 | -57.2941 | 2024-10-05 01:46:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 113.4 |
| c797ea7b-7e2e-38cc-a1f1-761abcc0679a | -18.6785 | -57.2734 | 2024-10-05 01:46:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 149.3 |
| d3182ca1-f5ac-36ca-8788-7d6c1e3b0cc6 | -19.1576 | -46.6279 | 2024-10-05 01:46:52 | GOES-16 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 103.1 |


[Clique aqui para ver as próximas entradas](README25.md)

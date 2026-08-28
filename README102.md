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

## Dados Diários - Página 102

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6e9d8714-716a-31c9-ba0d-b6aedab288ab | -6.598 | -45.201 | 2026-08-28 16:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 53.3 |
| 6136bd0e-e290-3bf9-a8dd-e8ae270393f4 | -9.2477 | -57.0697 | 2026-08-28 16:50:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 80.1 |
| baa487b6-e381-3593-ba7b-9c7381c44db1 | -12.3999 | -48.2073 | 2026-08-28 16:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 108.4 |
| 59b9e3b5-688d-3477-b664-09a4655893c0 | -6.641 | -58.4987 | 2026-08-28 16:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 78.1 |
| de9902eb-81ef-3ea0-bf52-6f2a2d50c83a | -6.8357 | -59.9571 | 2026-08-28 17:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 115.3 |
| a3c31290-58c2-3c72-b5a9-a4cf95886680 | -6.7105 | -45.1917 | 2026-08-28 17:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 44.3 |
| ba9d07ee-ee92-38fc-9c0b-1d1595b20d9c | -6.641 | -58.4987 | 2026-08-28 17:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 77.6 |
| ca1aeb4a-e834-33d5-b5c2-d2e97ed3228a | -6.598 | -45.201 | 2026-08-28 17:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 9e7fbafa-aa42-3ae4-88e9-67691b01a6d1 | -10.5601 | -50.4022 | 2026-08-28 17:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 100.1 |
| a8768350-7de4-3015-8706-036b45740279 | -5.78 | -57.5605 | 2026-08-28 17:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 8c373c54-3e9f-3257-a4c9-0142ee1768a1 | -10.2557 | -64.4915 | 2026-08-28 17:00:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 41.5 |
| 6da1a847-eba4-3bde-bf62-7fdebe4695a0 | -11.1998 | -55.0805 | 2026-08-28 17:00:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 881f7377-d326-3318-849e-cd6a0a6adff2 | -6.5608 | -56.5266 | 2026-08-28 17:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 1a924fff-5f41-3157-8a9c-09577354f7b9 | -6.8571 | -59.4179 | 2026-08-28 17:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 96.8 |
| 935a9670-c20b-3280-ae24-ff3a4be33a5c | -8.5777 | -54.8373 | 2026-08-28 17:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 114.3 |
| b39aebc2-fe86-35f7-9c57-f4aaccac41bf | -6.8019 | -59.4008 | 2026-08-28 17:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 103.7 |
| 38d59d02-b2d6-3cc1-bb44-a4e466d10a86 | -6.6167 | -45.1994 | 2026-08-28 17:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 55.7 |
| a3805080-f18a-3892-b021-fe96c3c0c3b1 | -6.0005 | -57.6689 | 2026-08-28 17:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 5a2b587e-e3d5-3397-9be8-fbd8a5ab7a7b | -11.1922 | -51.2284 | 2026-08-28 17:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 1f7df307-a8e8-3079-bce4-01c6d4541663 | -6.6169 | -45.1767 | 2026-08-28 17:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 273dc84b-fedc-3007-bfe6-d5a42f37a9e6 | -10.899 | -50.5159 | 2026-08-28 17:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 56188c80-2773-32ec-9163-c740619d37fa | -7.5668 | -61.2096 | 2026-08-28 17:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 812235f5-5acf-3587-8bbe-5eb003815fea | -8.8372 | -49.6291 | 2026-08-28 17:10:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 70012ef8-ec6f-3f40-8288-5cd437616a92 | -6.0005 | -57.6689 | 2026-08-28 17:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 66ea1647-215f-344a-bfb7-e6061098f0cd | -10.8463 | -50.2224 | 2026-08-28 17:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 4168fbbb-4d1e-3081-8689-752009ea2941 | -12.209 | -50.5601 | 2026-08-28 17:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 91.8 |
| bd78697d-0bdc-3a66-8dff-71887e6dfe39 | -10.899 | -50.5159 | 2026-08-28 17:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 23ca1354-1bf0-3601-8fd2-1df375ab4815 | -6.641 | -58.4987 | 2026-08-28 17:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 6410ea6b-e12f-3a9c-af04-fca667130008 | -6.6167 | -45.1994 | 2026-08-28 17:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 59.9 |
| de50d561-a67c-3fe6-aae7-e032120f8ec8 | -6.7691 | -58.6873 | 2026-08-28 17:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 9defd149-088e-3887-a1f1-f40f22dca6c8 | -6.254 | -55.391 | 2026-08-28 17:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 0936c8a6-51d4-3aa0-8064-7177c14b3972 | -6.8019 | -59.4008 | 2026-08-28 17:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 110.5 |
| 76666d4f-f047-3324-9577-a43c454ae8a6 | -6.6169 | -45.1767 | 2026-08-28 17:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 69aa53ba-d4cd-332c-9178-4f7f409eb505 | -8.5777 | -54.8373 | 2026-08-28 17:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 106.7 |
| ce21da9b-7fe3-3576-98dd-eea8d6205fa9 | -5.9995 | -57.8444 | 2026-08-28 17:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 6062fe85-34a9-303f-826b-c5e63a399bc6 | -8.6311 | -66.5287 | 2026-08-28 17:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 40.7 |
| 61742f92-bb64-32e0-86d9-72eeb8eaf620 | -7.0057 | -59.2575 | 2026-08-28 17:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 0aa36ed5-656a-3053-9d3d-9488e2d9c64a | -6.7647 | -59.4601 | 2026-08-28 17:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 91.9 |
| 1bd6933c-877a-3d26-b3b2-9765a495665d | -7.5668 | -61.2096 | 2026-08-28 17:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 1ad7dafe-b0c3-307b-91e6-157884bf6dc8 | -6.8386 | -59.4379 | 2026-08-28 17:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 3a35e292-0931-373f-be63-32e7fcefad4a | -6.598 | -45.201 | 2026-08-28 17:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 53.3 |
| 8677cd68-2270-37f3-9c8a-f03c08c441d5 | -10.4981 | -64.5005 | 2026-08-28 17:10:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 104.3 |
| 59f39f8b-0730-3fb4-9aaa-d17001d56ac0 | -6.5829 | -58.9851 | 2026-08-28 17:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.4 |
| d8fcb278-2e5c-3567-aea1-29bbf0db7e25 | -12.2281 | -50.5578 | 2026-08-28 17:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 79.3 |
| d1d90e1d-73cc-3240-be35-1b566462ffc4 | -8.631 | -66.5473 | 2026-08-28 17:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 69a01415-b9ac-3adb-9cde-9eb66ce9bf4b | -8.7846 | -70.8219 | 2026-08-28 17:10:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 88.8 |
| 4a7f3040-6f4b-33b8-bd33-1a4dec38212a | -13.4707 | -57.0574 | 2026-08-28 17:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 56bc159d-d3a3-3fd0-998e-064575e3cf0a | -11.97 | -45.53 | 2026-08-28 17:15:00 | MSG-03 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e245928e-750a-3460-9324-52b40c50bca6 | -14.88 | -52.63 | 2026-08-28 17:15:00 | MSG-03 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4000aa85-6271-3256-b73f-b1cb52bc4fbb | -6.769 | -58.7066 | 2026-08-28 17:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 8eb6e192-0dfe-33d1-9aa3-6d433aed68b8 | -7.5851 | -61.228 | 2026-08-28 17:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 708632fc-f350-3ebf-90f5-648e80610962 | -9.2477 | -57.0697 | 2026-08-28 17:20:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 86.3 |
| fffa4d13-1dac-3d08-bc39-382d1b7b7b59 | -10.9859 | -51.0807 | 2026-08-28 17:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 49.0 |
| 71518ff6-f532-3bd3-a345-4378999de688 | -9.1525 | -65.7874 | 2026-08-28 17:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 51.1 |
| aee08708-501c-366a-b51f-0157cec291b1 | -6.6167 | -45.1994 | 2026-08-28 17:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 637dfad6-029b-391c-95b1-abfe7fb44360 | -8.631 | -66.5473 | 2026-08-28 17:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 980d275d-3a00-39c2-82bb-e247073bab49 | -6.7094 | -59.443 | 2026-08-28 17:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 60d07aa8-cfc0-3c4c-8471-a11ce72c291b | -8.0928 | -45.8354 | 2026-08-28 17:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 115.3 |
| 39d37cf8-ba87-34d9-8102-3e245549c45b | -8.4526 | -70.6981 | 2026-08-28 17:20:00 | GOES-19 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 443cb0c7-5de4-3d16-9119-76a94b18de2e | -7.5846 | -61.3232 | 2026-08-28 17:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 114.2 |
| 9434ecbb-c937-3960-8964-4b108af6239e | -7.5104 | -61.3832 | 2026-08-28 17:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 43.9 |
| 9095b501-3c66-3781-9429-73df0998655f | -8.8185 | -62.3189 | 2026-08-28 17:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 45.5 |
| e7c34525-e009-3f3a-bca7-5081dee2ac53 | -7.4735 | -61.3846 | 2026-08-28 17:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 150.9 |
| 620379ce-6d2f-3fb0-91bd-a9fc8d96b20b | -6.6169 | -45.1767 | 2026-08-28 17:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 82517611-9af9-3a74-97aa-734cb2bcbe4b | -10.7649 | -50.6366 | 2026-08-28 17:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 29fbb83e-f1a1-35dd-b194-2106951bb0f9 | -6.0005 | -57.6689 | 2026-08-28 17:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 35d45c0c-0e8a-3341-9da1-0e4e1ff7c0b0 | -6.641 | -58.4987 | 2026-08-28 17:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 37d1e103-6ff0-30c0-903f-7155e2a029cd | -11.1998 | -55.0805 | 2026-08-28 17:20:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 4437e672-8aeb-3ab0-a56f-492f30b2b189 | -6.8019 | -59.4008 | 2026-08-28 17:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 101.4 |
| 808b9cf0-5831-3497-ac7b-0e6c41ed9e13 | -8.6311 | -66.5287 | 2026-08-28 17:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 47.0 |
| f8fe5834-eb82-3aae-a6c5-98affd23c787 | -6.5608 | -56.5266 | 2026-08-28 17:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 53.7 |
| c5aa7334-44ac-3b46-bb56-fbf356e10089 | -7.5668 | -61.2096 | 2026-08-28 17:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 667e1307-378c-3005-9c85-d9fa5dba2366 | -5.78 | -57.5605 | 2026-08-28 17:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 75.4 |
| c614fd88-a9fc-32f8-9890-877456e9407d | -12.209 | -50.5601 | 2026-08-28 17:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 9e375ba8-dfcb-3875-9f4b-ab78d9346796 | -8.6495 | -66.5468 | 2026-08-28 17:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 6b531d90-63f1-3022-9cda-dde50ed2f4bc | -25.17642 | -51.07716 | 2026-08-28 17:22:00 | NPP-375 | PRUDENTÓPOLIS | PARANÁ | Brasil | 4120606 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 86d8fa5a-c0f7-3ace-b5e4-ed0e5abeee5a | -24.85095 | -49.22543 | 2026-08-28 17:22:00 | NPP-375 | CERRO AZUL | PARANÁ | Brasil | 4105201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 1dd875f8-78f8-302c-931a-684af12f807f | -27.51935 | -51.53527 | 2026-08-28 17:22:00 | NPP-375 | ZORTÉA | SANTA CATARINA | Brasil | 4219853 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 211c6f12-881b-398e-a3e4-aa9c2896d9e8 | -26.19129 | -53.26956 | 2026-08-28 17:22:00 | NPP-375 | FLOR DA SERRA DO SUL | PARANÁ | Brasil | 4107850 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 95bb0aed-c443-3704-bd3b-86ebfbda9cc1 | -26.33145 | -53.08355 | 2026-08-28 17:22:00 | NPP-375 | MARMELEIRO | PARANÁ | Brasil | 4115408 | 41 | 33 | nan | nan | nan | Mata Atlântica | 13.9 |
| 5b894149-045c-3f24-bcc7-c861ffab249d | -27.32659 | -52.89378 | 2026-08-28 17:22:00 | NPP-375 | NONOAI | RIO GRANDE DO SUL | Brasil | 4312708 | 43 | 33 | nan | nan | nan | Mata Atlântica | 11.2 |
| 2acff473-dd7a-342a-b58b-73bc56b529ed | -25.0336 | -51.20634 | 2026-08-28 17:22:00 | NPP-375 | PRUDENTÓPOLIS | PARANÁ | Brasil | 4120606 | 41 | 33 | nan | nan | nan | Mata Atlântica | 11.3 |
| ba9eba98-2700-3762-9712-32e0b1af54e7 | -24.87407 | -50.91457 | 2026-08-28 17:22:00 | NPP-375 | IVAÍ | PARANÁ | Brasil | 4111407 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| b6af2fe3-d732-3888-84c0-474739d379de | -25.99876 | -53.69292 | 2026-08-28 17:22:00 | NPP-375 | PRANCHITA | PARANÁ | Brasil | 4120358 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 7e3092b5-63e7-34b3-a79c-f464ef9848b8 | -26.44922 | -51.04121 | 2026-08-28 17:22:00 | NPP-375 | MATOS COSTA | SANTA CATARINA | Brasil | 4210704 | 42 | 33 | nan | nan | nan | Mata Atlântica | 35.8 |
| fda0f86b-ff32-344c-9ccd-506eef5d3320 | -24.9288 | -51.08014 | 2026-08-28 17:22:00 | NPP-375 | CÂNDIDO DE ABREU | PARANÁ | Brasil | 4104402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 33.9 |
| aa7cbfef-a6b0-3172-a1b8-f0a678bed945 | -28.60909 | -55.3204 | 2026-08-28 17:22:00 | NPP-375 | SANTO ANTÔNIO DAS MISSÕES | RIO GRANDE DO SUL | Brasil | 4317707 | 43 | 33 | nan | nan | nan | Pampa | 5.1 |
| 6661615c-4982-3bb3-90a3-aaf68503da8c | -25.02423 | -50.0985 | 2026-08-28 17:22:00 | NPP-375 | PONTA GROSSA | PARANÁ | Brasil | 4119905 | 41 | 33 | nan | nan | nan | Mata Atlântica | 10.0 |
| 1f923e54-eb36-3348-897f-59be7f8e3a75 | -27.58084 | -51.08623 | 2026-08-28 17:22:00 | NPP-375 | ABDON BATISTA | SANTA CATARINA | Brasil | 4200051 | 42 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 868a1f07-752f-3916-a1e1-d1f067665573 | -27.3238 | -52.89837 | 2026-08-28 17:22:00 | NPP-375 | NONOAI | RIO GRANDE DO SUL | Brasil | 4312708 | 43 | 33 | nan | nan | nan | Mata Atlântica | 11.2 |
| 48594f1e-0439-3d6a-bb5d-5f976b1136f6 | -26.04894 | -51.5979 | 2026-08-28 17:22:00 | NPP-375 | BITURUNA | PARANÁ | Brasil | 4102901 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 3972d317-ed24-3f4f-a5c4-b61c12956521 | -26.83592 | -51.29757 | 2026-08-28 17:22:00 | NPP-375 | MACIEIRA | SANTA CATARINA | Brasil | 4210050 | 42 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| 4efbd895-e9bb-3cb8-97f3-0ceb27d7f502 | -27.19525 | -49.29906 | 2026-08-28 17:22:00 | NPP-375 | APIÚNA | SANTA CATARINA | Brasil | 4201257 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| c25af201-02b6-36e1-a74e-df4d29f78b63 | -27.83231 | -51.96261 | 2026-08-28 17:22:00 | NPP-375 | FLORIANO PEIXOTO | RIO GRANDE DO SUL | Brasil | 4308250 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| dd537e96-5b28-3b92-b3fc-07337c28ea39 | -27.31649 | -52.89563 | 2026-08-28 17:22:00 | NPP-375 | RIO DOS ÍNDIOS | RIO GRANDE DO SUL | Brasil | 4315552 | 43 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 4b98da51-0ff1-341e-b32b-7c8a28eaedfa | -27.34914 | -53.02434 | 2026-08-28 17:22:00 | NPP-375 | PLANALTO | RIO GRANDE DO SUL | Brasil | 4314704 | 43 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 18327bba-1570-3e37-871e-5055cced911c | -25.92224 | -52.64599 | 2026-08-28 17:22:00 | NPP-375 | CORONEL VIVIDA | PARANÁ | Brasil | 4106506 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| ceee179c-1977-3c18-84e9-8567a26dd9dc | -26.64424 | -51.07981 | 2026-08-28 17:22:00 | NPP-375 | CALMON | SANTA CATARINA | Brasil | 4203154 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 6b5b296c-b146-3953-909c-c8718541d122 | -27.02972 | -52.00229 | 2026-08-28 17:22:00 | NPP-375 | IRANI | SANTA CATARINA | Brasil | 4207809 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| e1ad773d-8d27-3180-9430-1287f0251e1a | -26.39143 | -52.15785 | 2026-08-28 17:22:00 | NPP-375 | PALMAS | PARANÁ | Brasil | 4117602 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |


[Clique aqui para ver as próximas entradas](README103.md)

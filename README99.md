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

## Dados Diários - Página 99

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fe4b276c-ad9e-32ad-9d7b-58ab2c3342d3 | -11.559 | -52.117 | 2025-08-26 06:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 48.8 |
| abe87d2a-7ce9-3134-8f01-5e2fae4ee848 | -9.1909 | -59.4619 | 2025-08-26 06:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 41.2 |
| 24358e1a-80a0-34f6-9d85-b03daa21b465 | -6.2275 | -60.018 | 2025-08-26 06:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 45.1 |
| ae4a85b9-65b3-33a7-81fb-a82f542c0e66 | -11.521 | -52.1209 | 2025-08-26 06:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 0b6f7a53-543f-342b-aa18-474ff0a40d23 | -11.6273 | -46.4126 | 2025-08-26 06:30:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 120.6 |
| 5c2ba3e7-ab9e-36ec-9b9b-6762d7efc4d8 | -9.1904 | -59.5201 | 2025-08-26 06:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 43.9 |
| 4bde7cbd-a287-38a5-a843-6eff5b9bca11 | -8.8734 | -62.4495 | 2025-08-26 06:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 37.5 |
| c8522513-93d4-3b37-9f30-0bf4703daf41 | -8.855 | -62.4313 | 2025-08-26 06:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 28c119ad-e74d-3412-b373-94bc8bf1e82b | -8.8548 | -62.4503 | 2025-08-26 06:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 124.0 |
| 5854f7fb-c577-37f6-b893-c49ca3bf04c3 | -8.8364 | -62.4321 | 2025-08-26 06:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 8fcf5b59-fbdc-395f-b17e-45dcd5ec1321 | -11.5207 | -52.142 | 2025-08-26 06:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 85c55866-3a8c-39f8-a990-7cade8519072 | -6.7635 | -59.6718 | 2025-08-26 06:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.0 |
| d7b24433-e233-3d5e-a216-22cefea73daf | -3.97967 | -51.0578 | 2025-08-26 06:35:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| fe351ebd-d511-367d-9fcf-e16d8059300e | -9.18005 | -59.52579 | 2025-08-26 06:37:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 20.6 |
| df25b674-d7f5-3c6f-890e-a16ff92810a2 | -6.76195 | -59.66211 | 2025-08-26 06:37:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 15.6 |
| ba080b12-46bf-32ab-b722-0f5dfd5a92e9 | -9.18879 | -59.52409 | 2025-08-26 06:37:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 7a4c6caf-0857-3827-be0c-e66a04f810ab | -9.1605 | -59.53245 | 2025-08-26 06:37:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 23.7 |
| 407cbf43-adbc-39a6-8ccd-a6ec6bda55c6 | -9.17244 | -59.515 | 2025-08-26 06:37:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 7a69deb3-575e-305f-8c12-6641fcfd96ea | -6.65719 | -58.79479 | 2025-08-26 06:37:00 | AQUA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| d8bf8a42-f68f-3adf-933a-e4154043d598 | -6.24084 | -60.00659 | 2025-08-26 06:37:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 38.5 |
| b1c5e83a-9ca1-3c24-90b6-750eb251b6d4 | -9.18167 | -60.79684 | 2025-08-26 06:37:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| f4306e22-055a-3fb5-8f54-07e2b420dfaa | -8.85576 | -62.43849 | 2025-08-26 06:37:00 | AQUA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 45.7 |
| ea72cfc2-3295-32a0-9f37-baa7295068c6 | -8.3478 | -62.9303 | 2025-08-26 06:37:00 | AQUA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 21.1 |
| 8a928ab3-f65d-3c5b-8029-a9a4cc4334da | -11.29988 | -55.11672 | 2025-08-26 06:37:00 | AQUA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 11.4 |
| a5061aa1-764f-336d-a0e0-9cfd7958c4ee | -8.54574 | -62.63432 | 2025-08-26 06:37:00 | AQUA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 082857f1-10cd-30e2-ad96-4feb2cb13f94 | -9.16484 | -59.50422 | 2025-08-26 06:37:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 9fb33223-9c09-3be8-af63-a764ec3fbd56 | -10.86921 | -55.78657 | 2025-08-26 06:37:00 | AQUA_M-M | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 12.0 |
| c1cc1be9-c37f-34c4-a97a-78cc1713197b | -8.10131 | -62.87763 | 2025-08-26 06:37:00 | AQUA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 11.4 |
| c1a23d21-1259-301e-a6f8-9a4cf04fd3db | -7.62198 | -61.04171 | 2025-08-26 06:37:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 4da1e476-9f5c-30df-9299-4c6e6e5dddd9 | -4.96207 | -55.80873 | 2025-08-26 06:37:00 | AQUA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 37.0 |
| de0ae038-0b30-3fcb-ad1b-928a2ede05ad | -9.23783 | -60.81686 | 2025-08-26 06:37:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| ee0eb626-cc74-330d-82a9-4d511aaadce3 | -8.24298 | -61.45898 | 2025-08-26 06:37:00 | AQUA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 9b0b2d77-775a-3d45-a7f3-4920deb8e1e4 | -11.52328 | -52.12659 | 2025-08-26 06:37:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 35.4 |
| b4438152-1535-3015-8257-2da6bc3353ff | -9.2339 | -60.90538 | 2025-08-26 06:37:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| edaf7aed-c065-33bd-81a8-7be7ef18de2d | -8.98704 | -65.42455 | 2025-08-26 06:37:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 70d0203c-8016-3018-bfe7-5f4455cb2808 | -6.76039 | -59.67204 | 2025-08-26 06:37:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 58ed2d91-a0b2-3f6e-a92f-2aeb24c60406 | -6.2544 | -60.01435 | 2025-08-26 06:37:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 6377912f-f450-3b82-b6b7-b25b14affb5a | -9.17388 | -59.5056 | 2025-08-26 06:37:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.6 |
| e3276094-b940-3764-aa8f-7ff0358adb0f | -8.84487 | -62.4367 | 2025-08-26 06:37:00 | AQUA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 205.3 |
| 5398befb-afac-3e9a-9a56-dbd6aafa0566 | -9.18585 | -59.54289 | 2025-08-26 06:37:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 34083693-528c-37bf-b7c2-e9c6cc300400 | -9.18292 | -59.50698 | 2025-08-26 06:37:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| ee9d2c58-51cd-37fe-941d-2991628c2d66 | -6.83563 | -58.95768 | 2025-08-26 06:37:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 36.4 |
| db3fdbbc-630e-30a3-bfac-20a85963c905 | -9.15905 | -59.54186 | 2025-08-26 06:37:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 28.8 |
| 8e2582be-6eb6-3711-b2ad-420fd7595183 | -8.24497 | -61.44673 | 2025-08-26 06:37:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| c0f6a951-ec36-31bd-a2cf-e7c767e60949 | -8.85347 | -62.45251 | 2025-08-26 06:37:00 | AQUA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 1e263636-5136-3e36-8a46-a9bf2df072dd | -9.79745 | -64.24958 | 2025-08-26 06:37:00 | AQUA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 3d701ef5-1d68-39aa-b254-711cea3da122 | -9.27043 | -56.90089 | 2025-08-26 06:37:00 | AQUA_M-M | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 13.9 |
| acb26e8a-52f5-371e-ad06-7a756a194cad | -4.95309 | -55.80745 | 2025-08-26 06:37:00 | AQUA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 18003db6-ea8a-3c7b-bcde-218198253cfa | -7.88778 | -63.00146 | 2025-08-26 06:37:00 | AQUA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 9612163e-7ddb-301b-84be-afdb10db6d8d | -6.695 | -58.54777 | 2025-08-26 06:37:00 | AQUA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 9.4 |
| e9b5ea83-11a9-3f99-819d-96162b3ec9d2 | -8.97324 | -65.4222 | 2025-08-26 06:37:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 29.2 |
| e1d491d7-2e00-3ab5-92c4-a82c0bc9ad70 | -6.77904 | -59.67497 | 2025-08-26 06:37:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 6887220a-d1d6-3d18-8bae-9dcd89c5269a | -6.30747 | -59.86229 | 2025-08-26 06:37:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 9.6 |
| d7b2f05f-51d6-3b23-8eee-22384522bd23 | -6.71007 | -58.56863 | 2025-08-26 06:37:00 | AQUA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 17b9d19e-eb80-361f-b0fa-75d04f650fa1 | -11.53861 | -52.10838 | 2025-08-26 06:37:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 43.8 |
| 6c7e00e2-50c2-3c4d-8292-0bb61da7f8aa | -6.81613 | -58.9643 | 2025-08-26 06:37:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 104.8 |
| 31827476-aa57-3fa3-8371-ca3c98431949 | -9.07268 | -65.71992 | 2025-08-26 06:37:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 24.4 |
| 34e9da61-cc9c-3b10-9554-b4245fd74cdb | -7.35399 | -59.66836 | 2025-08-26 06:37:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.3 |
| b3ea71c5-a689-301f-b772-f0e111aef107 | -6.81757 | -58.95498 | 2025-08-26 06:37:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 42.0 |
| 33463ced-08ae-3a86-bb2a-e62a14e7c2ff | -9.16339 | -59.51362 | 2025-08-26 06:37:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 16.4 |
| b4701a50-e8f2-3703-a6b6-1f4340b9a260 | -6.68747 | -58.53738 | 2025-08-26 06:37:00 | AQUA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 1237c5dc-edce-317e-9b8f-f7d79a49b9cc | -9.31478 | -63.42757 | 2025-08-26 06:37:00 | AQUA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 13.1 |
| a4df084e-7d3e-3ed0-a6d1-062b4bc7b843 | -9.1786 | -59.53522 | 2025-08-26 06:37:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.6 |
| ec197dd2-7ec5-3e4a-97d3-f2e05db7f6fe | -11.56353 | -52.11872 | 2025-08-26 06:37:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 27.1 |
| da87c53e-3bc3-31cf-a15a-bd73e28d14e4 | -6.8147 | -58.97362 | 2025-08-26 06:37:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 21.4 |
| a64a37b1-75b0-35be-98bf-2d15fecf991e | -6.25607 | -60.00377 | 2025-08-26 06:37:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 78f8fdda-309b-3706-9ac7-be87085b2e41 | -9.26906 | -59.78534 | 2025-08-26 06:37:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 623164f6-f25d-3e75-ac91-6d73624685c3 | -9.31202 | -63.444 | 2025-08-26 06:37:00 | AQUA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 1d2964f4-85e1-3e82-8809-2854e2d98138 | -4.96072 | -55.81789 | 2025-08-26 06:37:00 | AQUA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 32.6 |
| a6cef3a9-1ea3-31ce-b7de-486b616fe6a1 | -7.88292 | -63.00774 | 2025-08-26 06:37:00 | AQUA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 35.4 |
| 19ed477c-c645-3411-b989-ff4c6e73e2bb | -11.49785 | -52.1234 | 2025-08-26 06:37:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 16.7 |
| c2fd7d1f-4de0-37fe-aae9-1ab0220863d2 | -9.17204 | -59.45732 | 2025-08-26 06:37:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 29bb02b1-415b-3e07-ab66-5fcae28207dc | -6.63026 | -58.54169 | 2025-08-26 06:37:00 | AQUA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c0e1522a-7403-3c3f-95f7-2bf88326f375 | -9.18149 | -59.51638 | 2025-08-26 06:37:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 0f431bf7-9198-3cc4-9410-0e0d389ff3a0 | -6.69362 | -58.55685 | 2025-08-26 06:37:00 | AQUA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 60e847c9-4bc1-3c0f-9869-67d35d0ba7d8 | -9.18732 | -59.53349 | 2025-08-26 06:37:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 29.3 |
| 4496b71a-dd3f-3a68-8e87-60d7a9d424df | -9.64537 | -59.6253 | 2025-08-26 06:37:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 13.5 |
| f0687516-1b10-3a50-bae0-1808b579af7b | -7.38187 | -64.34063 | 2025-08-26 06:37:00 | AQUA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 43.7 |
| a9690e58-d478-32a2-b155-c25e38fe9e3b | -8.84257 | -62.45074 | 2025-08-26 06:37:00 | AQUA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 31.0 |
| 0513f35d-b4c3-322f-b589-84d28468b3a8 | -7.37847 | -64.3615 | 2025-08-26 06:37:00 | AQUA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 2a0d41cf-1a21-314c-824a-3c17b48959f2 | -9.27936 | -56.90221 | 2025-08-26 06:37:00 | AQUA_M-M | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 29e79d1e-9765-3306-ae89-12cea2d0954e | -6.24483 | -60.01286 | 2025-08-26 06:37:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 39.2 |
| 2a0474ef-f5d8-3de9-a020-4f54cee65614 | -7.2901 | -59.67196 | 2025-08-26 06:37:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| b399c296-b5e4-370f-8ff3-1e8575239ec5 | -6.82517 | -58.96565 | 2025-08-26 06:37:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 33.6 |
| 9517d26d-11d4-3f63-9314-e2c199df6d64 | -9.18394 | -59.43999 | 2025-08-26 06:37:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 903d5b28-1f9d-3f30-9084-06d623dd0ea3 | -6.76972 | -59.67345 | 2025-08-26 06:37:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 1e7f608d-3e18-3713-9416-fd6313e7ce78 | -6.91199 | -59.35953 | 2025-08-26 06:37:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| d71432f3-3668-3d3b-9ca8-b3d2e991d46a | -7.35553 | -59.65847 | 2025-08-26 06:37:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 13f4242c-5d8e-37e0-b5da-856340b5437f | -11.30154 | -55.1049 | 2025-08-26 06:37:00 | AQUA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 34.5 |
| 2905c381-f3e8-3359-8fb2-27ffe737a1fc | -9.16955 | -59.53382 | 2025-08-26 06:37:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 15.8 |
| b6dfaed7-af99-3db3-bb8b-849e4117b7e8 | -7.47265 | -61.33176 | 2025-08-26 06:37:00 | AQUA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| d3f84308-c0a5-34d8-bff6-a066a746a40a | -9.19173 | -59.50529 | 2025-08-26 06:37:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a56031b6-460d-3d1f-8f34-853ff90db3d0 | -6.70254 | -58.55819 | 2025-08-26 06:37:00 | AQUA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 3eb7fd2f-3702-3bbb-ab3c-2b96abf022f0 | -9.18107 | -59.4587 | 2025-08-26 06:37:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.5 |
| a23bddda-7d37-3f8b-95e8-e8fdd831a94e | -9.1576 | -59.5513 | 2025-08-26 06:37:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 43.2 |
| 1a407dfd-7028-311f-95f0-534f225344c2 | -10.25021 | -59.66053 | 2025-08-26 06:37:00 | AQUA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 1f4e9664-293d-3a61-93db-d721dcc2bc43 | -9.15615 | -59.56072 | 2025-08-26 06:37:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 26d7a2b5-cae3-3c33-bca8-ed79cc0d3367 | -10.39252 | -57.68955 | 2025-08-26 06:37:00 | AQUA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 9a904698-b82d-30b2-bc4a-88dd06d8de88 | -9.23219 | -60.91633 | 2025-08-26 06:37:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 15.8 |
| e72f42e1-0f93-342e-ac5d-d8ce75366752 | -11.53597 | -52.12829 | 2025-08-26 06:37:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 48.6 |


[Clique aqui para ver as próximas entradas](README100.md)

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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c76e83e5-11a0-3530-9381-c7edcd11c196 | -6.6948 | -58.7678 | 2026-09-02 01:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 6876f0c9-a82c-3ed9-a281-2ef047f26d3c | -6.6764 | -58.7686 | 2026-09-02 01:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 6a7fd37c-290d-302d-9447-12536a56d384 | -11.3334 | -50.618 | 2026-09-02 01:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 123.9 |
| 4da3fd65-a2c0-380d-be35-e0d76c31c5e8 | -11.3524 | -50.6159 | 2026-09-02 01:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 125.6 |
| 6eb0f9c6-d80b-3de3-8e68-f8f1b0d3466c | -11.3521 | -50.6373 | 2026-09-02 01:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 110.5 |
| 1edbb0cc-03ba-3db5-9ad4-52f70569fbeb | -9.1694 | -59.5271 | 2026-09-02 01:33:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f36361d9-3caf-3d57-b154-8d3d5800a4e7 | -8.259 | -62.754902 | 2026-09-02 01:33:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 279567f7-b54e-3638-b74a-20d7c9d15c11 | -11.349 | -50.6283 | 2026-09-02 01:33:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7821808b-2e44-30cd-a014-7127000d10c0 | -7.3666 | -60.608101 | 2026-09-02 01:33:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 46aa30bc-c9b8-3984-a14c-bc7c80ebc285 | -6.6957 | -58.752102 | 2026-09-02 01:33:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d9393dbf-4b67-362d-8981-4ec46d115f5e | -8.5639 | -63.195499 | 2026-09-02 01:33:00 | METOP-C | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| fbfe8e17-c220-32b1-9986-1d6a4e1a5cf8 | -2.1301 | -56.818501 | 2026-09-02 01:33:00 | METOP-C | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 77237d30-58b3-3864-b194-20f83c03a9dc | -6.6954 | -59.939499 | 2026-09-02 01:33:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 25bcd69b-409b-3803-8d92-03b246f333cc | -5.2532 | -55.903198 | 2026-09-02 01:33:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8b3bd7c1-fea7-3285-b418-21f74d1398dc | -3.6604 | -58.9132 | 2026-09-02 01:33:00 | METOP-C | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5b6b1bd2-f429-39c0-8c87-8edf46a44f95 | -8.4644 | -54.715599 | 2026-09-02 01:33:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 30805faa-6e7c-3e1e-986d-c02bfecfc5c5 | -8.9006 | -62.356201 | 2026-09-02 01:33:00 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 56bd3c4d-9d82-3d04-9447-2f201a2ff409 | -10.5022 | -59.619499 | 2026-09-02 01:33:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 669a94fa-a7ed-386d-a232-5ebb39dd43fa | -10.6797 | -54.0443 | 2026-09-02 01:33:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9839c8ae-2ede-3324-9b7f-1948701dce92 | -5.9818 | -53.585201 | 2026-09-02 01:33:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 51cfe2d4-8e88-3b83-b42e-e8b7f804522f | -6.6058 | -59.115601 | 2026-09-02 01:33:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5d598319-e77e-3a0c-8d62-3459323ee1e9 | -9.8603 | -64.974998 | 2026-09-02 01:33:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 6f7230cc-dcf6-3643-9d0a-1dd14ba41bfb | -8.7596 | -62.599098 | 2026-09-02 01:33:00 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| aa74fc96-7e7a-3be5-8bb2-25ca1d3cbd02 | -8.4704 | -54.698502 | 2026-09-02 01:33:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1210cc5d-cccc-32bc-803d-708618b7c030 | -5.177 | -60.287498 | 2026-09-02 01:33:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fced3639-a24e-3acc-b66f-a344f7ed3305 | -10.759 | -54.071899 | 2026-09-02 01:33:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5e1b8535-d41f-3ea1-b45e-31edbed03d59 | -9.0187 | -65.444901 | 2026-09-02 01:33:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 58e196a3-a608-3f2a-931f-550aa793def6 | -9.0307 | -65.405701 | 2026-09-02 01:33:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2ecbddf6-5c49-32f5-8fd1-53f1f5688f60 | -8.457 | -54.6861 | 2026-09-02 01:33:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0f8409b7-1f19-3c9c-9a3f-7177788145c2 | -5.5564 | -60.233101 | 2026-09-02 01:33:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b32c3683-1f43-342a-b985-d4d86e55912b | -7.1986 | -60.684502 | 2026-09-02 01:33:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3a63c20a-85ea-3cd6-885e-9c2c7a7a3d3a | -9.8818 | -64.979301 | 2026-09-02 01:33:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c56f6449-52f7-3251-90e7-a08e7759f5c2 | -8.7565 | -62.585201 | 2026-09-02 01:33:00 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f732e051-03c0-3c1d-8716-8a2618b3858b | -3.6209 | -60.5602 | 2026-09-02 01:33:00 | METOP-C | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 742bb951-b24f-326d-8abc-32f2c357c6d4 | -7.6208 | -57.606098 | 2026-09-02 01:33:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cdfc637d-b698-329e-a340-b708bd786cd5 | -3.6626 | -58.922501 | 2026-09-02 01:33:00 | METOP-C | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c1dc54bc-975a-39ca-ad8e-ce1627f19f3d | -10.6759 | -54.029301 | 2026-09-02 01:33:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ddae48ad-4a4e-3342-b0c6-d26be6643bad | -3.6191 | -60.552502 | 2026-09-02 01:33:00 | METOP-C | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 31d15193-d994-385b-af6c-f204784f7bb5 | -9.4675 | -56.742298 | 2026-09-02 01:33:00 | METOP-C | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 650b973d-93b8-3b14-be26-18651e9d01c6 | -6.773 | -59.432098 | 2026-09-02 01:33:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 832b667c-8ff2-3ea0-8c05-077fead9e72d | -8.1216 | -54.954899 | 2026-09-02 01:33:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c50e3e53-49f9-3c64-934e-2bec6659f3cc | -4.2336 | -62.234798 | 2026-09-02 01:33:00 | METOP-C | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a622f630-bcac-30ed-8969-51181ac8dcb7 | -3.125 | -61.226101 | 2026-09-02 01:33:00 | METOP-C | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a85f6e3a-3da5-31c3-a7db-e5314b1a7856 | -8.4607 | -54.700901 | 2026-09-02 01:33:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dd7e6ef6-bf8d-38a4-a9a2-4c48d49610d3 | -10.7476 | -54.026901 | 2026-09-02 01:33:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b5b9be57-6768-31eb-9d57-36c264610255 | -7.6798 | -67.115898 | 2026-09-02 01:33:00 | METOP-C | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6771fbc8-56b3-396e-bb21-ba32b19e33ae | -3.1169 | -61.2356 | 2026-09-02 01:33:00 | METOP-C | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 348616a0-19f4-3908-9261-315cdd94035f | -6.6874 | -59.949402 | 2026-09-02 01:33:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2cda5fbc-a136-350e-96d3-2ab49cd0f7ca | -11.7972 | -50.5313 | 2026-09-02 01:33:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 88c6e396-2cb7-3994-b720-bafbe6ebeb62 | -9.1391 | -60.956699 | 2026-09-02 01:33:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a159cc49-2c16-39b9-8aa3-aebd68bb84d3 | -9.4793 | -60.462299 | 2026-09-02 01:33:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f7f6ed19-474b-3a3d-825b-24a5d97cadb5 | -10.4706 | -64.477203 | 2026-09-02 01:33:00 | METOP-C | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| dff6e72e-b245-3634-b2c2-25cebcad7494 | -8.0998 | -58.273399 | 2026-09-02 01:33:00 | METOP-C | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a13e39ee-6c16-3538-8df9-db5b913f9854 | -7.6917 | -67.124199 | 2026-09-02 01:33:00 | METOP-C | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5212b587-7f14-3d07-9f10-a59f53b90211 | -6.688 | -58.7631 | 2026-09-02 01:33:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a790ff95-fcdd-33ef-91c6-d3bd9bc3aba7 | -8.4316 | -54.708199 | 2026-09-02 01:33:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 77265aa1-ab10-3615-a32b-20876ac99935 | -7.5668 | -60.447498 | 2026-09-02 01:33:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3c079c1f-19ed-384f-aaed-59d3440ac5ab | -7.0235 | -62.987 | 2026-09-02 01:33:00 | METOP-C | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 386c8fea-549d-3159-b387-26056ce733f9 | -5.5885 | -60.193501 | 2026-09-02 01:33:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d05f463a-c22f-31a2-a2e4-d9ee47f5c4f8 | -9.9301 | -60.493 | 2026-09-02 01:33:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0a3c5fc7-548a-3a89-b9d3-a62417550679 | -7.7383 | -60.966499 | 2026-09-02 01:33:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ce391617-a7d5-3ace-b1b2-154616d08dc0 | -7.365 | -60.600899 | 2026-09-02 01:33:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 70f73f5c-41c5-3f08-9be4-96153d1f12ee | -5.5805 | -60.2034 | 2026-09-02 01:33:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 381e6e5b-5903-3b4a-aa1c-91159c630e60 | -10.4988 | -59.604698 | 2026-09-02 01:33:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 27b80845-7f62-3a46-99ac-f1a81248fe30 | -11.7809 | -50.508999 | 2026-09-02 01:33:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 62b92e4b-cc48-3918-8c29-e5b4d5b3cb95 | -3.7555 | -59.32 | 2026-09-02 01:33:00 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ba2d3262-b9d0-36e8-9376-5542ad041ee6 | -14.0005 | -58.676102 | 2026-09-02 01:33:00 | METOP-C | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8fb6c7bf-38b8-3606-bd13-0c8ff4dd5ac2 | -7.4395 | -61.4175 | 2026-09-02 01:33:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 151e7fef-ca71-3e93-92a9-f2f53c23b862 | -7.4721 | -63.744801 | 2026-09-02 01:33:00 | METOP-C | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3c6b8430-bd14-34b7-aa39-fa0e6082210a | -7.6658 | -62.5462 | 2026-09-02 01:33:00 | METOP-C | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bdab9dcf-01a3-3458-a0b3-e4aa24e583d6 | -14.5066 | -59.842602 | 2026-09-02 01:33:00 | METOP-C | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 06e41eda-5844-3e26-bbe4-26b421a13e4d | -6.6073 | -58.596001 | 2026-09-02 01:33:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a2db034f-cf71-3415-b8a9-bcf7a0783a74 | -9.3912 | -60.572601 | 2026-09-02 01:33:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5f3f8137-5462-33a2-bc48-d00726f281bf | -6.7632 | -59.434399 | 2026-09-02 01:33:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1e3a049f-ae7f-385c-8f3c-ce3533205ad7 | -9.4421 | -67.422501 | 2026-09-02 01:33:00 | METOP-C | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 94422e5f-326c-394d-890e-83bae89793a0 | -8.4413 | -54.705799 | 2026-09-02 01:33:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 22ce3cb7-b5cc-3816-9980-9125401b92da | -7.1952 | -60.670101 | 2026-09-02 01:33:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| aaf1e60e-e83d-34d5-acfe-339f21bfb40d | -8.6914 | -62.937302 | 2026-09-02 01:33:00 | METOP-C | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 59b152d4-3da2-3c90-9394-5c9a0035717e | -3.0969 | -61.193699 | 2026-09-02 01:33:00 | METOP-C | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e5fc9838-00f5-3e65-a471-a4a244913915 | -6.6972 | -59.947201 | 2026-09-02 01:33:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 88e25cf0-aa1c-3665-bff1-ffb3ff4cde41 | -8.4486 | -54.735199 | 2026-09-02 01:33:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0238dc6b-e5b1-3319-987c-87beb7a48aca | -7.3485 | -60.5741 | 2026-09-02 01:33:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1a042eba-553e-3d6c-923a-8701db381fba | -3.2895 | -60.643299 | 2026-09-02 01:33:00 | METOP-C | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7f06a546-ae95-3068-b560-19d350418f23 | -9.1505 | -60.961498 | 2026-09-02 01:33:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d284886f-6d2e-36a0-af38-0bdddd6f423b | -9.3896 | -60.565498 | 2026-09-02 01:33:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6a47c931-48ec-37bd-99fc-6569e3a4e0a2 | -7.6895 | -67.1138 | 2026-09-02 01:33:00 | METOP-C | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9ec1c51e-5a4c-3ddf-9d91-aec290a83597 | -7.4593 | -61.369099 | 2026-09-02 01:33:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 65db3ab5-2b11-3731-90f9-4d118c939d6d | -11.303 | -54.0578 | 2026-09-02 01:33:00 | METOP-C | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c716ddf5-8011-3f11-910c-9e79bc959671 | -9.8426 | -64.987701 | 2026-09-02 01:33:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b1c09b29-b17a-323b-aa16-87f1d1d7d735 | -7.5371 | -60.7206 | 2026-09-02 01:33:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1182df1c-7716-3ddf-939c-6c4287d1fe67 | -1.5102 | -54.9674 | 2026-09-02 01:33:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| df1ed58f-cc99-3402-9026-b343a742688d | -3.1344 | -61.177502 | 2026-09-02 01:33:00 | METOP-C | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6935fee1-0ff9-3465-9d83-f0f8e7078fa4 | -8.9347 | -62.370399 | 2026-09-02 01:33:00 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 390f7295-423b-392a-9b6d-626608da41f0 | -3.6405 | -60.555801 | 2026-09-02 01:33:00 | METOP-C | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fdc96e7a-fc95-356e-b81d-5bb2433f80ba | -8.445 | -54.720501 | 2026-09-02 01:33:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5401294a-2a72-3245-89b8-8bfe3be872d4 | -9.0288 | -65.397003 | 2026-09-02 01:33:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| be72cfaa-ba11-3c2b-b21d-800b43b96274 | -6.7651 | -59.442501 | 2026-09-02 01:33:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 83db697f-7389-30a0-b8ae-9365d8d6feb8 | -9.0013 | -65.412102 | 2026-09-02 01:33:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 06c62fc2-ed8b-3823-902d-6fa98bbd3f8b | -6.6856 | -59.9417 | 2026-09-02 01:33:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 981dd185-c0f1-3227-ae41-a0efd20078fc | -5.1868 | -60.285301 | 2026-09-02 01:33:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README9.md)

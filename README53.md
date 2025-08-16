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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c2b25c1f-f361-364c-a7a7-7641f46b556c | -9.82583 | -63.01516 | 2025-08-16 05:23:00 | NOAA-21 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f2bb0445-1888-39da-9a33-0c77c0ac6401 | -9.04491 | -67.425 | 2025-08-16 05:23:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c88d1cbb-86f1-3622-891f-10ddc22b19cd | -10.05441 | -59.11846 | 2025-08-16 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 139a2a5c-4537-341e-b054-4e6409cfb091 | -9.21769 | -59.65289 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f1c3c0e9-a142-3a3e-8621-c2b6b113f319 | -8.98952 | -60.5034 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 3e93ea3b-7e38-35da-9190-e24563f65359 | -9.17354 | -59.64607 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 64cac082-9d12-3746-bfe3-d32801bbf853 | -9.16819 | -59.63008 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e51229a7-fed8-3758-8355-1f528080008c | -9.81077 | -48.54458 | 2025-08-16 05:23:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d4cd693b-1f20-3277-a895-5e19688d4453 | -9.39085 | -60.54486 | 2025-08-16 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 00627e48-b706-3610-8584-7e3c83f69f8b | -6.93616 | -59.99981 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9b708ec8-9ee6-3ec2-9991-f9e7e01bdef5 | -9.63103 | -63.09632 | 2025-08-16 05:23:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8ceee11b-c208-3a9f-b761-0d66a09d607c | -7.24794 | -57.62883 | 2025-08-16 05:23:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 00456f61-9ba1-3dfb-afb6-87fa57e60fa2 | -7.61556 | -63.32413 | 2025-08-16 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6682c7bd-9cc3-3b82-9916-0582f6a66f42 | -9.16763 | -59.63378 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 76697367-f33c-35d6-b491-6ffe4b318283 | -8.09789 | -61.18713 | 2025-08-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 17b210d3-7420-3058-b5ba-5382c8f261c3 | -7.87811 | -61.82654 | 2025-08-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e52e1e4e-caa3-3ad7-9070-46f87102a4ed | -6.87567 | -59.8393 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 38f99074-c6b0-3f4b-bd0a-b9111c4ed0e0 | -9.80469 | -48.53775 | 2025-08-16 05:23:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6057b742-2f8c-339a-9f9a-71337bcf7932 | -8.0323 | -61.51824 | 2025-08-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 06f80bbf-a65f-336a-8886-a6693d1f2a36 | -7.92574 | -61.74075 | 2025-08-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a8ad66f3-48ce-338a-85f7-83390a04b1f5 | -9.92294 | -60.486 | 2025-08-16 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6fb92d63-9c3c-3f75-abb2-18069c6e71f7 | -7.95488 | -63.46483 | 2025-08-16 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d8d83701-145e-397b-a5e8-8f0fce3c4ed3 | -7.52066 | -61.31166 | 2025-08-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3a81db4f-7a20-36dd-9431-d91706eaf384 | -8.99956 | -60.52661 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 66e14d01-9668-38b5-a835-b0bb5702dbea | -7.94605 | -63.21978 | 2025-08-16 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 25db51f5-67f4-36f5-a946-1a9a7670f247 | -8.99285 | -60.50391 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 5136f4e9-c396-3c37-a4c7-bc2835dd1bf4 | -7.91744 | -61.7502 | 2025-08-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 581e8504-4ba8-3000-974c-970cf0e02f64 | -9.51745 | -60.53914 | 2025-08-16 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 8544dae1-a366-3ef2-9803-e4fc4bf4eb31 | -7.42437 | -60.02879 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c73def42-7039-37a1-80e0-cc4c9eec6d60 | -7.24029 | -60.64626 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 080fcb81-e123-3528-b68e-d4003a3a3b3f | -7.61163 | -63.33541 | 2025-08-16 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a101dea6-1918-36c9-909a-f240f3beca2a | -7.6225 | -63.32525 | 2025-08-16 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3a8650c8-5e7f-3387-8260-f79f56020f38 | -8.92831 | -62.24072 | 2025-08-16 05:23:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 75559c54-5be9-334f-9713-013454bab776 | -7.12853 | -59.65285 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2913752b-f0b3-3cc8-a4a1-2e5703c315d9 | -7.53062 | -61.33455 | 2025-08-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 01cc334e-7c18-33af-83c1-bb6b940516eb | -9.51412 | -60.53862 | 2025-08-16 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 2241d865-5287-30d6-81cd-77306b8ebc8b | -9.39805 | -60.54237 | 2025-08-16 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 74e4ccc9-18b5-3c86-b0c6-b3cdc9fc4fc6 | -7.82445 | -61.32459 | 2025-08-16 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 14800c97-3c6e-3bff-ac5c-589e118803cc | -9.04562 | -67.42088 | 2025-08-16 05:23:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0f58a716-f9b6-3162-8140-988d3a9b2496 | -8.99678 | -60.52257 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 11018612-eed0-3786-9f79-367bcce3bae3 | -8.66182 | -62.46026 | 2025-08-16 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 279e8c7f-c79a-3d53-8a90-d3811760516b | -7.05121 | -59.62672 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 00168fce-93cd-333b-80cb-072bef08e80f | -6.94636 | -59.51202 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f75832cd-2594-3a50-aecb-e70c51d07d0e | -6.93753 | -59.54724 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6610b074-7ade-3583-b39a-374220416059 | -9.17046 | -59.63799 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 41401c3b-18d3-377c-b860-7c09ffaa9870 | -9.16253 | -59.64435 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 57d5ff45-ffb5-3eae-8ee9-2c111b0bf579 | -8.94609 | -62.23631 | 2025-08-16 05:23:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b2735a3a-f3a6-3473-9061-9eed8e4baaf8 | -9.80844 | -48.54541 | 2025-08-16 05:23:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 747d2f55-891a-3d7a-ac7c-fb2d2b004521 | -9.17811 | -59.66191 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e9ecd727-5b91-3aa5-ae4b-50c49de1b210 | -8.91851 | -60.76517 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f6756f7f-1e9a-3fd0-a9aa-2761530aa8a6 | -9.50746 | -60.53758 | 2025-08-16 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1cdecf73-ed21-3acb-9bc7-6f6c539a0962 | -9.50637 | -60.54465 | 2025-08-16 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 047db9fc-60a2-329f-88e6-c8cf6e02e9f3 | -3.82314 | -47.73727 | 2025-08-16 05:23:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 8c2f8ea6-afe3-35bb-9ae8-55099ef50602 | -6.9487 | -59.54166 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6b514527-d105-3af0-a7ad-3fbe3baab044 | -6.90995 | -59.63784 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 41ce6bb3-6d83-3ab4-ab7b-3843020e94b1 | -8.55738 | -63.93046 | 2025-08-16 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f861e840-db13-38b4-89b9-2e6ca9787dda | -7.50152 | -63.81871 | 2025-08-16 05:23:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 456d78ae-c7d1-3cee-a242-4264e09b8180 | -8.98518 | -60.53155 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 8082e4a3-f94f-3181-98f8-67c9ab40edd0 | -8.10949 | -61.19961 | 2025-08-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bf90807c-862f-3735-9c2b-4b490fb73f0b | -9.16139 | -59.62906 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| bb70d4a1-58e5-3542-a56b-a0a320a02ab5 | -7.6805 | -63.31883 | 2025-08-16 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f681c574-75fb-3ca0-ae27-5027e3366b75 | -6.93085 | -60.07782 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 336b961e-1eec-36ab-8c16-1c62b894fb36 | -7.12788 | -60.12255 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9c4d5dba-e594-3c9c-8b3f-c08c58c376e8 | -8.55804 | -63.92647 | 2025-08-16 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bb38190a-ea29-3fc0-9612-993abf6ff97c | -7.87368 | -61.81148 | 2025-08-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 143f490b-6075-3ca3-94c7-ca0307c4b207 | -7.24857 | -57.62459 | 2025-08-16 05:23:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 25977aa3-4efa-3777-a227-333c1333baf2 | -6.93979 | -59.55493 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6acf35bf-528e-3cd1-89c9-d9ebc79060eb | -9.17756 | -59.66558 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c083c950-b01c-3a7a-8eaa-01c138ce459e | -10.11183 | -57.77166 | 2025-08-16 05:23:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| dc910cd2-4c2b-38dd-ae38-c9b43fed5a75 | -7.91357 | -61.75318 | 2025-08-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ab21cafe-e25b-3749-98a4-703a9144a2c1 | -9.18711 | -59.64825 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 03ca7e09-b6ff-3f16-a5da-26978cf68672 | -7.5356 | -61.34601 | 2025-08-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ba10a9fb-8626-3cdd-abb3-a20e45bb8e46 | -9.16306 | -59.716 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6367e38e-9efb-355d-86a0-9b4101fc62a4 | -7.45672 | -60.41394 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 988ae3a0-e2e2-37a3-8c0a-584cf1e2d8e7 | -9.00004 | -60.50143 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5b2566b0-73b6-39cd-86c4-3f3acc7d8c45 | -8.85858 | -69.15318 | 2025-08-16 05:23:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8fc85ddb-38f2-3c92-b98a-1bfbb94e90ff | -6.93808 | -59.54367 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 23eebac3-3aee-3991-9a92-48441920193c | -7.31269 | -60.6186 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2651c0aa-b9b4-3511-8b7e-2ec90bbaca70 | -10.4327 | -60.28617 | 2025-08-16 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 695f9f3c-55e9-34a3-962a-61b7a3e0fec3 | -7.69437 | -63.32106 | 2025-08-16 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3771bb3d-63ed-3425-9971-1e73c5fa7d47 | -8.91065 | -60.72815 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 55236467-f7de-354c-ac13-57f4175b4863 | -8.54902 | -63.93729 | 2025-08-16 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6d96e894-e0b2-36a7-b2df-8d1aff297817 | -9.82246 | -63.01461 | 2025-08-16 05:23:00 | NOAA-21 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9ad92917-766e-3efa-9cbe-cdee2a1fe854 | -6.62812 | -60.01261 | 2025-08-16 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 99268af3-2eda-3636-a43a-4bc794288f87 | -9.5042 | -60.55877 | 2025-08-16 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 44859775-0bf7-3d72-8c30-a98fbb4fc0d3 | -7.6184 | -63.32853 | 2025-08-16 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4ca9bd52-6691-374a-80b5-11fdfa1ea510 | -8.98193 | -60.55263 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| eb91bdcc-1bd5-3776-a945-033983637f8e | -7.82391 | -61.32806 | 2025-08-16 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 61190c42-e3d2-3505-b58a-47684f3793f9 | -9.15687 | -59.63593 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a1f1c6eb-e6f5-3b68-934b-c3f4080718ca | -7.87977 | -61.81603 | 2025-08-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b905e42e-959d-31d6-bd97-bfc189b5a3bd | -9.50963 | -60.52343 | 2025-08-16 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| a8654826-ff3e-3fa9-8a5a-3b06db6a4395 | -10.11247 | -57.76714 | 2025-08-16 05:23:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a091b497-7054-3afb-8c00-6bc320998157 | -8.99624 | -60.52608 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 96c4faae-a356-3ae9-8cc5-629e80f00812 | -8.98959 | -60.52504 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 1bce871f-157e-33c1-bb4f-692791adc724 | -8.40506 | -70.44047 | 2025-08-16 05:23:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b2cbf434-15c4-33db-aa85-50e29dfbbeb6 | -9.21312 | -59.63711 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d29030b0-4c80-3357-b2fc-53399976bf1f | -9.92022 | -60.44194 | 2025-08-16 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d778b9d2-75a2-3c60-aa3b-954f55b50e00 | -8.97796 | -61.71273 | 2025-08-16 05:23:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 30.1 |
| f7a3ccc9-b1a3-3d94-9b04-a574a124d09c | -6.93644 | -59.55441 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c532de57-cebd-3317-85ca-96aee8efd2dc | -7.44905 | -59.93512 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |


[Clique aqui para ver as próximas entradas](README54.md)

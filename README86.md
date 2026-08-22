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

## Dados Diários - Página 86

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 340ca921-0fef-38a2-8ba3-f72f388b2774 | -6.8018 | -59.4201 | 2026-08-22 12:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 121.4 |
| 97b9bcd5-2026-3be4-8f4b-26816b797b43 | -11.4494 | -44.5353 | 2026-08-22 12:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 306.1 |
| 4d4b0c9d-fb25-35b2-9df9-fb7f233484bd | -8.5406 | -54.8197 | 2026-08-22 12:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 135.0 |
| 22c5616e-bf61-3e0e-95e1-d8d345b3a0dd | -6.8569 | -59.4564 | 2026-08-22 12:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 83.4 |
| 97aa03fe-4a69-35f1-b50b-84452a7e89d0 | -13.5481 | -51.7403 | 2026-08-22 12:50:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 205.3 |
| f4831060-1d0a-358a-8d0d-eaf2fb8fc2e8 | -11.625 | -46.5484 | 2026-08-22 12:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 146.4 |
| 2f37542e-7196-3e47-bdfb-3649aaf63c6e | -8.5404 | -54.8398 | 2026-08-22 12:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 107.5 |
| 03ca19ec-f09f-30c5-9faf-43116f79f562 | -6.8568 | -59.4757 | 2026-08-22 12:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 81.6 |
| c8888e6b-e185-3b9c-894b-947365684631 | -8.4739 | -46.9831 | 2026-08-22 12:50:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 51e7ed69-36b0-3f4f-a44e-160a6fd40acb | -11.4298 | -44.5615 | 2026-08-22 12:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 3d179986-30c1-32e9-9c78-ba29be96becc | -16.1279 | -43.6194 | 2026-08-22 12:50:00 | GOES-19 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 03129137-200c-3883-9131-ab7983b62267 | -6.8017 | -59.4394 | 2026-08-22 12:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.9 |
| b0090889-893e-33e7-b1ac-81d09bd72a60 | -8.5221 | -54.8007 | 2026-08-22 12:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 1c5803bf-e2e1-3d68-a50e-003980a7dfc4 | -7.0191 | -48.0323 | 2026-08-22 12:50:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 42a590b6-24d2-313f-8ca6-d49603e9dc7d | -6.7878 | -58.6477 | 2026-08-22 12:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 89.1 |
| 2db8f4ab-9e47-3ea9-93cc-3e3bb9f735d4 | -12.281 | -43.1574 | 2026-08-22 12:50:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 114.2 |
| 9f4f1164-9264-302b-b8da-8cef427d2c62 | -17.6092 | -44.6119 | 2026-08-22 12:50:00 | GOES-19 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 146.5 |
| d2d231f4-02af-3648-87e7-0db1b5aef4a8 | -6.7833 | -59.4208 | 2026-08-22 12:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 93cab2a2-ef2c-3348-9e9d-b2c5e21010b1 | -6.254 | -55.391 | 2026-08-22 12:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 115.8 |
| bb71a387-d038-3675-9c4a-e499c59dcc14 | -10.9435 | -51.4234 | 2026-08-22 12:50:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 101.9 |
| 3697b548-0236-3a7f-a6ed-a1175720d9df | -8.5408 | -54.7995 | 2026-08-22 12:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| a16a5d6d-21d7-3b91-b37d-373528dc1936 | -6.8062 | -58.6469 | 2026-08-22 12:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 111.6 |
| dba0f939-d08c-37a3-b4a3-d1e473a4399e | -9.1722 | -59.4629 | 2026-08-22 13:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 81.0 |
| e4068d2c-f77a-36fd-940d-2f03144f2075 | -6.254 | -55.391 | 2026-08-22 13:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 109.1 |
| 6e5af214-039a-3b41-bea9-7a0105ec8f6f | -6.8063 | -58.6275 | 2026-08-22 13:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 05a25b4d-2bfb-304b-b480-817d07b88746 | -8.3904 | -62.6774 | 2026-08-22 13:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 70.4 |
| b7361fef-66cf-3dc2-a4fa-8f2efa1ac56d | -8.522 | -54.8209 | 2026-08-22 13:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 147.1 |
| 3525d630-aef5-3b3f-b05c-c01195f17716 | -6.8569 | -59.4564 | 2026-08-22 13:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 93.2 |
| 64b430c3-18c4-328f-9dd9-245b54294ada | -6.8017 | -59.4394 | 2026-08-22 13:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 1bc99465-4d9e-3b25-9eb3-36b96b1737eb | -6.8188 | -59.6696 | 2026-08-22 13:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 99.5 |
| 0233aacf-99a5-3060-b919-1f55f2802023 | -11.1351 | -46.185 | 2026-08-22 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 6d676dad-cd58-37d8-aa7e-32908edb6af7 | -12.281 | -43.1574 | 2026-08-22 13:00:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 147.2 |
| 37b2dc17-db0b-36b2-93b8-6edcfd2999b9 | -6.8018 | -59.4201 | 2026-08-22 13:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 127.7 |
| bd1d85d6-1fd0-3942-9334-c8c1c78519f6 | -8.5406 | -54.8197 | 2026-08-22 13:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 158.3 |
| 0c5ae103-1239-331b-b303-6adf886ae7fc | -6.8005 | -59.6511 | 2026-08-22 13:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 135.5 |
| 9542888f-f71d-3389-86ef-607ddb5c4c8b | -9.0535 | -45.8715 | 2026-08-22 13:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 116.9 |
| 4b621e93-c484-3a68-9a7d-7f28537d834e | -6.7833 | -59.4208 | 2026-08-22 13:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 809203b7-8b70-3369-bf55-27dd197ba9cc | -8.5404 | -54.8398 | 2026-08-22 13:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 104.4 |
| 34e4a880-4e6c-301e-b2cd-1174c11977e8 | -6.7879 | -58.6283 | 2026-08-22 13:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 3796cf7c-d8f6-3c49-a0aa-eedd7bb6e313 | -11.4494 | -44.5353 | 2026-08-22 13:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 302.4 |
| 13373000-9426-32bf-9226-dd34ed108d3f | -12.8362 | -48.4567 | 2026-08-22 13:00:00 | GOES-19 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 00dbf512-a36d-3e6e-9244-19a286b5d3c0 | -8.5408 | -54.7995 | 2026-08-22 13:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 2955c9ac-dcb2-3e09-9507-af46dbec6973 | -6.8062 | -58.6469 | 2026-08-22 13:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 91.6 |
| b0c5b524-1be2-3ea4-82ec-7bb63306afc5 | -6.7878 | -58.6477 | 2026-08-22 13:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 152.0 |
| 3616ed9b-b2fb-3f50-8772-e3e7111a4ee0 | -8.5221 | -54.8007 | 2026-08-22 13:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 8d11dffc-368a-37fa-a311-864ec72a8b80 | -13.5481 | -51.7403 | 2026-08-22 13:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 258.7 |
| 35f413b0-8d36-3d4a-9550-487bc00e313a | -8.4739 | -46.9831 | 2026-08-22 13:00:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 0c285c54-7518-36cc-8280-d205b7503004 | -6.7832 | -59.4401 | 2026-08-22 13:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 7a8e1744-981b-305c-9585-e1f4cf246b2a | -8.5218 | -54.8411 | 2026-08-22 13:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 73ce24c7-b810-3505-a695-9e2cdebec3e8 | -11.3663 | -46.0405 | 2026-08-22 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 6e803c10-9a05-37dd-a6f4-45c4c9f37de0 | -9.0346 | -45.8735 | 2026-08-22 13:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 119.6 |
| fca5ad22-5fce-3782-be1f-13ef5f7ed1f0 | -16.1279 | -43.6194 | 2026-08-22 13:00:00 | GOES-19 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 97b67c7f-a23e-3edb-a34c-671de495b33d | -6.7691 | -58.6873 | 2026-08-22 13:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 65.3 |
| bdc2ba89-b8d4-31ba-b4cc-607fde9b5f32 | -8.9936 | -50.7215 | 2026-08-22 13:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 89.9 |
| 2fc6ff50-f328-3234-bcf6-a343d24f1a65 | -9.1724 | -59.4436 | 2026-08-22 13:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 7b889add-94ee-3654-99b2-ec9a0a10c9bf | -17.6092 | -44.6119 | 2026-08-22 13:00:00 | GOES-19 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 151.6 |
| da48a26c-dc5d-3f6b-976f-10bcb51ac126 | -6.8568 | -59.4757 | 2026-08-22 13:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 7556d6b5-ff98-3bb0-a787-23d4af157276 | -10.9435 | -51.4234 | 2026-08-22 13:00:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 112.9 |
| dadd0fb7-c906-3ee4-a85f-9af1429876f4 | -6.8004 | -59.6704 | 2026-08-22 13:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 236.4 |
| d10fe72f-1241-34e5-a45f-3cfd32d07b33 | -12.2806 | -43.1813 | 2026-08-22 13:00:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 119.3 |
| a626b699-18f1-389f-a17d-9b23a3bb8e70 | -10.9624 | -51.4214 | 2026-08-22 13:00:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 175623e3-8bb0-3f26-875e-3dd7341c46c9 | -6.8991 | -55.7176 | 2026-08-22 13:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| e73222ed-31c3-384c-9329-7f35f449f80c | -6.7692 | -58.6679 | 2026-08-22 13:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 97.2 |
| d0455811-ae0d-3258-8763-1961fe925e7c | -17.5891 | -44.6164 | 2026-08-22 13:00:00 | GOES-19 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 157.4 |
| 61276710-7a32-30b6-a61b-d1c11a8b62f5 | -6.7832 | -59.4401 | 2026-08-22 13:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 86.1 |
| f348e8c5-6b2b-3de9-87f3-bdcaf11c8fed | -11.4494 | -44.5353 | 2026-08-22 13:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 267.8 |
| f0502abe-948d-3b1c-9959-8e9ca46ce1a6 | -17.6092 | -44.6119 | 2026-08-22 13:10:00 | GOES-19 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 189.0 |
| 01d372b4-542b-36d9-9e08-7c8ca9257d79 | -11.6063 | -46.5284 | 2026-08-22 13:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 173.3 |
| 5833f9d8-58da-39c3-a978-0a752065d043 | -6.8004 | -59.6704 | 2026-08-22 13:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 272.5 |
| 1272abdb-b35f-3407-812a-ca349c66a685 | -8.5404 | -54.8398 | 2026-08-22 13:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 112.4 |
| 5d628f92-1af3-332d-b007-b29dccbcb433 | -13.5481 | -51.7403 | 2026-08-22 13:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 191.4 |
| 4b6f3b3a-e30c-399f-a78e-46f681e5b44f | -6.8568 | -59.4757 | 2026-08-22 13:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 89.0 |
| ba37c959-e657-37a0-9c57-85cbdf8e5449 | -10.9435 | -51.4234 | 2026-08-22 13:10:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 43ae352a-e179-38d3-bc00-3f632d18f0e1 | -11.6055 | -46.5736 | 2026-08-22 13:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 532.9 |
| 6d24349a-f502-3055-9cb1-40b317c15fa0 | -9.0124 | -50.7199 | 2026-08-22 13:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 6677ccb9-a350-3cfe-b114-aa1698dd7663 | -12.281 | -43.1574 | 2026-08-22 13:10:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 137.7 |
| c2379158-28f3-3c51-81af-c094d00b6b30 | -8.4742 | -46.9609 | 2026-08-22 13:10:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 6141007b-639e-3228-b091-0bbbea178f34 | -9.0343 | -45.8961 | 2026-08-22 13:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 98.8 |
| adc244cc-2b3b-3d6d-9eef-963dafa6c8ad | -11.3475 | -46.0203 | 2026-08-22 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 278b5ca8-c3ff-3df2-99d6-6b8fc9c88528 | -16.1279 | -43.6194 | 2026-08-22 13:10:00 | GOES-19 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 106.2 |
| 711b2e89-04a1-31ab-af3c-86957220b301 | -8.522 | -54.8209 | 2026-08-22 13:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 174.6 |
| f6dc81cd-133f-3011-85ad-809db7dad1a7 | -6.254 | -55.391 | 2026-08-22 13:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 104.6 |
| 6e9ca404-7a58-319f-bb37-73ac85a989a4 | -9.0535 | -45.8715 | 2026-08-22 13:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 109.8 |
| a241ad98-3a99-3e04-beb9-2a06bb393641 | -6.8991 | -55.7176 | 2026-08-22 13:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 80.6 |
| 07e81aa4-0990-322e-9a9e-f58ef881e2cd | -12.2806 | -43.1813 | 2026-08-22 13:10:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 107.3 |
| bfc5277a-6964-32d6-b3dd-0c3e82faea4a | -11.6059 | -46.551 | 2026-08-22 13:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1005.6 |
| 4a9c4c4b-552b-3627-946d-059d11b4a45d | -8.5408 | -54.7995 | 2026-08-22 13:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 87.6 |
| 3e773c67-fafc-32f0-9ce4-fb947d490d48 | -9.1722 | -59.4629 | 2026-08-22 13:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 1768461d-5e4a-3ef0-8502-7095cb6c1d23 | -6.8202 | -59.4194 | 2026-08-22 13:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 06bb3e40-c86b-373f-9c56-a3de1b6a5327 | -6.8188 | -59.6696 | 2026-08-22 13:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 104.8 |
| 120b4bc6-96c9-3698-8a91-306c014d0fcd | -15.1878 | -48.7448 | 2026-08-22 13:10:00 | GOES-19 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 9a13ba69-3c9b-33c2-a29e-f54590ecd162 | -9.0346 | -45.8735 | 2026-08-22 13:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 132.4 |
| 622f0f8b-5ba8-38ef-9974-42116da9bd53 | -11.5864 | -46.5762 | 2026-08-22 13:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 165.9 |
| bbf8dad2-7556-3f37-b365-0ee56bb1a807 | -6.7833 | -59.4208 | 2026-08-22 13:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 87.9 |
| 3c8b0f9c-921e-374b-9537-fca32fc878dc | -6.8018 | -59.4201 | 2026-08-22 13:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 135.4 |
| 349584bd-6c8c-355b-9f49-e36667cd96d7 | -11.3667 | -46.0177 | 2026-08-22 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 108.0 |
| e87ab8b5-bc5f-3022-bc98-45ae8b1d065d | -8.5406 | -54.8197 | 2026-08-22 13:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 183.9 |
| 8e4cd99f-116f-3438-aaa0-bfbe7ba833a4 | -8.9936 | -50.7215 | 2026-08-22 13:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 127.0 |
| 203f1a9e-e18a-31f8-b18b-5212f3303bc0 | -11.4498 | -44.512 | 2026-08-22 13:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 1dddfaad-eac5-3feb-a6a1-8323795f1abf | -11.3663 | -46.0405 | 2026-08-22 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 149.6 |


[Clique aqui para ver as próximas entradas](README87.md)

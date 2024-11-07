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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d9300d2a-4152-3ca4-9be9-0ac7f7e86a0d | -5.50285 | -43.79428 | 2024-11-07 04:18:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c07ce117-bc27-3ad3-9e96-4a6c5b6ec1c9 | -5.4478 | -43.58201 | 2024-11-07 04:18:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d027d35c-aded-33fc-b062-cea5f6860407 | -1.14947 | -53.74321 | 2024-11-07 04:18:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 804e2e04-2a2b-3d13-92bc-915b87693fc4 | -3.65947 | -52.34076 | 2024-11-07 04:18:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c69b8d66-0f06-3fa3-b84f-659ce4f71818 | -1.40857 | -54.49308 | 2024-11-07 04:18:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c69d6366-38e0-3ae8-b446-2eae344e6358 | -5.97824 | -45.56581 | 2024-11-07 04:18:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3e3f6340-1269-319b-b62d-226be6e8a08f | -2.82176 | -52.96687 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8cbebddf-cbe9-3137-937e-aa0214a263df | -3.15419 | -50.20543 | 2024-11-07 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1e1a5998-a122-311c-a61c-a761236e9d02 | -3.78211 | -47.73231 | 2024-11-07 04:18:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 59ef0417-32ca-30bc-b5f0-d849335f41bf | -2.23425 | -53.67545 | 2024-11-07 04:18:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| cf3190ee-0032-389d-a4d0-bea5853d6ac7 | -3.18152 | -50.58617 | 2024-11-07 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 70efed53-1c23-3a6d-9e30-1c5a5c3c0b5a | -7.85255 | -48.21135 | 2024-11-07 04:18:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ab10e1be-91df-3b14-b5ff-780cc7ebd4f0 | -3.72694 | -52.27527 | 2024-11-07 04:18:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f232bbc3-451b-38b3-b7cc-d5153e0d04c2 | -2.22595 | -46.89781 | 2024-11-07 04:18:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4417c9a9-a4ec-360e-a158-f9deb2a03eaa | -2.87443 | -51.30798 | 2024-11-07 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 928ce191-82cf-30a8-b22c-a5b1c4228e74 | -7.21008 | -43.90907 | 2024-11-07 04:18:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f20b71c6-40f3-306f-b878-72b95bc42b13 | -2.41264 | -47.78341 | 2024-11-07 04:18:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4cf80b0d-dae3-3265-9d5e-af7a7a896584 | -5.72661 | -43.81866 | 2024-11-07 04:18:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1e5cb0c5-c21c-3058-8fb3-8a399e592c54 | -4.76442 | -45.74067 | 2024-11-07 04:18:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f1fefa35-b46d-3b12-b71e-b9edca10667b | -5.32783 | -46.10317 | 2024-11-07 04:18:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f016866d-0300-3179-9a7b-b2b91a39896e | -5.9849 | -45.56686 | 2024-11-07 04:18:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1589a46f-e210-303f-af59-957a8dac8ec1 | -3.25356 | -46.46609 | 2024-11-07 04:18:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4cddd2a9-093e-3151-a6a4-cae904db0f86 | -5.4584 | -46.22807 | 2024-11-07 04:18:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 11bd9a50-4e1a-37d1-b7c5-4684bdf4ca09 | -2.42674 | -45.81907 | 2024-11-07 04:18:00 | NOAA-20 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d02a4c94-003d-3a4e-9c49-e103752513c1 | -4.51856 | -42.87046 | 2024-11-07 04:18:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 09b0bcc2-8d18-3fc6-b4b4-8ec5c032149e | -3.97574 | -48.40298 | 2024-11-07 04:18:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c82033e5-8c22-3a9a-be70-0bfb7cb5d972 | -4.11107 | -48.50443 | 2024-11-07 04:18:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a850f0e9-189b-308e-8699-12844da1e5c9 | -4.3756 | -48.58938 | 2024-11-07 04:18:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 99576e31-d638-385b-bf0c-f7022d3472fe | -6.68511 | -46.18726 | 2024-11-07 04:18:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 49aa93e8-c715-34b1-b01a-9627b15b3e6d | -2.24189 | -47.66456 | 2024-11-07 04:18:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 616f1c4b-2a9f-3622-8a26-b9596004963d | -3.03928 | -48.03244 | 2024-11-07 04:18:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ba029d7a-380c-3920-8382-6a79000c014a | -3.71802 | -51.20499 | 2024-11-07 04:18:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6d77bc9f-a759-31f1-9c97-0d0c9865638a | -3.1417 | -51.20142 | 2024-11-07 04:18:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1ef51342-7289-3c01-9e8f-ae0764552670 | -5.83997 | -46.23592 | 2024-11-07 04:18:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4691d809-faa2-35dc-b78f-99c274b03953 | -9.14534 | -37.09943 | 2024-11-07 04:18:00 | NOAA-20 | ÁGUAS BELAS | PERNAMBUCO | Brasil | 2600500 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d256bba4-5d21-37db-bd5e-48273867ba3a | -4.10723 | -48.50375 | 2024-11-07 04:18:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7f4ba06f-eaab-3702-9f2f-39d123d5da85 | -6.50606 | -44.67865 | 2024-11-07 04:18:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 118cfd1b-2a35-3382-bf76-723502a26295 | -2.84167 | -52.91219 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b08dcd9a-7068-3303-ba2a-26c95134132e | -5.54763 | -41.67495 | 2024-11-07 04:18:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| e71ebd52-4c9b-3e3a-bb53-e0c43d52b96a | -5.93369 | -43.77546 | 2024-11-07 04:18:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bd1898a3-dd3d-3ad3-b637-bf27ab7b17fc | -6.29008 | -43.7561 | 2024-11-07 04:18:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0e721ffb-1ad1-3d86-936c-3bdf65d6c270 | -2.82102 | -52.9057 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 005102dc-cffe-3c8b-bf65-56a21d9c2d71 | -7.5447 | -42.84918 | 2024-11-07 04:18:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| bcd37cfd-b4f9-308c-af80-ba23b94b8ea4 | -3.66508 | -50.25624 | 2024-11-07 04:18:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e2a4a5d9-bdd7-345f-828e-c1e53ed07873 | -2.79987 | -51.49422 | 2024-11-07 04:18:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 72743923-6d0f-3473-90d9-e7516db395fa | -4.47995 | -50.48715 | 2024-11-07 04:18:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 48201320-8e2a-3be1-b479-8e1231942ecd | -1.13413 | -53.72019 | 2024-11-07 04:18:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 690ab4ef-4ca9-341f-982e-6b31a59dc2a1 | -5.61796 | -45.93015 | 2024-11-07 04:18:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 02eddab6-99ca-3855-8abc-793740639d02 | -8.30613 | -43.6203 | 2024-11-07 04:18:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 70be6d80-98bb-3b8e-baa1-1cffc154ff96 | -2.86748 | -49.54586 | 2024-11-07 04:18:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2d40d4e3-6550-3b7b-a3db-85f8775ac406 | -2.281 | -53.81321 | 2024-11-07 04:18:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c4fcadd4-57fb-3270-8527-e4c056d4e466 | -3.56235 | -52.69719 | 2024-11-07 04:18:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9413aa47-8dbf-3b05-94c0-a8a22ca0fff9 | -3.02628 | -53.26524 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 048b3bd4-28f2-3777-99d6-f89ef5ffe7db | -1.13631 | -53.71599 | 2024-11-07 04:18:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d709f742-2873-3641-b39e-c42aef145627 | -5.04418 | -46.84565 | 2024-11-07 04:18:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d935dd94-bd0d-3ce6-8b2e-f95a5cdc3754 | -2.83757 | -51.35413 | 2024-11-07 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 50bd7816-9890-3500-adc0-f0d38eb3c2c7 | -2.62091 | -51.2984 | 2024-11-07 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f46604e0-aa45-3627-a7ac-2ada3db9046e | -4.34419 | -48.62618 | 2024-11-07 04:18:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 91758198-8ba1-3c12-a3dc-ca55bd39e10b | -3.71383 | -49.00007 | 2024-11-07 04:18:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| b5b85c03-ea6a-3e9b-85a6-833fc9112939 | -5.83866 | -46.26566 | 2024-11-07 04:18:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1401e954-b3a6-3480-951d-50e06da76e64 | -2.42978 | -53.66411 | 2024-11-07 04:18:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6986bd58-067d-39a7-b77b-cd758483d20b | -2.60941 | -51.30454 | 2024-11-07 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0ec3c658-cb2d-36e9-898b-1adfe118a4b2 | -2.38561 | -48.51593 | 2024-11-07 04:18:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f555402a-46a5-34be-8892-282ed089141d | -2.75643 | -53.22705 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d0785b22-c2a1-3841-9b3b-e9a727129d85 | -5.94034 | -43.7765 | 2024-11-07 04:18:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 75db2f6d-fd99-3b42-ac09-023f690880cf | -3.52726 | -50.35152 | 2024-11-07 04:18:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 85563546-bab4-3304-bb40-4aa56832fc58 | -7.29056 | -45.98745 | 2024-11-07 04:18:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 895ee4a4-575d-394b-bdc9-82933a35a1c8 | -5.3887 | -46.68638 | 2024-11-07 04:18:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 698da2e8-06d9-3212-9298-b356e8ed8d77 | -2.61972 | -51.30102 | 2024-11-07 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| ecfc68fc-2270-3369-8612-e9a5392f6314 | -3.21412 | -49.22873 | 2024-11-07 04:18:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 23aa93d7-e60c-39bb-a2b5-01da8e9ba085 | -2.8081 | -52.9506 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 4e81f686-bcf9-3754-b322-e305b76a59c1 | -2.84406 | -49.45167 | 2024-11-07 04:18:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 23e7bfb5-9e4f-3e1b-82fa-389da2544f6b | -2.42614 | -45.82278 | 2024-11-07 04:18:00 | NOAA-20 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 76fddc2c-9367-3c7e-9559-cd5cc97e3be8 | -3.37379 | -52.36208 | 2024-11-07 04:18:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a10f5ce9-f869-376d-9eef-5b24cd031e9a | -2.60496 | -51.30625 | 2024-11-07 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 13707d8c-1739-39b7-8d26-2fc5a9fc6d31 | -8.05593 | -42.93964 | 2024-11-07 04:18:00 | NOAA-20 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 0ab8789e-a64a-301f-a9b5-32599580129a | -1.13561 | -53.72021 | 2024-11-07 04:18:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 9e67498b-2036-357f-aeed-4010bf016f91 | -6.50179 | -44.68116 | 2024-11-07 04:18:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 96743eab-395f-39b6-b994-a2ea69731bf0 | -5.92944 | -43.64928 | 2024-11-07 04:18:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4534e3a8-242f-3245-a1ab-8efb21cc160c | -8.50908 | -42.10078 | 2024-11-07 04:18:00 | NOAA-20 | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| a5c4b951-3c9e-3d00-b816-9f5719d1efc7 | -5.50725 | -43.78784 | 2024-11-07 04:18:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1ec9f21f-119a-33b3-9af4-694a8e2c7fe6 | -2.84937 | -51.78023 | 2024-11-07 04:18:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 99154401-7840-34cb-b0b0-787bfb1712e2 | -4.25462 | -50.69939 | 2024-11-07 04:18:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ecf589f2-c0e7-3f63-96ac-a800c738cbc7 | -1.13765 | -54.22113 | 2024-11-07 04:18:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| db09ca11-3ff1-3f76-b052-c1a77798a309 | -8.50791 | -42.08419 | 2024-11-07 04:18:00 | NOAA-20 | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 627702a8-42c8-3c4d-9328-58b9e07959df | -2.24112 | -53.66887 | 2024-11-07 04:18:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 076daebe-f87d-3d5e-b42d-7f7996f5d36f | -3.44654 | -52.01208 | 2024-11-07 04:18:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c866a338-cdb3-3073-9992-4a0987a9cc75 | -4.34527 | -48.62889 | 2024-11-07 04:18:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 35c85901-6bc7-36d8-941f-2bca5c20b969 | -1.39043 | -52.21169 | 2024-11-07 04:18:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5aab73e7-f9a4-30bf-b536-0d44df34cc59 | -2.08012 | -52.04634 | 2024-11-07 04:18:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 513915b2-8a1b-398d-8a32-d61c9d2b9398 | -2.82304 | -52.92625 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d5c33442-a8f8-325f-89c8-b3053d1fd556 | -2.81571 | -52.90499 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c2a149c8-60c7-3ae2-90c3-676c0a3150bd | -3.70528 | -49.00225 | 2024-11-07 04:18:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| cc23b74b-66ab-31d6-901e-f81f693dd705 | -3.03654 | -53.27038 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b534231c-3573-3557-950e-ab873d3456de | -1.38837 | -52.21307 | 2024-11-07 04:18:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4e460d66-8602-3d7a-b012-6e2500511b0c | -2.75162 | -53.22263 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1eb34400-7ef0-3235-bbb1-49b0b2595b9e | -2.81664 | -52.93202 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b8327d73-fd4b-308c-a054-0e282da027c1 | -2.81289 | -52.95462 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| a1ca4e5a-aa6f-3b88-94c8-249d2024b80a | -5.43529 | -45.13259 | 2024-11-07 04:18:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ff859463-5320-39ac-aab5-42b84263a407 | -5.04643 | -46.85395 | 2024-11-07 04:18:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |


[Clique aqui para ver as próximas entradas](README29.md)

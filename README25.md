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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4054eb20-4a17-398d-9724-266fbe4c1dcd | -6.65376 | -58.83799 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7caf5ee8-b9f6-3575-8ed3-8f92d83a3e77 | -6.6354 | -58.85886 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b277ec1f-97a2-3145-950f-d0337dbefce1 | -8.60449 | -64.03445 | 2025-07-27 05:48:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7fb34936-8f03-393d-871e-89d7ed94fd22 | -6.62117 | -58.8511 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 90c68927-dbd4-3f78-9e00-fcaea0744c2b | -6.66029 | -58.8252 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a6c3465c-7872-34a6-9a5e-f4763bf4728f | -6.64666 | -58.85168 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| eae1042f-af17-3df3-af48-546d53e339e4 | -6.54386 | -56.1879 | 2025-07-27 05:48:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f8650950-121f-3380-88b9-6c287014f570 | -6.68761 | -58.84976 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 87b933ab-610d-385f-85d2-b5e91bb7a6dd | -6.66793 | -58.84407 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8151bff3-9d23-39b2-b19d-fc299314496c | -6.67175 | -58.85343 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ad387b17-6488-39a6-bd07-d01dec9e6d26 | -6.54923 | -56.19315 | 2025-07-27 05:48:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 52a4910c-1a67-3885-b6b2-a415e9c08151 | -6.68219 | -58.85191 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6453ce45-e7b7-3e44-b11b-771108bc623c | -9.02904 | -59.76441 | 2025-07-27 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 5a101ec3-df6c-375a-bb7a-683cb8c649ca | -6.64866 | -58.83529 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3469d580-d208-387d-afc0-d25ceda2cea6 | -6.65669 | -58.85312 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2b45520a-745e-3126-924e-e84e8b14e5e3 | -8.97792 | -61.51061 | 2025-07-27 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 68477292-0b56-3fbc-93fc-9bba7d5650b4 | -6.67295 | -58.84477 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 197ae623-c3e3-3e8f-98cb-c74edcba98c8 | -6.65461 | -58.83218 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c5750f28-df5a-3e3d-92dd-893695fd917a | -9.202 | -60.82608 | 2025-07-27 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5d7b3e8b-3513-3624-ac09-e8508d9b7a30 | -8.66461 | -63.85511 | 2025-07-27 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0009ea4c-ce09-3db8-a01b-61bfa13fd0b8 | -6.64541 | -58.82487 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 90d27799-6208-3e84-8436-d855426fc082 | -6.67876 | -58.83978 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 24ba48b8-92ba-3b38-9e40-ae522ef832c2 | -6.67454 | -58.83327 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| de31f11d-6a80-3c16-a613-16d9922c1df0 | -6.6592 | -58.83581 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 69f94935-9c32-3b8d-8259-8d58a1244f38 | -6.62822 | -58.83759 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 04ce1ccb-78a7-32b2-8689-4189c401d283 | -6.6571 | -58.85028 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9793af2c-a539-30f6-889e-97350c626e29 | -6.6525 | -58.8467 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 662bf58f-22c0-3186-9703-5560d3c4a2f7 | -7.29066 | -60.18153 | 2025-07-27 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e28edcf1-b499-3275-b36c-0477dfbca49a | -10.03703 | -59.11079 | 2025-07-27 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b8b59c21-6a22-37a9-8b1a-4b54059d9cd9 | -6.65909 | -58.83389 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 57e4f31d-d352-391e-aa41-fff4d953be80 | -6.65084 | -58.85813 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| d1b24d66-e15f-34db-8975-b5f95aa032d1 | -6.65878 | -58.83871 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7c8b619e-0590-3100-b095-2bc4a27253f2 | -6.64542 | -58.8603 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 4fc2766d-e55a-3487-9e5f-b02c8e2de99b | -6.67996 | -58.83112 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e45a1945-13cb-3735-a034-26514a5108d0 | -6.65962 | -58.83292 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a71dab12-3c75-3202-b6ee-31f921bbcdb5 | -6.63119 | -58.85257 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| db191643-3c46-3048-82cd-fbe686e0aa21 | -8.07328 | -63.86762 | 2025-07-27 05:48:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6fe4d060-f923-35de-86ac-cd2fa8b4e642 | -6.63499 | -58.86169 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a0d660f1-0d50-3679-8fb1-a16775470510 | -6.64668 | -58.8498 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7f4bb6ab-1720-3fed-8476-7da92e7f1aab | -6.63079 | -58.85538 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| a6ac4728-b0a0-3cb0-8373-e79c260fbb23 | -7.55786 | -61.40674 | 2025-07-27 05:48:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8804b76c-f05a-33e0-849d-0f1cf96951ab | -6.65126 | -58.85526 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 3512f589-0152-3eea-84ee-7214c1e17416 | -8.68491 | -64.22478 | 2025-07-27 05:48:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 294242e0-92f7-3cbe-878e-27e7e750b29e | -6.65328 | -58.83897 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 45980ab0-296a-3d42-b6e7-d6e679ac24c9 | -7.49346 | -63.82019 | 2025-07-27 05:48:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 74e55ce1-8f1e-33f3-9074-b3a09877aeaa | -6.63159 | -58.84976 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5e3ad1b1-933e-3b6f-bc35-f650ed1db4ae | -9.34946 | -64.6497 | 2025-07-27 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2afdb103-92ca-3d00-999a-86fb2a7d4c16 | -7.56212 | -61.40733 | 2025-07-27 05:48:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3abaecf3-0ba4-31f6-9a7a-69e16f91227d | -6.67757 | -58.84832 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| af498994-efb0-36d5-9545-d4b46127ccd0 | -6.67916 | -58.83693 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0c145037-650f-31f6-8a75-25f5302f47e4 | -6.68841 | -58.84403 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9477fa47-0136-3153-ad50-eb44740d33de | -6.67215 | -58.85054 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 564003e0-a8fb-3c30-b093-0b6600b5ef5d | -10.03782 | -59.10456 | 2025-07-27 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e5a8a3ac-3f1a-3498-8917-d2c536e05299 | -6.64373 | -58.83654 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3a0abae7-e0ff-3f11-bf06-7e75fcdb023e | -6.53786 | -56.18722 | 2025-07-27 05:48:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f17f6407-b0ca-30ff-b9dd-88274419cf56 | -6.64246 | -58.84534 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e43b39a6-4e5a-3ef2-b82d-0016c678a8d3 | -6.54324 | -56.1924 | 2025-07-27 05:48:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2e58991c-be5e-350f-824b-90371c0b6ea9 | -6.65836 | -58.84163 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ad5e9e8f-384e-3499-818a-eb9f9e77791d | -6.65334 | -58.8409 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2635ad7b-97ea-3ab4-a858-5da9e9d0838c | -7.57182 | -61.40057 | 2025-07-27 05:48:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fc9b6c8c-49b2-3c0b-9df0-1d00fd666054 | -6.65592 | -58.85699 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 8e3ef763-0b60-354e-8899-9319b8239ddd | -10.03672 | -59.10226 | 2025-07-27 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 356e4e00-a2b7-31ec-bb40-3b84b446732b | -6.63827 | -58.8389 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3747589b-6427-320a-97a2-e1e1493763fc | -6.62658 | -58.84905 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 30d61bd4-eed6-382a-a779-f63555c4260f | -7.17106 | -59.82687 | 2025-07-27 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a432f445-821b-383a-868a-5bdb1c873668 | -6.64628 | -58.85268 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 6b97ff83-d677-3720-b823-a662adf291fe | -7.56756 | -61.39995 | 2025-07-27 05:48:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5478912e-7938-354b-8551-f23258f41d17 | -6.64747 | -58.84404 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a717d69e-a3dd-3d95-8632-f0d4c0415e2d | -6.65749 | -58.84554 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9e4c1fa5-cd0c-3903-8889-9c1c5c517eab | -6.66713 | -58.84984 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3deaf49b-2cec-33cb-95e1-c8cdaf670512 | -6.63367 | -58.8353 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ac6fc081-d583-3ac6-a627-13693afb433c | -6.6509 | -58.85627 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| d6eb50c0-22b0-390a-891e-b8d0f17db67c | -6.68299 | -58.84616 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 18b1d644-33de-3568-9ba7-a3efe829ca96 | -6.64946 | -58.82947 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4dd70d32-d0ff-34ca-86aa-cde94dc946f2 | -6.65407 | -58.83315 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 746aa06c-3096-35ab-9dc9-da0ee9b7806a | -6.64331 | -58.83948 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 60ed4e22-a785-3c61-aa33-c585c4ac5bdb | -6.62578 | -58.85468 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| fb574562-c218-387b-bf0b-63a28b37fb11 | -6.63785 | -58.84184 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bb297ed1-4fc8-3315-a949-c9f9446c17c0 | -6.63241 | -58.84409 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 675ca472-e439-39d4-95fc-1b392c359b1d | -6.66873 | -58.83829 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 28be3c46-c2d1-3163-94bd-c9f0747b298d | -6.64833 | -58.84015 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 66246025-c7fd-3ac1-ab45-bf7af7d736dd | -6.65631 | -58.85413 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 104539f6-519c-3e08-9481-c851dc78ca49 | -8.6046 | -64.03586 | 2025-07-27 05:48:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 552beb18-6503-3585-8138-f07d0c232bfc | -6.63662 | -58.85041 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7330e109-5db5-3586-b547-515fe9cde911 | -6.63452 | -58.82936 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0641376c-d7df-33c3-8c7b-df434e3ec8d5 | -8.60323 | -64.04311 | 2025-07-27 05:48:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b3369ab3-7844-36d7-a72c-50ded0fe1229 | -6.64041 | -58.85957 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 75ef22a9-a53e-342c-b307-3f095e099b68 | -6.64082 | -58.85671 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| b2d369ae-8a1f-33fb-8053-67c676361965 | -8.60753 | -64.03934 | 2025-07-27 05:48:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d5490be3-58ec-376f-b62d-c8821f3c65db | -8.07762 | -63.86382 | 2025-07-27 05:48:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 62461aea-d158-325c-a25b-88c383ad2432 | -6.68801 | -58.84689 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1073fc3e-e1dd-3958-88c2-30d5b410357c | -6.645 | -58.82777 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8186abd4-c6b7-3b36-8bd5-70f4653ca5bc | -6.64791 | -58.84306 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ccb5ad3a-cc18-368c-b58e-a42fafbd42fd | -6.49364 | -56.19905 | 2025-07-27 05:48:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6680816b-94ea-3326-ad7d-46e8301351a0 | -6.66411 | -58.83464 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 22575eb1-ba95-3ba7-9dd6-2de9f13e41de | -6.6387 | -58.83593 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 101f6084-9be3-3b2c-ab94-d375a1e09c81 | -6.64589 | -58.85556 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 102137dc-14fa-36a8-8aa5-0f9ffa138e72 | -6.65169 | -58.85054 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 06ef8ddc-c688-30a1-9e0a-a250101c7ae5 | -9.02838 | -59.76929 | 2025-07-27 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| dcec7f76-9b8c-3406-9487-485205f3d2c1 | -6.65829 | -58.8397 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README26.md)

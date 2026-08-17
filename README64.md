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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 50b22c75-7b17-39ec-b061-2c85b6282b0b | -8.72184 | -71.00943 | 2026-08-17 06:01:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5aaaf401-d0af-3394-87f7-7b1abcf4d4e4 | -7.5311 | -60.68493 | 2026-08-17 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dcb26390-62c0-3e07-9fe5-531d0a7a1c73 | -8.90152 | -60.55217 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 77c0149a-745d-393a-824c-598276371d52 | -8.95883 | -60.52937 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5db3e678-3fe1-36dd-b1a6-52997bd6cd2d | -6.70237 | -58.96621 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 44b7044a-5488-3ddf-9803-e2207e1ae7cf | -8.95635 | -60.53203 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 36469b4d-cd8a-3b21-b899-e3d68c51ab8b | -7.38054 | -59.99664 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a74597f7-c02b-369b-b97a-6c5323faad55 | -8.97694 | -60.52395 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ef60eb54-c79a-3925-958e-9889c2b36e2d | -8.97941 | -60.50408 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 47f58249-90ac-396d-a9dd-138a8e8e2fbe | -6.78238 | -59.4568 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9d6bd775-62b1-3b8f-b181-907c8c6a464a | -10.06303 | -62.45287 | 2026-08-17 06:01:00 | NOAA-21 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5e43a940-4986-321b-8d47-81f25ee02fee | -8.95444 | -60.56499 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fca8d20a-9ef3-3704-ab61-84204a1a1ff1 | -6.87601 | -56.41367 | 2026-08-17 06:01:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e244e233-aa15-37a9-8370-128772538118 | -7.43607 | -60.02189 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7c577655-1705-32d2-a014-bcc6409beddb | -6.85119 | -58.97688 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 32825850-5aa2-3357-9f84-49e772bb0377 | -10.06342 | -62.44981 | 2026-08-17 06:01:00 | NOAA-21 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6843afde-dbd8-3a8f-8aeb-f9d9bf98da36 | -6.62352 | -59.08162 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f5e6b631-57a3-32a9-b2dc-3411b5a291b8 | -6.61431 | -58.96791 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c73c53da-8099-3d3c-8326-dd6e930eaa47 | -6.96145 | -59.04076 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5f8df2ae-25d2-32c7-99ab-84cf8c042c1e | -7.42536 | -60.01769 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bae8c5c2-9355-3d6a-8e13-dfe3c168777c | -10.05243 | -62.45451 | 2026-08-17 06:01:00 | NOAA-21 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6ed17f28-b2d4-32a8-9a6b-46946adc8626 | -6.83893 | -58.97505 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 566b08ce-2093-3323-a3ef-8a7cf32613b7 | -8.95686 | -60.52811 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6150cc26-69f6-3762-9c39-25eca4838096 | -10.91557 | -62.76504 | 2026-08-17 06:01:00 | NOAA-21 | JARU | RONDÔNIA | Brasil | 1100114 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 76c68e4a-ecde-3939-9975-5cc9e24379ef | -6.71917 | -58.93356 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0c9adfc7-9767-30b9-98c1-b9439aaa8f34 | -8.8955 | -60.59946 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 65f20055-ac8d-3ad5-9a88-b14304de1920 | -6.62097 | -58.96892 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| aa644973-d77a-3834-99a7-e3af9894791e | -8.95966 | -60.56961 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0213a18d-41be-3f7d-badf-f8fb7918777a | -8.36544 | -70.83074 | 2026-08-17 06:01:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8ca6ebd9-a9a1-3e44-8aeb-f2be02f72c8a | -6.71857 | -58.93821 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fd1286a0-bc9d-3774-8c40-6639a2097fb2 | -7.61902 | -60.94815 | 2026-08-17 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 69f2b7df-5d05-3bf1-8615-55ef65e65829 | -6.62831 | -58.96043 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 12.4 |
| d96bb883-4dd9-37d7-8b70-ad32fce17cd3 | -8.96308 | -60.52501 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 97dbf46d-9e22-311c-b75c-bcd52a40c42d | -6.64008 | -58.96189 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 96854a3d-f16f-3743-8b2e-bada4639b27e | -8.94597 | -60.52246 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 17b3c2d2-8d1f-3e2a-8ad9-08202d1111f2 | -8.95155 | -60.58836 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 584e4f4f-fa48-3e1c-931a-94d593348d3e | -6.7036 | -58.95707 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7fc725ac-60cf-3373-942a-bc32ec97bb0e | -6.62587 | -58.97451 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c6bdc1be-125f-3fab-97f3-94b77a58f4bc | -8.90002 | -60.5639 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b646a725-67ea-3e44-9bbd-45fca81b48b4 | -8.9535 | -60.5726 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3fbc1989-e1d0-32f2-84cd-c6c843c23602 | -8.89533 | -60.55523 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| fa6d6c7f-bae9-3d8d-bfed-5083643e5a9f | -9.47568 | -60.50268 | 2026-08-17 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 435d7146-3f45-33fb-8731-34d8abb25ff5 | -8.96256 | -60.52897 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7715dc50-fb9d-3c96-9a78-a6e6baf59c9f | -8.95331 | -60.59951 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6a86c49b-bc66-31ac-a0a4-e8bcb054ee12 | -6.71846 | -58.93959 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 5075c578-a039-336d-a82c-2ee93a82abb8 | -14.50306 | -59.33459 | 2026-08-17 06:03:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 9d705f3a-515d-330d-b02f-b582a7b8bf68 | -14.4965 | -59.33358 | 2026-08-17 06:03:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d4c644df-b926-386d-adf2-f99740fca099 | -14.50258 | -59.32461 | 2026-08-17 06:03:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 2ed9a2c7-40b6-32c5-9177-cf9e5f5d946e | -14.09829 | -58.43794 | 2026-08-17 06:03:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 58b32841-ab4d-3073-91a2-de0c8eaf6626 | -14.21029 | -60.20108 | 2026-08-17 06:03:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| be7e1508-f077-3757-b7cd-b366b6590c33 | -14.09072 | -58.44344 | 2026-08-17 06:03:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 72d4eed6-340a-3aa8-820c-9724ca04715a | -14.20978 | -60.20599 | 2026-08-17 06:03:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| d9f92873-aee8-3da4-b2d7-dc30f26a6b91 | -14.49544 | -59.32952 | 2026-08-17 06:03:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7d6fa88b-4298-3c30-a7b2-d7ee0ff87899 | -11.92792 | -64.10175 | 2026-08-17 06:03:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 522bf3d4-f822-3998-a996-387918196b4a | -14.49773 | -59.32175 | 2026-08-17 06:03:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7d38e6b7-9d09-3e92-b49b-46127c49accb | -14.212 | -60.20123 | 2026-08-17 06:03:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 1a17bdac-1bce-3bd8-9dfa-5d8c33539d48 | -14.502 | -59.33057 | 2026-08-17 06:03:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 91aacbf3-8a08-39f1-a74a-1e8948460ab0 | -14.5043 | -59.3227 | 2026-08-17 06:03:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 8ffe9d0d-e41e-3241-9381-53772f5391a5 | -11.93024 | -64.09992 | 2026-08-17 06:03:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 734c1724-5624-3020-9da9-f2e7ed62cb21 | -14.49711 | -59.32771 | 2026-08-17 06:03:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 348ae5f2-8c82-3383-a146-1beac7931be9 | -14.50368 | -59.32872 | 2026-08-17 06:03:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| c082c686-6247-36e5-bb90-1f73127308c4 | -6.6384 | -58.9636 | 2026-08-17 06:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 577ef185-6354-3811-8afa-2758b19692b6 | -6.6568 | -58.9628 | 2026-08-17 06:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.6 |
| afb30734-6ce3-3943-ade1-edb3566e5a07 | -15.9185 | -55.5518 | 2026-08-17 06:10:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 104768b7-48b3-3af5-be36-66f88e77b93b | -15.9189 | -55.531 | 2026-08-17 06:10:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 107.1 |
| 3587c378-de50-3838-970f-e238cb78d9e0 | -15.8994 | -55.5334 | 2026-08-17 06:10:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 115.9 |
| 53d64e38-642b-3015-ae96-b11a40e34088 | -11.4963 | -46.58475 | 2026-08-17 06:10:00 | AQUA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 0227a1c3-acb3-38e1-90d4-3b560f367da7 | -11.12581 | -46.51576 | 2026-08-17 06:10:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 161.5 |
| 8f9cdf32-7d48-3ce7-8113-be8ecc03cfff | -11.12921 | -46.496 | 2026-08-17 06:10:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 36a4aeb1-117f-32fc-acd6-3963f202d286 | -11.80689 | -44.81013 | 2026-08-17 06:10:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 7327b212-3eec-3ae0-9cd3-d7e4c81a4197 | -8.06264 | -48.51911 | 2026-08-17 06:10:00 | AQUA_M-M | COLINAS DO TOCANTINS | TOCANTINS | Brasil | 1705508 | 17 | 33 | nan | nan | nan | Cerrado | 34.3 |
| 2c6090a0-8fde-3214-b1d7-fb5b407ef29e | -7.40395 | -46.82309 | 2026-08-17 06:10:00 | AQUA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 94ed2ee2-2588-30af-b028-3364518cdffd | -12.252 | -43.14799 | 2026-08-17 06:10:00 | AQUA_M-M | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 699f207f-cedf-3d46-8d71-c60681c430a4 | -6.53345 | -43.11724 | 2026-08-17 06:10:00 | AQUA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 4868e864-41c3-3333-af53-d640159f225f | -8.05578 | -48.52529 | 2026-08-17 06:10:00 | AQUA_M-M | COLINAS DO TOCANTINS | TOCANTINS | Brasil | 1705508 | 17 | 33 | nan | nan | nan | Cerrado | 38.0 |
| ff1df117-e91d-3f74-8346-57c689e03a5c | -13.4354 | -43.84333 | 2026-08-17 06:12:00 | AQUA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 24.0 |
| 496c2213-11f0-38a4-8390-8578f5610eed | -14.86863 | -46.65063 | 2026-08-17 06:12:00 | AQUA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 10ae61f0-58e4-30b1-9038-075c319971ea | -13.43726 | -43.83189 | 2026-08-17 06:12:00 | AQUA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 5a4d6243-d833-3b41-b068-545926ca772d | -13.51793 | -46.23478 | 2026-08-17 06:12:00 | AQUA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 3370e9e3-d3e0-3c9e-8f29-f726e6f048a7 | -14.88351 | -46.63515 | 2026-08-17 06:12:00 | AQUA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 6477f7f2-d182-379a-9c61-aa31ab98365e | -14.47247 | -45.67678 | 2026-08-17 06:12:00 | AQUA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 2fe92196-31b1-3f53-8695-e7392f6f28e9 | -12.66846 | -48.50268 | 2026-08-17 06:12:00 | AQUA_M-M | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 27.3 |
| 8563712e-ea9f-3410-b597-8d7a5047f641 | -20.7333 | -47.81183 | 2026-08-17 06:14:00 | AQUA_M-M | NUPORANGA | SÃO PAULO | Brasil | 3533601 | 35 | 33 | nan | nan | nan | Cerrado | 26.9 |
| badfa7ee-67f1-3f88-bbf0-4de687a3a2fa | -20.73032 | -47.82827 | 2026-08-17 06:14:00 | AQUA_M-M | ORLÂNDIA | SÃO PAULO | Brasil | 3534302 | 35 | 33 | nan | nan | nan | Cerrado | 15.4 |
| c2872fa3-f2ea-3f7d-8969-4c8d4cc504ac | -11.1299 | -46.5019 | 2026-08-17 06:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 59.7 |
| d4d2c5bb-1d6f-33ed-a406-b3da024ac620 | -6.6384 | -58.9636 | 2026-08-17 06:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.9 |
| d5851c8e-3bd8-3174-9436-500c5e46e385 | -15.9189 | -55.531 | 2026-08-17 06:20:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 128.1 |
| 53661304-b784-3000-8c74-ac1688cd404f | -11.1296 | -46.5244 | 2026-08-17 06:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 55.4 |
| c25dab95-7e63-3ad2-813a-62f532403c40 | -15.9185 | -55.5518 | 2026-08-17 06:20:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 4e74f4cc-e84d-311c-a54e-d6a009cb8a79 | -15.8991 | -55.5541 | 2026-08-17 06:20:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 2f2957a2-dc48-3809-b3bc-95e1c90bb707 | -15.8994 | -55.5334 | 2026-08-17 06:20:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 125.4 |
| 0f9add6a-cb4c-3972-8983-34500fbdcc13 | -15.9189 | -55.531 | 2026-08-17 06:30:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 143.2 |
| 3a2f8bab-d84c-3ab3-a634-249be0ce52f8 | -11.1299 | -46.5019 | 2026-08-17 06:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 125b018c-cdca-391f-9378-6e5664f51a68 | -15.9185 | -55.5518 | 2026-08-17 06:30:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 114.0 |
| 33b21690-77c8-3fb4-88f8-9ecc89b7a6ef | -15.8994 | -55.5334 | 2026-08-17 06:30:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 104.7 |
| 7ee37fff-e223-3891-ba7b-c5aa23ffe1dc | -8.72351 | -62.90535 | 2026-08-17 06:37:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ee3988ed-3f9c-3822-b478-6112985dc53f | -7.8777 | -63.74685 | 2026-08-17 06:37:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d83ef1a5-fa13-3cd5-bec9-b009e25afb8a | -7.87689 | -63.75319 | 2026-08-17 06:37:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9565a507-3d0a-34a7-89b5-cef54239266d | -8.71886 | -71.01012 | 2026-08-17 06:37:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e8f1db52-2ab7-33fa-a265-f05bad921ad0 | -8.73081 | -62.90631 | 2026-08-17 06:37:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |


[Clique aqui para ver as próximas entradas](README65.md)

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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4e7685fb-ac18-3dbb-8050-0fe2d281803e | -2.3999 | -46.1699 | 2024-11-06 01:20:00 | GOES-16 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 42.2 |
| bd78451a-a71d-3b91-8269-9a7b88ef4ad4 | -3.0023 | -53.4434 | 2024-11-06 01:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 49.8 |
| b341fec3-dffc-30c2-8743-dfffabf9590b | -2.9555 | -51.046 | 2024-11-06 01:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 35.9 |
| 78973fa7-06c5-399c-a4dd-825cceb825df | -6.1226 | -43.9809 | 2024-11-06 01:20:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 173.3 |
| 0cc823df-fe17-3795-b0db-e5edb359f54c | -2.8065 | -51.4855 | 2024-11-06 01:20:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 42.2 |
| eed318d2-1a50-384e-b557-616799ba6976 | -2.0634 | -47.0606 | 2024-11-06 01:20:00 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 9d0eb124-e58d-37b5-9d20-e440bbbec8c6 | -6.5012 | -47.5033 | 2024-11-06 01:20:00 | GOES-16 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 146.9 |
| c60eb1bc-9820-3548-9e16-4ac09924df63 | -4.1247 | -43.5601 | 2024-11-06 01:20:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 59.3 |
| c3091eb1-9079-3a39-b21e-2870110a52ae | -2.6764 | -51.8395 | 2024-11-06 01:20:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 33.3 |
| ea549e35-4c06-3a08-9bbd-56f6b30438d3 | -3.6603 | -50.2291 | 2024-11-06 01:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 39.8 |
| c7de2744-ba54-33e9-bdf6-4085055f427a | -6.4909 | -44.6633 | 2024-11-06 01:20:00 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 093e0c2d-5cb7-3a38-bd02-668e5d3291ae | -3.0213 | -53.2607 | 2024-11-06 01:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 86.1 |
| 838e8976-c0c3-3866-9c55-adb0b1138e81 | 3.6 | -51.3168 | 2024-11-06 01:20:00 | GOES-16 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 73.7 |
| a8a78518-1302-33cc-8d19-65b50201c10c | -3.2348 | -50.3904 | 2024-11-06 01:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 34.0 |
| 657aca05-7fd1-3192-a231-06859c17dea0 | -3.0607 | -52.5066 | 2024-11-06 01:20:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 41.7 |
| eafce983-75f6-3d02-a1fd-7adddbd44b99 | -5.5632 | -43.6998 | 2024-11-06 01:20:00 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 053ee116-46c4-38eb-a072-b52ec5c835de | -6.4827 | -47.4827 | 2024-11-06 01:20:00 | GOES-16 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 132.8 |
| 4cba602e-4349-3fe5-a108-ef5530405a85 | -10.5916 | -36.9712 | 2024-11-06 01:20:00 | GOES-16 | JAPARATUBA | SERGIPE | Brasil | 2803302 | 28 | 33 | nan | nan | nan | Mata Atlântica | 71.1 |
| 9bcfa035-3cdf-3952-ad4c-f61a162f3a5d | -6.1041 | -43.9593 | 2024-11-06 01:20:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 109.9 |
| 01f3a169-bf02-3279-bfb3-02e54510a976 | -3.0212 | -53.281 | 2024-11-06 01:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 7a7e3bf4-538a-3080-9dca-468d73f09af3 | -2.9371 | -51.0465 | 2024-11-06 01:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 111.9 |
| 587693a7-2f81-37f9-9ef4-0f349a64518b | -3.6788 | -50.2284 | 2024-11-06 01:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 20f8a8bb-66d5-31b4-b974-1ce4b5355363 | -3.2054 | -53.2153 | 2024-11-06 01:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 47.6 |
| a25637a5-649d-3efc-92f1-91bf2372938f | -3.0396 | -53.2805 | 2024-11-06 01:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 86.3 |
| aaf3efc4-767d-3009-8fc8-fd0aaf3f5daa | -6.4825 | -47.5046 | 2024-11-06 01:20:00 | GOES-16 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 0efd85a8-3141-30d2-9064-96f43edbb82b | -2.1746 | -53.7036 | 2024-11-06 01:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 3e28cee5-7c2d-3ee0-bd4f-4f189a605856 | -3.1394 | -51.1861 | 2024-11-06 01:20:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 31.9 |
| ad0ae2d5-3aab-399a-8e98-48f1b1048294 | -3.1759 | -51.2681 | 2024-11-06 01:20:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 36.6 |
| cc0a5049-bc63-3da2-98c8-784493d8b5df | -2.1562 | -53.7039 | 2024-11-06 01:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 29.7 |
| 5f33bada-a8d9-3170-821f-8ef4d1e8ec5c | -3.2349 | -50.3695 | 2024-11-06 01:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 33.4 |
| 9eb6e70f-820b-39b4-890e-64b403e9b4f2 | -3.5262 | -51.3193 | 2024-11-06 01:20:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| e71ff596-2f69-39ae-859b-93132960a916 | -3.0397 | -53.2603 | 2024-11-06 01:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 107.9 |
| 66935c07-a3bc-3673-a071-5717c9204c23 | 3.6184 | -51.3162 | 2024-11-06 01:20:00 | GOES-16 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 37e064c9-0652-382e-8abe-3924cf8ab798 | -2.7244 | -54.1351 | 2024-11-06 01:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 88.0 |
| 30f2044e-2782-3f9c-bebd-d78dfec62ce2 | -2.1746 | -53.6834 | 2024-11-06 01:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 44.1 |
| 31fd8b7f-a647-3e28-a56c-a9fa7d8d9456 | -3.967 | -48.15 | 2024-11-06 01:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| f8d2b4cf-ec9d-3066-9697-ebad2f37349e | -3.0207 | -53.443 | 2024-11-06 01:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| a325343a-7470-324e-93a3-601f46e0dd55 | -2.0635 | -47.0387 | 2024-11-06 01:20:00 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 33.8 |
| 5ea8a86f-024a-351a-9517-ebce3fc66819 | -2.7243 | -54.1552 | 2024-11-06 01:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 135.6 |
| e7b3beb1-cb3f-3c2e-981a-d0e1d68f4192 | 3.6 | -51.3168 | 2024-11-06 01:30:00 | GOES-16 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 1d8bb15d-efa8-3391-ad9c-8b5a53d566f0 | -3.2163 | -50.391 | 2024-11-06 01:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 3ce916b1-d3b4-3b01-a0ce-0dffccad840e | -3.0207 | -53.4227 | 2024-11-06 01:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 89.3 |
| 7aba1f6d-baa7-36f0-853c-430a232b92ea | -2.3999 | -46.1699 | 2024-11-06 01:30:00 | GOES-16 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 35.5 |
| 831d7c70-016b-3f0d-bb44-ad600033d5c8 | -3.1433 | -50.2044 | 2024-11-06 01:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 33.5 |
| 13831d28-7d5d-306a-a121-ae4507c3a8df | -3.2348 | -50.3904 | 2024-11-06 01:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 35.4 |
| df350c49-dcc5-3f42-bf45-f41c0a9a8824 | -3.0023 | -53.4434 | 2024-11-06 01:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 36.9 |
| eb41bc70-1853-389e-92fa-2b1a4952c7d4 | -6.1226 | -43.9809 | 2024-11-06 01:30:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 127.4 |
| 0428afa6-abb2-318e-acb5-a8dbc1837106 | -4.5614 | -48.0141 | 2024-11-06 01:30:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 76.0 |
| f3d3297c-f6aa-3a30-837b-8c9dc2e9d49b | -6.4825 | -47.5046 | 2024-11-06 01:30:00 | GOES-16 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 74.8 |
| da25c64d-681d-3a0e-b150-1e70aed7953e | -2.706 | -54.1556 | 2024-11-06 01:30:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 91798f7e-90d7-3eb5-b6f7-ece3d299c9f0 | -2.6764 | -51.8395 | 2024-11-06 01:30:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 39.0 |
| a5dffd76-ccd4-3355-8a78-22318d818780 | -3.2054 | -53.2153 | 2024-11-06 01:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 9af6ee51-d0af-3402-9380-ad1da2ceb4db | -6.4909 | -44.6633 | 2024-11-06 01:30:00 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 494855fc-bd65-35b3-9bc6-b5a67d6fc25c | -3.1393 | -51.2069 | 2024-11-06 01:30:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 38.1 |
| 4393e559-0dc2-3519-8e92-86a71224df9b | -3.0607 | -52.5066 | 2024-11-06 01:30:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 40.5 |
| 9896dc91-e1f9-3df9-9ac7-70cf8e21d7d0 | -6.5014 | -47.4813 | 2024-11-06 01:30:00 | GOES-16 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 233.8 |
| 0d84fabf-ce59-360e-b175-3e6bf835ec01 | -3.0213 | -53.2607 | 2024-11-06 01:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 68.5 |
| a1ea2678-b6bc-3761-abce-10dc362d2374 | -3.1616 | -50.2248 | 2024-11-06 01:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 34.7 |
| e5b0e640-ae9b-3b99-962c-7de125db206b | -3.1213 | -51.1036 | 2024-11-06 01:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 52910ebd-905c-375e-b420-668339f3557c | -3.2053 | -53.2356 | 2024-11-06 01:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 4c71ed5c-122c-37e0-80e5-9d498a0567e9 | -3.967 | -48.15 | 2024-11-06 01:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| cc8db3a2-a10e-33c0-93f9-2cfc7d862dff | -3.0397 | -53.2603 | 2024-11-06 01:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 111.7 |
| 4ebe29e8-a0fd-3ef8-96ab-def1aa074cc8 | -2.1563 | -53.6838 | 2024-11-06 01:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 36.6 |
| 971fed53-8c80-37b5-b5a8-ab20b08537af | -3.2349 | -50.3695 | 2024-11-06 01:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 36.7 |
| 2150c8b8-789d-32c8-9e53-03afad778561 | -2.1746 | -53.7036 | 2024-11-06 01:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 94d0bd35-5163-31d7-855d-31085f8bd854 | -2.8661 | -45.6201 | 2024-11-06 01:30:00 | GOES-16 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 40.8 |
| 16dc16f1-3a9b-3658-8e14-5a0c72493635 | -2.8506 | -49.4744 | 2024-11-06 01:30:00 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 38.3 |
| 7dd2f802-2432-39e9-bbfd-e1eb862c2cea | -3.2415 | -53.3967 | 2024-11-06 01:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 44.3 |
| b63ac73e-9bda-3202-976c-5de9a7d5596c | -6.1414 | -43.9794 | 2024-11-06 01:30:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 105.7 |
| 52d905d9-0835-3746-bbbb-a6af2ded26ad | -3.1617 | -50.2038 | 2024-11-06 01:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 87.9 |
| 655c7965-a54c-3475-944e-f95e08aa392f | -6.4906 | -44.6862 | 2024-11-06 01:30:00 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 101.9 |
| 1b6cb3c5-4ce7-3550-afb5-0bca2b08feaa | -2.082 | -47.0602 | 2024-11-06 01:30:00 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| b04b8d76-2846-38bd-83c0-429c77ec1455 | -2.8065 | -51.4855 | 2024-11-06 01:30:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 52.1 |
| f109e7f2-9e18-3b1c-9608-85655bf477fb | -3.0212 | -53.281 | 2024-11-06 01:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| a7b9957b-dceb-3283-95aa-e18d9c6f18cb | -3.0396 | -53.2805 | 2024-11-06 01:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 96.1 |
| 6aa4d470-2bfb-3e51-82e8-c7810ec91ad4 | -2.7243 | -54.1552 | 2024-11-06 01:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 113.8 |
| 7d5aa597-5b7b-3951-9c28-f7bffc80a799 | -6.5094 | -44.6847 | 2024-11-06 01:30:00 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 120.1 |
| 4f33824c-b2a7-3f4d-be0a-8addae32f6ac | -3.5262 | -51.3193 | 2024-11-06 01:30:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 90cdb288-285b-31bf-bf6d-50c10ec90d20 | -3.1802 | -50.2032 | 2024-11-06 01:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 36.8 |
| 04107d66-5b2a-3c49-834a-e9394e0f7f69 | -3.6788 | -50.2284 | 2024-11-06 01:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 48f6ff21-461a-335b-8dd9-64f9316651ad | -2.7428 | -54.1347 | 2024-11-06 01:30:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 36.4 |
| f6a150fa-da83-3b33-94a6-3c91fbddb56c | -2.7427 | -54.1548 | 2024-11-06 01:30:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 01ecb4f3-6a32-3628-8dde-b4c5e6ddf090 | -3.0207 | -53.443 | 2024-11-06 01:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 1b766c60-a4e6-3835-b7d9-9f896d512ed3 | -2.082 | -47.0383 | 2024-11-06 01:30:00 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 37.3 |
| 68245046-dbde-347a-8762-e95a60977f2f | -6.1229 | -43.9578 | 2024-11-06 01:30:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 5c6c4d0b-54a6-3567-bd99-2f20647468a2 | -6.1416 | -43.9563 | 2024-11-06 01:30:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 0390f2ec-75ee-33e5-a6ac-2051cd6f493e | -6.1041 | -43.9593 | 2024-11-06 01:30:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 117.6 |
| 22122d02-56de-39e4-b773-371f8ab24ab1 | -4.1434 | -43.5591 | 2024-11-06 01:30:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 65.6 |
| a75c9d1f-dadb-358d-a891-bd70b9a83214 | -2.0634 | -47.0606 | 2024-11-06 01:30:00 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 36.6 |
| 6ba19897-522d-3985-80b8-8f2551f06497 | -6.5096 | -44.6618 | 2024-11-06 01:30:00 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 70.7 |
| c4acb216-15fa-3f78-851b-7d2dbdc8ffce | -3.3285 | -50.0723 | 2024-11-06 01:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 2c57b2e2-3f80-38c8-9454-b879d29e98ba | -6.1039 | -43.9824 | 2024-11-06 01:30:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 42793539-2d56-39c6-b54c-dbeee83186d4 | -4.1246 | -43.5833 | 2024-11-06 01:30:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 121.4 |
| 091dfebd-af6e-384c-9368-3beb6ec8fb91 | -3.2164 | -50.3701 | 2024-11-06 01:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 37cd0deb-2436-3e3e-991e-7bac7f564f04 | -2.706 | -54.1355 | 2024-11-06 01:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 39.5 |
| 3ec19626-c48a-335b-b48c-41ad6a9d7c6b | -3.6603 | -50.2291 | 2024-11-06 01:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| db361451-2187-3fe2-a9ee-bf51deb385ad | -2.6764 | -51.8189 | 2024-11-06 01:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 71.2 |
| b4769967-2e3c-355b-b714-0f9d67879bc2 | -4.1432 | -43.5822 | 2024-11-06 01:30:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 132.4 |
| 51ffbe4c-51e4-39e4-b94b-79803e06c5e8 | -3.0023 | -53.4232 | 2024-11-06 01:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 42.1 |
| c3065cf1-12b9-399c-8201-cc96414a06cc | -6.5012 | -47.5033 | 2024-11-06 01:30:00 | GOES-16 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 159.0 |


[Clique aqui para ver as próximas entradas](README15.md)

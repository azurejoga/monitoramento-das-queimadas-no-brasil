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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 86a04ad5-62a9-3d84-9cc8-61e172883831 | -2.0055 | -54.45864 | 2025-11-13 05:01:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 60f41f19-bd95-398f-bd09-92da03912dd9 | -2.8681 | -51.47099 | 2025-11-13 05:01:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| c8bfeb81-901b-3456-af17-f6bc1619222f | -2.00604 | -54.45521 | 2025-11-13 05:01:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cc41067f-9b90-370d-8b41-0712a8a61bd4 | -3.03806 | -50.2892 | 2025-11-13 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1c6dd588-2941-3c74-94ea-46e0b1991357 | -2.72598 | -47.40469 | 2025-11-13 05:01:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 37b3ac13-928a-3215-b0c4-7142d7807aad | -3.15932 | -50.62118 | 2025-11-13 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ce46459b-0440-32cf-9a3a-71af2e2baf4f | -1.74814 | -54.38659 | 2025-11-13 05:01:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7f76e4ae-e523-382f-8a38-d73e5d660a9e | -2.44995 | -49.25893 | 2025-11-13 05:01:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 798265d8-2a34-3fe7-bd26-17b2941e85dd | -2.61756 | -49.21189 | 2025-11-13 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e7866b8c-0bd5-37d7-b380-181102f8b906 | -3.36445 | -48.40892 | 2025-11-13 05:01:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7492bead-4282-33e8-a434-e5a23709d379 | -3.36828 | -48.41417 | 2025-11-13 05:01:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e6aee003-8a7f-30f5-b762-73c8aae89797 | -3.43611 | -45.58478 | 2025-11-13 05:01:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c5f6f6a8-bdcf-3d07-bbc0-5d5cc40071e6 | -2.46457 | -54.78047 | 2025-11-13 05:01:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5f8fee37-9a38-32a1-a188-1b2c74067da9 | -1.10508 | -54.17663 | 2025-11-13 05:01:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b117764f-5eb9-3573-8717-15a972217a45 | 0.66017 | -51.54646 | 2025-11-13 05:01:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 38dafa8a-4d3d-3e91-bcc9-b5cc881ed19e | -3.34005 | -48.38655 | 2025-11-13 05:01:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7d9e2d4c-e622-36ff-a3c4-f61a81d235a2 | -3.34977 | -48.3833 | 2025-11-13 05:01:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2c207d90-82b1-3691-9113-5c69cb99a2fa | -2.89259 | -51.45498 | 2025-11-13 05:01:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 942c99e5-6880-3a44-8250-c6c01c2a621e | -0.71955 | -48.64282 | 2025-11-13 05:01:00 | NOAA-20 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 025b6ce4-5973-342e-8bc0-a5eb36e1d5f2 | -3.03412 | -50.28848 | 2025-11-13 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 6ac56028-41b9-3f9f-9f36-dfbcc624822e | -1.76763 | -55.29717 | 2025-11-13 05:01:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1acfc36c-2f3e-35e3-a796-25f624c0b39e | -1.81282 | -53.80467 | 2025-11-13 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d2e0c794-4615-3f76-9c6e-396f33932460 | -3.37909 | -50.13457 | 2025-11-13 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cfea1214-0fd3-3cb2-8491-6b115df96c52 | -2.63747 | -49.22287 | 2025-11-13 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 80d6bd38-9abe-35f7-8e80-93eece05ef30 | -2.87109 | -51.47588 | 2025-11-13 05:01:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| aeb7f89c-e747-34c5-a54f-80d98127aab0 | -4.25206 | -43.79266 | 2025-11-13 05:01:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6cd94759-446a-3a6e-8ed1-4990a321e576 | -2.06311 | -56.61929 | 2025-11-13 05:01:00 | NOAA-20 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fc12c228-72c0-3975-8b1c-6cbb72d0221b | -2.73006 | -45.48124 | 2025-11-13 05:01:00 | NOAA-20 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 43529fa6-7f85-3d90-a774-9120ad745d9a | -3.22588 | -45.59188 | 2025-11-13 05:01:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 386a01d7-5c84-35f5-bac3-dc1d44fe8d28 | -2.86442 | -51.47044 | 2025-11-13 05:01:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e8c7df9c-3a3d-354b-ab9c-0bd805b180f8 | -2.45414 | -49.25956 | 2025-11-13 05:01:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d8ae3987-9951-3910-84c2-3a176695cb4b | -1.85555 | -55.30069 | 2025-11-13 05:01:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8ed5b8eb-fdcd-3433-a67c-f907e8aa8a77 | -3.21241 | -50.19416 | 2025-11-13 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 2eaea2df-28ac-3031-8f95-d84753ff4f8b | -2.92438 | -51.75616 | 2025-11-13 05:01:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2cdf2a2e-e670-3645-9dff-3d79bd389a70 | -2.87297 | -52.79391 | 2025-11-13 05:01:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 190afb5c-9fbc-35e5-bc14-ae6756a15f91 | -0.72381 | -48.64348 | 2025-11-13 05:01:00 | NOAA-20 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b082403b-6232-31f1-bb96-45ea7e7cddd0 | -3.21292 | -50.19076 | 2025-11-13 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 64b9e81a-bbc0-35de-b1dc-0a64afbc0a55 | -3.09254 | -49.27121 | 2025-11-13 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b369b058-7142-3f93-90c2-8d608c031669 | -2.72544 | -47.40628 | 2025-11-13 05:01:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1522684e-1741-32ff-98bc-2bb755160a1b | -3.34386 | -48.38058 | 2025-11-13 05:01:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3f5a808c-96fb-3e2a-8caf-3d2dbfc4d586 | -2.45372 | -49.26657 | 2025-11-13 05:01:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 69d14be7-c551-39c6-9d4b-2bf436a5321e | -3.33792 | -48.38904 | 2025-11-13 05:01:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 67b2fa42-7636-337d-ad63-3944b6377d34 | -2.94341 | -52.51504 | 2025-11-13 05:01:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 95d15b71-4e99-3f0a-a631-854ad32390c5 | -3.2397 | -50.04152 | 2025-11-13 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f3beed46-7134-371c-8bd9-690f2ea3337a | -2.44874 | -49.26661 | 2025-11-13 05:01:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e6331a6b-4268-3897-8fe0-960af2ba24ff | -3.36897 | -48.40954 | 2025-11-13 05:01:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0dafbe99-ee3f-3629-9734-41db5bf53e36 | -3.44175 | -45.58222 | 2025-11-13 05:01:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 21ee7ae3-892b-3bed-aa3d-80149c75c25e | -3.38877 | -50.27076 | 2025-11-13 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f433eb45-2a8f-357b-9033-bdfb361c10a4 | -1.93338 | -52.09547 | 2025-11-13 05:01:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| aa65a5b3-bbe8-31a3-aeb7-d16e416426a8 | -2.00327 | -54.45126 | 2025-11-13 05:01:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 719f019c-34b7-3d0a-970f-ecb3e567bdfe | 1.45684 | -55.85822 | 2025-11-13 05:01:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d427c40f-ac79-30e7-a6e7-d02bc6ad52bb | -2.86673 | -51.47965 | 2025-11-13 05:01:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1821fd80-fca4-3ad5-9c39-a2483d0fe7e1 | -3.03333 | -50.29358 | 2025-11-13 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 931684b4-3300-3f72-a89b-8e1c7d6a922b | -2.72953 | -45.48477 | 2025-11-13 05:01:00 | NOAA-20 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 298b061e-5aa2-31be-8ff2-1f9c169af5c0 | -2.00382 | -54.44781 | 2025-11-13 05:01:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0481b6fa-1d89-3263-a4e6-a54edf8899e5 | -1.64872 | -53.29119 | 2025-11-13 05:01:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8bd2e801-1f66-372b-9545-461fa0ed2c52 | -2.06253 | -56.62293 | 2025-11-13 05:01:00 | NOAA-20 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 40ce1a61-ae16-36ce-aeb6-b2ed47fa8084 | -2.45009 | -49.2621 | 2025-11-13 05:01:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 466fe5a3-1999-38c4-a2e6-645c82bfde9e | -1.77082 | -55.23413 | 2025-11-13 05:01:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f7cee7e3-31e7-391b-93dd-19e11370f897 | 1.46533 | -55.84564 | 2025-11-13 05:01:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1e7dde0b-54c3-3f74-bc72-7decb2a9510e | -1.81172 | -53.81165 | 2025-11-13 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8360f51e-174b-35e0-83c5-90f8aabf30ad | -2.55475 | -51.24959 | 2025-11-13 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 240882af-a4cd-3f83-9f83-3f43606080aa | -2.89972 | -48.06713 | 2025-11-13 05:01:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ee069574-95ff-3baa-9247-c0baec959fcf | -3.09678 | -49.27185 | 2025-11-13 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8519beb0-6293-357c-9fde-d83a3a681489 | -3.38826 | -50.27417 | 2025-11-13 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9ab20407-3e18-30dc-a8b2-bdbed23eeb6a | -3.08426 | -49.27095 | 2025-11-13 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 63091826-4249-3766-b1f4-13675e600909 | -2.88842 | -48.07975 | 2025-11-13 05:01:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cdbad8ad-b90a-3b9e-b01e-77d8568eec9f | -2.72518 | -47.40985 | 2025-11-13 05:01:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 750db926-a6e2-32f9-aeb2-68e596b84b54 | -3.20841 | -50.1936 | 2025-11-13 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2b9daf96-8b6b-3860-bb1d-bedc58e77c43 | -3.39924 | -50.17344 | 2025-11-13 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8518ac45-f873-3b02-8670-658cbecc93c4 | -3.44212 | -45.58201 | 2025-11-13 05:01:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 618c5276-bdcc-3754-8196-a64c96cdc15c | -3.22692 | -45.58994 | 2025-11-13 05:01:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 28c72a57-31ab-39d0-a11f-5203af15cefa | -2.44934 | -49.26278 | 2025-11-13 05:01:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f8bfa4e2-a228-3c8a-a872-35849097bce8 | -2.92801 | -51.75668 | 2025-11-13 05:01:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ef534924-dc2b-3ac2-8252-7421bffdc872 | -3.27864 | -50.21471 | 2025-11-13 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f121f30b-a493-3768-bb81-be4cc0c52d3d | -3.35008 | -49.83478 | 2025-11-13 05:01:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 03cdd2be-45e5-3463-8c20-7b1b83a00dc8 | -3.15014 | -50.26618 | 2025-11-13 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1c7a3d3a-f6fe-3522-927b-dd8756ce0747 | -3.46645 | -43.19301 | 2025-11-13 05:01:00 | NOAA-20 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3401b7f3-8bbd-3164-b8d7-c70bce98065b | -3.3728 | -48.41483 | 2025-11-13 05:01:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 962011e8-0962-31ed-bffd-0ab72bee8b31 | -2.0637 | -56.61564 | 2025-11-13 05:01:00 | NOAA-20 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2199c938-f9ed-39d4-970d-ff53aae3d3a9 | -2.86657 | -51.47753 | 2025-11-13 05:01:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 33ce10ca-9996-3dfa-84d9-c9ed330974f0 | -3.41688 | -49.99958 | 2025-11-13 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 90d1274b-69ba-3c15-818b-33b8560ba444 | -3.44121 | -45.58581 | 2025-11-13 05:01:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 027300d7-d420-3f30-876b-33009bbe7755 | -1.82891 | -53.81075 | 2025-11-13 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b201acd3-19cc-3319-a4bb-8314fb141a77 | -2.43302 | -48.62101 | 2025-11-13 05:01:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 39643e1a-bbd1-352b-8107-e40b436ce46c | -3.03776 | -51.03487 | 2025-11-13 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fb5c4165-4b32-3d3f-b709-1a17d1042885 | -1.37497 | -55.39501 | 2025-11-13 05:01:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ccd9a5da-5e08-3eae-986e-1d61291b2553 | -3.34909 | -48.38794 | 2025-11-13 05:01:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f52bb792-599d-3c89-8c0d-93201778e319 | -3.76395 | -47.72615 | 2025-11-13 05:01:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b8d4d5ff-9a01-36fc-94a3-251af526566c | -3.09696 | -49.27286 | 2025-11-13 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6bb73e0d-ef51-33f2-9e57-524eb19bd8cd | -3.46079 | -43.18685 | 2025-11-13 05:01:00 | NOAA-20 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 06bb5dbc-8208-357b-af09-b6866ca49b9e | 1.45741 | -55.86189 | 2025-11-13 05:01:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| af37d469-b273-365c-a2ed-c10ae091e8a5 | -2.14326 | -53.64735 | 2025-11-13 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| fac2c5f7-7c87-3479-b6e1-fc354e66e1ce | -3.09211 | -49.27616 | 2025-11-13 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 009df581-4b05-3c0d-a69c-8a25272a52c8 | -2.55105 | -51.24901 | 2025-11-13 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6719e0a3-7f8f-30aa-817e-9fd3c7a966d2 | -3.33621 | -48.38128 | 2025-11-13 05:01:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e068a3dd-a4c7-3ac3-87b9-e38b863e905b | -3.36514 | -48.40431 | 2025-11-13 05:01:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dc2ca42e-9d8d-321d-b79c-bd24ce1da2df | -2.87041 | -51.48021 | 2025-11-13 05:01:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 09512c3b-6302-34dd-8d6e-76fe2cdd1f82 | -3.76413 | -47.72798 | 2025-11-13 05:01:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 62f8c6ea-cbb0-3f08-aabe-8694d5e9c5c4 | -3.46511 | -43.19011 | 2025-11-13 05:01:00 | NOAA-20 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README34.md)

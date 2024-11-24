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

## Dados Diários - Página 87

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8fb7f1fb-f392-363a-89bd-041cb1823c1b | -3.02799 | -49.44275 | 2024-11-24 05:42:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d2dee665-baa7-3f87-b8a7-ca6fa8bf7ff6 | -3.20294 | -52.57107 | 2024-11-24 05:42:00 | AQUA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| ca5b426f-7b40-314f-98b5-9bead0bf1d9e | -2.9435 | -51.42213 | 2024-11-24 05:42:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| cff93a67-237f-3ba1-aa45-9a7a96a9cc5d | -3.30066 | -50.02854 | 2024-11-24 05:42:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| b5a0015b-0008-3247-8f8a-e683c7c7e0f6 | -3.84526 | -44.04579 | 2024-11-24 05:42:00 | AQUA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 9fdc57ee-d41a-3ff4-aeb7-563bf9705294 | -3.48431 | -49.9152 | 2024-11-24 05:42:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 80d916a3-e9fc-3e66-a76c-a30886135ebd | -3.13084 | -52.98009 | 2024-11-24 05:42:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 70e593ff-c6d9-3e29-a985-72db2f74c31d | -4.18996 | -50.68646 | 2024-11-24 05:42:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2930e66f-d2b3-3577-9568-239ab6cb63a5 | -3.34737 | -50.50988 | 2024-11-24 05:42:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 6c9f2d99-34ca-31e4-ad03-2c4124548f1c | -2.58405 | -54.21847 | 2024-11-24 05:42:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| a5d3a13a-056a-34a3-b6e4-c67b5dd6c745 | -3.49394 | -50.46256 | 2024-11-24 05:42:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| c8976f35-e782-388b-88a6-7383ea95d10d | -4.05358 | -48.31942 | 2024-11-24 05:42:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 90fa972d-e362-31fc-af67-d3034fa46b5c | -2.78473 | -51.6736 | 2024-11-24 05:42:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 7833e465-dee0-362a-9c03-2dc1506b76b1 | -3.24083 | -50.669 | 2024-11-24 05:42:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 23cc0298-d150-3dde-b84c-e85b05790ad3 | -15.21992 | -60.37957 | 2024-11-24 05:42:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 19ab6128-9945-3a3f-b026-f8fbbd0ac3e8 | -15.43583 | -60.21928 | 2024-11-24 05:42:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 61890b1b-ec37-3790-888e-175b80d1c044 | -21.31161 | -49.18531 | 2024-11-24 05:44:00 | AQUA_M-M | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| 9d2c7eba-8e92-37a5-93a8-20c2c7ae2b41 | -29.85962 | -51.1624 | 2024-11-24 05:48:00 | AQUA_M-M | ESTEIO | RIO GRANDE DO SUL | Brasil | 4307708 | 43 | 33 | nan | nan | nan | Pampa | 8.6 |
| 0772ff7b-6e8f-3bbe-8c0e-cafa405fd780 | -29.86134 | -51.14664 | 2024-11-24 05:48:00 | AQUA_M-M | ESTEIO | RIO GRANDE DO SUL | Brasil | 4307708 | 43 | 33 | nan | nan | nan | Pampa | 8.9 |
| 224ff02d-8f9b-3f54-abf9-a3a268a455e3 | -2.3211 | -53.862 | 2024-11-24 06:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 5faf47ec-fd2f-3ea6-a488-6e0678510b4e | -3.2207 | -45.2925 | 2024-11-24 06:40:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 9e177bba-75ff-3091-ba0c-808997492545 | -3.1645 | -45.3622 | 2024-11-24 06:40:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 034a5437-f07b-3167-98a4-c8a7e2dae24a | -3.146 | -45.3629 | 2024-11-24 06:40:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 127.1 |
| 20336829-8151-39a6-924b-fbc3e423dd73 | -3.2021 | -45.2932 | 2024-11-24 06:40:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 83c0accd-3e67-3346-a691-5dd4033726b6 | -3.5159 | -53.8132 | 2024-11-24 06:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| bd7bc3f3-5a98-3a9e-aa03-353e0c02e2b0 | -3.1461 | -45.3404 | 2024-11-24 06:50:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 96.7 |
| 9688d020-6674-3fec-b4cb-d09e171f88c9 | -3.1647 | -45.3397 | 2024-11-24 06:50:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 897b4b90-1d11-3e07-9fa6-02ff62e77e43 | -3.2207 | -45.2925 | 2024-11-24 06:50:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 17b692f0-2436-3afe-b2d2-c72948e11282 | -6.2553 | -35.1708 | 2024-11-24 06:50:00 | GOES-16 | GOIANINHA | RIO GRANDE DO NORTE | Brasil | 2404200 | 24 | 33 | nan | nan | nan | Mata Atlântica | 118.4 |
| f2ae7770-2e37-3cf9-a77f-fefab84d25f4 | -3.1645 | -45.3622 | 2024-11-24 06:50:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 119.1 |
| 133d7066-61b1-3cd8-b3c9-4f2feb7a7671 | -6.2744 | -35.1686 | 2024-11-24 06:50:00 | GOES-16 | GOIANINHA | RIO GRANDE DO NORTE | Brasil | 2404200 | 24 | 33 | nan | nan | nan | Mata Atlântica | 148.7 |
| 9de520ea-d749-3fb6-945d-f7eae5f7d6a9 | -3.2021 | -45.2932 | 2024-11-24 06:50:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 65.9 |
| f638da68-6d1c-3bfb-b64c-257b7167c1bd | -3.146 | -45.3629 | 2024-11-24 06:50:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 224.1 |
| 46588b9e-ed49-3f06-a9ca-09a0c6d6e84c | -3.5159 | -53.8132 | 2024-11-24 07:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 076a06d7-8e16-371a-b78c-be7172a4d53a | -3.1461 | -45.3404 | 2024-11-24 07:00:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 64.6 |
| b60c3e13-51cd-3015-9483-84859e5e07c6 | -3.1645 | -45.3622 | 2024-11-24 07:00:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 8550df10-3ad8-33af-b87e-7beb0aa9ea98 | -3.146 | -45.3629 | 2024-11-24 07:00:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 129.2 |
| 9cd0906d-8c15-36bc-a9df-88dea19c18ef | -3.146 | -45.3629 | 2024-11-24 07:10:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 103.6 |
| 019b8c53-016a-31f6-b14a-8c052362010c | -3.1645 | -45.3622 | 2024-11-24 07:10:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 62.5 |
| ec8def0d-7b15-3ebd-a2e4-28bdecea5728 | -3.4975 | -53.8137 | 2024-11-24 07:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 734fe1f0-19a7-31e4-ad4e-74ddbf31becf | -3.5159 | -53.8132 | 2024-11-24 07:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 85.0 |
| a9b3df09-349e-350c-bc28-898cfd4ba795 | -3.4975 | -53.8137 | 2024-11-24 07:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 91619314-5f1a-36a4-9aa8-432e920b9e13 | -3.5159 | -53.8132 | 2024-11-24 07:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 79.2 |
| b4e02618-df61-3619-b2fb-bd404e782549 | -3.1645 | -45.3622 | 2024-11-24 07:20:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 7f7581bf-9ddb-3232-b0ed-70bf251450ab | -3.146 | -45.3629 | 2024-11-24 07:20:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 65085552-8ccf-3212-836d-41cb0a4c153f | -3.5159 | -53.8132 | 2024-11-24 07:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 41ff9a32-02d4-3095-b1ca-31dfc9b32179 | -3.4975 | -53.8137 | 2024-11-24 07:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 1a3302cc-8b24-3a05-b2dc-178f406e5957 | -3.1645 | -45.3622 | 2024-11-24 07:30:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 56.4 |
| b701ca82-c675-3ed7-abbb-52c40d01485d | -3.2208 | -45.27 | 2024-11-24 07:40:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 83.1 |
| cc85d77d-d553-35f3-8e8c-58a40a92801e | -3.2211 | -45.2024 | 2024-11-24 07:40:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 0456abb0-9aa5-31f8-b8b7-b8d5d0a02bc6 | -3.5159 | -53.8132 | 2024-11-24 07:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 3c8e36de-37aa-361e-8c61-d20e8cc0ff88 | -3.2208 | -45.27 | 2024-11-24 07:50:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 99011b43-0ef9-315a-a12f-867e9b2d2f31 | -3.5159 | -53.8132 | 2024-11-24 07:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 5ebd5c30-a677-3fee-b626-f428d1239b55 | -3.5159 | -53.8132 | 2024-11-24 08:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 5c2ff779-f2b3-3a2f-836e-a5bad41a111b | -2.6439 | -45.4481 | 2024-11-24 10:30:00 | GOES-16 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 84.2 |
| f5d8fca0-d294-353e-a902-3356ab5de937 | -2.3744 | -48.2478 | 2024-11-24 10:30:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 108.8 |
| 13b74684-5fde-32a9-9a53-72d0d7767508 | -2.3928 | -48.2473 | 2024-11-24 10:40:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 98.0 |
| 9d9d4787-240b-3574-a739-8885e20531b2 | -2.3744 | -48.2478 | 2024-11-24 10:40:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 138.7 |
| dfe4b712-17e4-39c6-b42e-c9c3f72a4eba | -2.3744 | -48.2478 | 2024-11-24 10:50:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 124.6 |
| fe5082fb-9aea-339b-8076-7f004c630a5d | -9.10866 | -37.58479 | 2024-11-24 11:34:00 | TERRA_M-M | CANAPI | ALAGOAS | Brasil | 2701605 | 27 | 33 | nan | nan | nan | Caatinga | 44.9 |
| 941d692d-4c7c-3d7c-b8c5-7ec715373546 | -9.11234 | -37.56196 | 2024-11-24 11:34:00 | TERRA_M-M | CANAPI | ALAGOAS | Brasil | 2701605 | 27 | 33 | nan | nan | nan | Caatinga | 57.8 |
| 68b35670-a63b-3d9b-9f9f-503822cf5453 | 0.4141 | -50.858 | 2024-11-24 11:40:00 | GOES-16 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 84.3 |
| 98eaee5f-bb66-34db-88f9-ae3ee35c97d2 | -3.4793 | -42.1874 | 2024-11-24 12:10:00 | GOES-16 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 83.2 |
| 22486987-7fbf-3780-a2e8-fb3788a4c1fe | -3.2021 | -41.605 | 2024-11-24 12:10:00 | GOES-16 | BOM PRINCÍPIO DO PIAUÍ | PIAUÍ | Brasil | 2201919 | 22 | 33 | nan | nan | nan | Caatinga | 79.1 |
| bfb20442-6a0d-3215-8498-c19de43345e9 | 0.4141 | -50.858 | 2024-11-24 12:10:00 | GOES-16 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 1c69add5-a12e-3ecf-a94c-8b79feca83bd | -1.4024 | -54.4774 | 2024-11-24 12:20:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 653436fe-0d0d-3e22-8922-5f3d60583ce4 | 0.4141 | -50.858 | 2024-11-24 12:20:00 | GOES-16 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 88.4 |
| 36c655cf-3c71-3a05-a9d2-aa139396f9b8 | -2.3211 | -53.862 | 2024-11-24 12:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 9a6624df-2382-3841-8138-463f7bebd47f | -2.3211 | -53.862 | 2024-11-24 12:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 97.4 |
| d1f6a77e-bbc2-3e5c-b45d-078ddb518d15 | -3.1226 | -42.5346 | 2024-11-24 12:50:00 | GOES-16 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 8941f017-ef07-37b8-8b22-594dbda43c69 | -4.4198 | -44.0974 | 2024-11-24 12:50:00 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 66c4390d-d629-3ffd-9da3-4b23e91b510b | -5.0998 | -43.151 | 2024-11-24 12:50:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 5bf6e76d-0e9a-3ea9-98e4-48bc295e61c2 | -2.3211 | -53.862 | 2024-11-24 12:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 063cfd2e-6e6e-343d-a666-2259af680ff4 | -1.479 | -52.5178 | 2024-11-24 12:50:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| c9e50a0b-eb9c-30af-939b-6d02031f57ce | -3.5947 | -44.9153 | 2024-11-24 12:50:00 | GOES-16 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 93edcaf6-74dd-3f67-baa5-47d9428fae04 | -2.3211 | -53.862 | 2024-11-24 13:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 80.6 |
| de313844-7ad4-3383-b899-f7c7d077ff6e | -1.6419 | -53.8731 | 2024-11-24 13:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 9b6e0843-e2a0-3987-991c-5c0c99957220 | -3.1226 | -42.5346 | 2024-11-24 13:00:00 | GOES-16 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 104.8 |
| 55aad947-3e48-37e0-8d75-103c90bd0516 | -1.479 | -52.5178 | 2024-11-24 13:00:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 216edfc6-7934-3cb2-8159-85f80bad74ef | -4.4198 | -44.0974 | 2024-11-24 13:00:00 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 236417a4-3b82-306e-9868-35754a6ea089 | -3.1414 | -42.5102 | 2024-11-24 13:10:00 | GOES-16 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 9473c14c-2933-3f96-8786-52aa189d0887 | -1.3874 | -52.3351 | 2024-11-24 13:10:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 578d4db5-d537-303e-967b-360f0102e5a7 | -1.479 | -52.5178 | 2024-11-24 13:10:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 76.8 |
| bfe5b483-0e89-316a-b936-f7211a2ee53a | -1.6419 | -53.8731 | 2024-11-24 13:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 7625da51-713d-34ac-af21-80af189eca41 | -3.8928 | -41.8568 | 2024-11-24 13:10:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 79.0 |
| 4d7418ac-d6b0-390f-8d16-fb4d28392481 | -2.3211 | -53.862 | 2024-11-24 13:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 96.3 |
| 0a8c29c6-ea48-383e-a1dc-f6571ab687fe | -1.3666 | -53.8362 | 2024-11-24 13:10:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| e07e7ab3-f49b-3e23-8631-d15b9e74e9b0 | -2.3211 | -53.862 | 2024-11-24 13:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 02797a2e-fd1d-37ca-b68b-d46b37539cbf | -2.3395 | -53.8617 | 2024-11-24 13:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| eb2ce22b-0b12-3bbd-b305-07f8a4c75f70 | -3.8928 | -41.8568 | 2024-11-24 13:20:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 102.1 |
| e908ff6e-a6c4-3369-bdf5-1d3b24e34f67 | -2.1744 | -53.7842 | 2024-11-24 13:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 77.0 |
| e981d1fd-3090-3032-8a60-e864ef7523bf | -1.6419 | -53.8731 | 2024-11-24 13:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 85.2 |
| f6b758c4-18bd-3fd0-97b7-07d29d562936 | -1.479 | -52.5178 | 2024-11-24 13:20:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 78.1 |
| c95da06b-f114-3a5d-8491-cb647457edc2 | -1.3666 | -53.8362 | 2024-11-24 13:30:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 6318067b-393e-3263-9c69-af94b2b6a59f | -2.1744 | -53.7842 | 2024-11-24 13:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 3af41515-89cc-3f89-a35d-ba455c900b0d | -1.6419 | -53.8731 | 2024-11-24 13:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 107.2 |
| 819436e8-b2f3-3213-a945-4c4b0b587268 | -3.8928 | -41.8568 | 2024-11-24 13:30:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 103.4 |
| b3638fe8-9de4-3646-b2b1-bd82892c3701 | -2.3395 | -53.8617 | 2024-11-24 13:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 1d53aa45-b388-3feb-89ba-9fed0f09498a | -0.2851 | -51.5009 | 2024-11-24 13:30:00 | GOES-16 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 031d0802-af30-3f20-bfc5-1505a8de8af4 | -2.3211 | -53.862 | 2024-11-24 13:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 161.4 |


[Clique aqui para ver as próximas entradas](README88.md)

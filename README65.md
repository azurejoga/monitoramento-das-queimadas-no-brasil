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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 81e2469a-3f99-3310-b128-8c80ceae05c6 | -1.2313 | -47.35179 | 2024-11-17 05:57:00 | AQUA_M-M | NOVA TIMBOTEUA | PARÁ | Brasil | 1505007 | 15 | 33 | nan | nan | nan | Amazônia | 31.7 |
| cd3f3ca7-ec5e-32dd-bbc4-d5b3ccc99f15 | -1.21481 | -51.78352 | 2024-11-17 05:57:00 | AQUA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 868f4077-36a3-30da-b964-a1018308695a | -1.36778 | -52.24786 | 2024-11-17 05:57:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0492096f-2456-3e16-972f-900c665d68d8 | -3.79382 | -51.37266 | 2024-11-17 05:57:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| b30bb1a9-6670-3955-8da3-627c0d53bff4 | -1.62876 | -53.28123 | 2024-11-17 05:57:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 838a74cc-8474-3320-9ee4-7c28a676a22b | -1.63835 | -52.66137 | 2024-11-17 05:57:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 1cfeb083-fc6a-3d2f-b983-be55a2b17577 | -4.55603 | -48.00562 | 2024-11-17 05:57:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 127.8 |
| 12b43c9e-2d46-3463-972c-e89f077a3c38 | -1.13642 | -51.68638 | 2024-11-17 05:57:00 | AQUA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 2795c6a5-3f03-30bf-882d-e6109823d80e | -4.54562 | -45.23478 | 2024-11-17 05:57:00 | AQUA_M-M | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 29.1 |
| 8c838930-cd66-32a5-8a62-6990fae81f09 | -2.56456 | -54.73354 | 2024-11-17 05:57:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| cd20830b-61af-31f4-bc4b-8de2de123571 | -1.29367 | -51.74162 | 2024-11-17 05:57:00 | AQUA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 5bbc4183-7eb7-3f3b-ba24-0bd0c806cfd7 | -3.57859 | -50.52459 | 2024-11-17 05:57:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| d60cfb73-f6c8-3999-bcea-4b1a6f027ae5 | -0.95527 | -51.72786 | 2024-11-17 05:57:00 | AQUA_M-M | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 258c723a-b86a-35c2-94a9-7d649f2fa40e | -2.85742 | -46.73009 | 2024-11-17 05:57:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 29.7 |
| 97bb9229-37a8-3e4f-81d0-1e7656a8353d | -1.33203 | -51.86686 | 2024-11-17 05:57:00 | AQUA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 5817a4a3-d853-3975-8936-e9c321c90d7c | -2.23685 | -53.60189 | 2024-11-17 05:57:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 763229d3-fd8f-3cbe-b0de-6ae75e11d14a | -2.32476 | -53.56714 | 2024-11-17 05:57:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d29dc0af-6822-3cef-8239-608975bc305e | 0.6098 | -51.7674 | 2024-11-17 05:57:00 | AQUA_M-M | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 33.4 |
| 22e846ff-23df-3965-8748-2d99a63f8286 | -3.53023 | -50.512 | 2024-11-17 05:57:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 9197362c-5e74-3f2a-b1e5-584dbd7dc009 | -1.64207 | -52.51183 | 2024-11-17 05:57:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2699d679-c5fe-3f88-a244-ccdbfd8aeffe | -2.14744 | -46.91542 | 2024-11-17 05:57:00 | AQUA_M-M | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 6a02d3d9-8224-3b47-9435-2deaeedeaa38 | -3.09533 | -51.3119 | 2024-11-17 05:57:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| e161b1e2-b178-3fa6-b981-fc34d8d079a4 | -1.33348 | -51.85719 | 2024-11-17 05:57:00 | AQUA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9693a059-1b2d-3bc8-ac41-5631abdaff17 | -1.14429 | -51.69757 | 2024-11-17 05:57:00 | AQUA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 25e1f201-3df4-3da5-8a37-3057ff915e7d | -3.75011 | -54.71574 | 2024-11-17 05:57:00 | AQUA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e70799d9-9968-35ce-8a53-b21a58904e0c | -1.66651 | -47.97113 | 2024-11-17 05:57:00 | AQUA_M-M | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 24.0 |
| c771cb7d-57c4-3c7f-9c58-3a081ed348a1 | -3.53106 | -50.24679 | 2024-11-17 05:57:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 23.5 |
| be9ad263-a933-3971-bcb5-8ef3646f7e17 | -1.32276 | -51.86554 | 2024-11-17 05:57:00 | AQUA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 0e13e1e9-51d9-334a-9f14-892dbeb4be70 | -2.60404 | -47.556 | 2024-11-17 05:57:00 | AQUA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 22.5 |
| 2b2600af-a957-32b7-818e-d14bc8b04e5a | -0.10809 | -51.58876 | 2024-11-17 05:57:00 | AQUA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 9ca28e43-7108-3ccb-af51-7fb0d0559d78 | -4.80843 | -44.47248 | 2024-11-17 05:57:00 | AQUA_M-M | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 44.3 |
| b438e3fd-8dfe-35ff-9704-2fb1ebc1badd | -1.20552 | -51.78219 | 2024-11-17 05:57:00 | AQUA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 54201b78-608e-3de9-aec5-0b175ae14710 | -1.61813 | -52.48378 | 2024-11-17 05:57:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9fc1138b-2e3e-3305-abc6-17324a79a43e | -3.71543 | -51.8394 | 2024-11-17 05:57:00 | AQUA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 3ba8651c-3f00-3abb-abe6-99ca676195c4 | -1.41034 | -51.07973 | 2024-11-17 05:57:00 | AQUA_M-M | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| b6911aae-20d6-31f4-a7f2-ee5d674b9ee4 | 0.61893 | -51.76605 | 2024-11-17 05:57:00 | AQUA_M-M | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 33.4 |
| e5acd674-91ac-3c3f-8b15-1eff053bf70a | -1.63699 | -52.6705 | 2024-11-17 05:57:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 21.2 |
| 1929594e-129b-35b1-b262-0e39bb3bbc35 | 0.61122 | -51.77682 | 2024-11-17 05:57:00 | AQUA_M-M | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 26.0 |
| a94e8078-e481-363d-9e48-9c142ecab483 | -0.95576 | -52.41009 | 2024-11-17 05:57:00 | AQUA_M-M | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 68fddba7-12be-371b-8e17-0785dc375e75 | -2.56589 | -54.72467 | 2024-11-17 05:57:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 41f58a43-f62b-36c3-8e42-765905c94aee | -2.23554 | -53.61071 | 2024-11-17 05:57:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| a1078e9a-c4f2-319b-95a3-983c32308a01 | -3.52445 | -50.25261 | 2024-11-17 05:57:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 17.6 |
| be5a014f-5893-3af8-a72e-49fb0a7e168d | -0.04606 | -53.25171 | 2024-11-17 05:57:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 42fa96e8-d76e-353a-8078-cf6c1ccbc89f | -1.19746 | -52.02734 | 2024-11-17 05:57:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| e2b93c28-a24d-34a0-bef4-42bc688e9e9b | 0.40244 | -50.86598 | 2024-11-17 05:57:00 | AQUA_M-M | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 10.6 |
| e0d6d39f-8c25-3b3e-a92b-28a4f72408b9 | -12.40116 | -57.52333 | 2024-11-17 05:59:00 | AQUA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 0c8b1dd0-2b11-3b2f-9a63-7b6776b607db | -14.54419 | -59.95218 | 2024-11-17 05:59:00 | AQUA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 79873998-8f70-33f3-a316-5c9eae904439 | -12.39358 | -57.51243 | 2024-11-17 05:59:00 | AQUA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 11450efd-62d3-33e3-8729-ed962d1212b9 | -4.5614 | -48.0141 | 2024-11-17 06:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 6d6648c8-2581-3272-ab01-02da9a083c73 | -4.5616 | -47.9925 | 2024-11-17 06:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| c38da0e9-1566-3066-8c2f-82d30b6f17d3 | 0.6159 | -51.7676 | 2024-11-17 06:00:00 | GOES-16 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 67a54138-8600-3fe4-8648-8a0a13b8f6fe | -2.6322 | -48.5634 | 2024-11-17 06:00:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| e3f6c104-5193-32f4-868c-455b69178b61 | -19.48507 | -56.61184 | 2024-11-17 06:01:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 4d819a65-6892-3b38-972a-7f2e2e2c5110 | -19.49409 | -56.61325 | 2024-11-17 06:01:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.3 |
| 942a7732-7880-3269-9500-36131b63b98d | -2.8615 | -46.7086 | 2024-11-17 06:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 1f98b43b-d451-38de-b52c-4bf17edeff17 | -2.8801 | -46.7079 | 2024-11-17 06:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 20b3e951-6437-30aa-8639-60862e4afe91 | -3.1287 | -45.0706 | 2024-11-17 06:20:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 740a7e79-de67-3ba7-a3fc-25ae9e72dd47 | -2.6322 | -48.5634 | 2024-11-17 06:20:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 81.4 |
| fca48f8c-1644-308c-b34a-52641ea8f27f | 0.6159 | -51.7676 | 2024-11-17 06:20:00 | GOES-16 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 9c3ed16b-6bdf-3626-aff3-c06195fd79b3 | -3.1836 | -45.2715 | 2024-11-17 06:20:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 00cdf0f3-b9b3-33a9-88d7-3f20a0f3bbf7 | -4.5616 | -47.9925 | 2024-11-17 06:20:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 0fd7a95b-db39-3443-ac01-785d9aac0ea7 | -4.5614 | -48.0141 | 2024-11-17 06:20:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 03c0faa2-5316-3028-99c0-a337db74f072 | -3.5309 | -50.2547 | 2024-11-17 06:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 00ce80b3-5d06-3592-9f99-4d8063873b2e | -2.88 | -46.73 | 2024-11-17 06:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 0a3f0d5a-5b59-3eff-858d-1fb98944b08a | -3.531 | -50.2337 | 2024-11-17 06:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 40.8 |
| 47213d77-f048-3a72-8f44-153eb901fdca | -4.5616 | -47.9925 | 2024-11-17 06:30:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 93d07b87-62e6-3bbf-a645-d16f731b6ddb | -3.1839 | -45.2038 | 2024-11-17 06:30:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 96.5 |
| ddaa7958-2f45-30db-b523-c109c593545e | -2.6322 | -48.5634 | 2024-11-17 06:30:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 90.3 |
| da31cec8-b8b1-3cf2-838d-982db6c688fd | -2.8614 | -46.7306 | 2024-11-17 06:30:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 3e295455-022c-39d6-8b4b-eece139578ac | -3.5309 | -50.2547 | 2024-11-17 06:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 103.0 |
| bfdc3ce8-5632-3d90-ab90-69767d81a40c | -4.5614 | -48.0141 | 2024-11-17 06:30:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| bdca9359-080f-3d58-ae39-f1453789063f | -3.5124 | -50.2553 | 2024-11-17 06:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 41.1 |
| e3b1ff8d-5459-3e2f-bc0b-76e9739f02da | -3.5308 | -50.2757 | 2024-11-17 06:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 39.4 |
| c23a38e2-12ac-3e37-92c4-7ce4d4f9bd6d | 0.6159 | -51.7676 | 2024-11-17 06:30:00 | GOES-16 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 70.2 |
| ac794d4d-594f-3e76-a562-db67fec8c86e | -4.5614 | -48.0141 | 2024-11-17 06:40:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 338f9cae-e673-3b30-8903-89f499e915fd | 0.6159 | -51.7676 | 2024-11-17 06:40:00 | GOES-16 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 70.7 |
| cdf78dce-acec-36a3-b90f-c16c35b1ebc9 | -4.5616 | -47.9925 | 2024-11-17 06:40:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 50.6 |
| dcb801a4-a797-3cd5-9439-1979d8722a9d | -2.6322 | -48.5634 | 2024-11-17 06:40:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 2bfe16d9-2368-357a-a272-473390ee9d43 | 0.6159 | -51.7676 | 2024-11-17 06:50:00 | GOES-16 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 4d0ef161-3948-339d-89e0-81bf49919e7b | -2.6322 | -48.5634 | 2024-11-17 06:50:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| ca08e1fb-acff-3d9c-9986-56a85b844bd8 | -3.7991 | -44.9738 | 2024-11-17 06:50:00 | GOES-16 | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 78.2 |
| f86ea7a6-ee14-3069-b55f-c3bf2c74eb50 | -3.7991 | -44.9738 | 2024-11-17 07:00:00 | GOES-16 | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 140.2 |
| e67e9ef5-84d6-3837-abc8-9c8bd8a8083c | -3.799 | -44.9965 | 2024-11-17 07:00:00 | GOES-16 | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 37079557-fed6-3111-8a4e-abd9b3dafadb | 0.6159 | -51.7676 | 2024-11-17 07:00:00 | GOES-16 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 89b0461d-a854-3ac9-af3a-f4b839e26db7 | -2.6322 | -48.5634 | 2024-11-17 07:00:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 610872a1-a9d2-3d33-83b8-4e5721863e46 | -3.2396 | -45.2242 | 2024-11-17 07:10:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 9c1cd13b-ec9a-349a-ab14-057e71db6494 | -4.5614 | -48.0141 | 2024-11-17 07:10:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 38.6 |
| 30608f60-7aaf-3ed7-81a9-ff96c644c1d2 | 0.6159 | -51.7676 | 2024-11-17 07:10:00 | GOES-16 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 7ac26a45-bdb8-3ee4-aef4-8efef60c6b0a | -3.7992 | -44.9512 | 2024-11-17 07:10:00 | GOES-16 | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 57.5 |
| a7b53a3c-8f04-379c-b18b-c051731c72ad | -2.6322 | -48.5634 | 2024-11-17 07:10:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 46.2 |
| b4328264-9edb-3573-8eaf-2030952704e8 | -3.799 | -44.9965 | 2024-11-17 07:10:00 | GOES-16 | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 65.6 |
| be6e1804-4031-320a-834b-97a3e806bbfb | -3.7991 | -44.9738 | 2024-11-17 07:10:00 | GOES-16 | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 208.6 |
| 8abb3608-cc9a-37fb-b574-612f737580ef | -3.799 | -44.9965 | 2024-11-17 07:20:00 | GOES-16 | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 2077c43b-05ce-3f3f-a369-cd6a3a75eb90 | -3.7991 | -44.9738 | 2024-11-17 07:20:00 | GOES-16 | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 225.8 |
| 9511aecd-158e-3f38-a657-60bc803432f8 | 0.6159 | -51.7676 | 2024-11-17 07:20:00 | GOES-16 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 54.7 |
| d8480ce7-b485-3bc5-b608-ea40805bc965 | -2.6322 | -48.5634 | 2024-11-17 07:20:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 79a8896a-75f5-330f-a078-83a7a34c17b2 | 0.6159 | -51.7676 | 2024-11-17 07:30:00 | GOES-16 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 747d08d0-9fda-3d0e-bec3-1aadb223c609 | -2.6322 | -48.5634 | 2024-11-17 07:30:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 9a6c7750-ebea-3823-8960-a14529a4fac9 | -3.7991 | -44.9738 | 2024-11-17 07:30:00 | GOES-16 | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 144.4 |
| fb423fca-ffe0-321b-aed3-b1d2c69ca91a | -2.6322 | -48.5634 | 2024-11-17 07:40:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 34.7 |


[Clique aqui para ver as próximas entradas](README66.md)

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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8dfe8961-a489-3c2b-b6a9-f242f6e082da | -10.60393 | -37.0208 | 2025-01-31 00:02:00 | TERRA_M-M | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 33.3 |
| 9f59ae6f-4e57-3564-ba40-acb796509310 | -11.59527 | -40.65828 | 2025-01-31 00:02:00 | TERRA_M-M | PIRITIBA | BAHIA | Brasil | 2924801 | 29 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 22bd5be5-3c45-37ba-ab4d-a2a738a36a32 | -10.74547 | -37.05054 | 2025-01-31 00:02:00 | TERRA_M-M | SANTO AMARO DAS BROTAS | SERGIPE | Brasil | 2806602 | 28 | 33 | nan | nan | nan | Mata Atlântica | 25.1 |
| 70b793bb-ace7-3605-bb5e-2b79ed0f672d | -11.55574 | -37.79752 | 2025-01-31 00:02:00 | TERRA_M-M | JANDAÍRA | BAHIA | Brasil | 2917904 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 00468dbe-e225-387e-af20-ffef29bf1860 | -10.61284 | -37.01956 | 2025-01-31 00:02:00 | TERRA_M-M | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 15.1 |
| 7cbc35db-4223-326a-935b-611b6710bf8a | -10.61409 | -37.02868 | 2025-01-31 00:02:00 | TERRA_M-M | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 14.9 |
| b24f0272-7739-3b01-bbfb-7d47e74f67cc | -13.92126 | -41.80529 | 2025-01-31 00:02:00 | TERRA_M-M | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 12.0 |
| e330ada3-1559-3c79-8f30-9048bac1d4fa | -11.24328 | -37.2529 | 2025-01-31 00:02:00 | TERRA_M-M | ITAPORANGA D'AJUDA | SERGIPE | Brasil | 2803203 | 28 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| 7b62db25-cf72-371e-a0d1-47a62755ebd4 | -11.24453 | -37.2622 | 2025-01-31 00:02:00 | TERRA_M-M | ITAPORANGA D'AJUDA | SERGIPE | Brasil | 2803203 | 28 | 33 | nan | nan | nan | Mata Atlântica | 17.4 |
| 05f05970-17f0-3b06-8f19-ead163abe82c | -10.60518 | -37.02991 | 2025-01-31 00:02:00 | TERRA_M-M | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 34.1 |
| 64848c53-0bb1-3359-af78-a11bd9f5f6f2 | -11.59256 | -40.6501 | 2025-01-31 00:02:00 | TERRA_M-M | PIRITIBA | BAHIA | Brasil | 2924801 | 29 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 384881ab-b77f-322c-934c-396752784daf | -6.69377 | -35.04731 | 2025-01-31 00:05:00 | TERRA_M-M | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 11.8 |
| 6d05310c-fecc-3944-bfb1-457094a13d56 | -7.73449 | -35.16184 | 2025-01-31 00:05:00 | TERRA_M-M | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| f624a431-611a-39fd-bed1-38a5dcd2d647 | -7.73311 | -35.15234 | 2025-01-31 00:05:00 | TERRA_M-M | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| 8172f2e1-1b81-3130-9a9b-6c5c51b11ac7 | -7.45784 | -35.16278 | 2025-01-31 00:05:00 | TERRA_M-M | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 13.1 |
| 11e9b522-8b36-34b7-bb65-21fc99ad05cb | -9.43048 | -35.54728 | 2025-01-31 00:05:00 | TERRA_M-M | PARIPUEIRA | ALAGOAS | Brasil | 2706448 | 27 | 33 | nan | nan | nan | Mata Atlântica | 10.9 |
| 7d1f40dd-522d-3f91-9c9c-9e192d7b78e8 | -7.74125 | -35.01407 | 2025-01-31 00:05:00 | TERRA_M-M | IGARASSU | PERNAMBUCO | Brasil | 2606804 | 26 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| cf2b1f72-f091-3f7a-b0ef-5b34a7ee81c1 | -9.30337 | -36.01972 | 2025-01-31 00:05:00 | TERRA_M-M | MURICI | ALAGOAS | Brasil | 2705507 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| da21333e-59f2-3135-9d9d-3f10d382d631 | -9.85642 | -37.28428 | 2025-01-31 00:05:00 | TERRA_M-M | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 4.3 |
| ffc759ff-1e08-3d31-b9b9-5d4a52a5d0e8 | -10.10602 | -38.17603 | 2025-01-31 00:05:00 | TERRA_M-M | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 0e50daaa-7407-3e69-965f-3a4183c69f87 | -7.45923 | -35.17236 | 2025-01-31 00:05:00 | TERRA_M-M | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| bf150879-b32f-37f8-a341-476750229e02 | -7.75042 | -35.0126 | 2025-01-31 00:05:00 | TERRA_M-M | IGARASSU | PERNAMBUCO | Brasil | 2606804 | 26 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 508199a7-3640-34b3-8b84-ec2b44e718db | -4.14853 | -38.25268 | 2025-01-31 00:05:00 | TERRA_M-M | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 20e07ebf-5cd9-3b93-8bda-299c6fbb73a8 | -9.59446 | -36.05895 | 2025-01-31 00:05:00 | TERRA_M-M | PILAR | ALAGOAS | Brasil | 2706901 | 27 | 33 | nan | nan | nan | Mata Atlântica | 13.1 |
| 2b594622-c57b-3d4c-a03c-24648cb279d2 | -6.70502 | -38.08041 | 2025-01-31 00:05:00 | TERRA_M-M | APARECIDA | PARAÍBA | Brasil | 2500775 | 25 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 3403418d-17fc-3fa6-a764-5ac93a20347f | -5.36174 | -36.83855 | 2025-01-31 00:05:00 | TERRA_M-M | CARNAUBAIS | RIO GRANDE DO NORTE | Brasil | 2402501 | 24 | 33 | nan | nan | nan | Caatinga | 9.6 |
| a596ed7b-bc60-367a-b435-d8d211954a61 | -9.30212 | -36.01079 | 2025-01-31 00:05:00 | TERRA_M-M | MURICI | ALAGOAS | Brasil | 2705507 | 27 | 33 | nan | nan | nan | Mata Atlântica | 16.1 |
| 9a987b2a-79e3-3137-99a2-b18ffb7083ba | -17.8781 | -40.1207 | 2025-01-31 00:20:00 | GOES-16 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 73.1 |
| 29943944-32e1-3c53-aeba-dfa860986542 | -9.4174 | -35.9435 | 2025-01-31 00:50:00 | GOES-16 | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 121.9 |
| 01e8b3d5-553f-37cc-a6de-ffe0eb83bccd | -9.417 | -35.9707 | 2025-01-31 00:50:00 | GOES-16 | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 147.2 |
| f0389aa4-5d73-30ea-9244-52b27a587384 | -16.26544 | -59.84268 | 2025-01-31 01:38:00 | TERRA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 85b161f2-51bf-38cf-9ca6-dc7305124fd0 | -16.28069 | -56.79469 | 2025-01-31 01:38:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 17.7 |
| 758608b8-9b3c-3034-8f30-84c83993a8bb | -9.38212 | -35.75791 | 2025-01-31 02:45:00 | NOAA-20 | FLEXEIRAS | ALAGOAS | Brasil | 2702801 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 5e6d9f7a-1654-3c76-9040-1cabca53c773 | -9.38067 | -35.76497 | 2025-01-31 02:45:00 | NOAA-20 | FLEXEIRAS | ALAGOAS | Brasil | 2702801 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 67284110-5ecd-386c-8e01-cb910530ef6d | -17.7962 | -40.1692 | 2025-01-31 03:00:00 | GOES-16 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 115.9 |
| 2e644453-fbaa-3634-bc4f-a6cdfb7cfdf8 | -3.82956 | -41.56562 | 2025-01-31 03:34:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| e3c3361c-de5e-3f25-9042-95024d212b1c | -5.36387 | -36.83863 | 2025-01-31 03:34:00 | NOAA-21 | CARNAUBAIS | RIO GRANDE DO NORTE | Brasil | 2402501 | 24 | 33 | nan | nan | nan | Caatinga | 2.4 |
| c7e5f1af-04cf-38b4-8899-648be359d760 | -5.00814 | -37.30005 | 2025-01-31 03:34:00 | NOAA-21 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 08ea1423-a33f-3846-a4e1-7720adde5398 | -5.29877 | -35.99359 | 2025-01-31 03:34:00 | NOAA-21 | PARAZINHO | RIO GRANDE DO NORTE | Brasil | 2408805 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 23f51019-8bd3-3980-910a-8a8e3ef60aa2 | -9.38102 | -35.76471 | 2025-01-31 03:36:00 | NOAA-21 | FLEXEIRAS | ALAGOAS | Brasil | 2702801 | 27 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| 7b811f12-6f6a-3e5d-9cd8-4444cb636fde | -11.24426 | -37.25446 | 2025-01-31 03:36:00 | NOAA-21 | ITAPORANGA D'AJUDA | SERGIPE | Brasil | 2803203 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| af60c96d-9ded-397f-8284-6a056602b019 | -9.43162 | -35.55712 | 2025-01-31 03:36:00 | NOAA-21 | PARIPUEIRA | ALAGOAS | Brasil | 2706448 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 0d3399b1-0caf-390e-9102-3af82cdb86be | -10.10824 | -38.17306 | 2025-01-31 03:36:00 | NOAA-21 | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2e5c204a-ed41-3d14-9a93-4618057d82aa | -11.5541 | -37.7949 | 2025-01-31 03:36:00 | NOAA-21 | JANDAÍRA | BAHIA | Brasil | 2917904 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 240fd3bb-5451-311e-828f-26b3fffe6e1c | -9.43104 | -35.56072 | 2025-01-31 03:36:00 | NOAA-21 | PARIPUEIRA | ALAGOAS | Brasil | 2706448 | 27 | 33 | nan | nan | nan | Mata Atlântica | 11.7 |
| 2e047973-c783-3b38-9d06-4552ef1505ff | -11.62093 | -37.72487 | 2025-01-31 03:36:00 | NOAA-21 | JANDAÍRA | BAHIA | Brasil | 2917904 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| b1e7d0ac-1690-392b-90c1-cc098b4a1bde | -8.33162 | -37.58501 | 2025-01-31 03:36:00 | NOAA-21 | SERTÂNIA | PERNAMBUCO | Brasil | 2614105 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 68d3e86c-9ed9-3389-8c0f-2592257355fc | -11.55051 | -37.79433 | 2025-01-31 03:36:00 | NOAA-21 | JANDAÍRA | BAHIA | Brasil | 2917904 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 0d55a202-6e16-303b-a3a4-5eedd69090f2 | -11.24711 | -37.25903 | 2025-01-31 03:36:00 | NOAA-21 | ITAPORANGA D'AJUDA | SERGIPE | Brasil | 2803203 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| f80db0d8-4b41-3a2e-ae26-27d3533d9ff2 | -10.69748 | -37.04783 | 2025-01-31 03:36:00 | NOAA-21 | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 7639e29b-af3c-324b-a903-5d7c58961beb | -11.24295 | -37.26242 | 2025-01-31 03:36:00 | NOAA-21 | ITAPORANGA D'AJUDA | SERGIPE | Brasil | 2803203 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 897db09f-4ea8-3e5a-a6dd-efbde2673e48 | -11.24646 | -37.26302 | 2025-01-31 03:36:00 | NOAA-21 | ITAPORANGA D'AJUDA | SERGIPE | Brasil | 2803203 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| d9305b94-603f-354d-a8d7-274f72b37229 | -8.33089 | -37.58947 | 2025-01-31 03:36:00 | NOAA-21 | SERTÂNIA | PERNAMBUCO | Brasil | 2614105 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| fb64ea83-9d2a-3292-8543-8a5cece3202a | -5.43092 | -39.46538 | 2025-01-31 03:36:00 | NOAA-21 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 5d7d2366-1d2c-3746-beb5-0ddd962edfa4 | -10.74489 | -37.04354 | 2025-01-31 03:36:00 | NOAA-21 | SANTO AMARO DAS BROTAS | SERGIPE | Brasil | 2806602 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 6f132d3b-8c7a-3603-8196-9c489e8226c2 | -16.8452 | -39.17122 | 2025-01-31 03:38:00 | NOAA-21 | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 307d7738-1e4d-3fce-968e-c696f4288d64 | -16.07444 | -43.63437 | 2025-01-31 03:38:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 430831ae-06f2-3811-84cb-72418d217bf6 | -17.5085 | -39.27295 | 2025-01-31 03:38:00 | NOAA-21 | ALCOBAÇA | BAHIA | Brasil | 2900801 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| f5819e7b-3cea-3d24-8c46-38767ebcdf0a | -15.70822 | -39.04073 | 2025-01-31 03:38:00 | NOAA-21 | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| dae3b176-c042-389d-ab46-e4b0d94af9f7 | -12.86351 | -38.36874 | 2025-01-31 03:38:00 | NOAA-21 | SALVADOR | BAHIA | Brasil | 2927408 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| f9775777-7e9b-3466-8062-fd68360ca501 | -14.72368 | -39.3744 | 2025-01-31 03:38:00 | NOAA-21 | BARRO PRETO | BAHIA | Brasil | 2903300 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 86792bf1-4670-34e4-9d68-ccfc03bebff2 | -12.40855 | -38.86058 | 2025-01-31 03:38:00 | NOAA-21 | SÃO GONÇALO DOS CAMPOS | BAHIA | Brasil | 2929305 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8e79a1b3-2e9f-3583-a052-4955ec1d0814 | -17.06776 | -39.42524 | 2025-01-31 03:38:00 | NOAA-21 | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 215c46c2-9136-3343-b467-da7de4cb4b45 | -15.59815 | -41.82918 | 2025-01-31 03:38:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 265f2813-99dd-3ab2-953e-4df0a5006e87 | -16.03791 | -42.13416 | 2025-01-31 03:38:00 | NOAA-21 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 5f151d66-3c29-3ccb-a829-d0683859f4bd | -11.66852 | -38.09673 | 2025-01-31 03:38:00 | NOAA-21 | APORÁ | BAHIA | Brasil | 2901908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| a93e40f8-81e9-322f-a22e-69edb141b708 | -17.79967 | -40.16518 | 2025-01-31 03:38:00 | NOAA-21 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 3a151715-bc15-3d3b-b70f-e10271113e2b | -11.25948 | -44.48799 | 2025-01-31 03:38:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 49c8bceb-5d38-3ed3-88ff-fd9b356d6881 | -13.92435 | -41.80057 | 2025-01-31 03:38:00 | NOAA-21 | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b54ce262-1021-3b4d-ad79-62892673855c | -14.11998 | -41.67689 | 2025-01-31 03:38:00 | NOAA-21 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b504b1ce-6d81-3b42-80b4-c9f46005d040 | -19.71695 | -40.35287 | 2025-01-31 03:40:00 | NOAA-21 | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 30df4ed4-5928-35ed-a7de-6ed585bb5893 | -20.43425 | -40.36623 | 2025-01-31 03:40:00 | NOAA-21 | VILA VELHA | ESPÍRITO SANTO | Brasil | 3205200 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 72692179-63e7-3d74-a5d8-03f4db2d35b0 | -3.82979 | -41.56582 | 2025-01-31 03:59:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| d748a341-086e-3f34-820d-e4bcba2d58a5 | -9.43367 | -35.55997 | 2025-01-31 04:01:00 | NPP-375D | PARIPUEIRA | ALAGOAS | Brasil | 2706448 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 0b8b22d8-9304-36b2-88e5-c61390f9318d | -9.37467 | -35.76529 | 2025-01-31 04:01:00 | NPP-375D | FLEXEIRAS | ALAGOAS | Brasil | 2702801 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 8cbeb121-e11d-34ef-8897-8a65d9b8f8d4 | -11.2564 | -44.48949 | 2025-01-31 04:01:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a8a66299-5f92-3195-9cba-3365643f3c92 | -9.42956 | -35.5594 | 2025-01-31 04:01:00 | NPP-375D | PARIPUEIRA | ALAGOAS | Brasil | 2706448 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| d1ba1cf1-a4cc-3951-929c-ae7c4972225a | -6.32353 | -43.73993 | 2025-01-31 04:01:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d050c7aa-328d-35c0-a585-141155faf745 | -9.3787 | -35.76591 | 2025-01-31 04:01:00 | NPP-375D | FLEXEIRAS | ALAGOAS | Brasil | 2702801 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 5a03a56b-bf40-3b6c-b376-b400e54e0034 | -5.36308 | -36.83918 | 2025-01-31 04:01:00 | NPP-375D | CARNAUBAIS | RIO GRANDE DO NORTE | Brasil | 2402501 | 24 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 31eda5d6-113d-361e-a610-dd8a415b200f | -11.26004 | -44.49012 | 2025-01-31 04:01:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1da12493-2d14-3d19-bd8c-0a0ecbd00145 | -8.33207 | -37.58601 | 2025-01-31 04:01:00 | NPP-375D | SERTÂNIA | PERNAMBUCO | Brasil | 2614105 | 26 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 43940b9c-1b12-3fa3-b3fc-3b4673f2ad0c | -9.4301 | -35.5557 | 2025-01-31 04:01:00 | NPP-375D | PARIPUEIRA | ALAGOAS | Brasil | 2706448 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| a8444355-a422-36fe-b567-19f0051797b8 | -9.43226 | -35.55907 | 2025-01-31 04:01:00 | NPP-375D | PARIPUEIRA | ALAGOAS | Brasil | 2706448 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| a8fb490e-7ab8-33a9-b4de-11b1da258e7e | -11.66704 | -38.09723 | 2025-01-31 04:01:00 | NPP-375D | APORÁ | BAHIA | Brasil | 2901908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| ca04cce4-521f-32bc-a6d9-6fb888192fcc | -9.37415 | -35.76888 | 2025-01-31 04:01:00 | NPP-375D | FLEXEIRAS | ALAGOAS | Brasil | 2702801 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 8886927b-788d-3e96-b3ee-146cd0893777 | -9.43585 | -35.56332 | 2025-01-31 04:01:00 | NPP-375D | PARIPUEIRA | ALAGOAS | Brasil | 2706448 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 8d9d1b61-f9b8-351c-9900-a8d7fa5d8434 | -11.24478 | -37.26025 | 2025-01-31 04:01:00 | NPP-375D | ITAPORANGA D'AJUDA | SERGIPE | Brasil | 2803203 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| a3cac58a-53f0-34a5-993f-2913271b8d78 | -7.84326 | -35.20042 | 2025-01-31 04:01:00 | NPP-375D | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| 0f95ad32-12c9-3468-a3f5-575f19d492a3 | -11.24544 | -37.2556 | 2025-01-31 04:01:00 | NPP-375D | ITAPORANGA D'AJUDA | SERGIPE | Brasil | 2803203 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 8088e392-e070-3367-a503-1c02e1e8089f | -9.43174 | -35.56274 | 2025-01-31 04:01:00 | NPP-375D | PARIPUEIRA | ALAGOAS | Brasil | 2706448 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 7861974a-a409-3c4e-ac01-ba4775f7363e | -11.55558 | -37.793 | 2025-01-31 04:01:00 | NPP-375D | JANDAÍRA | BAHIA | Brasil | 2917904 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 7538c86f-e40d-399a-8409-ee1f21e9726b | -9.43313 | -35.56364 | 2025-01-31 04:01:00 | NPP-375D | PARIPUEIRA | ALAGOAS | Brasil | 2706448 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 572ce346-85cf-3c68-8ef8-7207c6f01e62 | -5.43084 | -39.46567 | 2025-01-31 04:01:00 | NPP-375D | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 57e7c698-cdff-3078-bbba-0dfdd16ede14 | -5.36218 | -36.83987 | 2025-01-31 04:01:00 | NPP-375D | CARNAUBAIS | RIO GRANDE DO NORTE | Brasil | 2402501 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| fec4b3da-40ae-37b6-a2d4-4b57b77d7c9d | -11.24413 | -37.26489 | 2025-01-31 04:01:00 | NPP-375D | ITAPORANGA D'AJUDA | SERGIPE | Brasil | 2803203 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| fb9c9975-29ed-3d51-98b5-eb9923c2d82a | -6.42594 | -40.02016 | 2025-01-31 04:01:00 | NPP-375D | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 6e7ab0b4-6164-3831-a77e-bc8f262bb184 | -6.32516 | -43.73822 | 2025-01-31 04:01:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d704185e-74ef-3856-bb9e-0efe5da02aaf | -7.83917 | -35.19975 | 2025-01-31 04:01:00 | NPP-375D | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| cedb232b-fb7f-3de8-9733-c7f423bb3add | -5.86728 | -39.16853 | 2025-01-31 04:01:00 | NPP-375D | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |


[Clique aqui para ver as próximas entradas](README2.md)

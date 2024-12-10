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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f8a1d361-2e5b-37d7-a9cd-1ff8c9138ab5 | -1.5442 | -52.68095 | 2024-12-10 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7b48999f-7fd0-38d5-aef9-bb76dbf2f0d2 | -12.24899 | -52.4558 | 2024-12-10 04:53:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6083151c-90e8-3b97-ab90-4532625bd717 | -2.81345 | -53.069 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 22e96939-c0e3-3e75-af25-0457f612ff26 | -3.82034 | -51.26049 | 2024-12-10 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d985db31-2d58-3015-834f-3580d6215a93 | -4.54861 | -48.01024 | 2024-12-10 04:53:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8f9c36e5-c724-32a1-99d3-c2d7b9f68e6c | -1.69518 | -55.67371 | 2024-12-10 04:53:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 805e7de5-e59e-30a8-bff0-182ad066ea25 | -3.50755 | -54.49659 | 2024-12-10 04:53:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 690e43d0-6a83-3396-ab28-c3f5361cd942 | -3.51344 | -52.18363 | 2024-12-10 04:53:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 98589f48-0864-352d-b180-1dc4c37a2c79 | -4.54686 | -48.01313 | 2024-12-10 04:53:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a8cf5b7a-5c85-34de-8f89-ccebdd6050ab | -2.39867 | -55.32138 | 2024-12-10 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f16f27f3-5279-38e2-a9e1-1bd20be04e11 | -2.8201 | -53.04847 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a6e14cb6-3d34-3e82-a9fb-3b2600665454 | -4.39428 | -47.77632 | 2024-12-10 04:53:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 18917531-c0a9-3ff2-a0c9-9fa6d7870a74 | -2.82065 | -53.04496 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e1e5e0bb-e29c-3734-ad49-65335d1447b1 | -2.62864 | -48.06142 | 2024-12-10 04:53:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| a7687a33-472a-3642-8d92-a2c5d7a62565 | -2.17368 | -53.65079 | 2024-12-10 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 12672db7-e023-3b21-824d-bb8c2412062e | -3.70307 | -50.93906 | 2024-12-10 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 466b31ee-f866-33c6-9d79-bb401a271074 | -2.9913 | -52.84638 | 2024-12-10 04:53:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 70362445-db5d-38f9-8434-5bb32c183825 | -2.814 | -53.06549 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 902e89bc-9faa-3f6e-8750-004c4cdbfa8f | -3.71754 | -52.44407 | 2024-12-10 04:53:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6d38817c-8085-3935-96f3-80d19ec928e5 | -6.91254 | -43.50946 | 2024-12-10 04:53:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 02b462dd-7c53-3ce2-8544-049e0e984e2d | -3.46833 | -53.966 | 2024-12-10 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| df894a24-5107-3d0b-937a-a65b0d7d3530 | -3.02872 | -54.19437 | 2024-12-10 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 01384f1c-0cd7-369b-b843-bee24362550c | -2.45994 | -53.65701 | 2024-12-10 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5282ee14-a2f6-3450-8e2c-dbc97589457d | -1.90807 | -52.83437 | 2024-12-10 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 194de749-c464-331e-97d7-6692cffc2dc8 | -3.79174 | -50.1078 | 2024-12-10 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 34eb9ec4-a7e8-339e-92ba-74c22fc5d557 | -4.89117 | -48.05304 | 2024-12-10 04:53:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 434a9940-accb-3a67-bb4c-1aeee4196530 | -2.45484 | -53.64516 | 2024-12-10 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ae277614-e054-34c0-93d1-238ad0729199 | -2.81722 | -52.98006 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 952ae50f-583a-37e2-ae69-b2ad38b3fc65 | -3.08028 | -54.04551 | 2024-12-10 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| df4d856a-515b-3c0f-9395-c85d329420e8 | -5.51579 | -46.26 | 2024-12-10 04:53:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4582908c-d2ef-3135-81e8-6705ffecbf07 | -10.02998 | -53.75034 | 2024-12-10 04:53:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| a5fb7214-df48-3e67-b36f-30ea05777678 | -2.9974 | -52.85087 | 2024-12-10 04:53:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 1219a2f0-a65f-35bd-bf04-43489e15de0a | -3.6116 | -54.30315 | 2024-12-10 04:53:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 12d74f7f-05e8-3d71-a3de-eba39116e141 | -3.97615 | -45.623 | 2024-12-10 04:53:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9fef02b4-9214-3772-ae2a-20a7adaedf48 | -2.36469 | -53.8413 | 2024-12-10 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ea11665a-2dd9-39e8-88ec-887bc4edc8fb | -2.62933 | -48.05687 | 2024-12-10 04:53:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 357fda2f-373f-3d08-abe7-1682959d122d | -3.46551 | -53.96178 | 2024-12-10 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cbbb4649-5053-3858-90d2-5cd82b1fa7f7 | -2.4449 | -49.02741 | 2024-12-10 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4247498e-e829-3f6b-85dc-838d6671e265 | -4.5717 | -48.92256 | 2024-12-10 04:53:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f719f873-950b-34a0-ba81-3b9975eb0c0a | -2.47519 | -53.62604 | 2024-12-10 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d09639f5-08e2-3a19-8044-97c7af954a4d | -4.48614 | -43.8504 | 2024-12-10 04:53:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 66427fab-1382-3d1e-ba89-26b154708e58 | -2.79161 | -52.86172 | 2024-12-10 04:53:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| edc24685-4dab-33af-a4ab-918c88eaa9a7 | -3.53031 | -54.58969 | 2024-12-10 04:53:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ab577bcb-d9d1-3672-918e-7a6f9e9f1e31 | -1.64483 | -45.91616 | 2024-12-10 04:53:00 | NOAA-21 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a9fdc691-af12-3bb8-8ce5-299c453384c4 | -5.59064 | -49.11204 | 2024-12-10 04:53:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4ada9a57-a0d3-38ee-82dd-60c9ed4babda | -2.95902 | -53.72317 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6d64408f-848b-3228-9476-35586e144101 | -2.7571 | -54.15639 | 2024-12-10 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 477d6696-f423-308f-a1dd-e3e8ea841bb2 | -3.50764 | -54.67756 | 2024-12-10 04:53:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 552f5e24-a279-3abc-8735-1dac698f950e | -3.92271 | -53.67066 | 2024-12-10 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 01d1b3f9-4673-30f1-b09a-e34ab56bc911 | -3.27651 | -51.08283 | 2024-12-10 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b1fc69ba-bba2-316a-bfc6-38708cb976ea | -2.63985 | -54.68681 | 2024-12-10 04:53:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2361cbfd-c401-3280-ad19-85c16cbf0ce4 | -12.25064 | -52.44461 | 2024-12-10 04:53:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ec406ad4-c2fe-3cf5-99cc-5bc76a29635d | -3.61271 | -50.57184 | 2024-12-10 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e4d57326-2068-328a-a142-b19c205a7483 | -2.45823 | -53.66792 | 2024-12-10 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 51b1eb5b-c4ca-30cd-bd57-3805cfdbfdee | -12.59669 | -48.52158 | 2024-12-10 04:53:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2ad7c1c5-172b-3ec2-ba12-24e9288f6a31 | -10.38243 | -52.00346 | 2024-12-10 04:53:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c918ec88-4a8f-31d0-a9e4-060a47bc8bf8 | -3.34791 | -50.99315 | 2024-12-10 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3d8d9b36-f2d5-3185-a303-770a03a55df2 | -3.94323 | -51.0373 | 2024-12-10 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eba3a96f-7521-3b55-bd2b-17a77eb242f5 | -3.52881 | -53.94197 | 2024-12-10 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 99f51024-f05d-3e2d-97c0-da5896e98fcf | -4.56068 | -48.92085 | 2024-12-10 04:53:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c9c1c916-1359-35c0-99ce-6b39ed8a9d79 | -2.41352 | -53.66483 | 2024-12-10 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d8dffec4-da72-3600-af6c-06112029e653 | -3.5917 | -53.3131 | 2024-12-10 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7c9e6a13-5f09-3a18-ab50-8a94968d4d69 | -3.60038 | -53.8413 | 2024-12-10 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e4c7e805-d7fe-383f-9774-4470183955c5 | -2.4718 | -53.62553 | 2024-12-10 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f45fb381-f8e6-33cc-90c6-5d3572beccf0 | -2.83512 | -53.06155 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b955a60e-8c3d-3d20-a4aa-7961cdeb0f20 | -2.53449 | -48.92033 | 2024-12-10 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 00569359-662b-3944-a3f4-1fbaa612e6cf | -2.86537 | -54.22726 | 2024-12-10 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 73df0ba9-c1ee-3a42-a448-f3371ee86c4f | -4.04844 | -54.09681 | 2024-12-10 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a77829e2-0c45-31dc-8afc-61bade5d3481 | -3.83826 | -50.14959 | 2024-12-10 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3a009621-3db6-3169-8e9e-0bf236284c7e | -3.10419 | -53.75661 | 2024-12-10 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b3ee7c68-3f76-315a-8335-01de23a55b6f | -10.35866 | -57.24672 | 2024-12-10 04:53:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2fbdee2d-dcfe-3837-9b22-20b4eb1cf714 | -12.3647 | -54.1733 | 2024-12-10 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 80aad4af-b96f-3da0-9c26-eab469140aa2 | -3.23834 | -52.78935 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0ac943da-466f-384b-8669-91afa478b453 | -3.04871 | -54.24321 | 2024-12-10 04:53:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8355598c-d6f3-3ec2-8d08-16bb5eaa6cf4 | -2.6105 | -54.23842 | 2024-12-10 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8fa5d3f1-ca04-3745-a709-5f1ec9be557a | -2.6978 | -52.91853 | 2024-12-10 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9e550a2b-d978-3ae7-8552-7f3b170fe5b1 | -3.03275 | -54.19116 | 2024-12-10 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9e1597bf-8305-36ef-91be-f3b1e878dac6 | -2.9625 | -53.11723 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 41574244-bcad-3919-80e6-ef7a5fbdc8b4 | -3.10071 | -54.07143 | 2024-12-10 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 59d23db1-0fea-3a85-ac5f-185d79a12039 | -3.68583 | -54.32175 | 2024-12-10 04:53:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c4b49ff2-0275-34be-9223-cb5a79d48a55 | -2.78719 | -52.86816 | 2024-12-10 04:53:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 9c930f14-367b-31c2-aceb-6dc1815ee253 | -4.04327 | -50.80416 | 2024-12-10 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 765d312b-7353-3f07-84ff-3d789d39b934 | -2.41744 | -53.68413 | 2024-12-10 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3d268a51-7b60-3e00-916f-da3063d4443e | -2.88536 | -49.01129 | 2024-12-10 04:53:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 07637898-e8dd-3d9e-8ef6-32e01bb63bbe | -5.62793 | -44.83967 | 2024-12-10 04:53:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ed1a5bcf-2192-3254-ab48-80e740570174 | -12.92548 | -47.88799 | 2024-12-10 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eb512d3f-94f5-3631-ac7f-6c562d35e7fc | -2.47343 | -49.03182 | 2024-12-10 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 389d924c-c23e-3a35-9601-eb455d607d43 | -3.05215 | -54.24379 | 2024-12-10 04:53:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 01f2bb8c-91de-3066-bc3b-dae332b225ef | -2.38009 | -53.8324 | 2024-12-10 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d32146b0-ddf7-35ae-88ad-25771ec69125 | -2.30126 | -53.9994 | 2024-12-10 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 974481c5-54ed-32f9-bacd-2654cd0b68a8 | -12.37682 | -54.16083 | 2024-12-10 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| aeeef187-7859-3c2b-ba01-d0fd5a154755 | -3.20957 | -46.81119 | 2024-12-10 04:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 032cd8e6-a040-3e48-bdfa-3b80d45a04da | -4.39649 | -47.7613 | 2024-12-10 04:53:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 04b06f34-f38e-3db2-b6c8-e89af547ff99 | -12.16233 | -55.17386 | 2024-12-10 04:53:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c6dc9634-07a9-3e1a-987d-f2b023de1060 | -12.25009 | -52.44834 | 2024-12-10 04:53:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8fae6c9e-a67c-3369-bb12-d2a94f743e02 | -1.64543 | -45.91216 | 2024-12-10 04:53:00 | NOAA-21 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| faacf101-501c-3bd2-8429-e1adc8581e64 | -5.91351 | -48.05604 | 2024-12-10 04:53:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 22.1 |
| e11ffd11-f01c-365f-a5c3-595fa82f8ad0 | -12.85884 | -51.93552 | 2024-12-10 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1d2d0e55-77c5-374c-b3f3-2ed6aa03c939 | -4.01852 | -54.75064 | 2024-12-10 04:53:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3b17f0d2-347c-371e-8339-151b5d4076e0 | -2.92228 | -52.96054 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |


[Clique aqui para ver as próximas entradas](README25.md)

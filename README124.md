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

## Dados Diários - Página 124

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1fb1a6e5-32af-3954-9417-b8fa6f0ad9bf | -11.0256 | -57.2038 | 2024-10-10 04:46:09 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 1780715b-468c-33b7-8a44-d4d35a83f40e | -11.0443 | -57.2222 | 2024-10-10 04:46:09 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 64.2 |
| e0ab9f4e-375d-3b82-8262-c44db1c634b7 | -21.61257 | -44.64717 | 2024-10-10 04:49:00 | NOAA-20 | CARRANCAS | MINAS GERAIS | Brasil | 3114600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 3b6b1205-6bd6-3792-aa6e-efc317aa644f | -21.61224 | -44.65068 | 2024-10-10 04:49:00 | NOAA-20 | CARRANCAS | MINAS GERAIS | Brasil | 3114600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 284ac14a-a827-3de8-99bb-a80584bfa2b4 | -21.61191 | -44.65414 | 2024-10-10 04:49:00 | NOAA-20 | CARRANCAS | MINAS GERAIS | Brasil | 3114600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 355ed782-e63b-34a1-abc6-5729b79f173d | -21.60651 | -44.65326 | 2024-10-10 04:49:00 | NOAA-20 | CARRANCAS | MINAS GERAIS | Brasil | 3114600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 4e8315d9-a1c0-3efc-b987-c191fe0bbda6 | -21.39331 | -55.69012 | 2024-10-10 04:49:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 88a78934-ac1d-3270-87c5-9b4b3a2664d0 | -21.38997 | -55.68947 | 2024-10-10 04:49:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f99faa51-54dd-3bae-b4f7-06926308623d | -2.6717 | -53.3299 | 2024-10-10 04:55:20 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 105.7 |
| dd830d64-a7de-3c51-a6dc-6dc0e1788d2a | -2.69 | -53.3497 | 2024-10-10 04:55:20 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 04c5b11b-36aa-3877-8ca3-edcbbf354776 | -2.6716 | -53.3502 | 2024-10-10 04:55:20 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 234.8 |
| e51511a7-9936-3ad8-89f9-75f749f50be9 | -2.6716 | -53.3704 | 2024-10-10 04:55:20 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 43.0 |
| 382513d5-1eb8-338b-b25f-c42672bc258b | -2.6533 | -53.3506 | 2024-10-10 04:55:20 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 131.1 |
| 08600220-db86-368b-8385-3452b8dc6c3b | -6.7654 | -59.3252 | 2024-10-10 04:55:44 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 79.3 |
| cb1df219-b742-31a6-ba48-ad0478f17001 | -6.7655 | -59.3059 | 2024-10-10 04:55:44 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 86bfe3f4-6040-3c14-8242-2a7291878ba4 | -6.7839 | -59.3245 | 2024-10-10 04:55:44 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 21846643-59a0-3bfa-9035-ec35242b2396 | -6.784 | -59.3052 | 2024-10-10 04:55:44 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 17ee0a58-5e5f-30a9-bbd8-40b0979c06c9 | -7.0417 | -59.4103 | 2024-10-10 04:55:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 0278ccfa-f927-391b-8ef0-fa25eb013b2d | -7.0601 | -59.4095 | 2024-10-10 04:55:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.3 |
| fe5937f7-f87c-3368-bf50-d90a97613964 | -7.0785 | -59.428 | 2024-10-10 04:55:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 2e9d8a13-9ed7-3491-ab2f-8dfa6d3302e9 | -7.0786 | -59.4087 | 2024-10-10 04:55:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 151.8 |
| 69245501-ee61-3694-8a6c-ad4341b2f625 | -7.0971 | -59.408 | 2024-10-10 04:55:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 94.5 |
| 3b6f9eac-2c31-31fc-82bc-e8b4dc6d5c5d | -10.3707 | -61.2513 | 2024-10-10 04:56:04 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 636b88c1-48ac-3a3e-9174-e8b396a82da1 | -10.3708 | -61.232 | 2024-10-10 04:56:04 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 51.9 |
| ded23887-65e7-31f1-90e2-d5736536037a | -4.95111 | -42.9818 | 2024-10-10 05:12:00 | AQUA_M-M | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 1911f7c3-2739-3793-b991-246381f78daf | -4.94975 | -42.99096 | 2024-10-10 05:12:00 | AQUA_M-M | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 69918b6a-5eb5-39c9-9e29-ea0399442ac3 | -5.76032 | -43.19154 | 2024-10-10 05:12:00 | AQUA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 5.3 |
| fd64e6fd-ad15-34e4-a819-9b11408474cf | -5.5149 | -42.78824 | 2024-10-10 05:12:00 | AQUA_M-M | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 79042825-807f-3d29-a01d-7908ac4351ff | -5.51353 | -42.79758 | 2024-10-10 05:12:00 | AQUA_M-M | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| d921d6c2-ce68-3f5c-90eb-14c8103d658c | -4.50185 | -43.83878 | 2024-10-10 05:12:00 | AQUA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 11278ac9-f477-3f40-a05a-868d8e8c4ebc | -4.50053 | -43.84759 | 2024-10-10 05:12:00 | AQUA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d0365aec-84ee-354c-afc9-45b6147a2c5e | -5.49645 | -44.27794 | 2024-10-10 05:12:00 | AQUA_M-M | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 29ec64ae-2ae5-3032-9567-9c58743ddd68 | -5.49513 | -44.28675 | 2024-10-10 05:12:00 | AQUA_M-M | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| b108faf6-7c08-3f20-b361-18ecadbada85 | -5.23406 | -44.79632 | 2024-10-10 05:12:00 | AQUA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| f15c7034-a99e-37e6-9604-57c7295302e5 | -3.80814 | -45.49549 | 2024-10-10 05:12:00 | AQUA_M-M | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 65b5d051-c788-30ff-bcbe-f7150d046e42 | -5.20505 | -44.92872 | 2024-10-10 05:12:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 3df69eff-edc9-341f-b273-708682e483ef | -5.20371 | -44.93764 | 2024-10-10 05:12:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 52815ef6-db3e-35cc-91f9-e501a74c03bb | -5.09988 | -46.11287 | 2024-10-10 05:12:00 | AQUA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 581c92f7-2773-3ecc-a8e6-359c04bc7408 | -2.17214 | -45.93761 | 2024-10-10 05:12:00 | AQUA_M-M | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 32.5 |
| 17dbdfe0-e5e9-394f-aef1-bedc2391dcc7 | -2.1706 | -45.9478 | 2024-10-10 05:12:00 | AQUA_M-M | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 6e9469fc-26c0-302d-b13c-827cf976a691 | -4.85247 | -47.5181 | 2024-10-10 05:12:00 | AQUA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 39963d15-7068-330e-a8b4-a8112b98a34c | -3.93074 | -46.44864 | 2024-10-10 05:12:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 863df502-523e-3b06-a1c4-8def66b7e491 | -3.91002 | -46.4562 | 2024-10-10 05:12:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |
| f40d028a-ff78-312e-a21e-41bd0098b180 | -3.90046 | -46.45479 | 2024-10-10 05:12:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 7.0 |
| f0e30d8c-363b-3442-b4f1-f04c800817c2 | -2.75334 | -48.68938 | 2024-10-10 05:12:00 | AQUA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 1f5f4afd-6cbf-34e2-a4ac-cf26b6beb2be | -4.12123 | -48.26302 | 2024-10-10 05:12:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 7fb8db46-f8fb-34b4-b81b-19097a828895 | -4.1191 | -48.27672 | 2024-10-10 05:12:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| c54784d2-9d74-3028-940c-b26c53663e40 | -4.11258 | -48.24769 | 2024-10-10 05:12:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 36.1 |
| 5885f00c-6d3b-3135-be13-5f8c88385065 | -4.11228 | -49.06783 | 2024-10-10 05:12:00 | AQUA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 7f789051-f31c-3652-8041-2fb4505000eb | -4.11044 | -48.26133 | 2024-10-10 05:12:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 161.1 |
| 72b50bc8-c08c-3ffd-89a4-d87491e12149 | -4.10828 | -48.27516 | 2024-10-10 05:12:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 7bd4d5b0-3a7e-3bc1-b328-0d453c9b5dc0 | -4.10178 | -48.24612 | 2024-10-10 05:12:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 22.4 |
| 3f5fe748-2c15-3bf0-9794-68ad1baeae73 | -4.09965 | -48.25965 | 2024-10-10 05:12:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 31.0 |
| b3878b53-9cb4-34e5-bc80-a0629a067fb1 | -4.09751 | -48.27327 | 2024-10-10 05:12:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 4190c85d-0320-3849-8b58-6683a8cfbd75 | -3.9238 | -48.34674 | 2024-10-10 05:12:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 3a55b954-b596-3bcd-b8a9-64fae43ff86d | -3.91505 | -48.33131 | 2024-10-10 05:12:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 08fb776a-6831-352b-9dd4-4c620cb4850c | -3.91289 | -48.34508 | 2024-10-10 05:12:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 23.4 |
| 24f5649e-86d1-34e2-bb3c-53d0fe2b0c2c | -4.7948 | -48.89263 | 2024-10-10 05:12:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 71845f4a-83d8-3d24-be86-ce984b1a34b7 | -2.99161 | -49.52246 | 2024-10-10 05:12:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 67343ef2-a5ab-3ecc-bc95-df5b0c26f31a | -2.95188 | -49.19423 | 2024-10-10 05:12:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 2d28c991-16c0-3edb-b824-0d1e69632b68 | -2.7848 | -49.24201 | 2024-10-10 05:12:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 614a13ac-531e-3c91-ada2-8924ec3c968b | -2.60708 | -49.79268 | 2024-10-10 05:12:00 | AQUA_M-M | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 69c1d79d-7ea9-30ab-96c8-2c0cac0f2809 | -3.68836 | -50.11598 | 2024-10-10 05:12:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 6f792a27-2786-38ba-8efa-44c952486754 | -4.0986 | -51.00989 | 2024-10-10 05:12:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 21.1 |
| f40718f6-b0e8-304a-b971-5e859046fb8c | -4.09422 | -51.01377 | 2024-10-10 05:12:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 1d7ed3ff-a021-30ed-bd5e-d27dea8688b2 | -4.08512 | -51.00776 | 2024-10-10 05:12:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 891e493b-4e50-333f-a850-aae98e30a410 | -3.3374 | -53.2159 | 2024-10-10 05:12:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 43.1 |
| 768bf5f4-b36b-3f2a-b4fa-563d111989ee | -3.33192 | -53.20737 | 2024-10-10 05:12:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 38.1 |
| 36d8f4ff-5fac-3e67-8fb4-adf782513a2a | -2.85634 | -52.89761 | 2024-10-10 05:12:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 32.9 |
| 449eaf19-cdf0-3695-bffd-bd5f844353ee | -2.8512 | -52.93013 | 2024-10-10 05:12:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 36.8 |
| c7e5be93-505b-3769-84bb-8d9419cff259 | -2.68292 | -53.319 | 2024-10-10 05:12:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 118.1 |
| 2042751e-cc52-3cc3-b1eb-b2d036ac1d4a | -2.67722 | -53.3548 | 2024-10-10 05:12:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 152.4 |
| d171a281-dec4-3a3c-ab45-445211fe42fe | -2.676 | -53.31314 | 2024-10-10 05:12:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 105.2 |
| cfb4142e-b66a-387f-a33e-e3a22064e0dd | -2.67052 | -53.34903 | 2024-10-10 05:12:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 285.8 |
| bb89ed28-034c-3342-9741-00b59b853f7f | -2.66637 | -53.31641 | 2024-10-10 05:12:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 74714da3-f479-3e81-a23e-3c272b02dd05 | -2.66063 | -53.35223 | 2024-10-10 05:12:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 139.3 |
| e3250329-dd0a-338a-80a9-7ed856cbfb4e | -2.65394 | -53.34641 | 2024-10-10 05:12:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 179f6fbd-6181-37bb-9759-b63ba90eec17 | -15.236 | -43.58988 | 2024-10-10 05:14:00 | AQUA_M-M | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 7.8 |
| a9038071-02e9-3a29-bc29-3a0b82d01d57 | -6.00603 | -42.89609 | 2024-10-10 05:14:00 | AQUA_M-M | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 8f3c58eb-70f8-3903-8306-e151c4f42942 | -6.00468 | -42.90536 | 2024-10-10 05:14:00 | AQUA_M-M | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| fb8ee1f3-d435-3263-a02f-21d73c82a594 | -6.27039 | -43.42366 | 2024-10-10 05:14:00 | AQUA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| c8358a08-1ed2-391a-b4ee-7f1b429b6ed4 | -7.22674 | -42.2962 | 2024-10-10 05:14:00 | AQUA_M-M | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 1d1b86af-7063-3786-882b-2536e64ee04e | -7.09814 | -42.61972 | 2024-10-10 05:14:00 | AQUA_M-M | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 5e16f91f-b8dc-37b5-a14b-89938fbd70d3 | -6.72954 | -43.55856 | 2024-10-10 05:14:00 | AQUA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 22.3 |
| ffb19d9c-a6fe-3733-8390-142ec2eda55a | -7.68956 | -42.98756 | 2024-10-10 05:14:00 | AQUA_M-M | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 14.8 |
| fb508140-372b-3bc2-bf29-45fb6444c215 | -7.65404 | -42.39748 | 2024-10-10 05:14:00 | AQUA_M-M | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| ee6810a5-adc4-3415-92cd-7db305bf0e83 | -8.1556 | -42.95549 | 2024-10-10 05:14:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 74.3 |
| 004d0379-8423-358c-8e53-4d28f0834c39 | -8.15419 | -42.96529 | 2024-10-10 05:14:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 78.9 |
| e844c11f-de86-30a5-b1db-91c9fa03b0b4 | -12.30065 | -43.7352 | 2024-10-10 05:14:00 | AQUA_M-M | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| e997ee34-3fed-3f34-8c95-dbdb01ac1177 | -12.29133 | -43.73389 | 2024-10-10 05:14:00 | AQUA_M-M | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 41.3 |
| 4713d07c-81ea-31be-ab3a-8501eafc335b | -12.28993 | -43.74377 | 2024-10-10 05:14:00 | AQUA_M-M | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 15.8 |
| a91f2115-2850-3412-8fb5-ca2e78dba8e0 | -11.90146 | -43.88401 | 2024-10-10 05:14:00 | AQUA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f4d1f6fd-e524-39f3-adf4-f1d40fb8ddea | -11.52668 | -43.99278 | 2024-10-10 05:14:00 | AQUA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| f985eef8-4c58-37e0-b788-0c71d69d22ed | -14.045 | -44.01648 | 2024-10-10 05:14:00 | AQUA_M-M | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 13.3 |
| f924e6ba-b17a-33ac-972c-81d199a45572 | -14.04359 | -44.02668 | 2024-10-10 05:14:00 | AQUA_M-M | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 15.1 |
| b6bfa62c-5d57-31ad-9e8e-c9c4ca7c6acc | -14.03789 | -44.02026 | 2024-10-10 05:14:00 | AQUA_M-M | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 8b0820d8-b1f7-33f3-8e2a-ba0bd51cb711 | -6.35132 | -43.81585 | 2024-10-10 05:14:00 | AQUA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| d58acd6c-9751-36bc-83b3-e90c8b9be09c | -6.33013 | -43.76138 | 2024-10-10 05:14:00 | AQUA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| f6d9f993-2734-3995-b020-568abe9bf987 | -6.17414 | -43.70458 | 2024-10-10 05:14:00 | AQUA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| d6404ee2-8bc9-3742-9507-127809daef89 | -6.00194 | -43.48668 | 2024-10-10 05:14:00 | AQUA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |


[Clique aqui para ver as próximas entradas](README125.md)

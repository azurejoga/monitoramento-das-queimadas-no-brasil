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
| 17cda428-3964-379c-a7a0-3d7de15bdb77 | -5.28421 | -60.11609 | 2026-09-09 05:29:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e8adc3bd-0a0b-3ec8-ad7d-d0daa9ded955 | -5.37138 | -56.0248 | 2026-09-09 05:29:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 5186e5b1-274c-3c89-b500-148618000ae2 | -3.38355 | -61.32087 | 2026-09-09 05:29:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 834479b0-d635-3796-b7b6-36ad3c74270b | -6.80001 | -58.95078 | 2026-09-09 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 14e98da8-ffd1-3c39-8be9-0979473bc2fd | -3.41491 | -61.31514 | 2026-09-09 05:29:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b67c8308-4e33-364a-a1e8-91e37f296148 | -3.96561 | -59.36282 | 2026-09-09 05:29:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6c20951a-59d4-31ec-a5f7-44cfea4ab1a7 | -5.91994 | -63.47527 | 2026-09-09 05:29:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2cc11d34-bad5-30e1-84a5-bcaec8ef880a | -5.28478 | -60.11238 | 2026-09-09 05:29:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 85463990-b9f2-36e4-a114-ecbaebd0124d | -5.18776 | -59.76028 | 2026-09-09 05:29:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 258ca7e0-34b7-3a18-821a-49b8656c7c9b | -7.12403 | -56.5146 | 2026-09-09 05:29:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8d2221df-a212-3630-b81c-70769f6f2cfd | -6.95492 | -59.75911 | 2026-09-09 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b7168e1c-7b51-31f6-bb15-fa2f6bb1a589 | -2.9372 | -57.88653 | 2026-09-09 05:29:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bfd3a3c0-9e05-33ca-8519-ca65234821a2 | -3.14048 | -60.63071 | 2026-09-09 05:29:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 072f35df-ca2d-3572-b2e7-6b672181bdab | -5.37452 | -56.03363 | 2026-09-09 05:29:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 20e6bcd8-0f7f-3723-91ed-e5244f07be80 | -3.48112 | -60.0063 | 2026-09-09 05:29:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0b341ec6-81f4-3654-a2d4-7f9764751d9a | -4.44452 | -54.82711 | 2026-09-09 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 43cc7f25-7623-3778-ae83-baae4c72edf8 | -4.43991 | -54.82988 | 2026-09-09 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7aa41196-a862-3539-82c3-7c583fcda39a | -3.43426 | -59.26125 | 2026-09-09 05:29:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4ca4dbe3-cee5-34b6-abca-f137653ee57c | -3.13716 | -60.6302 | 2026-09-09 05:29:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 84e86c62-b373-3b87-be26-98c5e5f150ba | -6.75953 | -59.73851 | 2026-09-09 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2ee46a46-b5ce-3f10-9d59-a39b14e06e25 | -5.37021 | -56.033 | 2026-09-09 05:29:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 91a9851d-4b0a-34c3-b408-04da5c4e4f95 | -6.7652 | -58.95882 | 2026-09-09 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ee5b733d-4a03-390b-ba62-c7e5cf7179f0 | -5.59046 | -60.24516 | 2026-09-09 05:29:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a19ca6b0-67dc-3501-b1b8-f793dc58ce0d | -3.13994 | -60.6342 | 2026-09-09 05:29:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fabc7ea1-5726-3e6f-9863-9332a444e526 | -3.41768 | -61.31908 | 2026-09-09 05:29:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3b12129f-de65-30ec-8738-e768e381557f | -6.78663 | -58.94004 | 2026-09-09 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6cbac98c-ea2a-349f-a5e7-5e5213cb0df8 | -4.91357 | -55.82235 | 2026-09-09 05:29:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c9d79296-8971-3ff2-bc37-822d24cfe32c | -3.37623 | -59.40815 | 2026-09-09 05:29:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b6d72dd0-a94d-359a-83ca-8e0a55e49ea2 | -5.44497 | -60.23471 | 2026-09-09 05:29:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6b90397b-d9ea-3f38-8b44-1d1d7189a6be | -3.41747 | -59.25475 | 2026-09-09 05:29:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 021e6d40-f619-3e71-b9b4-3eacd3292a6a | -3.36586 | -59.42974 | 2026-09-09 05:29:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5b2f5ace-43a3-32f1-bb3c-3c35e000ebdc | -3.39687 | -61.34405 | 2026-09-09 05:29:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8b79e0e1-a102-35aa-b3e5-a8fe4077641d | -6.83926 | -51.49647 | 2026-09-09 05:29:00 | NOAA-21 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f03f39aa-b25f-396c-87da-7d58b1b19911 | -6.75869 | -59.73903 | 2026-09-09 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b9e5e8a4-69d9-38eb-8d8c-910458d56432 | -7.08364 | -59.82106 | 2026-09-09 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8ab683f8-eeef-35cd-831b-beb5c95b2fa4 | -6.5592 | -62.89526 | 2026-09-09 05:29:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 1e7eed33-1dc5-3ac1-8c6f-519ae02b56dd | -3.96154 | -59.36612 | 2026-09-09 05:29:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f661e8e8-73da-3e50-a60a-403668083c47 | -4.49864 | -55.49129 | 2026-09-09 05:29:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 60827616-4912-303b-99a5-e3621f0ef515 | -3.36241 | -59.42922 | 2026-09-09 05:29:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 99d4d03b-2629-3215-b890-b9021a8d96ac | -3.66383 | -58.75533 | 2026-09-09 05:29:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 88559a26-fa55-30cb-b879-7bdfe717389d | -6.56197 | -62.89925 | 2026-09-09 05:29:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0aa9f864-eb9f-3716-a3c3-3c43fd6f2d27 | -4.09444 | -60.66275 | 2026-09-09 05:29:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fc63c70d-28fc-3bf7-98b4-003e29c8329c | -7.12134 | -56.51186 | 2026-09-09 05:29:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 67c37bd4-b612-31f1-81c8-1827819bd9a8 | -5.59387 | -60.24567 | 2026-09-09 05:29:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a1eddde6-677c-3b6a-889a-025f6df17586 | -4.20748 | -60.00042 | 2026-09-09 05:29:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fc3ffd3f-6e28-3a46-8ccf-9cbbc7f41939 | -7.17126 | -59.5481 | 2026-09-09 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 03e3abe0-5821-3e9b-b4af-0d58d905f78b | -6.55866 | -62.89874 | 2026-09-09 05:29:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 239fc0f6-3a3a-32bb-8342-1af9ee2dde94 | -3.18785 | -58.98327 | 2026-09-09 05:29:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| be708f49-a636-33f7-958b-17535370c00b | -6.55975 | -62.89178 | 2026-09-09 05:29:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 13f6dc0c-8fad-3248-b4e6-348c6acecd2d | -6.78726 | -58.93573 | 2026-09-09 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2856d3b5-58c8-3a2a-b12c-da6a2d68d5cb | -3.68206 | -58.52449 | 2026-09-09 05:29:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8935f456-c326-3fa0-846e-782a50a0b5e1 | -5.88327 | -55.71383 | 2026-09-09 05:29:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7df9c227-4508-3d50-a400-3623c160c45b | -3.42078 | -60.20689 | 2026-09-09 05:29:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1b057d1e-57c0-3807-97e7-3162d5caf02d | -4.24202 | -62.22732 | 2026-09-09 05:29:00 | NOAA-21 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 6b82ddcd-f12a-33f5-a0da-3124c2e2904d | -5.55521 | -60.24732 | 2026-09-09 05:29:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 34aa257e-3cd3-33e5-a01f-cb3cc1bf611b | -3.43832 | -59.25796 | 2026-09-09 05:29:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| cf285ec2-fbb5-38e8-ab10-18d7fcbf4e67 | -3.64501 | -59.55177 | 2026-09-09 05:29:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0e35d8dd-a330-3c42-bde7-a464364ecc57 | -6.92856 | -55.61975 | 2026-09-09 05:29:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d8a2b739-3c6e-3861-8de1-293deffed17e | -3.44197 | -61.07571 | 2026-09-09 05:29:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4bd8d578-1263-3bd8-a1cc-610881dc3bde | -3.51389 | -56.90128 | 2026-09-09 05:29:00 | NOAA-21 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b6c4d00f-1583-3b33-b392-27c5fb7c7cc3 | -5.5933 | -60.24937 | 2026-09-09 05:29:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2eb3e44f-6aab-3872-add2-638f6e0b06e7 | -3.90002 | -59.60535 | 2026-09-09 05:29:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a523fe93-5234-320e-b574-0237422f1448 | -3.15374 | -60.65407 | 2026-09-09 05:29:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 5f3ea992-eca0-38f4-a5f7-6bca4b45cd45 | -5.29071 | -60.12038 | 2026-09-09 05:29:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9e86f0ef-2e7d-3acd-b005-d3f8b02ea43a | -6.63631 | -59.44764 | 2026-09-09 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 94dfbac7-689a-36e8-b0d5-0a2208c303d0 | -5.36824 | -56.01593 | 2026-09-09 05:29:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 31241a61-c5a2-3f60-a8af-88d3b2e1629d | -5.28706 | -60.12032 | 2026-09-09 05:29:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 18fcecc7-bf1b-3137-ba3b-2aad02d57072 | -2.71372 | -59.76779 | 2026-09-09 05:29:00 | NOAA-21 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 509c6372-fb66-34ef-b09c-26b19a4088ce | -4.09779 | -60.66326 | 2026-09-09 05:29:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fee02031-4ac0-3a6e-b961-218c2426dd0b | -6.77285 | -58.95735 | 2026-09-09 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c6a1431f-53a3-30ef-98d6-90cdc9385be1 | -7.46246 | -59.85144 | 2026-09-09 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 64fb609a-ba6c-3375-9032-a04d553af78d | -3.13661 | -60.63369 | 2026-09-09 05:29:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ab952bc7-7bc6-3b89-901d-ce453b80d857 | -3.77277 | -58.84903 | 2026-09-09 05:29:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 30c7168a-f007-38c6-bbb3-a7f6517c4f84 | -3.68321 | -58.52784 | 2026-09-09 05:29:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c4314aab-71cb-3585-afcd-249de04b9176 | -6.24264 | -51.67715 | 2026-09-09 05:29:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 843c551a-1943-336f-94d5-1e8353744f29 | -6.76854 | -58.96112 | 2026-09-09 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b0b7a570-68b0-3f5b-b2b1-6ee0d9999d2e | -3.12565 | -57.68577 | 2026-09-09 05:29:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 87653249-2dcf-3a1f-9d05-f2ead8adfede | -3.15707 | -60.65459 | 2026-09-09 05:29:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 10.8 |
| ddc6cf12-2656-3911-ada2-313caee61920 | -3.35781 | -59.43623 | 2026-09-09 05:29:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 396a2728-7768-30f0-89ae-1d6d1293db44 | -3.95866 | -59.36176 | 2026-09-09 05:29:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b189bcbe-aa12-3bd8-9065-5e378b299d4f | -6.24909 | -51.67368 | 2026-09-09 05:29:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 646411e6-0a1b-3446-b66c-636113c5f48d | -6.10235 | -59.96819 | 2026-09-09 05:29:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5147bd1b-1441-3291-8c50-6a228a69800a | -3.82978 | -59.40105 | 2026-09-09 05:29:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7fc7007a-b604-376b-bc0f-669d4110056e | -8.27793 | -55.1102 | 2026-09-09 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7ba9c740-fef3-345d-93fc-2f7cff9e8afc | -3.2005 | -60.55015 | 2026-09-09 05:29:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f6b5b41f-898b-3f0f-b4f5-dee6dfc5b6eb | -3.96272 | -59.35844 | 2026-09-09 05:29:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b80ca9d6-0463-3546-a1b1-854f73f5adef | -3.77632 | -58.84957 | 2026-09-09 05:29:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ea3385c2-65c6-3ba6-8c99-2931725b8cb1 | -3.19621 | -61.23495 | 2026-09-09 05:29:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e8c39b66-e766-315d-8e92-237ef63980cc | -5.36393 | -56.01531 | 2026-09-09 05:29:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 821027ce-ed8d-3456-b806-dd0e02db3524 | -3.38302 | -61.32431 | 2026-09-09 05:29:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 027116a6-54a7-3f6a-b829-16e87ea8c22f | -6.75522 | -58.95036 | 2026-09-09 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9b8dd6be-fdcb-3e94-b7d0-a5d85f25e57d | -3.83266 | -59.40539 | 2026-09-09 05:29:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| de51bd11-a1cf-33f9-9c6c-1b169a7b96d4 | -6.24966 | -51.66949 | 2026-09-09 05:29:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c8bee97c-d8cb-3f88-9604-db7ca55fdd3c | -6.83983 | -51.49208 | 2026-09-09 05:29:00 | NOAA-21 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 750a7b14-d04f-3797-94a9-06e1767ad712 | -3.89658 | -59.60482 | 2026-09-09 05:29:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b038098a-8b8f-30c2-807c-b1efc93b94a0 | -5.3708 | -56.02889 | 2026-09-09 05:29:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f6fafeea-2788-3eeb-80e1-a4c5bfe78552 | -5.88389 | -55.70953 | 2026-09-09 05:29:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5c7e95ef-7dd1-32b9-aea1-613ffab5b01c | -5.47963 | -60.23624 | 2026-09-09 05:29:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7abc3a31-d194-3895-996c-2dbd77e22dc7 | -3.89314 | -59.60428 | 2026-09-09 05:29:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 15806550-0a0f-3d30-8ffd-2d0f9aa8454e | -6.77314 | -58.95559 | 2026-09-09 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README26.md)

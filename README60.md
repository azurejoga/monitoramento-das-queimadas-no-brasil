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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 694aa595-7bb0-358e-90ea-ed3528272f98 | -3.95803 | -48.15667 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2176c92a-637d-32f5-a76f-65e5542fa28f | -3.4266 | -49.24292 | 2024-11-09 04:33:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b8d526e7-6f68-3d92-b29f-1d1872117e4d | -5.44991 | -43.26505 | 2024-11-09 04:33:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| ad45a69c-bcea-3574-84b4-c36587a333ec | -3.0284 | -51.09499 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ef2816d4-5096-32a8-83d2-eae0e3f5d1bc | -4.81463 | -50.59842 | 2024-11-09 04:33:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 72f717a6-d448-35c1-87f9-bf88a6cebc41 | -3.22871 | -50.44715 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9a127a43-3bcf-307a-a31a-7d68c2c4872e | -3.0672 | -48.06659 | 2024-11-09 04:33:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 237b3d5b-a7bc-3e2e-8270-b89937e9214a | -5.49629 | -46.31015 | 2024-11-09 04:33:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6a802e65-5c37-3700-8440-098edb8c7197 | -3.53634 | -51.10188 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 59867a08-09a9-3c88-9f7c-c7188959311a | -3.32707 | -49.09586 | 2024-11-09 04:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0963ba51-0233-35b0-8fd6-c13412db1422 | -4.13097 | -43.59105 | 2024-11-09 04:33:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4aa49d46-5ca1-36ff-bf84-883394cb9d32 | -3.95194 | -48.15218 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fac9cb76-109c-3012-bcdb-e6031636c722 | -4.07121 | -47.21484 | 2024-11-09 04:33:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0652b584-a6e2-3e58-a4a7-314d3c70804d | -2.88836 | -51.74932 | 2024-11-09 04:33:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cf581985-eb03-33d1-9c1d-ae35d18842d0 | -3.94862 | -48.15167 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a8386323-aa71-3905-8406-b72716520da8 | -4.20677 | -45.86005 | 2024-11-09 04:33:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 52.5 |
| a36c399e-914c-3835-b237-26023bf01ca6 | -3.98927 | -49.2811 | 2024-11-09 04:33:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 88db872a-209e-338e-92f1-f80f9ef383d5 | -3.95031 | -48.1626 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 2d72d2a5-6b08-312a-a117-d6d17dd75bfb | -3.27717 | -51.06579 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 205485dd-38c3-3b35-b212-3b5ad6e59fd0 | -3.12397 | -50.14687 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f71cd8f5-bc2d-33f5-b1e2-3efbc802540d | -4.51588 | -45.67865 | 2024-11-09 04:33:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f3767a99-fd1e-3307-9b80-aab7486f4172 | -3.19994 | -46.49551 | 2024-11-09 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 50fdb2c2-e8a4-3b20-9d6a-f6661f91fb29 | -4.12391 | -46.91955 | 2024-11-09 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e65f1973-47d5-3fed-acfe-7b72e668c012 | -2.65616 | -49.87284 | 2024-11-09 04:33:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 14260f37-040a-3d1b-92eb-c4ffa6683169 | -4.37926 | -47.22448 | 2024-11-09 04:33:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8cd69ae0-aca7-36b1-b3e3-8ee6ba04bbb6 | -4.11614 | -46.90416 | 2024-11-09 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7e8e9fc4-8507-349c-bbe4-2154b21a4a33 | -3.07561 | -51.35862 | 2024-11-09 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4d45c8f3-8fc1-3361-a6d8-17199c8d2d70 | -3.33707 | -50.08482 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 052b2891-fe3b-38fe-a4ca-f57054e2ca54 | -3.35281 | -50.25921 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 93bddc65-2675-324f-965f-7bddb76b0124 | -3.58819 | -47.34693 | 2024-11-09 04:33:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 21.9 |
| 72f56387-5abe-37b1-a19c-fc1804d36ff8 | -2.07965 | -54.69176 | 2024-11-09 04:33:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 7e61b803-f0b2-3b23-90df-b1d6cabc93a4 | -4.23824 | -47.56159 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0f90aee6-db81-3abd-b713-6640c459b68c | -5.31628 | -50.7033 | 2024-11-09 04:33:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5b99ff48-ac8b-3a19-ba61-cf708a9d3b58 | -4.32157 | -45.6187 | 2024-11-09 04:33:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f4c830a5-a45f-3015-a8dc-20a333ce815c | -5.58042 | -43.14437 | 2024-11-09 04:33:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 7a979170-5bc3-34b8-b319-b6c01c3006f0 | -3.40813 | -47.58576 | 2024-11-09 04:33:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c9ead124-27ee-3a6f-803d-30e74273acff | -3.85098 | -46.61796 | 2024-11-09 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1e99f9e9-6305-36b1-bd1e-dada95b51c5e | -3.52865 | -50.87278 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| c5052867-d004-3848-85f3-dbb9a5260ca5 | -3.03309 | -51.52552 | 2024-11-09 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4d616533-bc9c-3c6a-b299-624671013655 | -7.6321 | -43.53824 | 2024-11-09 04:33:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 61ca39e3-ed56-302c-abba-9ea1a66f8dff | -4.25225 | -48.53553 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| ed4543aa-d8aa-3c15-bd36-99781ae50754 | -5.08981 | -46.54744 | 2024-11-09 04:33:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c49aeb06-2477-3fed-a1de-3d969e8b6f12 | -4.21812 | -48.53759 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6e449559-c693-3528-9c03-e9e9da928230 | -2.93893 | -49.52985 | 2024-11-09 04:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a78015da-f2ee-3376-a4b6-f7845531b99b | -3.07551 | -49.53471 | 2024-11-09 04:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cb2f804d-ba05-37c3-85b2-dda74bad4020 | -3.23854 | -51.18889 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 53de8fe1-a3f5-3d8b-b0a7-559fe40d87b8 | -2.90603 | -51.46919 | 2024-11-09 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 791a0821-ee40-3248-b3c3-ddb35253561c | -3.03456 | -50.30002 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4578df87-c239-31a1-9f06-b80d709edd72 | -3.87949 | -46.65423 | 2024-11-09 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5f5db12b-a4db-32b1-9b31-4325bcd7f047 | -4.87226 | -45.77748 | 2024-11-09 04:33:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 979e6bc8-c697-39cb-8a25-d680516dee1d | -4.22844 | -50.64181 | 2024-11-09 04:33:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bdd6fa05-ff6f-3a17-ab24-d8537a48cb3f | -2.86944 | -50.33031 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 39b57583-0f1a-36a4-907c-be1b1be4c746 | -3.21995 | -50.38637 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 25c1784c-0eff-3cb9-9cd9-18fbeeb65f1a | -6.16023 | -43.59023 | 2024-11-09 04:33:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fb2e97b5-a356-38e0-8ead-913ebcd814cd | -2.92736 | -49.35732 | 2024-11-09 04:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c539678a-f4a0-380e-b1ab-ad84416aa63a | -3.1075 | -51.35412 | 2024-11-09 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 30761922-0bec-3094-8e45-4dd4910ae06c | -3.02562 | -48.02808 | 2024-11-09 04:33:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 14650cce-1ce2-3341-8323-6dd477d4bcd0 | -3.2832 | -51.51723 | 2024-11-09 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5565b56f-5872-3546-a532-13e087c5a160 | -5.74758 | -41.98888 | 2024-11-09 04:33:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 3a9f4fd5-592f-31a3-b79a-2225e338ad39 | -4.64608 | -46.02261 | 2024-11-09 04:33:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 802ced09-7b3f-3371-a38a-d1ffdc131f4f | -10.21286 | -36.24587 | 2024-11-09 04:33:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 24.8 |
| 26753ff6-f03e-31b5-94d5-57b58085a584 | -2.88465 | -48.29628 | 2024-11-09 04:33:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| a83c3bf5-f4d2-367d-86b0-ed2aa0c925d4 | -3.58629 | -50.22815 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 94a54e5e-f3af-3368-9ac4-b3753eea3425 | -3.73071 | -53.4041 | 2024-11-09 04:33:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 91eddede-847e-3772-9d7f-6662a393491f | -3.11736 | -53.11995 | 2024-11-09 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4732debd-c42b-33cf-90ed-13412da5b8a2 | -5.79113 | -45.9632 | 2024-11-09 04:33:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ed0baf6f-f337-35e3-be35-38ac91daf1a2 | -4.33538 | -45.89767 | 2024-11-09 04:33:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0574c045-ac0c-3b05-9763-6d52852c8eb0 | -3.17905 | -50.38845 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4ca34641-d111-3f2a-8ece-4eeb11bd7f19 | -3.05491 | -48.01481 | 2024-11-09 04:33:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| da56c8d0-fe27-39ae-93bd-06fed81b469c | -4.82648 | -47.32254 | 2024-11-09 04:33:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e47f1f13-ff8c-34e6-bdb8-dad05a8339a5 | -2.77987 | -52.87454 | 2024-11-09 04:33:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 664bbbef-dc50-37b3-8e94-07c57a264e77 | -3.97573 | -48.1311 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e23bd7cc-4fff-3c10-a011-7ef75969e11f | -3.20164 | -46.50645 | 2024-11-09 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3da9fa4f-9f2a-3c03-b49b-b57c55f004c3 | -5.07715 | -47.93989 | 2024-11-09 04:33:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 387c04bf-d896-36f5-8065-a872f21a84ad | -2.93666 | -49.43218 | 2024-11-09 04:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4141c342-f231-324c-9bce-ccf0bdbe46be | -4.41494 | -45.94309 | 2024-11-09 04:33:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 51038ba5-7c02-3a7b-a700-15342ba77508 | -7.63462 | -43.54881 | 2024-11-09 04:33:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b806e6ba-ef46-3688-9917-4fee37d0c841 | -3.97303 | -48.16978 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5fe628ef-e7ca-3b5f-9ea2-192512233a10 | -3.35574 | -50.26382 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 253330cd-b3d7-3743-b209-0b07a6cb76f0 | -2.43414 | -53.66356 | 2024-11-09 04:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 930901e4-34c6-398f-a368-30b4054d65cd | -5.20354 | -44.92057 | 2024-11-09 04:33:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f50bc4d9-276c-3b9b-b0b0-87f6f2b136ea | -4.59421 | -48.48165 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 239848e5-bfdd-3467-8425-28d3b23dcc1a | -5.24829 | -45.95716 | 2024-11-09 04:33:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3b8f6942-f668-3180-8f88-4b7fad17edfb | -4.25537 | -47.58183 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 38.3 |
| 750c4e8f-76b4-3b62-ab7a-78ee06fd6de8 | -9.12958 | -43.18028 | 2024-11-09 04:33:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 17cda6e7-7c30-34a5-a6d1-3df894009f1b | -3.26243 | -46.31247 | 2024-11-09 04:33:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 48a4dc7d-fc6e-3e5c-a414-caac99a1c1c2 | -2.84775 | -51.77497 | 2024-11-09 04:33:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 416ff742-a301-3c9b-9b74-5d6f45aa6650 | -3.25236 | -46.46445 | 2024-11-09 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bbe0c371-bcb2-34b5-be14-246cfcca75fb | -4.16457 | -48.24987 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 93832153-3ca7-363e-8ad5-bf5b4ca56760 | -4.24472 | -48.02106 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| db9625e0-f218-3dd1-9e05-aa08e8866c31 | -4.11447 | -46.10018 | 2024-11-09 04:33:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fabc109b-545d-3a0c-8e2b-c6779fe84bee | -3.08101 | -49.59032 | 2024-11-09 04:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f75f7e76-98f6-3222-b9be-29eb4b51a988 | -3.12789 | -51.10406 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eda23beb-76d3-35cc-ade1-52d22d563537 | -4.21702 | -48.5446 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 71728318-0bcb-36f6-9ae6-7b28321e03fa | -3.96358 | -48.16465 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 20a993f5-bcd3-3233-a334-b3ddfaa6b6f8 | -3.24529 | -50.72041 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bcea8b04-6901-38c5-bc56-9bbb7a7d78ea | -3.96196 | -48.17505 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 9b2328f3-89d6-3737-ae33-85bbdace397a | -4.38995 | -46.80484 | 2024-11-09 04:33:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3a6f778d-b46e-332b-ae07-e7d4d34a476c | -2.84327 | -51.35461 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 73cc819c-c25f-3abe-8b5f-12179b20d704 | -2.72814 | -51.71853 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |


[Clique aqui para ver as próximas entradas](README61.md)

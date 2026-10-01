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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 46a5ef07-9d52-3879-8fb2-0ca8f31471b1 | -3.56621 | -51.48173 | 2026-10-01 04:32:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| d539e113-8163-3881-ae3a-7f284bc1c14b | -5.42665 | -43.44894 | 2026-10-01 04:32:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 89f4844e-7a5d-3ec6-93fe-04b58f4dca74 | -4.12547 | -46.87451 | 2026-10-01 04:32:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2e6255ed-c69c-3203-ae78-bf26330c6b7e | -5.75781 | -45.16449 | 2026-10-01 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3a906bef-01ce-35e8-ba20-9b8a0e32e1ce | -5.24551 | -46.77407 | 2026-10-01 04:32:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 288b393f-1487-304c-bdb3-7bf329623260 | -4.26048 | -50.74783 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 219616f1-9253-3221-8e0e-3518e488d05c | -2.49433 | -56.91468 | 2026-10-01 04:32:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 74782c55-b23c-358c-ba4e-9d55d20c2152 | -4.25669 | -50.78575 | 2026-10-01 04:32:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a78429ca-69eb-3748-a4fa-0a117b7ea896 | -3.16388 | -54.08739 | 2026-10-01 04:32:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| cc24f665-2c4c-32c8-a9f3-a867688a9021 | -3.12156 | -50.28687 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 315013a9-7de2-39b0-8d7f-73f304f06837 | -3.01902 | -53.88221 | 2026-10-01 04:32:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bbf7a577-e66e-3768-989c-7113250cc25b | -4.02396 | -54.19848 | 2026-10-01 04:32:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bca7fbbd-a2cd-3958-b161-e9b1a29e9485 | -1.20479 | -49.28566 | 2026-10-01 04:32:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d54eddb0-9a01-3877-99b2-a462dcd97c6e | -4.25528 | -50.76987 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| e8cd4690-47da-32bb-8b4f-4c12e16de4d5 | -2.27393 | -48.75262 | 2026-10-01 04:32:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 882b2eab-554a-3cb6-b392-9ce962089d4c | -2.89817 | -54.14669 | 2026-10-01 04:32:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 70348799-bdba-31ae-8b68-a1119d45c013 | -3.37736 | -50.95075 | 2026-10-01 04:32:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 521d6ba7-d1e8-3001-be42-8871474bcc32 | -3.11061 | -50.28005 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d82fa9e6-1e7e-379d-8428-faeb43a85c96 | -4.27087 | -50.73377 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6b02918f-aea8-3ce8-bf31-d85b6a6ba439 | -3.56985 | -54.32899 | 2026-10-01 04:32:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 26bc1301-714d-33a4-9376-acbf10f7ad30 | -4.0438 | -54.23375 | 2026-10-01 04:32:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d47c915b-56dd-329d-a69f-499ea7b5b07b | -4.28621 | -50.78001 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 243.8 |
| 2595a024-9f94-32bb-a903-3b1ead786380 | -3.10822 | -50.29487 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5d82d3c6-925e-34d8-8ab8-3899a98e3218 | -2.98178 | -51.02568 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 524e64a6-7891-31c1-a8bd-9c81c067da81 | -4.30544 | -50.7623 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 6fd0a55e-1982-365a-a509-9dd4d9a74323 | -4.04137 | -48.99218 | 2026-10-01 04:32:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4cf5e8c1-cdc1-3175-ad4c-b78fa764e4df | -4.06563 | -51.10289 | 2026-10-01 04:32:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4c0d8cbc-ce53-3362-b08b-5d2b4db66544 | -3.15068 | -54.08047 | 2026-10-01 04:32:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2088095e-964a-3ff8-91be-3686e9a55e9c | -0.39455 | -51.85172 | 2026-10-01 04:32:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 56a4a626-2bcd-34f1-b566-42c68f4b41ec | -4.27966 | -50.79483 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 129e2191-51a8-3f09-b562-772f6a799b39 | -3.17756 | -54.0987 | 2026-10-01 04:32:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| d6dc4bc4-2bee-3b6d-b42b-6da9b2695d93 | -5.1207 | -56.00784 | 2026-10-01 04:32:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 79743428-f74d-3462-98f8-772937b3f122 | -3.87551 | -50.66329 | 2026-10-01 04:32:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4e27b8c9-070a-3be9-ba7b-1d54498b4925 | -3.37676 | -50.95436 | 2026-10-01 04:32:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bc843d28-21a6-3a9c-93ae-35e32b76dbff | -2.26922 | -47.8762 | 2026-10-01 04:32:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 91ed667d-4238-36e2-a536-571540b47e21 | -4.2743 | -50.77803 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 154.5 |
| 7b880e7f-7704-3b24-afb7-b26297c50406 | -4.37391 | -49.73255 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c2d8a553-5712-3eaa-a4c4-ac99e577beb1 | -2.97235 | -51.0317 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 09cf0ac3-d126-3529-9b61-4156fed7305a | -5.57921 | -42.72944 | 2026-10-01 04:32:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 46dfdab1-0000-3fa0-807d-05160dc14866 | -4.28478 | -50.76411 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 4e116654-9e42-3d7a-b441-f674dbf4cbe3 | -3.3745 | -50.94281 | 2026-10-01 04:32:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 289beabd-d7d0-3c4c-be5c-0d425175f4da | -4.29329 | -50.78647 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 30.6 |
| 156605c4-12b9-32e8-9131-884583fdb593 | -6.28129 | -44.14103 | 2026-10-01 04:32:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a0766d58-9636-30c2-926c-659029ecb3e3 | -3.97442 | -51.9193 | 2026-10-01 04:32:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d603b8b0-cf22-3cbb-afb4-c55842621c16 | -5.44861 | -44.53936 | 2026-10-01 04:32:00 | NOAA-20 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| dd67112f-cc5d-30c3-8a8f-3fb05237893d | 1.84481 | -55.56177 | 2026-10-01 04:32:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6e35824f-8622-3250-996b-d9eb06dd3b3c | -5.75947 | -45.15387 | 2026-10-01 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| f394535c-2e31-31a4-98bd-307cec3fda5b | -4.25815 | -50.73705 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 26b54e94-3bd3-37de-a638-4d918db96041 | -5.33726 | -46.19724 | 2026-10-01 04:32:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e8949bc4-fc81-3fa6-896c-89dbc134c46e | -3.18519 | -48.01944 | 2026-10-01 04:32:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 64cf99e2-d65c-32b3-9935-a3f3d17c791c | -4.26199 | -50.76377 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 84f0a2e1-bf31-3e90-a280-0c630b2a3aef | -4.2684 | -50.7492 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| f141f062-4553-38ff-832a-df4aa20b9a26 | -3.98241 | -56.08682 | 2026-10-01 04:32:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3c38c4f5-868e-3545-97ab-282b558d9201 | -4.31712 | -50.79034 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6811aa2b-6f31-3787-bd79-dbbd8ad53b6a | -5.32444 | -47.47362 | 2026-10-01 04:32:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 082ab9b3-8dc4-3126-9674-d74e46feb525 | -4.30039 | -50.79291 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f91ce910-4bdc-34e8-a3fe-64359d17ea79 | -4.25304 | -50.75896 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 39.6 |
| 47fe4bca-217c-3326-9adb-940431213506 | -5.29761 | -55.87412 | 2026-10-01 04:32:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a3d757ab-cd88-3102-94b1-72877333dd5d | -3.59527 | -54.5543 | 2026-10-01 04:32:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 39f5c6d9-7ac1-3793-a631-03bf4976d6ea | -4.63594 | -50.61169 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f117f87d-ee9c-3a8e-8532-141d776d5d83 | -4.29043 | -50.75457 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5b1f472f-f30c-3eff-8191-925448fa2a0d | -3.00256 | -54.23117 | 2026-10-01 04:32:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 31c1c1d2-0416-381a-8aeb-ec56238add94 | -3.00768 | -54.232 | 2026-10-01 04:32:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 651fbb79-a675-3a7c-9685-8ffafb5f32da | 1.79459 | -55.64811 | 2026-10-01 04:32:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f3ec44ff-e7b2-3680-8fa1-aa5d928ff9d3 | -5.12636 | -48.80263 | 2026-10-01 04:32:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 68fbe5a3-c12a-3178-a845-94a91a1ac5d2 | -4.27715 | -50.7366 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| eabd9232-ece7-33cf-87e8-c934f7efa76c | -4.25478 | -50.74866 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 2c1a0efa-5d57-3f09-824a-d712bfd06d93 | -4.25089 | -50.7568 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 91249dbd-c544-32b1-bdf8-6792042226a1 | -2.96411 | -51.03037 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 27912c7e-c9a1-33f1-95b5-f328b368c96b | -4.25256 | -50.74649 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 90cb6d07-918e-3b6f-9da8-a092904bb109 | -4.29724 | -54.80064 | 2026-10-01 04:32:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c1b89cc4-6589-3331-aa32-23bfe05966a5 | -2.99646 | -51.03942 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0dc69fdd-749c-329e-bd32-80e00848ba92 | -5.80989 | -46.21548 | 2026-10-01 04:32:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9ba5930f-d547-38e7-b765-07a42ae5e353 | -4.25006 | -50.76194 | 2026-10-01 04:32:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 8ddd30b9-9237-3be7-91b6-58a648420165 | -6.01322 | -49.56051 | 2026-10-01 04:32:00 | NOAA-20 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| df87e5ea-bcb7-3805-84da-15e2f0d0303f | -4.27319 | -50.7447 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| a574fd91-fbcd-3801-9b15-d1a49363d199 | -4.16181 | -48.89708 | 2026-10-01 04:32:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 84ac1784-c5a2-3f58-882f-dd9457cca5ae | -3.02813 | -51.27591 | 2026-10-01 04:32:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 04b28d2c-4681-393a-8450-f32d7c34bced | -2.97587 | -51.03605 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 80c28acf-3fd7-3253-8c72-450b1ef87bf6 | -6.72167 | -45.99064 | 2026-10-01 04:32:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a059261d-c00b-36ab-b06f-100172649c56 | -4.38973 | -54.8281 | 2026-10-01 04:32:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 70bbf9f3-4db6-3a7f-9f53-34246af7d887 | -6.00961 | -49.55989 | 2026-10-01 04:32:00 | NOAA-20 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 29.9 |
| 870d730b-0add-3082-b151-ebf121b62195 | -4.25217 | -50.7641 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 8b7c2f36-8d67-31cd-aa7d-a2c9aa0207b9 | -3.68702 | -47.12776 | 2026-10-01 04:32:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 281fca76-2f41-30e3-8528-c4568e7a6447 | -6.18888 | -44.85283 | 2026-10-01 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 33720475-a10b-383e-a433-b992a32b442d | -3.16188 | -54.09907 | 2026-10-01 04:32:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 55356e60-af7d-3d54-b1b8-eee2d30a0e11 | -6.82446 | -45.17951 | 2026-10-01 04:32:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 926beabf-644d-3be8-8d0b-1923efd17b03 | -3.00406 | -51.07107 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 13b390dd-71cf-3792-aaf0-c7c8bb773a74 | -3.00818 | -54.22899 | 2026-10-01 04:32:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7c709267-6b89-386d-97fb-e2ead8799c94 | -4.0398 | -54.22679 | 2026-10-01 04:32:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1e6b5249-4f8f-3a87-8739-09d3ba214c38 | -3.87414 | -51.97615 | 2026-10-01 04:32:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6141fb2b-e5c3-3ec1-96ef-19caea17c589 | -3.00525 | -51.06367 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5c1b56f5-e477-36f0-b8f8-791af3467fba | -2.99705 | -51.03573 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f54b1d16-dc36-37cf-a64f-762a20aab9ce | -3.1083 | -50.26951 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 265f18cd-712b-3804-bf62-783d8c0cd681 | -1.81361 | -57.10363 | 2026-10-01 04:32:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 02aa5f56-2149-3924-beee-a424ac08de2e | -1.08009 | -54.1059 | 2026-10-01 04:32:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0a98139e-edb1-347e-b357-1a24d6fb3938 | -3.1562 | -54.0785 | 2026-10-01 04:32:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2fafcf8b-7162-3bd2-a48a-923d0ab63d85 | -5.10202 | -45.66406 | 2026-10-01 04:32:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 77ba1529-ef8c-3a89-8cc0-ea893b2f5d2e | -3.63113 | -54.50721 | 2026-10-01 04:32:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dcb68f02-8bae-3759-8cc0-b2dc29864b3e | -4.27147 | -50.74627 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |


[Clique aqui para ver as próximas entradas](README46.md)

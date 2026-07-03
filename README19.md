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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b343b6a7-8408-33f1-a868-6ede2d5ec229 | -19.50902 | -52.73796 | 2026-07-03 05:44:00 | NPP-375D | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 650072f6-b4aa-38b7-9a02-615bee2b7274 | -12.7553 | -44.5194 | 2026-07-03 05:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 129.3 |
| 68b92e6b-74ca-3a07-93bf-73c952559dbe | -10.9397 | -43.0593 | 2026-07-03 05:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 22f32a53-4453-3ea0-ac4a-bd49111ccadc | -12.7557 | -44.4959 | 2026-07-03 05:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 44.4 |
| eea00b62-85a6-3a8d-9292-bb07f1f6a250 | -10.9593 | -43.0326 | 2026-07-03 05:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 8b5c491a-f5b8-39ba-be33-3f2d773d4236 | -5.7945 | -45.0586 | 2026-07-03 05:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 55.7 |
| f677bf1e-fa32-3b64-ac5e-efb34e70c7cd | -10.9588 | -43.0565 | 2026-07-03 05:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 69.4 |
| c45744b9-dead-3b86-b2d5-d29aa3f883c0 | -10.9401 | -43.0355 | 2026-07-03 05:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 4c24f790-9c86-3454-b1ba-e316a552516e | -9.79136 | -65.54051 | 2026-07-03 05:59:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b6d9d5f1-c0e6-37c4-8564-ffcd14f15540 | -9.0742 | -65.42121 | 2026-07-03 05:59:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9ec90939-fdb4-392b-a914-d7e7e01f945a | -11.62518 | -59.01957 | 2026-07-03 05:59:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bef6c67f-0417-372e-b361-ad1df4eaac42 | -9.02437 | -59.53473 | 2026-07-03 05:59:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2c1a78a0-687d-3a43-ab34-066b4d5988f1 | -11.6321 | -59.01176 | 2026-07-03 05:59:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4f793ec8-0d67-3086-a281-20a72dd27180 | -10.90021 | -56.85297 | 2026-07-03 05:59:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a3207126-3886-30cf-b8ef-24b946c5ba6f | -11.41097 | -56.06028 | 2026-07-03 05:59:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 09eaff5d-4843-3396-ba99-309fe0ea0fb4 | -11.41798 | -56.06134 | 2026-07-03 05:59:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 130014b7-7299-38ff-9548-167727c9f904 | -9.07792 | -65.42177 | 2026-07-03 05:59:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 103e13b9-2134-38bc-8ee9-0c2207f2b035 | -11.63108 | -59.02024 | 2026-07-03 05:59:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9055de54-da3a-33ff-bf7e-6bfc7a5c24d0 | -12.43023 | -58.41811 | 2026-07-03 05:59:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4fc913c8-8976-30d8-8a92-482d4132ecff | -10.89954 | -56.85884 | 2026-07-03 05:59:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fe27f88e-1849-379a-ae1e-4324cd2dc2ff | -12.43078 | -58.41322 | 2026-07-03 05:59:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1c7ccac8-7539-3442-903a-8c3eb64d4e47 | -9.02342 | -59.542 | 2026-07-03 05:59:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3497958e-8915-30a1-aa3e-1e345638ed85 | -11.41721 | -56.06794 | 2026-07-03 05:59:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 92ea2e35-31cb-3505-abd9-031280c3b9ec | -11.63159 | -59.01604 | 2026-07-03 05:59:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9fe8f14e-836e-32e1-9d50-af3c482e5c64 | -11.41542 | -56.06391 | 2026-07-03 05:59:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 68d6d97f-98fa-312c-bf0f-2e988d5d624d | -9.23499 | -65.74765 | 2026-07-03 05:59:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 881f03e4-18ee-3124-80f7-79a4a9111efc | -9.36267 | -65.74278 | 2026-07-03 05:59:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e0336bcf-8309-3cc6-a8e6-85a2a3af14ed | -11.79327 | -57.00194 | 2026-07-03 05:59:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 323cc343-ebd7-3782-8ab4-06845cd5326d | -9.64466 | -67.49123 | 2026-07-03 05:59:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e1b99ed3-b6ec-3217-9952-2841a534625f | -9.37647 | -65.77602 | 2026-07-03 05:59:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e5e096c4-4c8b-358e-a213-371387d9965b | -11.41615 | -56.05726 | 2026-07-03 05:59:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 80bf332d-042f-3348-aa20-032e4a4e299d | -11.62568 | -59.01531 | 2026-07-03 05:59:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f12050ba-9a98-393c-846b-0b6a189f2ed2 | -10.9397 | -43.0593 | 2026-07-03 06:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 123.7 |
| 0fe6cf09-e8c3-3aba-9d2e-d44cece3229c | -5.7945 | -45.0586 | 2026-07-03 06:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 49.0 |
| ac04758e-a8ee-3e9f-b752-4c2e555301b0 | -12.7553 | -44.5194 | 2026-07-03 06:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 131.9 |
| 6faf10c3-a928-30a6-bbfd-ee24d1ecf953 | -10.9401 | -43.0355 | 2026-07-03 06:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 89.9 |
| e8388f7f-90a6-3dab-9420-e3d2214af95e | -5.7945 | -45.0586 | 2026-07-03 06:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 51.2 |
| a05b1a3a-19f0-33a7-a226-f9399493a4a4 | -12.7553 | -44.5194 | 2026-07-03 06:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 116.7 |
| 85a1ddac-a6e6-39df-b579-b68a7c7e1dae | -10.9397 | -43.0593 | 2026-07-03 06:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 110.4 |
| 8ba9dcdf-da75-3abb-8989-6fe1a00289be | -10.9401 | -43.0355 | 2026-07-03 06:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 54e57790-ee72-3a5c-b0ea-2c833e6e3870 | -5.7945 | -45.0586 | 2026-07-03 06:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 59.7 |
| a616b011-4fdb-3760-8dab-26c9f91e08f8 | -10.9397 | -43.0593 | 2026-07-03 06:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 84.5 |
| c0ea8376-5cd3-3e38-b72c-56541ca4609f | -12.7553 | -44.5194 | 2026-07-03 06:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 648510cc-6fd0-3435-9069-363abeee1f28 | -10.9401 | -43.0355 | 2026-07-03 06:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 71.1 |
| b9a0c75e-0caf-38f3-ac6d-b5ca37b79563 | -10.9397 | -43.0593 | 2026-07-03 06:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 6e0b5c4c-3cb0-3286-9361-bf18915b09da | -5.7945 | -45.0586 | 2026-07-03 06:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 53.0 |
| e20b0b1d-d3e1-34eb-aedd-58bdba6be810 | -12.7553 | -44.5194 | 2026-07-03 06:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 8e1e5f7c-542b-32a7-9069-225b50febe79 | -10.9588 | -43.0565 | 2026-07-03 06:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 78864014-1cd5-31a7-a188-3577248eeeb1 | -10.9401 | -43.0355 | 2026-07-03 06:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 9911ac2a-c95f-3cf6-b8c5-9291b1272375 | -10.9401 | -43.0355 | 2026-07-03 06:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 53.1 |
| c717e983-af94-398e-9af4-96ebd6db55cb | -12.7553 | -44.5194 | 2026-07-03 06:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 3ae155cf-ca49-3978-bc9d-3d69143d3ce5 | -10.9397 | -43.0593 | 2026-07-03 06:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 04f3b396-cb99-39e8-a087-4f4cde753d3c | -5.7945 | -45.0586 | 2026-07-03 06:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 73f25ba6-f1d5-3ec4-8a4e-7796f3bb6bda | -12.7553 | -44.5194 | 2026-07-03 06:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 1693427e-4da2-3ac8-8b44-08ff93fea35f | -5.7945 | -45.0586 | 2026-07-03 06:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 47.8 |
| e4eaa1fd-dd5b-30f7-b6c4-624d4c90c20f | -10.9397 | -43.0593 | 2026-07-03 06:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 7a0c3f40-9007-3798-b4a2-70ff25f2d576 | -10.9401 | -43.0355 | 2026-07-03 06:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 60.3 |
| de82ffc1-1f99-3604-be6c-cce0adf1f9b8 | -5.7945 | -45.0586 | 2026-07-03 07:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 49.8 |
| c750d840-6a39-31f8-a350-ec3be13360c5 | -10.9401 | -43.0355 | 2026-07-03 07:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 55.2 |
| 30dc64f0-8a0e-35c4-8430-560f23f4f780 | -12.7553 | -44.5194 | 2026-07-03 07:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 1dfff06b-860c-361e-b629-7f174ff7db53 | -10.9397 | -43.0593 | 2026-07-03 07:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 50.0 |
| 42b1f3eb-c126-3b85-accd-ca2e20970ac4 | -4.01072 | -48.06039 | 2026-07-03 07:05:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 24.2 |
| cc8880a5-7c88-31c2-b992-0ed6797cec56 | -4.01089 | -48.05515 | 2026-07-03 07:05:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 24.1 |
| 244cff0e-55da-3445-88bd-f5b167da9675 | -5.79628 | -45.07045 | 2026-07-03 07:07:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 58.1 |
| f10ac3c1-6326-3c4a-9dab-6a0442602be2 | -11.4148 | -56.0523 | 2026-07-03 07:07:00 | AQUA_M-M | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 60d1b91c-48a5-33ea-9cac-08686a243b95 | -5.80121 | -45.03254 | 2026-07-03 07:07:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 18d06b84-4efe-3eba-a538-dafa7c18d131 | -5.79247 | -45.06203 | 2026-07-03 07:07:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 51c41c47-1f3c-35ba-9ee1-8152ec7061c5 | -11.63802 | -59.00839 | 2026-07-03 07:09:00 | AQUA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 3566b1a1-a2d1-3a85-8d4c-cf6c9dd821b0 | -5.7945 | -45.0586 | 2026-07-03 07:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 57.2 |
| 53e1c0cb-d4ef-39f3-b7c8-e74230937658 | -12.7553 | -44.5194 | 2026-07-03 07:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 48.3 |
| 04af7539-97db-3818-8042-b2fd7a92b6cf | -12.7553 | -44.5194 | 2026-07-03 07:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 54.8 |
| 7e1b2f17-2be2-3293-af84-3f1be8acad97 | -5.7945 | -45.0586 | 2026-07-03 07:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 40104400-35ce-3020-8768-41c2a5da5fcd | -12.7553 | -44.5194 | 2026-07-03 07:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 48.2 |
| 2c5ba336-bf95-36c5-8273-83edb0354664 | -10.9397 | -43.0593 | 2026-07-03 07:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 216e4add-e8b6-395e-9165-f7755e274f05 | -10.9401 | -43.0355 | 2026-07-03 07:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 58.3 |
| dd92f4a2-3b38-3305-a4c6-240a042a3732 | -5.7945 | -45.0586 | 2026-07-03 07:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 54.5 |
| a8e66b3b-bebc-3821-ae53-5f6fc36b9832 | -5.7945 | -45.0586 | 2026-07-03 07:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 407e3a5c-24b3-356a-bce9-0efc4ca1f92b | -12.7553 | -44.5194 | 2026-07-03 08:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 44.9 |
| 7b9e94d8-d2ab-31b4-90d6-554331eaebb3 | -10.9397 | -43.0593 | 2026-07-03 08:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 52.5 |
| bed3560d-9263-3041-85dc-09753be14152 | -5.7945 | -45.0586 | 2026-07-03 08:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 55.8 |
| 2912755e-f740-3b9b-8fe2-c77c2b57d50b | -5.7945 | -45.0586 | 2026-07-03 08:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 0c01a480-f487-3e05-a568-e79f7769a4d7 | -5.7945 | -45.0586 | 2026-07-03 08:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 62.2 |
| e793ca7d-2b4f-3e67-86d9-b86b53dfa831 | -5.7945 | -45.0586 | 2026-07-03 08:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 21063c6b-5a34-3d7d-a707-9b5df20b5c14 | -5.7945 | -45.0586 | 2026-07-03 10:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 1cc2b2b0-e33a-3aeb-9f38-c128075d4cb7 | -5.7945 | -45.0586 | 2026-07-03 11:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 187.2 |
| 435998a9-cab8-3137-9563-0311a2871d15 | -5.7945 | -45.0586 | 2026-07-03 11:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 233.0 |
| 22a30d8f-cf35-321b-80f3-ae50e906723e | -5.8132 | -45.0573 | 2026-07-03 11:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 7f1cd791-30e2-3d85-b35a-e4bd0b3c73ed | -5.7758 | -45.0599 | 2026-07-03 11:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 84.7 |
| c4b09ca9-6a58-3732-83ce-360bea23d885 | -5.7945 | -45.0586 | 2026-07-03 11:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 416.5 |
| 08cca171-9e12-35f4-ab38-c7f8c7716be2 | -5.8132 | -45.0573 | 2026-07-03 11:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 114.6 |
| 32e016d5-d3a2-3dab-a3c4-51414188b1f7 | -5.7947 | -45.0359 | 2026-07-03 11:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 00d3d7f0-2391-3ecd-be5c-37e136eeec6b | -5.7943 | -45.0813 | 2026-07-03 11:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 119.1 |
| e9cf8f11-9abd-37dd-b5ae-304ceddd7c2f | -6.90539 | -42.85659 | 2026-07-03 11:28:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 5dc9fbca-6d84-3c71-a62c-4b5606ee1114 | -6.91516 | -43.71061 | 2026-07-03 11:28:00 | TERRA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 8.9 |
| e6cc665a-e8f0-3b3b-96f0-18e8cf8545d8 | -6.92486 | -43.71204 | 2026-07-03 11:28:00 | TERRA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 24.9 |
| 3c36a0ff-3c18-33fa-ab83-25450351491f | -3.4181 | -41.69704 | 2026-07-03 11:28:00 | TERRA_M-M | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| c5782940-cd2e-3e83-ab1e-6f800af62d1e | -5.80004 | -45.04939 | 2026-07-03 11:28:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 136.8 |
| 2d46a126-26bd-388e-b61a-93730dd2d74a | -6.83403 | -44.73695 | 2026-07-03 11:28:00 | TERRA_M-M | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 008e1ebe-2b3a-3a7f-a255-87b331696c15 | -9.47064 | -47.41058 | 2026-07-03 11:28:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| a0738b39-6ee7-3336-bffc-34d017219b3a | -3.41537 | -41.71578 | 2026-07-03 11:28:00 | TERRA_M-M | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 16.3 |


[Clique aqui para ver as próximas entradas](README20.md)

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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 325ea248-c822-3389-96af-ea83cd3a1f03 | -9.0622 | -46.6341 | 2025-10-03 02:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 61.1 |
| f049c9cc-2088-334f-892b-d073f33e37fb | -7.7746 | -42.5865 | 2025-10-03 02:00:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 150.6 |
| f2ec3cd9-d9d4-3285-a8a6-58d59a1b4656 | -11.144 | -43.4082 | 2025-10-03 02:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 106.8 |
| 9a54e408-d714-3b5b-804e-20047fa49c1a | -14.1926 | -46.1091 | 2025-10-03 02:00:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 4ad88876-1cb3-3774-be14-3e9aeb90abcc | -6.0603 | -44.629 | 2025-10-03 02:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 6ab32cc4-652e-3bf0-bf81-d5095c452246 | -7.7749 | -42.5628 | 2025-10-03 02:00:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 96.9 |
| 0151f48f-7366-340c-a064-503acbfd1180 | -10.9667 | -51.1039 | 2025-10-03 02:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 31.1 |
| 3b05765e-d407-3b17-b648-54b57c031d66 | -7.7557 | -42.5885 | 2025-10-03 02:00:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 103.8 |
| 4eb8ad2d-16a6-31c6-9d66-2c1c024a879b | -9.062 | -46.6565 | 2025-10-03 02:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 8b87280c-19f0-36c5-9305-9a35cfe0945f | -5.6363 | -43.9027 | 2025-10-03 02:10:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 73.8 |
| eaed0e8d-36b0-3a75-a816-5c9efa551b60 | -11.1444 | -43.3845 | 2025-10-03 02:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 83.8 |
| d76e3203-3049-3c50-8462-f33243b4afd2 | -6.0605 | -44.6061 | 2025-10-03 02:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 83.5 |
| e529f908-d579-3771-b005-4197073c32fa | -6.0418 | -44.6076 | 2025-10-03 02:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 73cbab73-1192-3d8c-aad0-da3a2d90eabf | -10.2587 | -50.3478 | 2025-10-03 02:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 35.6 |
| e7c41dec-9fec-3bb5-a9d2-0bcb7727fad3 | -12.6135 | -46.9499 | 2025-10-03 02:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 842c817e-3d79-389d-928d-7ec43ef2bba9 | -9.9182 | -43.7212 | 2025-10-03 02:10:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 68.6 |
| c1f9f6fc-f491-3db3-bbc6-fe1df3e7f017 | -12.6323 | -46.9697 | 2025-10-03 02:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 98.0 |
| 9887697b-c6da-3497-bf7e-3a7e6282dffc | -9.0808 | -46.6545 | 2025-10-03 02:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 69038121-ddb7-3cb4-8f61-b144290331d7 | -10.2781 | -50.3032 | 2025-10-03 02:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 106.3 |
| f9f126f6-d4e6-3232-a40a-1373f67a8981 | -13.1345 | -47.882 | 2025-10-03 02:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 55207be1-c7cf-35dc-a30e-e73ea173b1f0 | -7.7749 | -42.5628 | 2025-10-03 02:10:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 98.0 |
| 81922018-12ec-3897-b8b6-00e04182c49c | -9.0811 | -46.6321 | 2025-10-03 02:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 43.5 |
| 4b00f69c-1507-3133-822d-ac0250849a60 | -7.7557 | -42.5885 | 2025-10-03 02:10:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 100.0 |
| 57814b5d-bffa-394d-960f-a4f9cf8be418 | -10.297 | -50.3013 | 2025-10-03 02:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 39.6 |
| c1ce9aed-58d1-3910-98c6-481880a4cefe | -11.9163 | -46.2817 | 2025-10-03 02:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 959adb1c-e0a0-3bac-9898-65655b75b51b | -7.7746 | -42.5865 | 2025-10-03 02:10:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 138.4 |
| 83cdf733-7efb-3258-b462-ea77b275619f | -6.0603 | -44.629 | 2025-10-03 02:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 5118c010-d80f-396b-924f-85fa58f32d8d | -11.144 | -43.4082 | 2025-10-03 02:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 95.0 |
| ecb4823b-91ea-3a10-a1a4-1cdcf4728ec8 | 1.5103 | -55.8259 | 2025-10-03 02:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 9c0147b8-eb01-3f30-9a48-4a38de5d7a3f | -8.1728 | -47.0119 | 2025-10-03 02:10:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 5c8e0ade-9620-3a63-a972-5dd90f5b6abd | -13.9775 | -48.157 | 2025-10-03 02:10:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 139.2 |
| 7e26d2af-8c41-3f0f-8140-4735cb68fbb7 | -13.9771 | -48.1793 | 2025-10-03 02:10:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 103.7 |
| 695c4a89-19ba-3767-9f84-70db7775fb7d | -6.0416 | -44.6304 | 2025-10-03 02:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 116.4 |
| ccb7a96d-256c-359b-85aa-198d65dce12e | -9.0622 | -46.6341 | 2025-10-03 02:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 50.8 |
| 1bd8a4e5-d387-3510-aef8-d1c9042356da | -14.9342 | -46.8965 | 2025-10-03 02:10:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 116.4 |
| b24ac832-e37d-37d3-9802-1662b43c0f48 | -12.6131 | -46.9725 | 2025-10-03 02:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 118.6 |
| 81767271-d1d2-39fa-966a-06d0d323857a | -8.798 | -46.6616 | 2025-10-03 02:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 55.7 |
| 8bba39c9-ade5-3b2c-a139-372f4ad69439 | -11.8967 | -46.3071 | 2025-10-03 02:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 35cc3f3d-ac60-39c6-a552-279b9bbeb339 | -8.6138 | -54.976 | 2025-10-03 02:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 46.0 |
| d6c7a88a-c621-358d-82d2-e0506f4778f9 | -10.2781 | -50.3032 | 2025-10-03 02:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 5f5ae83a-b1a8-3c75-be2a-093e47591f96 | -7.7557 | -42.5885 | 2025-10-03 02:20:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 91.5 |
| 968e1635-fd1b-3cd6-9c7a-f73b603c06c1 | -10.967 | -51.0826 | 2025-10-03 02:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 28.4 |
| 4fad06ec-bbf9-3dbe-a638-c32cea2c8785 | -7.7749 | -42.5628 | 2025-10-03 02:20:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 94.5 |
| b0b1c588-89cd-3bde-8af1-bf5733fea1e9 | -6.3446 | -44.2856 | 2025-10-03 02:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 107.5 |
| 1a951945-02c2-36c7-a355-3457e4f58659 | -11.144 | -43.4082 | 2025-10-03 02:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 135.2 |
| dec86204-a77d-32b3-bda9-c0d0dc30caa5 | -6.0416 | -44.6304 | 2025-10-03 02:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 108.0 |
| 50655d7f-f00e-37cb-8024-a93836ec809e | -18.2167 | -53.3607 | 2025-10-03 02:20:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 57.8 |
| c84485ca-a194-3f0d-ba3f-f68d89b14d4b | -9.062 | -46.6565 | 2025-10-03 02:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 4149abee-d238-38f8-ab5b-abe4874f9e9c | -6.3444 | -44.3086 | 2025-10-03 02:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 171.9 |
| 0471eaaf-1696-3944-9b92-7c5b18035506 | -12.6135 | -46.9499 | 2025-10-03 02:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 86.6 |
| e8ef3b2c-2050-3272-b7a3-aacd51a42fa9 | -12.6131 | -46.9725 | 2025-10-03 02:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 121.4 |
| d7981616-8ae1-3b54-a41e-95716d095b1a | -8.6138 | -54.976 | 2025-10-03 02:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| e47c412b-eb7b-3f65-ab87-d7f259559c82 | -13.9775 | -48.157 | 2025-10-03 02:20:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 93.2 |
| bb1ce51e-c6ef-301f-b788-84fbbd26d2f5 | -14.9347 | -46.8736 | 2025-10-03 02:20:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 103.3 |
| 3698744d-dcc7-30a6-ba5d-546d1f7a9d50 | -6.0605 | -44.6061 | 2025-10-03 02:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 25de9fc9-6a63-39ed-be2d-2fde649d439d | -6.0418 | -44.6076 | 2025-10-03 02:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 81.2 |
| a90338f5-9c86-37d7-a3c0-26821ba4e804 | -13.1345 | -47.882 | 2025-10-03 02:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 86.6 |
| bfd37885-6ebf-365e-b721-35bb691dff98 | -9.0808 | -46.6545 | 2025-10-03 02:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 56.9 |
| 1969d56b-20f9-3c89-9cb7-87f53417a9a9 | -10.297 | -50.3013 | 2025-10-03 02:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 34.5 |
| bec298ea-6f90-3984-9816-3f799f6acd28 | -14.7083 | -43.8869 | 2025-10-03 02:20:00 | GOES-19 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Caatinga | 69.9 |
| a9be94d7-40a2-3f51-80d2-593f12571aee | -12.6323 | -46.9697 | 2025-10-03 02:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 97.1 |
| d38ddcd0-5147-3813-a6a0-8dd443a3f4e6 | -14.9538 | -46.8931 | 2025-10-03 02:20:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 62.9 |
| d79ad533-93f8-32a5-b80b-e7075318e901 | -11.1631 | -43.4054 | 2025-10-03 02:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 88.3 |
| aafa8612-49dd-3f12-8a32-d3ef30b54876 | -14.9342 | -46.8965 | 2025-10-03 02:20:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 167.3 |
| e398bfa7-a548-358a-80ee-a14f44ee7276 | -9.9182 | -43.7212 | 2025-10-03 02:20:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 66.5 |
| 9d797747-6457-39a0-b388-56957ad5b320 | -6.0603 | -44.629 | 2025-10-03 02:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 043dc096-11b2-3c9c-963f-463dfe5955fd | -8.6324 | -54.9747 | 2025-10-03 02:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 39.2 |
| 3f07268e-1ee0-34ed-88f8-64643aa0e195 | -7.7746 | -42.5865 | 2025-10-03 02:20:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 131.5 |
| f04fab2e-52fb-338c-bac6-83d3a0d8a25f | -7.7746 | -42.5865 | 2025-10-03 02:30:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 127.1 |
| 52f024c7-4163-3401-af56-95d439fd0f4c | -4.6504 | -45.8077 | 2025-10-03 02:30:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 334.1 |
| c96aeed4-6cfe-3b6c-b3d2-9adf01a37346 | -9.9182 | -43.7212 | 2025-10-03 02:30:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 77.1 |
| 6af17298-63b9-3e6e-b0a4-210524015fc8 | -4.6505 | -45.7853 | 2025-10-03 02:30:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 357.8 |
| e1e9f062-a94c-3121-9754-b0483c439e8c | -13.9771 | -48.1793 | 2025-10-03 02:30:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 68.5 |
| a62c8957-6e25-39de-aeaf-62752954ec0f | -9.8991 | -43.7237 | 2025-10-03 02:30:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 66.2 |
| 973f3869-9b12-3525-a856-53746ef833fd | -6.0605 | -44.6061 | 2025-10-03 02:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 2173b6da-de5e-3420-982c-2e354df477fd | -6.3444 | -44.3086 | 2025-10-03 02:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 135.4 |
| 5e58424c-2584-35bf-8319-5da14f531cb5 | -6.0418 | -44.6076 | 2025-10-03 02:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 7c2cb8ab-7699-3a2a-a509-43d978f6fa8b | -4.6878 | -45.7832 | 2025-10-03 02:30:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 70.2 |
| f7e193da-2716-368b-a6fe-628e5266889b | -14.7083 | -43.8869 | 2025-10-03 02:30:00 | GOES-19 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Caatinga | 95.0 |
| d3d8b1ac-3493-39e5-971f-18b8b2180190 | -4.6692 | -45.7842 | 2025-10-03 02:30:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 639.4 |
| 400870f2-6aca-34b2-b329-572910f129de | -8.6138 | -54.976 | 2025-10-03 02:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 93ed8fb7-b227-3296-9ffc-98555ba98ede | -12.6323 | -46.9697 | 2025-10-03 02:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 102.1 |
| 13954bbb-f69d-31da-a5c8-88015c9ae28e | -14.9342 | -46.8965 | 2025-10-03 02:30:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 113.7 |
| 03609cf7-5d56-32cb-9556-56a9dacc3171 | -4.669 | -45.8066 | 2025-10-03 02:30:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 742.8 |
| 331f6e2e-7a08-3421-81ed-8f165a29a353 | -7.7557 | -42.5885 | 2025-10-03 02:30:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 85.7 |
| 80a3b572-7b6e-3e71-9da1-9c456c4978f9 | -12.6131 | -46.9725 | 2025-10-03 02:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 127.2 |
| 55f7d62e-aa5f-39d5-b65b-850706aa51bd | -12.6135 | -46.9499 | 2025-10-03 02:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 7fc490b7-6bcd-3f58-8c66-92faa2bc1dc0 | -11.144 | -43.4082 | 2025-10-03 02:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 81.7 |
| d7b4b8ac-f9f3-3131-88b9-8ee832b65cbd | -6.0603 | -44.629 | 2025-10-03 02:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 85dfdf22-ba12-3edd-892c-329e32b5ab1f | -6.0416 | -44.6304 | 2025-10-03 02:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 102.0 |
| 40d8fb4b-cb70-3639-b6e4-e0c89c2d6ec5 | -18.2167 | -53.3607 | 2025-10-03 02:30:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 7de5f6af-f77e-326a-a97c-90d44db9dceb | -10.2781 | -50.3032 | 2025-10-03 02:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 33.3 |
| 3d4f7856-155c-35cb-b863-26e6dc49179b | -13.1345 | -47.882 | 2025-10-03 02:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 101.8 |
| 72311316-286d-3b7f-b647-e522e14af182 | -7.7749 | -42.5628 | 2025-10-03 02:30:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 80.8 |
| 2829ddaa-d04f-3955-b447-d762d2088bb8 | -4.6877 | -45.8056 | 2025-10-03 02:30:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 660d5951-75a0-3926-afac-10286ac43431 | -10.2212 | -50.3303 | 2025-10-03 02:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 33.2 |
| 6639ca05-5596-3fd5-bd69-76e41979ef60 | -13.776 | -47.5843 | 2025-10-03 02:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 74.2 |
| b0d461dd-a571-3dea-a8c1-ce1c3fada3ca | -6.0603 | -44.629 | 2025-10-03 02:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 66861f7a-8d89-3633-978a-6953c3daacce | -12.6323 | -46.9697 | 2025-10-03 02:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 9cc59dfe-3733-3e4f-9b2a-ef2c84b058f2 | -9.9172 | -50.5094 | 2025-10-03 02:40:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 41.6 |


[Clique aqui para ver as próximas entradas](README14.md)

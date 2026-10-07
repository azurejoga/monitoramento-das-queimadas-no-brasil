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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0bfb92d7-a8f8-34d0-9f5e-df310a97d99f | -3.0 | -54.1287 | 2026-10-07 00:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 109.7 |
| 021cd72f-4547-3a20-8ce4-cef1dad17328 | -2.7612 | -54.1142 | 2026-10-07 00:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 116.8 |
| c4935724-cdaa-316e-a6a9-a850317324cc | -8.7036 | -45.2061 | 2026-10-07 00:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 331.4 |
| 9a8e8e61-758a-3e8d-9e05-8838ce4e6788 | -5.7374 | -45.176 | 2026-10-07 00:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 7964c980-f460-3123-9413-3e79957544cb | -1.2922 | -54.5585 | 2026-10-07 00:30:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 0f553650-2567-3b96-be96-e2f026b9a084 | -9.1362 | -65.3022 | 2026-10-07 00:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 37d0ebac-f186-3ad0-b0d1-6183a28c71d4 | -2.7796 | -54.0937 | 2026-10-07 00:30:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 203.4 |
| 129eb4eb-cb32-3af5-bed4-bd9abb002f96 | -3.0558 | -53.9263 | 2026-10-07 00:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 49b412f3-e91f-3cf1-9753-2bfb13b28fb7 | -5.9835 | -40.9367 | 2026-10-07 00:30:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 82.3 |
| 446987bb-e2c2-3676-bd10-3004b1e649ee | -3.5515 | -59.4807 | 2026-10-07 00:30:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 85.1 |
| 8c68f689-2be2-3aa2-a54f-91b4d33d1be3 | -8.2868 | -50.2519 | 2026-10-07 00:30:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| de67b7f6-6243-3fdf-9dad-d58d81c43667 | -7.8234 | -72.7142 | 2026-10-07 00:30:00 | GOES-19 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 29.3 |
| 45d3eabb-a4fe-35de-a110-e0f962ff1993 | -2.7796 | -54.1138 | 2026-10-07 00:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 135.5 |
| cf057eda-efbb-3b3e-8704-2a4d84630618 | -13.4922 | -44.3713 | 2026-10-07 00:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 94bf9349-f679-3e88-9887-c9bb5f0c4742 | -8.7033 | -45.2289 | 2026-10-07 00:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 148.8 |
| 9e730d35-8dcf-3236-a9cf-af357f5d152d | -2.7613 | -54.0941 | 2026-10-07 00:30:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 322.6 |
| 27909df9-a62b-30c2-a01e-102abe8e8fb5 | -3.6205 | -55.2907 | 2026-10-07 00:30:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 88e2e56c-d942-3d70-876a-d47776e1d968 | -3.0375 | -53.9066 | 2026-10-07 00:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 92.4 |
| dc7312e4-d470-30a3-af9f-e328b37daf2d | -3.0374 | -53.9268 | 2026-10-07 00:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 109.5 |
| 58dae585-b1af-3d42-9506-c1df71974820 | -3.0001 | -54.1086 | 2026-10-07 00:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 70efa7e4-edeb-3418-b646-7de405716197 | -3.1114 | -53.7839 | 2026-10-07 00:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 93.8 |
| 5608357b-b82c-3742-b5c1-e9e7556c9c25 | -3.1787 | -50.5597 | 2026-10-07 00:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 195.7 |
| cce96833-bc1e-3c27-b4a1-af8916444730 | -5.7189 | -45.1547 | 2026-10-07 00:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 160.1 |
| d360f76b-8d13-3df8-8ead-3e2d12e8efba | -3.4578 | -50.0679 | 2026-10-07 00:40:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 1e081a54-765a-35ae-81bb-d7e5118b2e06 | -5.7189 | -45.1547 | 2026-10-07 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 181.0 |
| 86609062-8f86-3b85-94b5-a895cbe41ecf | -5.7374 | -45.176 | 2026-10-07 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 4226eaff-aa05-354f-aa3d-3ee9221ce2db | -2.7612 | -54.1142 | 2026-10-07 00:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 103.2 |
| 43396408-b7d4-3a09-8280-7454d919362e | -11.0646 | -45.8312 | 2026-10-07 00:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 141.1 |
| 479ae878-b7e9-3d3d-b228-1dcafe47db77 | -3.0375 | -53.9066 | 2026-10-07 00:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 91.3 |
| 51c063d4-d191-35f9-97e6-32d06424e8a5 | -5.9838 | -40.9123 | 2026-10-07 00:40:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 71.0 |
| 4cc76317-4900-38e8-83a2-2adb366e349d | -5.7376 | -45.1533 | 2026-10-07 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 7782db79-031d-3c31-90f9-3732fad54768 | -8.7039 | -45.1832 | 2026-10-07 00:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 8ed11b15-a05d-3344-8223-3cba55846964 | -5.9835 | -40.9367 | 2026-10-07 00:40:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 126.5 |
| 31ac0893-6297-353b-8903-f1233e3116df | -3.0001 | -54.1086 | 2026-10-07 00:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 81221fcd-b679-3833-b44d-8cebf922aec6 | -8.7225 | -45.204 | 2026-10-07 00:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 106.9 |
| 6119c72b-70d8-39a7-809b-254bf9f593bc | -2.7797 | -54.0736 | 2026-10-07 00:40:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| ccf9e749-430c-32c5-9da7-f42eba35b085 | -2.7613 | -54.0941 | 2026-10-07 00:40:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 283.2 |
| d8263653-c72f-35f1-99b2-ef4c60a9149e | -3.0373 | -53.9469 | 2026-10-07 00:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 85f5ef90-de30-3fc7-8fb4-879ecd33c52c | -8.7228 | -45.1812 | 2026-10-07 00:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 97.5 |
| d1213862-db8d-3505-a8db-3a7eb7a24ad1 | -7.8234 | -72.7142 | 2026-10-07 00:40:00 | GOES-19 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 22.3 |
| dac6c4ec-c7ee-3a25-98ca-0d261f5b88a2 | -1.801 | -57.1161 | 2026-10-07 00:40:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 89.5 |
| 5cfa4366-92b6-3a65-9999-13ec12d44932 | -3.8997 | -59.3198 | 2026-10-07 00:40:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 31020da4-77aa-398d-8c09-b82c334dc82b | -3.1787 | -50.5807 | 2026-10-07 00:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 108.5 |
| 472d3d2e-36d3-3738-b8ef-5ecb9853b46e | -8.6847 | -45.2081 | 2026-10-07 00:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 35.0 |
| b253fe1e-8e81-3000-8165-198735e032c5 | -3.1101 | -54.1661 | 2026-10-07 00:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 3b66c7bd-b7c0-31f1-bbe9-9af51e7f7236 | -2.7796 | -54.0937 | 2026-10-07 00:40:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 191.4 |
| 63546264-7fe8-3e86-9a05-620dd4dec8bc | -5.9649 | -40.914 | 2026-10-07 00:40:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 82.9 |
| 0eea6a5b-6095-3201-8cd5-a47dc2439533 | -3.8566 | -55.9967 | 2026-10-07 00:40:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 106.8 |
| 5115e499-01c2-3840-b0b5-6eb9a5c02e74 | -3.0557 | -53.9464 | 2026-10-07 00:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 463de81d-baed-3f81-a4a4-867369d0c736 | -8.2868 | -50.2519 | 2026-10-07 00:40:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 962cd438-4441-359c-9fe7-af1327a4c4a4 | -3.0374 | -53.9268 | 2026-10-07 00:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 102.5 |
| 32a86384-e308-3113-861a-9c0c49eccace | -3.1114 | -53.7839 | 2026-10-07 00:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 101.7 |
| c779102b-060d-335a-b946-b2ce726f49d3 | -3.8567 | -55.9769 | 2026-10-07 00:40:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 9d5aca7c-a437-3188-a85a-e63c68e2ca0f | -2.9448 | -54.1501 | 2026-10-07 00:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 71001acd-4e5e-3ddb-9e29-e0b5310f27e2 | -2.9264 | -54.1706 | 2026-10-07 00:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 102de7ec-f968-351b-ab12-9552e9feb639 | -3.4763 | -50.0673 | 2026-10-07 00:40:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 233d7d01-41c2-3e96-bd36-4db1cc70a82b | -2.7613 | -54.074 | 2026-10-07 00:40:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 114.1 |
| 8082862d-c711-3b9e-8ff9-cbf25ef2a5ac | -8.2865 | -50.2731 | 2026-10-07 00:40:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 185.8 |
| 9f1b5062-09d8-3b48-bfb2-516e82ff648e | -8.7036 | -45.2061 | 2026-10-07 00:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 217.4 |
| 3b91d2b4-1f82-3325-98b8-bacb2082c678 | -3.1972 | -50.5592 | 2026-10-07 00:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 54864bcd-2db0-38d1-9932-374cc4aacd08 | -3.4577 | -50.089 | 2026-10-07 00:40:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 115.6 |
| 384a67bf-2e7c-3c7c-9107-f20837517f9d | -5.7187 | -45.1773 | 2026-10-07 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 105.2 |
| 0638744e-dd46-3ae0-a0a5-230b0c504b1e | -13.4922 | -44.3713 | 2026-10-07 00:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 76.3 |
| f4b84b0e-49ed-3b52-9a89-ad54e14a7f0b | -3.5515 | -59.4807 | 2026-10-07 00:40:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 85.4 |
| a83b85f3-730e-3fd8-9af1-b65b09905d92 | -1.8011 | -57.0967 | 2026-10-07 00:40:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 60.5 |
| d277ccc5-ada0-3ffd-8c81-a380ae0d1b59 | -3.3906 | -58.1953 | 2026-10-07 00:40:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 48.6 |
| e762c489-9445-30d2-8f60-5d603de135ed | -3.0 | -54.1287 | 2026-10-07 00:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 116.0 |
| 4a776d88-9de3-33e5-a60c-3627bdc27a93 | -11.2333 | -44.8678 | 2026-10-07 00:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 5c2aaa1d-e2cc-3231-890c-94150ac97943 | -5.9647 | -40.9383 | 2026-10-07 00:40:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 151.9 |
| 2d95d024-30af-3d45-b80c-4a460aad63d1 | -1.2922 | -54.5585 | 2026-10-07 00:40:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 73fa775c-40ca-3f02-b7fb-7b1794f34905 | -3.5061 | -51.6924 | 2026-10-07 00:40:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 1c38bc4e-05af-3b45-b281-c93bf0c0df0c | -3.1787 | -50.5597 | 2026-10-07 00:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 176.3 |
| 45b5df63-a4d9-3516-89e3-682dfdceac08 | -9.1362 | -65.3022 | 2026-10-07 00:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 56.7 |
| b26379fb-201b-33af-8119-8f95fc541f83 | -8.7033 | -45.2289 | 2026-10-07 00:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 85.3 |
| bdaec9c5-7282-3b9d-b6ac-a74c02db20b5 | -3.0558 | -53.9263 | 2026-10-07 00:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| ba7b19be-e366-37d0-8bab-56bc8ac57cc6 | -10.9949 | -45.4298 | 2026-10-07 00:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 70.8 |
| f4cf066c-77f0-3a39-9583-3eaf6b4c21eb | -2.9264 | -54.1505 | 2026-10-07 00:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| c86d2a82-7fa2-34e3-b0b9-17516ca29f05 | -11.7335 | -43.649 | 2026-10-07 00:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 114.8 |
| 8fdf645b-b5ee-315e-99e8-b2cd5350a590 | -2.9816 | -54.1291 | 2026-10-07 00:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| d94a879a-4d51-3c5d-874a-6b0e8687ba85 | -2.9447 | -54.1702 | 2026-10-07 00:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| f4b94868-b7da-3582-8541-4263bf7df321 | -2.7796 | -54.1138 | 2026-10-07 00:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 115.9 |
| 448573da-918d-3e54-ae34-82f2f181dcc7 | -3.0184 | -54.1282 | 2026-10-07 00:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 97.4 |
| 85194034-3cf8-31b3-b231-72a367a609d1 | -11.065 | -45.8084 | 2026-10-07 00:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 638b2b13-8df6-341a-b6a1-155f2ff34020 | -2.7874 | -51.6719 | 2026-10-07 00:40:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| f547d609-96d7-3443-b3bb-fcd57febfce1 | -9.4621 | -67.0817 | 2026-10-07 00:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 1f0a6813-0748-3811-a9b3-56871d9d3b71 | -3.8997 | -59.339 | 2026-10-07 00:40:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 76a03205-9f1e-37f1-ba42-5b6ffd619d7c | -4.7589 | -55.6516 | 2026-10-07 00:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 78.2 |
| a9e8374d-9a7d-37e0-8537-90d681045257 | -13.5117 | -44.368 | 2026-10-07 00:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 00f82512-a74e-3f25-b011-11bca84ec77b | -3.4762 | -50.0883 | 2026-10-07 00:40:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 162.2 |
| a7a12687-5b4c-3c0c-9eec-46e37dc2990f | -3.055 | -54.1474 | 2026-10-07 00:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 0ef70202-cace-3aef-9c29-3a0a925e79cb | -3.1115 | -53.7637 | 2026-10-07 00:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 111.4 |
| 5ea358e6-5e4e-38ef-8d45-0bb536deaf08 | -2.9437 | -54.1035 | 2026-10-07 00:47:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 819dceb3-83fb-34b4-800a-e984f3e50dd7 | -3.1199 | -53.7575 | 2026-10-07 00:47:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1e3ae581-ab5f-3a5c-becd-3b5167e0fa82 | -2.7635 | -54.079899 | 2026-10-07 00:47:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4af8e983-8f1b-3ede-a973-a2fdf896a020 | -3.3448 | -59.481098 | 2026-10-07 00:47:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cf7944b3-d78b-34a4-b242-f750cf6dfcb7 | -3.0913 | -53.723202 | 2026-10-07 00:47:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ad365ed7-8705-35df-990c-53c8cee7c5f8 | -3.2782 | -54.039101 | 2026-10-07 00:47:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 228c7de6-6356-3943-8540-64653fb6f456 | -3.8078 | -51.028099 | 2026-10-07 00:47:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a61f72bc-75bf-3c71-9f9c-41a5c27d91d3 | -2.7692 | -54.104698 | 2026-10-07 00:47:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b16b7d55-8d52-314e-9be6-3a09a6275d42 | 1.7207 | -55.617199 | 2026-10-07 00:47:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README5.md)

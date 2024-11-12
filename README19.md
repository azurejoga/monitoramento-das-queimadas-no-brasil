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
| 6ba75dbd-0ac0-3e5b-9d7c-2979f385fb44 | 1.06235 | -60.60042 | 2024-11-12 05:16:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7cde8eaa-5664-3ecf-88ce-b300206c0a2f | -1.47633 | -54.32897 | 2024-11-12 05:16:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4a9ea505-6424-32f7-9aa3-88925575968f | 0.76505 | -59.83088 | 2024-11-12 05:16:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9c945d96-9772-3c66-99f1-5f16e79041ff | -2.12308 | -50.69093 | 2024-11-12 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 26.1 |
| b61e162f-9ec4-303a-9a2e-3d8bb52b474d | -1.62859 | -55.07288 | 2024-11-12 05:16:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5272afdf-b403-39a6-bb52-f3db23290bed | -2.13043 | -50.6773 | 2024-11-12 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2304612e-aa52-3e7f-b8d1-10a76720cf8e | 1.05156 | -60.60207 | 2024-11-12 05:16:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2358f6ce-cb4b-3ee4-9a19-dc3e318a4b55 | -2.12266 | -50.69715 | 2024-11-12 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| dadc6da4-cb31-3f1d-b07a-ae03e376dba3 | -2.12341 | -50.69202 | 2024-11-12 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 26.2 |
| 6fcce609-8e18-39c9-84aa-8dd5f508c144 | -1.62797 | -55.07693 | 2024-11-12 05:16:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 45b4427e-e579-30c1-955a-5e6c8287915f | -2.1199 | -50.67986 | 2024-11-12 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 51cc9f39-a213-3ce3-93c9-64f1462d6d11 | -2.12864 | -50.6865 | 2024-11-12 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2fb4f376-fd02-3512-b19e-9542b88d3db9 | -2.13182 | -50.69752 | 2024-11-12 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| e48d3926-1391-3b1a-9124-bcb9fd89c865 | 0.96936 | -59.74569 | 2024-11-12 05:16:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1e6db757-ae92-3802-971f-f45f42b42980 | -2.7625 | -49.31808 | 2024-11-12 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ad25c6d3-1e49-31e4-b003-a0dbfcfecd71 | 1.08396 | -60.59716 | 2024-11-12 05:16:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 56adfb08-d86c-321a-bd40-cbcc929cdb28 | -2.67364 | -49.26627 | 2024-11-12 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0571f918-8c0f-3024-a0d8-c14104267370 | -2.13023 | -50.67619 | 2024-11-12 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a471b7d6-89c7-3f5d-bf5f-beae19f9937a | 1.05452 | -60.59739 | 2024-11-12 05:16:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f7adb00c-7370-386b-a166-3cb287312c79 | -2.76451 | -49.34169 | 2024-11-12 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d672fc6b-eec9-393d-8632-79dae4f73d20 | -5.23667 | -56.06279 | 2024-11-12 05:18:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a3e68cfa-1884-3920-872c-f681be754121 | -4.34019 | -55.44812 | 2024-11-12 05:18:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 71566771-04f8-3f2c-9084-c5216adabfc0 | -4.36016 | -55.43834 | 2024-11-12 05:18:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d1baf445-8b38-33ef-9d9b-54bda3b803d2 | -5.1498 | -60.37516 | 2024-11-12 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6f0987a5-3fea-393e-baf5-91592c570676 | -2.71562 | -57.34348 | 2024-11-12 05:18:00 | NOAA-21 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7a62c632-e723-3dc9-b517-509bce7430f1 | -3.39945 | -54.9072 | 2024-11-12 05:18:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cb17f474-4799-32c8-8452-b893709c8000 | -3.10531 | -54.28999 | 2024-11-12 05:18:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9f72e391-187f-3eb2-953d-e046074fee60 | -4.11568 | -50.23744 | 2024-11-12 05:18:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 739b813a-aebf-32cf-b740-231051d29667 | -3.51756 | -49.95353 | 2024-11-12 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c842ed2d-a003-3a32-ae64-0f8302cc9690 | -3.95112 | -48.18579 | 2024-11-12 05:18:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 9b8fd3ba-4ad6-30b3-889a-7e2230e054c6 | -3.25328 | -49.89648 | 2024-11-12 05:18:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2bf26d82-5a47-3559-acbc-1d02adb040f9 | -3.05895 | -50.31726 | 2024-11-12 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e4ac1449-c301-30e4-9322-5c33fa2acd08 | -4.25163 | -50.25481 | 2024-11-12 05:18:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9f02090d-6a61-3284-8383-9872adbfed7a | -3.7652 | -49.47628 | 2024-11-12 05:18:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8c81b59f-d875-3328-9502-cf560e5ac92c | -2.51523 | -54.24754 | 2024-11-12 05:18:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ec3fbeca-2b01-3359-864f-50d10415efb4 | -3.07018 | -54.5784 | 2024-11-12 05:18:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4e3d9d7e-b1dc-3935-9905-ff0f7b167626 | -3.10462 | -54.29465 | 2024-11-12 05:18:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 86095c43-c393-386a-8fed-9ff68206cd44 | -2.04 | -56.65666 | 2024-11-12 05:18:00 | NOAA-21 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 1711d6fc-44d3-3767-b685-89ef73b49628 | -3.66917 | -53.51261 | 2024-11-12 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2be750bd-122b-3ad6-ba8d-8a1b2dfac805 | -3.10219 | -54.28474 | 2024-11-12 05:18:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c4c64d87-1d89-3600-a07c-e35365c59b83 | -4.20368 | -55.15783 | 2024-11-12 05:18:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 06a78488-a0a8-3451-abce-0ba54ff81e6a | -3.33758 | -54.18506 | 2024-11-12 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8510a44a-dd87-35f5-b9f0-8d6952ae56e4 | -3.52223 | -49.95732 | 2024-11-12 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b560a04f-1f29-3440-8db3-73b0830fbe69 | -3.43439 | -50.30584 | 2024-11-12 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f2704d05-bbf1-3a40-94cf-be51d3b6fb75 | -1.9113 | -56.91713 | 2024-11-12 05:18:00 | NOAA-21 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ed50fb01-c22a-3e72-b0fd-ae1c2fe5bf87 | -3.7925 | -50.09851 | 2024-11-12 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 5920802f-98c8-382c-85f3-7bf7765b675c | -3.66199 | -54.65847 | 2024-11-12 05:18:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 2f15b53e-8c4a-3d51-b17a-9832b10a74f8 | -3.33957 | -54.18248 | 2024-11-12 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b310f329-0025-3660-a864-89002e43660c | -3.34265 | -54.18795 | 2024-11-12 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 13c4367f-2e1c-3ff3-bcf9-b8992b462b4e | -3.08074 | -49.20573 | 2024-11-12 05:18:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 037c7c2b-3231-366f-b412-9edc07a25d7b | -3.78741 | -50.09771 | 2024-11-12 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 489e1acf-610f-3c91-bebf-f809e7d05ff2 | -3.39576 | -54.90668 | 2024-11-12 05:18:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fd48d384-2840-3d4b-a278-2b8354aba374 | -4.34435 | -55.36456 | 2024-11-12 05:18:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 27.5 |
| 15b5aa5d-dc95-3317-a306-a3b08668ec48 | -3.57782 | -53.78257 | 2024-11-12 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 53d465ec-4019-347d-b488-a56bb7297428 | -3.75456 | -50.18095 | 2024-11-12 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e6b0a3cf-f75b-32c2-a933-4e32e2b08013 | -2.99338 | -49.54082 | 2024-11-12 05:18:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 14591a0c-6e5b-343d-874c-7529666ebbdc | -3.34453 | -54.19117 | 2024-11-12 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 7bbdd77b-54e6-3101-9344-e8265d23f3b2 | -3.34142 | -54.18569 | 2024-11-12 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 51c2895c-8812-3120-bff5-762d2b5725cd | -2.62511 | -54.28973 | 2024-11-12 05:18:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0d25baf3-1e6a-3793-9699-2ff40910999d | -3.72974 | -53.78307 | 2024-11-12 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9944baa6-a2fd-3e32-8ad3-cdf0716de505 | -3.28766 | -50.05214 | 2024-11-12 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d81e4585-89d8-35ca-ac37-25dbe7b78b50 | -3.35627 | -53.40459 | 2024-11-12 05:18:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dc096eb9-8fca-310a-9119-233606089ead | -4.01912 | -49.0079 | 2024-11-12 05:18:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2fdec1ec-8990-3cc5-8849-c09318d6b2b9 | -3.09564 | -54.30553 | 2024-11-12 05:18:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 638b418e-3415-3fb4-8cb5-1d1a09d80994 | -3.73007 | -53.78617 | 2024-11-12 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a40afa72-02b7-3cab-8653-ebfecf774032 | -3.34837 | -54.19179 | 2024-11-12 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 42c73c31-e0d7-310d-b1f3-d900678a2926 | -3.51621 | -49.9626 | 2024-11-12 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0e588eb9-4f77-31cc-8f69-0b021c5e4fbe | -2.98581 | -54.08394 | 2024-11-12 05:18:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7783817a-64e6-38f1-a3bb-5c124248ac64 | -3.57704 | -53.7877 | 2024-11-12 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c7ca7e1e-e5cb-36d8-972e-ba50e99274d5 | -3.81136 | -47.79725 | 2024-11-12 05:18:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 538643e4-05a3-3e9d-b958-472175dcc05e | -3.51162 | -53.79353 | 2024-11-12 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 89b81bb8-0694-3787-9639-f88e137bfc51 | -3.43396 | -50.30871 | 2024-11-12 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c38f4459-51ed-3e2d-aab1-1ee417893258 | -3.95291 | -48.17334 | 2024-11-12 05:18:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2ab9991d-bf69-329d-8ce8-181656e781b6 | -3.43896 | -50.30945 | 2024-11-12 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 10e104cf-4aba-37bd-8f6c-13c78a17713c | -4.42214 | -49.71796 | 2024-11-12 05:18:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 56d44f77-5252-3170-89e0-b355017b9611 | -3.95746 | -48.18296 | 2024-11-12 05:18:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 70c0bc34-c2cd-37fa-beb3-201b9552fb28 | -3.10087 | -54.29686 | 2024-11-12 05:18:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 45bf26d1-5fce-37fb-aebc-3d8c8c3ba732 | -2.51145 | -54.24691 | 2024-11-12 05:18:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 46c6a4b1-1c94-369e-afbf-7542f8e77c79 | -3.06541 | -54.57544 | 2024-11-12 05:18:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 65b55460-4b3d-3876-a820-8c8c1c6c5c78 | -3.10151 | -54.2894 | 2024-11-12 05:18:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e47d7aac-581d-3822-abab-8c08c93f616b | -4.73862 | -49.53413 | 2024-11-12 05:18:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 02b13aed-bcc0-317e-80c2-988f761c5338 | -3.25372 | -49.89343 | 2024-11-12 05:18:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6ca09f6e-63ae-3c50-974c-693607189caf | -3.40923 | -50.37315 | 2024-11-12 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 293e76cc-3eaf-38a5-b78d-26574fc02ef5 | -3.3419 | -54.19279 | 2024-11-12 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2a3ee33c-572f-3ac4-98f6-254defcb5447 | -4.42042 | -50.50024 | 2024-11-12 05:18:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 067b602c-947f-3984-8cda-5c5c32294c8e | -3.95804 | -48.1789 | 2024-11-12 05:18:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bdd2273a-ae65-3cbd-8168-2bab22d108dd | -3.79579 | -50.04025 | 2024-11-12 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0c9bf0fa-468b-30a4-90e4-9374190e4b23 | -3.07489 | -49.20826 | 2024-11-12 05:18:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2ab19b8f-fe70-3292-850e-a3da96b6f1ae | -3.79207 | -50.10149 | 2024-11-12 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| d5ef5560-680c-35f9-9c0a-2dedcbbe1b59 | -3.94419 | -48.15116 | 2024-11-12 05:18:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9b5cb232-0df0-36c0-b879-9d5dbd70776a | -3.95689 | -48.18697 | 2024-11-12 05:18:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 0dfb311a-cd17-3106-b3e1-7f092e6346e9 | -3.51711 | -49.95655 | 2024-11-12 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 59b58f1f-3ec2-3d73-8fac-f151808da828 | -3.71101 | -53.75185 | 2024-11-12 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ad99cb15-3798-3d7a-92f7-55dd8db2a5a6 | -3.53521 | -54.09021 | 2024-11-12 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d398b9d9-66a4-37f5-9ef7-f8210f8cdba9 | -4.28333 | -50.6748 | 2024-11-12 05:18:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3047dea5-99a8-3be5-822b-d0ffbce26811 | -2.98815 | -49.53998 | 2024-11-12 05:18:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9d4442d8-a7b7-3452-b1f8-8ba9632b02e9 | -4.33867 | -55.44975 | 2024-11-12 05:18:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7b8bd2c8-9107-327b-9ba6-4bf19cb77f16 | -3.36895 | -50.05404 | 2024-11-12 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 65c24370-b276-3529-8082-b9bbc5cc91c9 | -2.62273 | -54.27998 | 2024-11-12 05:18:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7c07c08b-0b2f-3a16-bd27-316aa30cf8c3 | -3.43524 | -50.30003 | 2024-11-12 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README20.md)

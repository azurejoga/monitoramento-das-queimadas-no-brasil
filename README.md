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
| cce6224e-775d-3707-b23a-e9b8c5dcf4c3 | -13.42672 | -43.85405 | 2026-01-03 00:28:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 17b9bb52-8f26-331d-8b7d-2b6b7be9fef9 | -11.84605 | -43.72999 | 2026-01-03 00:30:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 858c374a-5ca9-3a65-8a9a-9ede69e54802 | -11.85435 | -43.73429 | 2026-01-03 00:30:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 3ae9aca3-352e-3521-9be4-c36bf284465b | -5.98286 | -44.58679 | 2026-01-03 00:32:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 7007c279-9fa2-35a5-b2c0-5b589ba3063c | -3.16546 | -54.97567 | 2026-01-03 00:32:00 | TERRA_M-M | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 1f3fa8bb-1742-3896-a108-c15448e868e2 | -5.32693 | -43.56247 | 2026-01-03 00:32:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 91743bae-1917-323e-8349-5bb82d4ee109 | -0.80361 | -48.7644 | 2026-01-03 00:32:00 | TERRA_M-M | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| d8313257-2ea2-3dff-9b5b-1e56b337fc01 | -1.85593 | -54.35737 | 2026-01-03 00:32:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 161f5488-e900-3785-a9b4-25fc1162d04a | -4.34281 | -48.60429 | 2026-01-03 00:32:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 178a6d4a-2774-3095-b554-100aecfc74b2 | -1.68594 | -54.03636 | 2026-01-03 00:32:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 1f7a771a-3e10-33a6-b406-108bed5a0bc9 | -4.0077 | -50.22452 | 2026-01-03 00:32:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 2c0376a6-b8ad-3009-afff-6d4a3edf3525 | -4.75484 | -46.71741 | 2026-01-03 00:32:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 8fa94cc5-508f-34c2-9c7f-31dc93261e84 | -4.24584 | -46.7873 | 2026-01-03 00:32:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 96eb4bb6-86b5-3af6-8fbf-44582cec4257 | -5.78532 | -47.80148 | 2026-01-03 00:32:00 | TERRA_M-M | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 12ab9921-2c55-3f96-8344-9c8c114c315c | -4.34133 | -48.59378 | 2026-01-03 00:32:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 30a7d397-9a0e-377c-837f-b0dc7c5eaa07 | -2.38775 | -47.60896 | 2026-01-03 00:32:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 02ad4112-ed97-32f8-b9a1-07e0a0834f59 | -0.82669 | -48.78425 | 2026-01-03 00:32:00 | TERRA_M-M | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| bd7bf430-282d-3b3f-bb80-d1a94f269e54 | -4.35238 | -48.60283 | 2026-01-03 00:32:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 5b5b8f6a-16b0-3f2d-ae27-1093bbe51255 | -5.98235 | -44.59328 | 2026-01-03 00:32:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 11a435bb-d88a-3695-8d30-1bb5e3334726 | -1.68732 | -54.04639 | 2026-01-03 00:32:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 34.8 |
| 70a64722-912e-31a4-80e6-a63b5e97f69a | -2.56285 | -48.46685 | 2026-01-03 00:32:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| da61ef80-5c92-3d3b-99f2-2763565f952d | -4.35089 | -48.59223 | 2026-01-03 00:32:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| c0451908-edba-3966-9035-864a635aadb1 | -2.56126 | -48.4556 | 2026-01-03 00:32:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 29.9 |
| d0a2ff71-f29c-31f2-b15d-265493a68072 | -2.4733 | -48.05353 | 2026-01-03 00:32:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 5a91b2a3-78f2-36e6-a1a8-f9707ecea1a9 | -0.80212 | -48.75897 | 2026-01-03 00:32:00 | TERRA_M-M | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 2e1158de-1d46-3b68-9951-6bdf95602411 | -2.39145 | -47.60158 | 2026-01-03 00:32:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 6a9c47e8-20aa-3fe7-9c7e-b7173b9b9fdd | -4.17247 | -43.62156 | 2026-01-03 00:32:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 21.4 |
| eb41a381-19ff-39ca-a7a9-95c1b36591b5 | -0.83661 | -48.78284 | 2026-01-03 00:32:00 | TERRA_M-M | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 4c1edbb6-a294-3fe8-96ec-004670cb720e | -2.42505 | -49.31791 | 2026-01-03 00:32:00 | TERRA_M-M | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 93e9da51-0674-3e81-9a4a-8cd749a7ae3f | -0.80366 | -48.77032 | 2026-01-03 00:32:00 | TERRA_M-M | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 3181abb8-c103-3cfc-b829-bcb13147f518 | -2.71513 | -49.16946 | 2026-01-03 00:32:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 5ae8dae7-5e75-32d9-9355-e2afc365ae28 | -0.96892 | -46.86961 | 2026-01-03 00:32:00 | TERRA_M-M | TRACUATEUA | PARÁ | Brasil | 1508035 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 04b7ec8f-9b15-3f72-a69d-24fbd08c5499 | -5.23151 | -49.08937 | 2026-01-03 00:32:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 3f842192-416a-356b-acfe-0ddb498cfa35 | -2.71367 | -49.15922 | 2026-01-03 00:32:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 719e088d-ac13-3096-9d25-cd9551bcd200 | -2.13937 | -48.00207 | 2026-01-03 00:32:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 523441b2-8ccd-3d80-a1ce-fe75e2f1a689 | -2.0759 | -54.26143 | 2026-01-03 00:32:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 86dc27ac-fee5-33c5-836d-156d414bf5f6 | -1.85125 | -54.35362 | 2026-01-03 00:32:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| d2bff49c-bd24-3f66-adfa-5b1d373d3b0d | -5.03808 | -43.6073 | 2026-01-03 00:32:00 | TERRA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 34.9 |
| 2822bee9-8d2b-35c1-85f0-8a22f23ee1a3 | -4.319 | -45.06009 | 2026-01-03 00:32:00 | TERRA_M-M | BOM LUGAR | MARANHÃO | Brasil | 2102077 | 21 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 0fc609ef-1c35-3180-a658-aafd2ac1f081 | -5.08818 | -49.51194 | 2026-01-03 00:32:00 | TERRA_M-M | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 06a2bc5e-a45a-3214-aee5-7532f255951d | -4.18047 | -43.63913 | 2026-01-03 00:32:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| c1739e8c-76a4-3d25-a96a-ded019ab8936 | -1.85452 | -54.34685 | 2026-01-03 00:32:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 46508cff-5bc5-3037-ae3a-638d8c74d665 | -2.39219 | -56.05931 | 2026-01-03 00:32:00 | TERRA_M-M | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| e55078e5-179f-3fc8-9b7e-3afc9cf59855 | -5.04304 | -43.60098 | 2026-01-03 00:32:00 | TERRA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 42.4 |
| 4f878294-7600-329e-9448-e1d565961794 | -2.9395 | -51.76598 | 2026-01-03 00:32:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e58d9d42-f3d6-3320-b6b4-b471171092aa | -1.32707 | -47.76821 | 2026-01-03 00:32:00 | TERRA_M-M | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 1ac27c28-2a20-3dfc-bd04-a7ff17ce9e9f | 2.5272 | -60.9931 | 2026-01-03 00:34:00 | TERRA_M-M | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 27.7 |
| 2aabf7f8-6c82-3e0f-9388-2d14ca5ce615 | 0.45826 | -60.44213 | 2026-01-03 00:34:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 23.2 |
| 70311107-2fb0-3edb-a4ef-fe4a240bc62d | -0.48061 | -48.50237 | 2026-01-03 00:34:00 | TERRA_M-M | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 82c2dcf4-cb4a-3ff3-9647-eea8a7aad776 | 1.28563 | -60.30968 | 2026-01-03 00:34:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 33.1 |
| f55becb5-ca8e-3e2a-9f08-3727c7fb7729 | -0.83079 | -52.52047 | 2026-01-03 00:34:00 | TERRA_M-M | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| af7b22e5-caaf-38e2-b940-4e0ba076daf8 | 3.1298 | -60.72644 | 2026-01-03 00:34:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 5fd5301d-ff68-3163-aced-aca10bbc56d0 | -1.18092 | -53.78506 | 2026-01-03 00:34:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| bf19ad73-191e-38d5-828a-3f0dded01867 | 1.28019 | -60.33069 | 2026-01-03 00:34:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 123.8 |
| e2f296e4-381b-355b-bc2f-d49ae4745b63 | 1.28176 | -60.33607 | 2026-01-03 00:34:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 95.1 |
| 2cbb3ca1-3221-3c4e-9c4e-e71e8f3c1851 | -0.48224 | -48.51429 | 2026-01-03 00:34:00 | TERRA_M-M | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| f4f40a8d-9ca5-3da5-a421-2eaedd608724 | -0.60559 | -52.42053 | 2026-01-03 00:34:00 | TERRA_M-M | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 5.6 |
| fbd786b0-9398-3095-8ff1-981666646ee2 | -0.73414 | -52.4231 | 2026-01-03 00:34:00 | TERRA_M-M | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 5.9 |
| f0571110-0544-3bdc-aa25-71dcaad060e0 | 2.52596 | -60.99957 | 2026-01-03 00:34:00 | TERRA_M-M | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 23.0 |
| dbd18e8b-ef41-3a5d-8384-7c85d9103937 | 0.4657 | -60.430901 | 2026-01-03 01:03:00 | METOP-B | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 5c2c2ead-9737-3b5f-a835-a3e6c0699f58 | 3.1301 | -60.701698 | 2026-01-03 01:03:00 | METOP-B | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| da8455a7-1615-36af-af46-bb19783343d1 | 1.283 | -60.319698 | 2026-01-03 01:03:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| b91f5586-da3e-364f-80b5-ee46ed8f33f5 | 3.1121 | -60.965698 | 2026-01-03 01:03:00 | METOP-B | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 03274b90-acc2-3856-8610-a6657f287396 | 3.1281 | -60.7104 | 2026-01-03 01:03:00 | METOP-B | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| f489bd0a-5191-35bb-ab8d-bac2e8a281dd | 3.4396 | -60.558498 | 2026-01-03 01:03:00 | METOP-B | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| e15a220c-a86b-3ac9-8fcd-267ec6be0f34 | 1.285 | -60.3111 | 2026-01-03 01:03:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 773eef1e-9d7e-3e0f-9a8c-c49d29a5aa42 | 2.5504 | -60.353001 | 2026-01-03 01:03:00 | METOP-B | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 6cc49bb5-5b88-313a-87a7-960e1cd01b7b | 0.4676 | -60.4226 | 2026-01-03 01:03:00 | METOP-B | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 1e635fc5-b9c1-3677-98bd-1debd2469c29 | 1.2774 | -60.322102 | 2026-01-03 01:42:00 | METOP-C | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| de3e10cc-39d7-3b3b-8ca2-44d792932932 | 0.4611 | -60.434101 | 2026-01-03 01:42:00 | METOP-C | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 471481e2-1afb-3b67-8df9-6b77a644ae44 | -7.5214 | -63.2616 | 2026-01-03 01:42:00 | METOP-C | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e37633b2-39e6-3a18-98ac-e70c026798e6 | 1.2748 | -60.3335 | 2026-01-03 01:42:00 | METOP-C | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 774e3318-205b-3638-9f48-d79882c8eede | 3.1265 | -60.7188 | 2026-01-03 01:42:00 | METOP-C | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| bbfd8f38-068f-3265-a4c0-06b1a736c915 | -7.5198 | -63.254601 | 2026-01-03 01:42:00 | METOP-C | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4b00e581-b3dc-350c-a5d6-0ea1a3cb703e | 1.28 | -60.3106 | 2026-01-03 01:42:00 | METOP-C | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| ada2da9e-29c3-30f6-8dff-47c97330ed1f | 2.523 | -60.9837 | 2026-01-03 01:42:00 | METOP-C | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| dfce4ca1-fc82-3bfd-9f15-031f2b00c352 | -7.4584 | -35.21082 | 2026-01-03 03:17:00 | NOAA-21 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 6eaad9cc-fc4e-33f0-bd34-e2623a989f84 | -7.81369 | -35.24395 | 2026-01-03 03:17:00 | NOAA-21 | CARPINA | PERNAMBUCO | Brasil | 2604007 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 5a52f05b-d422-3f0c-a0fc-bfc49d4e7412 | -9.48649 | -35.79578 | 2026-01-03 03:17:00 | NOAA-21 | RIO LARGO | ALAGOAS | Brasil | 2707701 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| c83578a6-0556-339c-9825-362d3bf21249 | -7.45771 | -35.21487 | 2026-01-03 03:17:00 | NOAA-21 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 77a996ed-f66b-3aa5-9e86-700164bda1c7 | -9.85404 | -36.17511 | 2026-01-03 03:17:00 | NOAA-21 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 5825cb08-89c0-36d6-b259-29fc1d4cb983 | -9.1235 | -35.5873 | 2026-01-03 03:17:00 | NOAA-21 | MATRIZ DE CAMARAGIBE | ALAGOAS | Brasil | 2705101 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| dfc21cec-fe2e-3e5f-99cd-27a319db3556 | -7.58129 | -40.10431 | 2026-01-03 03:17:00 | NOAA-21 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 5e18a675-3e25-30e7-8c9a-c6c2dfffa685 | -2.94569 | -39.92802 | 2026-01-03 03:17:00 | NOAA-21 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 8.9 |
| eca7ad08-aa53-3741-bf5b-8e8734e981bb | -2.94655 | -39.92302 | 2026-01-03 03:17:00 | NOAA-21 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 4.4 |
| c6bb4a94-6686-3d44-b8a5-43d50409175d | -7.58721 | -40.1054 | 2026-01-03 03:17:00 | NOAA-21 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 818e7be8-f150-39ca-823c-b5a6fb82d5f6 | -7.71788 | -35.39107 | 2026-01-03 03:17:00 | NOAA-21 | VICÊNCIA | PERNAMBUCO | Brasil | 2616308 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 09dda47b-4da7-3671-ab7f-1f9870ae7a87 | -9.48721 | -35.79169 | 2026-01-03 03:17:00 | NOAA-21 | RIO LARGO | ALAGOAS | Brasil | 2707701 | 27 | 33 | nan | nan | nan | Mata Atlântica | 19.0 |
| f2deec6b-c2ce-3d42-8cf4-32b1f2474909 | -7.71358 | -35.39024 | 2026-01-03 03:17:00 | NOAA-21 | VICÊNCIA | PERNAMBUCO | Brasil | 2616308 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 2f61e0a6-7023-3e15-81c6-09808efd13ba | -7.81301 | -35.24801 | 2026-01-03 03:17:00 | NOAA-21 | CARPINA | PERNAMBUCO | Brasil | 2604007 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 090726e6-b72d-376b-af34-9f771b31f29b | -9.11923 | -35.58657 | 2026-01-03 03:17:00 | NOAA-21 | MATRIZ DE CAMARAGIBE | ALAGOAS | Brasil | 2705101 | 27 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| e2b8c444-96e7-35dd-b6d2-e2a057217520 | -9.48794 | -35.78757 | 2026-01-03 03:17:00 | NOAA-21 | MACEIÓ | ALAGOAS | Brasil | 2704302 | 27 | 33 | nan | nan | nan | Mata Atlântica | 19.0 |
| 42c50e7a-4179-3d34-8260-e0d18e7ab452 | -9.11992 | -35.58258 | 2026-01-03 03:17:00 | NOAA-21 | MATRIZ DE CAMARAGIBE | ALAGOAS | Brasil | 2705101 | 27 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| 58118a07-4939-3db1-8dda-1e179ff588a5 | -16.92269 | -40.1299 | 2026-01-03 03:19:00 | NOAA-21 | JUCURUÇU | BAHIA | Brasil | 2918456 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 88c56591-f856-3ff7-a61b-da1a5084d0f8 | -4.44398 | -38.05759 | 2026-01-03 03:19:00 | NOAA-21 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3ec86799-ca1c-3a81-8f8e-2bd9bd5abcf1 | -13.42695 | -43.86022 | 2026-01-03 03:19:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f90b02fd-705c-3360-bca3-59ec0efc0f3c | -16.92244 | -40.1278 | 2026-01-03 03:19:00 | NOAA-21 | JUCURUÇU | BAHIA | Brasil | 2918456 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 2db39e32-a11c-3d23-96a0-718c8ee3753c | -13.4283 | -43.85406 | 2026-01-03 03:19:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ee40af30-c196-32b8-a7d8-e1fefad0bb84 | -13.46605 | -38.93933 | 2026-01-03 03:19:00 | NOAA-21 | CAIRU | BAHIA | Brasil | 2905404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 97cacba0-0555-3309-9263-4098b943019a | -17.18865 | -40.22475 | 2026-01-03 03:19:00 | NOAA-21 | ITANHÉM | BAHIA | Brasil | 2916005 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |


[Clique aqui para ver as próximas entradas](README2.md)

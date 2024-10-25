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

## Dados Diários - Página 99

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1ee5bdc0-af1c-3f09-a8c9-47e068af91b7 | -7.87693 | -61.63623 | 2024-10-25 05:04:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6f1675d0-1d8b-346d-ba9d-06e4cb97b156 | -9.80338 | -61.516 | 2024-10-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 50469fc3-598e-3335-8c2f-0aa775fb0a5f | -9.80278 | -61.51948 | 2024-10-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 29a95941-c037-309b-96f4-5141aff156c8 | -10.20618 | -61.39518 | 2024-10-25 05:04:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a2b901cc-49e6-35d2-aaef-952e9aa3260e | -10.20305 | -61.39367 | 2024-10-25 05:04:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d232bc3f-f223-389d-8c60-1eee08082e06 | -10.20226 | -61.39445 | 2024-10-25 05:04:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9b3ac431-d475-3f6a-b317-7be248e798f9 | -10.2022 | -61.39876 | 2024-10-25 05:04:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 542f2422-0d72-3508-b681-77336180fc7e | -12.05436 | -63.14326 | 2024-10-25 05:04:00 | NOAA-20 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 7.8 |
| d487f8d9-0cb7-348b-b6b9-1898300bc42d | -12.05364 | -63.14735 | 2024-10-25 05:04:00 | NOAA-20 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 7.8 |
| e2ec9c1f-4ea3-3964-9202-df823c6d7e22 | -12.04938 | -63.14655 | 2024-10-25 05:04:00 | NOAA-20 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 2018c006-b359-36dc-8d57-b9b65aa3c181 | -12.04865 | -63.15065 | 2024-10-25 05:04:00 | NOAA-20 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 680f8bb8-faf2-3339-a5f2-fd8a04749d3d | -12.04511 | -63.14574 | 2024-10-25 05:04:00 | NOAA-20 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 11.1 |
| bfc9e5ab-265b-3deb-888d-aadcca8e29ee | -12.04439 | -63.14984 | 2024-10-25 05:04:00 | NOAA-20 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e6d34850-c8fd-3d90-9c8c-b0e80e21381c | -11.98228 | -63.17619 | 2024-10-25 05:04:00 | NOAA-20 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 90218fab-a0d8-3a2c-a8b0-6aa1e31a9852 | -11.97726 | -63.17948 | 2024-10-25 05:04:00 | NOAA-20 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ff3ed221-896d-315a-9e00-5649ac21c02a | -12.97764 | -62.73896 | 2024-10-25 05:04:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 56dc3310-a513-392f-9acc-a9a202ce40e1 | -12.97632 | -62.74646 | 2024-10-25 05:04:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dd58add7-c9b0-39c4-8ab9-33fd09e9d767 | -12.97222 | -62.74569 | 2024-10-25 05:04:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 324ebb9a-4fb5-335a-8438-e0158e433ffc | -12.94581 | -62.7991 | 2024-10-25 05:04:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 077d4bef-d176-33d4-b31d-d15eb7fabc9d | -12.83264 | -62.16182 | 2024-10-25 05:04:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 35a96365-db60-32fb-8ef8-0f38e5deaf4c | -12.38553 | -62.94036 | 2024-10-25 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3787708c-8a2f-3c6c-b920-e7d90a8aec66 | -12.38134 | -62.93958 | 2024-10-25 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a2f045d6-caa8-38ca-8106-8a8a0b1afcee | -12.53762 | -63.25758 | 2024-10-25 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a3c29fae-db63-370c-aa1a-2da7ea137745 | -12.53732 | -63.30851 | 2024-10-25 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d5a85417-f922-33eb-9df8-3e81b54135d2 | -12.53444 | -63.05678 | 2024-10-25 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2e4d940e-cd38-3cbd-b47d-52dad0e22817 | -12.53372 | -63.06075 | 2024-10-25 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7122f7cf-5f95-31d3-910c-3866f61a1534 | -12.53304 | -63.30771 | 2024-10-25 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4ffe96c1-1b3b-321a-8952-5663d64cd56f | -12.53023 | -63.05598 | 2024-10-25 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6ec290dc-c1ea-32d6-a207-10d3a1050b6d | -12.52951 | -63.05996 | 2024-10-25 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 726504d0-8bfc-3596-b100-9ad016443609 | -12.52603 | -63.05519 | 2024-10-25 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e92ef14f-8efb-3396-8142-3117d983aebd | -12.5253 | -63.05917 | 2024-10-25 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 19b8751a-14f8-3987-803d-378f6cdd55c5 | -12.52182 | -63.05441 | 2024-10-25 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| db2990b3-76f0-386f-8030-1354e7b9ba4f | -12.5211 | -63.05838 | 2024-10-25 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4eebcce6-60e1-31fe-9b40-1a0afd94a288 | -12.51947 | -63.30941 | 2024-10-25 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d1871cb4-d99f-3a54-8d6e-e2a9073d1583 | -12.51689 | -63.05759 | 2024-10-25 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 25f6653e-0b24-3aca-88b6-8f8799598d51 | -12.5152 | -63.3086 | 2024-10-25 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ff9cfae7-9c5f-3e29-9c05-b26dbbb8313e | -12.47236 | -63.16239 | 2024-10-25 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5ea43183-3492-3b5b-b638-0e7fbe94efcf | -12.46812 | -63.16158 | 2024-10-25 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 97bf68e9-451e-341c-8070-7cb03166cf4a | -12.4674 | -63.16563 | 2024-10-25 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 6.0 |
| a407ae32-6d52-3e3c-abad-57db18f6a093 | -12.46669 | -63.16969 | 2024-10-25 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 5b9603ad-96c0-30a5-8460-76b71048ace8 | -12.46317 | -63.16483 | 2024-10-25 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 6.8 |
| f0391a58-90cc-3093-afb8-d0a6429810ab | -12.46244 | -63.16888 | 2024-10-25 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 5c56c7cf-4e09-3539-8987-277cd0442555 | -12.46218 | -63.24469 | 2024-10-25 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ae7d722b-32d0-36b5-a528-f1c276ec02e7 | -12.46172 | -63.17293 | 2024-10-25 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 759cafea-38aa-399a-9d5d-ac1ea6c3b8c4 | -12.46146 | -63.24879 | 2024-10-25 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 23822170-c99f-35ec-8538-d735333034f5 | -12.461 | -63.17699 | 2024-10-25 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 642f544d-032c-3357-901a-45ddc4bd19d3 | -12.46028 | -63.18105 | 2024-10-25 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 5.5 |
| d78b923d-d658-316a-a35a-e2eb93527460 | -12.45676 | -63.17619 | 2024-10-25 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 5.1 |
| a12eece6-af07-312d-99f1-30f0757bf57e | -12.45666 | -63.2014 | 2024-10-25 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4fc0d2c5-ec90-3a41-ac60-becdddfb0f7c | -12.45603 | -63.18025 | 2024-10-25 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 2a12ac0e-2b0b-30d4-9ea0-f54f8325506b | -12.45594 | -63.20547 | 2024-10-25 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6896ab2f-705e-31f1-9244-881a14be70af | -12.45531 | -63.18431 | 2024-10-25 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 05e177fc-db4d-35db-8e02-fc458e2ce700 | -12.45459 | -63.18837 | 2024-10-25 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 688ccd35-9269-3ff2-8f42-e60c357c18eb | -12.45314 | -63.19652 | 2024-10-25 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 03f34799-0f92-3638-aff3-5b87195ee94b | -12.45241 | -63.20059 | 2024-10-25 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1f8173f0-f289-33e5-8eb4-06f490457dfe | -12.45107 | -63.18351 | 2024-10-25 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1c70ae6a-b4e1-3d67-b33c-6f13cf7a310a | -12.45034 | -63.18758 | 2024-10-25 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b3ceb171-e46a-3378-99d0-17ac47ba1419 | -12.44889 | -63.19572 | 2024-10-25 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8b1277a0-4f62-3d34-a123-6917dfda529f | -7.86557 | -63.73878 | 2024-10-25 05:04:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 81771b81-da63-3f1b-80b0-ca79dedd416c | -7.86465 | -63.744 | 2024-10-25 05:04:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b611de57-18be-3024-b6eb-acbc36ad43f7 | -7.00183 | -63.05121 | 2024-10-25 05:04:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c4573523-a866-367d-9426-cd346dffd2e1 | -6.53054 | -62.94709 | 2024-10-25 05:04:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 66ead77a-d4b5-38d4-a473-759251778807 | -6.52971 | -62.95193 | 2024-10-25 05:04:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b1b2d3eb-c033-3064-aa8a-dc091e7a50b1 | -6.52509 | -62.95112 | 2024-10-25 05:04:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 84fa9ff2-f640-34d3-90fd-9d37f7e7fe5e | -12.00009 | -63.90534 | 2024-10-25 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 6d904e47-6e58-3652-b6fc-9f3e0f046563 | -11.99927 | -63.90992 | 2024-10-25 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 4e0f1489-2d60-3a1f-afe2-52a84514f283 | -11.99561 | -63.90445 | 2024-10-25 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 42d70f85-c819-3c85-b369-425bab32df50 | -11.99478 | -63.90905 | 2024-10-25 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 1f0cd09d-b72b-349e-b734-cfb2219c62a5 | -11.99112 | -63.90358 | 2024-10-25 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 7ceccd1b-c608-3176-b871-4fc7dbcbeb46 | -11.99029 | -63.90818 | 2024-10-25 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 2c49003e-ac89-3aaf-b6df-0bdc8523fd01 | -12.39047 | -63.86887 | 2024-10-25 05:04:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 483300c4-1714-3749-aef7-4eea8e006bc2 | -12.38964 | -63.87337 | 2024-10-25 05:04:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 276b982d-5df0-3c4f-95a4-f65472e4dd53 | -12.38882 | -63.87785 | 2024-10-25 05:04:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 66e08010-e555-396f-9d4c-0cb60a64c5c0 | -12.38799 | -63.88235 | 2024-10-25 05:04:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 01e540fd-c711-3062-8c6f-dc903cfb4e82 | -12.38716 | -63.88686 | 2024-10-25 05:04:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1fa40309-6e4d-37a3-85d2-fd480d1e477c | -12.38437 | -63.87697 | 2024-10-25 05:04:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e2b6468f-0c56-35b8-b7e5-ba65b42b820b | -12.38354 | -63.88147 | 2024-10-25 05:04:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2e93ba17-9096-340b-849e-d6332a7fca22 | -12.38271 | -63.88597 | 2024-10-25 05:04:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3273f6d3-3b34-31e6-8ef6-28dfdad7d5a1 | -12.38243 | -63.86258 | 2024-10-25 05:04:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 80a6c082-3bd1-3cca-a609-d3fa7889956c | -12.38188 | -63.89048 | 2024-10-25 05:04:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 12319eaf-88dd-310a-89ca-c011d4f8a05f | -12.3816 | -63.86708 | 2024-10-25 05:04:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6abb9d7f-3725-3d87-a78c-15e582e235b7 | -12.38076 | -63.87158 | 2024-10-25 05:04:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b814b9d9-da96-3271-93d1-0838ea842349 | -12.37993 | -63.87608 | 2024-10-25 05:04:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 12f34ab5-8e5e-338a-9a91-1c5d6e0d98e5 | -12.3791 | -63.88058 | 2024-10-25 05:04:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ab110e11-29d9-32c6-8945-0f4108ccfacf | -12.37826 | -63.88509 | 2024-10-25 05:04:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0c776a49-296b-318f-bef6-865105aeea7a | -12.37799 | -63.86171 | 2024-10-25 05:04:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 994f4012-2cb0-3648-9f90-4dcf5fc0289e | -12.37743 | -63.8896 | 2024-10-25 05:04:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5b39dc3c-8079-3369-90d5-cd3b6047eb5f | -12.37715 | -63.8662 | 2024-10-25 05:04:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a5547f59-be34-3db7-b766-868728c28b1b | -12.37498 | -63.86338 | 2024-10-25 05:04:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9245bd2a-5d85-378d-84a5-9f0d11de93ce | -12.37418 | -63.8679 | 2024-10-25 05:04:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 773e4200-526e-3315-82e9-e2761c39b5f0 | -12.37354 | -63.86086 | 2024-10-25 05:04:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 48ac1e40-86b0-37d0-9a79-6573389bbedb | -12.3727 | -63.86536 | 2024-10-25 05:04:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2a290127-2275-3648-8ce6-53fc050c83f9 | -12.37053 | -63.86253 | 2024-10-25 05:04:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c65797a3-15a3-3d55-bb58-67aa792b38b9 | -12.36909 | -63.86002 | 2024-10-25 05:04:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4cde6d55-2a27-36df-9285-75c3aa77386a | -12.36825 | -63.86452 | 2024-10-25 05:04:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 04e44b5f-89ec-3a12-ac19-eb6f06d96f70 | -12.36608 | -63.86169 | 2024-10-25 05:04:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 32944909-c309-3211-af0a-14641b596001 | -12.36464 | -63.85918 | 2024-10-25 05:04:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d86ba79d-b2c5-38e1-96ba-bd035fe50a48 | -7.27532 | -64.65398 | 2024-10-25 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2343cbad-c698-3c20-8277-a421e0f5f56d | -7.27478 | -64.65704 | 2024-10-25 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b39e3b98-3695-333c-9574-0d4a238c76b9 | -7.27423 | -64.6601 | 2024-10-25 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |


[Clique aqui para ver as próximas entradas](README100.md)

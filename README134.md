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

## Dados Diários - Página 134

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9c7cfe48-2ea9-359d-90e7-b7bf0e1cff74 | -9.47918 | -62.38996 | 2024-10-03 04:51:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d0aaa81b-cf04-34c6-94d0-07deb6c41da2 | -9.47858 | -62.39316 | 2024-10-03 04:51:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b259eeb2-09e4-3351-abda-de70b2c5173a | -9.47798 | -62.39642 | 2024-10-03 04:51:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 5.8 |
| c22c675e-00b1-355b-896d-7a3e91e11f26 | -9.47451 | -62.38557 | 2024-10-03 04:51:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 36eb09f2-c7a9-329c-b909-b6e536b3c721 | -9.4739 | -62.38885 | 2024-10-03 04:51:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dd11ed56-d90d-3016-912a-4b2e058cc129 | -9.46923 | -62.38444 | 2024-10-03 04:51:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6d862be3-e31e-316f-8298-7202c7c5588d | -9.46861 | -62.38775 | 2024-10-03 04:51:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 12282d57-fa2a-3f95-9b0b-eb0491853fee | -9.44043 | -62.10389 | 2024-10-03 04:51:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 91a052e5-ebe8-3fcd-a13c-21cc4f19a081 | -9.43984 | -62.1071 | 2024-10-03 04:51:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5f48bab4-7c81-36cb-9c02-6af435bb374c | -10.17186 | -62.31578 | 2024-10-03 04:51:00 | NPP-375D | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fc0eea75-5496-39fc-b4c1-fc1c460b3a54 | -10.16665 | -62.31478 | 2024-10-03 04:51:00 | NPP-375D | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 350e72df-efb9-388e-8489-b201a6c65e74 | -10.63992 | -62.81212 | 2024-10-03 04:51:00 | NPP-375D | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bd86f06b-3d7f-3854-8854-c30a19fcdc00 | -10.63928 | -62.81554 | 2024-10-03 04:51:00 | NPP-375D | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d65e52c0-b7e7-348c-88b0-4d0a7ae70782 | -10.63396 | -62.8144 | 2024-10-03 04:51:00 | NPP-375D | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6f3159f7-3342-3da6-9395-140e387dce91 | -12.07946 | -62.05512 | 2024-10-03 04:51:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 89820b9d-52d7-35b9-ae8f-9e687adc2bf5 | -11.91714 | -62.63609 | 2024-10-03 04:51:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0e6f369c-a62f-3d4f-b2b2-37121bd2ace5 | -11.4835 | -62.47838 | 2024-10-03 04:51:00 | NPP-375D | ALVORADA D'OESTE | RONDÔNIA | Brasil | 1100346 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 47c4d1fc-a93c-3f98-8211-4d82243acd87 | -11.48291 | -62.48145 | 2024-10-03 04:51:00 | NPP-375D | ALVORADA D'OESTE | RONDÔNIA | Brasil | 1100346 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5c929e85-0989-36b2-8dc7-14648e8bb546 | -11.48255 | -62.4783 | 2024-10-03 04:51:00 | NPP-375D | ALVORADA D'OESTE | RONDÔNIA | Brasil | 1100346 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 33c139f8-6d18-310b-a9fe-671ed40a7cc0 | -11.48199 | -62.48138 | 2024-10-03 04:51:00 | NPP-375D | ALVORADA D'OESTE | RONDÔNIA | Brasil | 1100346 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fd8ab23f-ecc5-34d8-af5a-c9e23e9dee85 | -11.34344 | -63.05037 | 2024-10-03 04:51:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 82f7f40f-4d60-391a-913a-d758c68624a3 | -12.82334 | -62.8952 | 2024-10-03 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bf71f80b-2051-3bb1-be0f-e2e2c7d34aa7 | -12.82273 | -62.89832 | 2024-10-03 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 318ebbb0-0777-37b8-8e76-cb22de5a0e66 | -12.78182 | -62.91679 | 2024-10-03 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 69fcb71f-3f24-3ae9-bbc8-e6a744ba99b7 | -12.78121 | -62.91996 | 2024-10-03 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 71bf107d-9526-39f1-bdc9-35aa003c68bb | -12.77665 | -62.91571 | 2024-10-03 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 161a780e-306f-3c07-ab91-4024194c0472 | -7.58583 | -63.3647 | 2024-10-03 04:51:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7b2efbe8-ee1c-30c9-b506-3a85399f7a87 | -12.75992 | -62.91887 | 2024-10-03 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d969f37d-b755-301d-b73c-94ecf748356d | -12.75932 | -62.92205 | 2024-10-03 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 34463da3-9591-3e65-a152-183d4699b9cb | -12.75414 | -62.92101 | 2024-10-03 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 707c8355-2a80-3c52-bbc7-200915e3013e | -12.7529 | -62.87138 | 2024-10-03 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b3db06eb-cfb9-33b2-ac38-87831e836d6c | -12.75108 | -62.88087 | 2024-10-03 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9a4ff5d1-f78b-3fd4-90e9-5f8de023baba | -12.75048 | -62.88402 | 2024-10-03 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 60217921-d49b-3747-84ce-39402de4c89a | -12.74896 | -62.91996 | 2024-10-03 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9ea195d2-2e27-3440-930a-8cd049bd7052 | -12.74775 | -62.87033 | 2024-10-03 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ebc7e6f7-51e6-3e74-9566-e15916351d9c | -12.74714 | -62.8735 | 2024-10-03 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| aec1f2a8-7744-3a84-ba3a-d9ea6723ad1a | -12.74653 | -62.87665 | 2024-10-03 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b0b1db10-9373-31c4-8b8e-a11880c4a234 | -12.74592 | -62.87982 | 2024-10-03 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 8b995368-ef28-365d-aaea-da4a997801a0 | -12.74531 | -62.88298 | 2024-10-03 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 53a1ec2b-edd7-3ac6-bc67-7396da018cf5 | -12.745 | -62.91255 | 2024-10-03 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| eb1c6f9a-25c6-3562-8458-c55099029079 | -12.74471 | -62.88614 | 2024-10-03 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c438134a-01a9-31d3-9f62-b372819100cd | -12.7441 | -62.8893 | 2024-10-03 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e2cab054-92b0-3c5f-87d1-711e29d6de4d | -12.74379 | -62.9189 | 2024-10-03 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 010e7dae-1243-34e9-b98b-08e5d79c4a87 | -12.74227 | -62.89882 | 2024-10-03 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a97eb1da-bffa-3c40-b890-ddc347683598 | -12.74166 | -62.90199 | 2024-10-03 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| df079271-c13b-3399-9f56-38fbcf6aea61 | -12.74105 | -62.90516 | 2024-10-03 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 263ccfc4-20e5-31cd-8995-f4ddd9e5633e | -12.90618 | -62.467 | 2024-10-03 04:51:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 8.3 |
| c69677bd-b9e0-3654-b75c-20f7f382b58d | -12.90231 | -62.46006 | 2024-10-03 04:51:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 857f4ff1-26cc-31dc-9ffd-4d40bd391312 | -12.90117 | -62.46599 | 2024-10-03 04:51:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 4aa398ac-0f88-37c5-830a-b33ad0b30de7 | -12.89979 | -62.45631 | 2024-10-03 04:51:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 3015a9be-fb9f-357c-bc86-f493025f8fc4 | -12.89869 | -62.46227 | 2024-10-03 04:51:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 4f97169a-d902-3c2a-a475-28327079db17 | -12.8973 | -62.45905 | 2024-10-03 04:51:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 91c4d5d2-5a16-362c-8968-7e180fee4fe3 | -12.89616 | -62.46498 | 2024-10-03 04:51:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 11.7 |
| b1f211f8-e534-394c-837b-fc83d4662faf | -12.89479 | -62.45528 | 2024-10-03 04:51:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 8.1 |
| f7cf6eab-3a75-3aa0-844e-6b065875ea0d | -12.89368 | -62.46123 | 2024-10-03 04:51:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 8.1 |
| cc6dd348-416d-395e-b3a4-994e365f57e8 | -12.89345 | -62.45208 | 2024-10-03 04:51:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 6bf89da8-5d71-394d-bc09-bd763d694412 | -12.8923 | -62.45802 | 2024-10-03 04:51:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ce8bc65d-ef34-3b54-8a4c-265588d5e11e | -12.88978 | -62.45425 | 2024-10-03 04:51:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 50cffdbd-3041-3ecd-b784-619efc1c7844 | -12.88845 | -62.45106 | 2024-10-03 04:51:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 8994bc8d-b9d9-3e18-864a-08d7697fc545 | -12.88729 | -62.457 | 2024-10-03 04:51:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 56eaa6d6-2f0f-3615-a0d1-6945a1aa9f70 | -12.88478 | -62.4532 | 2024-10-03 04:51:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| ebd6a039-b88a-3f4e-ab03-1ded4c1c273d | -12.88229 | -62.45597 | 2024-10-03 04:51:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d63eb9b2-0be5-3c99-a6a7-477dfb8a7247 | -12.88114 | -62.46188 | 2024-10-03 04:51:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 6.9 |
| c7f16767-63ca-3b46-80fc-f30fb5dde813 | -12.87977 | -62.45217 | 2024-10-03 04:51:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 10ce1a94-7ecf-3a47-9162-0756b4a68664 | -12.87867 | -62.4581 | 2024-10-03 04:51:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 9797ea2f-9b64-382f-bfa5-8a7fa20d09cc | -12.87756 | -62.46404 | 2024-10-03 04:51:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 7.2 |
| d3467970-ab99-3b4d-82a3-c3077c583854 | -12.87728 | -62.45495 | 2024-10-03 04:51:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f0e919dc-5b85-316a-a0e8-e8a2881cd809 | -12.87613 | -62.46087 | 2024-10-03 04:51:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 6256aa24-1e94-3304-8c24-1feb96eb7160 | -12.87498 | -62.46679 | 2024-10-03 04:51:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 44bc89bb-b50c-3372-93d0-67caa96c3913 | -12.87365 | -62.45709 | 2024-10-03 04:51:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 3817133a-883c-3660-a22a-174f9fada926 | -12.87254 | -62.46303 | 2024-10-03 04:51:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 1096a7da-29a7-3fac-ae4c-94967eb96390 | -12.87112 | -62.45988 | 2024-10-03 04:51:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| dc5f2bc8-4547-36fe-9f23-96d1fb075c83 | -12.86864 | -62.45606 | 2024-10-03 04:51:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ab4d2f00-21bf-3d32-b25f-ff49c3f58960 | -12.86611 | -62.45885 | 2024-10-03 04:51:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0b689e26-d8c8-3386-9834-f59090b195ed | -12.86495 | -62.46476 | 2024-10-03 04:51:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6c11ab82-2601-373c-ab39-23cf0736fe2c | -12.86364 | -62.45501 | 2024-10-03 04:51:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f4b3396b-1d66-3ca0-89f6-d827409dcd15 | -12.86252 | -62.46095 | 2024-10-03 04:51:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6d60eae8-60ff-319b-943c-c5c4b18f54a4 | -12.86141 | -62.46688 | 2024-10-03 04:51:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f4919477-af33-32d8-8a8f-31e327f26b8b | -12.85752 | -62.45992 | 2024-10-03 04:51:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3bc5892a-7b37-3d59-aece-fab66d069cf4 | -12.64626 | -63.11386 | 2024-10-03 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 5d0d1d35-c981-3a4e-814d-abec918a978e | -12.64594 | -63.101 | 2024-10-03 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 72e85ab2-beeb-3a76-8c42-7fc7f403ce38 | -12.64561 | -63.11716 | 2024-10-03 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 45391ed5-6473-3658-91e9-a0c8a93c678b | -12.64557 | -63.13179 | 2024-10-03 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 0d3d4a97-ce35-3c83-bc38-9cd6b92555a2 | -12.64532 | -63.10429 | 2024-10-03 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8803d874-308c-3559-8cfd-a3099436979e | -12.6447 | -63.10758 | 2024-10-03 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c3e5ce86-28ed-35cd-ab91-2946412b4efa | -12.64432 | -63.1384 | 2024-10-03 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b6dedc39-c413-3a6c-ac68-6a4d1edc0a80 | -12.64408 | -63.11087 | 2024-10-03 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 57d04f57-5160-3b58-86cc-d8bc347a8b71 | -12.64345 | -63.11417 | 2024-10-03 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 5.6 |
| f6f2de15-4eda-3810-a54f-70a7bff703ea | -12.64301 | -63.13037 | 2024-10-03 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 1bdf93a6-2334-3365-963b-b37518f0408e | -12.64296 | -63.10294 | 2024-10-03 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d0bc62e3-9746-3962-baa4-ee1c98a99e96 | -12.64283 | -63.11746 | 2024-10-03 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 5376afab-a7ac-3f9b-a397-529fa7d744c8 | -12.64236 | -63.13367 | 2024-10-03 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 5.1 |
| c7d633e7-9e3a-3915-8b8e-22138774d2e9 | -12.64231 | -63.10622 | 2024-10-03 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4404e591-6347-32d3-b0bd-4fad626f43f7 | -12.64166 | -63.10951 | 2024-10-03 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ee74c660-85c7-3a83-910e-6a971697750e | -12.64101 | -63.11279 | 2024-10-03 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 83a974e6-ed24-3263-86ee-66e35937dcae | -12.64094 | -63.12739 | 2024-10-03 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 2f38ce42-112d-34f3-9f6a-4080fa806a29 | -12.64036 | -63.11609 | 2024-10-03 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 0cf8f06d-b15c-3663-9487-3bbb6af3ce87 | -12.63971 | -63.11939 | 2024-10-03 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0b5de5ce-6c45-3c3a-a184-f965927fe27d | -12.63906 | -63.12269 | 2024-10-03 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 6c3aef33-ecb6-3a6e-a499-340c569d871c | -12.63883 | -63.10977 | 2024-10-03 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |


[Clique aqui para ver as próximas entradas](README135.md)

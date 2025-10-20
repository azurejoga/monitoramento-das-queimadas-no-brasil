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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 190a026c-22d0-35ec-9414-22de7951e406 | -4.83748 | -45.79596 | 2025-10-20 05:04:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fff51076-213d-3701-b710-2999d95335fd | -4.67493 | -46.82695 | 2025-10-20 05:04:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f1661afc-df16-330f-95d7-08c9e93db4e4 | -8.02719 | -63.88824 | 2025-10-20 05:04:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 62868e38-7068-313d-b6b4-30bc9ec0a97d | -3.50471 | -55.48093 | 2025-10-20 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b0a36345-09fd-3a18-b7d7-2bc9e2ca1012 | -6.85896 | -46.2975 | 2025-10-20 05:04:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3c28917a-0d18-3ea2-8e33-d33440ce95f6 | -4.83225 | -45.79628 | 2025-10-20 05:04:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5ef3334a-439a-3ef3-a1b6-e21c1260aee8 | -5.68207 | -48.00217 | 2025-10-20 05:04:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dd08411f-2fda-328a-b2bd-43c710648908 | -5.08911 | -45.89165 | 2025-10-20 05:04:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a0e1bae9-7cfb-3dba-94fc-b0edcb101301 | -4.75152 | -46.85909 | 2025-10-20 05:04:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 449c1b09-8040-3d2c-a3de-cae6023c6526 | -5.62312 | -43.6422 | 2025-10-20 05:04:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0eb637c2-008c-3970-85a9-2bf2ef3c6c02 | -4.67536 | -46.82401 | 2025-10-20 05:04:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9ccbeb0f-0bdf-38b1-b29d-de605d97b53e | -7.0699 | -46.19651 | 2025-10-20 05:04:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 2ba2acc1-7c37-371d-84b0-87a29dc7d81d | -3.50141 | -55.48042 | 2025-10-20 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 00602683-4f7b-379f-a0b0-eba8d72b90e9 | -4.67329 | -46.82228 | 2025-10-20 05:04:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d77a1d65-1b95-3b6d-b368-29e301e8cd25 | -6.85944 | -46.29398 | 2025-10-20 05:04:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 75dabee2-56a8-3c25-831d-4e3c988d3087 | -5.36332 | -45.50763 | 2025-10-20 05:04:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 051ff201-85e1-3e8a-a541-be45dc192d26 | -6.85397 | -46.29317 | 2025-10-20 05:04:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9476431d-f378-30f5-b484-5adab38ff624 | -3.49811 | -55.4799 | 2025-10-20 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1d9c7f8d-b4ef-303a-b5f2-881a3693ba8c | -5.0896 | -45.88817 | 2025-10-20 05:04:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9bb94061-6059-3c6d-a90f-bc0a39790835 | -3.75034 | -55.56212 | 2025-10-20 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 77a72b2b-ae58-3aa3-be49-93f01a1cbe65 | -4.82902 | -42.75248 | 2025-10-20 05:04:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e4387485-2b63-3aaf-a9af-5dd49d1973a2 | -5.36847 | -45.51196 | 2025-10-20 05:04:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6772d041-b238-33e8-bb2a-fc5ddf0a833b | -5.68278 | -47.997 | 2025-10-20 05:04:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8b084489-fdf5-3417-bc02-d2aa0df5336f | -8.99528 | -63.6369 | 2025-10-20 05:04:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eeb5739e-cec4-3b8f-9c75-246464012dd9 | -7.21001 | -45.41784 | 2025-10-20 05:04:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c276e3e4-4bf0-3822-a417-112334a5d909 | -3.37391 | -54.74693 | 2025-10-20 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 449aecd7-9951-3a65-9dbf-a667ae18f3d8 | -4.83137 | -45.79933 | 2025-10-20 05:04:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b07c2267-8245-3da3-ae9d-42d4e2a08647 | -3.50417 | -55.48436 | 2025-10-20 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 09486667-fbb7-37b9-9566-39e132455438 | -5.0901 | -45.88471 | 2025-10-20 05:04:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8a104e48-21c5-3790-a269-8ae998d1da60 | -7.06945 | -46.19978 | 2025-10-20 05:04:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 61decace-99ba-3db8-af3a-294c597cc756 | -3.84568 | -49.91306 | 2025-10-20 05:04:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 06da67e5-8e3d-3549-96c7-b8bfcf0e23d2 | -2.95381 | -59.16393 | 2025-10-20 05:04:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2c42674e-b3a3-35c8-943a-95eed8548bec | -8.64567 | -63.04972 | 2025-10-20 05:04:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6aee909c-9588-3cd3-bc5a-4dad2542b9de | -5.6295 | -43.6431 | 2025-10-20 05:04:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 25a84218-a967-3781-a472-382e0409b0af | -4.38731 | -49.68256 | 2025-10-20 05:04:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ef2ef6f8-f9ca-3c6c-af7c-fa87678aef3a | -4.83693 | -45.79969 | 2025-10-20 05:04:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fcab20c0-9db7-3fcc-b70b-ca9ed17b6f7a | -4.83191 | -45.79564 | 2025-10-20 05:04:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 004503a2-26dd-34a4-8a73-1a338dece7c7 | -6.83245 | -51.77529 | 2025-10-20 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d1bf168d-b453-3d3a-a84c-8f8eae014587 | -6.85744 | -46.92983 | 2025-10-20 05:04:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f84ac54b-7996-3200-94db-2d65b77e28a4 | -8.36418 | -64.077 | 2025-10-20 05:04:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4ab9dacd-ef9e-3cbd-895f-d1d2172c8a62 | -3.85385 | -49.91423 | 2025-10-20 05:04:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 621cd311-cad4-3d4e-a96c-dc72aaa403b3 | -3.74275 | -52.26871 | 2025-10-20 05:04:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6fd2fa1a-9e7f-3e5e-ba79-b0bcfa1690d8 | -5.59998 | -51.41511 | 2025-10-20 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 743fd375-ed1a-31f9-b0f3-5f9d6267f7d5 | -5.83831 | -47.56258 | 2025-10-20 05:04:00 | NOAA-21 | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 56c2f93f-b2e2-3124-8561-1252f67c4e30 | -5.84327 | -47.56315 | 2025-10-20 05:04:00 | NOAA-21 | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| adc7cd13-cd8d-33b4-b4d3-45219b31c3b4 | -3.74926 | -55.56899 | 2025-10-20 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 85d85aeb-c56a-3e08-89bc-9bd272a2edc8 | -3.84563 | -51.40453 | 2025-10-20 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e7e0bef9-701a-3078-a880-f501c09f9972 | -6.43277 | -42.99467 | 2025-10-20 05:04:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b274046d-1b7e-3959-94b4-d1d1d0f2720e | -6.85448 | -46.28945 | 2025-10-20 05:04:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c7925bdf-8552-36d4-9697-7b09ed236794 | -3.40238 | -54.06432 | 2025-10-20 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 04a37d53-7477-36c4-b0e5-f5273bd0abfc | -4.83276 | -45.7926 | 2025-10-20 05:04:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1a7ed4bf-2ddf-3af6-bdac-7205c4c3ab5a | -3.84976 | -49.91364 | 2025-10-20 05:04:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| aabc32e7-76a1-3a45-9dc9-0edd54d1119b | -5.08861 | -45.89513 | 2025-10-20 05:04:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6dbf460b-882b-39cf-a8a2-cc6aee4c417a | -4.86786 | -48.40266 | 2025-10-20 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 04203216-3a43-343e-92af-23d05cb001f7 | -3.84462 | -51.38612 | 2025-10-20 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9a8a6db3-8fb2-3fa3-984b-7636c0382781 | -3.50747 | -55.48487 | 2025-10-20 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9856c9bf-345d-3d67-b684-646165a625af | -5.6288 | -43.64824 | 2025-10-20 05:04:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 74bba907-a9e7-3e66-a580-a8a066776214 | -4.83174 | -45.79998 | 2025-10-20 05:04:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e57cbdf3-7604-3d58-980e-beadcac94d29 | -11.58381 | -49.54055 | 2025-10-20 05:04:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e5efe842-cd0e-32f9-ac73-f88705f01eec | -5.10732 | -43.19573 | 2025-10-20 05:04:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e4fe8c3c-4d4f-3838-9011-c183523398ef | -6.12253 | -57.71169 | 2025-10-20 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| c8630068-ba8d-31f8-ae22-a71b3f30088f | -7.21583 | -45.4187 | 2025-10-20 05:04:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b8a42822-b124-3a97-afc5-03e938edf035 | -3.62502 | -51.40189 | 2025-10-20 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 327bc511-6d87-359c-ad43-b2ebe9c62ae4 | -5.75744 | -50.22115 | 2025-10-20 05:04:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f6a48fe5-5b8d-353f-bb14-7c16c579b02a | -3.84922 | -49.9173 | 2025-10-20 05:04:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1e46863d-5e9b-30df-a879-8b693f9862bf | -5.62241 | -43.64738 | 2025-10-20 05:04:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 8c920453-24c8-3b94-9dc5-1238ef3b5c47 | -6.42608 | -42.99359 | 2025-10-20 05:04:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fab49a9d-7a2f-30a6-8536-4573448a6839 | -3.51077 | -55.48538 | 2025-10-20 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| adfface5-a8fe-3ee1-9010-507d025748b3 | -4.8365 | -42.74742 | 2025-10-20 05:04:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2d279428-2d6a-3d5d-9385-ac2071447710 | -9.89958 | -64.17689 | 2025-10-20 05:06:00 | NOAA-21 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| df20726e-287e-3f26-8f21-41be843f1c82 | -9.64627 | -64.7388 | 2025-10-20 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 364304a7-aef8-31ee-8cb9-f20189e48b2a | -16.40124 | -54.82404 | 2025-10-20 05:06:00 | NOAA-21 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 31842187-06de-3ff1-8d4d-28ba92c2701b | -14.23186 | -51.78838 | 2025-10-20 05:06:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8c5cce03-3a2f-32e2-b7bd-352a6507295b | -9.64044 | -65.25538 | 2025-10-20 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 207434c9-87a1-3752-bbc9-7c3c41a9a1d8 | -9.11154 | -65.36536 | 2025-10-20 05:06:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fcdbf443-bfea-3968-bcdb-7e1805e8708e | -14.21875 | -51.43237 | 2025-10-20 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c7ab70dc-9bcb-3585-a745-4d142bf55f49 | -14.21393 | -51.4359 | 2025-10-20 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ac2dc289-719c-3e8d-b669-9e7df2da38db | -14.23217 | -51.7956 | 2025-10-20 05:06:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c26121db-729e-3210-8e2c-392b07b78b87 | -9.89482 | -64.17602 | 2025-10-20 05:06:00 | NOAA-21 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 978e4a98-abeb-3e7c-8a1d-6735aaaa844c | -14.2091 | -51.43944 | 2025-10-20 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2a95b4d4-d1d3-35f4-b72e-4c0f58846963 | -15.30258 | -59.2332 | 2025-10-20 05:06:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 21bd791e-4250-3ffa-95dd-e5a1ff65b2b1 | -9.64558 | -65.25632 | 2025-10-20 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bf049f1d-cc68-30e1-a4d0-7dde7b36ee4f | -14.23133 | -51.79232 | 2025-10-20 05:06:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fa69e51e-d6ef-3b3b-bf71-51e18a6ef357 | -9.64132 | -64.73782 | 2025-10-20 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1e53a2e2-19eb-3a94-865b-47c34935635d | -14.20374 | -51.51426 | 2025-10-20 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2d7478be-bb75-3572-a570-84e7735da513 | -9.64029 | -64.74355 | 2025-10-20 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a103b7ef-1d6f-360d-b4dc-e5da6b4a9543 | -16.80531 | -53.93106 | 2025-10-20 05:06:00 | NOAA-21 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f774ac0c-b087-3b61-accf-9fcf657c4a41 | -9.63482 | -64.74545 | 2025-10-20 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7b2de388-edf7-3122-b92f-74b1762167c5 | -16.78495 | -52.21263 | 2025-10-20 05:06:00 | NOAA-21 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2ea41b0d-4419-3475-87bf-c977f62af350 | -10.63611 | -61.78707 | 2025-10-20 05:06:00 | NOAA-21 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 70a06160-3d9a-35a0-bcef-91ecf551a947 | -9.73247 | -64.94896 | 2025-10-20 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a7f8e626-55f4-3f64-839e-d3fa7008f7e1 | -11.5885 | -49.54121 | 2025-10-20 05:06:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 98c0411b-82fd-3c7e-9f83-bce94a41776f | -14.89478 | -52.934 | 2025-10-20 05:06:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 759783f5-ccbc-3d86-92c0-9b06ae599034 | -14.23026 | -51.80023 | 2025-10-20 05:06:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2169967f-0736-35a6-9b3f-40f226c1351d | -14.21767 | -51.44066 | 2025-10-20 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a5972187-07c5-3c18-a1a1-337e93cba7d5 | -14.18564 | -51.52002 | 2025-10-20 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c0e00549-e508-3335-9da3-3bea917ed957 | -10.63548 | -61.79066 | 2025-10-20 05:06:00 | NOAA-21 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d02208f0-1563-3904-9d6c-d0021ab3f2c8 | -9.64182 | -64.73501 | 2025-10-20 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b4a9d102-d1e6-37f9-bd9c-d85b881dde52 | -11.8466 | -49.81421 | 2025-10-20 05:06:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 04a6e472-c847-387c-a9db-91c02e750cfc | -9.11791 | -65.3599 | 2025-10-20 05:06:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |


[Clique aqui para ver as próximas entradas](README18.md)

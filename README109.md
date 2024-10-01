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

## Dados Diários - Página 109

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 37a97c26-56e4-3ef7-93cc-a3c361581bf1 | -13.69536 | -50.95704 | 2024-10-01 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b56857be-ac1c-3023-bf78-6a2b63fd43a1 | -13.64274 | -51.16105 | 2024-10-01 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e57cdae3-984c-324d-b782-a380a747e46c | -9.18674 | -51.32181 | 2024-10-01 05:06:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eb1c7bb1-c27d-3ed1-bf6d-1c5836fa218f | -9.17166 | -51.31235 | 2024-10-01 05:06:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fb346cc8-a394-369b-9fa5-8b049d3e79c5 | -9.16763 | -51.31172 | 2024-10-01 05:06:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eeadb41b-0606-3041-8606-d88706b5f5ce | -9.66319 | -50.92834 | 2024-10-01 05:06:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0929f405-5ecd-3796-a333-ab4ec4b2bd40 | -10.52767 | -51.08915 | 2024-10-01 05:06:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 188316c2-5388-36ff-a719-9f1f446010b2 | -10.52647 | -51.08641 | 2024-10-01 05:06:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 388f36ee-81dd-37d5-90fb-0aa942c9a68e | -10.52589 | -51.09052 | 2024-10-01 05:06:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ca5f2462-2887-3b8d-abc1-607cdf58f0fe | -10.52226 | -51.08611 | 2024-10-01 05:06:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bd731380-7fe4-37ac-a83c-666d8d5d9cee | -10.52168 | -51.0902 | 2024-10-01 05:06:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 342fd5e3-fac3-3620-9754-7a29a03f194c | -10.51645 | -51.09708 | 2024-10-01 05:06:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| eaf5a663-71d5-3783-b089-90448c088ccb | -10.50901 | -51.1197 | 2024-10-01 05:06:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1e5e1671-9b63-3f13-a2c0-defd5dc2b9a7 | -10.50849 | -51.1234 | 2024-10-01 05:06:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8e9f6db0-2804-3b31-8613-e789f9faceca | -10.50799 | -51.12693 | 2024-10-01 05:06:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a43810d3-62c4-398c-9afe-25ec883458b2 | -12.2741 | -51.5369 | 2024-10-01 05:06:00 | NOAA-21 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 533d6e0a-fdb7-3152-90c8-4f0245b6b820 | -12.27356 | -51.54083 | 2024-10-01 05:06:00 | NOAA-21 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d8a91d76-bae7-37d0-bbfc-43b02a8ee70a | -12.26995 | -51.5363 | 2024-10-01 05:06:00 | NOAA-21 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8869defd-d48f-3dfa-a82d-352d5a047928 | -12.26941 | -51.54023 | 2024-10-01 05:06:00 | NOAA-21 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1b1326b7-d071-31b8-97a2-57b7e070ad5c | -12.99377 | -51.35374 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e9384d34-e2cd-3407-b2ea-a6027e660bc7 | -12.99325 | -51.35778 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e54854a4-c594-3800-8b04-ebce252631d4 | -12.98476 | -51.35656 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e43763e7-40c9-3ffc-a364-c63ab472eb73 | -12.97481 | -51.43293 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c8efc440-6cf5-30f2-8526-3d566f72c405 | -12.97267 | -51.41634 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| c25637c1-2f35-35f7-bc69-09ef3353bcc0 | -12.97216 | -51.41827 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 12.0 |
| a735d93d-fc07-3ab6-8d9c-77a76fc32b02 | -12.97161 | -51.42226 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 809eaba5-c3f3-3df5-a616-b9c9154d252f | -12.97052 | -51.43023 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 38457a61-ab4d-3e28-90bc-048b3082c0a0 | -12.97007 | -51.43631 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5dbf96b8-5bd7-36e5-95a9-504d132bbc6b | -12.96997 | -51.43422 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5d8e4081-d197-38cd-af76-5b23d320e974 | -12.9674 | -51.42371 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 37d5658e-e8be-3708-8277-5310b1776faf | -12.96739 | -51.42165 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 65b56e04-6daa-35e8-b823-1cc070843e05 | -12.96688 | -51.4277 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 08d2330e-a116-354c-ac74-4ef0502c6265 | -12.96684 | -51.42564 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0fd76e42-047a-306e-8e36-b0366c81d213 | -12.9663 | -51.42963 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 22bd31c6-a6df-3985-852f-3c2ca036f660 | -12.96533 | -51.43969 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 56ec0106-4463-31a9-904e-9c07deca8f24 | -12.9652 | -51.4376 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d144ac24-5e4b-342d-8919-5f0ba87edfe5 | -12.96293 | -51.35966 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ca01d4f0-d335-3f85-acc8-3aecb5716d36 | -12.96266 | -51.42709 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| a0271a24-0d0b-3360-b26f-48f8c66f8b0e | -12.96111 | -51.43908 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5bc64cc0-9b8f-3ad5-a096-6fadadfb7d63 | -12.96059 | -51.44307 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 44eff427-b62f-3f68-9bb9-361679dc2471 | -12.96043 | -51.44098 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 110b027c-7f83-37b1-9b4a-8ce8e3c14d56 | -12.95924 | -51.35501 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7673a014-c247-3945-86ff-d58964948bc3 | -12.95895 | -51.42044 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 66b1d228-2160-3fc1-b94c-e7518d7e4cdc | -12.95567 | -51.44436 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 85a68120-a25f-3eb2-a807-504f2e240778 | -12.95513 | -51.44834 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b74595d6-6b9f-3122-8147-7ac44d4183e1 | -12.95418 | -51.42382 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 15.4 |
| b26e1f3d-595b-337d-96df-cfc72483a9c5 | -12.95363 | -51.42782 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 92de9caf-f2fb-367a-8d7e-f0eac3cf466a | -12.95037 | -51.45171 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 251e4ab1-df7a-323c-b229-3bd4e2182983 | -12.94996 | -51.42322 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 4472593f-a008-3bbd-aac0-124fdab48b5f | -12.94561 | -51.4551 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b4349b31-be15-32f5-85d0-6e61bd0d1f18 | -12.94465 | -51.43059 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 15b9dc3d-9aab-3245-a8ad-8c7312556f82 | -12.94411 | -51.43457 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.3 |
| e093aff8-0b92-331b-81af-3a23e346f8ec | -12.9414 | -51.45449 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9f573cef-4bc5-39b7-b693-2995cf066a51 | -12.94086 | -51.45848 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 35a9f922-160d-3b8a-9885-118a752a957a | -12.93989 | -51.43398 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.3 |
| c4ebb8ae-dc21-37d9-ab61-6d623088221d | -12.93719 | -51.4539 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 41020323-cdba-34e1-9598-9d224e3fc6c7 | -12.93665 | -51.45788 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7d8c8154-f83b-3021-8ba3-b96856acf45c | -12.93513 | -51.43736 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| b5664c81-96ac-3585-808e-05b279bb4ce7 | -12.9346 | -51.44134 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| e9ccd3f7-b245-3cfe-aa15-314c2d58c8ef | -12.93405 | -51.44533 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e00cd9b8-19ea-3993-bab8-d3c4c8ea1695 | -12.92509 | -51.4481 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 5da27da2-c2cf-3894-8de7-69e5e3db8da3 | -12.92455 | -51.45208 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f1252f89-725a-3448-84dd-c89765c8ead0 | -12.92034 | -51.45148 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9c1bda91-65da-3463-a61c-2c660a4a2157 | -12.91873 | -51.46341 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b9b44191-f5a1-30da-aaa0-83bc7e93fa60 | -12.72245 | -51.93148 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4d9915db-73fa-3be5-9794-57e296ee4768 | -12.7204 | -51.91589 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 3d5218b3-0e13-33c8-be24-311682973e95 | -12.71939 | -51.92341 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 58fcf81d-3a90-3cf5-80d2-823782b90491 | -12.71888 | -51.92715 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| af82ca1e-092a-3906-874b-efaaa7d1141a | -12.71633 | -51.91527 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 32f69914-6e44-37bc-bc43-f53465a11956 | -12.70907 | -52.03024 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 73f65b7c-3d3a-3c90-b183-d60440fb2079 | -12.57974 | -51.91139 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f3c26a60-4710-37ef-860b-c1243d104519 | -13.25012 | -51.24138 | 2024-10-01 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3254c2de-02d9-3b92-a701-c9a0f6f42e95 | -13.24958 | -51.24554 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 02012df7-e15a-384f-98d0-966f7a0838d6 | -13.24638 | -51.23662 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 42e0e982-cc09-3a45-b3fa-6781bb7c02e1 | -13.24583 | -51.24078 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5556a5f1-40eb-3f08-9685-847af67d2a5c | -13.24208 | -51.23602 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ef334471-2d43-3cbb-8d5b-74c70ba0d016 | -13.23778 | -51.23543 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e65924f2-2470-3ebf-a745-e75f830a4da2 | -13.23724 | -51.23957 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9c016666-06ee-3336-b9c7-da9890713772 | -13.23457 | -51.22652 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 84265185-cc56-3e5d-8ad6-174d905dcdb9 | -13.23403 | -51.23067 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fb002cfc-839f-3712-803b-e15c5d437557 | -13.23349 | -51.23481 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 182fad25-93e8-391c-8805-a5058eba045d | -13.23027 | -51.22591 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d557cfcc-98e2-37dc-81aa-d02531de0195 | -13.22974 | -51.23006 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 016c9eb2-1c02-3b5a-879a-7889433d96fc | -13.22652 | -51.22113 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| bcc3360d-8480-3eda-8428-c8e6ea20525c | -13.22598 | -51.22528 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d56d680a-bc8b-3739-8a4c-09f4a46e3e03 | -13.22544 | -51.22944 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4615bcec-f566-3ba2-ab3c-b2ff6c95d068 | -13.22276 | -51.21635 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4d9253b8-14ec-3d2f-85ee-046db21c7d6c | -13.22222 | -51.22051 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a607839d-46de-343a-8be4-87ea3ea30155 | -13.22168 | -51.22467 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fb979324-8021-30db-95c6-f279dc6cc2e8 | -13.21846 | -51.21574 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 53056303-1ac5-3800-bac2-ca82f7495777 | -13.21793 | -51.21989 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 30a42445-7d9b-3031-9fe8-4841791952f7 | -13.21542 | -51.21759 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 96da6a25-8eab-3cda-88f1-073c2ddfb464 | -13.21416 | -51.21512 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 21a11d16-50b7-3142-8c58-80aebf72b0dc | -13.21363 | -51.21928 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 833bb7b4-81bf-36fb-9f70-2e45a95a2232 | -13.21112 | -51.21698 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 118d0966-269f-3255-88fe-bde7d4fa071d | -13.20987 | -51.2145 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 7039d3c8-e609-36c4-9a00-d60bdc3fdb0f | -13.20683 | -51.21636 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ddcd52ff-9c4c-3078-844c-7e4928778af6 | -13.20557 | -51.21387 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| a6402d4b-10d2-38fd-bf12-73a9c261631c | -13.20253 | -51.21574 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f25c6729-4d81-33b3-b1ef-30491097a18e | -13.20197 | -51.21988 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README110.md)

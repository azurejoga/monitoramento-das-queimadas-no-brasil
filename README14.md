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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0f567c52-9e14-3bfe-9d10-72e32ef6e48a | -5.84774 | -48.38981 | 2025-07-12 05:06:00 | NPP-375D | PALESTINA DO PARÁ | PARÁ | Brasil | 1505494 | 15 | 33 | nan | nan | nan | Amazônia | 38.3 |
| c49be051-c30a-3009-86ea-30c86a53a8f3 | -6.62765 | -56.27766 | 2025-07-12 05:06:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6cc58d3b-0f97-37cd-8d9a-cd8940eb6d76 | -5.78403 | -45.10923 | 2025-07-12 05:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 27b0da7a-e085-3977-ad3b-e478a1a6d677 | -7.8692 | -56.62226 | 2025-07-12 05:06:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3077220c-95a2-3d22-93ad-9c4a81aaf146 | -5.84709 | -48.38834 | 2025-07-12 05:06:00 | NPP-375D | PALESTINA DO PARÁ | PARÁ | Brasil | 1505494 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| dc27abf6-f5b0-3075-a46d-e6d0b46c5e86 | -6.62932 | -56.28863 | 2025-07-12 05:06:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 02f428a4-4672-349c-8cb6-e56b155e6419 | -8.52836 | -54.77182 | 2025-07-12 05:06:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dd8861f5-52c7-3df4-985c-dc6e5769f485 | -6.42565 | -48.53483 | 2025-07-12 05:06:00 | NPP-375D | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b0bd3405-8abc-3680-bd73-a9819a702225 | -6.60846 | -43.88498 | 2025-07-12 05:06:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 6158a747-7432-32a0-bfb6-19c754941ee3 | -6.61308 | -43.88967 | 2025-07-12 05:06:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ef01e528-d0c5-311d-979d-b6aa118148fa | -8.68682 | -47.99292 | 2025-07-12 05:06:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7fcc55c2-2a0a-3c47-9915-14e72b5e54b9 | -5.78602 | -45.10529 | 2025-07-12 05:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 61762d6a-c260-379e-927c-5892bdfc85f4 | -5.78016 | -45.10435 | 2025-07-12 05:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 42a03fe8-23ca-398d-b242-3d4f7e665376 | -5.78458 | -45.10519 | 2025-07-12 05:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f2b1667c-af69-3d16-87ed-16cc08a31ac4 | -9.91541 | -47.82994 | 2025-07-12 05:06:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8ffe8aef-4d93-30f3-a70a-8a9030fab9f1 | -9.91502 | -47.83299 | 2025-07-12 05:06:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 326ef68b-5084-3cc3-beca-c79f822bd089 | -8.69055 | -47.9895 | 2025-07-12 05:06:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 72812ed3-f310-3354-be40-6121bf347041 | -9.51333 | -47.56503 | 2025-07-12 05:06:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e953023b-40c7-373f-ad79-119eaa12325b | -5.84236 | -48.38774 | 2025-07-12 05:06:00 | NPP-375D | PALESTINA DO PARÁ | PARÁ | Brasil | 1505494 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 0d4e0be6-1509-3646-9c42-5045e07198b1 | -8.6855 | -47.9887 | 2025-07-12 05:06:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6b0d73b2-29ac-317b-8566-6f8e5fde02aa | -5.78544 | -45.10934 | 2025-07-12 05:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 67794e28-01f1-323b-a999-95bf66fa6139 | -3.87134 | -54.23211 | 2025-07-12 05:06:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| f9979466-da2e-3e7b-a96b-54eb3ecbce72 | -3.19372 | -60.60331 | 2025-07-12 05:06:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 86211ba1-a718-3d57-83f2-b35b8e0d962b | -3.86799 | -54.23159 | 2025-07-12 05:06:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 8fa80b11-53db-38b9-bb7f-a46b0c212053 | -7.98451 | -46.41889 | 2025-07-12 05:06:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 527dd279-e875-3283-8fda-4468ec21d334 | -7.21617 | -43.10102 | 2025-07-12 05:06:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d37b684e-8952-373d-ba91-a0b56a6ffaf4 | -6.25081 | -43.36392 | 2025-07-12 05:06:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4be5556a-1a19-3626-bdc5-51d856eb56ef | -8.53175 | -54.77234 | 2025-07-12 05:06:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f5751e9d-80c0-3fe0-a8de-8701ae3ce082 | -7.22192 | -43.10256 | 2025-07-12 05:06:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 835bba69-8c76-300e-bceb-8d95f1dacba8 | -8.52498 | -54.77129 | 2025-07-12 05:06:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9d6019c0-d85e-3021-b4db-41c8aaf1713f | -7.90424 | -61.51368 | 2025-07-12 05:06:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| adb41f9e-6350-34ec-aed3-b1c86935fecc | -6.6332 | -56.28567 | 2025-07-12 05:06:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 51741f7a-ba17-3ca8-9425-bbb314729aae | -5.78486 | -45.11339 | 2025-07-12 05:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9ddab89d-dbce-37b8-8e22-3d0a1992c045 | -6.20558 | -55.63159 | 2025-07-12 05:06:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 933d7e05-637a-3160-8435-2605ccbd50f9 | -7.99567 | -46.42023 | 2025-07-12 05:06:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f4df764b-10ff-3600-9a40-de522bffd21e | -8.47152 | -49.61801 | 2025-07-12 05:06:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 70c3f718-34cc-379e-a7ed-835f22a99ee8 | -7.98646 | -46.40429 | 2025-07-12 05:06:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7fa1a372-9a32-3734-916e-967527e95a6e | -8.68512 | -47.99162 | 2025-07-12 05:06:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d16d6607-bab2-36a0-8fef-d7e7d543d0d0 | -5.84636 | -48.39326 | 2025-07-12 05:06:00 | NPP-375D | PALESTINA DO PARÁ | PARÁ | Brasil | 1505494 | 15 | 33 | nan | nan | nan | Amazônia | 32.4 |
| 2955de10-a1f8-316b-8284-6bc8b4904bfe | -6.63264 | -56.28915 | 2025-07-12 05:06:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1a947f81-4be0-3140-9bd2-2a45b79a6f44 | -7.90312 | -61.51057 | 2025-07-12 05:06:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 84195af4-150b-31b7-aa4e-fe68ebc3d60c | -5.78427 | -45.1175 | 2025-07-12 05:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ab97d06f-33d0-3c0a-883d-ace1db8b3476 | -8.47083 | -49.61471 | 2025-07-12 05:06:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 06985122-1587-3f55-a3ef-8c49b756aa3f | -6.60775 | -43.89027 | 2025-07-12 05:06:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 88bf2740-8ee5-3365-8b47-edd4a8769178 | -8.04188 | -50.10228 | 2025-07-12 05:06:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8d4b1b04-11e0-34be-ad46-d897e1488dc0 | -7.84532 | -56.66502 | 2025-07-12 05:06:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0d3abb45-c7d9-3b27-ab60-7d37dfbafb8c | -7.18148 | -56.71701 | 2025-07-12 05:06:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 079c6164-2da4-311e-933a-44cf10fb288a | -9.51859 | -47.56581 | 2025-07-12 05:06:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 44f7cb1b-09dc-3a4a-93a8-10e101093efc | -7.21514 | -43.10156 | 2025-07-12 05:06:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 1b2eaea2-aac1-3dd6-bc5e-8f0b585c0051 | -5.78934 | -45.11427 | 2025-07-12 05:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ce6adfb3-70ed-3a98-b91c-a4ce2070c793 | -8.71974 | -47.16413 | 2025-07-12 05:06:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3aed6f84-6e3f-3a68-8b4c-4728a1580230 | -9.27376 | -46.6116 | 2025-07-12 05:06:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 72b0c26f-facc-3420-9f56-49250147734c | -9.2677 | -46.61438 | 2025-07-12 05:06:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1f85a6f6-5cad-353a-b69c-fde9caddc789 | -7.59574 | -63.47342 | 2025-07-12 05:06:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dd2773a8-0e6e-3fbd-9d16-2ad9bcd48c2f | -7.94861 | -49.65846 | 2025-07-12 05:06:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 71e45014-accc-3170-8434-5096152545e4 | -4.11853 | -54.91672 | 2025-07-12 05:06:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 36697508-0308-3d64-9207-52292d333534 | -7.66947 | -56.75157 | 2025-07-12 05:06:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 32798447-c15e-3534-b4c6-0f49d3e4a0c2 | -8.84519 | -50.49279 | 2025-07-12 05:06:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 997e15cf-403d-3191-b267-8942842049b2 | -7.97887 | -46.41865 | 2025-07-12 05:06:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9fe40d04-aeb5-39e4-a4df-ed8f60537567 | -8.75339 | -43.95468 | 2025-07-12 05:06:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5ee1e5fc-d49f-3c22-b6a5-d2556aa3c94a | -8.30578 | -55.1097 | 2025-07-12 05:06:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8b030072-e9be-3795-bf9a-a8d3fec41fbf | -7.90489 | -61.50994 | 2025-07-12 05:06:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4cbf3749-5484-30c8-a5e0-0b43f5f31a07 | -8.75267 | -43.96041 | 2025-07-12 05:06:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f4f04d8a-63d3-3269-b2a5-9c83bd3efca6 | -9.27327 | -46.61531 | 2025-07-12 05:06:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8cf8b572-6c53-3c85-a924-ce39911ee2eb | -12.99809 | -46.2723 | 2025-07-12 05:08:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4da6f02e-3ea7-3ac6-a304-f82f8bc08e0b | -10.22907 | -56.76469 | 2025-07-12 05:08:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5c3ed9a5-926a-330a-8494-d9247de5dae3 | -9.64599 | -65.74245 | 2025-07-12 05:08:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cd35d270-c6ed-3e90-9948-030cda4f08c1 | -11.88176 | -58.71664 | 2025-07-12 05:08:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a2c6773a-b451-365f-8e80-3cab72c028b6 | -11.84012 | -47.51134 | 2025-07-12 05:08:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| ec0d64be-26b6-3c6a-808a-5f6c1f1675f6 | -10.13167 | -57.78197 | 2025-07-12 05:08:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7d9d540c-dc52-383e-a1be-6ab7321f4329 | -12.40792 | -45.34998 | 2025-07-12 05:08:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8da39882-edd2-3e65-8ce2-22e75dce9664 | -12.42058 | -45.35132 | 2025-07-12 05:08:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 13fd34bf-951e-32ae-a601-7a8fda083425 | -10.69557 | -48.30503 | 2025-07-12 05:08:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9e3306cb-402c-3e8b-9cf6-08c09289a6a3 | -10.57428 | -49.12731 | 2025-07-12 05:08:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 21.3 |
| e240cb9b-e625-310c-9f4f-15cb1dbc66e8 | -10.90392 | -49.20399 | 2025-07-12 05:08:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| dcd5cbed-d3a6-34c5-a01c-27150c83d38a | -12.41775 | -45.35577 | 2025-07-12 05:08:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 99c1234b-165c-3209-851f-c0ab23baa282 | -12.60832 | -48.37006 | 2025-07-12 05:08:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f4f2d328-4210-3c66-86a0-fe25a0d402b5 | -11.9468 | -49.29502 | 2025-07-12 05:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 474c8d1d-c7e1-39a1-b5da-3fcc13175e66 | -11.27334 | -46.40572 | 2025-07-12 05:08:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 859854ce-a865-3b9b-ae6c-abd3c1cdb1da | -11.4273 | -46.40332 | 2025-07-12 05:08:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f63c910c-2641-3186-afb4-ea8df63b675b | -13.12488 | -47.3124 | 2025-07-12 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e8653859-1a92-322a-b46d-1db7757d0faf | -11.86256 | -58.7058 | 2025-07-12 05:08:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fa8f2a6f-4989-3a07-882d-945a91b43082 | -9.02689 | -61.23188 | 2025-07-12 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 91238ea9-7596-324d-a905-e07677faec5c | -11.60548 | -47.61462 | 2025-07-12 05:08:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 03a7971d-6029-3d39-a612-47f8f3395104 | -10.68976 | -48.30992 | 2025-07-12 05:08:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| edb0413f-32b4-33d5-aa9a-283d654ac77d | -14.4296 | -58.71809 | 2025-07-12 05:08:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 390f3753-fac8-3fc8-8cb1-142c510108d6 | -11.88088 | -58.74332 | 2025-07-12 05:08:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b9faeb38-3079-3667-a963-0698d6204561 | -11.72794 | -47.47568 | 2025-07-12 05:08:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d425d56a-c1d5-3d27-9bca-4e5d59576580 | -12.42002 | -45.3564 | 2025-07-12 05:08:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 182464b0-2e01-30e1-a91e-38c6364d758c | -11.72884 | -47.46818 | 2025-07-12 05:08:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c08263df-8b04-36f6-b778-0206f15bf872 | -11.73354 | -47.47364 | 2025-07-12 05:08:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 55cb9a06-8de2-3492-9b49-2a7e5313b355 | -13.14222 | -47.31062 | 2025-07-12 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1490f78c-1e2a-3c87-a7b8-866bc63d931d | -10.22851 | -56.7682 | 2025-07-12 05:08:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| beb2f5cd-5402-3f57-a990-dfc1e54931cf | -11.72927 | -47.46462 | 2025-07-12 05:08:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 878e5a09-d064-34ab-b949-525cf17e7016 | -12.49269 | -51.27684 | 2025-07-12 05:08:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b1647c2f-289b-35d5-ae0c-30d75cb94100 | -11.49571 | -48.07723 | 2025-07-12 05:08:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 270be435-49e9-3192-9940-93b1bfcb7cea | -13.01994 | -47.82562 | 2025-07-12 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1d64b9e8-c3fc-34c1-985a-319782379481 | -11.93009 | -51.69342 | 2025-07-12 05:08:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 68da89bd-8b07-3aab-b7a1-a6dc6f80252d | -11.86992 | -52.25593 | 2025-07-12 05:08:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c83c1e2b-c7f5-39ed-bbbd-abc56eab6b12 | -11.73517 | -47.46178 | 2025-07-12 05:08:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |


[Clique aqui para ver as próximas entradas](README15.md)

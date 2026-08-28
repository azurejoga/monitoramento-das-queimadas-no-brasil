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

## Dados Diários - Página 115

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ca0392b0-0cd3-31cc-83c5-2f1694d124fb | -14.43989 | -53.38123 | 2026-08-28 17:26:00 | NPP-375 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 45a0543c-5d04-3964-82cd-2f51e9536397 | -6.43761 | -55.7746 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 6c3551d7-f2aa-3933-9cad-c46e88c52ef5 | -6.75122 | -55.68098 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 21.9 |
| 4ed4dd18-5106-39e9-bcad-17b1793d15d9 | -8.60612 | -54.7152 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| f5869b0f-4ec3-3fde-879a-7d6371a07206 | -6.42947 | -55.52166 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| f0bbe238-0641-359c-bef3-ff72cec6fe5d | -3.70643 | -45.25333 | 2026-08-28 17:28:00 | NPP-375 | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 11.6 |
| af88a653-9a7d-33a0-a84c-caa62550ccbf | -7.59395 | -61.35414 | 2026-08-28 17:28:00 | NPP-375 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 3bf4bc23-2ff5-349b-997d-298ba71f4a8a | -9.19375 | -59.56624 | 2026-08-28 17:28:00 | NPP-375 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.6 |
| b0fa30ad-0c6b-307d-b27a-38a41ecc4dbf | -9.92185 | -60.4375 | 2026-08-28 17:28:00 | NPP-375 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 73.9 |
| badda145-f561-32ae-995e-4abfa9608d0b | -6.12438 | -53.74276 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| cbca474a-e5d0-35be-a240-f25aff64de2f | -6.89978 | -43.64677 | 2026-08-28 17:28:00 | NPP-375 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 4d42f255-69f7-33c6-8eb0-dacdabefae61 | -7.37035 | -55.51173 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 5227e806-2ba3-307b-aa67-9fb11936dcdd | -9.68044 | -55.08749 | 2026-08-28 17:28:00 | NPP-375 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| c15688c3-5880-3bcb-bb1c-8e3c7ee780a0 | -5.99401 | -57.67997 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 5e6d011b-f11b-3c26-8129-33c934619229 | -9.40696 | -60.56939 | 2026-08-28 17:28:00 | NPP-375 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 249e1261-c68b-3a1c-8778-fbbc2988fe19 | -10.47688 | -64.48619 | 2026-08-28 17:28:00 | NPP-375 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 11.9 |
| a9736709-bf16-35ef-9831-8cb0e50f13e2 | -9.17298 | -65.92735 | 2026-08-28 17:28:00 | NPP-375 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 208f7de4-def6-353e-b63f-84466d6b7b71 | -6.07381 | -57.65278 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 61cd7daf-1a43-332b-817e-751474e828d9 | -8.04178 | -51.79831 | 2026-08-28 17:28:00 | NPP-375 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| d7b04d59-89ac-3c1f-9f82-4a8a0629cc9d | -10.76011 | -54.03233 | 2026-08-28 17:28:00 | NPP-375 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 26.6 |
| 5076fe3f-a7d0-3548-91f5-e0f7f264f087 | -10.39565 | -61.2023 | 2026-08-28 17:28:00 | NPP-375 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 9581d557-06c6-335e-b917-e6852e726c8a | -9.68606 | -55.07926 | 2026-08-28 17:28:00 | NPP-375 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e8a84782-a11d-30fe-8dbf-0e65bfa73b53 | -10.31884 | -68.4609 | 2026-08-28 17:28:00 | NPP-375 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 3936d543-082d-3eed-8756-0d861ee13e38 | -6.79861 | -43.55825 | 2026-08-28 17:28:00 | NPP-375 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 9.8 |
| ea06df45-4707-34b4-a6e7-de57891835b4 | -6.89838 | -43.64259 | 2026-08-28 17:28:00 | NPP-375 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 8773e237-1afd-364f-b80f-7b17217d8e3c | -6.27122 | -53.1418 | 2026-08-28 17:28:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| f87a4ff9-49b0-35a6-a654-41f76aad277b | -6.38734 | -57.46791 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| b4c8992c-79ad-3e5e-af76-456df98d377d | -9.92253 | -60.44235 | 2026-08-28 17:28:00 | NPP-375 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 2455532b-14c5-3dab-814e-5c75664858a9 | -6.11086 | -52.78868 | 2026-08-28 17:28:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 6f9be89f-f57b-3e5c-823c-31ae1ecfd013 | -7.92002 | -50.95369 | 2026-08-28 17:28:00 | NPP-375 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 904665eb-b193-34a5-ae7c-e16fb75c2c77 | -4.47882 | -55.40316 | 2026-08-28 17:28:00 | NPP-375 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 30.6 |
| 59b2df91-839c-3bae-9d32-e3242a14d449 | -7.28466 | -49.95435 | 2026-08-28 17:28:00 | NPP-375 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| a7e032b3-7145-300b-8558-89ac9058133b | -6.7625 | -59.15043 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| ecf738ba-4db9-3736-b685-bf5172391eec | -6.76776 | -59.45182 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| e7a1c834-ecd1-3c5a-a8fa-7c096ba822fc | -9.21017 | -65.86839 | 2026-08-28 17:28:00 | NPP-375 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f175726e-e37b-32ef-b0a1-06c81d4dc2c7 | -6.86282 | -60.07531 | 2026-08-28 17:28:00 | NPP-375 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 14.5 |
| db64d623-b7e9-32de-bacb-9479debbeac9 | -7.61997 | -44.81413 | 2026-08-28 17:28:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 247923e9-1716-3d03-88c7-6185b954e34c | -7.57957 | -61.30987 | 2026-08-28 17:28:00 | NPP-375 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| f3d66fff-1092-34eb-ace8-f18f4584f86e | -9.06055 | -45.91381 | 2026-08-28 17:28:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 10.2 |
| c6e8285a-50d6-3e25-8e19-1b8ec2fd74b0 | -7.36535 | -55.16758 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 45dbad79-02ff-37cb-b0a5-01e74fa81330 | -4.96437 | -44.89161 | 2026-08-28 17:28:00 | NPP-375 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 65.7 |
| be6a220a-d856-33bc-b9fb-e3adbe472cda | -2.92288 | -45.23076 | 2026-08-28 17:28:00 | NPP-375 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 0a08eca7-7aa4-3543-bc67-7fb678f922cc | -7.59123 | -63.36077 | 2026-08-28 17:28:00 | NPP-375 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 11.4 |
| bc150be3-c21e-3c77-89df-45f3e6f697a3 | -5.87877 | -57.76959 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 140.5 |
| 91956b6b-b024-3753-8c25-65de3ffb040e | -10.75951 | -54.02853 | 2026-08-28 17:28:00 | NPP-375 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 21.0 |
| a53a3d20-73d2-34ac-82c1-7aae2014613b | -6.78346 | -56.63506 | 2026-08-28 17:28:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 835fad43-482f-3f82-b113-562929bb9db3 | -10.5075 | -59.63311 | 2026-08-28 17:28:00 | NPP-375 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 38.3 |
| effee9ca-f8e3-3c59-84bd-e6d4ce38d992 | -6.17379 | -55.46968 | 2026-08-28 17:28:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9ac19738-172f-3921-9ef7-07bedfe04b21 | -9.61512 | -55.12031 | 2026-08-28 17:28:00 | NPP-375 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 43fe5542-5033-3e6b-8c87-2d3df2ca301d | -8.9594 | -62.38477 | 2026-08-28 17:28:00 | NPP-375 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 36.5 |
| 4d4203e1-ba0b-38df-a102-f5a75e67f915 | -6.94877 | -59.48625 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 0903ce47-d057-3ea6-8f37-e90d083c1183 | -8.09603 | -51.65517 | 2026-08-28 17:28:00 | NPP-375 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 822bf3ab-53f3-3845-8760-e8c220df891a | -8.95548 | -45.73171 | 2026-08-28 17:28:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e183a675-63d6-3c87-bdcc-abc1e7a0ab0d | -1.9081 | -47.02112 | 2026-08-28 17:28:00 | NPP-375 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b947e5e7-a001-3e81-a7d7-93c929885499 | -7.59896 | -61.33273 | 2026-08-28 17:28:00 | NPP-375 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 6830b32c-41bd-3fdf-abf4-4ff6a882e375 | -5.29023 | -50.93644 | 2026-08-28 17:28:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 394a2f28-1206-355d-9e96-804986bdf1bc | -6.73395 | -55.45873 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| d874078b-56d8-3b3c-80e6-12e9b0b78d62 | -9.16882 | -59.57409 | 2026-08-28 17:28:00 | NPP-375 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 16.3 |
| f558fb08-d2fd-3edc-b028-8ea8660e9393 | -6.25192 | -57.51409 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 2cb00bd8-7206-3252-b0cd-bb7841b09b40 | -6.82732 | -55.60967 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 35.5 |
| 0252cc59-7bfd-3f30-969e-f545f8ec1776 | -6.17662 | -55.46551 | 2026-08-28 17:28:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 8aadb46a-23eb-39c9-8395-55713047d5b5 | -5.82113 | -52.32822 | 2026-08-28 17:28:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 0736ed1b-4c98-3450-8951-1560981d85ac | -9.05939 | -58.99377 | 2026-08-28 17:28:00 | NPP-375 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| a00e36b2-a86a-3d74-973b-9649e9cde742 | -10.75098 | -54.04156 | 2026-08-28 17:28:00 | NPP-375 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 139.5 |
| 0a70a213-2176-3200-a7eb-2b1b8a595228 | -10.48747 | -64.48777 | 2026-08-28 17:28:00 | NPP-375 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 6441b50e-f189-36b2-901e-0967770c752b | -9.41151 | -60.57366 | 2026-08-28 17:28:00 | NPP-375 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| cb3f8504-0889-3296-9fbb-5c8de2af4982 | -7.93494 | -61.37104 | 2026-08-28 17:28:00 | NPP-375 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a7d51401-b548-32ad-9354-98706c92a1ea | -9.69684 | -65.08294 | 2026-08-28 17:28:00 | NPP-375 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ffe5bb51-f981-3864-8442-43f34e6edc61 | -8.99131 | -65.42545 | 2026-08-28 17:28:00 | NPP-375 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 20.7 |
| df0631ef-258c-3279-84b0-782aed0057b5 | -6.95232 | -59.48572 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 6f3f9614-a3a2-3d0d-b19e-f60e63c66b82 | -8.60596 | -54.77659 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 9a42d61a-744f-36c7-ad5b-220d02ebbde8 | -7.73989 | -61.06451 | 2026-08-28 17:28:00 | NPP-375 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 09979bae-4008-34b9-b961-4bc4dbe0b9ce | -5.81552 | -52.31869 | 2026-08-28 17:28:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| d713d860-597c-33b9-9a9e-0ffbc36fd9bd | -8.11297 | -51.65443 | 2026-08-28 17:28:00 | NPP-375 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| dc3b1f1b-477e-381e-b49b-40cc335a46e2 | -9.46708 | -51.69955 | 2026-08-28 17:28:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| c8ffff23-44b5-380c-b79d-a9cf553c826c | -9.46482 | -51.71013 | 2026-08-28 17:28:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| d4cb5c6c-8c5c-324a-b379-267f61be0355 | -7.00545 | -59.52685 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 42886964-14f0-3d6c-a216-e941fcae58d4 | -6.94551 | -59.48256 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c0d89877-8fe0-3bf2-890e-4550573ecbb7 | -6.33428 | -57.74165 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ade2ddb9-94e0-3651-a6a3-9263dad9c616 | -8.06825 | -45.88868 | 2026-08-28 17:28:00 | NPP-375 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 64bc109e-268a-38c6-be80-2080a080363b | -9.69446 | -65.10617 | 2026-08-28 17:28:00 | NPP-375 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e195f091-ce2d-3ffb-a2aa-15bbe4c6d84b | -7.48326 | -61.41911 | 2026-08-28 17:28:00 | NPP-375 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 16.7 |
| f37d3ed3-2884-3e64-b3ec-491af4339516 | -6.27804 | -53.1361 | 2026-08-28 17:28:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 33.1 |
| afa905d6-aa66-398b-a4a4-4726da81705c | -6.95319 | -59.48549 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 34.8 |
| 4820cf59-b858-33c5-957a-e2c1eaa536ad | -10.38841 | -61.24003 | 2026-08-28 17:28:00 | NPP-375 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 2aee66fe-f6e9-3657-8a0b-327ba235e9f9 | -10.2048 | -69.36483 | 2026-08-28 17:28:00 | NPP-375 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 24.3 |
| e7ec4430-9030-3139-8768-3908094774f6 | -6.58126 | -55.44203 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| cce505ef-d11c-3852-b07b-1abbc86f0ef5 | -9.25532 | -57.07037 | 2026-08-28 17:28:00 | NPP-375 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 5504e559-9982-3922-aefc-0d9bdf1e1709 | -6.59994 | -55.45029 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| b8a06102-5009-3eb4-8837-4a4c5067dc49 | -10.387 | -61.19986 | 2026-08-28 17:28:00 | NPP-375 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9d4c3a7f-4801-3c5a-b592-e8fe90edfd03 | -8.64457 | -62.85138 | 2026-08-28 17:28:00 | NPP-375 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 16.8 |
| f35ed6c2-ebf8-3e1e-9535-0f39430e1123 | -4.92644 | -55.77089 | 2026-08-28 17:28:00 | NPP-375 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 6f1604a9-74bc-318c-8c8c-36ebdb0235af | -9.16945 | -59.57839 | 2026-08-28 17:28:00 | NPP-375 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 14.4 |
| cd3621f3-6cf8-37b2-a1a6-003c1c2fe402 | -9.11652 | -60.30666 | 2026-08-28 17:28:00 | NPP-375 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| a11d9277-8225-3006-80b1-290b3f0f3e84 | -9.6782 | -55.09517 | 2026-08-28 17:28:00 | NPP-375 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| fedc6127-6ce4-3b1f-8e13-9310a1e1c94c | -8.01806 | -48.01786 | 2026-08-28 17:28:00 | NPP-375 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8918550c-6800-3fe4-a371-cbd3f05fb16d | -6.59906 | -44.69602 | 2026-08-28 17:28:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| eda6fabf-a433-3f5c-be58-c6ab15c7767c | -6.73627 | -59.64765 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 20.8 |
| d5d1b875-d0c8-3e25-bd49-21f95e14d9f8 | -6.59541 | -55.44354 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 7b51aa8e-4ec5-35d6-a495-b5579d4e961e | -4.60193 | -54.87115 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |


[Clique aqui para ver as próximas entradas](README116.md)

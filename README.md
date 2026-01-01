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
| d0969581-54a3-3cb1-8507-efe39d818bc6 | -9.5631 | -44.603 | 2026-01-01 00:00:00 | GOES-19 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 06248bbe-5a15-3683-99c1-5ae37cb77c86 | -9.5821 | -44.6007 | 2026-01-01 00:00:00 | GOES-19 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 512dc763-ed2d-37b4-a0a6-3b48bd406b3b | -3.0269 | -50.506001 | 2026-01-01 00:05:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 351946de-d036-3d94-b530-b3d96ae2ec74 | -1.367 | -46.044601 | 2026-01-01 00:05:00 | METOP-B | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4b17e2e6-a68f-3e8d-b9aa-a253847816d9 | -0.9915 | -53.201401 | 2026-01-01 00:05:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5bb5a325-48cc-3859-9964-180e644886a2 | -1.0853 | -48.9305 | 2026-01-01 00:05:00 | METOP-B | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2c6428c9-1a24-350f-8576-d0ec0abe9e04 | -3.8588 | -54.201401 | 2026-01-01 00:05:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4f7daf6d-1f94-3388-8e25-6d4c05a10f7f | -2.5551 | -48.914501 | 2026-01-01 00:05:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3cfca6ed-6ed9-3e16-883f-df3b821eb97d | -3.0343 | -53.113201 | 2026-01-01 00:05:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c8f801b6-698c-3d5c-9abd-dce28e91b2d2 | -5.9251 | -43.382099 | 2026-01-01 00:05:00 | METOP-B | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | nan |
| 69504641-c826-3fe9-be08-567bf6956616 | -4.6304 | -47.9328 | 2026-01-01 00:05:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 924f8df3-e6b8-3729-9f3e-0e82ccc00fb0 | -3.0252 | -50.498299 | 2026-01-01 00:05:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d04fc758-8ffd-33d6-b195-63129b7441c9 | -3.032 | -53.102501 | 2026-01-01 00:05:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0b9dc3e7-2b3d-3087-96f7-3b60d446b9ce | -5.7125 | -49.082901 | 2026-01-01 00:05:00 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5c65baf5-d572-305c-a69d-179946219550 | -5.0474 | -43.595699 | 2026-01-01 00:05:00 | METOP-B | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fe732890-7f3c-3078-b22d-65c63946a760 | -2.0334 | -45.894901 | 2026-01-01 00:05:00 | METOP-B | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| acfa9ed0-13a6-3026-8f14-1124e1bb1a68 | -4.6289 | -47.925999 | 2026-01-01 00:05:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 78577bf5-af47-39e8-9630-67718507b874 | -3.3732 | -43.749001 | 2026-01-01 00:05:00 | METOP-B | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3bffdddd-78bb-3a3e-930e-a729dc683c87 | -2.5452 | -48.916698 | 2026-01-01 00:05:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1bc4a6ce-2f0d-3f78-a3ee-83b7b8ca0023 | -5.7195 | -45.026299 | 2026-01-01 00:05:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| eca66717-4077-3c8f-8d5b-5e6f05ac0219 | -1.4846 | -46.0182 | 2026-01-01 00:05:00 | METOP-B | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e9785096-1a81-3c48-95df-920f6e2c74f0 | -4.2534 | -44.124599 | 2026-01-01 00:05:00 | METOP-B | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4076e82e-c14a-3d58-9bf2-512927da443e | -5.527 | -47.660599 | 2026-01-01 00:05:00 | METOP-B | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 47527d2e-ad82-35b9-b9df-081b2c51183e | -1.4863 | -46.025799 | 2026-01-01 00:05:00 | METOP-B | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ed80c6ce-1a2b-3c17-98e3-cc457082e7f6 | -3.8616 | -54.214298 | 2026-01-01 00:05:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 66f56b78-a906-32a8-b8f9-495e6ca02bea | -1.3687 | -46.0522 | 2026-01-01 00:05:00 | METOP-B | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ca43ec6d-3ccf-3402-91db-bf9564e0b83c | -5.9272 | -43.391201 | 2026-01-01 00:05:00 | METOP-B | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | nan |
| b52aa059-26bf-3804-8011-93c04a8c189c | -5.7212 | -45.033901 | 2026-01-01 00:05:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b7baff1a-94de-3c09-bcc4-e81edb297b53 | -1.6045 | -53.370399 | 2026-01-01 00:05:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e4da4bf0-be82-3bb4-bbf4-5c632ac1d6a4 | -4.5249 | -48.652199 | 2026-01-01 00:05:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9ae6de01-ac57-3cde-8448-dde80003245a | -2.5567 | -48.921398 | 2026-01-01 00:05:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c7e3c527-4314-358e-adc8-eda7a43ba7ba | -18.6099 | -40.001999 | 2026-01-01 00:05:00 | METOP-B | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ab250f3d-8a36-3807-815e-ddadafd4827f | -4.7212 | -42.029202 | 2026-01-01 00:05:00 | METOP-B | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| dad66f20-6a35-379c-9367-7336a13a04e3 | -5.7141 | -49.090199 | 2026-01-01 00:05:00 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 18e8f932-7058-346f-a1e3-f37962065190 | -4.5233 | -48.645199 | 2026-01-01 00:05:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dc5b55cb-1743-3ed2-9ce6-df91ecb9641c | -2.1217 | -46.236099 | 2026-01-01 00:05:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d0b31b8c-397b-3557-81b1-8a72a7488fe9 | -20.237499 | -40.218601 | 2026-01-01 00:05:00 | METOP-B | SERRA | ESPÍRITO SANTO | Brasil | 3205002 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 6743e6ae-df34-3e90-9003-19bad46899c0 | -0.9892 | -53.191299 | 2026-01-01 00:05:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 36ed1cf3-6661-3f5b-b67f-7d13a16f4782 | -18.607599 | -39.992199 | 2026-01-01 00:05:00 | METOP-B | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 148e8207-3f16-3a07-9809-d035ac45c5de | -22.891701 | -43.709599 | 2026-01-01 00:05:00 | METOP-B | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| aefee34a-6d82-3e7f-9969-f05590a8ec94 | -9.5631 | -44.603 | 2026-01-01 00:10:00 | GOES-19 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 029a4875-5649-3a94-b2cf-4ac2e65fe684 | -9.5821 | -44.6007 | 2026-01-01 00:10:00 | GOES-19 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 94f54ed2-2e76-3383-a25d-be8cc6ae1efc | -9.5631 | -44.603 | 2026-01-01 00:20:00 | GOES-19 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 73.8 |
| def32d72-4419-3e69-a4f7-f6c18ef59cea | -9.5821 | -44.6007 | 2026-01-01 00:20:00 | GOES-19 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 69.2 |
| ac2c4d5f-f5a4-3610-bd5e-861478bf479d | -9.5821 | -44.6007 | 2026-01-01 00:30:00 | GOES-19 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 780df8f6-a1e2-3318-b0b1-f52d16f62ee2 | -9.5631 | -44.603 | 2026-01-01 00:30:00 | GOES-19 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 942de35f-5523-327c-b077-fa248f52dea9 | -9.5821 | -44.6007 | 2026-01-01 00:40:00 | GOES-19 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 385ca6cf-3e40-341f-8302-4d473529952f | -9.5631 | -44.603 | 2026-01-01 00:40:00 | GOES-19 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 38b668d6-fbba-31ef-8437-75cbc6905dc6 | -5.7255 | -45.039001 | 2026-01-01 00:44:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 65883422-f183-3cca-a91b-2c8c1fc9e541 | -3.8763 | -54.226299 | 2026-01-01 00:44:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2d7fc22b-384d-3aeb-a726-a7830d04e87c | -5.7232 | -45.029301 | 2026-01-01 00:44:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ca9b85d2-1852-3c74-9c11-7402cf07a2f2 | -5.7124 | -49.096901 | 2026-01-01 00:44:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c72b966f-078b-3ed7-8ba6-72c3d0f76305 | -4.5301 | -48.665401 | 2026-01-01 00:44:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 15ce450e-00c2-3897-aab5-932fbc3efaeb | -5.9308 | -43.397598 | 2026-01-01 00:44:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3ca2c64f-91d6-314b-9d8f-ae3e43f53714 | -1.9306 | -53.351501 | 2026-01-01 00:44:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 071d555c-7161-3b62-b75c-081da2da0366 | -3.8665 | -54.2285 | 2026-01-01 00:44:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1269c3df-62ab-3267-98de-c00b541339f4 | -1.6077 | -53.380402 | 2026-01-01 00:44:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6beb6c65-6e54-3a0e-a8c3-bc6935ac9d91 | -3.8644 | -54.219002 | 2026-01-01 00:44:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0d94bb04-8e5f-3a84-8301-e049e622d2f5 | -0.9919 | -53.2089 | 2026-01-01 00:44:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8e85b4b5-e062-3b2b-b1f7-cf5dc222c860 | -5.7108 | -49.09 | 2026-01-01 00:44:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 68350171-554e-327a-a274-ad1bfd232863 | -3.026 | -50.5163 | 2026-01-01 00:44:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c127451b-99d3-3939-a3be-523ce54196e9 | -2.5577 | -48.924702 | 2026-01-01 00:44:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4614dfea-479d-3c01-b2ba-2a8e6eb9421c | -1.3677 | -46.051601 | 2026-01-01 00:44:00 | METOP-C | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2fe9ba62-81c0-3b79-82de-2efbe080b831 | -1.6096 | -53.3885 | 2026-01-01 00:44:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cf0a63e9-d1c7-3d1a-9dfc-81385b9b2db8 | -1.9288 | -53.343399 | 2026-01-01 00:44:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1e47319d-a6c7-30f5-bbcb-ed1c56598311 | -3.0244 | -50.509499 | 2026-01-01 00:44:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0f8be6fc-f04a-3f3a-ac99-91eea71bb1a3 | -5.9279 | -43.385399 | 2026-01-01 00:44:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | nan |
| 44b8008a-0008-3295-8b2c-c18ef2a07917 | -4.5285 | -48.658401 | 2026-01-01 00:44:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8ac990bd-9c9a-3ae0-bccf-d2392ab8258d | -4.6302 | -47.937698 | 2026-01-01 00:44:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c7234c27-d246-3f92-800d-778113b658de | -17.28561 | -51.95048 | 2026-01-01 00:49:00 | TERRA_M-M | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 3b914c18-980a-3e8e-a5d1-14ce48e35640 | -14.63131 | -55.8175 | 2026-01-01 00:49:00 | TERRA_M-M | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 7bc21b1a-a1eb-32af-a38e-a9d5a2409ac0 | -14.51343 | -52.55002 | 2026-01-01 00:49:00 | TERRA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 75d84df2-acee-3253-b500-40f1bdf69802 | -14.64316 | -55.83609 | 2026-01-01 00:49:00 | TERRA_M-M | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c1d5d147-13f3-32ba-9345-524bd5139b63 | -10.31667 | -54.15885 | 2026-01-01 00:49:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c5d1a133-6857-3996-8b74-898d27660eb3 | -14.64053 | -55.81618 | 2026-01-01 00:49:00 | TERRA_M-M | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 2f677fe6-9b1c-3a5d-b2a3-cef9d0091e21 | -14.63262 | -55.82743 | 2026-01-01 00:49:00 | TERRA_M-M | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7c33a411-7115-3162-be34-a5f3ee61f48a | -10.93559 | -49.42454 | 2026-01-01 00:49:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| f168487b-347f-3bcf-827d-96c57b178c10 | -14.64184 | -55.82611 | 2026-01-01 00:49:00 | TERRA_M-M | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 7eca66a3-1fca-3322-aff7-957e2f2cba3a | -9.5821 | -44.6007 | 2026-01-01 00:50:00 | GOES-19 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 69fd724e-f99e-372f-82cc-99790ceb00f6 | -9.5631 | -44.603 | 2026-01-01 00:50:00 | GOES-19 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 64.8 |
| dc5c8b19-9e93-34c0-82ba-0d335139df8d | -5.70858 | -49.10594 | 2026-01-01 00:52:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 931d75e3-5f79-3e8b-9f51-dfc8dc5eb8e8 | -1.61222 | -53.39108 | 2026-01-01 00:52:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| ca973125-bc60-38d8-91a8-188edb14c5b2 | -0.99353 | -53.20893 | 2026-01-01 00:52:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| fa754a1d-91b1-3772-91d3-b706919e23af | -3.02092 | -50.51684 | 2026-01-01 00:52:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 54c98e27-0caf-34f1-ae0d-d5a867d67011 | -3.87174 | -54.23051 | 2026-01-01 00:52:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 35.0 |
| b1871a1b-64d0-3cc5-af85-ae03f031221e | -0.9952 | -53.22098 | 2026-01-01 00:52:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 8ceddb0d-bf12-374f-bd89-864ab442e343 | -3.87312 | -54.24026 | 2026-01-01 00:52:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| c48107a7-34f7-3980-9d78-18e1daf341dc | -1.60137 | -53.38667 | 2026-01-01 00:52:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 6dfbc612-5647-344a-a68e-812053e5edc0 | 3.54527 | -60.86032 | 2026-01-01 00:54:00 | TERRA_M-M | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 1406cc72-af38-3100-9f59-db296773b6ac | -9.5821 | -44.6007 | 2026-01-01 01:00:00 | GOES-19 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 54.0 |
| b17030f3-f727-3396-8fe0-2eef8939c34a | -9.5631 | -44.603 | 2026-01-01 01:00:00 | GOES-19 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 49.7 |
| 5cc9e0c6-d3a0-3868-a9b2-38407fdb6604 | -9.5821 | -44.6007 | 2026-01-01 01:20:00 | GOES-19 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 50.3 |
| de54e1d8-e08a-31d8-b606-2017c6ffb43b | -9.5821 | -44.6007 | 2026-01-01 01:30:00 | GOES-19 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 48.3 |
| c4844ed3-925a-35b4-b5b1-b3a3015ddeea | -9.5631 | -44.603 | 2026-01-01 02:50:00 | GOES-19 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 42.3 |
| 510d66df-cb52-346a-bdf7-8bd3c86e75d0 | -6.14222 | -35.14952 | 2026-01-01 03:04:00 | NOAA-20 | SENADOR GEORGINO AVELINO | RIO GRANDE DO NORTE | Brasil | 2413201 | 24 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| e6852763-ed3f-36de-94be-3d7aab4fa5ab | -6.14395 | -35.14957 | 2026-01-01 03:04:00 | NOAA-20 | SENADOR GEORGINO AVELINO | RIO GRANDE DO NORTE | Brasil | 2413201 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| c2655d45-df2d-321d-87a0-537d9b66156d | -6.59632 | -35.1876 | 2026-01-01 03:06:00 | NOAA-20 | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 14e0d18f-d111-37bf-8451-d14795c3c716 | -6.59694 | -35.18411 | 2026-01-01 03:06:00 | NOAA-20 | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| acf28877-ba9d-3f12-ac34-84fd05ad32fe | -6.60301 | -35.18115 | 2026-01-01 03:06:00 | NOAA-20 | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| b2596923-f304-324e-8fe4-6b1defe4b356 | -6.55362 | -35.30146 | 2026-01-01 03:06:00 | NOAA-20 | JACARAÚ | PARAÍBA | Brasil | 2507309 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |


[Clique aqui para ver as próximas entradas](README2.md)

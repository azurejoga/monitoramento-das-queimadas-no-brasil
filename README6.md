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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 150e5251-a72d-3f4d-bfba-392d91e8dc24 | -4.7021 | -46.4064 | 2025-11-08 01:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 115.7 |
| 3ec36fa7-bf55-308a-af8c-bdb9b8074d0d | -4.4633 | -43.2152 | 2025-11-08 01:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 123.3 |
| ee920bc3-a427-3236-bfb3-a7999cbe3b1a | -3.3463 | -50.2189 | 2025-11-08 01:20:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 0ea8c0de-4784-38e3-97da-8a994d393573 | -3.4058 | -45.4424 | 2025-11-08 01:20:00 | GOES-19 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 88.4 |
| 4cd65647-08f5-39f6-b213-62545c2fff9d | -5.1535 | -41.2226 | 2025-11-08 01:20:00 | GOES-19 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 143.0 |
| 61b2fab3-d612-3c02-8e40-d1825075fcfc | -20.1886 | -47.397 | 2025-11-08 01:20:00 | GOES-19 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 142.1 |
| e6255c56-7ff6-3e71-beed-d8c84bf3dc12 | -4.6837 | -46.3852 | 2025-11-08 01:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 697645ad-6eac-3f96-b532-6474cf9e970a | -20.25 | -47.3827 | 2025-11-08 01:20:00 | GOES-19 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 0377e444-582c-36a1-ac6b-a89844ac9671 | -19.91556 | -57.31492 | 2025-11-08 01:28:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.9 |
| 9c4d649a-ee59-37d2-8b09-00785d7b98d5 | -3.4058 | -45.4424 | 2025-11-08 01:30:00 | GOES-19 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 89.1 |
| ee830ced-dc22-312a-a4b2-9718b1b9a79f | -4.6835 | -46.4074 | 2025-11-08 01:30:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 160.9 |
| 2c42a98e-b45a-305e-a673-d414293bb070 | -4.7021 | -46.4064 | 2025-11-08 01:30:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 53921588-6b7a-3a1d-bd12-7803ed925532 | -20.1893 | -47.3735 | 2025-11-08 01:30:00 | GOES-19 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 98.6 |
| e4c1517e-4a5e-3547-b2a5-d7e7e32efc77 | -3.3464 | -50.1979 | 2025-11-08 01:30:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 87714ed8-5095-321b-9e6f-42ee70223d96 | -10.2789 | -67.2815 | 2025-11-08 01:30:00 | GOES-19 | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 63862d87-c363-3987-9a6f-bf6228010c90 | -20.1886 | -47.397 | 2025-11-08 01:30:00 | GOES-19 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 106.9 |
| a8678692-7c95-3bed-8e5d-21b6b5390cb1 | -3.3463 | -50.2189 | 2025-11-08 01:30:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 29d9d0df-79af-377a-8d51-818a1242f402 | -4.6837 | -46.3852 | 2025-11-08 01:30:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 713f3483-5024-394a-8b5a-6198f59b7ec6 | -4.4633 | -43.2152 | 2025-11-08 01:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 88.5 |
| e13a58d5-b479-3bfd-9641-6057309a4da2 | -14.86302 | -59.42669 | 2025-11-08 01:30:00 | TERRA_M-M | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| e787a43d-8cf9-3e03-9ad7-8ee6b2a9c44d | -8.61376 | -63.52428 | 2025-11-08 01:32:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d6bbb8c0-d15a-37e3-89b3-ec4229cf5e0a | -9.50665 | -66.77145 | 2025-11-08 01:32:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 278c6f4d-76ec-3d86-a33f-235d8668f81a | -9.62759 | -68.60194 | 2025-11-08 01:32:00 | TERRA_M-M | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 15.6 |
| c21abcf4-4551-35a9-b263-f363e7f4eefd | -9.07843 | -61.69491 | 2025-11-08 01:32:00 | TERRA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 8004cdc1-5cda-3e7e-8775-a24a284c18c5 | -8.56591 | -67.00928 | 2025-11-08 01:32:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 707fa652-9852-3013-9114-44abe97e7a3d | -12.44095 | -63.1577 | 2025-11-08 01:32:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 292423b7-6527-37f2-a608-eea37cd79c18 | -10.0675 | -63.0541 | 2025-11-08 01:32:00 | TERRA_M-M | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 200dadb6-643d-3982-b66c-7b1fe92ea2f0 | -11.76233 | -61.07553 | 2025-11-08 01:32:00 | TERRA_M-M | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 8.2 |
| dbfd0f1a-7a1c-32e0-af65-53a4fa8e5649 | -12.14097 | -63.05374 | 2025-11-08 01:32:00 | TERRA_M-M | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 1cf6766f-b22f-3fac-a11a-c278ea767821 | -11.72169 | -61.42331 | 2025-11-08 01:32:00 | TERRA_M-M | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 29cc2756-4dc8-36ba-973a-21e352a3588d | -12.43208 | -63.15902 | 2025-11-08 01:32:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 12.4 |
| a3612a77-c8f1-3d7f-a0c4-0ff6e52bdc7c | -12.44982 | -63.15638 | 2025-11-08 01:32:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 9dcf63ad-e21e-32e5-a785-e0969a76871b | -12.45869 | -63.15506 | 2025-11-08 01:32:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 92328cbf-489b-30fc-aa65-1c082adc6d89 | -11.71223 | -61.42477 | 2025-11-08 01:32:00 | TERRA_M-M | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 897b35ea-4276-34ae-998c-ee8feb970340 | -12.44855 | -63.14732 | 2025-11-08 01:32:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 2e5e08df-d3c6-3ba5-a76c-b6db8b826ee7 | -9.96199 | -64.73978 | 2025-11-08 01:32:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| cbf0efef-570a-3840-b8a4-313b27d000e6 | -10.28641 | -67.27526 | 2025-11-08 01:32:00 | TERRA_M-M | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 137.5 |
| eb98934a-8ef2-3085-a695-ecc16b163bd7 | -9.67585 | -62.8899 | 2025-11-08 01:32:00 | TERRA_M-M | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 7c9ffeb0-78b7-36be-b76f-5a82c0a5b688 | -9.77745 | -62.5037 | 2025-11-08 01:32:00 | TERRA_M-M | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 10.2 |
| e8496ebe-dd25-3fa1-8302-101b133087ec | -11.26412 | -60.8927 | 2025-11-08 01:32:00 | TERRA_M-M | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 6.6 |
| e6948bf9-f38b-32a7-b0a3-764becbdb072 | -11.05907 | -60.88967 | 2025-11-08 01:32:00 | TERRA_M-M | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 2e434171-04b0-39c1-9460-f869b80a5bfa | -9.62506 | -68.60809 | 2025-11-08 01:32:00 | TERRA_M-M | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 7.8 |
| a41ed098-ca9a-3b3a-baa0-33a80f6edc80 | -9.43178 | -64.36298 | 2025-11-08 01:32:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 4737c0ba-01c9-39ec-8ca3-fe5c173e23c8 | -10.28787 | -67.28677 | 2025-11-08 01:32:00 | TERRA_M-M | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 577119c0-4871-34ec-9eb1-ed68f04b4df3 | -11.86862 | -62.8892 | 2025-11-08 01:32:00 | TERRA_M-M | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 952f8bd9-0bca-3004-a277-0c8d390af6e8 | -11.75269 | -61.07702 | 2025-11-08 01:32:00 | TERRA_M-M | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 7d1c59b0-9035-37f1-bb55-65020b12894c | -9.99622 | -63.65516 | 2025-11-08 01:32:00 | TERRA_M-M | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 19da7e54-16a4-3400-bc7e-0f3702ac59ab | -8.62229 | -66.81539 | 2025-11-08 01:32:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| d5d0c77b-4d3d-3506-863c-fe7065efc307 | -9.62325 | -68.5943 | 2025-11-08 01:32:00 | TERRA_M-M | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 202d68cf-6ed8-3ca4-956b-2e12b5892434 | -3.28205 | -64.86584 | 2025-11-08 01:34:00 | TERRA_M-M | ALVARÃES | AMAZONAS | Brasil | 1300029 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| fd8ce379-cafa-30e0-9dce-4ea87078391b | -3.3464 | -50.1979 | 2025-11-08 01:40:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| d48fe858-9d5b-39d8-aad5-1b66d2e4fd39 | -10.2789 | -67.2815 | 2025-11-08 01:40:00 | GOES-19 | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 805c74ae-d6e3-3e5e-a0cd-f991b14c1ca6 | -10.2975 | -67.2809 | 2025-11-08 01:40:00 | GOES-19 | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 80c18d85-8fb2-3cad-8ac9-f407ae90baaf | -4.4633 | -43.2152 | 2025-11-08 01:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 103.8 |
| a215f8ab-35b9-3983-93bf-4df1d74c9688 | -3.3463 | -50.2189 | 2025-11-08 01:40:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 24bcfe28-307c-3645-a573-b34ab5fb3647 | -4.6835 | -46.4074 | 2025-11-08 01:40:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 96.0 |
| 39c5d305-492e-3bcc-8323-45929a6dc914 | -4.7021 | -46.4064 | 2025-11-08 01:40:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 99aed8c1-d293-3ad5-b2f4-e6c5cdc8a676 | -3.4058 | -45.4424 | 2025-11-08 01:40:00 | GOES-19 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 4812bb27-2779-3fc9-bbf5-a11f13c25fca | -10.2789 | -67.2815 | 2025-11-08 01:50:00 | GOES-19 | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 23e6e903-183f-374f-a42a-6a3b52edbf78 | -4.6835 | -46.4074 | 2025-11-08 01:50:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 107.2 |
| e25c3e59-5519-3103-a3bf-7d68341be1e3 | -3.1639 | -45.497 | 2025-11-08 01:50:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 5ff24772-ad31-39eb-8292-2695614acbb0 | -3.4058 | -45.4424 | 2025-11-08 01:50:00 | GOES-19 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 72.0 |
| de19836d-c8c6-317b-b425-2444984c2d4b | -3.3463 | -50.2189 | 2025-11-08 01:50:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| a27066b6-68ee-39ae-9cd9-5e19eb2ec286 | -4.4633 | -43.2152 | 2025-11-08 01:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 81.5 |
| d2140107-3579-3815-8dce-b37c4b5f8802 | -3.3464 | -50.1979 | 2025-11-08 01:50:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 7f958240-67c1-3317-b7d0-a0ff1fb32018 | -3.1639 | -45.497 | 2025-11-08 02:00:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 12393aa5-ad10-3906-984e-e9a6af4b7984 | -4.6835 | -46.4074 | 2025-11-08 02:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 94.1 |
| 3eee07ad-aafd-3fd2-bf6e-510170b3ff46 | -4.4633 | -43.2152 | 2025-11-08 02:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 889045e3-121c-34ba-adae-dbb58a0d98fa | -3.3463 | -50.2189 | 2025-11-08 02:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| cd59461f-7d97-302a-80f5-4d2537966c05 | -3.4058 | -45.4424 | 2025-11-08 02:00:00 | GOES-19 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 64.5 |
| d967081e-e331-3c17-b85b-06853f197dc5 | -3.3464 | -50.1979 | 2025-11-08 02:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| a448885e-0f30-3f71-b261-16d1be7c2da4 | -5.4957 | -40.7832 | 2025-11-08 02:00:00 | GOES-19 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 32.9 |
| 3ad03d16-3b06-3ee4-8259-757272133d8d | -4.7021 | -46.4064 | 2025-11-08 02:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 7e6a744b-d36b-359c-b812-9d5177c36dd7 | -3.3464 | -50.1979 | 2025-11-08 02:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 94b436b9-cf85-3603-9986-6a0d19858af8 | -4.6835 | -46.4074 | 2025-11-08 02:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 73.4 |
| c4a6e549-9492-3b11-b904-6f9f14e8d8fd | -3.4058 | -45.4424 | 2025-11-08 02:10:00 | GOES-19 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 0ada1827-9fb9-3418-9a55-6f6a9452dc21 | -3.1639 | -45.497 | 2025-11-08 02:10:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 1284283d-7c2a-3006-b929-f0d5df43bb1b | -10.1613 | -36.2997 | 2025-11-08 02:10:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 76.4 |
| e983603e-3a5b-3299-a3ce-5091120c6d3d | -4.4633 | -43.2152 | 2025-11-08 02:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 81894d48-64c0-39e6-b283-bac2abfc3969 | -10.1806 | -36.2962 | 2025-11-08 02:10:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 125.5 |
| d3505385-5a0a-3094-a9dd-b22f6ea42a0b | -3.3463 | -50.2189 | 2025-11-08 02:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 4b8b4a2c-93c5-3754-a566-57a498a0890b | -5.4957 | -40.7832 | 2025-11-08 02:10:00 | GOES-19 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 44.8 |
| 13b55dfc-0b1e-3315-b118-6eb82c9811bd | -4.5747 | -45.9907 | 2025-11-08 02:20:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 26933aa6-4d1b-396c-922e-c55144af4519 | -3.4058 | -45.4424 | 2025-11-08 02:20:00 | GOES-19 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 86bdecaf-50ed-301b-b591-10f2fa9db3f7 | -4.6835 | -46.4074 | 2025-11-08 02:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 63.0 |
| ba266d55-4289-32f9-8750-3bf77b385d20 | -3.1639 | -45.497 | 2025-11-08 02:20:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 55.6 |
| c4eba0c1-d4cb-316a-94e8-dbea6d4b7963 | -3.3464 | -50.1979 | 2025-11-08 02:20:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 43.0 |
| 870c940c-3d69-330f-85ac-7a4e8f77f378 | -3.3463 | -50.2189 | 2025-11-08 02:20:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 45.6 |
| ccc53357-7faa-3ad0-bf27-3a19fe4fa3cf | -4.5931 | -46.012 | 2025-11-08 02:20:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 7480e4e9-eeab-31f5-9709-88d905640b8d | -4.4633 | -43.2152 | 2025-11-08 02:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 8969c767-1b88-3e91-af24-d5b3f05ab28e | -4.5933 | -45.9896 | 2025-11-08 02:20:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 114.0 |
| 02abb0de-4e59-35e5-94e7-b2332cdbe89b | -3.4058 | -45.4424 | 2025-11-08 02:30:00 | GOES-19 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 57beeb56-0216-3ef8-ab79-9088e2905d7d | -4.5931 | -46.012 | 2025-11-08 02:30:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 113.3 |
| 648757e7-fda8-3df3-98a6-19f8f0fb6a7d | -4.4633 | -43.2152 | 2025-11-08 02:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 0ad0090b-ca82-3f31-9d1f-ae841c77f81d | -4.5933 | -45.9896 | 2025-11-08 02:30:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 167.9 |
| 9629cc8a-b5cf-30a3-9e06-582e1c59f297 | -4.6835 | -46.4074 | 2025-11-08 02:30:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 77.9 |
| af4020b4-bc7e-37fd-bada-2d1cb4e60543 | -4.4633 | -43.2152 | 2025-11-08 02:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 61.1 |
| f9939d4b-2afe-38ff-ab25-1c0e90e46165 | -4.6835 | -46.4074 | 2025-11-08 02:40:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 85ac75ff-5aea-37b7-9cbb-f15466acabec | -4.5931 | -46.012 | 2025-11-08 02:40:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 87.2 |
| 00b70b8a-2a17-39dd-ae74-f295caf96b9a | -3.4058 | -45.4424 | 2025-11-08 02:40:00 | GOES-19 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 67.8 |


[Clique aqui para ver as próximas entradas](README7.md)

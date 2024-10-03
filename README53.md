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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 93942cfc-f31e-3f24-8d57-44bad8517f74 | -11.60562 | -65.00918 | 2024-10-03 02:09:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 610dc32c-4919-3004-92bc-8420e5a5b561 | -11.59803 | -65.01949 | 2024-10-03 02:09:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 14fd42b2-cb40-395f-aea8-c47fcd404f55 | -11.59676 | -65.0105 | 2024-10-03 02:09:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 17.9 |
| efa30e50-2b4c-319d-a89d-2cd012e0c82d | -11.59044 | -65.02979 | 2024-10-03 02:09:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 7.1 |
| a7d994ce-61d2-3a51-9029-26ee6427f68d | -11.58915 | -65.14928 | 2024-10-03 02:09:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 28b45a3c-73f4-3e9c-950d-6c5453001c85 | -11.58158 | -65.0311 | 2024-10-03 02:09:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 6.5 |
| c0a5d389-a215-32c5-964c-e6139fefc969 | -11.57807 | -65.14808 | 2024-10-03 02:09:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.2 |
| eae60fb3-4dba-3a25-bcdc-b2dfd0b54581 | -11.53134 | -65.07243 | 2024-10-03 02:09:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| db3bd78d-1779-3972-bad2-bbd4e8a4dcd9 | -11.52501 | -65.09173 | 2024-10-03 02:09:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 5d22b535-0c04-3456-ba94-3672ee0f6749 | -11.29174 | -65.00066 | 2024-10-03 02:09:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 12.9 |
| f1a4717a-8505-3b7b-8dcd-5b3475acea89 | -11.28665 | -64.96463 | 2024-10-03 02:09:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 9fdd1c0f-7896-33e3-be62-44914161bb75 | -11.28318 | -65.27372 | 2024-10-03 02:09:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 6.0 |
| b255fbde-62b4-397f-ae9e-2530cfaca10c | -11.26056 | -64.91918 | 2024-10-03 02:09:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 7.8 |
| bb50611b-76fb-3b86-94a2-6052b29e4778 | -11.16095 | -64.99545 | 2024-10-03 02:09:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 2e0c9afd-a2c7-31a7-b821-ea525a542789 | -11.12552 | -65.065 | 2024-10-03 02:09:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 09c84770-034c-3339-b6d4-5299dc84aaf0 | -11.68994 | -65.01831 | 2024-10-03 02:09:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 26.8 |
| 79555370-6535-3717-930f-9a6fc8ff995f | -11.68867 | -65.00931 | 2024-10-03 02:09:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 107dbe2d-35f7-33bc-80fa-9f3517aa5c64 | -11.68614 | -64.99131 | 2024-10-03 02:09:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 6b91f627-f497-363c-8c38-8e67cdcc7691 | -11.68488 | -64.98231 | 2024-10-03 02:09:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 21.1 |
| a6153a67-9920-3d1d-bb16-3294c948d644 | -11.68235 | -65.02862 | 2024-10-03 02:09:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 108f0bfd-3a0d-35ac-8d5f-400a120e0119 | -11.68109 | -65.01962 | 2024-10-03 02:09:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 33.7 |
| 5bab907a-2216-3b7b-8443-46cf8c95ab88 | -11.67982 | -65.01063 | 2024-10-03 02:09:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 18.4 |
| d2bda8e0-8a80-33ff-be75-795b03a26c18 | -11.67729 | -64.99262 | 2024-10-03 02:09:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 4ec5d8f9-52eb-3e55-95e9-f8a93d8186e6 | -11.67602 | -64.98363 | 2024-10-03 02:09:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 9.5 |
| a526157e-aad4-3f90-9d09-da70ca1e3f32 | -11.67223 | -65.02094 | 2024-10-03 02:09:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 2e626450-da53-3eab-9135-2d06f829f5b3 | -11.67097 | -65.01194 | 2024-10-03 02:09:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 6.0 |
| f184f192-b219-3a5a-be56-971c25fc2793 | -11.66873 | -65.20172 | 2024-10-03 02:09:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 984fdf1a-30c4-3cb4-8ba6-07c2aeca8ee0 | -11.66747 | -65.19274 | 2024-10-03 02:09:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 5ebcda2b-f68f-3ad5-966c-dc2130569817 | -11.66717 | -64.98493 | 2024-10-03 02:09:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 9b26290e-8871-3f4b-8be7-4e97d315ac24 | -2.9616 | -54.6503 | 2024-10-03 02:15:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 9a3b42eb-30a0-3531-a110-0dda2489c3ff | -4.0949 | -48.4894 | 2024-10-03 02:15:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 6dcf277c-fdb0-3a90-b10b-5a1faa8fe5b6 | -4.095 | -48.4679 | 2024-10-03 02:15:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| e0baf79f-f262-3613-b0e1-c09d8dbf3704 | -4.4844 | -42.8866 | 2024-10-03 02:15:31 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 121.7 |
| 8616b3d3-590b-3770-bf7a-ad211bf0053a | -4.4845 | -42.8631 | 2024-10-03 02:15:31 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 67c2fa26-1642-31f3-86d2-e18582f1d9d5 | -4.5373 | -43.3273 | 2024-10-03 02:15:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 52.9 |
| c4a28668-5a76-31db-bb94-15aacf959559 | -4.5375 | -43.304 | 2024-10-03 02:15:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 118.6 |
| f1d96693-fdd2-3029-947e-0ced0bacb328 | -4.58 | -48.0132 | 2024-10-03 02:15:32 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 59c7ad3a-bee7-32c6-a25a-a72042e74a68 | -4.9264 | -43.79 | 2024-10-03 02:15:34 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 114.1 |
| 530feb5a-be60-369e-ae6a-4db0160dc703 | -4.9265 | -43.7669 | 2024-10-03 02:15:34 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 08bdf0f9-c9b7-3470-91c4-c622c9394d96 | -4.9451 | -43.7888 | 2024-10-03 02:15:34 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 7a8b516f-b77f-3d94-bdbb-027d74db5f47 | -6.8777 | -59.0504 | 2024-10-03 02:15:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 43.5 |
| aec25599-c626-33ec-9f72-8b211939fc23 | -6.8778 | -59.031 | 2024-10-03 02:15:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 40.3 |
| f79ad67a-afa0-33be-a907-1fe2b2f36eb8 | -8.8506 | -45.5086 | 2024-10-03 02:15:56 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 155.9 |
| d03a1e90-9c3c-37b6-8902-62d3b3d526bc | -8.8509 | -45.4859 | 2024-10-03 02:15:56 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 39.3 |
| ce3344df-0dbf-31a3-b65b-c6b8be8c90e0 | -8.8695 | -45.5066 | 2024-10-03 02:15:56 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 82394ca4-26a2-3450-a627-5166a36bd04e | -8.8698 | -45.4838 | 2024-10-03 02:15:56 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 30.8 |
| cdf0c4bc-2a68-3f76-8b3d-1e25f85fbb87 | -8.8926 | -62.3348 | 2024-10-03 02:15:57 | GOES-16 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 61.8 |
| c9b73df1-0117-3e1e-ae08-7db71bc721f3 | -8.9976 | -67.4094 | 2024-10-03 02:15:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 62.1 |
| c7b2845f-0f6c-3a04-83b8-33bc2eb07b4a | -9.0149 | -67.7423 | 2024-10-03 02:15:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 740adfc2-a791-3ebd-af8b-aeb7cbd374e4 | -9.0515 | -67.871 | 2024-10-03 02:15:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 5fb9bf80-28c4-3637-b4b4-dc9a40bcbc1d | -9.0516 | -67.8525 | 2024-10-03 02:15:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 40.6 |
| 3fb7209d-8b72-3a8f-a82b-f10a4e7a4d37 | -9.1566 | -61.6758 | 2024-10-03 02:15:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 2cb52e4a-5793-3706-8bd8-28740c0df87a | -9.1752 | -61.6749 | 2024-10-03 02:15:59 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 203fe2a9-b917-34a9-9b90-398e80e5c0bc | -9.4368 | -64.5419 | 2024-10-03 02:16:00 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 19830d7f-7963-38bf-aeb8-9ca197d8ba2f | -9.494 | -68.4895 | 2024-10-03 02:16:01 | GOES-16 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 38.2 |
| 972373ac-a80a-350d-b962-4d0672c0255e | -10.8942 | -63.8971 | 2024-10-03 02:16:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 59.8 |
| bd72e57a-6d7d-37dc-9049-a8ab49193111 | -11.2565 | -60.6019 | 2024-10-03 02:16:10 | GOES-16 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 70.6 |
| f4b3945a-bd79-3fa3-a75c-1fc7d1946469 | -11.2566 | -60.5825 | 2024-10-03 02:16:10 | GOES-16 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 6e38a082-b381-3919-8ebd-bef75f7dced9 | -11.6743 | -64.9983 | 2024-10-03 02:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 70.3 |
| b7696514-bdb1-31b5-805f-2eed7dd9d4bc | -11.6742 | -65.0172 | 2024-10-03 02:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 3ae64337-a4b2-3848-9f90-58d90371b9f6 | -12.404 | -62.9817 | 2024-10-03 02:16:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 64.9 |
| bb4e618c-5041-3d8f-bf9a-7df335fff2e8 | -12.4038 | -63.0009 | 2024-10-03 02:16:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 92.3 |
| dae72a87-8cf4-30c6-802c-8173f612534c | -12.6486 | -63.1022 | 2024-10-03 02:16:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 43514426-8cbc-326d-8680-b030d7e14fb3 | -12.6484 | -63.1214 | 2024-10-03 02:16:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 97.0 |
| 83a555ec-de5c-3d0c-8831-b0ea0f57bb05 | -12.8999 | -62.4527 | 2024-10-03 02:16:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 85.4 |
| 6ac80188-258e-3ac7-9af9-cad98add64d9 | -12.8998 | -62.472 | 2024-10-03 02:16:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 126.2 |
| 96e43c52-2000-34ae-b82d-a8190a9ef76f | -12.8996 | -62.4913 | 2024-10-03 02:16:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 99.9 |
| b8e62ced-5898-38c4-b45f-965113bbd0c7 | -12.8991 | -62.5491 | 2024-10-03 02:16:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 8efd9e29-1753-306f-aa2c-6dcd1a41a171 | -12.881 | -62.4538 | 2024-10-03 02:16:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 6caa7309-adbd-3407-9145-d68b44580a49 | -12.8808 | -62.4731 | 2024-10-03 02:16:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 88.2 |
| 21c40d4a-ae57-39a9-9cb7-33ba0053f684 | -12.8049 | -62.497 | 2024-10-03 02:16:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 72.0 |
| e88203ec-fb08-3606-b023-e28fdc242714 | -12.9741 | -62.6409 | 2024-10-03 02:16:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 68.9 |
| f585e1ec-d1d0-3547-aaef-8bed768094ff | -12.9187 | -62.4708 | 2024-10-03 02:16:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 4bb5cab0-f330-3e3d-b93e-d72fb0a1a769 | -13.5562 | -51.2489 | 2024-10-03 02:16:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 82.4 |
| be19428a-9992-321b-9492-07662691d2e1 | -13.5558 | -51.2704 | 2024-10-03 02:16:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 121.4 |
| 831d1972-3a2a-3e25-a93d-7be714b8c584 | -13.5366 | -51.2728 | 2024-10-03 02:16:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 73.6 |
| b73a1703-808c-3ced-b484-612b8600fb52 | -13.5195 | -51.1467 | 2024-10-03 02:16:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 124.3 |
| f0e8b45c-fbeb-37b8-9383-8d640243c4e1 | -15.7676 | -49.9555 | 2024-10-03 02:16:34 | GOES-16 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 507b4682-d59f-3a4e-a0b7-1ab3778c68c9 | -15.7872 | -49.9523 | 2024-10-03 02:16:34 | GOES-16 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 102.6 |
| f6112bb0-1bb9-3fff-9240-9fb6fb4e7e47 | -16.7597 | -57.8124 | 2024-10-03 02:16:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 78.4 |
| 4fe68615-0a66-373d-97f9-81e2f25900f3 | -16.7594 | -57.8328 | 2024-10-03 02:16:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 94.5 |
| 19850c2b-732d-3d88-8274-e6d09d5bcaec | -16.761 | -57.7308 | 2024-10-03 02:16:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 72.3 |
| 3a9cdd26-2f84-317c-a9fe-28b2505fa700 | -16.7849 | -57.4425 | 2024-10-03 02:16:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 55.9 |
| 8364e443-123f-3b89-a4c5-a81143e1e83b | -16.7802 | -57.749 | 2024-10-03 02:16:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 50.2 |
| ddbfce5b-8030-30b5-a724-b23ba252b017 | -16.7793 | -57.8102 | 2024-10-03 02:16:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 82.1 |
| 02590479-c90d-31f7-97e9-65af58fb9731 | -16.779 | -57.8306 | 2024-10-03 02:16:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 148.4 |
| e54a84be-8205-3ddc-82b6-71de65b0102b | -16.7606 | -57.7512 | 2024-10-03 02:16:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 78.0 |
| 9aa3cd39-b40c-374a-9b70-4ff88025b382 | -16.7654 | -57.4447 | 2024-10-03 02:16:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 63.4 |
| 94d97603-1ff2-3e31-8690-a73729096975 | -16.9179 | -57.6926 | 2024-10-03 02:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 79.1 |
| 499c25a8-dcc5-3b3d-893c-c22068bae5ee | -16.9176 | -57.7131 | 2024-10-03 02:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 64.0 |
| 9abc5ba2-b066-39ea-babe-0df45566dda4 | -16.8986 | -57.6744 | 2024-10-03 02:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 48.9 |
| 6f194166-e6d9-31c6-a899-88c6e8400db4 | -16.8983 | -57.6949 | 2024-10-03 02:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 71.8 |
| 3ed01d4c-a964-35e9-960a-9cef17fd1924 | -16.7985 | -57.8284 | 2024-10-03 02:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 75.9 |
| d1d7eb40-e985-3c10-b70a-18587f07fb2c | -17.197 | -57.3741 | 2024-10-03 02:16:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 57.2 |
| 3960a7d2-32b0-3e80-8e5e-9b22471542f1 | -19.0344 | -43.1944 | 2024-10-03 02:16:51 | GOES-16 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 81.6 |
| 143454a7-6ccb-346c-b49a-c738e3af5e8a | -22.3094 | -44.0633 | 2024-10-03 02:17:08 | GOES-16 | VALENÇA | RIO DE JANEIRO | Brasil | 3306107 | 33 | 33 | nan | nan | nan | Mata Atlântica | 141.1 |
| c46d0a5b-4433-33e4-948d-4211a6d7d632 | -4.0949 | -48.4894 | 2024-10-03 02:25:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 8aff53c7-8742-37ca-981a-8854f41cf59a | -4.095 | -48.4679 | 2024-10-03 02:25:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| de3324cd-eca6-3bd5-9843-9b4429d163f5 | -4.4657 | -42.8877 | 2024-10-03 02:25:31 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 57.1 |
| ede547b7-92e1-3285-b0f5-be4ba20a25b5 | -4.4844 | -42.8866 | 2024-10-03 02:25:31 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 191.2 |


[Clique aqui para ver as próximas entradas](README54.md)

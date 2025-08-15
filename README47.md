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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4cf1ea5e-5f1a-3821-8006-a2cc8d58e15c | -13.31025 | -45.23353 | 2025-08-15 04:51:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f122f615-ed9b-33d6-a061-009185ef6c30 | -8.1092 | -61.19648 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3cbe3e74-2df9-3a21-82ef-21c289a7dcc8 | -11.19057 | -55.0107 | 2025-08-15 04:51:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 33c60ff5-be03-3c6b-9f18-382505dac404 | -9.50747 | -60.55094 | 2025-08-15 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 74613cf7-5cbd-33ab-b4c1-8ccae2a9044b | -14.02404 | -52.03696 | 2025-08-15 04:51:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ec509d7c-f787-3de0-8134-f6f8e2497873 | -11.34982 | -55.41446 | 2025-08-15 04:51:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| ed0c4496-2f0d-337f-85ec-23852b8717ac | -8.10529 | -61.18995 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1fe9bc60-77bb-34aa-83a4-a589d981e78b | -9.15471 | -59.6735 | 2025-08-15 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f2f83cc7-3e3f-34a1-8060-906cec28a53a | -6.91121 | -59.13647 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e2c18523-bf71-3143-99d0-efdfb89701a2 | -9.16571 | -59.6622 | 2025-08-15 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 052e20a4-036c-3fcf-b7cf-0f7f7a25b861 | -10.35931 | -50.81125 | 2025-08-15 04:51:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4dc2cfa7-6795-3fee-bf9b-f9c4b9b77fb8 | -9.38999 | -60.5482 | 2025-08-15 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 9328a751-9304-30d9-8bc4-9d9b4a19f979 | -9.20581 | -59.63865 | 2025-08-15 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 2c6aeb47-5f8f-3ae4-a744-105189c71ffa | -9.1692 | -59.69368 | 2025-08-15 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cc46f68b-3abc-3d10-8ddb-317e1599cbc2 | -8.31296 | -45.01193 | 2025-08-15 04:51:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a8147441-2744-37f4-be8e-e808e838b967 | -10.16414 | -59.66645 | 2025-08-15 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 74d0aa77-6018-3997-9a38-8a84501a808b | -6.8886 | -59.13695 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1ff0106e-7e19-3cfe-af2a-5fbc5d412f18 | -7.29679 | -60.62561 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6b459c7e-0e9c-3776-b488-3ba3d17eb1df | -9.16995 | -59.68941 | 2025-08-15 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7f2a4a64-3f20-3e94-bf45-8e3784be696f | -9.93471 | -60.48491 | 2025-08-15 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 37162faf-88ca-390a-8559-8200e8f6f60d | -11.34763 | -55.40654 | 2025-08-15 04:51:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6e0d327c-6ff4-360a-ac94-062bc519723c | -9.18358 | -45.32204 | 2025-08-15 04:51:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 14b85f43-e147-34a6-aa68-cff012523804 | -7.53136 | -61.34851 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 3d0b3c8d-a0d3-3ddc-a240-6e2d67de4896 | -6.90683 | -59.13572 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 013d840e-78e1-38f0-9923-fcc9fe51b37a | -7.0834 | -60.03545 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 85191587-4340-305d-b303-ac3b0c9c01be | -13.32724 | -45.22571 | 2025-08-15 04:51:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c290deff-5066-3c60-9a56-5dd1322066a7 | -14.07139 | -46.31761 | 2025-08-15 04:51:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 5d3cabf4-928b-3119-b6f2-e3b8a0a2c5af | -7.62865 | -63.52143 | 2025-08-15 04:51:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bb99c53b-c7e9-30f4-9e5a-0799f36a252e | -8.19136 | -42.26431 | 2025-08-15 04:51:00 | NOAA-20 | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 56fbd164-aa77-3879-8fc5-4b33c24073b6 | -11.02603 | -45.06656 | 2025-08-15 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1c558c9e-d146-33c9-b906-6156481a2921 | -7.14753 | -60.1253 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 73d1de53-bb03-3bb6-ac42-b1b864459f31 | -12.2654 | -48.78754 | 2025-08-15 04:51:00 | NOAA-20 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 03e417ee-89c1-3f4e-8aa8-e2b36509bbe7 | -9.84295 | -47.80988 | 2025-08-15 04:51:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2aed4e4f-4332-3a27-96d8-7b23c77b1edf | -7.88226 | -61.81409 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8b8be902-40cc-3e48-bc55-5e2cc8e57fb9 | -7.30159 | -60.62653 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| df2674cc-eedf-31ce-aebd-da9c68c5e69b | -8.10636 | -61.2064 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 86cbfab7-78ed-32fb-830b-76253b4b35bf | -11.73206 | -64.90005 | 2025-08-15 04:51:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 01646966-263c-3827-9be6-4db0da850a4d | -13.00692 | -56.87532 | 2025-08-15 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 64bb9bae-849b-3e5b-86cc-80f3c82903c5 | -8.1083 | -61.19517 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 350b47c2-240d-306d-9daf-e3b50a309ba0 | -9.15606 | -59.69139 | 2025-08-15 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d94b3ef3-227b-3fed-82b7-e9c296819eba | -10.91857 | -55.00698 | 2025-08-15 04:51:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 878db4ac-eccc-3a54-986d-72817c6e2bf5 | -13.57832 | -46.96844 | 2025-08-15 04:51:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b7fa3569-0f2e-3b0f-a858-82a207c87506 | -13.56914 | -46.96567 | 2025-08-15 04:51:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 400acfb3-6f1b-389c-8c41-5111c5b07d98 | -9.19927 | -59.65041 | 2025-08-15 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c19a5f7b-0e84-3ea2-80cb-0fe050804c7b | -11.3516 | -55.40344 | 2025-08-15 04:51:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 108afb32-6815-3167-b7d5-3417d21a125f | -9.92024 | -60.48693 | 2025-08-15 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e4427b10-8f01-3a71-afbb-7f17bcfb9983 | -8.31138 | -45.02345 | 2025-08-15 04:51:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c8a74f94-e5c5-3b78-875b-a85b90dada11 | -7.94269 | -61.75292 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 775ee060-824d-3cf9-9f8e-a80c279a76d6 | -12.49695 | -47.02333 | 2025-08-15 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 972a633e-c597-3b59-bab7-254b07f4a9d9 | -6.90173 | -59.13927 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8ee2389d-afa3-3da7-8cc2-591f0e83a495 | -9.1553 | -59.69568 | 2025-08-15 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0ca74822-264e-321d-841a-7c310b3436f7 | -7.23062 | -57.65739 | 2025-08-15 04:51:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 45bd4330-1613-365f-97f7-91c24c52c26e | -11.35101 | -55.40711 | 2025-08-15 04:51:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e9bb8b9c-041a-3bac-858d-8639c7a8227b | -13.56745 | -46.95665 | 2025-08-15 04:51:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a30d672f-3c5d-32c7-be64-51e0904adf74 | -9.17008 | -59.66297 | 2025-08-15 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 0d8c2034-d27d-394f-aeac-2768cc1d551f | -13.27792 | -50.83284 | 2025-08-15 04:51:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b842828c-ba41-302b-99b1-2e9539500302 | -11.73604 | -64.89869 | 2025-08-15 04:51:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 10b1ee91-efa5-3c7f-b12f-a4abde6ad01d | -7.32076 | -60.6246 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 96504ef5-c8bb-3eb0-8ba2-f52d10e33abc | -9.397 | -60.54185 | 2025-08-15 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b70becaa-6931-3790-a30f-93a5d6ba097f | -6.65616 | -58.82475 | 2025-08-15 04:51:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 0bcff724-f4aa-3527-a9bf-b22d2b9ee720 | -8.10819 | -61.20207 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 94786c56-db5b-3580-a40f-b4dd59e80a45 | -7.15536 | -59.64053 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2531e01c-dc1b-36dd-9e8a-7aefc3b99f5c | -6.88205 | -59.14888 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2b21b3eb-e3b1-3f61-af48-32dad37a2f75 | -9.50287 | -60.55005 | 2025-08-15 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 1e312df3-8bd9-361d-a452-7b725d0447fe | -9.15849 | -59.65205 | 2025-08-15 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5df318f7-9c98-3c0c-b51f-daf34de956c1 | -6.67174 | -59.08449 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4bedd783-f4e0-33b3-b622-15751300b9b4 | -9.17795 | -59.69522 | 2025-08-15 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| da4888b4-fd5a-39cd-a87d-02490ae374cd | -9.18395 | -59.66088 | 2025-08-15 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d4460096-218f-358d-a015-e1e741e21f01 | -9.50091 | -60.53469 | 2025-08-15 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 47f80df2-a490-330d-901f-41a033ded69d | -7.62211 | -63.52446 | 2025-08-15 04:51:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 440bfe92-755e-3526-8ffb-e4ceb8b876ae | -7.28601 | -64.69452 | 2025-08-15 04:51:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1e0410d2-913c-36a0-bdee-057b50761f2f | -6.67155 | -58.82558 | 2025-08-15 04:51:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 13cee613-4d87-300f-b060-689d531dc19e | -12.75894 | -44.4177 | 2025-08-15 04:51:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| ca36199e-b165-3682-805e-92166de79791 | -6.69306 | -58.82927 | 2025-08-15 04:51:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 158b0a4d-51aa-3762-976b-cf46cd3b5406 | -11.0286 | -45.07278 | 2025-08-15 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d26bb264-3282-3873-9b73-e20103644fbf | -7.52065 | -61.38038 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 45a79f6c-fb63-3c87-b52f-cb67d9500a9d | -10.16055 | -59.66164 | 2025-08-15 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0c355cd6-1056-3195-a5de-fd4f4fd11d95 | -6.87183 | -59.84022 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2dea5a2f-7a80-377c-9453-19a016b63ece | -8.55984 | -63.9146 | 2025-08-15 04:51:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f3c13dda-3679-3c1b-b4aa-fca6c1d90208 | -6.91854 | -59.14645 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ce118dbb-c3ff-3c44-9499-149d468e184b | -8.67584 | -62.44853 | 2025-08-15 04:51:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 68b46d88-2532-37be-8612-5c07fbb2b5ac | -6.92517 | -59.52979 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9e048d41-f1d7-3eec-98b4-b295e06ab455 | -13.57086 | -46.96771 | 2025-08-15 04:51:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b0aef8d9-58cf-37f8-bb1d-83a22b1a1105 | -7.4667 | -60.40931 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 144cff1a-16fc-3c85-81cd-1cc208fcebbb | -7.31497 | -60.6292 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 84741772-8e74-3a28-80aa-dc734f535bd4 | -8.56568 | -63.91573 | 2025-08-15 04:51:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 84f5ddeb-80cd-3da8-9eb0-4815d5dc2a48 | -13.13277 | -57.16445 | 2025-08-15 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d739b10d-de96-332d-9149-435f68733be7 | -9.19851 | -59.65479 | 2025-08-15 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d86318c7-c2db-3875-bf20-4f3329278ade | -14.79372 | -42.72308 | 2025-08-15 04:51:00 | NOAA-20 | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| b684d70b-40e6-309e-b561-a04586cc1cf0 | -6.66294 | -58.8241 | 2025-08-15 04:51:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 41e83ab7-1122-3275-a480-7dfe1ff64abb | -7.54916 | -63.4981 | 2025-08-15 04:51:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 251eee19-d3f6-34ee-9c49-8b90bcba8c32 | -7.52883 | -61.32877 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 57b68b70-3f37-3ede-9431-8a918682bfd9 | -6.94884 | -59.99446 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 08256f3c-75fb-3b93-a2b8-53179bb8cb9a | -6.66365 | -58.82003 | 2025-08-15 04:51:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| ae2c5beb-ac00-3ef0-acc2-8599657ff880 | -7.26029 | -60.63559 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fcb139c4-ce66-3053-9bd4-d3e1364b1fad | -7.15458 | -59.6451 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ea0f0cbd-cf9c-370d-a69f-e0d96b1ffa2d | -6.66665 | -59.08795 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8ce299a3-21e1-3f60-bf07-51659cd06f99 | -12.59404 | -46.96373 | 2025-08-15 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5e9e61a1-f288-3098-ae01-eb617b20ea8c | -13.13346 | -57.16032 | 2025-08-15 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f69642a0-316c-30a9-8ae2-5c13b9b14596 | -6.64323 | -58.82259 | 2025-08-15 04:51:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README48.md)

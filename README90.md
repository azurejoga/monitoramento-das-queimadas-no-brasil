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

## Dados Diários - Página 90

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 170bcde1-efe0-33d8-b136-d976b59dac7e | -9.47768 | -60.49046 | 2025-09-08 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2ae091f5-806f-3620-96ca-c0fcf4cc2296 | -9.82699 | -67.64761 | 2025-09-08 05:42:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 776770e2-cf10-3e6b-94d9-5b1b40545aee | -9.26078 | -67.60876 | 2025-09-08 05:42:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9af57ebf-38f4-37db-b792-7ffe0070f2f9 | -7.3994 | -61.62882 | 2025-09-08 05:42:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 17.6 |
| e743a4c0-41ab-3847-a997-800c40d7d824 | -6.83417 | -52.80937 | 2025-09-08 05:42:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7e41ff3d-66d4-3a43-aa5e-6c6e909a3eb2 | -9.35645 | -65.42333 | 2025-09-08 05:42:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 37d25672-7a06-3303-bdbe-0937c9b61939 | -10.77076 | -59.85475 | 2025-09-08 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bcdc70ca-0d76-3146-b46b-ab361217d4fa | -10.51046 | -57.79787 | 2025-09-08 05:42:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3bee328b-efa8-3fe6-9ca0-0d33fd52e5e7 | -9.44938 | -61.82109 | 2025-09-08 05:42:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 10.7 |
| a8eee287-fa4c-3080-9a6b-bcc3b37f8f2d | -9.18293 | -60.77783 | 2025-09-08 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 32398b2b-58be-3606-9391-3f775aa927a5 | -9.1314 | -65.94868 | 2025-09-08 05:42:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b5f5f54d-86f4-38df-b304-ba857aa07fcd | -9.06693 | -60.49196 | 2025-09-08 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 54247e34-eaf5-343f-b967-6a53c0f5860a | -6.83491 | -52.80371 | 2025-09-08 05:42:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f8c1cd17-151e-32e7-84b8-98f708bae84b | -9.9491 | -60.1483 | 2025-09-08 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f5258b33-e22a-33c4-940c-ee4d364660bc | -9.88898 | -67.91089 | 2025-09-08 05:42:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1910c6ad-56ff-39ee-a09e-25c7473ebea8 | -6.82147 | -52.80278 | 2025-09-08 05:42:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fab0565f-bf68-3790-a9a6-c333407c1ec8 | -10.5754 | -61.25513 | 2025-09-08 05:42:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2d63ab08-5126-3897-8615-d051d545e875 | -9.34704 | -63.81763 | 2025-09-08 05:42:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 79efc471-0c87-3f5e-acab-0666cec01f6b | -11.22462 | -55.00934 | 2025-09-08 05:42:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 983e4a02-3e86-3f4d-b53a-1888179aec4c | -9.17333 | -59.3788 | 2025-09-08 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 08b1d1b1-a393-3d46-a77a-061dc69dd8d6 | -10.58377 | -61.234 | 2025-09-08 05:42:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9dcbf3af-a613-3606-945c-1e025d9bdcdc | -9.87407 | -63.35775 | 2025-09-08 05:42:00 | NOAA-20 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 94804fdb-36ad-3c67-92b8-3e367586316c | -9.43993 | -59.20795 | 2025-09-08 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 19.0 |
| e10b560c-ea40-3767-8b2c-43edf36aff81 | -9.10473 | -60.96988 | 2025-09-08 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 63eea950-42a8-3a02-abf1-d5120db03d19 | -9.95567 | -67.19449 | 2025-09-08 05:42:00 | NOAA-20 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9d0e0d83-d6e7-39ce-8f33-edb0975f5bd3 | -6.96059 | -62.93003 | 2025-09-08 05:42:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1adc26d8-47be-3135-bbd6-b56bd361c280 | -8.09286 | -54.75965 | 2025-09-08 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e888c503-4a4c-33f8-8fba-a5c5900e8b61 | -9.45917 | -56.04851 | 2025-09-08 05:42:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a73c3624-6871-3b1e-800f-e53f6b5c98b8 | -10.89787 | -55.71754 | 2025-09-08 05:42:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 37878e1b-2709-3ffa-b4ae-88c523898f00 | -9.66257 | -67.74905 | 2025-09-08 05:42:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 85df49b5-e8ea-3b7d-b2d8-7807c563e459 | -10.57888 | -61.25943 | 2025-09-08 05:42:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f2b96efb-340f-362b-b444-37258637289f | -9.44487 | -61.82529 | 2025-09-08 05:42:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 07a50725-5179-31de-9077-768d01a49718 | -7.90162 | -61.7832 | 2025-09-08 05:42:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 982da8b7-8f9f-3a6c-b6b5-c5d2a7cd7237 | -9.45866 | -56.05232 | 2025-09-08 05:42:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0b6938b3-b102-362e-98a6-e1a0f1ef2080 | -9.20473 | -65.91399 | 2025-09-08 05:42:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| da8b6660-5145-37fc-97ce-e2e599c69a0d | -10.87392 | -55.71856 | 2025-09-08 05:42:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 575a5e86-4790-3106-b44a-edf78e323224 | -10.17324 | -61.14289 | 2025-09-08 05:42:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 977dbdc4-a5be-3589-b085-7477d92a8045 | -6.91908 | -62.94368 | 2025-09-08 05:42:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9b9463cc-df64-34ae-97a0-c41966fd9afd | -11.78012 | -60.89191 | 2025-09-08 05:42:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 807519d4-8752-3d2d-ad8d-189a8521d794 | -9.93394 | -60.10025 | 2025-09-08 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e77b6dec-af59-3369-a062-59b3e1b56aa9 | -9.75535 | -65.08427 | 2025-09-08 05:42:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 70fe5150-59f2-3493-87a4-55c730cdd4c8 | -9.51308 | -67.49995 | 2025-09-08 05:42:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 0b313881-8bab-3db1-80aa-af9fcbeb69a8 | -11.18115 | -55.05846 | 2025-09-08 05:42:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bf5db8c1-d316-3a09-9693-72366f3dece9 | -7.10615 | -63.0696 | 2025-09-08 05:42:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 2c85e76e-025b-3196-b721-1ad99b9bcf8f | -10.50538 | -57.79718 | 2025-09-08 05:42:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6594929f-a28f-3593-9791-fd072d5dc3e5 | -11.05233 | -54.17406 | 2025-09-08 05:42:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 401189a9-1cce-3254-ae7e-489b06b7df38 | -9.47406 | -60.48607 | 2025-09-08 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fdbbef23-3a95-3110-839c-41ac28451e8b | -12.19518 | -53.91843 | 2025-09-08 05:42:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1edc928e-27d4-39ea-8570-ac930bf73341 | -7.4025 | -61.63395 | 2025-09-08 05:42:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 17.6 |
| f05c4ebd-5857-327c-8f95-1b43d7869062 | -8.36121 | -70.06073 | 2025-09-08 05:42:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d13835f7-6d13-38b9-b98c-8384f5efb8d0 | -10.0496 | -59.36418 | 2025-09-08 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 27e8904b-b1d7-3bba-8f8b-fa9f035909e8 | -6.95298 | -62.93287 | 2025-09-08 05:42:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 59710129-a62e-3964-b28a-eae08a1737f4 | -9.36769 | -65.93612 | 2025-09-08 05:42:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 69e2536b-9206-3b61-a9cd-ae571663a7a5 | -9.37045 | -65.94013 | 2025-09-08 05:42:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4932a003-3716-334f-8dd9-aaf9563c6f0c | -9.84203 | -53.32553 | 2025-09-08 05:42:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 838c8ef8-b484-316e-96bf-0e1ff82f5965 | -8.9827 | -65.44619 | 2025-09-08 05:42:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 68a6167d-2d59-3a2a-9a96-3f8e568da050 | -9.68519 | -63.1703 | 2025-09-08 05:42:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0256e573-6d4a-3932-8c67-d3cb70907f98 | -9.17011 | -59.36916 | 2025-09-08 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 947f5f79-f533-3365-ab0e-a4a8536e58d4 | -9.18397 | -60.77056 | 2025-09-08 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c28251eb-e3bd-3f9b-8c35-c568cfbcc000 | -6.54169 | -54.99414 | 2025-09-08 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 957d1ed0-6ebe-3453-b7ea-cdc9f4322de0 | -9.45597 | -56.05494 | 2025-09-08 05:42:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 71c7dc7c-843f-312b-ae5c-b13d0b60f008 | -9.46936 | -60.48928 | 2025-09-08 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fa8ba0c7-fffa-30f5-8b7e-0161152cb634 | -7.12359 | -63.07226 | 2025-09-08 05:42:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a4246896-283d-34f2-b2b7-7772eb8a7024 | -9.38602 | -62.33655 | 2025-09-08 05:42:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b1bf5cd8-2f7f-336c-833f-eb1de8f5d80f | -9.12809 | -65.94815 | 2025-09-08 05:42:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d4c006b4-0f5b-3e49-ab3f-97a6cc1d1e32 | -9.37707 | -65.94118 | 2025-09-08 05:42:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7ec29226-dba3-3851-a69d-9d6dc990c137 | -8.59144 | -67.22031 | 2025-09-08 05:42:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a9f8ceac-6cb3-31fe-8a4e-14ad13f91e8c | -12.82592 | -52.94287 | 2025-09-08 05:42:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8c66a191-9180-3b7e-aa16-44dd1e1a255c | -9.24683 | -57.06836 | 2025-09-08 05:42:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d8af5b96-0b13-3bc4-ba98-8019413c0a82 | -9.46256 | -56.04801 | 2025-09-08 05:42:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 88b6e276-ac32-3ed7-bf80-84d934731bb7 | -7.39564 | -61.62826 | 2025-09-08 05:42:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 29fafaa4-6277-3f33-b9c6-98203767fa71 | -10.5808 | -61.25559 | 2025-09-08 05:42:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d0627f86-2662-3e33-8e83-e9de3b8c0431 | -11.18211 | -55.05235 | 2025-09-08 05:42:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2e7bcd99-0f90-3a73-8322-bcafe13ebd6e | -7.90537 | -61.78375 | 2025-09-08 05:42:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4ec4ac7f-ebaa-31a0-bac0-0f72f466d8c0 | -12.8211 | -52.88565 | 2025-09-08 05:42:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9173a23b-f07c-33c1-8228-160773383444 | -6.967 | -62.93499 | 2025-09-08 05:42:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3a337e39-9c54-3bda-9008-94448b80fd54 | -7.40383 | -61.62481 | 2025-09-08 05:42:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 9d737db4-1273-3900-93c0-3b029cd8704d | -9.94967 | -60.14426 | 2025-09-08 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2293304b-7948-3e3f-bece-9dafd9c04306 | -6.95068 | -62.92452 | 2025-09-08 05:42:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 183a3365-b991-3f2b-a75b-9e218a64768e | -9.43157 | -62.36144 | 2025-09-08 05:42:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b18457ea-96e1-3dfc-9c07-81016ecd463d | -9.37376 | -65.94066 | 2025-09-08 05:42:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bc3f7cf9-3062-3e8d-89aa-547959b3b427 | -8.72038 | -69.11179 | 2025-09-08 05:42:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5f23b44d-1997-360f-81c3-51562e930354 | -9.81891 | -53.32232 | 2025-09-08 05:42:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 33b4df93-be3a-30b0-a279-2587bf5ad2c0 | -9.7331 | -63.43113 | 2025-09-08 05:42:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 098e64a1-1675-3bf8-9fdf-63aabd6e8525 | -9.1303 | -65.95564 | 2025-09-08 05:42:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1babd3f5-2ce9-3ce2-8320-9cda887e5b05 | -9.35303 | -64.26358 | 2025-09-08 05:42:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8860482d-c5d2-32d7-b580-a4cf9df3377e | -9.43462 | -62.36639 | 2025-09-08 05:42:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a3479d93-7731-3960-b508-8b9770351a5f | -9.82261 | -53.31711 | 2025-09-08 05:42:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7d03264f-f396-38d8-a999-4caf16756a79 | -7.90208 | -61.78608 | 2025-09-08 05:42:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 9d93507b-1b6c-3ec5-bf4d-c869a67cf060 | -10.51161 | -57.80188 | 2025-09-08 05:42:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d6792f49-8b15-3028-9a5a-5a72c091ac24 | -7.39491 | -61.63034 | 2025-09-08 05:42:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d93d4905-a7f7-3f49-ab26-5a601134aa9d | -6.95709 | -62.92949 | 2025-09-08 05:42:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f1c1bf10-38ae-34f5-8b0d-7b74fb20e7f0 | -9.48075 | -60.49861 | 2025-09-08 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a9b917c7-a890-3635-8a74-9ee4da8118df | -10.51202 | -57.79884 | 2025-09-08 05:42:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5f3941b5-672d-3314-8b11-4f726e74b158 | -10.42366 | -60.75211 | 2025-09-08 05:42:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| aaeb9a93-1ba2-358b-aa0f-abe8a7be7204 | -6.91968 | -62.93977 | 2025-09-08 05:42:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d130864e-1eab-3e84-ba8a-2ed76f2a31d8 | -9.47298 | -60.49364 | 2025-09-08 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| edd5076d-c122-3b61-8184-a165e1ca82b3 | -10.58248 | -61.23461 | 2025-09-08 05:42:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bdfe65ca-d4bd-32bf-a381-d25d19ca25ad | -9.452 | -60.52169 | 2025-09-08 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f4e36abf-5968-3aee-9903-96bb8f134a02 | -10.87601 | -60.73466 | 2025-09-08 05:42:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README91.md)

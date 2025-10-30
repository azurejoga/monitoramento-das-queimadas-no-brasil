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
| 4f743a07-ac80-3f30-a33e-83f466f807e3 | -6.5254 | -46.9074 | 2025-10-30 00:00:00 | GOES-19 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 0e7e8f64-ab15-35a0-82d1-6f25f6cb49e2 | -13.3743 | -54.3159 | 2025-10-30 00:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 107.5 |
| 6aec0d40-3129-35fd-8b21-aee318a479b3 | -12.8152 | -43.4481 | 2025-10-30 00:00:00 | GOES-19 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 153.6 |
| b8262943-228e-3cbb-a658-8d83a90f982b | -8.3125 | -47.9236 | 2025-10-30 00:00:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 9aa75347-7283-363b-b74a-527559809d51 | -14.781 | -44.9835 | 2025-10-30 00:00:00 | GOES-19 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 74.3 |
| e7074603-e0ad-3aa8-9bc7-9ab31634a945 | -10.2182 | -36.3433 | 2025-10-30 00:00:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 65.1 |
| 61cc94b6-f6d6-34ca-b72c-9d2a2102f289 | -3.8054 | -43.9002 | 2025-10-30 00:00:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 377a3684-abc2-39c0-883e-46dd116763a4 | -8.3123 | -47.9455 | 2025-10-30 00:00:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 07cb58cd-b21e-3071-b193-9d1e7ca30843 | -13.3169 | -54.3221 | 2025-10-30 00:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 100.6 |
| 4fc835ae-edfe-38e1-803d-fc3e83033d37 | -4.4805 | -43.4237 | 2025-10-30 00:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 87e345e5-37f1-31e1-bc68-ef69d9e7a86a | -13.3172 | -54.3014 | 2025-10-30 00:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 76.7 |
| ea1d25b8-6e81-33c0-b75d-ca76c29585e3 | -12.8345 | -43.4448 | 2025-10-30 00:00:00 | GOES-19 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 97a0e1c5-1893-3bd4-a5ac-29ab76bcfc72 | -3.7867 | -43.9011 | 2025-10-30 00:00:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 95c250c2-b78a-3957-97ae-9e4e029606d2 | -6.112 | -47.2017 | 2025-10-30 00:00:00 | GOES-19 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 7dfa99b3-f8bd-3260-884e-abefe1cb52b9 | -13.3552 | -54.3179 | 2025-10-30 00:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 59.0 |
| cab5a3c0-c1fd-31f0-99de-e68a3cdc8d75 | -9.8824 | -47.4344 | 2025-10-30 00:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 82.3 |
| b7c19890-8a58-3fc5-8bd0-bc9a5277c9ce | 3.146 | -60.7075 | 2025-10-30 00:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 83.9 |
| 4479d1d7-0db3-3187-9775-e08ae3f90816 | -7.3787 | -47.6105 | 2025-10-30 00:00:00 | GOES-19 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 43.6 |
| 45c01886-28c3-3bfb-a0c3-715021547cb6 | -10.2187 | -36.3162 | 2025-10-30 00:00:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 62.2 |
| dc265ea5-01d4-335c-8d21-554e0dffa49f | -8.3311 | -47.9438 | 2025-10-30 00:00:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 101.0 |
| cd58b3ec-3b7b-35cd-aaba-a04e11261a68 | -4.2648 | -59.675 | 2025-10-30 00:00:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 90.1 |
| bf97bceb-106b-3cc8-b1ae-5f78cb05067f | -8.3313 | -47.9219 | 2025-10-30 00:00:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 126.1 |
| 26b0cde9-c53a-3a7f-aa26-50288afe831d | -15.1059 | -41.9882 | 2025-10-30 00:00:00 | GOES-19 | CORDEIROS | BAHIA | Brasil | 2909000 | 29 | 33 | nan | nan | nan | Mata Atlântica | 63.6 |
| 857f05c6-bf08-3ea6-9e1a-ee23d86c1519 | -4.2832 | -59.6554 | 2025-10-30 00:00:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 153.2 |
| 75eaed32-65fb-3ed5-bd57-e3f6a1308c27 | -6.0108 | -41.9708 | 2025-10-30 00:00:00 | GOES-19 | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | 64.2 |
| 1b3868cf-a36a-34a4-9df2-3b745e9b26c8 | -9.7607 | -36.1009 | 2025-10-30 00:00:00 | GOES-19 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 55.3 |
| 5f846eba-023f-3494-bb5a-b472887b0d0b | -2.7741 | -45.3989 | 2025-10-30 00:00:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 80fc01af-837f-3015-b614-97ead7f8da0f | -4.4804 | -43.447 | 2025-10-30 00:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 69.9 |
| afc04670-0ccf-3cb7-a766-570fe51763fd | -13.374 | -54.3365 | 2025-10-30 00:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 445cf7f8-f210-3551-b1d5-af3cd3597d0f | -4.2649 | -59.6558 | 2025-10-30 00:00:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 165.8 |
| bdec9cca-0be1-33dc-b9a0-37dff2a239e0 | 3.1461 | -60.6886 | 2025-10-30 00:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 112.3 |
| c07217ab-5ef3-3030-84cc-589a6b797aed | -8.3123 | -47.9455 | 2025-10-30 00:10:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 9e9e3306-11e7-3289-9666-3ab1c25c31d4 | -18.2451 | -42.6313 | 2025-10-30 00:10:00 | GOES-19 | SÃO JOSÉ DO JACURI | MINAS GERAIS | Brasil | 3163508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 63.7 |
| 6ca61b16-ec1c-3c7c-87c8-4520ebe9fa55 | -13.3932 | -54.3345 | 2025-10-30 00:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 723b82c2-5023-3851-85ac-278ef60f9c7e | -5.7966 | -40.8068 | 2025-10-30 00:10:00 | GOES-19 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 68.1 |
| 93badf08-c5bb-3d6c-8314-9202dcd953a9 | -3.8054 | -43.9002 | 2025-10-30 00:10:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 70.4 |
| b8bcde55-974c-3ee6-8b56-eb5ad5894723 | -8.3125 | -47.9236 | 2025-10-30 00:10:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 43334326-de40-33ba-a6d9-c2fcc34eb914 | -3.7867 | -43.9011 | 2025-10-30 00:10:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 58d67c2b-3ae2-3b0b-813c-53f8582a97c5 | -8.3313 | -47.9219 | 2025-10-30 00:10:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 150.8 |
| ab21b362-1d0f-3946-b595-f87b77143688 | -13.374 | -54.3365 | 2025-10-30 00:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 91.0 |
| d3c40929-e104-3afb-aa15-a3383d2bb8f9 | -13.3743 | -54.3159 | 2025-10-30 00:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 136.6 |
| 66370cec-33a2-3ad9-9ce8-11378de01611 | -4.2831 | -59.6745 | 2025-10-30 00:10:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 1066fd7d-4d4d-39b8-b793-c9bb6e0f6422 | -4.2649 | -59.6558 | 2025-10-30 00:10:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 174.3 |
| a1491fbf-2e62-3ada-8be0-b233b33f19dc | -12.8152 | -43.4481 | 2025-10-30 00:10:00 | GOES-19 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 46b1f6a6-484e-3353-8ed8-a1136abaec2b | 3.146 | -60.7075 | 2025-10-30 00:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 6f1358cd-546e-3fb7-8a2d-ac3d613b6d45 | -4.2648 | -59.675 | 2025-10-30 00:10:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 86.5 |
| 285fdcfd-718c-3da2-879e-276c9a03b202 | -8.3311 | -47.9438 | 2025-10-30 00:10:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 108.9 |
| 9b49fb19-2100-315e-9437-04bb589b8f46 | -6.0108 | -41.9708 | 2025-10-30 00:10:00 | GOES-19 | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | 63.3 |
| b985ee0e-b9c4-3c8c-aaeb-286f68d65072 | -4.4804 | -43.447 | 2025-10-30 00:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 9d2ae1b8-62f7-3b5e-a868-47505adb326c | -4.7084 | -42.9429 | 2025-10-30 00:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 0e03b798-1b95-3d6c-81aa-cda15dce44b5 | -13.3172 | -54.3014 | 2025-10-30 00:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 89.3 |
| 518e7e2d-d5a5-3ed6-92d6-b7e09bd3ccd7 | -2.7741 | -45.3989 | 2025-10-30 00:10:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 61.4 |
| c939caa0-28d0-3440-bd86-c0b34888e43e | -13.3169 | -54.3221 | 2025-10-30 00:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 106.5 |
| 0043fc40-9caa-3c8c-9c66-4d3c22a1c652 | -4.2832 | -59.6554 | 2025-10-30 00:10:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 148.1 |
| 0def750d-13e5-3dab-9023-46ed5f78825a | -5.3851 | -47.2052 | 2025-10-30 00:10:00 | GOES-19 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 93.3 |
| 0c0c294d-584b-3967-950e-4073ccb52308 | 3.1461 | -60.6886 | 2025-10-30 00:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 112.2 |
| 96e867c9-7c6e-3c51-a59f-b2e61feb6be7 | -4.7271 | -42.9417 | 2025-10-30 00:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 360adf1c-fa72-3525-b42f-69b2522ff1b0 | -15.1059 | -41.9882 | 2025-10-30 00:10:00 | GOES-19 | CORDEIROS | BAHIA | Brasil | 2909000 | 29 | 33 | nan | nan | nan | Mata Atlântica | 67.1 |
| c982f7dc-f47f-34ee-a25d-d44e2a775e94 | -14.781 | -44.9835 | 2025-10-30 00:10:00 | GOES-19 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 956f3e27-4e73-3310-be4c-d3baeb222afa | -4.2649 | -59.6367 | 2025-10-30 00:20:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 67.0 |
| c79bc1a2-e2e1-3260-869e-7a88eb6bc1b4 | -8.3125 | -47.9236 | 2025-10-30 00:20:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 122.6 |
| ab39c585-7660-346c-a86b-5840b57f236e | -4.2648 | -59.675 | 2025-10-30 00:20:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 128ea8b8-ac0d-32a5-ace9-11ee3347aa30 | -4.2831 | -59.6745 | 2025-10-30 00:20:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 91f9ef6e-b5d3-32e1-955f-e24a7f8c7b55 | -7.9693 | -46.7423 | 2025-10-30 00:20:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 58.0 |
| cc349502-ddc4-3225-9b74-8334d5c0184a | -4.2832 | -59.6554 | 2025-10-30 00:20:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 115.1 |
| 845375ab-d0f1-3d2d-89a3-057144f2af4d | -3.7867 | -43.9011 | 2025-10-30 00:20:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 63.6 |
| f222e0c5-9710-361d-b066-0d652c5ed85d | -4.4804 | -43.447 | 2025-10-30 00:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 1df096b7-36bc-3654-8aaa-15e546f06aaf | -3.8054 | -43.9002 | 2025-10-30 00:20:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 02973936-e5f0-350f-b07e-ab856c98e57f | -6.0108 | -41.9708 | 2025-10-30 00:20:00 | GOES-19 | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | 72.9 |
| c9312d38-10dc-30c5-8268-d0b70711bc00 | -7.9508 | -46.7218 | 2025-10-30 00:20:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 48.5 |
| 67115fef-7613-3cf8-b178-16ac2ae373da | -10.6313 | -52.1891 | 2025-10-30 00:20:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 0c010152-34d2-3dc5-a542-9ef2ac51360d | -8.3311 | -47.9438 | 2025-10-30 00:20:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 4e69ea61-727b-33e4-b8b7-8007c3e59e0e | -4.2649 | -59.6558 | 2025-10-30 00:20:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 145.6 |
| dbea9bb5-7d6b-3f34-86b5-cdd380264d42 | -8.3123 | -47.9455 | 2025-10-30 00:20:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 72.8 |
| ca2fcc3e-d61c-3c52-af59-6a725e4c4848 | -15.1059 | -41.9882 | 2025-10-30 00:20:00 | GOES-19 | CORDEIROS | BAHIA | Brasil | 2909000 | 29 | 33 | nan | nan | nan | Mata Atlântica | 54.2 |
| 09711121-9c78-353c-b60e-41320242175d | -5.3851 | -47.2052 | 2025-10-30 00:20:00 | GOES-19 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 121.8 |
| b018df06-2343-38b3-abef-c4c2e8b5c755 | -2.7741 | -45.3989 | 2025-10-30 00:20:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 0cd548db-73a8-360c-b2f5-f995fbd2f382 | -8.3313 | -47.9219 | 2025-10-30 00:20:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 161.4 |
| 6da55a04-0549-321b-8ba9-d059f41ca6c6 | 3.1461 | -60.6886 | 2025-10-30 00:20:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 97.4 |
| 72756a78-dd18-3f78-a2b6-9f84a91c5161 | -13.374 | -54.3365 | 2025-10-30 00:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 88.5 |
| 20be0a8e-e4ad-3b83-b444-d6013deeac1b | -3.2317 | -46.8716 | 2025-10-30 00:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 45.2 |
| c216a5b2-e9d5-378f-8bb2-66305436b125 | -18.2451 | -42.6313 | 2025-10-30 00:20:00 | GOES-19 | SÃO JOSÉ DO JACURI | MINAS GERAIS | Brasil | 3163508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 79.6 |
| fa0ac0af-922c-331a-8bc7-2d5fbe86ccc4 | -13.3743 | -54.3159 | 2025-10-30 00:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 125.8 |
| dff0a251-a406-36fc-9db0-1846c4a4c693 | 3.146 | -60.7075 | 2025-10-30 00:20:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 82.3 |
| f2ec2b3a-1b18-39af-813a-b279b18453d3 | -7.9696 | -46.7201 | 2025-10-30 00:20:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 46.6 |
| 1729f8b2-dfa1-3d62-b5cf-ff4ed8ad298e | -7.9506 | -46.7441 | 2025-10-30 00:20:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 8ee077c7-b780-3dda-a4cf-123bec8bef42 | -12.8152 | -43.4481 | 2025-10-30 00:20:00 | GOES-19 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 72.3 |
| a0e4a32b-76ef-31a9-be23-6ac1033973f3 | -13.3935 | -54.3138 | 2025-10-30 00:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 82.4 |
| e5178eb9-a5ed-3d13-adc0-3e611d674882 | -12.8152 | -43.4481 | 2025-10-30 00:30:00 | GOES-19 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 74.6 |
| d218d92a-f48d-34c0-bb61-f92e90fcfd12 | -8.3313 | -47.9219 | 2025-10-30 00:30:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 210.3 |
| 625c1f84-f276-3eeb-bf37-26c71c74d281 | -8.3125 | -47.9236 | 2025-10-30 00:30:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 84.1 |
| a4e44cd7-382f-303a-a6f7-40cd808f6347 | -13.374 | -54.3365 | 2025-10-30 00:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 85.9 |
| ff4ae9ff-7db4-35ca-8b67-072e05894e4d | 3.1278 | -60.6889 | 2025-10-30 00:30:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 60.5 |
| eb9164db-7ffc-3fe3-bc5d-93b9bad3b5bd | -3.8054 | -43.9002 | 2025-10-30 00:30:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 6b58e5b5-fb11-3495-9707-5df0a67628d8 | -3.7867 | -43.9011 | 2025-10-30 00:30:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 98cf37a2-3856-345d-bb4e-6840936a8033 | -13.3932 | -54.3345 | 2025-10-30 00:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 8a25092a-8582-3217-9329-90b262d449f7 | -13.3552 | -54.3179 | 2025-10-30 00:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 86.9 |
| 8aaa82ad-a7b7-330c-95db-1b9bf1347c19 | 3.146 | -60.7075 | 2025-10-30 00:30:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 76559b10-0bb1-3839-8114-79ac0b191760 | -12.1962 | -46.6944 | 2025-10-30 00:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 54.9 |
| 2580c0ed-0e4a-33f7-9915-93762968f32f | 0.2852 | -51.2114 | 2025-10-30 00:30:00 | GOES-19 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 54.7 |


[Clique aqui para ver as próximas entradas](README2.md)

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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c0d4ebbd-526e-3222-9e4b-bb6bce4f4524 | -12.8049 | -62.497 | 2024-10-03 00:46:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 87.3 |
| eb9197f1-b69c-3606-ae46-4e9374e56c14 | -12.8808 | -62.4731 | 2024-10-03 00:46:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 98.7 |
| b4dedd88-4081-3c85-8564-ff05b6f22e7b | -12.881 | -62.4538 | 2024-10-03 00:46:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 97.1 |
| fe158329-f7ac-3be9-8899-31032f04e257 | -12.8996 | -62.4913 | 2024-10-03 00:46:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 108.4 |
| e475b8b0-a39e-359c-a047-d8cd519c7b70 | -12.8998 | -62.472 | 2024-10-03 00:46:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 144.4 |
| 243e67a8-987c-3a09-9a60-9af5448e6b8c | -12.8999 | -62.4527 | 2024-10-03 00:46:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 102.9 |
| 6e991c17-41fb-3f10-b898-d9cf6829580f | -12.9741 | -62.6409 | 2024-10-03 00:46:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 64518b12-787d-3990-a637-51795fde7dc8 | -13.5369 | -51.2514 | 2024-10-03 00:46:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 108.2 |
| 406f8f3a-4d9a-3f97-823b-05bede0a6c4b | -13.5373 | -51.23 | 2024-10-03 00:46:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 72.8 |
| b66d1156-3b87-3239-b98d-ea43023f3912 | -13.5558 | -51.2704 | 2024-10-03 00:46:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 83a8b7f1-51f3-3864-b481-c6ee0f90de71 | -13.5562 | -51.2489 | 2024-10-03 00:46:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 257.3 |
| c2315e55-8f62-386f-bae0-0294e006ebf5 | -13.5565 | -51.2275 | 2024-10-03 00:46:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 177.3 |
| 951b92cf-2244-3907-9a3d-b185a569c0f7 | -14.522 | -45.2414 | 2024-10-03 00:46:27 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 77.9 |
| abdbc1fa-083b-3b87-a87e-e578450a9383 | -14.5225 | -45.218 | 2024-10-03 00:46:27 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 115.9 |
| cfc03551-0c30-3270-a869-17cc2520c375 | -14.7017 | -48.7559 | 2024-10-03 00:46:28 | GOES-16 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 48.5 |
| 6cc837d2-cd3b-31c1-a861-f4ce1b29dd03 | -16.7594 | -57.8328 | 2024-10-03 00:46:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 146.3 |
| 19065323-a5e5-3f67-a369-cca885e760b6 | -16.7597 | -57.8124 | 2024-10-03 00:46:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 137.3 |
| 552eb000-f52c-318c-9bfb-4968b95528a0 | -16.779 | -57.8306 | 2024-10-03 00:46:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 87.5 |
| de0c48fd-7b37-37c0-96ef-5dd51f514ca2 | -16.7793 | -57.8102 | 2024-10-03 00:46:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 80.1 |
| cb64d216-79d6-3d80-b903-ecc367767911 | -16.7985 | -57.8284 | 2024-10-03 00:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 51.9 |
| e6340f75-2200-3821-b106-4e32679a3ed6 | -16.7988 | -57.808 | 2024-10-03 00:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 46.1 |
| 71b184b8-663c-3279-b7da-7663d1dcb2cf | -18.8406 | -42.9235 | 2024-10-03 00:46:50 | GOES-16 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 56.7 |
| 78bb1b81-db40-33f4-ba5e-53a1556aebe7 | -18.8927 | -41.2248 | 2024-10-03 00:46:50 | GOES-16 | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 93.6 |
| 6d42a908-ab10-38e3-8577-38dd067d97b5 | -18.8935 | -41.199 | 2024-10-03 00:46:50 | GOES-16 | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 83.6 |
| 431a3bc8-3a71-3abe-84d6-cc8cebe82469 | -19.0344 | -43.1944 | 2024-10-03 00:46:51 | GOES-16 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 79.1 |
| 8be2d343-5a38-3d47-8ca5-512436d90505 | -21.306 | -47.6227 | 2024-10-03 00:47:03 | GOES-16 | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 09441a85-15ed-37e7-b7d2-6e247b4b146b | -21.3067 | -47.599 | 2024-10-03 00:47:03 | GOES-16 | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 87.2 |
| c734643e-34b1-3d26-b082-09b1337e94c6 | -21.3875 | -47.6497 | 2024-10-03 00:47:04 | GOES-16 | SÃO SIMÃO | SÃO PAULO | Brasil | 3550902 | 35 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 98db302e-ad6b-3634-a7b6-c630749905ae | -21.3882 | -47.6261 | 2024-10-03 00:47:04 | GOES-16 | SÃO SIMÃO | SÃO PAULO | Brasil | 3550902 | 35 | 33 | nan | nan | nan | Cerrado | 63.6 |
| c0bd9bb1-bcd4-3036-a47f-ab82a6228324 | -21.346 | -55.6626 | 2024-10-03 00:47:04 | GOES-16 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 114.6 |
| 76533167-1340-3264-857e-2fc54dd68bed | -21.8445 | -48.2178 | 2024-10-03 00:47:06 | GOES-16 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 698d37ab-76d3-39ea-a401-c6d86b9f1100 | -21.8452 | -48.1943 | 2024-10-03 00:47:06 | GOES-16 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 63.8 |
| d4589aa7-ff5d-3bc4-972b-169ef897a76e | -21.8799 | -48.4195 | 2024-10-03 00:47:06 | GOES-16 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 65.4 |
| dc743d9d-6274-3d73-ad7f-0b8cf27c3fe1 | -21.9 | -48.438 | 2024-10-03 00:47:06 | GOES-16 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 29344259-7272-391e-9bd0-87c7979312e2 | -21.9007 | -48.4145 | 2024-10-03 00:47:06 | GOES-16 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 72.4 |
| c59fd52c-fda0-3ece-8804-5dc1599e6620 | -21.9014 | -48.391 | 2024-10-03 00:47:06 | GOES-16 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 4a0bf276-27da-3507-a857-85c6d22f494e | -21.9021 | -48.3674 | 2024-10-03 00:47:06 | GOES-16 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 133.4 |
| 50dd46de-2c64-32ba-96dd-bf087fdd3a5d | -21.9028 | -48.3439 | 2024-10-03 00:47:06 | GOES-16 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 95.9 |
| a118d53f-0d5d-3b9e-a10d-4f9e29e6546b | -21.9215 | -48.4094 | 2024-10-03 00:47:06 | GOES-16 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 87.2 |
| f80c101f-159f-3ced-aa21-8ddd2c0746f1 | -21.9229 | -48.3624 | 2024-10-03 00:47:06 | GOES-16 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 91add9b2-1c6b-3077-a8a3-9e6563069a77 | -21.9236 | -48.3388 | 2024-10-03 00:47:06 | GOES-16 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 2bbf9f5d-37a3-379c-be60-f3e2a2ba0db9 | -22.3495 | -47.9515 | 2024-10-03 00:47:09 | GOES-16 | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 100.1 |
| ea80d128-1663-3a6b-a47c-37cb9c424a76 | -22.3502 | -47.9278 | 2024-10-03 00:47:09 | GOES-16 | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 167.6 |
| b4fe74da-e583-38ec-aa2a-c084ce4f459d | -22.3704 | -47.9462 | 2024-10-03 00:47:09 | GOES-16 | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 95235190-c5ef-38a1-8fbc-082bd1b56114 | -22.3711 | -47.9225 | 2024-10-03 00:47:09 | GOES-16 | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 169.4 |
| c0357a0a-ed1c-382e-90c9-13077a86fe52 | -22.3719 | -47.8987 | 2024-10-03 00:47:09 | GOES-16 | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 4a24af1d-c136-335c-b7e3-41a262681219 | -3.3854 | -42.2866 | 2024-10-03 00:55:25 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 228.9 |
| fc301ad0-3e06-3ef5-8dc6-293e97aa4e08 | -3.3855 | -42.263 | 2024-10-03 00:55:25 | GOES-16 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 189.3 |
| cae9bb9d-a8cc-3f7b-9143-bda75823ba7a | -3.4039 | -42.3094 | 2024-10-03 00:55:25 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 52.1 |
| 63ee0527-bac1-350d-867c-480d16127c0f | -3.404 | -42.2858 | 2024-10-03 00:55:25 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 417.6 |
| 4e7f3ff3-56d0-300b-a2e2-f2fc8f77ab5f | -3.4042 | -42.2621 | 2024-10-03 00:55:25 | GOES-16 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 322.8 |
| 4d227a87-a58a-3d46-94d4-a13f0386fe7e | -3.4043 | -42.2384 | 2024-10-03 00:55:25 | GOES-16 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 24.9 |
| 71e8c447-64c2-3436-88be-1658952b27a0 | -3.4227 | -42.2849 | 2024-10-03 00:55:25 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 6d736aa9-2181-356b-9568-9665fd890e6e | -3.4229 | -42.2612 | 2024-10-03 00:55:25 | GOES-16 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 65.2 |
| c66c7018-af53-37fc-a34b-4a54f86c9bc6 | -3.802 | -47.8104 | 2024-10-03 00:55:27 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 85b989f3-4bde-38b1-bd19-a08d31b77410 | -4.0949 | -48.4894 | 2024-10-03 00:55:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 82.9 |
| 09c8cdaf-c7a2-3415-97d5-3880680b7357 | -4.095 | -48.4679 | 2024-10-03 00:55:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| cb12dd1e-af7a-388e-beea-3131f62353cb | -4.1134 | -48.4886 | 2024-10-03 00:55:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 4cd33624-e7da-356b-9a16-38cd8e014e02 | -4.4657 | -42.8877 | 2024-10-03 00:55:31 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 6739c0b6-3886-3378-9b61-4154c17a8cdc | -4.5373 | -43.3273 | 2024-10-03 00:55:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 197d0d7d-8e4e-3895-a9f4-8ee68aaabc95 | -4.5375 | -43.304 | 2024-10-03 00:55:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 147.6 |
| 18483921-79c3-3832-837a-23b7b8c0c1cd | -4.9264 | -43.79 | 2024-10-03 00:55:34 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 77.6 |
| f7132c2c-cc6f-3644-805c-f748a2496e6c | -4.9265 | -43.7669 | 2024-10-03 00:55:34 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 86.3 |
| a2417e96-c4ed-31fe-89e2-8c3d842907af | -5.2441 | -43.8151 | 2024-10-03 00:55:35 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 210.9 |
| 1ce8f84d-5d16-33da-bf36-7c3e36a718a3 | -5.2443 | -43.792 | 2024-10-03 00:55:35 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 212.7 |
| dadfd54c-ae86-3996-96ec-cea840418e54 | -6.6453 | -54.952 | 2024-10-03 00:55:44 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 1905d04a-6a4d-319b-be2f-40c963cffab6 | -6.8777 | -59.0504 | 2024-10-03 00:55:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 519c598d-930c-32c5-a68b-18540746351e | -7.2056 | -59.7886 | 2024-10-03 00:55:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 0de4ad57-3620-3bac-a33c-c1f0179096f4 | -7.6326 | -67.2013 | 2024-10-03 00:55:50 | GOES-16 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 38.6 |
| 1b207604-60ef-3b14-9c37-b8a95229acd3 | -8.8506 | -45.5086 | 2024-10-03 00:55:56 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 76.2 |
| a7d810df-e5fd-371e-9cc5-46298ef50b59 | -8.8695 | -45.5066 | 2024-10-03 00:55:56 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 45.8 |
| 190b2703-e519-3735-bc2c-0ef8a4734c7a | -8.6488 | -66.7139 | 2024-10-03 00:55:56 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 71.4 |
| a53d74f6-b984-34a3-9ce5-b45c8195d874 | -8.6675 | -66.6762 | 2024-10-03 00:55:56 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 34d03076-018b-3fbf-bb9f-d25333a36793 | -8.9976 | -67.4094 | 2024-10-03 00:55:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 64.8 |
| bd568e0e-c8a7-3b4a-833d-e7dcdb924e66 | -9.0149 | -67.7423 | 2024-10-03 00:55:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 84.5 |
| dc73c3d3-16a1-3fbb-ae8d-501de52fd3a9 | -9.0334 | -67.7419 | 2024-10-03 00:55:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 341f65ea-b526-39db-9fe9-6ec1476b0a3f | -9.0515 | -67.871 | 2024-10-03 00:55:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 2e2a1af3-126c-3951-a94d-97b77c0169af | -9.0516 | -67.8525 | 2024-10-03 00:55:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 37.6 |
| 1b16f083-54f5-3a70-9139-a8c584cd477e | -9.1566 | -61.6758 | 2024-10-03 00:55:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 86.1 |
| 9efa7948-f0c1-314a-8f63-9ec06ae3fc9c | -9.4574 | -40.3641 | 2024-10-03 00:55:59 | GOES-16 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 68.3 |
| f99605b9-0041-3c15-8c2d-b4025a9e8379 | -9.1752 | -61.6749 | 2024-10-03 00:55:59 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 117.1 |
| 49c1bbb0-f6b6-314e-9a3c-e85867a58c39 | -9.1754 | -61.6558 | 2024-10-03 00:55:59 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 89ae2952-adeb-33bd-91db-dd70c28ac40b | -9.3839 | -61.0526 | 2024-10-03 00:56:00 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 87.9 |
| 7bfcfa92-39e4-3f5c-b8b2-47b4e50084dc | -9.4025 | -61.0517 | 2024-10-03 00:56:00 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 93.6 |
| 29c5e585-0f1d-318f-bc07-8c0b0eba4f06 | -9.3832 | -68.3441 | 2024-10-03 00:56:00 | GOES-16 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 13.7 |
| e1e58ab1-098b-3d1c-8d2f-93dfbb1abe8f | -9.4244 | -67.2313 | 2024-10-03 00:56:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 45.0 |
| 4e5e8f57-2815-3af3-a463-3f4f9bd1adc9 | -9.4367 | -64.5607 | 2024-10-03 00:56:00 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 9d83c093-9a01-335c-a38d-a3803909a702 | -9.4368 | -64.5419 | 2024-10-03 00:56:00 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 107.5 |
| 30b82a48-17d5-3cf1-83ac-31cf1fc84050 | -9.468 | -62.3857 | 2024-10-03 00:56:00 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 67.8 |
| bd61a265-6c94-3a1a-8904-886fe63da375 | -9.4865 | -62.4039 | 2024-10-03 00:56:00 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 5defca23-c9c8-31ee-b8b5-427d8b2b97bb | -9.4866 | -62.3849 | 2024-10-03 00:56:00 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 116.3 |
| e137205a-0e6d-30c5-b25b-24431a7a7c0d | -9.4939 | -68.508 | 2024-10-03 00:56:01 | GOES-16 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 50.7 |
| af8ac2df-344c-3491-97ee-7faefc011c05 | -9.494 | -68.4895 | 2024-10-03 00:56:01 | GOES-16 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 84.5 |
| b267ce1f-2896-309f-a4d8-aea86ddf6f20 | -9.5125 | -68.4891 | 2024-10-03 00:56:01 | GOES-16 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 36.1 |
| ed8b326b-c4dd-3eda-b97c-07b88c435cdf | -9.7173 | -64.2302 | 2024-10-03 00:56:02 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 53.0 |
| bfd4a8ac-d784-32dd-81e3-65756beeec8a | -10.1802 | -57.2848 | 2024-10-03 00:56:04 | GOES-16 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 86.4 |
| ed993972-c19c-3840-9297-49ad7eeabfe4 | -10.1804 | -57.265 | 2024-10-03 00:56:04 | GOES-16 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 83.3 |
| 2def07df-a764-3503-bd3e-212ae95fd004 | -10.6978 | -46.1514 | 2024-10-03 00:56:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 49.4 |
| 3662d435-2739-3d1f-b480-9ebd3f485df1 | -10.7165 | -46.1716 | 2024-10-03 00:56:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 52.7 |
| e3a3894c-aa25-3f6b-9658-8dcad5a8c91d | -10.6505 | -53.6994 | 2024-10-03 00:56:06 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 72.6 |


[Clique aqui para ver as próximas entradas](README22.md)

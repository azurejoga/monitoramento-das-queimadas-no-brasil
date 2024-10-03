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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d2cbdbe7-6b04-320d-86e5-a5340c9730c9 | -18.8406 | -42.9235 | 2024-10-03 00:36:50 | GOES-16 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 148.7 |
| 554ba0ad-f752-3769-add0-8f575388f874 | -18.8927 | -41.2248 | 2024-10-03 00:36:50 | GOES-16 | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 95.9 |
| 628f6a6f-ea61-3e0e-826d-42a11d6ae0e4 | -18.8935 | -41.199 | 2024-10-03 00:36:50 | GOES-16 | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 87.1 |
| 77c437fd-484d-3860-85af-b3a4bb1dbb6c | -18.8609 | -42.9182 | 2024-10-03 00:36:50 | GOES-16 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 73.8 |
| cafa054d-5fba-3c13-9c6f-a1a607fc6cda | -20.6617 | -42.0115 | 2024-10-03 00:36:59 | GOES-16 | CARANGOLA | MINAS GERAIS | Brasil | 3113305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 97.3 |
| cf1284fe-1bf2-36d8-8727-cfbdce61c405 | -20.6625 | -41.9858 | 2024-10-03 00:36:59 | GOES-16 | CARANGOLA | MINAS GERAIS | Brasil | 3113305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 82.5 |
| 5d7cb840-a696-36b0-9fa1-6301be72d8c8 | -21.306 | -47.6227 | 2024-10-03 00:37:03 | GOES-16 | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 1c10b3a7-c95b-3ff4-aeff-a0fa0b19d341 | -21.3067 | -47.599 | 2024-10-03 00:37:03 | GOES-16 | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 90.5 |
| d26a5d52-449b-3229-99e8-57f8b98279bc | -21.3456 | -55.6841 | 2024-10-03 00:37:04 | GOES-16 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 1f0113db-9c8c-3306-b339-fef42e6cdd8a | -21.346 | -55.6626 | 2024-10-03 00:37:04 | GOES-16 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 116.9 |
| 17e2141c-2cf4-31bc-b5f4-5c6bf984f54f | -21.8653 | -48.2127 | 2024-10-03 00:37:06 | GOES-16 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 47f74742-1871-3a17-8fcc-d6eb98937c44 | -22.3495 | -47.9515 | 2024-10-03 00:37:09 | GOES-16 | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 7a837d9d-8a4c-3900-a9d6-c65b4bb7be77 | -22.3502 | -47.9278 | 2024-10-03 00:37:09 | GOES-16 | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 137.8 |
| d597ca95-e600-32af-8a47-3ace09c366d6 | -22.3704 | -47.9462 | 2024-10-03 00:37:09 | GOES-16 | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 109.8 |
| 4af2add2-8ae6-3fa8-9159-d2a15225304f | -22.3711 | -47.9225 | 2024-10-03 00:37:09 | GOES-16 | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 194.5 |
| 6d35f615-8269-3e3b-b6db-2102248faeaa | -22.3719 | -47.8987 | 2024-10-03 00:37:09 | GOES-16 | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 95.8 |
| df8c0d97-7cca-30cf-9689-834891e876a1 | -1.0368 | -53.5171 | 2024-10-03 00:45:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| d9aaf2b5-280e-3a55-a155-984de1c28622 | -3.3854 | -42.2866 | 2024-10-03 00:45:25 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 218.7 |
| 4e4aa561-2d89-3497-aae1-7fe50c5e75f1 | -3.3855 | -42.263 | 2024-10-03 00:45:25 | GOES-16 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 146.5 |
| 62d24a52-78b9-35ad-92ee-01cc490f4736 | -3.4039 | -42.3094 | 2024-10-03 00:45:25 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 49.3 |
| 4428e772-c337-3625-9492-5f129bc763d4 | -3.404 | -42.2858 | 2024-10-03 00:45:25 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 363.5 |
| edfb95d4-a1f7-36c8-af22-bb07d8534eec | -3.4042 | -42.2621 | 2024-10-03 00:45:25 | GOES-16 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 228.2 |
| dd5edbfb-2b21-37a3-9fe2-ccf69e190a3c | -3.4227 | -42.2849 | 2024-10-03 00:45:25 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 3de09216-8b73-3ee0-948b-3e57060d665e | -3.4229 | -42.2612 | 2024-10-03 00:45:25 | GOES-16 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 49.6 |
| fa7bbd01-6178-3a77-a1d9-3c6e16a40a72 | -3.802 | -47.8104 | 2024-10-03 00:45:27 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 4eb125d6-a3d2-33f6-8d20-78c7a8d98ea4 | -4.0949 | -48.4894 | 2024-10-03 00:45:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 83.5 |
| cc23f74e-e12b-3958-92fb-59cd7439aae3 | -4.095 | -48.4679 | 2024-10-03 00:45:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 74.6 |
| e05ce937-5393-36b0-8551-32334a0e3e78 | -4.1134 | -48.4886 | 2024-10-03 00:45:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| c87eece0-4882-3590-8beb-5131c5efb319 | -4.4286 | -42.8431 | 2024-10-03 00:45:31 | GOES-16 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 781293b3-7735-31ec-ae1f-bb996f99c0ab | -4.4657 | -42.8877 | 2024-10-03 00:45:31 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 7cbf4de1-d20e-3bbd-8e49-f6508ee20a12 | -4.5373 | -43.3273 | 2024-10-03 00:45:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 56.9 |
| 64ef8058-babf-36fd-bb8e-39e6bed87d55 | -4.5375 | -43.304 | 2024-10-03 00:45:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 101.3 |
| 2b5b1c18-88cc-3820-8ffd-cbde7b7f098e | -4.58 | -48.0132 | 2024-10-03 00:45:32 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 0526d1dc-a4ae-379d-b522-199f788d0c57 | -4.9264 | -43.79 | 2024-10-03 00:45:34 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 83.4 |
| c4bc4fdf-402b-3c69-b1b0-2155dcb904cb | -4.9265 | -43.7669 | 2024-10-03 00:45:34 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 3fd958b6-5a43-3d2c-98b3-973fb52ecf18 | -5.2253 | -43.8164 | 2024-10-03 00:45:35 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 55.8 |
| 6e1fa7e2-585c-3bd5-bf0d-1823a368e241 | -5.2255 | -43.7932 | 2024-10-03 00:45:35 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 6917acb2-7b81-33a9-9d38-0e41f68ebd3a | -5.2441 | -43.8151 | 2024-10-03 00:45:35 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 298.3 |
| 6e9980f5-dddb-3365-8847-9a65441d98eb | -5.2443 | -43.792 | 2024-10-03 00:45:35 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 313.2 |
| 5ce87c6a-aadd-3d7e-b8ff-541285f6886f | -5.8547 | -44.5988 | 2024-10-03 00:45:39 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 65dee421-8229-3639-8052-aee878378d5a | -6.6453 | -54.952 | 2024-10-03 00:45:44 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 1e597540-a523-3a35-a30a-849011f08eee | -6.8777 | -59.0504 | 2024-10-03 00:45:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 0ff6dc69-fdb4-353f-8081-17f2e358f32a | -6.8778 | -59.031 | 2024-10-03 00:45:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 49e9fd4e-3132-33f9-9955-76921f74d184 | -7.2056 | -59.7886 | 2024-10-03 00:45:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 6f5aaac8-b931-3de4-885c-fd61effff788 | -7.6326 | -67.2013 | 2024-10-03 00:45:50 | GOES-16 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 38.7 |
| 260290f7-b3ce-3481-8cf2-3f12966a18a1 | -8.8506 | -45.5086 | 2024-10-03 00:45:56 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 94261394-6147-3eca-a7b6-4f588b917090 | -8.8695 | -45.5066 | 2024-10-03 00:45:56 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 50.0 |
| 8922d2be-5cf5-31ea-9ad9-b4e602d7bdcb | -8.6488 | -66.7139 | 2024-10-03 00:45:56 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 87.8 |
| 575fc5fb-a42e-368b-97ab-371556aac16f | -8.6489 | -66.6953 | 2024-10-03 00:45:56 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 39.9 |
| 739ae9ae-2694-309d-8382-cec127440146 | -8.649 | -66.6767 | 2024-10-03 00:45:56 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 32a06482-2913-3eba-8815-5abb94f4583a | -8.6675 | -66.6762 | 2024-10-03 00:45:56 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 7b88cc8e-e314-394b-ada9-80a10b90f080 | -8.8926 | -62.3348 | 2024-10-03 00:45:57 | GOES-16 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 55.8 |
| fb3a22fe-5ecf-3603-868d-ada3c3b5a8fc | -8.9791 | -67.4099 | 2024-10-03 00:45:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 44.9 |
| 5205e6c9-503d-39c1-b6dc-05d402c7fbe5 | -8.9976 | -67.4094 | 2024-10-03 00:45:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 53.0 |
| aef7942a-c484-395e-8254-df0a972489ca | -9.0149 | -67.7423 | 2024-10-03 00:45:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 93.1 |
| 25758742-e65a-3230-883c-ef08d3c693f7 | -9.0334 | -67.7419 | 2024-10-03 00:45:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 3e646f92-cce2-3e70-998b-a87cb5e929ae | -9.0515 | -67.871 | 2024-10-03 00:45:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 56.0 |
| ca564b8b-6613-31f0-a1a1-c130ed0233c6 | -9.1566 | -61.6758 | 2024-10-03 00:45:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 1195e917-c13b-3627-a2ce-ef741b2e91fc | -9.4574 | -40.3641 | 2024-10-03 00:45:59 | GOES-16 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 51.5 |
| cccbae54-abdf-3334-a28c-a141840f743f | -9.1752 | -61.6749 | 2024-10-03 00:45:59 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 144.4 |
| 4990b880-2649-3d3d-8cec-00fda036cca7 | -9.1754 | -61.6558 | 2024-10-03 00:45:59 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 72.6 |
| d2430c1e-07be-360f-90d5-f7b0e154b7d6 | -9.3839 | -61.0526 | 2024-10-03 00:46:00 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 114.5 |
| 81df874a-41d8-36db-bd6b-ea56fe0b663b | -9.4025 | -61.0517 | 2024-10-03 00:46:00 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 49112c10-2dd1-3bd9-9209-1fb782d1506f | -9.3832 | -68.3441 | 2024-10-03 00:46:00 | GOES-16 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 15.9 |
| b2acf358-da67-36ff-a351-4040f1c76c1a | -9.3833 | -68.3256 | 2024-10-03 00:46:00 | GOES-16 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 19.4 |
| ce3df8ec-3d6c-3f24-b6ae-ba0cc5262463 | -9.4367 | -64.5607 | 2024-10-03 00:46:00 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 735ddc8c-af19-36db-a04a-4742a04459c6 | -9.4368 | -64.5419 | 2024-10-03 00:46:00 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 112.7 |
| fd7cb1ca-fa42-3074-9cd3-6dbcbcb2669a | -9.468 | -62.3857 | 2024-10-03 00:46:00 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 8dd16c97-a877-37c5-8d19-891758f79cbc | -9.4865 | -62.4039 | 2024-10-03 00:46:00 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 44468cf7-f587-34e3-a4c4-8216e1e23aef | -9.4866 | -62.3849 | 2024-10-03 00:46:00 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 121.2 |
| 58e71b30-ba74-3513-8acc-37cca1309234 | -9.4939 | -68.508 | 2024-10-03 00:46:01 | GOES-16 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 43.1 |
| c232e3e0-dabb-36ba-8ce3-31b2690a0804 | -9.494 | -68.4895 | 2024-10-03 00:46:01 | GOES-16 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 77.5 |
| e43bdeac-74c7-3134-a3c1-65cd321ea872 | -9.5125 | -68.4891 | 2024-10-03 00:46:01 | GOES-16 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 52.6 |
| b9861a8a-f582-316f-8dc1-818cd8e3ae40 | -9.7173 | -64.2302 | 2024-10-03 00:46:02 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 51.8 |
| ca17e036-d23e-3ae6-b7ca-2a74a606d2ac | -9.9067 | -67.3294 | 2024-10-03 00:46:03 | GOES-16 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 42.9 |
| e50ae82d-8890-3ef0-8fa9-038f9d914937 | -10.129 | -56.7722 | 2024-10-03 00:46:04 | GOES-16 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 49.0 |
| c6f9d4b8-b82e-3d69-92bd-7d67fc6dd507 | -10.1292 | -56.7523 | 2024-10-03 00:46:04 | GOES-16 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 41.6 |
| 1aaf6796-a71f-3b79-aa7d-fb70e768c18a | -10.1615 | -57.2861 | 2024-10-03 00:46:04 | GOES-16 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 63.5 |
| e8cebc0b-9c8c-3b70-a8e9-96b138fdfcb4 | -10.1617 | -57.2663 | 2024-10-03 00:46:04 | GOES-16 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 9331cdd1-5b5d-3e33-b216-5905b5c2f263 | -10.1802 | -57.2848 | 2024-10-03 00:46:04 | GOES-16 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 102.9 |
| fa8c0b63-13df-330e-9d57-0a8447be806e | -10.1804 | -57.265 | 2024-10-03 00:46:04 | GOES-16 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 98.8 |
| 8c050538-66f6-3944-9a0d-07cb49ebab3a | -10.7165 | -46.1716 | 2024-10-03 00:46:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 57377cf1-d8a8-3e43-b8f5-6fe4bc5a907c | -10.6505 | -53.6994 | 2024-10-03 00:46:06 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 35ba33b7-cdf0-3d38-b1e0-7aef65cd0e3e | -10.9769 | -46.5443 | 2024-10-03 00:46:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 0526678c-0997-3d2f-9559-1e1ad49a48b4 | -10.8942 | -63.8971 | 2024-10-03 00:46:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 61.0 |
| e43f0b8c-cf9e-3b70-9d06-a1e8bbe75382 | -11.2565 | -60.6019 | 2024-10-03 00:46:10 | GOES-16 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 48b50995-23b6-355e-9721-4a04de710118 | -11.2566 | -60.5825 | 2024-10-03 00:46:10 | GOES-16 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 60.5 |
| f7bf8f06-3f9d-3ed9-b112-4e7fe640aab9 | -11.4357 | -54.305 | 2024-10-03 00:46:11 | GOES-16 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 54492519-96ee-38dc-bacd-b9e323d01993 | -11.6742 | -65.0172 | 2024-10-03 00:46:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 73.5 |
| cf36072c-58ba-3f4b-8a39-0f532eae468e | -11.693 | -65.0163 | 2024-10-03 00:46:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 8a353ab0-c82e-33f5-b348-0f70017e6eec | -12.2668 | -45.958 | 2024-10-03 00:46:15 | GOES-16 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 43.0 |
| 2872e85e-8ed9-3165-a9ee-2aaaefcc8173 | -12.3851 | -62.9828 | 2024-10-03 00:46:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 1760c74d-5dba-33e8-8446-09fbd4715b29 | -12.4038 | -63.0009 | 2024-10-03 00:46:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 98.9 |
| f9eada44-23fd-3a4f-9551-74c373f315e9 | -12.404 | -62.9817 | 2024-10-03 00:46:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 906a88d3-3c7e-3ae8-a704-cc5005a19693 | -12.5329 | -53.1212 | 2024-10-03 00:46:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 6d812bf9-bb86-3157-bb57-fe0e4a99b335 | -12.5332 | -53.1003 | 2024-10-03 00:46:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 007501fe-f695-3b7a-9e0c-e0c42a9c7c4a | -12.6295 | -63.1225 | 2024-10-03 00:46:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 26dd1207-2d6f-351d-a8e7-b146934670bc | -12.6484 | -63.1214 | 2024-10-03 00:46:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 117.8 |
| 63d53100-38da-342e-806b-6d673bc302d9 | -12.6486 | -63.1022 | 2024-10-03 00:46:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 93.3 |
| 2a54d881-be5f-3d56-8ef8-2e41daf216df | -12.8047 | -62.5163 | 2024-10-03 00:46:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 66.2 |


[Clique aqui para ver as próximas entradas](README21.md)

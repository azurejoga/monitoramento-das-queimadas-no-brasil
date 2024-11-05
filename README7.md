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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8e37b446-2eb1-35fc-aca7-462ed638bd2a | -8.9336 | -65.0471 | 2024-11-05 00:30:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 74.1 |
| c7ca4ed5-279f-3ff4-96cd-0d0a4ebf2a0d | -1.3876 | -52.1918 | 2024-11-05 00:30:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 1998d141-8aac-3642-8589-7a4b40a6c48c | -6.0853 | -43.9608 | 2024-11-05 00:30:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 108.1 |
| 513d0807-5f92-3083-95b5-0d71492f4695 | -4.4079 | -43.1252 | 2024-11-05 00:30:00 | GOES-16 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 63.6 |
| d692a9f2-3186-3b48-9d19-04c54f618ebe | -5.2155 | -47.4782 | 2024-11-05 00:30:00 | GOES-16 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 74311e8f-aae1-3890-905a-2ea301a55b47 | -3.1787 | -50.5807 | 2024-11-05 00:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| f05bbc54-2ed7-3c6d-ab5a-be808ec17d02 | -4.4268 | -43.1007 | 2024-11-05 00:30:00 | GOES-16 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 54.5 |
| f249698d-0737-31ca-8da2-40876874eb6e | -2.7881 | -51.4859 | 2024-11-05 00:30:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 42.7 |
| b711d407-713e-32e1-a749-e13824e11465 | -5.0731 | -44.1493 | 2024-11-05 00:30:00 | GOES-16 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 36.9 |
| dac44c8c-7fe0-3e38-9a73-bdf0132f1ffc | -3.9669 | -48.1716 | 2024-11-05 00:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 0e081ee4-91bc-37ae-b51c-17c163486a22 | -5.0724 | -44.2412 | 2024-11-05 00:30:00 | GOES-16 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 56.5 |
| d292e460-a715-38ef-9aa5-139ea024c828 | -4.4266 | -43.1241 | 2024-11-05 00:30:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 49.0 |
| dea65e17-4cfe-3bb7-8006-94ee8407ac68 | -3.4612 | -45.5299 | 2024-11-05 00:30:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 92.0 |
| 8693cd9a-29d6-3850-8df5-8e6c6b95605c | -3.4613 | -45.5075 | 2024-11-05 00:30:00 | GOES-16 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 41.4 |
| 75bb9536-1761-3bb4-b8e0-9251e71c62e2 | -3.5446 | -47.3855 | 2024-11-05 00:30:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 121.2 |
| 34637ecb-56c5-3d38-a4ed-b1599223b3b3 | -5.6944 | -45.8323 | 2024-11-05 00:30:00 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 145.1 |
| 9fd81f59-a2e4-38c3-96df-2cea83a1811f | -2.6506 | -48.5844 | 2024-11-05 00:30:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| fc2ecb3d-eef4-3f54-99ed-ab1bf3de472d | -3.5444 | -47.4073 | 2024-11-05 00:30:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| fa6c1e07-2143-3d53-b098-991206f9bc66 | -4.2429 | -48.5474 | 2024-11-05 00:30:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 7e8ad8a5-e51d-30e1-9090-640916fba7d9 | -4.408 | -43.1018 | 2024-11-05 00:30:00 | GOES-16 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 72.4 |
| fa109a8a-f6a4-3831-8a59-482ce39e29a9 | -5.2157 | -47.4563 | 2024-11-05 00:30:00 | GOES-16 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 743a1526-2a98-35c0-86e2-cea412bff10d | -11.8634 | -43.888 | 2024-11-05 00:30:00 | GOES-16 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 1ed6d434-273c-31ac-b25e-4594563fc53b | -12.4015 | -63.2884 | 2024-11-05 00:30:00 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 24c2cb2d-48ab-3416-a795-cb4873fbe8d8 | -9.8567 | -36.1111 | 2024-11-05 00:40:00 | GOES-16 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 77.0 |
| 11b5e585-5894-3abc-a13a-ba82d71ecc80 | -6.1041 | -43.9593 | 2024-11-05 00:40:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 308.5 |
| 1848489c-136a-31b3-90ec-b8af147a704f | -11.8639 | -43.8644 | 2024-11-05 00:40:00 | GOES-16 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 77.0 |
| dda2501e-4d0c-3f31-83d0-2856397e1f8f | -3.5444 | -47.4073 | 2024-11-05 00:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 93.1 |
| c90e5595-82f2-3335-b61c-676b8b48cb8b | -3.4798 | -45.5291 | 2024-11-05 00:40:00 | GOES-16 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 82.8 |
| bcae5366-0e9b-3a80-93ea-1d4f03c43c9d | -6.1043 | -43.9362 | 2024-11-05 00:40:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 85.4 |
| f795823c-6a5d-3278-a0bc-50ec6169e709 | -4.2459 | -48.0293 | 2024-11-05 00:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 42.8 |
| 9feafd1a-5bd2-3476-b66c-ecae1be118cc | -4.4079 | -43.1252 | 2024-11-05 00:40:00 | GOES-16 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 85.9 |
| e84957c4-2bfb-39e9-abff-3c3e25c16666 | -4.606 | -46.8758 | 2024-11-05 00:40:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 13989ccf-66bc-35bb-87aa-54e32f0a6654 | -6.1229 | -43.9578 | 2024-11-05 00:40:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 7e7d8a32-977b-3821-99bf-7cd090dc2cc8 | -3.461 | -45.5524 | 2024-11-05 00:40:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 44.8 |
| 377fd586-529b-3138-8458-e900c6e99cfc | -5.7131 | -45.831 | 2024-11-05 00:40:00 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 46.4 |
| 7704e03d-8b7b-39a6-9b99-9478b4f5afba | -3.0906 | -54.5073 | 2024-11-05 00:40:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 52.1 |
| e2f82f9c-0560-3702-9466-21d2af30c63e | -3.4799 | -45.5067 | 2024-11-05 00:40:00 | GOES-16 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 41.3 |
| e9603e81-61ab-3278-9deb-120de44597f7 | -3.563 | -47.4066 | 2024-11-05 00:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 47fb6e5d-a7ff-37a6-b121-15f351327135 | -2.8065 | -51.4855 | 2024-11-05 00:40:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 5fa4c725-3c5e-30e1-a889-f259b43e7f30 | -5.0537 | -44.2424 | 2024-11-05 00:40:00 | GOES-16 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 44.0 |
| b611e6cf-a7cd-32ef-8007-b821df17886f | -5.6944 | -45.8323 | 2024-11-05 00:40:00 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 124.0 |
| 056c8c27-447d-3cd5-8c0a-55dbe4ec01bc | -5.6946 | -45.8098 | 2024-11-05 00:40:00 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 46.2 |
| 10273b03-b90f-3507-93f0-dbd9ae39643d | -4.3806 | -47.2388 | 2024-11-05 00:40:00 | GOES-16 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 61c58c89-b323-3d5f-9ab1-cb9e18684c68 | -2.6507 | -48.5629 | 2024-11-05 00:40:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| fa4ef6ea-4ee0-3c4c-93cc-9d8942be2db4 | -3.5632 | -47.3629 | 2024-11-05 00:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 43.9 |
| 4de4b39e-5f4e-3ba3-9947-cc31f4f3268f | -3.9669 | -48.1716 | 2024-11-05 00:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| d4803337-e434-3cf7-aadb-159f1a083734 | -6.1039 | -43.9824 | 2024-11-05 00:40:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 94.1 |
| c2e3ec06-d9a6-3ffd-89b8-a10009d6da87 | -3.5446 | -47.3855 | 2024-11-05 00:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 197.2 |
| 0ab7c22e-63a0-391e-9230-da5f12031bdf | -3.5447 | -47.3636 | 2024-11-05 00:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| db73a942-fd4d-3f23-8a68-40fef9ef1f92 | -1.406 | -52.1916 | 2024-11-05 00:40:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 43.3 |
| d675ed7e-605e-322e-ba15-89080f770d36 | -11.8446 | -43.8674 | 2024-11-05 00:40:00 | GOES-16 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 238a85b8-5055-3ec4-8f7c-e3ad6a0f94da | -3.5631 | -47.3847 | 2024-11-05 00:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 159.1 |
| 05f05ca9-9707-396c-8907-0e54e69656cc | -5.0724 | -44.2412 | 2024-11-05 00:40:00 | GOES-16 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 43.1 |
| de5f839d-1e24-366b-bd3e-aced1c2df70b | -4.408 | -43.1018 | 2024-11-05 00:40:00 | GOES-16 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 102.4 |
| abf13656-fb60-3247-9181-737aa2600751 | -6.0853 | -43.9608 | 2024-11-05 00:40:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 5347d34e-47b1-358e-a75d-c39d51b15e61 | -3.4613 | -45.5075 | 2024-11-05 00:40:00 | GOES-16 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 62.0 |
| c79bc460-c846-3a51-9202-0a601505660a | -3.4612 | -45.5299 | 2024-11-05 00:40:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 136.0 |
| da254a70-86bd-33ea-9fbc-4ada72ee498a | -3.967 | -48.15 | 2024-11-05 00:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 97.2 |
| c14be8b2-9347-322e-b332-1c72371f4a7c | -3.1787 | -50.5807 | 2024-11-05 00:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 6755e814-55b6-398f-9b84-3e957b2871bc | -4.4268 | -43.1007 | 2024-11-05 00:40:00 | GOES-16 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 40.9 |
| b819172c-38e5-31be-a2e7-dc1e094acf22 | -5.6943 | -45.8547 | 2024-11-05 00:40:00 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 53.7 |
| 526a450a-6ce6-3d55-a948-1e4d912007d4 | -5.6758 | -45.8335 | 2024-11-05 00:40:00 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 2d0ec569-b5df-3f8d-a29e-1adc7f13365b | -5.6758 | -45.8335 | 2024-11-05 00:50:00 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 44.9 |
| 9f8525e3-83d4-3e89-98c6-3e14ef3d7a99 | -1.406 | -52.1916 | 2024-11-05 00:50:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 40.5 |
| 2ad45cf3-f1bc-3286-b145-2784f88d8b25 | -5.0724 | -44.2412 | 2024-11-05 00:50:00 | GOES-16 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 40.9 |
| 865cc52c-c4e4-3cbe-890c-13141a10c1b1 | -11.8639 | -43.8644 | 2024-11-05 00:50:00 | GOES-16 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 5f7478f0-05b9-307d-ae20-cffff5042bc2 | -6.1043 | -43.9362 | 2024-11-05 00:50:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 583d2561-f662-3b27-92c7-ed328ce85c56 | -3.4798 | -45.5291 | 2024-11-05 00:50:00 | GOES-16 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 75.9 |
| b4ab99b2-af26-3afe-b205-62905f814fd9 | -11.8634 | -43.888 | 2024-11-05 00:50:00 | GOES-16 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 58.7 |
| a9cd8ae3-dd7b-3a34-ace0-e50db88adddf | -6.0853 | -43.9608 | 2024-11-05 00:50:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 9fce725e-4c18-3939-8373-3596b3c88816 | -5.6943 | -45.8547 | 2024-11-05 00:50:00 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 53.7 |
| fa96faea-79f3-3269-987f-24a847cfdc0e | -3.5631 | -47.3847 | 2024-11-05 00:50:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 220.2 |
| 7926f767-ced5-3779-abe0-38d1b3ea3400 | -3.5632 | -47.3629 | 2024-11-05 00:50:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 06108018-d4c1-3941-8f49-0b5c753bc19a | -4.2243 | -48.5482 | 2024-11-05 00:50:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| eb3f7b6b-1a99-3c80-a62d-8a6ee6f4aa02 | -3.563 | -47.4066 | 2024-11-05 00:50:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 942e51a7-0688-3184-8307-fc334817ef23 | -5.6944 | -45.8323 | 2024-11-05 00:50:00 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 123.9 |
| bb648012-6e5a-3c4c-86fc-7a230ef7bf22 | -2.6691 | -48.5624 | 2024-11-05 00:50:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 072c1e57-0f02-309d-a894-a855a63ac875 | -3.5446 | -47.3855 | 2024-11-05 00:50:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 172.6 |
| f78ba623-6a82-366f-a3b5-9ea2685982fb | -5.0725 | -44.2182 | 2024-11-05 00:50:00 | GOES-16 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 35.7 |
| d46c2e9c-4328-3146-9fd7-f8e5ce063439 | -6.1229 | -43.9578 | 2024-11-05 00:50:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 73.1 |
| cc57f104-cc0f-3af5-b782-b859b40357ac | -4.408 | -43.1018 | 2024-11-05 00:50:00 | GOES-16 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 1ec47e4a-ff19-35d0-8f2f-06f395ca3c00 | -3.967 | -48.15 | 2024-11-05 00:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 102.4 |
| 63f536c8-450f-39e3-8ed4-a8eb38050481 | -3.5444 | -47.4073 | 2024-11-05 00:50:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 720a0368-203d-3280-a4fe-d3d0b8770fac | -3.5447 | -47.3636 | 2024-11-05 00:50:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| f7f62a62-e992-330f-9485-a46ecc1c3998 | -4.4266 | -43.1241 | 2024-11-05 00:50:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 78960ad5-b1ae-3c1f-ad30-6132088dd9fc | -2.6507 | -48.5629 | 2024-11-05 00:50:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 09444005-ff34-34d2-9bd0-9393e35a8240 | -6.1041 | -43.9593 | 2024-11-05 00:50:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 199.8 |
| 384d8f2f-2f33-30f9-9b75-1b55d48efe3e | -5.6946 | -45.8098 | 2024-11-05 00:50:00 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 48.4 |
| ea1107cc-9f8f-3ac2-ab67-5b6c9308f094 | -2.8065 | -51.4855 | 2024-11-05 00:50:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 5ac0d800-9379-3dbb-b941-e73d21269731 | -4.0481 | -46.9255 | 2024-11-05 00:50:00 | GOES-16 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 44.6 |
| c49e3341-713e-39f2-b940-09c6aaf3b243 | -4.4079 | -43.1252 | 2024-11-05 00:50:00 | GOES-16 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 86.2 |
| d9d77e7b-04f0-3050-8331-d87cb6d5997a | -6.1039 | -43.9824 | 2024-11-05 00:50:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 61.6 |
| dd5bc3d6-e592-3f92-a822-2e7f6c653037 | -4.4268 | -43.1007 | 2024-11-05 00:50:00 | GOES-16 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 62.8 |
| dee85da4-abb3-3818-befd-bf748910e044 | -3.4612 | -45.5299 | 2024-11-05 00:50:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 6b8b8b44-5865-3695-af8c-95a688f9450f | -6.521 | -35.2488 | 2024-11-05 01:00:00 | GOES-16 | MONTANHAS | RIO GRANDE DO NORTE | Brasil | 2407708 | 24 | 33 | nan | nan | nan | Mata Atlântica | 86.8 |
| c4f60258-f9f0-3031-b495-1b2550cbcb5f | -4.4266 | -43.1241 | 2024-11-05 01:00:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 6f734295-1ce3-35b4-ae9d-b3915f6db01f | -5.6946 | -45.8098 | 2024-11-05 01:00:00 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 47.3 |
| 3526019d-8ab9-303a-aa01-5fb10d92ae7d | -3.563 | -47.4066 | 2024-11-05 01:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 86.0 |
| 9a4c3da0-8d51-36df-9779-1e8195bf99ef | -3.5444 | -47.4073 | 2024-11-05 01:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 80.3 |
| 7beebfea-85f5-3861-a9f6-d0669387acdb | -4.4079 | -43.1252 | 2024-11-05 01:00:00 | GOES-16 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 93.6 |


[Clique aqui para ver as próximas entradas](README8.md)

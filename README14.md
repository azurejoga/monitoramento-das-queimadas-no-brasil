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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5329436a-e041-31b7-bb23-f730510c8a70 | -5.91935 | -45.42602 | 2025-10-12 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 918d8fda-dc51-3ecf-9312-5b1a79f6ecdb | -5.90524 | -38.47628 | 2025-10-12 04:14:00 | NOAA-21 | PEREIRO | CEARÁ | Brasil | 2310803 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ad9be714-73ce-3f69-ac70-54cefa0e3148 | -7.65931 | -42.5901 | 2025-10-12 04:14:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a26f74e1-53d3-301f-89da-8cda35e890d1 | -4.82481 | -43.13295 | 2025-10-12 04:14:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c02c3c32-efae-3678-be1f-41e698d0dc58 | -4.37597 | -46.53496 | 2025-10-12 04:14:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b4f7ab83-d3f3-3925-9753-2bf15fcc6ee3 | -11.67335 | -43.77316 | 2025-10-12 04:14:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 53ac1a28-c278-334a-9dde-30c878ac8e1d | -5.77901 | -42.47334 | 2025-10-12 04:14:00 | NOAA-21 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 37fef89c-57ec-392c-977d-f62b9c75f40d | -9.77964 | -42.95409 | 2025-10-12 04:14:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 64680e0d-e83f-33d3-8c2f-1274c00cdfb0 | -6.17887 | -44.86146 | 2025-10-12 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 39f6d47a-769f-32e5-8086-949703058f6f | -5.29225 | -44.4563 | 2025-10-12 04:14:00 | NOAA-21 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 7857f133-8e44-3a13-bb2e-f1e7caf136c4 | -6.28114 | -44.40642 | 2025-10-12 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0de31a91-b69d-3f4c-b22f-85c2e96707e4 | -8.98463 | -39.92285 | 2025-10-12 04:14:00 | NOAA-21 | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 1.9 |
| fe058f67-70ce-3bd1-8015-22a77bc2f127 | -7.70659 | -42.37087 | 2025-10-12 04:14:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 76b85026-038d-3428-bcc2-8d62495af304 | -7.65869 | -42.5721 | 2025-10-12 04:14:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 1d361d26-422a-3000-8a2b-fd6f3d0c828f | -10.06882 | -45.03799 | 2025-10-12 04:14:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3a5d3e9a-dfbc-33e9-b100-185e12ff0ae7 | -8.02118 | -44.44881 | 2025-10-12 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 421ff885-dd94-397f-b89c-19a4f909fe5e | -5.41583 | -40.98713 | 2025-10-12 04:14:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1aeb0057-90be-3c70-8a98-aa804fb77f04 | -6.27009 | -42.98822 | 2025-10-12 04:14:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8d5a5fad-7ffa-3e67-8d7c-4551022a8e58 | -8.15096 | -43.32214 | 2025-10-12 04:14:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b43010d2-9a76-352e-875e-ea805d59ec18 | -11.4465 | -43.48056 | 2025-10-12 04:14:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| afdffe14-1a78-3484-bc5a-d149ef9be03a | -7.43215 | -45.15444 | 2025-10-12 04:14:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 723554b9-1de6-3a19-b9f2-b963b0d0c9b0 | -6.83573 | -42.78814 | 2025-10-12 04:14:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3b2c6d72-3803-32d1-9abb-b10486966a64 | -5.81668 | -44.03172 | 2025-10-12 04:14:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a0efbac4-1b6d-3a82-9978-f87508279fb0 | -11.45036 | -43.47755 | 2025-10-12 04:14:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4e14bcf3-6f44-3a61-ac7d-320faa5de25b | -7.26263 | -40.12626 | 2025-10-12 04:14:00 | NOAA-21 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 662e8ec8-98cb-3671-af38-c8bdf583876e | -8.01021 | -39.59905 | 2025-10-12 04:14:00 | NOAA-21 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 480a456d-f25f-3f7b-b6c2-be60b2d6728a | -4.8188 | -43.14965 | 2025-10-12 04:14:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d8b8b9f0-b303-3688-8a28-a17f2e9e3800 | -6.33216 | -41.60189 | 2025-10-12 04:14:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| dafa070e-2c3d-359d-940d-1ca164b6babb | -5.20616 | -44.35748 | 2025-10-12 04:14:00 | NOAA-21 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d30cac65-e479-36de-930d-b87d2d6c90bd | -4.27954 | -46.93826 | 2025-10-12 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6f250a71-f279-34f4-a193-4b66cf69181c | -5.47828 | -43.39566 | 2025-10-12 04:14:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9545ec30-aec9-3bb6-8100-2e9e5fcccbd8 | -7.35928 | -44.79934 | 2025-10-12 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f79b870a-ac4c-39e8-ae7f-accd06212a78 | -5.47882 | -43.3922 | 2025-10-12 04:14:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 714db216-e18d-3244-b682-8abc3e3e444e | -7.98972 | -44.47579 | 2025-10-12 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9bc7dbcd-bb84-3e15-8983-1d57be2fb158 | -6.81048 | -42.97161 | 2025-10-12 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e204c312-e59f-341f-be15-5642706a07d5 | -7.85401 | -44.51582 | 2025-10-12 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1df67fe5-6aef-30d0-a3f1-cff87028adda | -5.96514 | -43.30714 | 2025-10-12 04:14:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 50032648-9658-3080-b3c0-408d8fb919c7 | -8.63163 | -47.00063 | 2025-10-12 04:14:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3f232371-d31f-35d6-b57f-04669e6fff65 | -5.43 | -41.36873 | 2025-10-12 04:14:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 7c4aefc0-e150-311c-bc9e-7f892edf739b | -7.01425 | -42.09698 | 2025-10-12 04:14:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| d0cddf6f-6e31-35f0-963f-1b9309a3b867 | -10.1791 | -44.58144 | 2025-10-12 04:14:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4ceab02e-61ec-3ec8-8ed0-5bb5d2601030 | -6.73253 | -42.20488 | 2025-10-12 04:14:00 | NOAA-21 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 681f08f5-329c-3e4a-9a30-a293cf7400a3 | -11.65254 | -41.6581 | 2025-10-12 04:14:00 | NOAA-21 | CANARANA | BAHIA | Brasil | 2906204 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9ace9a13-8d92-3519-b190-b367a1f54217 | -11.36901 | -44.00443 | 2025-10-12 04:14:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0aaea06c-0225-34bd-9a0e-d828e19a6606 | -7.35986 | -44.79572 | 2025-10-12 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ffe28c7c-8c58-3914-914d-ef917c2f70ee | -8.2171 | -43.33667 | 2025-10-12 04:14:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 224ef7c3-9877-31ee-8ee2-f77fa26c91a0 | -5.33627 | -43.42997 | 2025-10-12 04:14:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 47ab21ad-17ee-32c3-a862-8dc41045c328 | -7.3587 | -44.80296 | 2025-10-12 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 86eb8464-71f0-30d4-8356-583b151374ac | -6.26793 | -43.002 | 2025-10-12 04:14:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cac783a8-faac-30f9-85fc-a4b5fad03e33 | -7.5771 | -43.96506 | 2025-10-12 04:14:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b6aea029-532a-3100-8ef2-b4b7bfa0aa14 | -7.51658 | -44.60374 | 2025-10-12 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 669baf1f-f7e2-3488-bffc-d8f014d20053 | -3.84625 | -50.76743 | 2025-10-12 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| acc2d58a-c4c9-31d7-8f5e-93a144f36e3b | -6.04426 | -42.47617 | 2025-10-12 04:14:00 | NOAA-21 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| a8fad7e9-f276-34a4-85ca-8a4ef99863da | -5.70196 | -40.7195 | 2025-10-12 04:14:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 38dd6a3d-9cdc-361d-9bf7-43ce175dfe34 | -6.46809 | -44.64194 | 2025-10-12 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 332f535c-74bc-33be-8ae6-4feefa0badf6 | -6.66607 | -41.37007 | 2025-10-12 04:14:00 | NOAA-21 | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f51acb05-48c9-3d0a-9cf3-b9442490ac9a | -4.94695 | -44.7665 | 2025-10-12 04:14:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1c966a71-e6d6-358e-b205-3751a73be3f5 | -5.59432 | -41.10033 | 2025-10-12 04:14:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 53f594af-f17c-3da0-932e-28b0a5b32b34 | -4.81934 | -43.14621 | 2025-10-12 04:14:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ed8343a5-f8fe-3ec9-ba37-3c7d1542334c | -5.24 | -42.98374 | 2025-10-12 04:14:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 2.8 |
| deb73592-9284-33dc-9b4d-93ec396d02bc | -5.8355 | -49.02045 | 2025-10-12 04:14:00 | NOAA-21 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 769c3dc0-8dea-3f6b-9319-f43c01d560eb | -4.82097 | -43.13588 | 2025-10-12 04:14:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 06f6d4aa-5586-3c1e-9cd8-21a2d57484f4 | -6.98434 | -42.44498 | 2025-10-12 04:14:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 4a15e75a-f07e-3bd0-92df-7c9b8471630e | -6.2319 | -41.56822 | 2025-10-12 04:14:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 29be6b3a-8843-3583-8506-47e7585b71d1 | -7.67635 | -42.56767 | 2025-10-12 04:14:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 24b53807-3236-339a-88af-5a89f4f87d7f | -6.25428 | -43.02454 | 2025-10-12 04:14:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b999b84f-589f-3d5e-b6ed-dda77c1fa0c5 | -7.43343 | -42.97117 | 2025-10-12 04:14:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 2cc9edb1-b394-3ea8-b0a4-b6e7fb1f75b1 | -6.5686 | -39.5653 | 2025-10-12 04:14:00 | NOAA-21 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 660627b0-6eb6-398e-8f13-039abfba7e2e | -11.50233 | -43.49303 | 2025-10-12 04:14:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 13e31676-fc56-3f29-8f87-d88c27222953 | -6.5059 | -42.43814 | 2025-10-12 04:14:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| ece6eaac-1391-3e3e-adb8-299c4f82eddc | -5.65018 | -42.77378 | 2025-10-12 04:14:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 423e914d-75a5-3551-911a-7fd0cb1f2a0a | -7.88567 | -44.51004 | 2025-10-12 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e44baf52-c25f-3858-b510-be7784ab0d5c | -4.27648 | -46.93286 | 2025-10-12 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 67c07bd0-846d-31b7-8600-fe1968f9423c | -7.34922 | -43.85713 | 2025-10-12 04:14:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bfe08609-832c-31f5-b7a2-66f14dab2c83 | -6.4653 | -44.63783 | 2025-10-12 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dfc5d9b2-31dc-3d48-be56-76ba268ad537 | -6.17595 | -41.75383 | 2025-10-12 04:14:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2ed84764-1de8-3b0a-958b-c938b7247793 | -6.74423 | -42.87646 | 2025-10-12 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 55132527-58cb-34cb-b12d-fde995b526d8 | -5.39974 | -40.97395 | 2025-10-12 04:14:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 95fa9d9c-dc00-3cd4-92df-5db3ea5a9b0b | -6.22798 | -41.57133 | 2025-10-12 04:14:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a910ce3b-d202-3fe4-ac91-6bac10708bbb | -8.70728 | -46.83428 | 2025-10-12 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 11e8cade-4093-36d6-996d-3934ea15d13c | -7.2064 | -45.48661 | 2025-10-12 04:14:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 08191985-674b-355f-894c-d295fc1d6dcf | -6.74016 | -42.15578 | 2025-10-12 04:14:00 | NOAA-21 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 7b69ebb7-89f7-39fd-8727-e894db727b56 | -10.17537 | -44.53781 | 2025-10-12 04:14:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e64f717e-8050-36d7-b4a8-e71cccf10c4f | -11.49956 | -43.48896 | 2025-10-12 04:14:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a0b1649c-b738-35b4-a3b9-1125bfbc4fa3 | -7.87743 | -44.45433 | 2025-10-12 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 57507adf-85bd-335f-a503-8712235b4579 | -5.3072 | -42.87803 | 2025-10-12 04:14:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 1.4 |
| edcc9528-f1be-3be8-a1f7-86ddc5932b66 | -10.15664 | -44.54906 | 2025-10-12 04:14:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4bd116b0-13ad-3e50-8586-306d43c4a46b | -7.75255 | -44.21127 | 2025-10-12 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0f5c18e4-8aba-3fa1-a147-e82b11e22f92 | -7.43274 | -45.1508 | 2025-10-12 04:14:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 70423a5d-73f8-3747-a5ec-511f7e635c49 | -8.1916 | -43.32143 | 2025-10-12 04:14:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 10.4 |
| 7094e764-1c0e-3588-b4e1-43b44eb1e724 | -7.88455 | -44.51715 | 2025-10-12 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 45f58d8f-20ce-3f62-a28b-dd25f5bdaa97 | -6.64937 | -44.27594 | 2025-10-12 04:14:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e6744b41-75fc-3b49-9876-f837b112bc26 | -11.75418 | -43.31456 | 2025-10-12 04:14:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9331d0de-57ba-336f-aeb7-b2c8df4caf27 | -7.62544 | -47.50905 | 2025-10-12 04:14:00 | NOAA-21 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d2305221-cf0e-3cad-b771-d35b1c6b2a83 | -7.50813 | -44.63525 | 2025-10-12 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9c2da644-781d-3806-971b-61124b28d64f | -5.34179 | -43.43793 | 2025-10-12 04:14:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b1e028b2-c467-39a5-a921-e6f2beb577a9 | -5.66798 | -42.6815 | 2025-10-12 04:14:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f9becb3a-78fb-3b3a-bbb0-2ff19d904b75 | -7.50369 | -45.12782 | 2025-10-12 04:14:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| d543b44b-2521-3955-b694-718e74a5cda5 | -7.14613 | -42.49902 | 2025-10-12 04:14:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 25547222-07aa-3dc1-9645-1f96cda820c0 | -5.29013 | -44.4597 | 2025-10-12 04:14:00 | NOAA-21 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |


[Clique aqui para ver as próximas entradas](README15.md)

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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 484ee4da-28e5-3dbb-b985-e5466b97998e | -7.99407 | -39.42648 | 2024-12-13 00:20:00 | TERRA_M-M | SERRITA | PERNAMBUCO | Brasil | 2614006 | 26 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 1792b092-b3d3-3fba-8f1a-b8c6577a94ec | -4.51075 | -42.06297 | 2024-12-13 00:20:00 | TERRA_M-M | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 0286d7d5-fa3e-3f62-b1c8-69bebe9c07dd | -8.7143 | -44.00816 | 2024-12-13 00:20:00 | TERRA_M-M | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 66eae1ff-8821-3ce7-8bd1-c2506a97d9be | -3.32422 | -45.70695 | 2024-12-13 00:20:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 67b73356-7e99-37eb-84ee-d808cf49ecae | -4.55659 | -43.57791 | 2024-12-13 00:20:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 15.8 |
| fa63ce76-accc-363a-a6e7-48ed1c93c98f | -6.11768 | -43.95913 | 2024-12-13 00:20:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 09f5577e-76c0-3334-9579-a2e5f7e61db8 | -8.16626 | -43.82178 | 2024-12-13 00:20:00 | TERRA_M-M | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 32c7a68f-f592-3966-ac52-271c0f76d7f2 | -4.81001 | -44.47582 | 2024-12-13 00:20:00 | TERRA_M-M | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 28cd90ca-0e3b-3ee8-8a3a-cf7f5746ebd4 | -6.77011 | -44.82246 | 2024-12-13 00:20:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 7a987131-ba2b-3fcb-9876-0f1cfa3e730e | -3.30378 | -43.5313 | 2024-12-13 00:20:00 | TERRA_M-M | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| d42e53a7-8d3e-39ac-aa36-c22117dd194e | -3.83553 | -41.5724 | 2024-12-13 00:20:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 15.4 |
| 35d33598-27a3-3862-a80a-63a3b51a6caa | -5.96814 | -43.37374 | 2024-12-13 00:20:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 5.7 |
| dd6cf1ab-451d-38da-ba52-78c46909df7c | -7.98821 | -35.11077 | 2024-12-13 00:20:00 | TERRA_M-M | SÃO LOURENÇO DA MATA | PERNAMBUCO | Brasil | 2613701 | 26 | 33 | nan | nan | nan | Mata Atlântica | 11.9 |
| 4980a59b-2c51-385f-a438-8edda522f6e9 | -6.74504 | -35.10453 | 2024-12-13 00:20:00 | TERRA_M-M | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 27.0 |
| 6bd89eb6-2aba-399a-b1d1-d4242332c5a6 | -5.22232 | -43.29538 | 2024-12-13 00:20:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 31.6 |
| 7fba3caa-5934-3bd6-ace9-e5c6d6e243db | -5.39522 | -40.66839 | 2024-12-13 00:20:00 | TERRA_M-M | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 329236c3-eb1c-364c-bf77-4ac3d82f7e73 | -9.2889 | -39.27191 | 2024-12-13 00:20:00 | TERRA_M-M | CHORROCHÓ | BAHIA | Brasil | 2907707 | 29 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 8e6156f6-5d43-3352-9dda-8f9b0f057653 | -4.16738 | -42.44799 | 2024-12-13 00:20:00 | TERRA_M-M | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 39.3 |
| a2de5a79-fb08-37e3-900a-1d4f835c3e92 | -3.32214 | -45.69162 | 2024-12-13 00:20:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 495fc025-2a95-31f5-a459-39fa1a37c0a1 | -9.29014 | -39.28085 | 2024-12-13 00:20:00 | TERRA_M-M | CHORROCHÓ | BAHIA | Brasil | 2907707 | 29 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 4815c186-b438-3551-83e1-e17aa5386985 | -2.7165 | -45.53786 | 2024-12-13 00:20:00 | TERRA_M-M | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 1a4dd981-c797-3290-8a76-701d02480eeb | -6.62426 | -39.17932 | 2024-12-13 00:20:00 | TERRA_M-M | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 5.8 |
| dd39c043-af2c-3088-86f8-6f1d4415e334 | -3.25141 | -42.41079 | 2024-12-13 00:20:00 | TERRA_M-M | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 806d39a7-dd44-3dbb-bdbd-325e4c7cc08e | -5.45273 | -44.81796 | 2024-12-13 00:20:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 28.9 |
| 147d5feb-8d68-3a27-a9ea-1323dd419c0e | -4.30759 | -45.93395 | 2024-12-13 00:20:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 7537bce7-40ce-38bd-bd13-fe919a322e49 | -9.00747 | -36.15975 | 2024-12-13 00:20:00 | TERRA_M-M | CANHOTINHO | PERNAMBUCO | Brasil | 2603702 | 26 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| e763108e-e0da-334f-958b-835f255dfe10 | -2.83619 | -42.27242 | 2024-12-13 00:20:00 | TERRA_M-M | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7906b8d0-58fd-33e1-b9b1-8c0a7d15e5d0 | -3.29651 | -45.58755 | 2024-12-13 00:20:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 7.8 |
| b2015138-8192-35e8-8062-b09e9168c0cc | -2.96591 | -40.22405 | 2024-12-13 00:20:00 | TERRA_M-M | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 5.0 |
| e06889f4-7847-394f-a5d1-448210d4195d | -6.05754 | -44.03657 | 2024-12-13 00:20:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 21.5 |
| e9199363-624a-3fdd-b025-8c7f70837c01 | -4.52122 | -42.07117 | 2024-12-13 00:20:00 | TERRA_M-M | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 11.6 |
| e98d9e43-5563-3142-bce3-55e94fa9384c | -7.15207 | -41.46419 | 2024-12-13 00:20:00 | TERRA_M-M | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| f65d1172-fab6-3852-9885-3b67e8bf774f | -6.75888 | -44.82444 | 2024-12-13 00:20:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| b8ac79c2-b2ca-34c6-aaf6-308235b8d2e9 | -4.31381 | -45.92741 | 2024-12-13 00:20:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 16.5 |
| e92de990-b08b-3d85-b541-6c1b4bf33b99 | -3.47432 | -45.79114 | 2024-12-13 00:20:00 | TERRA_M-M | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 35.8 |
| 359dbb6d-2df6-389b-90d1-d00ef9be9602 | -5.76123 | -40.98963 | 2024-12-13 00:20:00 | TERRA_M-M | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 72a0afb4-9a17-3e27-ac21-e6ae3b3dd38d | -7.45676 | -34.94375 | 2024-12-13 00:20:00 | TERRA_M-M | CAAPORÃ | PARAÍBA | Brasil | 2503001 | 25 | 33 | nan | nan | nan | Mata Atlântica | 15.2 |
| 9077686a-0fbc-31f7-90c6-df367232ec35 | -2.29509 | -45.73063 | 2024-12-13 00:20:00 | TERRA_M-M | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 10.5 |
| c662c369-e23d-37b4-9979-d97adfb9ed02 | -5.73453 | -39.54002 | 2024-12-13 00:20:00 | TERRA_M-M | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 18.9 |
| 118ff373-3a45-3cd7-bbe8-d0b886fea329 | -2.83938 | -40.30267 | 2024-12-13 00:20:00 | TERRA_M-M | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 11.7 |
| 34e0a227-6555-3855-aa8d-1dbf50959c1e | -4.54518 | -43.57378 | 2024-12-13 00:20:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| a65c68d4-8eb9-34e9-9408-558b54fc568e | -4.55668 | -43.58366 | 2024-12-13 00:20:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 91606dfd-7bad-364c-b15a-45a660d793e2 | -5.38328 | -43.50215 | 2024-12-13 00:20:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| f836e14d-f090-3518-a992-d5847120260a | -3.47318 | -45.80079 | 2024-12-13 00:20:00 | TERRA_M-M | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 415643b1-95d4-34b5-8d22-ffe0ba03d8f1 | -8.37051 | -35.12851 | 2024-12-13 00:20:00 | TERRA_M-M | IPOJUCA | PERNAMBUCO | Brasil | 2607208 | 26 | 33 | nan | nan | nan | Mata Atlântica | 19.3 |
| a4b23b8b-bd30-3d46-afd5-0b22ccc922f2 | -4.25251 | -41.92923 | 2024-12-13 00:20:00 | TERRA_M-M | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 15.1 |
| 74ae94fc-ee53-3fce-b940-7c2ef9e5acb9 | -5.46379 | -44.81653 | 2024-12-13 00:20:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 6ebe0611-f230-3a72-9699-58465b91a7b0 | -5.19882 | -37.69622 | 2024-12-13 00:20:00 | TERRA_M-M | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 50e420a5-a340-3a1f-bbef-1e666af95dbc | -5.39399 | -40.65952 | 2024-12-13 00:20:00 | TERRA_M-M | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 75aeaffe-db8a-3b75-9d0b-238119fe6257 | -6.92566 | -43.50714 | 2024-12-13 00:20:00 | TERRA_M-M | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 257.4 |
| 3f45f0fd-dcec-39a3-8cbe-1702e2be21f9 | -3.14785 | -45.58932 | 2024-12-13 00:20:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 64.8 |
| c7373999-697a-3edd-86dd-1dee2b9c8607 | -3.06218 | -46.48048 | 2024-12-13 00:20:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 4a8acc23-02ff-39d8-aaba-923fd7fb7d67 | -3.59373 | -40.8285 | 2024-12-13 00:20:00 | TERRA_M-M | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 543b7750-4a03-345f-8d81-fc09db8ddd55 | -3.36307 | -42.28312 | 2024-12-13 00:20:00 | TERRA_M-M | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 44cd1852-b3f2-343b-a9d9-4d3e205feb05 | -3.25273 | -42.42032 | 2024-12-13 00:20:00 | TERRA_M-M | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 4fe9c1d4-35cc-3224-a1fb-b1ee424d6da7 | -6.97042 | -43.00334 | 2024-12-13 00:20:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 40dd3e6e-e72d-364c-9e7f-ebc400f052c1 | -4.64929 | -43.81126 | 2024-12-13 00:20:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 3ce3cf8a-cb5e-3d08-9c61-75cc2ce04e69 | -5.21398 | -43.30783 | 2024-12-13 00:20:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 258b429e-c182-3bca-965d-48154955dcf8 | -5.45091 | -44.80388 | 2024-12-13 00:20:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 34.4 |
| 22a1781a-bd3d-34e5-8777-88ae5ce33b67 | -3.98475 | -44.56384 | 2024-12-13 00:20:00 | TERRA_M-M | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 8643930d-5c3c-3003-8274-da68be2c941e | -3.47648 | -45.80672 | 2024-12-13 00:20:00 | TERRA_M-M | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 36.4 |
| 8cdfc4a5-7ca9-3efd-b502-d8f9266f7f44 | -3.18599 | -45.6146 | 2024-12-13 00:20:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 14.5 |
| c77a9247-2b4b-3d8e-b12a-02a2260770de | -5.96662 | -43.36253 | 2024-12-13 00:20:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 0e107678-1e19-3250-a929-51a12bf8495a | -2.8305 | -40.30393 | 2024-12-13 00:20:00 | TERRA_M-M | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 16.0 |
| f884580e-1eca-3dea-85a8-f856d7a794a9 | -3.4827 | -45.78363 | 2024-12-13 00:20:00 | TERRA_M-M | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 08c54298-999b-305b-ba54-edc646d1cd58 | -9.32275 | -36.01154 | 2024-12-13 00:20:00 | TERRA_M-M | MURICI | ALAGOAS | Brasil | 2705507 | 27 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| 453b2fb6-f813-3bc1-bbde-3e8e07aa04c0 | -4.16605 | -42.43827 | 2024-12-13 00:20:00 | TERRA_M-M | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 19.6 |
| 1db30dc3-cb5a-3b51-b852-d90c4ca3f89f | -5.08379 | -42.56266 | 2024-12-13 00:20:00 | TERRA_M-M | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 438d6839-3d5a-3686-8af6-4a7d5ee8e77d | -7.21014 | -35.06211 | 2024-12-13 00:20:00 | TERRA_M-M | CRUZ DO ESPÍRITO SANTO | PARAÍBA | Brasil | 2504900 | 25 | 33 | nan | nan | nan | Mata Atlântica | 124.1 |
| 7e7c1400-9812-3188-99c0-c95731bce772 | -6.56914 | -39.4413 | 2024-12-13 00:20:00 | TERRA_M-M | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 13.8 |
| 864a0bc5-5d69-35bb-9c05-ffbbd3bed902 | -6.95359 | -43.49771 | 2024-12-13 00:20:00 | TERRA_M-M | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 7d04ce69-2fbb-3579-a5cc-fb72d723108f | -3.48806 | -45.80514 | 2024-12-13 00:20:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 78da04ab-b572-3adb-b0cd-51b38ebdd104 | -6.63337 | -35.0494 | 2024-12-13 00:20:00 | TERRA_M-M | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| 8a75d3b8-d878-362a-b9ad-d0ec618e8666 | -5.95814 | -39.68099 | 2024-12-13 00:20:00 | TERRA_M-M | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 14.0 |
| ce42bec1-15a9-3cdc-bbb2-64b31b1abd84 | -10.16412 | -36.30302 | 2024-12-13 00:20:00 | TERRA_M-M | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 1f28e07d-dc15-3461-9930-9e7d1aa919ff | -4.76946 | -44.41482 | 2024-12-13 00:20:00 | TERRA_M-M | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 27.7 |
| 1d1e2a9f-8f5d-343f-9a78-45c43088da83 | -3.26584 | -46.92899 | 2024-12-13 00:20:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 133.5 |
| d67da448-b7a6-36e8-b3bc-87f163cf04cd | -5.24306 | -45.14502 | 2024-12-13 00:20:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 4f829537-b969-3bc4-bc87-71410665f8c2 | -4.64277 | -42.87843 | 2024-12-13 00:20:00 | TERRA_M-M | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 84a7d3d7-3ef1-3e97-8edd-b5c193f558f4 | -5.73327 | -39.53104 | 2024-12-13 00:20:00 | TERRA_M-M | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 18.5 |
| f6f97c7b-e0bd-3a26-a224-8a394e322b30 | -5.62518 | -44.8318 | 2024-12-13 00:20:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 1c55fb63-f1fd-32db-938f-cc5cce73f677 | -3.87155 | -40.64518 | 2024-12-13 00:20:00 | TERRA_M-M | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 6af208f0-37a1-38c5-a2af-ab445b12f1cc | -5.58204 | -43.61679 | 2024-12-13 00:20:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 7b65fb20-5868-346d-b5c5-7b2612ca71de | -11.77987 | -44.17038 | 2024-12-13 00:20:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 6762766b-c109-3ae3-a86d-14abcb110c77 | -11.86301 | -46.95212 | 2024-12-13 00:20:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 36b1b9b0-9973-33b3-8489-67b803bc0143 | -3.27328 | -45.50008 | 2024-12-13 00:20:00 | TERRA_M-M | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 86fdc643-49c7-365c-8b0b-318ef690cb7a | -9.81265 | -36.27317 | 2024-12-13 00:20:00 | TERRA_M-M | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 50.3 |
| be4149ff-7f25-3baf-a33a-db769a3b2888 | -8.26388 | -48.01939 | 2024-12-13 00:20:00 | TERRA_M-M | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 6fcfe28b-e1ea-3c84-8c7d-e4b6e2598bc2 | -4.42889 | -44.13951 | 2024-12-13 00:20:00 | TERRA_M-M | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 7d4508f1-4dcf-3ad5-b0b6-57520ab5156f | -7.99532 | -39.43539 | 2024-12-13 00:20:00 | TERRA_M-M | SERRITA | PERNAMBUCO | Brasil | 2614006 | 26 | 33 | nan | nan | nan | Caatinga | 11.9 |
| d3883673-ae61-38f1-a5d5-47a46818c428 | -3.91651 | -40.69547 | 2024-12-13 00:20:00 | TERRA_M-M | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 3.6 |
| c503432d-a162-34c5-8f84-e56efb07dc1b | -7.10961 | -38.90232 | 2024-12-13 00:20:00 | TERRA_M-M | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 5.5 |
| de7dc707-0952-32f5-9314-62cfbed1b77c | -6.56787 | -39.43234 | 2024-12-13 00:20:00 | TERRA_M-M | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 14.9 |
| 834ab22a-78e1-3772-b844-dc1f9566ca92 | -9.92663 | -36.28361 | 2024-12-13 00:20:00 | TERRA_M-M | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 10.4 |
| cbcda7f1-add3-32b7-a97d-b7e9eaf7a58e | -6.59303 | -44.16614 | 2024-12-13 00:20:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 80cbf40c-5da2-320b-9b09-b281da0aba7c | -11.52226 | -45.00691 | 2024-12-13 00:20:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 6ac60b2c-e641-3510-aaee-b45aee864d68 | -9.08135 | -35.42022 | 2024-12-13 00:20:00 | TERRA_M-M | PORTO DE PEDRAS | ALAGOAS | Brasil | 2707404 | 27 | 33 | nan | nan | nan | Mata Atlântica | 11.3 |
| 5bff7b04-546f-34bd-9d9b-82d425a234a8 | -6.91541 | -43.50851 | 2024-12-13 00:20:00 | TERRA_M-M | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 63050d84-e128-3957-866f-2738d6af7b08 | -6.30736 | -43.46912 | 2024-12-13 00:20:00 | TERRA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 25.5 |
| 5fc002f4-ffd8-3f27-ba83-da6add8c00c9 | -7.58123 | -47.12392 | 2024-12-13 00:20:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 17.2 |


[Clique aqui para ver as próximas entradas](README4.md)

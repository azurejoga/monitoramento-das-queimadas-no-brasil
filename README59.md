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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e816a5f9-f7a2-3566-bad0-f29e1f4fcc5c | -6.07037 | -41.90324 | 2025-10-17 04:19:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e924f4c6-aa44-3544-8acf-be79702e25a9 | -7.45135 | -46.84393 | 2025-10-17 04:19:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 20206faf-3ba6-372f-9346-c9cb25d03203 | -5.90844 | -44.74557 | 2025-10-17 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 33e46ce6-3139-38d0-bc26-074435c3946f | -8.40317 | -46.23396 | 2025-10-17 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dba1fe84-9b3d-379c-b85c-a69bbbf667f1 | -10.11782 | -44.56425 | 2025-10-17 04:19:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 21c2b4af-31f2-3793-b4e5-286f633616d8 | -8.4021 | -46.21923 | 2025-10-17 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 226b7993-6ca0-3ee5-a257-4217055b1c19 | -11.42177 | -44.21321 | 2025-10-17 04:19:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0e3c561f-ca9e-36c1-804f-1c8aaf50314b | -8.23943 | -44.02144 | 2025-10-17 04:19:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 76bd94b8-3415-38dc-8976-a336d9b3d8fb | -7.48228 | -42.7588 | 2025-10-17 04:19:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 0d4e45c2-8566-36ca-a021-ab6992629187 | -5.20862 | -46.19402 | 2025-10-17 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| de201e0a-6686-3d1a-8126-133b7f97e878 | -7.9857 | -44.14447 | 2025-10-17 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a9d102e1-f2fc-34c5-907e-eda724aa35d1 | -10.00453 | -47.48761 | 2025-10-17 04:19:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1250b3c6-e430-3d06-910e-4e3b8ff6bcc9 | -9.89746 | -47.66871 | 2025-10-17 04:19:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 18428c2a-1256-38d5-b893-f0d59f2ee2c8 | -5.25383 | -44.20808 | 2025-10-17 04:19:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2bc75179-7345-3dd1-82e6-d391291d3f1b | -7.03237 | -41.81899 | 2025-10-17 04:19:00 | NOAA-21 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 9c54fa98-b49c-373d-ade8-701186e1fb03 | -10.10023 | -44.61206 | 2025-10-17 04:19:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fe1dd03d-2055-3793-889a-3be5f264a59a | -4.92197 | -46.73048 | 2025-10-17 04:19:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d9c8fc88-9312-3391-acb2-ae7682282671 | -5.52005 | -43.3076 | 2025-10-17 04:19:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 63ca0796-1570-3f2e-8ba0-38eba3642a6b | -10.80786 | -43.93581 | 2025-10-17 04:19:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ed753fc0-0442-305b-b382-288a965f18d8 | -9.25056 | -44.36664 | 2025-10-17 04:19:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8424fac8-117c-3496-8aff-0e9da532b604 | -6.99962 | -46.9882 | 2025-10-17 04:19:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e332c5b3-a9dc-3500-a852-0774949b8c46 | -11.39507 | -44.13751 | 2025-10-17 04:19:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 65e1c281-51ff-3d35-93e2-dad0c00b8838 | -5.97896 | -42.79685 | 2025-10-17 04:19:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| b38018be-9ade-35be-ab0f-47499524d6dc | -5.18543 | -44.27841 | 2025-10-17 04:19:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e2d8eb35-475c-34fd-99ee-eb7318d4f687 | -9.70291 | -44.56417 | 2025-10-17 04:19:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7b9f7cc3-d2ff-3607-be52-bb1acd0d9c18 | -8.44937 | -44.18065 | 2025-10-17 04:19:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0291d75a-ab6d-3824-a229-29236a62da9f | -6.03402 | -41.90575 | 2025-10-17 04:19:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| a3b1757c-62d4-3572-b888-d86347891301 | -10.50327 | -43.41921 | 2025-10-17 04:19:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 05a6a86c-db9f-3340-ba59-680fdc2e2c47 | -6.20374 | -41.74299 | 2025-10-17 04:19:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 0cd1cdd7-f9d5-38a6-ad67-dc44faa6e4e2 | -8.2577 | -43.33909 | 2025-10-17 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| fb10a0bb-7f6d-3f45-bfaf-9ad79a150620 | -9.7205 | -48.91773 | 2025-10-17 04:19:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 1abd0f1d-2cc3-389f-bbb2-e8e4bb709b10 | -6.14108 | -41.72544 | 2025-10-17 04:19:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 481865c9-7908-364a-9ef6-a802cc89f76f | -7.68471 | -42.55851 | 2025-10-17 04:19:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 2704c797-75bf-3bf4-995f-d2d5f9b60501 | -4.21777 | -48.36213 | 2025-10-17 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 450344aa-220a-326d-88b2-8fa592bfe64c | -9.5754 | -49.11292 | 2025-10-17 04:19:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 02a115bb-fb0a-3e55-a7b3-de25078d5dd1 | -7.94965 | -44.11367 | 2025-10-17 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 120a1e80-755b-3406-bcfa-3ebf8ac97c89 | -5.91725 | -44.75401 | 2025-10-17 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d5d810ea-2b1b-36a9-9653-884ce780b384 | -6.0762 | -41.91216 | 2025-10-17 04:19:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 54a9cbf1-4669-38c8-884a-ff2f34c7b7c7 | -5.51452 | -43.86802 | 2025-10-17 04:19:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2fa54662-8b33-3bf0-b937-e6e71230920e | -4.46531 | -48.27391 | 2025-10-17 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5a853a0f-e2a0-3be1-bfe5-20e2bd44aadf | -8.22272 | -43.99712 | 2025-10-17 04:19:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9f07aae4-53c8-3635-bc60-ba2975d365ed | -5.85425 | -43.87145 | 2025-10-17 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9dc7064b-a0cc-3cfa-b85b-5d887a7299ea | -5.20321 | -43.74818 | 2025-10-17 04:19:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d450a84b-07de-39dc-a776-09801d52694c | -5.33664 | -43.08677 | 2025-10-17 04:19:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6f2cfda4-048e-30ba-b56c-983d093da29d | -10.50387 | -43.43853 | 2025-10-17 04:19:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 25.4 |
| bda2c29e-47f2-38bc-9ce5-49463582e94c | -10.51024 | -45.04088 | 2025-10-17 04:19:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2b42c8af-7506-345b-9566-1637af15437b | -9.13172 | -46.64083 | 2025-10-17 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dd3e20aa-4113-3976-8feb-3d4689186214 | -6.60739 | -44.80002 | 2025-10-17 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2473443e-c7a4-3d77-a4db-c4f512d651e9 | -6.13988 | -41.73348 | 2025-10-17 04:19:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 8d137da0-ce90-32af-b649-b8e6abd2ffaf | -9.0864 | -48.02872 | 2025-10-17 04:19:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 15.7 |
| d9a3cbc3-3a08-3968-b7b3-3be5ff38841e | -3.84124 | -50.97711 | 2025-10-17 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 73de7bb1-3a73-3763-ade6-22355cd2e999 | -4.77781 | -42.82541 | 2025-10-17 04:19:00 | NOAA-21 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 61922b45-a693-3968-98fc-05129de139d9 | -9.05532 | -45.14046 | 2025-10-17 04:19:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 21316bbb-56c0-3077-a6cf-930f74c651d7 | -11.39931 | -44.22474 | 2025-10-17 04:19:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c1bced30-3987-3e0a-953e-3ef30e6eb435 | -6.09 | -42.39126 | 2025-10-17 04:19:00 | NOAA-21 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8c5efbe0-9a0f-3ab0-b935-9eaa7870e844 | -9.13523 | -46.59724 | 2025-10-17 04:19:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 03f916fa-e25d-3f97-b525-ae9a4f5ef3dc | -7.7622 | -42.45848 | 2025-10-17 04:19:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 0ad1c1bc-da7d-3225-927d-5e2c498c42a6 | -6.2036 | -41.76632 | 2025-10-17 04:19:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 64dfc6d4-edcc-33a1-a1b5-ca02b14d31fa | -5.51121 | -43.86751 | 2025-10-17 04:19:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ea0c1fff-7a94-3c73-a61b-4215436ff3b5 | -6.19072 | -42.99294 | 2025-10-17 04:19:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| aa750a12-27c8-3692-940e-af1bf5d4b529 | -8.47271 | -50.10326 | 2025-10-17 04:19:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1d44a0ce-7e8a-3acd-9cca-c5f104a85f43 | -8.25645 | -44.06366 | 2025-10-17 04:19:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 48932571-a32d-379e-a8b5-ec52728f359e | -10.5015 | -43.4076 | 2025-10-17 04:19:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7387d1c3-fdbc-3599-b430-4089fabef806 | -6.69178 | -40.86385 | 2025-10-17 04:19:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 21c36c1b-5070-398b-896e-a81229b35900 | -6.75714 | -42.36491 | 2025-10-17 04:19:00 | NOAA-21 | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b14e1ef9-ff9a-3576-972d-9c9cd8522018 | -9.25529 | -45.25427 | 2025-10-17 04:19:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 165afaf1-70a6-3443-aa2b-a5aeadfe50de | -6.28449 | -42.97761 | 2025-10-17 04:19:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1f3eea95-71c8-37da-b548-81b03b3a74d3 | -8.23771 | -43.32533 | 2025-10-17 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4f85f767-e07d-30bb-b822-3c426397cad6 | -6.53777 | -55.04737 | 2025-10-17 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0146595d-5f2a-3ff8-92e5-3202fd47985e | -7.2694 | -42.93781 | 2025-10-17 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| bebf5d84-547f-3540-b662-981fb081a610 | -3.40638 | -52.50407 | 2025-10-17 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ceafcbd6-8194-38c5-9c9c-b3e64f9e16b4 | -11.40765 | -44.19222 | 2025-10-17 04:19:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8643a322-5eb9-3899-863f-ae1b68d7a238 | -5.47461 | -44.66931 | 2025-10-17 04:19:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c7864277-f2f9-36da-b39f-97432c9100f6 | -5.36875 | -42.72323 | 2025-10-17 04:19:00 | NOAA-21 | DEMERVAL LOBÃO | PIAUÍ | Brasil | 2203305 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 82817c54-b35d-3cae-a767-a0b83a67e856 | -7.20692 | -45.49126 | 2025-10-17 04:19:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0fcb1f2e-5dbe-3121-8c5f-aa203d932db2 | -5.72806 | -41.31199 | 2025-10-17 04:19:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 50cae78f-b31e-3dcf-80df-c30dcb5487df | -11.40372 | -44.19537 | 2025-10-17 04:19:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d79750a8-2afd-32be-85da-338156dbe85c | -8.47318 | -44.18064 | 2025-10-17 04:19:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0e53c3d3-1d07-327f-870a-025620716fed | -8.17046 | -43.31112 | 2025-10-17 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| bbe8f959-31b6-3a2c-9415-b47219b98f3a | -8.19364 | -43.31847 | 2025-10-17 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 20.7 |
| 92b3069f-a3a8-3ac6-8ae0-a68298c2c30f | -4.28094 | -48.59132 | 2025-10-17 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8c0150fb-5a5c-33f0-bace-67f68441cd79 | -6.25158 | -44.02948 | 2025-10-17 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 095ea356-4db6-37a0-a7a5-1f81c28b7615 | -8.24675 | -43.33424 | 2025-10-17 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 6f696599-d88b-3aa8-b6fa-c545f320a25d | -8.2952 | -43.45736 | 2025-10-17 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4a03984f-a7fb-3616-a4b5-b98eff1fb20c | -5.45932 | -41.02689 | 2025-10-17 04:19:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d6b60e25-9dd9-323b-b588-78d33f1213fe | -7.34914 | -43.86147 | 2025-10-17 04:19:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 1cd73052-8e65-30b6-af85-3800e9727328 | -6.51694 | -46.51342 | 2025-10-17 04:19:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c8694d58-b007-3583-a551-2562cdc6af09 | -8.55766 | -44.58097 | 2025-10-17 04:19:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e6d6000c-0aa5-3410-b6ed-8e98b668d014 | -7.5726 | -43.82372 | 2025-10-17 04:19:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a07b402a-1aec-3255-ade9-e28d98819b75 | -7.05553 | -46.68211 | 2025-10-17 04:19:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b646656f-bb3c-36ac-abbf-89ed73a9d3d0 | -8.26373 | -44.08286 | 2025-10-17 04:19:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c1d1ebcf-dec7-3cc5-a25e-cb548172e02a | -5.77726 | -49.80766 | 2025-10-17 04:19:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c9d1c82a-149f-30c7-b877-5fa84b995981 | -10.29705 | -44.0382 | 2025-10-17 04:19:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 33.6 |
| 03411dd9-ab7f-3941-bbca-7cc4af2033d0 | -7.02942 | -41.81436 | 2025-10-17 04:19:00 | NOAA-21 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| fd7927e5-24ab-351d-b961-8059bd07a349 | -10.01199 | -45.63916 | 2025-10-17 04:19:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6c3ccc43-12a7-3ae2-91e4-a2bce59b5677 | -8.2255 | -44.00118 | 2025-10-17 04:19:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 583aab03-0e2b-3a52-a9d3-3c9c7cf61f11 | -5.36606 | -43.15661 | 2025-10-17 04:19:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 22590dd1-cb20-363e-8f80-d8e32bdbdddc | -10.71336 | -44.53738 | 2025-10-17 04:19:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 37371e7c-7ee5-3a5b-a2d0-509a2b9e96c9 | -5.8504 | -43.87439 | 2025-10-17 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4dee5bba-a7ac-3a93-8c52-065e062509b7 | -8.63217 | -54.62609 | 2025-10-17 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README60.md)

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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 005c51a8-1bc5-34fd-9d99-28702e9a33fd | -5.38946 | -36.81682 | 2025-02-01 03:42:00 | NPP-375D | ALTO DO RODRIGUES | RIO GRANDE DO NORTE | Brasil | 2400703 | 24 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 9247d617-5c91-337b-8852-16dfbba00385 | -5.75028 | -38.15305 | 2025-02-01 03:42:00 | NPP-375D | POTIRETAMA | CEARÁ | Brasil | 2311231 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 152d9960-7986-3406-9fb0-cca8c074e084 | -7.84524 | -35.19868 | 2025-02-01 03:42:00 | NPP-375D | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| d9b2428b-f2c6-3013-9087-aa79951c059b | -4.85084 | -38.33701 | 2025-02-01 03:42:00 | NPP-375D | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| bddd32e5-ab47-3b27-ac03-9d2a506bbc74 | -5.6947 | -38.05748 | 2025-02-01 03:42:00 | NPP-375D | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 9b3ac494-2797-35f4-85a6-1be6a212243c | -6.80209 | -37.97353 | 2025-02-01 03:42:00 | NPP-375D | SÃO DOMINGOS | PARAÍBA | Brasil | 2513968 | 25 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 140ad58a-9943-3939-9820-e1ba6609614f | -7.84191 | -35.19815 | 2025-02-01 03:42:00 | NPP-375D | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| dd9c21db-ff1e-31c4-9bc5-90db454486c5 | -4.85377 | -38.33558 | 2025-02-01 03:42:00 | NPP-375D | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e0c25365-2a14-3d1d-99ca-75f06aebb356 | -5.36543 | -36.83563 | 2025-02-01 03:42:00 | NPP-375D | CARNAUBAIS | RIO GRANDE DO NORTE | Brasil | 2402501 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| bcad6995-4674-3a90-9ca6-9405f5e0b23c | -7.38537 | -42.78619 | 2025-02-01 03:44:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5088db54-ea19-3524-b1c6-127c842bbfab | -8.46469 | -37.82684 | 2025-02-01 03:44:00 | NPP-375D | FLORESTA | PERNAMBUCO | Brasil | 2605707 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b19fae46-e405-3fbe-aeec-d8e2f8296457 | -10.51837 | -36.92176 | 2025-02-01 03:44:00 | NPP-375D | JAPARATUBA | SERGIPE | Brasil | 2803302 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 1757bdd6-e2f9-310a-91e5-9f8d0c33570a | -8.62784 | -40.44788 | 2025-02-01 03:44:00 | NPP-375D | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 7a45a2f4-27e8-3422-be69-dd9dc7c4f0df | -10.51503 | -36.92121 | 2025-02-01 03:44:00 | NPP-375D | JAPARATUBA | SERGIPE | Brasil | 2803302 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| f6fe2163-d733-3352-9087-f34d204d11dd | -9.58558 | -36.70553 | 2025-02-01 03:44:00 | NPP-375D | CRAÍBAS | ALAGOAS | Brasil | 2702355 | 27 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 6e09a40a-8e58-3fbd-a53d-852e11341af7 | -9.04734 | -35.87555 | 2025-02-01 03:44:00 | NPP-375D | IBATEGUARA | ALAGOAS | Brasil | 2703007 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| a5de187b-6f43-3791-9b89-c8736f68e850 | -8.47475 | -35.32574 | 2025-02-01 03:44:00 | NPP-375D | RIBEIRÃO | PERNAMBUCO | Brasil | 2611804 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 89a5e5c9-1257-3ff8-b0c6-23949b5e8adc | -11.01616 | -40.47982 | 2025-02-01 03:44:00 | NPP-375D | MIRANGABA | BAHIA | Brasil | 2921401 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b1fad1df-1a23-363a-9b50-89d35a55b2e1 | -10.19602 | -36.67825 | 2025-02-01 03:44:00 | NPP-375D | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Caatinga | 4.9 |
| aa607469-d727-3b67-a507-a1cb393eb4ab | -8.47087 | -35.32872 | 2025-02-01 03:44:00 | NPP-375D | RIBEIRÃO | PERNAMBUCO | Brasil | 2611804 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f21bd76d-6ce9-343c-bd99-de12ccb50fc2 | -8.4742 | -35.32925 | 2025-02-01 03:44:00 | NPP-375D | RIBEIRÃO | PERNAMBUCO | Brasil | 2611804 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 8ccc1f42-d094-351c-aa35-67be7b8d4b1e | -8.47032 | -35.33222 | 2025-02-01 03:44:00 | NPP-375D | RIBEIRÃO | PERNAMBUCO | Brasil | 2611804 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| cf27b071-a74c-33a5-846f-ef381592b5c8 | -8.47353 | -36.4035 | 2025-02-01 03:44:00 | NPP-375D | SÃO BENTO DO UNA | PERNAMBUCO | Brasil | 2613008 | 26 | 33 | nan | nan | nan | Caatinga | 0.5 |
| ed33a502-7d02-390f-ada3-33bfb8d83ad8 | -19.00506 | -40.49939 | 2025-02-01 03:46:00 | NPP-375D | SÃO GABRIEL DA PALHA | ESPÍRITO SANTO | Brasil | 3204708 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 350d65d6-e2ec-34d3-86a0-8a4a793dda7c | -20.35365 | -40.85969 | 2025-02-01 03:46:00 | NPP-375D | DOMINGOS MARTINS | ESPÍRITO SANTO | Brasil | 3201902 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 4c264c2a-0daa-30ab-8636-64f7ef9ff1ad | -17.67948 | -42.31578 | 2025-02-01 03:46:00 | NPP-375D | ANGELÂNDIA | MINAS GERAIS | Brasil | 3102852 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 99b0c704-119a-3504-95a3-8b602a13cdac | -20.35018 | -40.85905 | 2025-02-01 03:46:00 | NPP-375D | DOMINGOS MARTINS | ESPÍRITO SANTO | Brasil | 3201902 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 8469982d-6047-3305-a19e-e6d1aafba2e2 | -19.20845 | -40.09521 | 2025-02-01 03:46:00 | NPP-375D | SOORETAMA | ESPÍRITO SANTO | Brasil | 3205010 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| cba8d0ca-567a-3f50-8c2e-41f34a2efe97 | -20.79288 | -41.1297 | 2025-02-01 03:46:00 | NPP-375D | CACHOEIRO DE ITAPEMIRIM | ESPÍRITO SANTO | Brasil | 3201209 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| b06e40da-2206-353a-ab7f-5cd3338b5b45 | -17.67859 | -42.32079 | 2025-02-01 03:46:00 | NPP-375D | ANGELÂNDIA | MINAS GERAIS | Brasil | 3102852 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 203193ae-cd1a-3503-a133-72c4a54ad0c0 | 1.4134 | -59.9504 | 2025-02-01 03:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 4d81bb23-9863-3f0f-8c7e-f492d8d5d206 | -29.77816 | -51.17682 | 2025-02-01 03:51:00 | NPP-375D | SÃO LEOPOLDO | RIO GRANDE DO SUL | Brasil | 4318705 | 43 | 33 | nan | nan | nan | Pampa | 3.3 |
| 788c017d-417e-3575-9885-1c99dac66d24 | 1.4134 | -59.9504 | 2025-02-01 04:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 75.0 |
| bd61ac82-6481-3888-8625-f71f840a07ac | -5.38771 | -36.81511 | 2025-02-01 04:04:00 | NOAA-20 | ALTO DO RODRIGUES | RIO GRANDE DO NORTE | Brasil | 2400703 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 19f65a42-b0b4-3657-bd19-3f2e9d9bc61c | -4.85282 | -38.33282 | 2025-02-01 04:04:00 | NOAA-20 | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 791ff126-36b6-310d-98e7-8bcc6274b4cb | -4.18916 | -41.00761 | 2025-02-01 04:04:00 | NOAA-20 | CARNAUBAL | CEARÁ | Brasil | 2303402 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 249dcbed-0205-3316-8038-eacba1c1e603 | -5.36432 | -36.83419 | 2025-02-01 04:04:00 | NOAA-20 | CARNAUBAIS | RIO GRANDE DO NORTE | Brasil | 2402501 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 393ade12-4d83-3311-8aa7-81d009454558 | -4.85221 | -38.33686 | 2025-02-01 04:04:00 | NOAA-20 | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f53d9c49-254a-3efa-8d48-5a0f4fdadee9 | -5.38699 | -36.82001 | 2025-02-01 04:04:00 | NOAA-20 | ALTO DO RODRIGUES | RIO GRANDE DO NORTE | Brasil | 2400703 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b748006f-c16e-3971-a029-3808f647b54b | -5.52856 | -37.10125 | 2025-02-01 04:04:00 | NOAA-20 | AÇU | RIO GRANDE DO NORTE | Brasil | 2400208 | 24 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 594fae89-947d-30c3-97e5-b897df597d34 | -4.29959 | -39.27628 | 2025-02-01 04:04:00 | NOAA-20 | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |
| da9e7345-0132-35d5-b6d3-d72da54697ea | -5.3868 | -36.81752 | 2025-02-01 04:04:00 | NOAA-20 | ALTO DO RODRIGUES | RIO GRANDE DO NORTE | Brasil | 2400703 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a2745af2-452f-374b-8c01-cfadedc7f66b | -5.13445 | -38.67004 | 2025-02-01 04:04:00 | NOAA-20 | BANABUIÚ | CEARÁ | Brasil | 2301851 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 167995f4-1847-3e7f-b7b5-8a0940dff1e9 | -5.75091 | -38.15067 | 2025-02-01 04:06:00 | NOAA-20 | POTIRETAMA | CEARÁ | Brasil | 2311231 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e3b35622-29e1-3870-8478-eae3cf07d48a | -6.93835 | -43.53106 | 2025-02-01 04:06:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6eb933b6-e33a-357f-9f69-af419d970f83 | -5.83312 | -39.06917 | 2025-02-01 04:06:00 | NOAA-20 | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 265c7706-db4f-35e9-869d-4f848b3d8526 | -6.56051 | -37.43837 | 2025-02-01 04:06:00 | NOAA-20 | SERRA NEGRA DO NORTE | RIO GRANDE DO NORTE | Brasil | 2413409 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f73a1ab1-e0b2-33d7-9895-633df239d8df | -6.80171 | -37.97131 | 2025-02-01 04:06:00 | NOAA-20 | SÃO DOMINGOS | PARAÍBA | Brasil | 2513968 | 25 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 615fd6e2-a11d-3b89-941a-729cffcd4035 | -5.36537 | -40.21989 | 2025-02-01 04:06:00 | NOAA-20 | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 003ffc8c-a9b4-3d84-905c-52fdce9212d8 | -8.62985 | -40.44714 | 2025-02-01 04:06:00 | NOAA-20 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ea7cd388-bfb9-38b4-8c35-2e44828faf3b | -7.9295 | -41.76103 | 2025-02-01 04:06:00 | NOAA-20 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| cde9dbd1-d073-350f-9478-f00c34fe49dd | -10.69354 | -37.04766 | 2025-02-01 04:06:00 | NOAA-20 | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ecdce43a-8fdb-3417-a327-c61be8ea3360 | -9.58551 | -36.70457 | 2025-02-01 04:06:00 | NOAA-20 | CRAÍBAS | ALAGOAS | Brasil | 2702355 | 27 | 33 | nan | nan | nan | Caatinga | 5.8 |
| d54d0173-dda6-3361-85f2-9f25ffc0fb21 | -7.38641 | -42.78901 | 2025-02-01 04:06:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e69602de-5502-39b9-b0c0-ad9e17158b5a | -8.46645 | -37.8263 | 2025-02-01 04:06:00 | NOAA-20 | FLORESTA | PERNAMBUCO | Brasil | 2605707 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 7e1b9b04-72dc-3b82-bcc4-48e53f8d2b35 | -7.38697 | -42.78547 | 2025-02-01 04:06:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6c675353-8784-3f76-a0a6-1fda122f980d | -10.19743 | -36.67781 | 2025-02-01 04:06:00 | NOAA-20 | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 9a9e30b7-18b8-39a5-ad52-67be7f737892 | -8.47804 | -35.33012 | 2025-02-01 04:06:00 | NOAA-20 | RIBEIRÃO | PERNAMBUCO | Brasil | 2611804 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| aa8d60ea-5281-33c8-a34f-6ee928d408c7 | -11.2863 | -37.28617 | 2025-02-01 04:06:00 | NOAA-20 | ESTÂNCIA | SERGIPE | Brasil | 2802106 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 5285e4e4-3c3b-3734-8cec-64dfd2d902b5 | -10.51657 | -36.92258 | 2025-02-01 04:06:00 | NOAA-20 | JAPARATUBA | SERGIPE | Brasil | 2803302 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 9ddc0485-186f-3134-ad6a-8425094f7fc3 | -8.47352 | -35.32954 | 2025-02-01 04:06:00 | NOAA-20 | RIBEIRÃO | PERNAMBUCO | Brasil | 2611804 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| af689edf-5348-398a-81a9-561ea0c5d1b0 | -10.92871 | -38.81754 | 2025-02-01 04:06:00 | NOAA-20 | TUCANO | BAHIA | Brasil | 2931905 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 1694bec2-0a69-3cc9-94bf-9ed0c34abb86 | -11.01655 | -40.47665 | 2025-02-01 04:06:00 | NOAA-20 | MIRANGABA | BAHIA | Brasil | 2921401 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8d8f7445-9988-38e1-99a8-1de945b3a0ed | -13.47851 | -44.02153 | 2025-02-01 04:08:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e49bf1bc-07bb-3a6e-b67d-77e1261766c0 | -11.25871 | -44.49285 | 2025-02-01 04:08:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6da1e3e7-e823-38ec-8f01-6008e0fe8d6e | -13.47908 | -44.01795 | 2025-02-01 04:08:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0ed4278a-182b-311b-9b8d-f8f817b7ad68 | -12.27867 | -41.42694 | 2025-02-01 04:08:00 | NOAA-20 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 287fa037-412b-39f7-91ae-b30af72690b7 | -19.00456 | -40.50047 | 2025-02-01 04:08:00 | NOAA-20 | SÃO GABRIEL DA PALHA | ESPÍRITO SANTO | Brasil | 3204708 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 76e65414-9218-3a7b-8d7e-1789b0aca485 | -11.25931 | -44.48912 | 2025-02-01 04:08:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5b8c567f-7acc-3e71-8734-d31d75b7287e | -15.60708 | -41.36988 | 2025-02-01 04:08:00 | NOAA-20 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 0c1b720b-a822-3be7-a27a-41f9f32fbbb2 | 1.4134 | -59.9504 | 2025-02-01 04:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 3781e1c8-a9fb-3282-9ef4-814efe1a4c35 | -19.72076 | -49.84732 | 2025-02-01 04:10:00 | NOAA-20 | SÃO FRANCISCO DE SALES | MINAS GERAIS | Brasil | 3161304 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 134654f3-4da3-33fd-a867-87d425fdf795 | -20.35072 | -40.86061 | 2025-02-01 04:10:00 | NOAA-20 | DOMINGOS MARTINS | ESPÍRITO SANTO | Brasil | 3201902 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| a6342d22-bf52-3ad4-9b27-ff9296bd1d9e | -20.41567 | -43.55277 | 2025-02-01 04:10:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 8c92b8b7-0b3b-38b0-b78b-d91f35c5dbdc | -20.35444 | -40.86123 | 2025-02-01 04:10:00 | NOAA-20 | DOMINGOS MARTINS | ESPÍRITO SANTO | Brasil | 3201902 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 63dcd189-d6f8-3731-8a7e-d622c29c4ad1 | -22.78456 | -43.75755 | 2025-02-01 04:10:00 | NOAA-20 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 0fe839f5-5532-3c14-a0ec-7c68817accca | -20.34706 | -40.36218 | 2025-02-01 04:10:00 | NOAA-20 | CARIACICA | ESPÍRITO SANTO | Brasil | 3201308 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 475c3693-3480-3008-b13b-375ec71356a2 | -22.78536 | -43.75639 | 2025-02-01 04:10:00 | NOAA-20 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 4970d062-cd42-3110-8099-d0a9222df629 | -29.53431 | -51.32399 | 2025-02-01 04:12:00 | NOAA-20 | SÃO SEBASTIÃO DO CAÍ | RIO GRANDE DO SUL | Brasil | 4319505 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a6b7230e-b0cf-3afe-a9a4-fd4d8b70cf7a | -29.77707 | -51.17693 | 2025-02-01 04:12:00 | NOAA-20 | SÃO LEOPOLDO | RIO GRANDE DO SUL | Brasil | 4318705 | 43 | 33 | nan | nan | nan | Pampa | 3.4 |
| 049d0b9a-5eba-3a7f-ab82-c1c27928c0f3 | -31.73139 | -51.56885 | 2025-02-01 04:14:00 | NOAA-20 | SÃO JOSÉ DO NORTE | RIO GRANDE DO SUL | Brasil | 4318507 | 43 | 33 | nan | nan | nan | Pampa | 0.6 |
| 6fb16bdb-3b3c-3e4b-9564-4d1c048b746b | 1.4134 | -59.9504 | 2025-02-01 04:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 9a3cc877-5c78-3e7a-8ead-b23af0e21669 | 1.4134 | -59.9504 | 2025-02-01 04:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 62.8 |
| df6e2b2c-7030-3a7f-8203-ce1a2aa22bc4 | 1.4134 | -59.9504 | 2025-02-01 04:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 58.4 |
| c3254f3a-34a7-3b7a-bd2f-e9e694c30bfe | 1.4134 | -59.9504 | 2025-02-01 04:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 67.4 |
| f7292491-57fd-31fd-ad22-bed3b86d090e | 1.41204 | -59.94624 | 2025-02-01 04:55:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.7 |
| c54848ac-32e2-38de-9846-9bfd4323b8d9 | 1.42323 | -59.95535 | 2025-02-01 04:55:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 8.6 |
| ffb317db-9274-3367-b034-2d6439089134 | 1.41511 | -59.96398 | 2025-02-01 04:55:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8576c9ff-a8a7-3fc0-a1ac-644a6eeed820 | 1.41604 | -59.94012 | 2025-02-01 04:55:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c267b3ce-52b6-3e98-b91a-5b8bc097950e | 1.41179 | -59.94279 | 2025-02-01 04:55:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ca2c2f5d-0a49-3ef5-a998-fe7ae2d4206a | 1.41763 | -59.95079 | 2025-02-01 04:55:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 4a1fe940-93e0-3164-bc92-4305a5e7515a | 1.41921 | -59.96137 | 2025-02-01 04:55:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 10d08cf7-80a4-37f0-936e-639203c2a78e | 2.44062 | -60.65367 | 2025-02-01 04:55:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 4f1d420d-8c92-3e80-a71f-c14c6e31c8d1 | 1.41742 | -59.94739 | 2025-02-01 04:55:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 24e09311-dae6-392b-8711-260d2f732b43 | 0.79181 | -60.09238 | 2025-02-01 04:55:00 | NOAA-21 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c3b75ca1-bd66-35ed-a0c4-b68325292373 | 2.14204 | -60.8497 | 2025-02-01 04:55:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 97b0ca3b-1d7b-308b-97f8-3c2b987fc73b | 1.41283 | -59.95154 | 2025-02-01 04:55:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 9ec4d8e5-998b-3122-a893-d04e90297235 | 1.42085 | -59.9394 | 2025-02-01 04:55:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c0e123ad-7880-326b-8e5b-90ddea6d4c6c | 2.14248 | -60.85265 | 2025-02-01 04:55:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ccac1096-aaa8-3af2-8879-7efba20e133b | 1.41659 | -59.94205 | 2025-02-01 04:55:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |


[Clique aqui para ver as próximas entradas](README3.md)

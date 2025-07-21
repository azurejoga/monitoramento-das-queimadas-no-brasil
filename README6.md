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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0f903bf3-132f-3096-b601-602cd699def8 | -23.70673 | -51.65959 | 2025-07-21 04:02:00 | NPP-375D | MARUMBI | PARANÁ | Brasil | 4115507 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 22c64e09-de46-3d02-aed2-747ded3e0431 | -23.70241 | -51.65506 | 2025-07-21 04:02:00 | NPP-375D | MARUMBI | PARANÁ | Brasil | 4115507 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| ba899440-65f3-3712-a485-4ded197c577f | -23.70429 | -51.65966 | 2025-07-21 04:02:00 | NPP-375D | MARUMBI | PARANÁ | Brasil | 4115507 | 41 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| 52f99a17-81fa-3344-a035-ed0d99c70db0 | -23.3406 | -51.90706 | 2025-07-21 04:02:00 | NPP-375D | MARINGÁ | PARANÁ | Brasil | 4115200 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| c10083d9-d680-3293-99fc-f50b9237b040 | -23.70501 | -51.65632 | 2025-07-21 04:02:00 | NPP-375D | MARUMBI | PARANÁ | Brasil | 4115507 | 41 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| d9c1aac9-3255-3691-9d3b-1288e795ec29 | -23.70747 | -51.65627 | 2025-07-21 04:02:00 | NPP-375D | MARUMBI | PARANÁ | Brasil | 4115507 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 110a2cae-acba-3b5a-88ba-e93c696742bb | -24.54684 | -50.79443 | 2025-07-21 04:02:00 | NPP-375D | RESERVA | PARANÁ | Brasil | 4121703 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| dcb062ed-ca92-3175-a040-c110c3242275 | -7.2957 | -60.169 | 2025-07-21 04:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.4 |
| a4eb2c10-9970-3151-8ce9-9da591ca5e56 | -7.2772 | -60.1698 | 2025-07-21 04:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 92.4 |
| 24cb7f34-b320-3358-a06a-038229aabc3f | -7.2402 | -60.1904 | 2025-07-21 04:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 187f16b0-3d2f-30c1-9331-34f869ef62b7 | -3.58657 | -47.51963 | 2025-07-21 04:17:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7534385f-e77b-3966-9ab4-f717cb598d1f | -3.13316 | -47.0124 | 2025-07-21 04:17:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 015ff939-e014-3e1a-b985-7d865ca0fab9 | -4.29798 | -48.62144 | 2025-07-21 04:17:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e567a799-36c3-34a5-8409-b19d9b563ee7 | -3.68056 | -47.49162 | 2025-07-21 04:17:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a7345127-fd13-377f-8bd5-304684219cef | -3.10899 | -47.00933 | 2025-07-21 04:17:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| edea8081-6a25-3e0b-bda3-e500a625caaf | -4.5948 | -43.31457 | 2025-07-21 04:17:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 67be3779-37a2-397c-89dc-4cf1344d3ec2 | -4.60094 | -43.31914 | 2025-07-21 04:17:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2ed414b5-1840-3716-8820-ca3307dd2c5b | -4.0411 | -48.93601 | 2025-07-21 04:17:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8fa1c96d-55a3-3cc8-8ad6-0cfcc12e3846 | -3.8364 | -49.16104 | 2025-07-21 04:17:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ecbeee6c-d49c-3e20-910b-b15ba5ec0f22 | -3.58951 | -47.52446 | 2025-07-21 04:17:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8d3d7287-a629-357e-b446-5ee214fcfa64 | -3.04107 | -47.86076 | 2025-07-21 04:17:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| f93c5e85-363b-334d-b12a-6e16027b3278 | -3.59021 | -47.52021 | 2025-07-21 04:17:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 52b2ead8-42ba-3fb0-8b39-a9726fbd8f54 | -3.50379 | -49.05428 | 2025-07-21 04:17:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d0a8aa05-905b-38c6-b294-d1ec38977e04 | -2.902 | -48.24585 | 2025-07-21 04:17:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e48d33b0-0ae5-3b83-811a-c0f92a8a022b | -4.66752 | -41.96508 | 2025-07-21 04:17:00 | NOAA-20 | COCAL DE TELHA | PIAUÍ | Brasil | 2202711 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 94e75126-fec2-32c7-a33c-1de1e7661263 | -3.12603 | -47.01126 | 2025-07-21 04:17:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e29bdafb-5f44-300f-b59d-c052d2b7780e | -3.78206 | -41.68119 | 2025-07-21 04:17:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b795dff8-bfef-3332-8c84-959e4d1548c8 | -3.10835 | -47.01338 | 2025-07-21 04:17:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f2b3822a-8e2b-30c9-915d-d591172c5490 | -2.92109 | -49.07409 | 2025-07-21 04:17:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8ea72dad-dae9-36b8-97ba-474bd14074c5 | -3.83695 | -49.15757 | 2025-07-21 04:17:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 00633678-fd7a-309b-b1d4-b7e3d0b6a664 | -3.11191 | -47.01396 | 2025-07-21 04:17:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c7d061db-f6e1-3702-9893-99b3b57342a8 | -3.71386 | -49.07134 | 2025-07-21 04:17:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5ad43dd7-eb97-3ff3-ad4a-305ac1a51bed | -2.91041 | -48.24234 | 2025-07-21 04:17:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c59deaab-5411-3ff3-a5bb-0ed48dab05f8 | -4.5976 | -43.31861 | 2025-07-21 04:17:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 03112cf2-0864-3edc-8651-8e2dca99f40f | -3.50435 | -49.05083 | 2025-07-21 04:17:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ed4a12aa-38cf-3cc0-89dc-49187888fcbd | -2.92571 | -49.07114 | 2025-07-21 04:17:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ebeb1b72-c4e4-3260-a859-79b121a250a9 | -3.04035 | -47.86526 | 2025-07-21 04:17:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 7b94446c-cc5e-3ffb-952c-d0eca8c764ad | -3.11255 | -47.00991 | 2025-07-21 04:17:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 40d0d717-ce5a-3859-af07-25145f283640 | -3.03661 | -47.86467 | 2025-07-21 04:17:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 043caf4a-b9ea-328c-b18c-170825a6816d | -3.13672 | -47.01296 | 2025-07-21 04:17:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fd2b9e81-662e-3b9c-bca7-2722b476fd18 | -2.57053 | -42.75306 | 2025-07-21 04:17:00 | NOAA-20 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cff3e26d-5ffa-3a0a-957b-64701c6c0b32 | -3.23081 | -49.14542 | 2025-07-21 04:17:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b1aa0703-d00d-386c-aaba-16995c65660c | -2.90583 | -48.24646 | 2025-07-21 04:17:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 96acb577-1ef1-347c-8aca-2d60c3de5bbe | -3.12959 | -47.01183 | 2025-07-21 04:17:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bd85ad01-fecb-34e3-a052-d7adb16b70f6 | -3.12246 | -47.0107 | 2025-07-21 04:17:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c4439fae-66be-3e5d-b423-c04a8bfa400e | -3.71044 | -49.06726 | 2025-07-21 04:17:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e6a06e08-8c75-367c-a82b-d7473f7a1075 | -3.03734 | -47.86017 | 2025-07-21 04:17:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 824a0234-1511-30ff-893d-9268c8302bce | -10.66304 | -46.77694 | 2025-07-21 04:19:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a819a832-7486-32a5-b721-cd188200aa5a | -9.40416 | -47.96796 | 2025-07-21 04:19:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5ccf0a90-5926-3c75-9c1a-29a02bc80bb3 | -9.55744 | -40.60057 | 2025-07-21 04:19:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 63d72304-cdbf-30a6-a3b2-68671acecb9e | -12.46564 | -46.92014 | 2025-07-21 04:19:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 821afa0a-4ee3-3fc1-a2d2-38138ed46a7c | -8.04256 | -42.14782 | 2025-07-21 04:19:00 | NOAA-20 | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4352f867-159f-3aaf-b885-67090352374a | -10.13343 | -49.65944 | 2025-07-21 04:19:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2eea75a1-cc79-3e52-aa41-065365b05161 | -11.49613 | -48.07765 | 2025-07-21 04:19:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f5d2db56-aa04-3bbf-a20b-9bfb7907bc44 | -10.88196 | -47.1295 | 2025-07-21 04:19:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 37ac658a-5ea7-34db-ad61-91aff7c0afca | -6.57545 | -43.39624 | 2025-07-21 04:19:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a55da969-d67a-3475-bd09-36b0ef4b5197 | -10.15598 | -49.66344 | 2025-07-21 04:19:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fda2b45e-ae63-3461-ab7b-9eb7fdd8b96c | -7.11032 | -43.29097 | 2025-07-21 04:19:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5c567ba1-b659-3efd-9402-b01bd0419242 | -6.45923 | -45.18111 | 2025-07-21 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3b686420-15e5-3fa0-8aa6-255e2d8d9d55 | -6.19997 | -44.38929 | 2025-07-21 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9f595d59-34ed-3c55-bb6d-a092fcb1114a | -7.94803 | -43.97682 | 2025-07-21 04:19:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8af2dca0-d2aa-3c2d-8153-5479d6a9945a | -9.59523 | -48.54607 | 2025-07-21 04:19:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f60e7d64-ee66-3019-ba4f-bbcbd3a82890 | -11.49957 | -48.07822 | 2025-07-21 04:19:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e6506382-ca05-3187-9af1-aa4d8132e6c9 | -7.75604 | -42.15776 | 2025-07-21 04:19:00 | NOAA-20 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 0880ddd8-6972-3838-ba49-3452ce1296a0 | -8.07504 | -50.09228 | 2025-07-21 04:19:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0ba59c73-a744-340e-b93c-3a9c124367fb | -10.64979 | -44.48561 | 2025-07-21 04:19:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 559fe089-9a3a-3086-b07c-786954b2e7c6 | -10.68086 | -46.77255 | 2025-07-21 04:19:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7a7981c4-4ff9-392f-8a9c-8b7a616e2214 | -6.68414 | -43.00901 | 2025-07-21 04:19:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8df9c972-76e3-3ea9-907b-8bc8499f41e7 | -11.47479 | -47.28636 | 2025-07-21 04:19:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dc512117-5549-3474-8ffa-6d0990555f03 | -8.27156 | -46.07059 | 2025-07-21 04:19:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 360e1020-7ba0-3fae-9e26-fb341422059f | -6.1991 | -45.92006 | 2025-07-21 04:19:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 29adab43-9c73-387f-bf59-b23216275f17 | -5.09097 | -48.42477 | 2025-07-21 04:19:00 | NOAA-20 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a2b15e30-ee91-31ae-aea9-14c8b63e6382 | -6.78612 | -47.16269 | 2025-07-21 04:19:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 294b388b-9f76-355a-b01b-439a1e1b0edd | -6.89678 | -42.78859 | 2025-07-21 04:19:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 2e3126f9-da34-3320-821e-76cc9de0b2ff | -7.11823 | -43.2847 | 2025-07-21 04:19:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 6a61f16f-d3df-3073-920f-d97d89a05ae2 | -6.888 | -45.39118 | 2025-07-21 04:19:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 482345be-25f1-3890-9e09-e327dd97f8af | -5.26449 | -44.87083 | 2025-07-21 04:19:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 48ca06a6-b25d-3cc8-9203-ef5c683e14a0 | -7.75124 | -42.16534 | 2025-07-21 04:19:00 | NOAA-20 | PAES LANDIM | PIAUÍ | Brasil | 2207306 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 3eb61292-8111-33dc-b108-9101687e2867 | -6.17326 | -49.90005 | 2025-07-21 04:19:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a5c8c940-ac93-38aa-8c96-9b9f47d28cc7 | -8.9174 | -47.3652 | 2025-07-21 04:19:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a86d5e46-ec1f-3f9b-8ab8-5faabdb8ca0d | -7.25232 | -44.28388 | 2025-07-21 04:19:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 06c6519e-ce0b-39ef-b1fd-fe7e8aaff4b0 | -6.7702 | -43.80611 | 2025-07-21 04:19:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ba6d91a3-8cf6-3c64-bdbf-ec2f6487f87c | -10.68185 | -56.55444 | 2025-07-21 04:19:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ea21f325-8ccf-3910-9af7-1d527829c685 | -6.8988 | -44.24294 | 2025-07-21 04:19:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 572cbe1a-8b5e-39f3-b71f-e332a4cc9c33 | -7.07565 | -43.82749 | 2025-07-21 04:19:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5c661040-a5ed-3a67-9889-5114d9a3dd4b | -7.96306 | -43.96828 | 2025-07-21 04:19:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 660ad838-b073-39cf-a6dd-a0eed0e4bfda | -12.41364 | -45.89577 | 2025-07-21 04:19:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 899a757b-feda-3014-8672-f3d238240f3b | -6.57208 | -43.39575 | 2025-07-21 04:19:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 1.7 |
| dc3b2153-a326-317e-8635-70a4c3e45408 | -8.07046 | -50.09507 | 2025-07-21 04:19:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fa7895e9-4a18-37dc-a76a-56fd19fe0eec | -10.38199 | -49.93196 | 2025-07-21 04:19:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 48bb10b2-5d1f-3aa4-8c80-9f50850eafa8 | -10.09194 | -46.589 | 2025-07-21 04:19:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5cb7347c-1a19-3d94-924a-e59a61b4367c | -8.07803 | -49.90877 | 2025-07-21 04:19:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 420a4b11-b00f-3c92-a6ab-5ae8ed042461 | -10.84314 | -47.15643 | 2025-07-21 04:19:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ede2f53e-e507-3557-ae28-2ab848e2a6a1 | -8.88348 | -46.87908 | 2025-07-21 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e5436037-fe8a-307a-a461-db243b9b1c5a | -6.64662 | -44.16111 | 2025-07-21 04:19:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| df8d69bb-8029-395c-9f8a-40b2548ed90a | -6.95319 | -44.39407 | 2025-07-21 04:19:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4a979b07-c229-3405-b179-a29ec361a0b9 | -8.20113 | -42.29939 | 2025-07-21 04:19:00 | NOAA-20 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5a9e5acc-a8bb-3b72-afd5-ef9248d54321 | -6.34258 | -44.0415 | 2025-07-21 04:19:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5e928544-caa6-3841-a8cb-4e487b4e0456 | -6.51677 | -44.59888 | 2025-07-21 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fed86a64-a9df-3071-951e-c36a66a73815 | -6.89935 | -44.23943 | 2025-07-21 04:19:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README7.md)

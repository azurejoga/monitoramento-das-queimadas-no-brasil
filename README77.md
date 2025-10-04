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

## Dados Diários - Página 77

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6aa1f76e-c86e-3e57-85a5-4c28f7b4e4a5 | -15.31005 | -46.27554 | 2025-10-04 04:14:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| be944f94-5dc5-34c4-98ca-8abadda0df01 | -11.83623 | -45.02048 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7b1fb916-ba15-3237-96b7-0ac3a1a495b6 | -13.31594 | -47.24175 | 2025-10-04 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 13eee0a2-2896-3d3f-b2f6-7bfe2a163b8c | -14.6603 | -48.31279 | 2025-10-04 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 22.5 |
| b8938822-11ac-38e9-81ef-fb4084b69118 | -14.2301 | -46.08865 | 2025-10-04 04:14:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5abb2dc4-ddda-3082-ae0a-6c4615f47343 | -11.88459 | -44.99566 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d1a5df35-7808-38cb-b235-8e8db2df5fea | -9.94151 | -50.23803 | 2025-10-04 04:14:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2563d35b-fc50-39c8-8993-bd3369c09caa | -13.69712 | -47.34728 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 163ff39c-ae2b-3ab2-ad08-4a657c0d4fca | -8.62435 | -54.97848 | 2025-10-04 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6d3d6e8f-f4a4-369e-840a-a7cfd683046f | -14.68228 | -48.27238 | 2025-10-04 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 510460ff-fce5-3a19-95aa-25c6123b3ae6 | -9.90948 | -43.72059 | 2025-10-04 04:14:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 1bdb230f-746b-3d80-8a33-205c46c4526e | -14.93515 | -46.8632 | 2025-10-04 04:14:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| f0c0e47f-3e89-3719-8afb-d3fc7f956baa | -14.6671 | -48.29518 | 2025-10-04 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 6dde6442-ab3e-374e-8c5b-0ee26e91dc0f | -13.93043 | -48.17005 | 2025-10-04 04:14:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 13.9 |
| e7c8c5b3-6f4c-33c9-b2dc-1dfa66e53f53 | -14.79484 | -42.83302 | 2025-10-04 04:14:00 | NOAA-20 | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ab26c4a4-509c-35af-984d-1a9022cbedca | -14.22853 | -46.077 | 2025-10-04 04:14:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6a0665c9-b4db-3793-80c8-5ee50adeeb2d | -13.81223 | -47.58934 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 10671e56-10db-305f-8406-d033fc176dd2 | -7.77481 | -46.24729 | 2025-10-04 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dbeea4db-ba33-3ca2-87e7-a6c4e2b6f6d1 | -13.2381 | -47.36007 | 2025-10-04 04:14:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0b261937-0e15-3bf6-ae96-0afdcba25ff8 | -13.35028 | -47.23108 | 2025-10-04 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5bda7ac3-476b-3402-babf-1b2675c3672d | -13.62898 | -48.67428 | 2025-10-04 04:14:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4acbefb6-3a1a-36e3-91dd-bf0c86640280 | -13.99643 | -48.2 | 2025-10-04 04:14:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3b56c808-2f2c-3afe-ad67-73e5b098f19e | -9.34238 | -45.79206 | 2025-10-04 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d6f8b55c-7a58-33b6-a6bb-472ef915da36 | -9.92443 | -50.89988 | 2025-10-04 04:14:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 27647a73-52a4-32d0-b81a-b4e6c7997157 | -9.90175 | -45.95611 | 2025-10-04 04:14:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4df872ae-82c9-335b-bbad-d47b026d0cd3 | -14.20779 | -46.07725 | 2025-10-04 04:14:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 05e1c03a-9c97-3f0e-9891-eada7783506c | -14.83731 | -48.37528 | 2025-10-04 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1e08f5e1-d995-3226-ad84-76b5ee7d488f | -11.54534 | -47.67859 | 2025-10-04 04:14:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e0763635-6e16-3666-8f7d-f1c188d46515 | -11.10004 | -47.71691 | 2025-10-04 04:14:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 52315be9-c0cf-3682-bc18-eb62fe390ade | -8.17286 | -44.13158 | 2025-10-04 04:14:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f5f9690b-2183-3b72-ac8c-300009145f32 | -14.84858 | -48.28668 | 2025-10-04 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ed96372a-3774-3c1a-ba38-18c4b3711ecf | -11.20067 | -54.08771 | 2025-10-04 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c3700b13-55be-385f-bcfe-308bcc85546f | -14.92353 | -46.86972 | 2025-10-04 04:14:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 46ab5f29-f640-3e7c-8af3-978e62338d37 | -11.55705 | -47.67625 | 2025-10-04 04:14:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 099ab61b-1165-3408-bb64-f2b6ec42e0e4 | -8.53941 | -50.15725 | 2025-10-04 04:14:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0cb97de3-b05c-325d-a171-ce7c32bb0f19 | -14.87626 | -48.36668 | 2025-10-04 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.2 |
| b2756acf-fe8f-32e8-b22f-f0882057fa12 | -14.23526 | -46.07805 | 2025-10-04 04:14:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| afdcda25-7a54-3c9e-a69b-7c7b143439d4 | -8.51087 | -54.60058 | 2025-10-04 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| be026ce4-9ac0-3883-8ea8-233e14a1c171 | -12.92493 | -46.36983 | 2025-10-04 04:14:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bb311062-1fda-3a64-ab58-65881e695dc4 | -11.91779 | -46.36652 | 2025-10-04 04:14:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 12bee3be-5f80-3250-89a8-30303b90bb36 | -12.65335 | -46.97395 | 2025-10-04 04:14:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| ac024f3b-4a8b-3fba-b098-84d9e4afea81 | -13.39262 | -47.561 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 91dad902-4a7b-3b82-b0fe-028e8dc0c8d1 | -11.79233 | -46.83148 | 2025-10-04 04:14:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8d45fdd4-b44f-354b-a5de-b4a8b8d0c80d | -11.87083 | -44.97505 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c63a9eed-d6c5-392f-9f2f-318ab0c9d524 | -14.19989 | -46.66192 | 2025-10-04 04:14:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 73eea991-9f42-3f53-afaf-196f79f65b5b | -11.24939 | -47.80436 | 2025-10-04 04:14:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6c74a51b-c96b-37bc-8bc3-ef5ac2aa2e75 | -14.8887 | -48.35979 | 2025-10-04 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a364b3c3-71df-3917-a850-166a400274cb | -9.33549 | -54.52747 | 2025-10-04 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 66191037-3ee1-35c6-9ef8-3bae2283e710 | -13.12038 | -47.83793 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 9f62a98e-3067-35b5-9d8e-aa02220f7542 | -12.69878 | -48.54723 | 2025-10-04 04:14:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 0cd86032-2fcf-35ed-b696-91d4ec6c2b5d | -9.89626 | -43.73993 | 2025-10-04 04:14:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5c780f73-5446-34df-a310-0258ebdd15a0 | -10.12023 | -52.34711 | 2025-10-04 04:14:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 437ebee7-4bb3-368d-9228-ded91033bb62 | -11.91498 | -46.36219 | 2025-10-04 04:14:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0e4e6fea-51f4-3c81-829d-7d49789fab27 | -10.88375 | -44.30414 | 2025-10-04 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f2b6fc68-3e38-3c72-bf56-d4f3eeae5263 | -7.76254 | -46.23263 | 2025-10-04 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7c561b4a-9f85-3f9d-b9e5-d65a4d6fa046 | -11.12405 | -47.90059 | 2025-10-04 04:14:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c24003c5-b97f-333a-a32b-02848082cef3 | -8.17029 | -43.35676 | 2025-10-04 04:14:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b164f00b-a59d-3bb1-b538-935a62a79780 | -14.92589 | -46.89784 | 2025-10-04 04:14:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 232bb6ce-7fd1-3f06-9c40-b22d5923ab08 | -10.86405 | -45.4056 | 2025-10-04 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fc232296-8baa-30c4-9e66-6df854ce59d2 | -13.31604 | -47.60902 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6f1f6e70-be11-35e2-8c0b-d26eebd148dc | -14.22398 | -46.08385 | 2025-10-04 04:14:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 10e886cd-6304-3a36-89c4-160f81b9caac | -12.70256 | -48.54793 | 2025-10-04 04:14:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| afcb3c02-2b9b-3807-be8a-bc732ba2e180 | -14.92846 | -46.88238 | 2025-10-04 04:14:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6f0b3531-810b-391d-ad7c-2b9a4d8767d0 | -9.93474 | -50.2472 | 2025-10-04 04:14:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f830157e-e10c-37b5-9f04-1fc8c2d6baf9 | -13.34962 | -47.23503 | 2025-10-04 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d409f2f1-8c32-3fd4-92e3-4b4796a2b2ab | -9.10558 | -44.39742 | 2025-10-04 04:14:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 03156b37-c2cd-39a4-8dcc-f32cda5efc50 | -14.16444 | -49.20854 | 2025-10-04 04:14:00 | NOAA-20 | NOVA IGUAÇU DE GOIÁS | GOIÁS | Brasil | 5214879 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f9ae0f84-358d-3eef-86ff-313b214c5ac7 | -14.44274 | -46.38235 | 2025-10-04 04:14:00 | NOAA-20 | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fd96a9ab-eb92-3537-9058-59732e14f3cc | -14.92368 | -48.3306 | 2025-10-04 04:14:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 20a922b0-fd1e-35fb-adfd-e668af65b5a4 | -11.80542 | -48.91503 | 2025-10-04 04:14:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9bd1f192-afe6-380b-b0fb-bbd85455a8d8 | -11.78462 | -46.83443 | 2025-10-04 04:14:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3ad9d46f-f2cd-38c5-9e2c-af543a311e51 | -12.5467 | -41.30291 | 2025-10-04 04:14:00 | NOAA-20 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 0af00ead-4872-3c8a-905a-2e4485652fa2 | -8.22673 | -46.8062 | 2025-10-04 04:14:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 46c4bf5c-48ca-3283-be3c-e6f7f88fc830 | -9.56161 | -48.68231 | 2025-10-04 04:14:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e3a3a5aa-bb2d-3ac1-b9e2-3f354d8a7786 | -13.33469 | -47.62043 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| adc5cd12-47ca-3efd-8252-c5e7b42387b2 | -12.27278 | -47.81327 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e2e81428-8f43-3b29-8bac-725dc40fbde0 | -9.9356 | -50.24593 | 2025-10-04 04:14:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ddb619bf-cbcd-349a-998b-e6a9eeabb46a | -14.35112 | -46.10921 | 2025-10-04 04:14:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 527d7779-bfaa-36dc-89af-eeeae285fb82 | -12.52665 | -45.97703 | 2025-10-04 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| cebbc169-a9e7-36b4-a7ea-43bd9dfbc2b2 | -11.68038 | -44.2713 | 2025-10-04 04:14:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0cd14232-9c5e-3685-af8c-41db0dfb7d9c | -13.33537 | -47.58121 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cadd5b67-b23e-3775-af7d-f60610eb258c | -12.38786 | -54.45557 | 2025-10-04 04:14:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 051c3962-736c-3477-b6f9-af102303c145 | -9.19647 | -50.75837 | 2025-10-04 04:14:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 89f4d133-e958-3a2f-9f23-4d605f187c4c | -11.08011 | -47.8802 | 2025-10-04 04:14:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 32141489-635f-345b-8548-2a74893d37fa | -15.31722 | -46.37901 | 2025-10-04 04:14:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b90a20a1-5258-3d79-b20c-495de7c60f74 | -12.29684 | -55.13374 | 2025-10-04 04:14:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 02df7b88-21c1-3839-83e4-2389b1a737ad | -13.32088 | -47.2553 | 2025-10-04 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0c3bc05d-12a6-32e4-b241-06f0aa6fe37c | -14.97304 | -46.8463 | 2025-10-04 04:14:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 91a548a6-558e-3c80-86d8-46f17252d01b | -13.29951 | -47.81773 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 26769d05-c767-3d62-b06f-c2473542862b | -8.53622 | -50.16297 | 2025-10-04 04:14:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 72b1be0b-2815-3a88-8897-e095178d27c4 | -13.51012 | -47.27396 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9fe591f7-2b93-35e3-b6cc-1ebe59da0bc5 | -13.55334 | -47.25344 | 2025-10-04 04:14:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 98ba8fae-c006-3b63-bbf1-e373ab70552d | -14.22062 | -46.08329 | 2025-10-04 04:14:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0c5623fc-3278-329c-b306-749e4bd5eecc | -8.6078 | -54.965 | 2025-10-04 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ed95ba22-ebdf-3750-8d0a-fa5881a9c6ad | -11.90767 | -46.36947 | 2025-10-04 04:14:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fa2a3986-f91f-348f-a636-1a776cab5fda | -11.91308 | -46.37357 | 2025-10-04 04:14:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8ab3513e-2a9a-32c1-b439-f959007d1b05 | -15.19124 | -46.39876 | 2025-10-04 04:14:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0ff16687-d5fa-3b10-9a69-1145040909a9 | -8.92118 | -46.61519 | 2025-10-04 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6302520b-8bb0-3a57-9f2b-87d3a7bb4333 | -11.12667 | -47.2062 | 2025-10-04 04:14:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eab24486-c597-303b-9343-d005656c2bc4 | -11.90705 | -46.37328 | 2025-10-04 04:14:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README78.md)

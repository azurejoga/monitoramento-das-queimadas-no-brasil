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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 10b48e1b-fdc1-3ed4-8adb-8e7b75ae53c9 | -22.6423 | -47.44759 | 2025-08-23 04:55:00 | NOAA-21 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9b9182d1-a53e-31ec-aa5d-a0937c3c3413 | -20.8744 | -42.54358 | 2025-08-23 04:55:00 | NOAA-21 | ERVÁLIA | MINAS GERAIS | Brasil | 3124005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.2 |
| 4aedd9d4-9f99-3873-adc7-df47de9d1076 | -22.17273 | -43.28371 | 2025-08-23 04:55:00 | NOAA-21 | PARAÍBA DO SUL | RIO DE JANEIRO | Brasil | 3303708 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 6ea9f761-ed4c-3523-8045-574bad857f65 | -19.9472 | -47.49146 | 2025-08-23 04:55:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4c8d9d5d-8072-30c0-93c6-bfabe6cb2b67 | -20.47846 | -53.67701 | 2025-08-23 04:55:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8609d260-c9c2-3362-a70d-24767b372201 | -24.66798 | -49.44545 | 2025-08-23 04:55:00 | NOAA-21 | DOUTOR ULYSSES | PARANÁ | Brasil | 4128633 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| e13b8d35-3c8b-3bdf-b080-5f01f231e9a6 | -17.59105 | -46.56183 | 2025-08-23 04:55:00 | NOAA-21 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 0a660130-07ef-3f35-97d4-18cc956132e4 | -22.64448 | -47.44685 | 2025-08-23 04:55:00 | NOAA-21 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 6.9 |
| ad596891-84f8-3906-b256-e0eda182dd60 | -17.59175 | -46.55556 | 2025-08-23 04:55:00 | NOAA-21 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| f7dfe70b-15f0-3749-baf0-eb2dda36855a | -23.74385 | -51.0997 | 2025-08-23 04:55:00 | NOAA-21 | TAMARANA | PARANÁ | Brasil | 4126678 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 661cd683-cb12-3b21-94e4-bbf132939fb0 | -17.5921 | -46.55243 | 2025-08-23 04:55:00 | NOAA-21 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 54d4c654-c9a9-332d-b87c-e74be12fbdfc | -22.90247 | -46.39564 | 2025-08-23 04:55:00 | NOAA-21 | VARGEM | SÃO PAULO | Brasil | 3556354 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 9e928be5-4ed7-325f-abf0-7ad5a0f817c6 | -18.86308 | -49.46854 | 2025-08-23 04:55:00 | NOAA-21 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 830a34c6-c31a-36cf-a47b-9827a27f709e | -22.47355 | -44.27789 | 2025-08-23 04:55:00 | NOAA-21 | BARRA MANSA | RIO DE JANEIRO | Brasil | 3300407 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 1cf2f1f4-382c-3721-b65f-3d2c45d123a1 | -20.44514 | -42.13609 | 2025-08-23 04:55:00 | NOAA-21 | SÃO JOÃO DO MANHUAÇU | MINAS GERAIS | Brasil | 3162559 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| 41453715-2040-36cb-9dfc-7fb832210ac3 | -22.66339 | -46.91608 | 2025-08-23 04:55:00 | NOAA-21 | SANTO ANTÔNIO DE POSSE | SÃO PAULO | Brasil | 3548005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| dfe00af1-aeee-3b19-aef2-32d6498e4a3b | -20.18879 | -50.96642 | 2025-08-23 04:55:00 | NOAA-21 | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 08eddde5-c7d8-3a63-ae79-d377e1cb523f | -22.19292 | -44.55479 | 2025-08-23 04:55:00 | NOAA-21 | BOCAINA DE MINAS | MINAS GERAIS | Brasil | 3107208 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| 4d5c4ea4-2924-3551-800d-4367b996964b | -22.53926 | -43.72372 | 2025-08-23 04:55:00 | NOAA-21 | MENDES | RIO DE JANEIRO | Brasil | 3302809 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| a7a5d0e6-9f4f-386c-88b2-0775b2481ddd | -17.61009 | -46.69963 | 2025-08-23 04:55:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ce9a2f33-e281-32c3-8d14-861030b017b9 | -22.633 | -47.43662 | 2025-08-23 04:55:00 | NOAA-21 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b8d74b65-e59f-3292-89ee-e9c50468730b | -19.32119 | -46.83952 | 2025-08-23 04:55:00 | NOAA-21 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a2609855-99e0-35fb-befc-1b5ec5e4f3f7 | -22.63235 | -47.44297 | 2025-08-23 04:55:00 | NOAA-21 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 21c31fa6-6e98-35ab-b87e-8d19ed77803b | -22.19251 | -44.55987 | 2025-08-23 04:55:00 | NOAA-21 | BOCAINA DE MINAS | MINAS GERAIS | Brasil | 3107208 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| 51706992-273d-371f-8cad-70538f073c9d | -20.87236 | -42.54459 | 2025-08-23 04:55:00 | NOAA-21 | ERVÁLIA | MINAS GERAIS | Brasil | 3124005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 20.8 |
| 08b2aedf-b9dc-3a29-9d8e-69b754c75675 | -19.96575 | -47.51802 | 2025-08-23 04:55:00 | NOAA-21 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e8e31408-f089-39e6-8ebb-d0e9f39c5867 | -23.16105 | -48.74029 | 2025-08-23 04:55:00 | NOAA-21 | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 42f5cf1c-2fb5-39bc-a5e9-224d7cb4192d | -19.94844 | -47.48015 | 2025-08-23 04:55:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7535ee2a-ead2-3fd9-ac7c-76eb6a8b5440 | -22.62937 | -47.44155 | 2025-08-23 04:55:00 | NOAA-21 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 072a9036-0e4a-3fab-933b-779ff6c4c818 | -22.64263 | -47.44434 | 2025-08-23 04:55:00 | NOAA-21 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9b76fe97-efd9-33ce-982f-f6d59fef8c25 | -17.07863 | -53.37928 | 2025-08-23 04:55:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f7593546-7564-3056-a757-bf4d376d675c | -22.64933 | -47.45062 | 2025-08-23 04:55:00 | NOAA-21 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c1513552-5c70-3426-a64e-5ad27aec2e0c | -22.64902 | -47.45387 | 2025-08-23 04:55:00 | NOAA-21 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e39e72dd-cdb2-3650-a9e3-aab32a2d16ae | -19.96141 | -47.51144 | 2025-08-23 04:55:00 | NOAA-21 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cdcf3b14-c957-3c42-b665-dff2a071193a | -22.54001 | -43.72354 | 2025-08-23 04:55:00 | NOAA-21 | MENDES | RIO DE JANEIRO | Brasil | 3302809 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| cd3b750a-2be2-3b60-ab4b-9685e1755ceb | -17.61042 | -46.69657 | 2025-08-23 04:55:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0f04ea61-6d28-30c4-b972-b21e204f288d | -16.52771 | -55.02782 | 2025-08-23 04:55:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d552aa99-5fcd-3b2b-87b0-f3b980f76c34 | -22.47555 | -44.27815 | 2025-08-23 04:55:00 | NOAA-21 | BARRA MANSA | RIO DE JANEIRO | Brasil | 3300407 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 3f7e50c5-4936-3712-9989-b508a7fc2ec7 | -22.48134 | -44.2844 | 2025-08-23 04:55:00 | NOAA-21 | BARRA MANSA | RIO DE JANEIRO | Brasil | 3300407 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 2046c8a3-2d83-3638-92d0-975c2a07bc25 | -20.09288 | -47.74732 | 2025-08-23 04:55:00 | NOAA-21 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f8247173-d4ae-3bde-b652-163e6e91497e | -22.64995 | -47.44404 | 2025-08-23 04:55:00 | NOAA-21 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 769286c2-1a3f-35ec-a260-b6056944780d | -17.57855 | -48.74392 | 2025-08-23 04:55:00 | NOAA-21 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bd501dbd-5772-3034-b2e8-302b7d9ca0e5 | -22.7718 | -43.68481 | 2025-08-23 04:55:00 | NOAA-21 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 9436e98d-3535-3d41-9ba8-5db721c66b2d | -19.95652 | -47.51014 | 2025-08-23 04:55:00 | NOAA-21 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f08f4d30-fbbd-3b7a-b23f-94379866791e | -18.95349 | -50.02541 | 2025-08-23 04:55:00 | NOAA-21 | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8e2a5412-95f8-3e2c-b98c-56b5aaa906b1 | -22.77188 | -43.68268 | 2025-08-23 04:55:00 | NOAA-21 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 136bfba0-4746-3f1a-9b96-58c9ac4e2052 | -21.44537 | -52.66393 | 2025-08-23 04:55:00 | NOAA-21 | SANTA RITA DO PARDO | MATO GROSSO DO SUL | Brasil | 5007554 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7b85e62d-46da-38b4-8246-11af34adcb0c | -23.74138 | -51.10022 | 2025-08-23 04:55:00 | NOAA-21 | TAMARANA | PARANÁ | Brasil | 4126678 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 281e9d79-e7b9-344c-80ac-9407182368e8 | -20.56466 | -54.6181 | 2025-08-23 04:55:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 10db79ac-67fa-3068-95f0-c00aa9ba4974 | -22.62721 | -47.44231 | 2025-08-23 04:55:00 | NOAA-21 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2a0c83d3-39c5-3896-bb56-4b838eb1bac4 | -20.44515 | -42.13415 | 2025-08-23 04:55:00 | NOAA-21 | SÃO JOÃO DO MANHUAÇU | MINAS GERAIS | Brasil | 3162559 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.9 |
| d5479425-d7f8-3c00-b7c6-1dadc5f08ba5 | -22.21739 | -56.19243 | 2025-08-23 04:55:00 | NOAA-21 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c3af554c-0a78-3110-a9c6-5b9dccbfbeb2 | -20.44548 | -42.13174 | 2025-08-23 04:55:00 | NOAA-21 | SÃO JOÃO DO MANHUAÇU | MINAS GERAIS | Brasil | 3162559 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| 75e49764-a329-33c6-86f6-f07ef6a8ef92 | -17.59484 | -49.42578 | 2025-08-23 04:55:00 | NOAA-21 | PONTALINA | GOIÁS | Brasil | 5217708 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 55a030db-607b-36ce-b7a6-07ded47b987a | -17.88029 | -53.20697 | 2025-08-23 04:55:00 | NOAA-21 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7666e8a4-2ac5-3659-bd96-6487d260bf50 | -20.34907 | -46.51987 | 2025-08-23 04:55:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 25846c97-87dd-3956-9cb6-10c394d581ac | -17.27794 | -53.26049 | 2025-08-23 04:55:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7aadeaee-d831-369d-8816-850830ef112c | -20.35415 | -46.52287 | 2025-08-23 04:55:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6766be59-a95b-3deb-ba8c-7ce91cd8346c | -17.12297 | -53.38626 | 2025-08-23 04:55:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9b302e68-7549-3bd1-b3f6-234ce2f7fe79 | -17.68165 | -50.09691 | 2025-08-23 04:55:00 | NOAA-21 | EDÉIA | GOIÁS | Brasil | 5207402 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f29f915e-2bae-364d-8fbd-13bcb7a7ddea | -22.66272 | -46.92305 | 2025-08-23 04:55:00 | NOAA-21 | SANTO ANTÔNIO DE POSSE | SÃO PAULO | Brasil | 3548005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| cb92e573-9805-3538-8fb8-910c7d77eac2 | -19.94778 | -47.48614 | 2025-08-23 04:55:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8543204d-0a67-344d-b6cb-0ff4c0a1c074 | -23.74088 | -51.10431 | 2025-08-23 04:55:00 | NOAA-21 | LONDRINA | PARANÁ | Brasil | 4113700 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e65ca9e9-aa42-3bdf-8ec8-51f2a4dbd657 | -20.88022 | -54.99961 | 2025-08-23 04:55:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fe27eff6-514f-3360-989e-13e7b5843388 | -23.74338 | -51.10376 | 2025-08-23 04:55:00 | NOAA-21 | TAMARANA | PARANÁ | Brasil | 4126678 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 38911d23-fb28-30e9-b09a-66b621464bb9 | -20.48206 | -54.73297 | 2025-08-23 04:55:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 76c9c994-5aaf-3e40-85de-fe1b34ffe61f | -17.80935 | -52.06573 | 2025-08-23 04:55:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| aaefd38b-54f9-3151-b473-c2625a9a0a55 | -17.59545 | -46.5687 | 2025-08-23 04:55:00 | NOAA-21 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 734ef3eb-2cc9-3938-ac71-88e2cee2cd08 | -17.88085 | -53.20306 | 2025-08-23 04:55:00 | NOAA-21 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| af8d8a07-2270-37da-b647-6a403f6b91ac | -22.5324 | -43.72819 | 2025-08-23 04:55:00 | NOAA-21 | MENDES | RIO DE JANEIRO | Brasil | 3302809 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 4e5d4e29-3add-334b-ae0f-63a6b04fcd2d | -17.61075 | -46.6935 | 2025-08-23 04:55:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d0fb83ad-44e2-3eca-a46e-b1861814a2e3 | -17.59069 | -46.56496 | 2025-08-23 04:55:00 | NOAA-21 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 14.3 |
| ac3245eb-7ca8-3627-832e-6ea22e6d349f | -19.97496 | -47.5129 | 2025-08-23 04:55:00 | NOAA-21 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c0799579-71fe-316c-8ab4-ec505f064516 | -22.17462 | -43.28184 | 2025-08-23 04:55:00 | NOAA-21 | PARAÍBA DO SUL | RIO DE JANEIRO | Brasil | 3303708 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 54d1ee85-9b2f-399c-b26b-ffc555a0ddf2 | -23.49284 | -47.63152 | 2025-08-23 04:55:00 | NOAA-21 | ARAÇOIABA DA SERRA | SÃO PAULO | Brasil | 3502903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 4fbce98f-4dd1-39ac-bada-95aa641daf40 | -22.47937 | -44.28425 | 2025-08-23 04:55:00 | NOAA-21 | BARRA MANSA | RIO DE JANEIRO | Brasil | 3300407 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| e3f878c8-f8b9-3f62-bbb6-16a5918f4dc4 | -22.64197 | -47.45082 | 2025-08-23 04:55:00 | NOAA-21 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3cc9520f-4d93-3f61-b264-fe6cc4fe6c89 | -19.94281 | -47.48563 | 2025-08-23 04:55:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 27048e90-2794-32df-852f-45161c28ac8d | -17.58663 | -46.55491 | 2025-08-23 04:55:00 | NOAA-21 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 85f15668-d745-327b-85bc-618c0fbd3cdb | -23.39437 | -50.35489 | 2025-08-23 04:55:00 | NOAA-21 | RIBEIRÃO DO PINHAL | PARANÁ | Brasil | 4121901 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 862a26d1-53c1-3e15-8400-f18c1635c569 | -17.66164 | -50.12424 | 2025-08-23 04:55:00 | NOAA-21 | EDÉIA | GOIÁS | Brasil | 5207402 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| aff1d731-e9de-3602-9227-4df45ddf86f8 | -16.84656 | -53.19431 | 2025-08-23 04:55:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 066c3bd2-a4b4-3550-9b23-0936b4cd0e1e | -17.59581 | -46.56559 | 2025-08-23 04:55:00 | NOAA-21 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 9e58cae6-30eb-32e7-b0e6-d03263edc6b8 | -18.68492 | -41.19551 | 2025-08-23 04:55:00 | NOAA-21 | SÃO JOÃO DO MANTENINHA | MINAS GERAIS | Brasil | 3162575 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 1896a5d2-fa3c-36e6-ae57-94df81e791fa | -22.47599 | -44.27283 | 2025-08-23 04:55:00 | NOAA-21 | BARRA MANSA | RIO DE JANEIRO | Brasil | 3300407 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 2b2262ad-8ebc-3ce8-9ab9-7603fb74b5b7 | -18.97005 | -52.46814 | 2025-08-23 04:55:00 | NOAA-21 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 192dc871-093a-3d96-b489-05e4976a2860 | -21.95313 | -45.59063 | 2025-08-23 04:55:00 | NOAA-21 | SÃO GONÇALO DO SAPUCAÍ | MINAS GERAIS | Brasil | 3162005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 557b4de0-8a26-3920-a923-58d74eabca98 | -22.49279 | -43.82022 | 2025-08-23 04:55:00 | NOAA-21 | BARRA DO PIRAÍ | RIO DE JANEIRO | Brasil | 3300308 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 0a326188-bf86-3ea2-8658-7b205033b431 | -17.60059 | -46.09294 | 2025-08-23 04:55:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8e6486a4-f22d-321f-a69e-73b87de8d6fb | -19.52385 | -47.08503 | 2025-08-23 04:55:00 | NOAA-21 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 963fcaee-3659-325e-8314-9329c96e5ad0 | -20.44613 | -42.12343 | 2025-08-23 04:55:00 | NOAA-21 | LUISBURGO | MINAS GERAIS | Brasil | 3138674 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 2935a6aa-0097-35b2-ba63-b0706df51967 | -17.57781 | -48.74562 | 2025-08-23 04:55:00 | NOAA-21 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0dd55341-ea82-39a5-9808-1e2e4ab50c02 | -22.53359 | -43.72232 | 2025-08-23 04:55:00 | NOAA-21 | MENDES | RIO DE JANEIRO | Brasil | 3302809 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| e7b6b07c-3140-3b9f-9ff7-0a096c4f4f7a | -19.52352 | -47.08808 | 2025-08-23 04:55:00 | NOAA-21 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b5b882f2-fe61-3f70-8e19-fbe9bf426159 | -22.30608 | -43.16707 | 2025-08-23 04:55:00 | NOAA-21 | AREAL | RIO DE JANEIRO | Brasil | 3300225 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| d921a463-9f51-3a7f-a9c8-42ba5d3fcc09 | -17.58593 | -46.56118 | 2025-08-23 04:55:00 | NOAA-21 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 20.7 |
| d73dd07c-a777-35d2-b33b-53c847d7d07c | -17.59246 | -46.5493 | 2025-08-23 04:55:00 | NOAA-21 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e86042ef-b732-38d7-b48f-226de1c02925 | -20.56185 | -54.61372 | 2025-08-23 04:55:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7c59c270-6a9f-3130-ad1d-97d51f66824b | -20.08697 | -46.12086 | 2025-08-23 04:55:00 | NOAA-21 | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4f208b8f-8d17-36d4-aeb8-6db44242e8c9 | -20.19276 | -50.96697 | 2025-08-23 04:55:00 | NOAA-21 | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |


[Clique aqui para ver as próximas entradas](README57.md)

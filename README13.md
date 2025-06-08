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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 09c8831a-f31d-389d-bb10-b0f550f3844c | -9.18593 | -63.33322 | 2025-06-08 05:18:00 | NOAA-21 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 215dbc15-be82-3d7a-9644-b822f33aafa0 | -11.12727 | -54.64273 | 2025-06-08 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 55f0ff65-431f-3f22-8633-39489a050c6b | -12.37591 | -57.41039 | 2025-06-08 05:18:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 90558072-25a7-3162-b143-fc9505aec790 | -9.43253 | -62.28913 | 2025-06-08 05:18:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f696dbd1-f74b-3427-8b1e-6d1ef2a9b9dc | -7.89336 | -61.47279 | 2025-06-08 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f5e3d2b2-71b7-3aa8-8294-bf9ae4989a6d | -8.77553 | -47.18417 | 2025-06-08 05:18:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| db0d2cf5-4288-3bab-bd99-afb3e3dcb6e7 | -10.33883 | -57.48798 | 2025-06-08 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ae10b09d-23c6-3ea0-8c84-d957c98162cf | -11.80085 | -48.09238 | 2025-06-08 05:18:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 3a45fc7e-3c99-3f98-9d53-59d16679d57a | -10.39709 | -47.00834 | 2025-06-08 05:18:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 82e20866-8c68-39ee-b3bd-c6a66490aac6 | -9.92711 | -59.90061 | 2025-06-08 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0e718fe1-6ab2-371a-bd48-fd24a1c284ab | -11.12346 | -54.65108 | 2025-06-08 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6a801aa0-5363-36bd-8779-1af380da566a | -11.25987 | -60.7934 | 2025-06-08 05:18:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0bbf54df-f28f-3d91-b1b9-ce51a8f3f150 | -12.66561 | -58.21959 | 2025-06-08 05:18:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5d14b855-293e-3392-a074-af71c9c7eaf1 | -11.13831 | -53.94423 | 2025-06-08 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bf839dfa-e53b-37f2-aa24-2a7eca887c6e | -9.40302 | -48.44048 | 2025-06-08 05:18:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 923125e6-17cf-3b2f-b424-9b605487bf39 | -11.12398 | -54.64734 | 2025-06-08 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ce4ecde1-cc33-3e27-b325-0d0c8393d8b7 | -10.95011 | -55.33433 | 2025-06-08 05:18:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1935cf45-71b0-39d0-9ea2-9448bf53ea87 | -12.52386 | -58.34747 | 2025-06-08 05:18:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 57c9dd9b-7e57-313b-af0c-5c0726b00cb6 | -11.12677 | -54.6465 | 2025-06-08 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ac98a4de-c0dd-3614-80ab-61350fcbf480 | -12.37176 | -57.41396 | 2025-06-08 05:18:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2d020d61-0c96-3ead-9475-5cd42d6be992 | -11.12812 | -54.64788 | 2025-06-08 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8954ccd4-73ce-3bea-82cc-8fbd3df01b23 | -9.07734 | -47.14279 | 2025-06-08 05:18:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| fbd41754-94e0-319e-be2a-462a423e6ba2 | -7.90791 | -61.51385 | 2025-06-08 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bede68f5-da72-305d-a995-9690a26ccc9f | -9.85356 | -62.21682 | 2025-06-08 05:18:00 | NOAA-21 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 864c1d8b-15e5-3a78-972e-7e9aab9ac8f6 | -12.96699 | -46.75104 | 2025-06-08 05:18:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9b5d379c-df2b-3543-a72c-ab5d8fed32cb | -12.95996 | -46.75002 | 2025-06-08 05:18:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 89cf61af-f7fb-3f15-adce-c9192b1a5e59 | -12.53129 | -58.34473 | 2025-06-08 05:18:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 42ae3d00-7258-3378-8f7b-3f8f42594dc9 | -12.52159 | -58.36269 | 2025-06-08 05:18:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 41c11ee1-a59b-33e8-be58-d415599df4f0 | -10.53746 | -56.3866 | 2025-06-08 05:18:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d239f703-a0ba-3bde-8ac5-1aed8d9cd4c0 | -8.52406 | -50.02391 | 2025-06-08 05:18:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d6717b09-414f-31d2-aaa3-147151c9d0ec | -11.4689 | -61.94703 | 2025-06-08 05:18:00 | NOAA-21 | CASTANHEIRAS | RONDÔNIA | Brasil | 1100908 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b3a27ecd-eba9-3b8b-a8d1-4ec6f6b42938 | -12.5233 | -58.35128 | 2025-06-08 05:18:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 988ee32d-043e-3bb0-8307-4c14ddcdba5d | -11.5476 | -56.45253 | 2025-06-08 05:18:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 36b57c8d-ba7a-3359-b400-a9a911c78b5e | -12.21055 | -49.63633 | 2025-06-08 05:18:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2212d2ce-7c71-3619-b685-86dadd814ece | -9.64826 | -55.16225 | 2025-06-08 05:18:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3ebaa53d-b62f-3f29-97b8-cb998cc8c659 | -12.37533 | -57.41449 | 2025-06-08 05:18:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b0daf36f-3b57-3f81-aedb-1ded9147515c | -12.26887 | -55.07787 | 2025-06-08 05:18:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ba8d8e06-5490-3f72-8294-c0f4ab950927 | -10.40456 | -47.00321 | 2025-06-08 05:18:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fed42e0e-234f-3740-9d3b-55133182ecad | -12.66964 | -58.21624 | 2025-06-08 05:18:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| aef6b9e9-2e22-381a-ae47-5a14f2a44f88 | -8.3094 | -55.0999 | 2025-06-08 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 46e8b324-0a40-36d9-966c-a72cdd21df1a | -9.40359 | -48.43582 | 2025-06-08 05:18:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 98d308a6-180d-35ed-a769-c576f9689d5e | -12.36691 | -57.40245 | 2025-06-08 05:18:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 5a15d5a0-0311-3af0-96a2-63e67fa58cb3 | -12.36996 | -57.40107 | 2025-06-08 05:18:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 6e78dc7d-8415-3c30-ba68-5dbaf885f2b8 | -11.11985 | -54.64678 | 2025-06-08 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f7370cda-f219-3260-995d-2aa1958f6d4a | -12.3682 | -57.41341 | 2025-06-08 05:18:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 239d8cd1-455b-3228-bf2a-098244b04576 | -11.54325 | -56.45647 | 2025-06-08 05:18:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5d76228b-7bbc-3310-9c05-08443420f8fd | -12.53072 | -58.34855 | 2025-06-08 05:18:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 74358cfc-5359-371e-89c8-3174416b76c0 | -7.90508 | -61.50952 | 2025-06-08 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fbd10393-b649-3eb3-a7ec-6352d1c64152 | -7.90447 | -61.51331 | 2025-06-08 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e360b4e1-cad3-32f5-914c-24c994123a04 | -11.12504 | -54.63982 | 2025-06-08 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 55bc64e7-bef1-3f5a-91fa-5e0ac0e18340 | -12.53301 | -58.35673 | 2025-06-08 05:18:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 92fa0eac-36b2-31f1-a32a-bc9892a600ed | -10.29716 | -57.13324 | 2025-06-08 05:18:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 273d9319-6c19-3dac-9d1a-872a37699e99 | -12.52901 | -58.36 | 2025-06-08 05:18:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 491715a3-dd87-3733-9153-d67336d5de1f | -12.27344 | -55.07475 | 2025-06-08 05:18:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fa65ef8c-3cc2-3f17-89f8-4be3fbc82cbe | -9.41406 | -48.4516 | 2025-06-08 05:18:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 5c9dbac3-6b1b-3e48-be14-d69a8300202e | -11.55131 | -56.45306 | 2025-06-08 05:18:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bbc6f9ab-e742-338b-86cf-f329356b97e6 | -9.26828 | -56.29519 | 2025-06-08 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b0775ba6-705a-35f9-95fd-933bb5526c7e | -13.3685 | -54.25092 | 2025-06-08 05:18:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6bb1b905-9187-3a6c-b4b6-ada624d20f8c | -11.83146 | -57.8189 | 2025-06-08 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b0c070f9-0c47-3898-b29a-9d84686dc488 | -12.52729 | -58.348 | 2025-06-08 05:18:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 36c07e92-8a0c-33f7-8c52-5d27e7c7a6f4 | -11.14263 | -53.9449 | 2025-06-08 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 32bca522-c86c-3800-8e19-49b60387ae77 | -11.54515 | -56.443 | 2025-06-08 05:18:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 20a5f9e7-643e-393a-a6bb-2cc1f8499703 | -12.37235 | -57.40984 | 2025-06-08 05:18:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 793c7683-8875-356f-b9f8-98de331cf463 | -11.11933 | -54.65052 | 2025-06-08 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1b0bf4a1-2230-379b-9b44-1ddd28d17e3b | -10.49215 | -53.66584 | 2025-06-08 05:18:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 85355dda-582d-3e16-8130-850cd58e9c03 | -12.02482 | -57.08982 | 2025-06-08 05:18:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bdd0a669-2106-3ee2-bec3-06ee16edfedb | -11.78592 | -54.77915 | 2025-06-08 05:18:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3c16ca30-7942-34e9-af2b-0dd386656c59 | -9.40797 | -48.4507 | 2025-06-08 05:18:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 1968a6cb-e9d3-3465-9e0b-336b55a32783 | -10.49651 | -53.66655 | 2025-06-08 05:18:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 278cbef5-7164-336e-b954-d1aebbe291d4 | -10.53379 | -56.38601 | 2025-06-08 05:18:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2400ce5a-be59-38aa-8a99-51d972ac1e40 | -11.54388 | -56.45199 | 2025-06-08 05:18:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7991097a-7bb8-337a-8857-823f7d792465 | -11.12091 | -54.63928 | 2025-06-08 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| a60b14d4-ba7b-367e-83d5-1fa7c7fe836d | -10.39365 | -47.00106 | 2025-06-08 05:18:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 73a351de-7e09-3f61-8af1-8d8322d6253c | -11.46951 | -61.94333 | 2025-06-08 05:18:00 | NOAA-21 | CASTANHEIRAS | RONDÔNIA | Brasil | 1100908 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| eb50c6bf-9742-3d7a-8f10-2a7fd8a6932b | -8.52789 | -50.02592 | 2025-06-08 05:18:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| f51516a8-610a-3337-a32c-a88c56e9b642 | -9.40417 | -48.43115 | 2025-06-08 05:18:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 583a117f-7818-3dbc-9483-1f16619081cd | -11.53954 | -56.45592 | 2025-06-08 05:18:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e49dbddf-c17e-3941-ad5e-736ef9740dbd | -9.62078 | -55.09965 | 2025-06-08 05:18:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ad38656f-5b69-3e4c-92e9-869bbd674569 | -9.07869 | -47.1441 | 2025-06-08 05:18:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 348486d0-0ace-3cd5-a714-082e1bca9899 | -8.52838 | -50.02231 | 2025-06-08 05:18:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 33b2c0b8-f38f-3910-8517-31258a8690d2 | -9.07139 | -47.14894 | 2025-06-08 05:18:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4f563439-9027-37a4-ad0f-4a26ebaac721 | -12.36878 | -57.4093 | 2025-06-08 05:18:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 6a8e7b98-cddb-36dc-a6d3-902a70a722ee | -9.40854 | -48.44608 | 2025-06-08 05:18:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 36406c80-9ca9-3969-b67d-fa8d3ffdba52 | -11.80145 | -48.08713 | 2025-06-08 05:18:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 1a52396d-c3f3-3198-bd0a-5e62719fde87 | -9.26739 | -56.29712 | 2025-06-08 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5d8ae4ae-d5fa-3fca-805e-24e03ebb6233 | -10.4004 | -47.00194 | 2025-06-08 05:18:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e8a8f52b-a91c-38dc-8547-0846cd12abe4 | -11.79503 | -48.08617 | 2025-06-08 05:18:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| f23cccc3-e6f6-3e13-ab8c-10247d08433c | -11.80728 | -48.0932 | 2025-06-08 05:18:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b2736ec6-ba75-3b63-85b5-c823ab3a1f73 | -12.52559 | -58.35944 | 2025-06-08 05:18:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 750c4e67-5c06-3f92-93d6-581e06bfec68 | -12.52844 | -58.3638 | 2025-06-08 05:18:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ab522654-795f-30f2-b0e9-067e319d8297 | -11.12451 | -54.64359 | 2025-06-08 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 952ed60d-5b2f-37dd-b650-345d1341a605 | -8.52903 | -50.02841 | 2025-06-08 05:18:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b151253f-f623-37c0-825f-b58da4533de7 | -9.41463 | -48.44698 | 2025-06-08 05:18:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 9c7a448e-0822-337e-ac7b-4c921343765a | -12.37294 | -57.40572 | 2025-06-08 05:18:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 9f07277d-31c8-3907-b538-7708303f9170 | -11.54887 | -56.44354 | 2025-06-08 05:18:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4f0047ef-354d-3e27-9839-4e8aff9a7026 | -12.52502 | -58.36325 | 2025-06-08 05:18:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9cf16a70-b9be-35cf-bf05-7522c4299fda | -10.75349 | -48.57885 | 2025-06-08 05:18:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ccfa17fc-e16b-376e-b6c8-31ee18ba0768 | -9.84439 | -48.60774 | 2025-06-08 05:18:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 72b0c900-a426-3bc4-b522-ba01ad3c911a | -14.88986 | -48.12401 | 2025-06-08 05:21:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 2a46720a-a636-37b6-a098-6816357ccc6a | -18.72112 | -54.19213 | 2025-06-08 05:21:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README14.md)

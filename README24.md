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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 80e09a96-c1d5-39e7-948b-cc31e9c46358 | -8.3903 | -62.6963 | 2026-08-21 04:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 54.2 |
| f9fe8f3a-1c39-357f-9bb7-763b7f0e4ffa | -9.4069 | -60.4362 | 2026-08-21 04:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 94.8 |
| be7f8fb2-a4e2-38e3-a98a-fd8e39b5c2b8 | -6.1177 | -59.9069 | 2026-08-21 04:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 570249e0-0496-3ac7-950e-13e20f1ed1be | -6.2341 | -55.6109 | 2026-08-21 04:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 93.6 |
| a0869fde-935a-3d92-a669-fc98dad9878d | -9.4259 | -60.3967 | 2026-08-21 04:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 64.6 |
| b7411366-7123-308e-b300-05694a9eed2f | -6.2156 | -55.6118 | 2026-08-21 04:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| e7eb7418-8383-3827-959b-9e84ef5431af | -11.1747 | -54.0216 | 2026-08-21 04:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 44a12acf-b1b4-3d81-aac8-0a65ccf7bd3d | -7.36 | -45.8361 | 2026-08-21 04:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 50.4 |
| 86aba9ff-6987-3bd5-8b83-d6cff4f07330 | -11.1558 | -54.0233 | 2026-08-21 04:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 990a6fcf-ab55-3a8b-b3f4-f2d10502bd71 | -7.3415 | -45.8152 | 2026-08-21 04:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 52.3 |
| 6215c48b-e5f1-3f07-8f0e-026b31c24207 | -3.5406 | -48.1889 | 2026-08-21 04:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 90.6 |
| 7a7c21c6-aa60-39e6-9a03-dd6668820f91 | -6.6938 | -58.942 | 2026-08-21 04:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 0bfce597-86ac-3111-b76f-0d73c39c9a84 | -9.4071 | -60.417 | 2026-08-21 04:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 226.5 |
| 7c67b1a5-c8ec-3888-b3fe-3ceadec1c33e | -9.4072 | -60.3977 | 2026-08-21 04:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 75.8 |
| e4de2a98-88be-3656-9b09-d699af56b0bd | -9.3885 | -60.4179 | 2026-08-21 04:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 2e502826-2581-3793-90bf-b31d47c720bb | -7.45786 | -46.15633 | 2026-08-21 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 42e789ec-94fd-3cd2-8bbf-f36559b8f039 | -4.1106 | -48.93482 | 2026-08-21 04:00:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4006bf48-ccb6-3bae-8980-555cf317aaf6 | -4.01239 | -48.06494 | 2026-08-21 04:00:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 02bbf6bc-b4e2-30ec-b906-490047b05a01 | -3.98031 | -47.20633 | 2026-08-21 04:00:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 400c8747-f41d-3428-a8e7-3f0fe3ed173f | -3.00759 | -40.43438 | 2026-08-21 04:00:00 | NOAA-20 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c2c88653-6763-3e5d-9fd7-7b93f6c59047 | -6.27363 | -43.27675 | 2026-08-21 04:00:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b0ad7635-e429-3b61-bfd9-078f861c8757 | -5.12259 | -40.59488 | 2026-08-21 04:00:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1faf9d93-1c43-32bb-a735-e513a0e6ce7a | -6.87092 | -43.74499 | 2026-08-21 04:00:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f39dbeeb-ccc1-34a3-af38-f18413672e7d | -4.11138 | -48.93032 | 2026-08-21 04:00:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 91daf469-c56f-3d34-939e-3c19b51196b1 | -5.59935 | -44.00556 | 2026-08-21 04:00:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 29.0 |
| 3fcb1b7e-ffca-3685-8ff7-c1e8d55c9f1d | -6.8796 | -43.74277 | 2026-08-21 04:00:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 478b9a44-2e12-3ddf-89b7-41818da31ce0 | -7.36425 | -45.82325 | 2026-08-21 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| ae5b1b7d-4ef5-3ff1-b1dd-cb97ad2d22b5 | -7.36884 | -45.82412 | 2026-08-21 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c02cbe3b-beda-3468-aa34-a1d10531b0ee | -7.03132 | -45.89667 | 2026-08-21 04:00:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9f901e8b-a5b6-303e-857a-359dcc6dd00d | -4.05087 | -50.30042 | 2026-08-21 04:00:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 99f1ac7b-ac56-359f-994a-c00cb27a2f5d | -7.36215 | -45.80814 | 2026-08-21 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 44.2 |
| e7c2b328-648e-3d43-85b7-8f21bd61a3ff | -7.45318 | -46.1554 | 2026-08-21 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 405d0bc9-f626-3052-a79e-72b4a0454a86 | -4.12623 | -44.05404 | 2026-08-21 04:00:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d3a6f8a5-3dc7-363c-80aa-11bfe60ea0cc | -3.96006 | -43.10574 | 2026-08-21 04:00:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 43438cbf-aca9-3258-a2ef-de954a494e65 | -6.34568 | -44.08305 | 2026-08-21 04:00:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0c62bd46-9e5d-3b8b-9588-d05a29bf747a | -7.63217 | -45.77281 | 2026-08-21 04:00:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 79e8a777-590a-3389-80d4-8ed0d7b21a20 | -4.00735 | -48.06047 | 2026-08-21 04:00:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e57f8523-c85f-37ee-abd7-37e70c133861 | -3.9744 | -47.20866 | 2026-08-21 04:00:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0a23dc79-c07b-31ec-8875-c2b1f6e82581 | -7.37429 | -45.82011 | 2026-08-21 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 330a51a7-7010-3585-902d-9c7d745c1327 | -6.33055 | -46.52132 | 2026-08-21 04:00:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6b663f14-fe48-3a92-a618-ed14abc188f5 | -6.87556 | -43.7421 | 2026-08-21 04:00:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cf259579-cdc3-3c3f-af9f-1fbb88d89aa7 | -7.36969 | -45.81929 | 2026-08-21 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 69e6e58c-c102-35b5-9e3c-15839b8cb3b3 | -4.00982 | -48.06464 | 2026-08-21 04:00:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5cbaa84c-e344-32ee-8550-675cdda577c7 | -4.09275 | -42.50923 | 2026-08-21 04:00:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 3dcde38f-b4dd-3c4f-9b00-a21d744a72b0 | -6.26967 | -43.2761 | 2026-08-21 04:00:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c23799b7-ea1d-3bc3-97e6-6a86089c4061 | -3.53657 | -48.18536 | 2026-08-21 04:00:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 2cf48bd7-09cb-315e-a692-8a629a76f2c6 | -7.63837 | -45.76411 | 2026-08-21 04:00:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bfdc9e87-8927-3460-8407-c50d02ebd0c7 | -4.04995 | -50.3031 | 2026-08-21 04:00:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 62f96379-c80b-379f-8e99-72549e0d4d45 | -3.53148 | -48.18047 | 2026-08-21 04:00:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| ab6d9bde-4b39-391b-bc9b-d39adae43ce7 | -6.87436 | -43.74923 | 2026-08-21 04:00:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 382459ab-9154-3e3a-9dec-d2cbfc26e96c | -6.86747 | -43.74078 | 2026-08-21 04:00:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 9.8 |
| b1200d1a-d004-33cf-a8bd-33016c0ea310 | -2.7634 | -48.57804 | 2026-08-21 04:00:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b438f15e-6360-3f1d-bd42-94118014098e | -6.87152 | -43.74142 | 2026-08-21 04:00:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 9.8 |
| fddae09b-c3a9-3883-b6ab-48e86762d9a5 | -6.24237 | -43.68467 | 2026-08-21 04:00:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 58e5bafe-677c-3810-a868-95c111e4721c | -7.34668 | -45.81519 | 2026-08-21 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 062f44ed-8327-38c6-b3ef-283fb3f56d42 | -4.09931 | -42.49773 | 2026-08-21 04:00:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| d0eaac10-08f3-383f-9c58-2119af7cbc04 | -3.53792 | -48.17737 | 2026-08-21 04:00:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 477f16ef-e6dc-3904-84a4-fdda10075c47 | -3.26317 | -49.53173 | 2026-08-21 04:00:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b54ca929-8074-35a0-857d-3a9993209edb | -7.35756 | -45.80733 | 2026-08-21 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 32cd0219-6996-3570-8b21-8f6aa16938ab | -7.34752 | -45.81043 | 2026-08-21 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 067ac485-2798-3e72-bb52-c7a954c5ccfe | -3.54301 | -48.18225 | 2026-08-21 04:00:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 157bc377-78de-398e-9a74-a35166a85150 | -4.09353 | -42.50432 | 2026-08-21 04:00:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 74fc962c-4de5-370f-bff8-825967188e13 | -7.14128 | -47.50717 | 2026-08-21 04:00:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7e65423d-22c2-3959-9fcf-3815a5d5d4c2 | -5.78908 | -46.10909 | 2026-08-21 04:00:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a220e502-389e-3a44-b889-b9c10dc42a02 | -3.96353 | -43.10999 | 2026-08-21 04:00:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| a1d85c0f-cbfb-3e7d-b673-2a63ab6cfa85 | -7.35212 | -45.81124 | 2026-08-21 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 31.1 |
| f7a63fa1-5905-3909-8a25-71bff65c68a0 | -7.36676 | -45.80893 | 2026-08-21 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 44.2 |
| c376635e-6e82-38e7-b08e-da570b0c882b | -4.0434 | -50.30219 | 2026-08-21 04:00:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 39cd6ae9-47fb-3285-b522-d01d189232dd | -6.87212 | -43.73787 | 2026-08-21 04:00:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 9.8 |
| d5bba8d8-a617-3fd5-8005-4d1642d47d47 | -7.14216 | -47.50869 | 2026-08-21 04:00:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7d2b9aa7-1132-32a6-a475-fdfba2ad4c9b | -3.95948 | -43.10932 | 2026-08-21 04:00:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 842d0e39-0718-3577-bcd5-9768daf09a48 | -6.87749 | -43.70596 | 2026-08-21 04:00:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b5573916-c060-3f8f-afd7-0748949c2bdb | -4.04441 | -50.29662 | 2026-08-21 04:00:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 88c43b7a-7192-3fce-8238-e98c8c7d44c0 | -2.0483 | -48.03579 | 2026-08-21 04:00:00 | NOAA-20 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1106bd41-bbb1-334d-b81f-b192e2094e70 | -3.5308 | -48.18448 | 2026-08-21 04:00:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 27ebad69-b906-3a0f-9f7d-3ef42780002d | -6.34153 | -44.08225 | 2026-08-21 04:00:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d319c543-f73d-3179-af9b-b719af6aa556 | -7.03595 | -45.89764 | 2026-08-21 04:00:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cc616a2b-a5c1-328d-aa20-e21e9f19c7d1 | -7.63896 | -42.72889 | 2026-08-21 04:00:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 60ab9af3-792f-31d7-8d54-eedbe7f8c088 | -6.86807 | -43.73722 | 2026-08-21 04:00:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 62495874-4827-3b1e-9740-6317dfe29103 | -4.04432 | -50.2995 | 2026-08-21 04:00:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 14ab3f8e-73cb-3c0d-8e2b-50b44edb5fe0 | -2.04247 | -48.03483 | 2026-08-21 04:00:00 | NOAA-20 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3c6e7d1f-4d36-36d5-bb60-f8e5180c8373 | -7.35589 | -45.81681 | 2026-08-21 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 31.1 |
| 80041530-49a2-3f61-b001-8679314b3323 | -8.52003 | -39.34648 | 2026-08-21 04:00:00 | NOAA-20 | CABROBÓ | PERNAMBUCO | Brasil | 2603009 | 26 | 33 | nan | nan | nan | Caatinga | 0.3 |
| b861a86b-1b4a-3d11-89ce-4e4eefe9aa4b | -7.35505 | -45.82158 | 2026-08-21 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 7813f4b7-038f-3f4c-b9f5-dffb548198a5 | -5.60709 | -44.01078 | 2026-08-21 04:00:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 283b82d5-2f25-3fd2-bac8-f468125d0e95 | -4.05095 | -50.29753 | 2026-08-21 04:00:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 4c3ef02e-3892-3ed3-a27a-f10827a7724d | -7.63298 | -45.76811 | 2026-08-21 04:00:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 09ca4e39-809c-3f10-a5ae-e217a4f89c1f | -5.9468 | -44.23424 | 2026-08-21 04:00:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e4feaa72-83da-35c9-a66a-0917ac65660f | -6.33546 | -46.52219 | 2026-08-21 04:00:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c46aec34-5225-327e-88be-40e0c6ede2ca | -7.37219 | -45.80497 | 2026-08-21 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 28.1 |
| 2316f4a1-ebf3-3b6d-8980-8802f683aba8 | -6.33408 | -46.52072 | 2026-08-21 04:00:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3ef0e0ba-456c-35cb-81a2-cce1e2bda1de | -5.6616 | -51.64479 | 2026-08-21 04:00:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 2107c987-bff2-32bc-9a86-910eadf465dd | -6.13562 | -44.91429 | 2026-08-21 04:00:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 78b0dfcb-a545-3bbf-835d-9676778012a1 | -3.54233 | -48.18631 | 2026-08-21 04:00:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 3956effc-2679-37e1-b53d-c729ecea5b31 | -4.09768 | -42.50755 | 2026-08-21 04:00:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 54c40345-682e-390d-9d75-c5844eb160be | -6.86687 | -43.74436 | 2026-08-21 04:00:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dce34b78-4958-3b89-8e71-d48acdcbb22f | -6.57463 | -43.49726 | 2026-08-21 04:00:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9b1200c7-36b5-35c3-9d8f-eb6cab38d944 | -3.53724 | -48.18137 | 2026-08-21 04:00:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 64019301-8b5b-3171-96a4-adc3ce001c62 | -7.63918 | -45.75943 | 2026-08-21 04:00:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2fa32085-6aa4-3784-a18c-14fd640ea621 | -7.64345 | -40.42543 | 2026-08-21 04:00:00 | NOAA-20 | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 0.5 |


[Clique aqui para ver as próximas entradas](README25.md)

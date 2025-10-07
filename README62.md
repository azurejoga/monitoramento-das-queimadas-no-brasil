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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e888cc08-7eb0-306e-9e33-eabd9eb4e03d | -14.9156 | -51.44146 | 2025-10-07 04:38:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 12.8 |
| af43b932-ab83-310b-8636-c570781dec0f | -13.05679 | -47.92472 | 2025-10-07 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8876d3f6-0289-3b1b-85e1-470e971d2929 | -10.55578 | -54.87002 | 2025-10-07 04:38:00 | NPP-375D | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b1c4cba2-1d3c-3c8a-84ea-62958a14747e | -13.58923 | -48.68336 | 2025-10-07 04:38:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d38783e0-16c6-334d-95da-1c1d944daa72 | -11.50327 | -44.9735 | 2025-10-07 04:38:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a0c4d3b8-c472-303b-ae34-72f3b475cb71 | -14.77499 | -46.07016 | 2025-10-07 04:38:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 31.2 |
| c5e5a783-5dc1-37d8-9628-6aee049ae745 | -14.76135 | -46.05877 | 2025-10-07 04:38:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 5f6eaf59-fa1e-363e-86c9-d3e53380a0bd | -16.3467 | -47.04794 | 2025-10-07 04:38:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d3146500-1e99-37ee-bc96-187596cd46a3 | -15.88614 | -46.25563 | 2025-10-07 04:38:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ba520762-a1be-308f-a7db-2973e6fd205d | -15.91357 | -48.82721 | 2025-10-07 04:38:00 | NPP-375D | CORUMBÁ DE GOIÁS | GOIÁS | Brasil | 5205802 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a150bfb8-a7b5-31d0-b62e-0602faaf3035 | -16.13499 | -46.178 | 2025-10-07 04:38:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2cef91f8-a2a1-382b-9a85-85ccc6123a35 | -11.79493 | -45.10564 | 2025-10-07 04:38:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 98d9d9ec-1d62-3153-912e-8bce49f0d56c | -11.22577 | -47.77248 | 2025-10-07 04:38:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| add7bc33-4316-32c2-b4ee-68c153888687 | -13.3953 | -47.60125 | 2025-10-07 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f508b3e7-cae0-3694-8ebb-f971f5bf98a1 | -11.84622 | -44.914 | 2025-10-07 04:38:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5b74acc0-918d-3c8f-be92-2baee401457d | -11.9482 | -46.46057 | 2025-10-07 04:38:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fad86914-1258-3710-a7c1-e7aff3c6821f | -14.92154 | -46.80438 | 2025-10-07 04:38:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d07fb6ff-0a73-3027-9771-2e6be52c5e4d | -11.3849 | -43.49109 | 2025-10-07 04:38:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e2efff25-12ff-3e6e-bd05-f19c1484b6a2 | -11.94961 | -46.44263 | 2025-10-07 04:38:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2aeb25ac-7df3-33c3-9fcf-2059e25721e1 | -11.9513 | -45.48539 | 2025-10-07 04:38:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a702c9cd-9f2c-3fbe-9ac3-5784f480c74f | -11.92407 | -51.53845 | 2025-10-07 04:38:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f34b321b-80cd-380a-bcb1-cabd5d45abd6 | -10.89273 | -53.74906 | 2025-10-07 04:38:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c08ab79a-562d-3b92-bf2f-68d5f5476a9e | -11.03005 | -50.91127 | 2025-10-07 04:38:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1c1d0189-a0aa-3643-9204-5faf76c6f6e2 | -10.43079 | -51.63725 | 2025-10-07 04:38:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 55c09955-fd2b-316a-8508-ae7f597d11e2 | -12.13617 | -50.87238 | 2025-10-07 04:38:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a5760e42-b64e-3e6f-9a9d-037877cd17ea | -16.29054 | -45.2472 | 2025-10-07 04:38:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6e581961-4143-3c35-a02c-da4672f08bf3 | -14.76817 | -46.06448 | 2025-10-07 04:38:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 4d2db277-7cb0-359f-b67d-d12a04651973 | -11.71631 | -44.29852 | 2025-10-07 04:38:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c12dac40-3de2-3618-809e-d478d4a2db39 | -14.62145 | -52.49115 | 2025-10-07 04:38:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| de2e6944-39b6-3d0c-9c5d-a2b3fcfe8da5 | -15.36625 | -47.31963 | 2025-10-07 04:38:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6ff7cea6-aa13-31d3-a263-0509aee1d7d4 | -13.2868 | -48.06152 | 2025-10-07 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 09b1641b-0257-335e-9d6a-ccb3286823b6 | -17.56635 | -46.07243 | 2025-10-07 04:38:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 366c52e0-ca2d-3bdb-a73b-b2b0f7783fc5 | -14.77125 | -46.06963 | 2025-10-07 04:38:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 31.2 |
| 6682b7cd-8615-3822-be39-3e7d88099cb3 | -15.58225 | -47.26765 | 2025-10-07 04:38:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c4c8cbf8-8884-3abb-b802-e1f96f8c98e8 | -14.76573 | -46.05481 | 2025-10-07 04:38:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| e97c49a5-59ab-3e9e-b1ab-1edaacc50ecc | -13.73672 | -48.6521 | 2025-10-07 04:38:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 21e3fbdc-860c-3c0f-8a17-7465254af89c | -13.07203 | -47.89301 | 2025-10-07 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ae02f762-faf1-32ed-a9d3-ec16e46748fd | -10.6193 | -48.65755 | 2025-10-07 04:38:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d6f6c18f-e977-30ac-921e-eb97c3e515bf | -12.41806 | -46.70693 | 2025-10-07 04:38:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ae3eecf8-2f16-3d7c-9b0a-d5c6a15df20a | -17.09224 | -43.38314 | 2025-10-07 04:38:00 | NPP-375D | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| ff306934-a9eb-3f8a-b22d-4b6ae420ffe6 | -12.66271 | -45.03141 | 2025-10-07 04:38:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dfd7beef-0153-3e7b-901b-dca2c60f5e58 | -15.19905 | -56.8205 | 2025-10-07 04:38:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c48e2e6c-09cc-363e-8399-b83f555540ef | -13.26074 | -47.1654 | 2025-10-07 04:38:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0fa014c5-d6db-3e6d-9fc1-14dcab7e2f30 | -13.33122 | -47.17152 | 2025-10-07 04:38:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 800c548e-5f2a-3136-af08-2df2d55789e5 | -12.89826 | -54.74777 | 2025-10-07 04:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 8c05f767-01f4-33d3-8ff3-be094c9f920b | -13.73952 | -48.65626 | 2025-10-07 04:38:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 43978c2f-3c2b-327e-9f0d-0d46d6fc8a5e | -14.92028 | -46.81294 | 2025-10-07 04:38:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fccbee98-bf99-3d0a-a5b7-8560f9595567 | -18.04351 | -43.14927 | 2025-10-07 04:38:00 | NPP-375D | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 4e562fd1-7c87-397b-929e-457dc0e35ce3 | -14.9373 | -46.80233 | 2025-10-07 04:38:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fdb18899-ffe9-3ded-a4e5-6099675b731c | -13.38703 | -47.53989 | 2025-10-07 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 89576cec-1e67-3b56-99b6-c3819df0abc9 | -10.62026 | -49.05735 | 2025-10-07 04:38:00 | NPP-375D | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| abc2dd78-5647-337d-8a66-77f4c550e1ee | -14.64704 | -52.53381 | 2025-10-07 04:38:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 50b5b406-f352-3767-a2b5-043c0d34bd65 | -15.14571 | -45.81263 | 2025-10-07 04:38:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8d74750b-0a8e-3552-aa64-b0a5c6ab58c1 | -10.46013 | -51.244 | 2025-10-07 04:38:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 0437fc22-50f5-37c5-990e-d4fad3618a32 | -13.76224 | -45.73143 | 2025-10-07 04:38:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| f34a5279-f2c3-3ba4-baac-0d1e9bcc2690 | -15.26676 | -48.05758 | 2025-10-07 04:38:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 48541c57-1893-3115-8d87-b0fe0bb80e0c | -14.6339 | -48.32676 | 2025-10-07 04:38:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 49e026ba-044e-38f1-aa51-5f5aba2f16fc | -14.36464 | -47.72607 | 2025-10-07 04:38:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d1ed8f24-a12a-3080-a221-61aa69eb7df8 | -15.27875 | -46.33705 | 2025-10-07 04:38:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 419cc8cc-5a02-3fab-aba9-cf64eb8f2590 | -13.05187 | -48.70854 | 2025-10-07 04:38:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b65defae-81ff-36eb-aa97-2b486eeb2231 | -11.16777 | -47.73798 | 2025-10-07 04:38:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5f951b8e-397f-3f70-b718-538c32250c98 | -17.97664 | -44.99107 | 2025-10-07 04:38:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| acc8984f-2967-3f10-83a2-b8c0bf5789d3 | -12.40996 | -50.2643 | 2025-10-07 04:38:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 38203b12-5acc-35dc-9596-3feabae9b9d7 | -10.39836 | -50.30683 | 2025-10-07 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 1c7911d6-c6f4-32fc-8972-446d285fbe64 | -12.17671 | -47.77372 | 2025-10-07 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f7e2d1c8-9499-3359-b137-49c9ce388642 | -14.7397 | -46.02274 | 2025-10-07 04:38:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 12.5 |
| ad428001-106d-3581-a195-6a49ef8b1b3c | -12.16141 | -51.43734 | 2025-10-07 04:38:00 | NPP-375D | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0d60bdc0-7e5a-35c2-94ef-440a71f4690b | -11.23701 | -47.76684 | 2025-10-07 04:38:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b6ad5fdf-30a1-3afd-aea5-35993f73c108 | -15.0062 | -56.10522 | 2025-10-07 04:38:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 72357455-01c4-3942-9048-0b64dbd6bcb7 | -13.51902 | -48.6173 | 2025-10-07 04:38:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cf8246f5-5564-3f34-9ed1-2bc0308281a0 | -14.90636 | -46.85759 | 2025-10-07 04:38:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dc5ff73e-c5b8-343e-8ab9-60c473e97875 | -12.25551 | -51.34238 | 2025-10-07 04:38:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 61150ba2-af7e-3ffa-8a6a-ac3f0b08f36a | -15.99623 | -50.83498 | 2025-10-07 04:38:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 898dcf64-28f4-3891-ae5d-c47260c96bee | -11.05404 | -50.90675 | 2025-10-07 04:38:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 5040d110-bdd6-3f45-a270-99da521b72c7 | -11.94707 | -46.44395 | 2025-10-07 04:38:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 58cf7f5d-1dde-3b72-a2c3-1d99a763f7cb | -17.563 | -50.44967 | 2025-10-07 04:38:00 | NPP-375D | ACREÚNA | GOIÁS | Brasil | 5200134 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 57caf027-2dbd-3800-b7ad-291faf9a8c50 | -14.92179 | -51.44639 | 2025-10-07 04:38:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 3d3b1e9f-c5b9-3351-b768-17e400d5773e | -11.02734 | -51.15322 | 2025-10-07 04:38:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 563bc456-74a6-38c5-80f6-41eb03a01a88 | -13.09821 | -47.99509 | 2025-10-07 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2c57236c-dc7e-3493-9773-fe0e5d600334 | -15.37037 | -47.31617 | 2025-10-07 04:38:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c0be3436-0b19-31c0-b48f-b9eba1f4f557 | -8.22481 | -61.1786 | 2025-10-07 04:38:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 58b81d7e-57f6-3fe8-b48f-a8922b9b95cb | -11.84545 | -44.91927 | 2025-10-07 04:38:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 31608535-5341-3f59-a7b1-5ea4cc021f4b | -11.71955 | -44.30429 | 2025-10-07 04:38:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4c363dff-1fc6-358b-b647-d87caa8b6872 | -14.91348 | -46.86619 | 2025-10-07 04:38:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 726e6185-4c5c-3f37-85ab-f9510a610e3a | -11.88518 | -44.95722 | 2025-10-07 04:38:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 30cd82ea-ba71-3d20-b261-8f9005af341d | -13.59202 | -48.68751 | 2025-10-07 04:38:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 0035e00d-4bfb-3d27-b0bf-98c8eaaa1645 | -11.25603 | -50.27506 | 2025-10-07 04:38:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4d5fc004-1c23-381e-941d-7b817b751ca7 | -12.17996 | -50.92579 | 2025-10-07 04:38:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9237dc69-c012-346d-bf32-c0d231cf5e84 | -15.9865 | -50.9379 | 2025-10-07 04:38:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| de23a1e8-97a8-38df-8f5c-715105652823 | -13.71185 | -48.08518 | 2025-10-07 04:38:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fc262488-f0e0-3852-bd5d-c8b69601bd83 | -18.28012 | -45.45804 | 2025-10-07 04:38:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 28ab7a67-9101-3703-990f-1fb75a6b4bff | -10.09393 | -50.5234 | 2025-10-07 04:38:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7f9f065a-eb18-30fb-8c32-6461b7311a02 | -15.39227 | -48.00201 | 2025-10-07 04:38:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a20a4b40-8ede-3371-a012-ff662790f891 | -15.96103 | -50.84019 | 2025-10-07 04:38:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| da2334ce-3eb2-340a-ad12-c34228e15b44 | -11.2944 | -48.27212 | 2025-10-07 04:38:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 696ad2cb-5ea8-3a09-ad4c-2f2e52e8aaad | -14.92657 | -46.80004 | 2025-10-07 04:38:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ff1f72be-e12d-3570-9aac-242a16c8ad37 | -11.84454 | -44.91146 | 2025-10-07 04:38:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8508f74d-56a3-3af1-b976-2530f14d981f | -13.23682 | -47.24581 | 2025-10-07 04:38:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 22dba75b-e223-3614-b1f6-3d8f0bff298f | -10.4277 | -50.31924 | 2025-10-07 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 93647a42-e063-33e8-8a24-fe4e6e952556 | -11.15152 | -47.75372 | 2025-10-07 04:38:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README63.md)
